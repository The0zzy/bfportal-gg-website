# Generated by Django 3.2.12 on 2022-08-28 05:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailsvg", "0004_remove_svg_edit_code"),
        ("core", "0042_alter_experiencescategory_icon"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subcategory",
            name="icon",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailsvg.svg",
            ),
        ),
    ]