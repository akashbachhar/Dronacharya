# Generated by Django 3.2.6 on 2021-08-29 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0003_alter_subject_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('serial', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True)),
                ('meeting_link', models.CharField(max_length=200)),
                ('time', models.DateTimeField(blank=True, null=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.subject')),
            ],
        ),
    ]
