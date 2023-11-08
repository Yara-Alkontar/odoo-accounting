from odoo import api, fields, models, _

class ResCompany(models.Model):
    _inherit = "res.company"

    account_journal_early_pay_discount_gain_account_id = fields.Many2one('account.account', domain="[('deprecated', '=', False), ('company_id', '=', id)]", help="Account used to write the journal item in case of gain while selling an asset")
    account_journal_early_pay_discount_loss_account_id = fields.Many2one('account.account', domain="[('deprecated', '=', False), ('company_id', '=', id)]", help="Account used to write the journal item in case of loss while selling an asset")
    
