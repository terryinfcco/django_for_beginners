# pages/urls.py
from django.urls import path
# import a GCBV
from .views import homePageView

urlpatterns = [
	# empty string is because this is the root page of the website
	# homePageView is the GCBV that we're using
	# optional named URL pattern called home
	path("", homePageView, name="home"),
]