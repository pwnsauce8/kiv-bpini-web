from django.db import models


NN_CHOICES = (
    ('rnn', 'RNN - Recurrent neural network'),
    ('gan', 'GAN - Generative Adversarial Network'),
)

GENRE_CHOICES = (
    ('comedy', 'Comedy'),
    ('horror', 'Horror'),
    ('thriller', 'Thriller'),
    ('documentary', 'Documentary'),
    ('drama', 'Drama'),
    ('history', 'History'),
    ('mystery', 'Mystery'),
    ('animation', 'Animation'),
    ('adventure', 'Adventure'),
    ('family', 'Family'),
    ('fantasy', 'Fantasy'),
    ('romance', 'Romance'),
    ('action', 'Action'),
    ('crime', 'Crime'),
    ('short', 'Short'),
    ('sci-fi', 'Sci-Fi'),
    ('war', 'War'),
    ('biography', 'Biography'),
    ('film-noir', 'Film-Noir'),
    ('music', 'Music'),
    ('western', 'Western'),
    ('talk-show', 'Talk-Show'),
    ('sport', 'Sport'),
    ('musical', 'Musical'),
    ('news', 'News'),
    ('reality-tv', 'Reality-TV'),
    ('game-show', 'Game-Show'),
)


class Subtitle(models.Model):
    select_model = models.CharField(max_length=100, choices=NN_CHOICES)
    first_word = models.CharField(max_length=200, null=True, blank=True)
    select_genre = models.CharField(max_length=100, choices=GENRE_CHOICES, default='', blank=True)
    end = models.BooleanField(default=True)

    def __str__(self):
        return self.first_word
