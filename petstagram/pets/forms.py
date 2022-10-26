from django import forms

from petstagram.pets.models import Pet


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'personal_photo', 'date_of_birth']
        widgets = {
            'name':forms.TextInput(attrs={'placeholder': "Pet name"}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'personal_photo': forms.TextInput(attrs={'placeholder': 'Link to image'}),
        }
        labels = {
            'name': "Pet Name",
            'date_of_birth': "Date of Birth",
            'personal_photo': 'Link to Image'
        }


class PetDeleteForm(PetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _,field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
            # field.widget.attrs['disabled'] = 'disabled'

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance