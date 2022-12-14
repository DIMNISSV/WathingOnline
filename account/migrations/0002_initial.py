# Generated by Django 4.1.3 on 2022-11-11 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('account', '0001_initial'),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favorite_categories',
            field=models.ManyToManyField(blank=True, to='post.category'),
        ),
        migrations.AddField(
            model_name='user',
            name='favorite_genres',
            field=models.ManyToManyField(blank=True, to='post.genre'),
        ),
        migrations.AddField(
            model_name='user',
            name='favorite_posts',
            field=models.ManyToManyField(blank=True, to='post.post'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='subscribe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.subscribe', verbose_name='Подписка'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
