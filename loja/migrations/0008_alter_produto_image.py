# Generated by Django 4.2.7 on 2025-02-17 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0007_carrinho_alter_usuario_perfil_carrinhoitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='image',
            field=models.BinaryField(blank=True, null=True),
        ),
    ]
