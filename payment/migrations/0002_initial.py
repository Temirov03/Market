# Generated by Django 4.2.1 on 2023-05-26 13:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("provider", "0001_initial"),
        ("payment", "0001_initial"),
        ("income", "0001_initial"),
        ("order", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="paymenttransaction",
            name="created_user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="created_user",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Yaratgan xodim",
            ),
        ),
        migrations.AddField(
            model_name="paymenttransaction",
            name="deleted_user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="deleted_user",
                to=settings.AUTH_USER_MODEL,
                verbose_name="O'chirgan xodim",
            ),
        ),
        migrations.AddField(
            model_name="paymenttransaction",
            name="income",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="income.income",
                verbose_name="Maxsulot krimi",
            ),
        ),
        migrations.AddField(
            model_name="paymenttransaction",
            name="order",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="order.order",
                verbose_name="Zakaz",
            ),
        ),
        migrations.AddField(
            model_name="paymenttransaction",
            name="outlay",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="payment.outlay",
                verbose_name="Xarajat nomi",
            ),
        ),
        migrations.AddField(
            model_name="paymenttransaction",
            name="provider",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="provider.provider",
                verbose_name="Yetkazib beruvchi",
            ),
        ),
        migrations.AddField(
            model_name="outlay",
            name="outlay_category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="payment.outlaycategory",
                verbose_name="Xarajot kategoriyasi",
            ),
        ),
    ]
