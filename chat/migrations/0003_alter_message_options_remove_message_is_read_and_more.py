# Generated by Django 4.1.3 on 2022-11-06 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0002_message_remove_messages_room_remove_messages_user_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ('-timestamp',)},
        ),
        migrations.RemoveField(
            model_name='message',
            name='is_read',
        ),
        migrations.RemoveField(
            model_name='message',
            name='message',
        ),
        migrations.RemoveField(
            model_name='message',
            name='receiver',
        ),
        migrations.AddField(
            model_name='message',
            name='attachment',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='message',
            name='text',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='message_sender', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('initiator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='convo_starter', to=settings.AUTH_USER_MODEL)),
                ('receiver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='convo_participant', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='conversation_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='chat.conversation'),
        ),
    ]
