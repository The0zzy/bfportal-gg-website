# Generated by Django 3.2.12 on 2022-10-11 09:28

import core.helper
import django.db.models.deletion
import wagtail.blocks
import wagtail.contrib.routable_page.models
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0077_alter_revision_user"),
        ("core", "0064_auto_20221008_1001"),
    ]

    operations = [
        migrations.CreateModel(
            name="EventsPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "extra_content",
                    wagtail.fields.StreamField(
                        [
                            (
                                "heading",
                                wagtail.blocks.CharBlock(form_classname="full title"),
                            ),
                            ("cover_image", wagtail.images.blocks.ImageChooserBlock()),
                            ("text", wagtail.blocks.RichTextBlock()),
                            ("raw_html", wagtail.blocks.RawHTMLBlock()),
                        ],
                        blank=True,
                        use_json_field=None,
                    ),
                ),
                (
                    "meta_title",
                    models.CharField(
                        blank=True,
                        help_text="If set this title is displayed in embeds",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "meta_description",
                    models.TextField(
                        blank=True,
                        help_text="If set this description is displayed in embeds",
                        null=True,
                    ),
                ),
                (
                    "meta_image",
                    models.URLField(
                        blank=True,
                        help_text="If set this image is displayed in embeds. Recommend size 1200x630px",
                        null=True,
                        validators=[core.helper.validate_image_link],
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(
                wagtail.contrib.routable_page.models.RoutablePageMixin,
                "wagtailcore.page",
            ),
        ),
        migrations.AlterField(
            model_name="experiencepage",
            name="xp_farm",
            field=models.BooleanField(
                default=False,
                help_text="Is the experience an xp farm",
                verbose_name="XP farm ?",
            ),
        ),
    ]
