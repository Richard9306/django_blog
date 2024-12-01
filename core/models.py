from django.core.validators import FileExtensionValidator
from django.db import models
from django.core.exceptions import ValidationError
from PIL import Image


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


def custom_upload_to(instance, filename):
    import uuid
    ext = filename.split('.')[-1]
    new_filename = f"{instance.pk}_{uuid.uuid4()}.{ext}"
    return f"user_{instance.pk}/{new_filename}"

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")
    image = models.ImageField(
        upload_to=custom_upload_to,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
        blank=True
    )

    def clean(self):
        if self.image:
            try:
                with Image.open(self.image) as img:
                    width, height = img.size
                    max_width = max_height = 500
                    if width > max_width or height > max_height:
                        raise ValidationError(f"Image dimensions should not exceed {max_width}x{max_height} pixels.")
            except (IOError, SyntaxError) as e:
                raise ValidationError("Uploaded file is not a valid image.")




    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} on '{self.post}'"