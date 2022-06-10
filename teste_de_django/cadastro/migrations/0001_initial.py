# Generated by Django 4.0.5 on 2022-06-08 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=9)),
                ('endereco', models.TextField()),
                ('numero', models.IntegerField()),
                ('complemento', models.CharField(max_length=40)),
                ('bairro', models.CharField(max_length=40)),
                ('cidade', models.CharField(max_length=40)),
                ('uf', models.CharField(max_length=2)),
                ('descricao', models.TextField()),
            ],
        ),
    ]
