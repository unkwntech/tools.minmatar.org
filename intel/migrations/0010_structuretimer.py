# Generated by Django 4.1.5 on 2024-01-17 18:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("intel", "0009_alter_structureintel_unique_together"),
    ]

    operations = [
        migrations.CreateModel(
            name="StructureTimer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("structure_name", models.CharField(max_length=255)),
                (
                    "structure_type",
                    models.CharField(
                        choices=[
                            ("astrahus", "Astrahus"),
                            ("fortizar", "Fortizar"),
                            ("keepstar", "Keepstar"),
                            ("raitaru", "Raitaru"),
                            ("azbel", "Azbel"),
                            ("sotiyo", "Sotiyo"),
                            ("athanor", "Athanor"),
                            ("tatara", "Tatara"),
                        ],
                        max_length=255,
                    ),
                ),
                ("structure_type_id", models.BigIntegerField()),
                ("alliance_name", models.CharField(max_length=255)),
                ("alliance_id", models.BigIntegerField()),
                (
                    "timer_type",
                    models.CharField(
                        choices=[("armor", "Armor"), ("structure", "Structure")],
                        max_length=255,
                    ),
                ),
                ("timer", models.DateTimeField()),
                ("system", models.CharField(max_length=255)),
                ("system_id", models.BigIntegerField(blank=True, null=True)),
                (
                    "constellation",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("constellation_id", models.BigIntegerField(blank=True, null=True)),
                ("region", models.CharField(blank=True, max_length=255, null=True)),
                ("region_id", models.BigIntegerField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("created_by_character_id", models.BigIntegerField()),
                ("created_by_character_name", models.CharField(max_length=255)),
            ],
        ),
    ]