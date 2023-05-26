# Generated by Django 4.2.1 on 2023-05-26 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Movement",
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
                    "status",
                    models.CharField(
                        choices=[
                            ("created", "Yaratilgan"),
                            ("accepted", "Tasdiqlangan"),
                            ("completed", "Tugallangan"),
                            ("canceled", "Rad etilgan"),
                        ],
                        max_length=255,
                        null=True,
                        verbose_name="Statusi",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Warehouse",
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
                ("name", models.CharField(max_length=255, verbose_name="Baza nomi")),
            ],
            options={
                "verbose_name": "Baza",
                "verbose_name_plural": "Bazalar",
            },
        ),
        migrations.CreateModel(
            name="WarehouseProduct",
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
                ("count", models.IntegerField(verbose_name="Soni")),
                (
                    "total",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=17,
                        null=True,
                        verbose_name="Summasi",
                    ),
                ),
                (
                    "self_price",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=17,
                        verbose_name="Maxsulotning tan narxi",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="product.product",
                        verbose_name="Maxsulot nomi",
                    ),
                ),
                (
                    "warehouse",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="warehouse.warehouse",
                        verbose_name="Baza",
                    ),
                ),
            ],
            options={
                "verbose_name": "Bazadagi maxsulot",
                "verbose_name_plural": "Bazadagi maxsulotlar",
            },
        ),
        migrations.CreateModel(
            name="MovementItem",
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
                ("count", models.IntegerField(verbose_name="Maxsulot soni")),
                (
                    "movement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="warehouse.movement",
                        verbose_name="Ko'chirma",
                    ),
                ),
                (
                    "warehouse_product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="warehouse.warehouseproduct",
                        verbose_name="Maxsulot",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="movement",
            name="from_warehouse",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="from_warehouse",
                to="warehouse.warehouse",
                verbose_name="Bazadan",
            ),
        ),
        migrations.AddField(
            model_name="movement",
            name="to_warehouse",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="to_warehouse",
                to="warehouse.warehouse",
                verbose_name="Bazaga",
            ),
        ),
    ]
