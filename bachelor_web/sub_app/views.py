from django.shortcuts import render
from django.contrib import messages

import threading

from .Functions import gan_generate
from .Functions.rnn_generate import RNN_generator
from .forms import *


def index(request):
    """
    A start view
    """
    form = TaskForm()
    context = {'form': form}
    return render(request, 'index.html', context)


def generate(request):
    """
    A view, which run background process to generate text using selected model
    """
    form = TaskForm()
    context = {'form': form}

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            tmp = form.cleaned_data['select_model']
            if tmp == 'rnn':
                t = threading.Thread(target=generate_using_rnn, args=[request, form.cleaned_data['first_word']])
                t.setDaemon(True)
                t.start()
                t.join()
            elif tmp == 'gan':
                t = threading.Thread(target=generate_using_gan, args=[request])
                t.setDaemon(True)
                t.start()
                t.join()
            context = {'form': form, 'select_model': tmp, 'first_word': form.cleaned_data['first_word']}
    return render(request, 'index.html', context)


def generate_using_rnn(request, first_word):
    """
    Method which run RNN generating algorithm
    """
    rnn = RNN_generator(first_word)
    result = rnn.run()
    messages.info(request, result)


def generate_using_gan(request):
    """
     Method which GAN generating algorithm
    """
    result = gan_generate.run()
    messages.info(request, result)
