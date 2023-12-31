# Generated by Django 3.2.16 on 2023-09-03 15:17

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20230903_1809'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='posts_follow_prevent_self_follow',
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.CheckConstraint(check=models.Q(('user', django.db.models.expressions.F('following')), _negated=True), name='posts_follow_prevent_self_follow'),
        ),
    ]
