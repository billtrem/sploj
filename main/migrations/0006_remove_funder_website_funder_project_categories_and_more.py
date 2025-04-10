# Generated by Django 5.1.7 on 2025-03-26 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_projectcategory_color_alter_projectcategory_info_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funder',
            name='website',
        ),
        migrations.AddField(
            model_name='funder',
            name='project_categories',
            field=models.ManyToManyField(blank=True, related_name='funders', to='main.projectcategory'),
        ),
        migrations.AddField(
            model_name='funder',
            name='show_on_info_page',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='funder',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
