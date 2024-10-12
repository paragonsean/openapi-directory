from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def list_available_content_blocks(request: web.Request, modified_after=None, modified_before=None, limit=None, offset=None) -> web.Response:
    """List Available Content Blocks

    This endpoint will list existing Content Block information.  ### Successful Response Properties &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR_REST_API_KEY {   \&quot;count\&quot;: \&quot;integer\&quot;,   \&quot;content_blocks\&quot;: [     {       \&quot;content_block_id\&quot;: \&quot;string\&quot;,       \&quot;name\&quot;: \&quot;string\&quot;,       \&quot;content_type\&quot;: \&quot;html or text\&quot;,       \&quot;liquid_tag\&quot;: \&quot;string\&quot;,       \&quot;inclusion_count\&quot; : \&quot;integer\&quot;,       \&quot;created_at\&quot;: \&quot;time-in-iso\&quot;,       \&quot;last_edited\&quot;: \&quot;time-in-iso\&quot;,       \&quot;tags\&quot; : \&quot;array of strings\&quot;     }   ] } &#x60;&#x60;&#x60;  ### Possible Errors - &#x60;Modified after time is invalid.&#x60; The date you have provided is not a valid or parsable date. Please reformat this value as a string in ISO 8601 format (&#x60;yyyy-mm-ddThh:mm:ss.ffffff&#x60;).  - &#x60;Modified before time is invalid.&#x60; The date you have provided is not a valid or parsable date. Please reformat this value as a string in ISO 8601 format (&#x60;yyyy-mm-ddThh:mm:ss.ffffff&#x60;).  - &#x60;Modified after time must be earlier than or the same as modified before time.&#x60;  - &#x60;Content Block number limit is invalid.&#x60; The &#x60;limit&#x60; parameter must be an integer (positive number) greater than 0.  - &#x60;Content Block number limit must be greater than 0.&#x60; The &#x60;limit&#x60; parameter must be an integer (positive number) greater than 0.  - &#x60;Content Block number limit exceeds maximum of 1000.&#x60; The &#x60;limit&#x60; parameter must be an integer (positive number) greater than 0.  - &#x60;Offset is invalid.&#x60; The &#x60;offset&#x60; parameter must be an integer (positive number) greater than 0.  - &#x60;Offset must be greater than 0.&#x60; The &#x60;offset&#x60; parameter must be an integer (positive number) greater than 0.

    :param modified_after: (Optional) String in ISO 8601  Retrieve only content blocks updated at or after the given time.
    :type modified_after: str
    :param modified_before: (Optional) String in ISO 8601  Retrieve only content blocks updated at or before the given time.
    :type modified_before: str
    :param limit: (Optional) Positive Number  Maximum number of content blocks to retrieve, default to 100 if not provided, maximum acceptable value is 1000.
    :type limit: str
    :param offset: (Optional) Positive Number  Number of content blocks to skip before returning rest of the templates that fit the search criteria.
    :type offset: str

    """
    return web.Response(status=200)


async def list_available_email_templates(request: web.Request, modified_after=None, modified_before=None, limit=None, offset=None) -> web.Response:
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


async def see_content_block_information(request: web.Request, content_block_id=None, include_inclusion_data=None) -> web.Response:
    """See Content Block Information

    This endpoint will call information for an existing Content Block.  ### Successful Response Properties &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR_REST_API_KEY {   \&quot;content_block_id\&quot;: \&quot;string\&quot;,   \&quot;name\&quot;: \&quot;string\&quot;,   \&quot;content\&quot;: \&quot;string\&quot;,   \&quot;description\&quot;: \&quot;string\&quot;,   \&quot;content_type\&quot;: \&quot;html or text\&quot;,   \&quot;tags\&quot;:  \&quot;array of strings\&quot;,   \&quot;created_at\&quot;: \&quot;time-in-iso\&quot;,   \&quot;last_edited\&quot;: \&quot;time-in-iso\&quot;,   \&quot;inclusion_count\&quot; : \&quot;integer\&quot;,   \&quot;message\&quot;: \&quot;success\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - &#x60;Content Block ID cannot be blank.&#x60; - A Content Block has not been listed or is not encapsulated in quotes.  - &#x60;Content Block ID is invalid for this App Group.&#x60; - This Content Block does not exist or is in a different company account or app group.  - &#x60;Content Block has been deleted - content not available.&#x60; - This Content Block, though it may have existed earlier, has been deleted.  - &#x60;Include Inclusion Data - error&#x60; - One of true or false is not provided.

    :param content_block_id: (Required) String  The Content Block ID. This can be found by either listing Content Block information or going to the Developer Console, then API Settings, then scrolling to the bottom and searching for your Content Block API Identifier.
    :type content_block_id: str
    :param include_inclusion_data: (Optional) Boolean  When set to ‘true’, the API returns back the Message Variation API ID of Campaigns and Canvases where this content block is included, to be used in subsequent calls. The results exclude archived or deleted Campaigns or Canvases.
    :type include_inclusion_data: str

    """
    return web.Response(status=200)


async def see_email_template_information(request: web.Request, email_template_id=None) -> web.Response:
    """See Email Template Information

    Use to get information on your email templates.  Use the Template REST APIs to programmatically manage the email templates that you have stored on the Braze dashboard, on the Templates &amp; Media page. Braze provides two endpoints for creating and updating your email templates.  ### Request Components - [Template Identifier](https://www.braze.com/docs/api/identifier_types/)

    :param email_template_id: (Required) String  Your email template&#39;s API Identifier.
    :type email_template_id: str

    """
    return web.Response(status=200)
