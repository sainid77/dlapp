from django import forms


class FileUploadForm(forms.Form):
    file = forms.FileField(
        widget=forms.ClearableFileInput(
            attrs={
                'multiple': True,
            }
        )
    )

    class Meta:
        verbose_name = 'File upload form'
