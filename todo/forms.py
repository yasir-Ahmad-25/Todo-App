from django import forms
from .models import Tasks
class TodoForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title' , 'description' , 'due_date']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'})
        }

    def save(self, commit=True):
        # Check if the user is set; if not, raise an error.
        if not self.user:
            raise ValueError("User must be set before saving the task.")
        
        # Set the user to the task instance
        self.instance.user = self.user
        
        # Save the task instance with the associated user
        return super().save(commit=commit)