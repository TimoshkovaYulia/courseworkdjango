# Generated by Django 5.2.dev20241205110412 on 2024-12-05 12:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_rename_profile_acount_profileaccount'),
    ]

    operations = [
        migrations.CreateModel(
            name='commentAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_body', models.CharField(max_length=256)),
                ('comment_date', models.DateField(auto_now_add=True)),
                ('comment_time', models.TimeField(auto_now_add=True)),
                ('comment_liked_by', models.ManyToManyField(related_name='liked_comments', to='polls.profileaccount')),
                ('id_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.answer')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.profileaccount')),
            ],
        ),
    ]