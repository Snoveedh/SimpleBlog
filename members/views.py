from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm , PasswordChangeForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import ProfilePageForm, SignupForm , EditProfileForm, PasswordChangingForm
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView
from mysimpleblog.models import Profile



class UserRegisterView(generic.CreateView):
    # form_class = UserCreationForm
    form_class = SignupForm     # Here Using the sign up form after adding some fields to the register form
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    # form_class = UserchangeForm
    form_class = EditProfileForm     # Here Using the sign up form after adding some fields to the register form
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user



#Creating our own views file for password change. Bcz the django inbuilt html pages are loading and the paaterns are different with our nav bar, so this is the reason we are going to create our own view in our format.

class PasswordsChangeView(PasswordChangeView):
    # form_class = PasswordChangeForm
    form_class = PasswordChangingForm
    # success_url = reverse_lazy('home')
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, 'registration/password_success.html', {})



class ShowProfilePage(DetailView):
    model = Profile
    template_name='registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePage, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id= self.kwargs['pk'])
        context["page_user"] = page_user
        return context



class EditProfilePage(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'profile_pic', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url', 'pinterest_url']
    success_url = reverse_lazy('home')

class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_user_profile_page.html'
    # fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
