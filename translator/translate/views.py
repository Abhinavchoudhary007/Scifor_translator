from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TranslationForm
from .models import TranslationHistory
from deep_translator import GoogleTranslator

def home_view(request):
    return render(request, 'translate/home.html')

def translate_view(request):
    translation = None  # Initialize translation variable
    history = TranslationHistory.objects.all()  # Retrieve translation history
    if request.method == 'POST':
        form = TranslationForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            language = form.cleaned_data['language']
            translated_text = GoogleTranslator(source='auto', target=language).translate(text)

            # Save the translation to history
            TranslationHistory.objects.create(original_text=text, translated_text=translated_text, language=language)

            translation = translated_text  # Store the translation result

    else:
        form = TranslationForm()

    return render(request, 'translate/translate.html', {'form': form, 'translation': translation, 'history': history})

def delete_translation(request, translation_id):
    TranslationHistory.objects.filter(id=translation_id).delete()  # Delete the translation entry
    return redirect('translate')  # Redirect back to the translate page
