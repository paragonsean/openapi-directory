from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def list_available_email_templates_0(request: web.Request, modified_after=None, modified_before=None, limit=None, offset=None) -> web.Response:
    """List Available Email Templates

    Use this endpoint to get a list of available templates in your Braze account.  Use the Template REST APIs to programmatically manage the email templates that you have stored on the Braze dashboard, on the Templates &amp; Media page. Braze provides two endpoints for creating and updating your email templates.  ### Successful Response Properties &#x60;&#x60;&#x60;json {   \&quot;count\&quot;: number of templates returned   \&quot;templates\&quot;: [template with the following properties]:     \&quot;email_template_id\&quot;: (string) your email template&#39;s API Identifier,     \&quot;template_name\&quot;: (string) the name of your email template,     \&quot;created_at\&quot;: (string, in ISO 8601),     \&quot;updated_at\&quot;: (string, in ISO 8601),     \&quot;tags\&quot;: (array of strings) tags appended to the template }   &#x60;&#x60;&#x60;

    :param modified_after: (Optional) String in ISO 8601  Retrieve only templates updated at or after the given time.
    :type modified_after: str
    :param modified_before: (Optional) String in ISO 8601  Retrieve only templates updated at or before the given time
    :type modified_before: str
    :param limit: (Optional) Positive Number  Maximum number of templates to retrieve, default to 100 if not provided, maximum acceptable value is 1000.
    :type limit: str
    :param offset: (Optional) Positive Number  Number of templates to skip before returning rest of the templates that fit the search criteria.
    :type offset: str

    """
    return web.Response(status=200)


async def see_email_template_information_0(request: web.Request, email_template_id=None) -> web.Response:
    """See Email Template Information

    Use to get information on your email templates.  Use the Template REST APIs to programmatically manage the email templates that you have stored on the Braze dashboard, on the Templates &amp; Media page. Braze provides two endpoints for creating and updating your email templates.  ### Request Components - [Template Identifier](https://www.braze.com/docs/api/identifier_types/)

    :param email_template_id: (Required) String  Your email template&#39;s API Identifier.
    :type email_template_id: str

    """
    return web.Response(status=200)
