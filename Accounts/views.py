from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.


def profile(request):
    return render(request,'accounts/profile.html')





@login_required
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important for security

            return redirect('password_change_done')
        else:
            print(form.non_field_errors) 
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/profile.html', {'form': form})