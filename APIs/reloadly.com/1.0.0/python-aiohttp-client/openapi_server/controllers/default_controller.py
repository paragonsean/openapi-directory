from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_a_new_question_request import CreateANewQuestionRequest
from openapi_server import util


async def create_a_new_question(request: web.Request, body=None) -> web.Response:
    """Create a New Question

    You may create your own question using this action. It takes a JSON object containing a question and a collection of answers in the form of choices.

    :param body: 
    :type body: dict | bytes

    """
    body = CreateANewQuestionRequest.from_dict(body)
    return web.Response(status=200)


async def list_all_questions(request: web.Request, ) -> web.Response:
    """List All Questions

    


    """
    return web.Response(status=200)
