# Generated by Django 4.2.4 on 2023-09-04 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='게시글 제목')),
                ('content', models.TextField(verbose_name='게시글 내용')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성시간')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정시간')),
            ],
        ),
    ]
