from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.s3_config import S3Config
from openapi_server.models.s3_config_create_request import S3ConfigCreateRequest
from openapi_server.models.s3_config_update_request import S3ConfigUpdateRequest
from openapi_server.models.s3_tag import S3Tag
from openapi_server.models.s3_tag_create_request import S3TagCreateRequest
from openapi_server.models.s3_tag_list import S3TagList
from openapi_server import util


async def create_s3_config(request: web.Request, body, x_sds_auth_token=None) -> web.Response:
    """Create S3 storage configuration

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.3.0&lt;/h3&gt;  ### Description:   Create new S3 configuration.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: New S3 configuration is created.  ### Further Information: Forbidden characters in bucket names: [&#x60;.&#x60;]   &#x60;bucketName&#x60; and &#x60;endpointUrl&#x60; are deprecated, use &#x60;bucketUrl&#x60; instead.  ### Virtual hosted style access  Example: https://&lt;span style&#x3D;\&quot;color:red;\&quot;&gt;bucket-name&lt;/span&gt;.s3.&lt;span style&#x3D;\&quot;color:red;\&quot;&gt;region&lt;/span&gt;.amazonaws.com/&lt;span style&#x3D;\&quot;color:red;\&quot;&gt;key-name&lt;/span&gt; 

    :param body: 
    :type body: dict | bytes
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = S3ConfigCreateRequest.from_dict(body)
    return web.Response(status=200)


async def create_s3_tag(request: web.Request, body, x_sds_auth_token=None) -> web.Response:
    """Create S3 tag

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.9.0&lt;/h3&gt;  ### Description:   Create new S3 tag.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: New S3 tag is created.  ### Further Information: * Maximum key length: **128** characters.   * Maximum value length: **256** characters.   * Both S3 tag key and value are **case-sensitive** strings.   * Maximum of **20 mandatory S3 tags** is allowed.

    :param body: 
    :type body: dict | bytes
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = S3TagCreateRequest.from_dict(body)
    return web.Response(status=200)


async def remove_s3_tag(request: web.Request, id, x_sds_auth_token=None) -> web.Response:
    """Remove S3 tag

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.9.0&lt;/h3&gt;  ### Description:   Delete S3 tag.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: S3 tag gets deleted.  ### Further Information: None.

    :param id: S3 tag ID
    :type id: int
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request3_config(request: web.Request, x_sds_auth_token=None) -> web.Response:
    """Request S3 storage configuration

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.3.0&lt;/h3&gt;  ### Description:   Retrieve S3 configuration.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: S3 configuration is returned.  ### Further Information: None.  ### Virtual hosted style access  Example: https://&lt;span style&#x3D;\&quot;color:red;\&quot;&gt;bucket-name&lt;/span&gt;.s3.&lt;span style&#x3D;\&quot;color:red;\&quot;&gt;region&lt;/span&gt;.amazonaws.com/&lt;span style&#x3D;\&quot;color:red;\&quot;&gt;key-name&lt;/span&gt; 

    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_s3_tag(request: web.Request, id, x_sds_auth_token=None) -> web.Response:
    """Request S3 tag

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.9.0&lt;/h3&gt;  ### Description:   Retrieve single S3 tag.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: S3 tag is returned.  ### Further Information: None.

    :param id: S3 tag ID
    :type id: int
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_s3_tag_list(request: web.Request, x_sds_auth_token=None) -> web.Response:
    """Request list of configured S3 tags

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.9.0&lt;/h3&gt;  ### Description:   Retrieve all configured S3 tags.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: S3 tags are returned.  ### Further Information: An empty list is returned if no S3 tags are found / configured.

    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def update_s3_config(request: web.Request, body, x_sds_auth_token=None) -> web.Response:
    """Update S3 storage configuration

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.3.0&lt;/h3&gt;  ### Description:   Update existing S3 configuration.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: S3 configuration is updated.  ### Further Information: Forbidden characters in bucket names: [&#x60;.&#x60;]   &#x60;bucketName&#x60; and &#x60;endpointUrl&#x60; are deprecated, use &#x60;bucketUrl&#x60; instead.  ### Virtual hosted style access  Example: https://&lt;span style&#x3D;\&quot;color:red;\&quot;&gt;bucket-name&lt;/span&gt;.s3.&lt;span style&#x3D;\&quot;color:red;\&quot;&gt;region&lt;/span&gt;.amazonaws.com/&lt;span style&#x3D;\&quot;color:red;\&quot;&gt;key-name&lt;/span&gt; 

    :param body: 
    :type body: dict | bytes
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = S3ConfigUpdateRequest.from_dict(body)
    return web.Response(status=200)
