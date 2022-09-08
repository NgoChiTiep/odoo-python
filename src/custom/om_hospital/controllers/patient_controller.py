import json

from odoo import http
from odoo.http import Response


class PatientController(http.Controller):
    @http.route('/api/patients', methods=['GET'], auth='public', cors='*')
    def handler(self, **kwargs):
        headers_json = {'Content-Type': 'application/json'}
        try:
            patients_list = http.request.env['hospital.patient'].sudo().search([])
            list = []
            for item in patients_list:
                list.append({'id': item.id, 'name': item.name, 'gender': item.gender, 'age': item.age })
            response = {
                "status": "200",
                "data": list
            }
        except Exception as e:
            response = {
                "status": "error",
                "content": "not found"
            }
        return Response(json.dumps(response), headers=headers_json)
