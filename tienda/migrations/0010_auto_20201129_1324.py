# Generated by Django 3.1.3 on 2020-11-29 19:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tienda', '0009_venta_venta_finalizada'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detalle_venta',
            name='id_usuario',
        ),
        migrations.AddField(
            model_name='venta',
            name='id_usuario',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
