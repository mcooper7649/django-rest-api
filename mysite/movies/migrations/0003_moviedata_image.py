# Generated by Django 4.0.5 on 2024-07-13 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_moviedata_typ'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='image',
            field=models.ImageField(default='Images/None/NoImg.jpg', upload_to='Images/'),
        ),
    ]
