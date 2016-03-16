from django.template import RequestContext
from .models import Photo, Category
from .forms import CategorySelectionForm
from django.shortcuts import render_to_response
from django.db.models import Q

def index(request):

    """
    All photos, with most recent first.
    """

    photo_list = Photo.objects.order_by('-photo_date')

    return render_to_response("photosite/index.html", { 
            "category_list": CategorySelectionForm(), 
            "photo_list": photo_list,
            })

def cat_filter(request):

    """
    Filter the photos by category.
    'All categories' has a category_id of ''.
    """

    category_id = request.GET.get('category_list')
    if category_id == '':
    	photo_list = Photo.objects.order_by('-photo_date')
    else:
        photo_list = Photo.objects.order_by('-photo_date')
        photo_list = photo_list.filter(category=category_id)

    # make sure the selected category is shown
    category_list = CategorySelectionForm(request.GET)	

    return render_to_response("photosite/index.html", { 
            "category_list": category_list, 
            "photo_list": photo_list,
            })

def photo_search(request):

    """
    Search for photos with the specified text in the title or description.
    The search is not case-sensitive.
    """

    photo_search = request.GET.get('search_term')

    photo_list = Photo.objects.filter(Q(photo_title__icontains=photo_search) | 
                               Q(photo_description__icontains=photo_search))
    photo_list = photo_list.order_by('-photo_date')

    return render_to_response("photosite/index.html", {
            "searched_for": photo_search, 
            "category_list": CategorySelectionForm(), 
            "photo_list": photo_list,
            })