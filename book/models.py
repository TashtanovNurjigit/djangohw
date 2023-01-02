from django.db import models


class Book(models.Model):
    GENRE = (
        ('Detective', 'Detective'),
        ('Horror', 'Horror'),
        ('Fantasy', 'Fantasy'),
        ('Comedy', 'Comedy'),
        ('Fiction', 'Fiction'),
        ('Thrillers', 'Thrillers'),
        ('Adventures', 'Adventures')

    )
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=100, choices=GENRE, null=True)
    author = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title


class CommentTvShow(models.Model):
    choice_show = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comment_object')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)


class Expert(models.Model):
    ACTIVITY = (
        ('Writer', 'Писатель'),
        ('Publicist', 'Publicist'),
        ('Teacher', 'Teacher'),
        ('Student', 'Student')
    )
    name = models.CharField(max_length=100)
    info = models.TextField()
    activity = models.CharField(max_length=100, choices=ACTIVITY)

    def __str__(self):
        return self.name


class ExpertRecommendation(models.Model):
    choice_show = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='expert_recommendation')
    name_expert = models.ForeignKey(Expert, on_delete=models.CASCADE)
    recommendation = models.TextField()

    def __str__(self):
        return self.name_expert
