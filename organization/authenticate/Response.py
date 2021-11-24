import json

class BaseResponse:

    def __init__(self, result, message):
        self.result = result
        self.message = message

    def get_response_body(self):
        return {
            'result': self.result,
            'message': self.message
        }

