from django.db import models

STATUS_CHOICES = [
        ('new', 'New'),
        ('in_process', 'In process'),
        ('done', 'Done')
    ]


class Things(models.Model):
    status = models.CharField(max_length=40, choices=STATUS_CHOICES, default='new')
    description = models.TextField(null=False, blank=False)
    description_more = models.TextField(null=True, blank=True)
    date_of_completion = models.DateField(null=True, blank=True, default=None)

    def __str__(self):
        return self.description
