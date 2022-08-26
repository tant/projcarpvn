from django.urls import path
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('',views.home, name="home"),

    path('ajax/ajax-load-more-2.html', TemplateView.as_view(template_name='ajax-load-more-2.html'), name="loadmore2"),
    path('ajax/ajax-load-more-3.html', TemplateView.as_view(template_name='ajax-load-more-3.html'), name="loadmore3"),
    path('ajax/ajax-services-customapp.html', TemplateView.as_view(template_name='ajax-services-customapp.html'), name="servicecustomapp"),
    path('ajax/ajax-services-outsource.html', TemplateView.as_view(template_name='ajax-services-outsource.html'), name="servicedoutsource"),
    path('ajax/ajax-team-detail.html', TemplateView.as_view(template_name='ajax-team-detail.html'), name="teamdetail"),
    path('ajax/blog-ajax-load-more-2.html', TemplateView.as_view(template_name='blog-ajax-load-more-2.html'), name="blogloadmore2"),
    path('ajax/blog-ajax-load-more-3.html', TemplateView.as_view(template_name='blog-ajax-load-more-3.html'), name="blogloadmore3"),
    
]