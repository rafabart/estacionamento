# Generated by Django 2.1.2 on 2019-08-12 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190811_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='proprietario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='core.Pessoa'),
            preserve_default=False,
        ),
    ]