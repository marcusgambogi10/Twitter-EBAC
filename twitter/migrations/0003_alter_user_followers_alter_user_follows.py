# Generated by Django 4.2.3 on 2024-03-18 22:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("twitter", "0002_alter_user_followers_alter_user_follows"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="followers",
            field=models.ManyToManyField(related_name="followed_by", to="twitter.user"),
        ),
        migrations.AlterField(
            model_name="user",
            name="follows",
            field=models.ManyToManyField(related_name="following", to="twitter.user"),
        ),
    ]