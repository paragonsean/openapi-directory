from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_name_availability_input import CheckNameAvailabilityInput
from openapi_server.models.check_name_availability_output import CheckNameAvailabilityOutput
from openapi_server.models.communication_details import CommunicationDetails
from openapi_server.models.communications_list_result import CommunicationsListResult
from openapi_server.models.exception_response import ExceptionResponse
from openapi_server import util


async def communications_check_name_availability(request: web.Request, support_ticket_name, subscription_id, api_version, check_name_availability_input) -> web.Response:
    """communications_check_name_availability

    Check the availability of a resource name. This API should to be used to check the uniqueness of the name for adding a new communication to the support ticket.

    :param support_ticket_name: Support ticket name
    :type support_ticket_name: str
    :param subscription_id: Azure subscription id
    :type subscription_id: str
    :param api_version: Api version
    :type api_version: str
    :param check_name_availability_input: Input to check
    :type check_name_availability_input: dict | bytes

    """
    check_name_availability_input = CheckNameAvailabilityInput.from_dict(check_name_availability_input)
    return web.Response(status=200)


async def communications_create(request: web.Request, support_ticket_name, communication_name, subscription_id, api_version, create_communication_parameters) -> web.Response:
    """communications_create

    Adds a new customer communication to an Azure support ticket. Adding attachments are not currently supported via the API. &lt;br/&gt;To add a file to a support ticket, visit the &lt;a target&#x3D;&#39;_blank&#39; href&#x3D;&#39;https://portal.azure.com/#blade/Microsoft_Azure_Support/HelpAndSupportBlade/managesupportrequest&#39;&gt;Manage support ticket&lt;/a&gt; page in the Azure portal, select the support ticket, and use the file upload control to add a new file.

    :param support_ticket_name: Support ticket name
    :type support_ticket_name: str
    :param communication_name: Communication name
    :type communication_name: str
    :param subscription_id: Azure subscription id
    :type subscription_id: str
    :param api_version: Api version
    :type api_version: str
    :param create_communication_parameters: Communication object
    :type create_communication_parameters: dict | bytes

    """
    create_communication_parameters = CommunicationDetails.from_dict(create_communication_parameters)
    return web.Response(status=200)


async def communications_get(request: web.Request, support_ticket_name, communication_name, subscription_id, api_version) -> web.Response:
    """communications_get

    Returns details of a specific communication in a support ticket.

    :param support_ticket_name: Support ticket name
    :type support_ticket_name: str
    :param communication_name: Communication name
    :type communication_name: str
    :param subscription_id: Azure subscription id
    :type subscription_id: str
    :param api_version: Api version
    :type api_version: str

    """
    return web.Response(status=200)


async def communications_list(request: web.Request, support_ticket_name, subscription_id, api_version, top=None, filter=None) -> web.Response:
    """communications_list

    Lists all communications (attachments not included) for a support ticket. &lt;br/&gt;&lt;/br&gt; You can also filter support ticket communications by &lt;i&gt;CreatedDate&lt;/i&gt;�or &lt;i&gt;CommunicationType&lt;/i&gt; using the $filter parameter. The only type of communication supported today is &lt;i&gt;Web&lt;/i&gt;. Output will be a paged result with &lt;i&gt;nextLink&lt;/i&gt;, using which you can retrieve the next set of Communication results. &lt;br/&gt;&lt;br/&gt; Support ticket data is available for 12 months after ticket creation. If a ticket was created more than 12 months ago, a request for data might cause an error.

    :param support_ticket_name: Support ticket name
    :type support_ticket_name: str
    :param subscription_id: Azure subscription id
    :type subscription_id: str
    :param api_version: Api version
    :type api_version: str
    :param top: The number of values to return in the collection. Default is 10 and max is 10.
    :type top: int
    :param filter: The filter to apply on the operation. You can filter by communicationType and createdDate properties. CommunicationType supports Equals (&#39;eq&#39;) operator and createdDate supports Greater Than (&#39;gt&#39;) and Greater Than or Equals (&#39;ge&#39;) operators. You may combine the CommunicationType and CreatedDate filters by Logical And (&#39;and&#39;) operator.
    :type filter: str

    """
    return web.Response(status=200)
