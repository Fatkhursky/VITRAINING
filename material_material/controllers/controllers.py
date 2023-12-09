# -*- coding: utf-8 -*-
# from odoo import http
import json
from odoo import http, _, exceptions
from odoo.http import content_disposition, request, Response
from odoo.addons.web.controllers.main import Home
from odoo import SUPERUSER_ID
from odoo.exceptions import UserError
from odoo.http import Controller, dispatch_rpc, route
from odoo.http import request
from odoo.exceptions import ValidationError, AccessError
from odoo.tools import config
from odoo.tools.safe_eval import safe_eval

class MaterialApi(http.Controller):
    def _auth(self, authorization):
        if not 'Bearer' in authorization:
            return False
        token = authorization.replace('Bearer ', '')
        if request.env['res.users.apikeys']._check_credentials(scope='rpc', key=token):
            return True
        return False
    
    def eval_request_params(self, kwargs):
        for k, v in kwargs.items():
            try:
                kwargs[k] = safe_eval(v)
            except Exception:
                continue

    @route('/get-material', type='http', auth='public', save_session=False, csrf=False, cors="*", methods=['GET'])
    def search_read(self, **kw):
        self.eval_request_params(kw)
        auth = self._auth(request.httprequest.headers.get('Authorization'))

        if not auth:
            Response.status = '401'
            json_data = json.dumps(
                {'message': f'''Invalid bearerr token!'''}
            )
            return Response(json_data, content_type='application/json')
        try:
            materials = request.env['material.material'].sudo().search_read(**kw)
            print(f'''\033[96m{'MATERIA', materials}\033[0m''')
            json_data = json.dumps(
                {'results': materials}
            )
            return Response(json_data, content_type='application/json')
        except Exception as e:
            Response.status = '403'
            json_data = json.dumps(
                {'message': str(e)}
            )
            return Response(json_data, content_type='application/json')