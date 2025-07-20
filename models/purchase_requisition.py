from odoo import api, fields, models, _

from datetime import date


class PurchaseRequisition(models.Model):
    _name = "purchase.requisition"
    _description = "Purchase Requisition"

    name = fields.Char(string="Name" , readonly=1)
    employee_id = fields.Many2one("hr.employee", string="Employee ID")
    responsible_id = fields.Many2one("res.users", string="Responsible ID")
    dept_id = fields.Many2one("hr.department", string="Department ID")
    requisition_date = fields.Date(string="Requisition Date")
    requisition_deadline = fields.Date(string=" Requisition Deadline")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('inventory_approval', 'Inventory Approval'),
        ('purchase_approval', 'Purchase Approval'),
        ('confirmed', 'Confirmed'),
        ('received', 'Received'),
    ], default='draft', string="Workflow status")
    requisition_line_ids = fields.One2many("purchase.requisition.line", "requisition_id", string="Requisition Lines")

    def submit_for_inventory(self):
        for each in self:
            each.state='inventory_approval'
        return

    def submit_for_purchase(self):
        for each in self:
            each.state='purchase_approval'
        return


    def confirm(self):
        for each in self:
            each.state='confirmed'
        return


    def mark_as_received(self):
        for each in self:
            each.state='received'
        return


    @api.model
    def create(self , vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('purchase.requisition')
        return super(PurchaseRequisition, self).create(vals)

