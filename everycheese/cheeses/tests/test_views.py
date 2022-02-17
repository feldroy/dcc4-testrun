import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains

from ..models import Cheese
from ..views import CheeseDetailView, CheeseListView
from .factories import CheeseFactory


def test_good_cheese_list_view_expanded(rf):
    # Determine the URL 
    url = reverse("cheeses:list")
    # rf is pytest shortcut to django.test.RequestFactory
    # We generate a request as if from a user accessing
    #   the cheese list view
    request = rf.get(url)
    # Call as_view() to make a callable object
    # callable_obj is analogous to a function-based view
    callable_obj = CheeseListView.as_view()
    # Pass in the request into the callable_obj to get an 
    #   HTTP response served up by Django
    response = callable_obj(request)
    # Test that the HTTP response has 'Cheese List' in the
    #   HTML and has a 200 response code
    assertContains(response, 'Cheese List')

pytestmark = pytest.mark.django_db
