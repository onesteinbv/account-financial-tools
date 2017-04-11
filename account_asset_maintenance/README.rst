.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

==================================
Link between assets and equipments
==================================

This module links assets with equipments, allowing to create automatically
an equipment from the supplier invoice if an equipment category is assigned
in the asset category.

Moreover this module enhances the scrapping equipment functionality by
introducing the opportunity to set a mail template on companies in order to
automatically send a mail, according to that template, each time an equipment
of the company is scrapped. In addition, it forces the user to set a scrap
date when scrapping an equipment.

Configuration
=============

To configure this module, you need to:

#. Go to *Accounting > Configuration > Management > Asset Types*.
#. Select one asset type.
#. Fill the field "Equipment category" with the equipment category we want to
   assign to the auto-created equipments.

To configure the scrapping functionality introduced in this module you need to:

#. Go to 'Settings' -> 'Technical' -> 'Email' -> 'Templates' and create a new template you wish to use for equipment scrapping notifications
#. Go to 'Accounting' -> 'Configuration' -> 'Settings'
#. You will find a new section called 'Scrapping', there you will be able to select the mail template just created as 'Equipment Scrap Template Email'
#. Go to 'Maintenance' -> 'Equipments' and create a new equipment or select an already existing one
#. You will be able to select the mail template you previously created as 'Equipment Scrap Template Email' (for new equipments, the one selected in the settings will be automatically proposed)

Usage
=====

To use this module, you need to:

#. Go to *Accounting > Purchases > Vendor Bills*.
#. Create a new bill.
#. Create one invoice line.
#. Select an asset category with an equipment category filled.
#. Validate the invoice.
#. A new page called "Equipments" will appear with the auto-created equipments.
#. An equipment will created per each quantity indicated in the invoice line.
#. If the quantity is not integer (for example: 3.5), the upper integer number
   will be used (4 for the example).
#. If you cancel the bill, the created equipments will be removed.

You can access equipments for the created asset:

#. Go to *Accounting > Adviser > Assets*.
#. Open the created asset
#. You will see an smart-button with the string "Equipments" that links to the
   created asset.

If you want to scrap an equipment, you need to:

#. Go to 'Maintenance' -> 'Equipments' and select an already existing equipment
#. Click the button 'Scrap'
#. On the wizard select a date for the field 'Scrap Date' and click 'Scrap'

You will find that the selected date was automatically set to the 'Scrap Date' field of the equipment.
Moreover, if on the equipment an 'Equipment Scrap Template Email' was set, such template was used to generate a message to notify that the equipment was scrapped.

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/92/10.0

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/OCA/account-financial-tools/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smash it by providing detailed and welcomed feedback.

Credits
=======

Contributors
------------

* Pedro M. Baeza <pedro.baeza@tecnativa.com>
* Antonio Esposito <a.esposito@onestein.nl>

Maintainer
----------

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit https://odoo-community.org.
