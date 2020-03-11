from http import HTTPStatus


def build_response(response_data=None, response_msg="success", status_code=HTTPStatus.OK.value):
    return {
        "response_data": response_data,
        "response_msg": response_msg
    }, status_code
