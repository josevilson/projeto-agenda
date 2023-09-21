from django.http import Http404
from django.shortcuts import get_object_or_404, render

from contact.models import Contact

# Create your views here.


def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')[0:10]

    context = {
        'contacts': contacts,
    }

    return render(
        request,
        'contact/index.html',
        context

    )


def contact(request, id_contact):
    # single_contact = Contact.objects.filter(pk=id_contact).first()
    single_contact = get_object_or_404(Contact, pk=id_contact, show=True)

    if single_contact is None:
        raise Http404()

    context = {
        'contact': single_contact,
    }

    return render(
        request,
        'contact/contact.html',
        context

    )
