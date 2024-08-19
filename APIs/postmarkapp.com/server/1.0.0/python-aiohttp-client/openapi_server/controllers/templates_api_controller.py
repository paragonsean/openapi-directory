from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_template_request import CreateTemplateRequest
from openapi_server.models.edit_template_request import EditTemplateRequest
from openapi_server.models.email_with_template_request import EmailWithTemplateRequest
from openapi_server.models.send_email_response import SendEmailResponse
from openapi_server.models.send_email_templated_batch_request import SendEmailTemplatedBatchRequest
from openapi_server.models.standard_postmark_response import StandardPostmarkResponse
from openapi_server.models.template_detail_response import TemplateDetailResponse
from openapi_server.models.template_listing_response import TemplateListingResponse
from openapi_server.models.template_record_response import TemplateRecordResponse
from openapi_server.models.template_validation_request import TemplateValidationRequest
from openapi_server.models.template_validation_response import TemplateValidationResponse
from openapi_server import util


async def delete_template(request: web.Request, x_postmark_server_token, template_id_or_alias) -> web.Response:
    """Delete a Template

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param template_id_or_alias: The &#39;TemplateID&#39; or &#39;Alias&#39; value for the Template you wish to delete.
    :type template_id_or_alias: str

    """
    return web.Response(status=200)


async def get_single_template(request: web.Request, x_postmark_server_token, template_id_or_alias) -> web.Response:
    """Get a Template

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param template_id_or_alias: The &#39;TemplateID&#39; or &#39;Alias&#39; value for the Template you wish to retrieve.
    :type template_id_or_alias: str

    """
    return web.Response(status=200)


async def list_templates(request: web.Request, x_postmark_server_token, count, offset) -> web.Response:
    """Get the Templates associated with this Server

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param count: The number of Templates to return
    :type count: 
    :param offset: The number of Templates to \&quot;skip\&quot; before returning results.
    :type offset: 

    """
    return web.Response(status=200)


async def send_email_batch_with_templates_0(request: web.Request, x_postmark_server_token, body) -> web.Response:
    """Send a batch of email using templates.

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = SendEmailTemplatedBatchRequest.from_dict(body)
    return web.Response(status=200)


async def send_email_with_template_0(request: web.Request, x_postmark_server_token, body) -> web.Response:
    """Send an email using a Template

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = EmailWithTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def templates_post(request: web.Request, x_postmark_server_token, body) -> web.Response:
    """Create a Template

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def test_template_content(request: web.Request, x_postmark_server_token, body=None) -> web.Response:
    """Test Template Content

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = TemplateValidationRequest.from_dict(body)
    return web.Response(status=200)


async def update_template(request: web.Request, x_postmark_server_token, template_id_or_alias, body) -> web.Response:
    """Update a Template

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param template_id_or_alias: The &#39;TemplateID&#39; or &#39;Alias&#39; value for the Template you wish to update.
    :type template_id_or_alias: str
    :param body: 
    :type body: dict | bytes

    """
    body = EditTemplateRequest.from_dict(body)
    return web.Response(status=200)
