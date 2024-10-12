from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_user_task_list200_response import GetUserTaskList200Response
from openapi_server import util


async def get_user_task_list(request: web.Request, user_task_list_gid, opt_pretty=None, opt_fields=None) -> web.Response:
    """Get a user task list

    Returns the full record for a user task list.

    :param user_task_list_gid: Globally unique identifier for the user task list.
    :type user_task_list_gid: str
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    return web.Response(status=200)


async def get_user_task_list_for_user(request: web.Request, user_gid, workspace, opt_pretty=None, opt_fields=None) -> web.Response:
    """Get a user&#39;s task list

    Returns the full record for a user&#39;s task list.

    :param user_gid: A string identifying a user. This can either be the string \&quot;me\&quot;, an email, or the gid of a user.
    :type user_gid: str
    :param workspace: The workspace in which to get the user task list.
    :type workspace: str
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    return web.Response(status=200)
