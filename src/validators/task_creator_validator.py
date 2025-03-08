from cerberus import Validator

def task_creator_validator(request: any):
	body_validator = Validator({
		'data': {
			'type': 'dict',
			'schema': {
				'title': {
					'type': 'string',
					'required': True,
					'empty': False
				},
				'description': {
					'type': 'string',
					'required': True,
					'empty': False
				},
				'priority': {
					'type': 'string',
					'required': True,
					'empty': False
				},
				'status': {
					'type': 'string',
					'required': True,
					'empty': False
				}
			}
		}
	})

	response = body_validator.validate(request)

	if not response:
		raise Exception(body_validator.errors)