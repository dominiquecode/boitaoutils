from django.shortcuts import render
# from easygui import diropenbox


# Create your views here.
def home(request):

    if request.method == 'POST':
        source = request.POST.get('source')
        destination = request.POST.get('destination')

        # if destination is None:
        #     source = diropenbox()

        context = {'source': source,
                   'destination': destination, }
    else:
        context = {'source': "",
                   'destination': ""}

    return render(request, 'photos_home.html', context)
