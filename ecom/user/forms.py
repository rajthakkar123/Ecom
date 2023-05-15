from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import CustomUser,Address



class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	class Meta:
		model = CustomUser
		fields = ("email", "first_name","last_name","password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		print("in new user form")
		if commit:
			user.save()
		return user



class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['Flat_number_society','landmark','area','city','pincode']
        