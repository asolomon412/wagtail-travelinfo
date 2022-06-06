# Generated by Django 4.0.4 on 2022-06-06 18:31

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_banner_background_image_homepage_button_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('title', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(help_text='Text to display', required=True))]))], blank=True, null=True, use_json_field=None),
        ),
    ]
