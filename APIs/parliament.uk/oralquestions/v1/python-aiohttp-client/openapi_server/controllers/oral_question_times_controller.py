from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_response_list_published_written_question import ApiResponseListPublishedWrittenQuestion
from openapi_server.models.api_response_object import ApiResponseObject
from openapi_server import util


async def published_oral_question_time_get(request: web.Request, parameters_answering_date_start=None, parameters_answering_date_end=None, parameters_deadline_date_start=None, parameters_deadline_date_end=None, parameters_oral_question_time_id=None, parameters_answering_body_ids=None, parameters_skip=None, parameters_take=None) -> web.Response:
    """Returns a list of oral question times

    A list of oral question times meeting the specified criteria.

    :param parameters_answering_date_start: Oral Questions Time where the answering date has been set on or after the date provided. Date format YYYY-MM-DD.
    :type parameters_answering_date_start: str
    :param parameters_answering_date_end: Oral Questions Time where the answering date has been set on or before the date provided. Date format YYYY-MM-DD.
    :type parameters_answering_date_end: str
    :param parameters_deadline_date_start: Oral Questions Time where the deadline date has been set on or after the date provided. Date format YYYY-MM-DD.
    :type parameters_deadline_date_start: str
    :param parameters_deadline_date_end: Oral Questions Time where the deadline date has been set on or before the date provided. Date format YYYY-MM-DD.
    :type parameters_deadline_date_end: str
    :param parameters_oral_question_time_id: Identifier of the OQT
    :type parameters_oral_question_time_id: int
    :param parameters_answering_body_ids: Which answering body is to respond. A list of answering bodies can be found &lt;a target&#x3D;\&quot;_blank\&quot; href&#x3D;\&quot;http://data.parliament.uk/membersdataplatform/services/mnis/referencedata/AnsweringBodies/\&quot;&gt;here&lt;/a&gt;.
    :type parameters_answering_body_ids: List[int]
    :param parameters_skip: The number of records to skip from the first, default is 0.
    :type parameters_skip: int
    :param parameters_take: The number of records to return, default is 25, maximum is 100.
    :type parameters_take: int

    """
    parameters_answering_date_start = util.deserialize_datetime(parameters_answering_date_start)
    parameters_answering_date_end = util.deserialize_datetime(parameters_answering_date_end)
    parameters_deadline_date_start = util.deserialize_datetime(parameters_deadline_date_start)
    parameters_deadline_date_end = util.deserialize_datetime(parameters_deadline_date_end)
    return web.Response(status=200)
