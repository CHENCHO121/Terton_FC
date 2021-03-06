# Generated by Django 3.0 on 2020-09-29 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Academy_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_scholarship', models.TextField(max_length=500, null=True)),
                ('half_scholarship', models.TextField(max_length=500, null=True)),
                ('self_paid', models.TextField(max_length=500, null=True)),
                ('training', models.TextField(max_length=500, null=True)),
                ('football', models.TextField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name': 'Contact',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='media/upload')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='media/upload')),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery_Old_Age_Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/upload')),
            ],
            options={
                'verbose_name': 'Gallery Old Age Home',
            },
        ),
        migrations.CreateModel(
            name='Gallery_Orphange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/upload')),
            ],
            options={
                'verbose_name': 'Gallery Orphange',
            },
        ),
        migrations.CreateModel(
            name='Gallery_player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/upload')),
            ],
            options={
                'verbose_name': 'Gallery Player',
            },
        ),
        migrations.CreateModel(
            name='Old_Age_Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('info', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='media/upload')),
            ],
            options={
                'verbose_name': 'Old Age Home',
            },
        ),
        migrations.CreateModel(
            name='Orphanage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('info', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='media/upload')),
            ],
            options={
                'verbose_name': 'Orphanage',
            },
        ),
        migrations.CreateModel(
            name='ScholarshipForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('father', models.CharField(max_length=30, null=True)),
                ('mother', models.CharField(max_length=30, null=True)),
                ('age', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('qualification', models.CharField(max_length=40)),
                ('address', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Self_Training_Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('address', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('info', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='media/upload')),
            ],
            options={
                'verbose_name': 'Orphanage',
            },
        ),
        migrations.CreateModel(
            name='Student_Financial_Crisis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=60)),
                ('phone', models.IntegerField()),
                ('age', models.IntegerField()),
                ('school_year', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('reason_for_applying', models.CharField(max_length=30)),
                ('age_range', models.CharField(max_length=20)),
                ('school_type', models.CharField(max_length=20)),
                ('support_for', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Student Financial crisis Registration',
            },
        ),
    ]
