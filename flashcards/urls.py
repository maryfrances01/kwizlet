# from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r"^$", views.flashcards, name="flashcards"),
    re_path(r"create/", views.create_card_set, name="create_card_set"),
    re_path(
        r"create_card/(?P<card_set_id>[\d]+)", views.create_card, name="create_card"
    ),
    re_path(
        r"delete/(?P<card_set_id>[\d]+)", views.delete_card_set, name="delete_card_set"
    ),
    re_path(r"delete_card/(?P<card_id>[\d]+)", views.delete_card, name="delete_card"),
    re_path(r"edit/(?P<card_set_id>[\d]+)", views.edit_card_set, name="edit_card_set"),
    re_path(r"edit_card/(?P<card_id>[\d]+)", views.edit_card, name="edit_card"),
    re_path(r"view/(?P<card_set_id>[\d]+)", views.view_card_set, name="view_card_set"),
]
