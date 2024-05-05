# Generated by Django 4.2.11 on 2024-05-05 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_hashtag_post_hashtags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='hashtags',
            field=models.ManyToManyField(blank=True, related_name='hash_post', to='posts.hashtag'),
        ),
    ]
