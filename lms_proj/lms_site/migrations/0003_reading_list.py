# Generated by Django 4.2.3 on 2023-08-01 08:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lms_site', '0002_alter_lms_users_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reading_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_shelf', models.CharField(choices=[('read', 'Read'), ('want_to_read', 'Want_To_Read'), ('currently_reading', 'Currently_Reading')], default='want_to_read', max_length=20)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lms_site.books')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
