# Generated by Django 4.2.5 on 2024-11-05 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Joke',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Any', 'Any'), ('Programming', 'Programming'), ('Misc', 'Miscellaneous'), ('Dark', 'Dark'), ('Pun', 'Pun'), ('Spooky', 'Spooky'), ('Christmas', 'Christmas')], max_length=50)),
                ('type', models.CharField(max_length=10)),
                ('joke', models.TextField(blank=True, null=True)),
                ('setup', models.TextField(blank=True, null=True)),
                ('delivery', models.TextField(blank=True, null=True)),
                ('nsfw', models.BooleanField(default=False)),
                ('political', models.BooleanField(default=False)),
                ('sexist', models.BooleanField(default=False)),
                ('safe', models.BooleanField(default=True)),
                ('lang', models.CharField(max_length=10)),
            ],
        ),
    ]
