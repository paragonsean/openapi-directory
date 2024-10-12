from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.operation_status import OperationStatus
from openapi_server.models.survey_answers import SurveyAnswers
from openapi_server.models.survey_question import SurveyQuestion
from openapi_server import util


async def get_questions(request: web.Request, scope, type, attach_answers_for_project=None) -> web.Response:
    """Get survey questions in given scope and type

    Get survey questions in given scope and type

    :param scope: Scope
    :type scope: str
    :param type: Type
    :type type: str
    :param attach_answers_for_project: Project ID
    :type attach_answers_for_project: int

    """
    return web.Response(status=200)


async def submit_answers(request: web.Request, scope, type, body=None) -> web.Response:
    """Post survey answers for scope and type

    Post survey answers for scope and type

    :param scope: Scope
    :type scope: str
    :param type: Type
    :type type: str
    :param body: 
    :type body: dict | bytes

    """
    body = SurveyAnswers.from_dict(body)
    return web.Response(status=200)
