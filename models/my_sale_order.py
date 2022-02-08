from odoo import models, fields


class MyPurchaseOrder(models.Model):
    _inherit = 'sale.order.line'
    dimension = fields.Char(string='Dimension:')

    def _prepare_procurement_values(self, group_id=False):
        res = super(MyPurchaseOrder, self)._prepare_procurement_values(group_id)
        res.update({'dimension': self.dimension})
        return res

    def _prepare_invoice_line(self, **optional_values):
        res = super(MyPurchaseOrder, self)._prepare_invoice_line(**optional_values)
        res.update({'dimension': self.dimension})
        return res


class CustomSaleOrder(models.Model):
    _inherit = 'sale.order'
    dimension = fields.Char(string='Dimension:')

    def action_confirm(self):
        res = super(CustomSaleOrder, self).action_confirm()
        return res


class CustomStockMove(models.Model):
    _inherit = 'stock.move'
    dimension = fields.Char(string='Dimension')


class StockRuleInherit(models.Model):
    _inherit = 'stock.rule'

    def _get_stock_move_values(self, product_id, product_qty, product_uom, location_id, name, origin, company_id, values):
        res = super(StockRuleInherit, self)._get_stock_move_values(product_id, product_qty, product_uom , location_id, name,
                                                                    origin, company_id, values)
        res['dimension'] = values.get('dimension', False)
        return res


class CustomAccountMove(models.Model):
    _inherit = 'account.move.line'

    dimension = fields.Char(string='Dimension:')