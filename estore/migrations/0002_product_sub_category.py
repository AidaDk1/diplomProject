# Generated by Django 3.2 on 2022-08-23 18:56

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='category', chained_model_field='category', null=True, on_delete=django.db.models.deletion.CASCADE, to='estore.subcategory'),
        ),
    ]