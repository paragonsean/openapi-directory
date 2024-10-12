from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_name_availability_input import CheckNameAvailabilityInput
from openapi_server.models.check_name_availability_output import CheckNameAvailabilityOutput
from openapi_server.models.exception_response import ExceptionResponse
from openapi_server.models.support_ticket_details import SupportTicketDetails
from openapi_server.models.support_tickets_list_result import SupportTicketsListResult
from openapi_server.models.update_support_ticket import UpdateSupportTicket
from openapi_server import util


async def support_tickets_check_name_availability(request: web.Request, subscription_id, api_version, check_name_availability_input) -> web.Response:
    """support_tickets_check_name_availability

    Check the availability of a resource name. This API should to be used to check the uniqueness of the name for support ticket creation for the selected subscription.

    :param subscription_id: Azure subscription id
    :type subscription_id: str
    :param api_version: Api version
    :type api_version: str
    :param check_name_availability_input: Input to check.
    :type check_name_availability_input: dict | bytes

    """
    check_name_availability_input = CheckNameAvailabilityInput.from_dict(check_name_availability_input)
    return web.Response(status=200)


async def support_tickets_create(request: web.Request, support_ticket_name, subscription_id, api_version, create_support_ticket_parameters) -> web.Response:
    """support_tickets_create

    Creates a new support ticket for Quota increase, Technical, Billing, and Subscription Management issues for the specified subscription. &lt;br/&gt;&lt;br/&gt;A paid technical support plan is required to create a support ticket using this API. &lt;a href&#x3D;&#39;https://aka.ms/supportticketAPI&#39;&gt;Learn more&lt;/a&gt; &lt;br/&gt;&lt;br/&gt; Use the Services API to map the right Service Id to the issue type. For example: For billing tickets set *serviceId* to *&#39;/providers/Microsoft.Support/services/517f2da6-78fd-0498-4e22-ad26996b1dfc&#39;*. &lt;br/&gt; For Technical issues, the Service id will map to the Azure service you want to raise a support ticket for. &lt;br/&gt;&lt;br/&gt;Always call the Services and ProblemClassifications API to get the most recent set of services and problem categories required for support ticket creation.

    :param support_ticket_name: Support ticket name.
    :type support_ticket_name: str
    :param subscription_id: Azure subscription id
    :type subscription_id: str
    :param api_version: Api version
    :type api_version: str
    :param create_support_ticket_parameters: Support ticket request payload.
    :type create_support_ticket_parameters: dict | bytes

    """
    create_support_ticket_parameters = SupportTicketDetails.from_dict(create_support_ticket_parameters)
    return web.Response(status=200)


async def support_tickets_get(request: web.Request, support_ticket_name, subscription_id, api_version) -> web.Response:
    """support_tickets_get

    Gets details for a specific support ticket in an Azure subscription. &lt;br/&gt;&lt;br/&gt;Support ticket data is available for 12 months after ticket creation. If a ticket was created more than 12 months ago, a request for data might cause an error.

    :param support_ticket_name: Support ticket name
    :type support_ticket_name: str
    :param subscription_id: Azure subscription id
    :type subscription_id: str
    :param api_version: Api version
    :type api_version: str

    """
    return web.Response(status=200)


async def support_tickets_list(request: web.Request, subscription_id, api_version, top=None, filter=None) -> web.Response:
    """support_tickets_list

    Lists all the support tickets for an Azure subscription. &lt;br/&gt;&lt;br/&gt;You can also filter the support tickets by &lt;i&gt;Status&lt;/i&gt; or &lt;i&gt;CreatedDate&lt;/i&gt; using the $filter parameter. Output will be a paged result with &lt;i&gt;nextLink&lt;/i&gt;, using which you can retrieve the next set of support tickets. &lt;br/&gt;&lt;br/&gt;Support ticket data is available for 12 months after ticket creation. If a ticket was created more than 12 months ago, a request for data might cause an error.

    :param subscription_id: Azure subscription id
    :type subscription_id: str
    :param api_version: Api version
    :type api_version: str
    :param top: The number of values to return in the collection. Default is 25 and max is 100.
    :type top: int
    :param filter: The filter to apply on the operation. We support &#39;odata v4.0&#39; filter semantics. &lt;a target&#x3D;&#39;_blank&#39; href&#x3D;&#39;https://docs.microsoft.com/odata/concepts/queryoptions-overview&#39;&gt;Learn more&lt;/a&gt; &lt;br/&gt;&lt;i&gt;Status&lt;/i&gt; filter can only be used with &#39;eq&#39; operator. For &lt;i&gt;CreatedDate&lt;/i&gt; filter, the supported operators are &#39;gt&#39; and &#39;ge&#39;. When using both filters, combine them using the logical &#39;AND&#39;.
    :type filter: str

    """
    return web.Response(status=200)


async def support_tickets_update(request: web.Request, support_ticket_name, subscription_id, api_version, update_support_ticket) -> web.Response:
    """support_tickets_update

    This API allows you to update the severity level or your contact information in the support ticket. &lt;br/&gt;&lt;br/&gt; Note: The severity levels cannot be changed if a support ticket is actively being worked upon by an Azure support engineer. In such a case, contact your support engineer to request severity update by adding a new communication using the Communications API.

    :param support_ticket_name: Support ticket name
    :type support_ticket_name: str
    :param subscription_id: Azure subscription id
    :type subscription_id: str
    :param api_version: Api version
    :type api_version: str
    :param update_support_ticket: UpdateSupportTicket object
    :type update_support_ticket: dict | bytes

    """
    update_support_ticket = UpdateSupportTicket.from_dict(update_support_ticket)
    return web.Response(status=200)
