# Generated by Django 4.0.5 on 2022-06-18 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_name', to='blog.post'),
        ),
    ]
