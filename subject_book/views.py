from django.http import FileResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe, require_POST
from os.path import join as join_path
from django.conf import settings
from django.http import HttpResponse, Http404
from os.path import exists as path_exists
# Create your views here.
from reportlab.pdfgen import canvas

from project_subject1.settings import MEDIA_ROOT
from subject_book.forms import ModelBasedSubjectForm
from subject_book.models import Subject, Book, Uploads
from os.path import basename as file_basename
from subject_book.utils import uploads_url, gen_uuid


@require_safe
def subject_list(request):
    subjects = Subject.objects.all()

    return render(request, 'subject_list.html', {'subjects': subjects})


@require_POST
def create_subject(request):
    name = request.POST['name']
    subject = Subject(name=name, created_by=request.user)
    subject.save()
    return redirect('subject:list')


def create_subject_page(request):
    return render(request, 'create_subject.html', {})


def get(request, pk):
    subject = Subject.objects.get(pk=pk)
    return render(request, 'detail.html', {'subject': subject})


def delete_page_subject(request, pk):
    subject = Subject.objects.get(pk=pk)
    return render(request, 'delete_subject.html', {'subject': subject})


@require_POST
def delete_subject(request, pk):
    subject = Subject.objects.get(pk=pk)
    subject.delete()
    return redirect('subject:list')


def delete_page_book(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'delete_book.html', {'book': book})


def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('subject:list')


@require_POST
def create_book(request, pk):
    subject = Subject.objects.get(pk=pk)
    name = request.POST['name']
    author = request.POST['author']
    file = request.FILES['file']
    write_file(file)
    book = Book(name=name, author=author, file=file, subject_id=pk, generated_name=uploads_url(file.name))
    book.save()
    return redirect('subject:get', pk=pk)


def create_book_page(request, pk):
    subject = Subject.objects.get(pk=pk)
    return render(request, 'create_book.html', {'subject': subject})


@require_safe
def update_subject_page(request, pk):
    subject = Subject.objects.get(pk=pk)
    form = ModelBasedSubjectForm(instance=subject)
    return render(request, 'update_subject.html', {'form': form})


@require_POST
def update_subject(request):
    form = ModelBasedSubjectForm(request.POST)
    id = int(request.POST['id'])
    if form.is_valid():
        subject = form.save(commit=False)
        subject.id = id
        subject.created_by = request.user
        subject.save()
        return redirect('subject:list')
    return redirect("")


@require_safe
def download(request, generated_name):
    file = Uploads.objects.filter(generated_name=generated_name).first()
    path = join_path(MEDIA_ROOT, 'uploads', file.generated_name)
    if path_exists(path):
        with open(path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type=file.content_type)
            response['Content-Disposition'] = 'inline; filename=' + file_basename(path)
        return response
    raise Http404


def write_file(f) -> None:
    new_name = uploads_url(f.name)
    for chunk in f.chunks():
        with open(join_path(MEDIA_ROOT, 'uploads', new_name), mode="wb+") as file:
            file.write(chunk)

    file = Uploads(
        media_url=f'media/uploads/{new_name}',
        original_name=f.name,
        content_type=f.content_type,
        size=f.size,
        generated_name=new_name,
        code=gen_uuid()
    )
    file.save()
