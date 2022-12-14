# Generated by Django 4.1.3 on 2022-11-06 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_slug_post_timestamp_post_updated'),
        ('reply', '0002_rename_reply_reply_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply', to='posts.post'),
        ),
    ]
