from typing import List, Dict
from aiohttp import web

from openapi_server.models.interview import Interview
from openapi_server.models.survey_detail import SurveyDetail
from openapi_server.models.survey_metadata import SurveyMetadata
from openapi_server import util


async def surveys_get(request: web.Request, ) -> web.Response:
    """Returns a list of available Surveys

    


    """
    return web.Response(status=200)


async def surveys_survey_id_interviews_get(request: web.Request, survey_id, start=None, max_length=None) -> web.Response:
    """Fetches some interview records for a specific survey

    

    :param survey_id: 
    :type survey_id: str
    :type survey_id: str
    :param start: 
    :type start: int
    :param max_length: 
    :type max_length: int

    """
    return web.Response(status=200)


async def surveys_survey_id_metadata_get(request: web.Request, survey_id) -> web.Response:
    """Fetches the metadata for a specific survey

    

    :param survey_id: 
    :type survey_id: str
    :type survey_id: str

    """
    return web.Response(status=200)
