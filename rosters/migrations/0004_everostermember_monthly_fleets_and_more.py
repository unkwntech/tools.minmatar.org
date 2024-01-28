# Generated by Django 4.1.5 on 2024-01-24 21:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rosters", "0003_alter_everoster_alliance_id_alter_everoster_ceo_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="everostermember",
            name="monthly_fleets",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="everostermember",
            name="quarterly_fleets",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="everostermember",
            name="quarterly_kills",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]