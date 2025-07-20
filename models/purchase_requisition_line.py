from odoo import api, fields, models, _

from datetime import date

class PurchaseRequisitionLine(models.Model):
    _name="purchase.requisition.line"
    _description = "Purchase Requisition Line"

    requisition_id=fields.Many2one("purchase.requisition" , string="Related requisition ID")

    requisition_type=fields.Selection([
        ('internal_transfer','Internal Transfer'),
        ('external_transfer','External Transfer'),
    ] , string="Requisition Types")
    product_id=fields.Many2one("product.product" , string="Product requested")
    description=fields.Text(string="Additional description")
    qty_available=fields.Float(string="Quantity needed")
    vendor_id=fields.Many2one("res.partner" , string="Vendor (if applicable)")
