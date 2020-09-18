from django.urls import path

from . import views

app_name = 'bookstore'
urlpatterns = [
    path('', views.home, name='home'),
    path('account', views.AccountView.as_view(), name='account'),
    path('admin/', views.BookstoreAdminView.as_view(), name='admin'),
    path('stats', views.StatisticsView.as_view(), name='stats'),
    path('cart', views.CartView.as_view(), name='cart'),
    path('cart/order', views.OrderView.as_view(), name='order'),
    path('home', views.home, name='home'),
    path('login', views.LoginFormView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('register', views.RegistrationFormView.as_view(), name='register'),
    path('book/<slug:bid>/review-filter-newest/<int:rnum>', views.review_filter_newest, name = 'review_filter_newest'),
    path('book/<slug:bid>/review-filter-best/<int:rnum>', views.review_filter_best, name = 'review_filter_best'),
 	path('book/<slug:bid>/add-to-cart', views.add_to_cart, name = 'add_to_cart'),
 	path('book/<slug:bid>/review', views.review, name = 'review'),
    path('book/<slug:bid>/review/rate/<int:rid>', views.rate_user_review, name = 'rate_user_review'),
    
    path('book/<slug:bid>', views.book_details, name = 'book_details'),
    path('search/', views.search, name='search'),
    path('search/filter-author', views.search_filter_author, name='search_filter_author'),
    path('search/filter-year', views.search_filter_year, name='search_filter_year'),
    path('search/filter-score', views.search_filter_score, name='search_filter_score'),
    path('keyword/<slug:key>/<path:specified>', views.search_specific, name='search_specific'),
]
