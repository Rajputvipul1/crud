from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    cover_image = models.ImageField(upload_to='book_covers/', null=True, blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        """
        Override the delete method to also delete the associated image file when a book record is deleted.
        """
        if self.cover_image:
            # Remove the file from the storage
            storage, path = self.cover_image.storage, self.cover_image.path
            storage.delete(path)
        super().delete(*args, **kwargs)
