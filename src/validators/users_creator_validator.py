from cerberus import Validator
from fastapi import HTTPException

def users_creator_validator(request: any):
	body_validator = Validator({
		'data': {
			'type': 'dict',
			'schema': {
				'name': {
					'type': 'string',
					'required': True,
					'empty': False
				},
				'email': {
					'type': 'string',
					'required': True,
					'empty': False
				},
				'password': {
					'type': 'string',
					'required': True,
					'empty': False
				}
			}
		}
	})

	response = body_validator.validate(request)

	if not response:
		print(body_validator.errors)
		raise HTTPException(status_code=400, detail="Erro")