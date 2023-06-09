# Generated by Django 4.2.1 on 2023-05-26 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("warehouse", "0001_initial"),
        ("product", "0001_initial"),
        ("provider", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Income",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Yasalgan vaqti"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("created", "Yaratilgan"),
                            ("accepted", "Tasdiqlangan"),
                            ("completed", "Tugallangan"),
                            ("canceled", "Rad etilgan"),
                        ],
                        default="created",
                        max_length=255,
                        verbose_name="Statusi",
                    ),
                ),
                (
                    "total",
                    models.DecimalField(
                        decimal_places=2, default=0, max_digits=17, verbose_name="Narxi"
                    ),
                ),
                (
                    "provider",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="provider.provider",
                        verbose_name="Yitkazib beruvchi",
                    ),
                ),
                (
                    "warehouse",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="warehouse.warehouse",
                        verbose_name="Baza",
                    ),
                ),
            ],
            options={
                "verbose_name": "Maxsulotlar_krimi",
                "verbose_name_plural": "Maxsulotlar_krimlari",
            },
        ),
        migrations.CreateModel(
            name="IncomeItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=17, verbose_name="Narxi"
                    ),
                ),
                ("count", models.IntegerField(verbose_name="Soni")),
                (
                    "total",
                    models.DecimalField(
                        decimal_places=2, max_digits=17, verbose_name="Summasi"
                    ),
                ),
                (
                    "income",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="income.income",
                        verbose_name="Krim",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="product.product",
                        verbose_name="Maxsulot",
                    ),
                ),
            ],
            options={
                "verbose_name": "Maxsulot_krimi",
                "verbose_name_plural": "Maxsulot_krimlari",
            },
        ),
    ]
