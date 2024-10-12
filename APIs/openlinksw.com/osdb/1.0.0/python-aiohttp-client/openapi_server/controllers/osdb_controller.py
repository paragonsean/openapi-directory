from typing import List, Dict
from aiohttp import web

from openapi_server.models.action_help_response import ActionHelpResponse
from openapi_server.models.describe_action_response import DescribeActionResponse
from openapi_server.models.describe_service_response import DescribeServiceResponse
from openapi_server.models.error_model import ErrorModel
from openapi_server.models.exec_body import ExecBody
from openapi_server.models.list_actions_response import ListActionsResponse
from openapi_server.models.list_services_response import ListServicesResponse
from openapi_server.models.load_service200_response import LoadService200Response
from openapi_server.models.load_service_request import LoadServiceRequest
from openapi_server.models.login_response import LoginResponse
from openapi_server.models.logout_response import LogoutResponse
from openapi_server import util


async def action_help(request: web.Request, service_id, action_id) -> web.Response:
    """Action help

    Returns the help text for a given service action

    :param service_id: Service ID of the service supporting the action.
    :type service_id: str
    :param action_id: Action ID of the action for which help text is being requested.
    :type action_id: str

    """
    return web.Response(status=200)


async def describe_action(request: web.Request, service_id, action_id) -> web.Response:
    """Describe action

    Returns a description of a given service action.

    :param service_id: Service ID of the service supporting the action.
    :type service_id: str
    :param action_id: Action ID of the action to describe.
    :type action_id: str

    """
    return web.Response(status=200)


async def describe_service(request: web.Request, service_id) -> web.Response:
    """Describe service

    Returns a description of a given service

    :param service_id: Service ID of the service to describe.
    :type service_id: str

    """
    return web.Response(status=200)


async def execute_action(request: web.Request, service_id, action_id, body=None) -> web.Response:
    """Execute action

    Executes a registered service action and returns any output from the action. The data returned in the POST response body may be:  * the raw action output,  * a URL encapsulating the action request which executes the action when dereferenced  (only for actions using GET),  * RDF generated from the action output, * a URL to an RDF viewer&#39;s display of the generated RDF.  Any parameters required by the action are supplied as a JSON object in the POST body. The parameter types supported are: \&quot;query\&quot;, \&quot;header\&quot;, \&quot;uri\&quot;, \&quot;path\&quot; and \&quot;body\&quot;.  The parameter type determines where a supplied parameter value is inserted into the HTTP request constructed by OSDB to invoke the target service action. In addition to native parameters required by the service action, &#39;Execute action&#39; accepts some OSDB-specific parameters.&lt;br/&gt;&lt;br/&gt;  **Examples** * &#x60;&#x60;&#x60;curl -ik -X POST -d &#39;{ \&quot;latitude\&quot;:\&quot;37.7759792\&quot;, \&quot;longitude\&quot;:\&quot;-122.41823\&quot; }&#39; -H &#39;Content-Type: application/json&#39; https://osdb.openlinksw.com/osdb/api/v1/actions/uber/products/exec&#x60;&#x60;&#x60;   * &#x60;&#x60;&#x60;curl -ikL -X POST -d &#39;{ \&quot;latitude\&quot;:\&quot;37.7759792\&quot;, \&quot;longitude\&quot;:\&quot;-122.41823\&quot;, \&quot;osdb:output_type\&quot;:\&quot;generate_rdf\&quot;, \&quot;osdb:response_format\&quot;:\&quot;application/rdf+xml\&quot; }&#39; -H &#39;Content-Type: application/json&#39; https://osdb.openlinksw.com/osdb/api/v1/actions/uber/products/exec&#x60;&#x60;&#x60;  * &#x60;&#x60;&#x60;curl -ikL -X POST -d &#39;{ \&quot;latitude\&quot;:\&quot;37.7759792\&quot;, \&quot;longitude\&quot;:\&quot;-122.41823\&quot;, \&quot;osdb:output_type\&quot;:\&quot;display_rdf\&quot; }&#39; -H &#39;Content-Type: application/json&#39; https://osdb.openlinksw.com/osdb/api/v1/actions/uber/products/exec&#x60;&#x60;&#x60;  * &#x60;&#x60;&#x60;curl -ik -X POST -d &#39;{ \&quot;q\&quot;:\&quot;skiing\&quot;, \&quot;osdb:response_format\&quot;: \&quot;application/rdf+xml\&quot; }&#39; -H &#39;Content-Type: application/json&#39; https://osdb.openlinksw.com/osdb/api/v1/actions/facet/search/exec&#x60;&#x60;&#x60;  * &#x60;&#x60;&#x60;curl -ik -X POST -d &#39;{ \&quot;q\&quot;:\&quot;skiing\&quot;, \&quot;osdb:output_type\&quot;: \&quot;url_only\&quot; }&#39; -H &#39;Content-Type: application/json&#39; https://osdb.openlinksw.com/osdb/api/v1/actions/facet/search/exec&#x60;&#x60;&#x60;  * &#x60;&#x60;&#x60;curl -ik -X POST -d &#39;{ \&quot;Content-Location\&quot;: \&quot;http://demo.openlinksw.co.uk/pubs\&quot;, \&quot;osdb:body_data_src_url\&quot;: \&quot;http://ods-qa.openlinksw.com/DAV/home/osdb/pubs.csv\&quot;, \&quot;extractor\&quot;: \&quot;csv\&quot;, \&quot;osdb:response_format\&quot;: \&quot;application/rdf+xml\&quot;, \&quot;osdb:body_data_encoding\&quot;: \&quot;text/csv\&quot; }&#39; -H &#39;Content-Type: application/json&#39; https://osdb.openlinksw.com/osdb/api/v1/actions/csv_transformer/transform/exec&#x60;&#x60;&#x60;

    :param service_id: Service ID of the service supporting the action.
    :type service_id: str
    :param action_id: Action ID of the action to execute.
    :type action_id: str
    :param body: Any parameters required by the action are supplied as a JSON object in the request body. The properties of this object depend on the service action being invoked.
    :type body: dict | bytes

    """
    body = ExecBody.from_dict(body)
    return web.Response(status=200)


async def list_actions(request: web.Request, service_id) -> web.Response:
    """List actions

    Returns an array of action descriptions for the actions supported by the given service

    :param service_id: Service ID of the service for which actions are to be listed
    :type service_id: str

    """
    return web.Response(status=200)


async def list_services(request: web.Request, ) -> web.Response:
    """List services

    Returns descriptions of all services registered with the OSDB server.


    """
    return web.Response(status=200)


async def load_service(request: web.Request, body=None) -> web.Response:
    """Load service

    Loads a service description into the OSDB Service Registry

    :param body: Service to register with OSDB
    :type body: dict | bytes

    """
    body = LoadServiceRequest.from_dict(body)
    return web.Response(status=200)


async def login(request: web.Request, ) -> web.Response:
    """Login

    Logs a user into the OSDB server, authenticating them by their WebID and returning an OSDB session ID in cookie osdb.sid


    """
    return web.Response(status=200)


async def logout(request: web.Request, ) -> web.Response:
    """Logout

    Logs a user out of the OSDB server, ending their OSDB session


    """
    return web.Response(status=200)


async def unload_service(request: web.Request, service_id) -> web.Response:
    """Unload service

    Removes a service description from the OSDB Service Registry

    :param service_id: Service ID of the service to be unloaded
    :type service_id: str

    """
    return web.Response(status=200)
