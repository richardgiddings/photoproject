from django.test import TransactionTestCase
from django.core.urlresolvers import reverse
from .models import Photo, Category
from django.core.files import File
from django.utils import timezone


def create_category(category_title):
    """
    Create an instance of a Category model
    """
    return Category.objects.create(category_title=category_title)

def create_photo(photo_title, photo_description, filename):
    """
    Create an instance of a Photo model
    """
    return Photo.objects.create(photo_title=photo_title,
                                photo_description=photo_description,
                                photo_date=timezone.now(),
                                photo_full = 
    File(open("/Users/richardgiddings/django/code/photoproject/photosite/tmp/"+filename, 'rb')))

class PhotoViewTests(TransactionTestCase):

    reset_sequences = True

    def test_index_view_with_no_photos(self):
        """
        If no photos exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('photosite:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No photos match the chosen criteria.")
        self.assertQuerysetEqual(response.context['photo_list'], [])

    def test_index_view_with_photo_and_categories(self):
        """
    	Test a photo with categories assigned to it
        """
        category1 = create_category("Category 1")
        category2 = create_category("Category 2")
        photo = create_photo("Title", "Description", "test1.jpg")
        photo.category.add(category1)
        photo.category.add(category2)
        photo.save

        response = self.client.get(reverse('photosite:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['photo_list'],['<Photo: Title>'])

    def test_index_view_with_two_photos_and_categories(self):
        """
        Test photos with categories assigned to them
        """
        category1 = create_category("Category 1")
        category2 = create_category("Category 2")
        photo1 = create_photo("Title 1", "Description 1", "test1.jpg")
        photo2 = create_photo("Title 2", "Description 2", "test2.jpg")
        photo1.category.add(category1)
        photo2.category.add(category2)
        photo1.save
        photo2.save

        response = self.client.get(reverse('photosite:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['photo_list'],['<Photo: Title 2>', '<Photo: Title 1>'])

    def test_cat_filter_all_categories(self):
        """
        Test the filter category with a blank filter (all categories)
        """
        category1 = create_category("Category 1")
        category2 = create_category("Category 2")
        photo1 = create_photo("Title 1", "Description 1", "test1.jpg")
        photo2 = create_photo("Title 2", "Description 2", "test2.jpg")
        photo1.category.add(category1)
        photo2.category.add(category2)
        photo1.save
        photo2.save

        response = self.client.get(reverse('photosite:cat_filter'), {'category_list': ''})
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['photo_list'],['<Photo: Title 2>', '<Photo: Title 1>'])        

    def test_cat_filter_with_a_filter(self):
        """
        Test a category filter that narrows down the results
        """
        category1 = create_category("Category 1")
        category2 = create_category("Category 2")
        photo1 = create_photo("Title 1", "Description One", "test1.jpg")
        photo2 = create_photo("Title 2", "Description Two", "test2.jpg")
        photo3 = create_photo("Title 3", "Description One", "test3.jpg")
        photo1.category.add(category1)
        photo2.category.add(category2)
        photo3.category.add(category2)
        photo1.save
        photo2.save
        photo3.save

        response = self.client.get(reverse('photosite:cat_filter'), {'category_list': '2'})
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['photo_list'],['<Photo: Title 3>', '<Photo: Title 2>'])     

    def test_photo_search_no_results(self):
        """
        Test a photo search with valid characters that returns no results.
        """        
        category = create_category("Category")
        photo = create_photo("Title", "Description", "test1.jpg")
        photo.category.add(category)
        photo.save

        response = self.client.get(reverse('photosite:photo_search'), {'search_term': 'Wrong Title'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No photos match the chosen criteria.")

    def test_photo_search_with_no_characters(self):
        """
        Test a photo search where no characters have been specified.
        This should show all the photos. 
        """
        category1 = create_category("Category 1")
        category2 = create_category("Category 2")
        photo1 = create_photo("Title 1", "Description 1", "test1.jpg")
        photo2 = create_photo("Title 2", "Description 2", "test2.jpg")
        photo1.category.add(category1)
        photo2.category.add(category2)
        photo1.save
        photo2.save

        response = self.client.get(reverse('photosite:photo_search'), {'search_term': ''})
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['photo_list'],['<Photo: Title 2>', '<Photo: Title 1>'])

    def test_photo_search_with_valid_characters_with_results(self):
        """
        Test a photo search with valid characters that returns results.
        """
        category1 = create_category("Category 1")
        category2 = create_category("Category 2")
        photo1 = create_photo("Title 1", "Description One", "test1.jpg")
        photo2 = create_photo("Title 2", "Description Two", "test2.jpg")
        photo3 = create_photo("Title 3", "Description One", "test3.jpg")
        photo1.category.add(category1)
        photo2.category.add(category2)
        photo3.category.add(category2)
        photo1.save
        photo2.save
        photo3.save

        response = self.client.get(reverse('photosite:photo_search'), {'search_term': 'NE'})
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['photo_list'],['<Photo: Title 3>', '<Photo: Title 1>'])