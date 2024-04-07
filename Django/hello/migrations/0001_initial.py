# Generated by Django 4.1.11 on 2023-09-05 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='activities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=300)),
                ('type', models.CharField(max_length=20)),
                ('result', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
                ('event_date', models.DateTimeField(verbose_name='date logged')),
            ],
        ),
    ]
'''GeeksModel.objects.create(name="KB CAR PARKING RENT",address="1, Vinoba St, Kamatchi Nagar, Durga Nagar, Tambaram, Chennai, Tamil Na…",catogories="Parking lot",total=460,avail=138,full=322,locationid="ChIJAetFOCtfUjoR2i2g2V1Kr00").save() '''