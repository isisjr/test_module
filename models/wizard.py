# -*- coding: utf-8 -*-

from openerp import models, fields, api


class Wizard(models.TransientModel):

    _name = 'test_module.wizard'

    def _default_session(self):
        return self.env['test_module.session'].browse(self._context.get('active_ids'))#active_id para una sola session

    #session_id para una sola session
    session_ids = fields.Many2one('test_module.session',
                                 string="Session", required=True, default=_default_session)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    @api.multi
    def subscribe(self):
        #self.session_id.attendee_ids |= self.attendee_ids
        for session in self.session_ids:
            session.attendee_ids |= self.attendee_ids
        return {}