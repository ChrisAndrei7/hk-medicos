# Generated by Django 4.2.1 on 2024-01-13 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pedido_id', models.IntegerField()),
                ('valor', models.FloatField()),
                ('status', models.CharField(max_length=25)),
            ],
        ),
    ]
