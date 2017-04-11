# -*- coding: utf-8 -*-
# Copyright 2017 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Link between assets and equipments",
    "summary": "Create equipment when validating an invoice with assets",
    "version": "10.0.1.0.0",
    "category": "Accounting & Finance",
    "website": "https://www.tecnativa.com/",
    "author": "Tecnativa, "
              "Onestein, "
              "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "account_asset",
        "account_cancel",
        "mail",
        "maintenance",
    ],
    "data": [
        "views/account_asset_asset_views.xml",
        "views/account_asset_category_views.xml",
        "views/account_config_setting_views.xml",
        "views/account_invoice_views.xml",
        "views/maintenance_equipment_views.xml",
        "wizard/scrap_equipment.xml",
    ],
}
