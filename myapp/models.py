from django.db import models


class CustomUser(models.Model):
    fam = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    otc = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.fam} {self.name}"


class Coords(models.Model):
    id = models.AutoField(primary_key=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    pereval = models.ForeignKey('PerevalAdded', on_delete=models.CASCADE)
    data = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255)


class PerevalAdded(models.Model):
    id = models.AutoField(primary_key=True)
    beautyTitle = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    other_titles = models.CharField(max_length=255)
    connect = models.TextField(blank=True)
    add_time = models.DateTimeField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    coords = models.ForeignKey(Coords, on_delete=models.CASCADE)
    winter_level = models.CharField(max_length=255, blank=True)
    summer_level = models.CharField(max_length=255, blank=True)
    autumn_level = models.CharField(max_length=255, blank=True)
    spring_level = models.CharField(max_length=255, blank=True)
    images = models.ManyToManyField(Image, related_name='perevals')
    status = models.CharField(
        max_length=255,
        choices=(
            ('new', 'New'),
            ('pending', 'Pending'),
            ('accepted', 'Accepted'),
            ('rejected', 'Rejected')
        )
    )

    class Meta:
        db_table = 'pereval_added'


class SprActivitiesTypes(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()

    class Meta:
        db_table = 'spr_activities_types'


