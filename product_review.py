from odoo import api, fields, models

class ProductReview(models.Model):
    _name = 'product.review'
    _description = 'Product Review'

    product_id = fields.Many2one('product.template', string='Product', required=True)
    user_id = fields.Many2one('res.users', string='User', required=True)
    rating = fields.Selection([(str(i), str(i)) for i in range(1, 6)], string='Rating', required=True)
    review = fields.Text(string='Review')

    @api.model
    def create(self, vals):
        review = super(ProductReview, self).create(vals)
        return review
