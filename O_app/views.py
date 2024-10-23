from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Stanza
def set_rns():
    stanzes = Stanza.objects.all()
    for i in stanzes:
        if i.stanza_nr % 2:
            if i.stanza_rn == None:
                i.stanza_rn = to_roman((i.stanza_nr+1)/2)
                i.save()


def pages(request, efp=3):
    set_rns()
    stanses = Stanza.objects.all().order_by('stanza_nr')
    # pages = paginator.num_pages()
    page_number = request.GET.get('page')
    efp = request.GET.get('efp')
    if efp == None:
        efp = 2
    print('efp =', efp)
    paginator = Paginator(stanses,efp)
    page_obj = paginator.get_page(page_number)
    return render(request,'stanzes.html',{'page_obj':page_obj, 'efp':efp})
    # return render(request,'stanzes.html',{'page_obj':page_obj})



roman_numbers = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
                 'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
                 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
def to_roman(number):
    roman = ''
    for letter, value in roman_numbers.items():
        while number >= value:
            roman += letter
            number -= value
    return roman