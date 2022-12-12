from django.shortcuts import render
from django.views.generic import (
    CreateView
)
from django.views.generic.edit import (
    FormView
)
from rest_framework.generics import ListAPIView
from .forms import UserRegisterForm
from .models import User
from .serializers import UserSerializer



class UserRegisterView( FormView ):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url= '/'

    def form_valid( self, form ):

        User.objects.create_user(
            username  = form.cleaned_data[ 'username' ],
            email     = form.cleaned_data[ 'email' ],
            password  = form.cleaned_data[ 'password1' ],
            firstname = form.cleaned_data[ 'firstname' ],
            lastname  = form.cleaned_data[ 'lastname' ],
            gender    = form.cleaned_data[ 'gender' ]
        )

        return super().form_valid( form )



class UserListApiView( ListAPIView ):
    
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()


