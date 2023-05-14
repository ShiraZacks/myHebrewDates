# Generated by Django 4.1.9 on 2023-05-14 13:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hebcal", "0002_alter_hebrewdate_day_alter_hebrewdate_month"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hebrewdate",
            name="event_type",
            field=models.CharField(
                choices=[("🎂", "birthday"), ("💍", "anniversary"), ("🕯️", "yartzeit")], max_length=20
            ),
        ),
    ]
