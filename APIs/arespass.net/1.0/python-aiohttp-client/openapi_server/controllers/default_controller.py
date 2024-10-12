from typing import List, Dict
from aiohttp import web

from openapi_server.models.about import About
from openapi_server.models.ec import Ec
from openapi_server import util


async def about_get(request: web.Request, output_format=None) -> web.Response:
    """Metadata about this API&amp;#58; version number, release date and available languages.  Metadata requests are NOT billed. 

    

    :param output_format: **The format of the returned metadata.**  Allowed values are *json*, *xml* and *yaml*.  The default value is *xml*. 
    :type output_format: str

    """
    return web.Response(status=200)


async def ec_get(request: web.Request, password, output_format=None, penalty=None, req_id=None) -> web.Response:
    """The entropy calculator - alias ec -, analyzes a password and calculates its entropy.  Entropy calculator requests are billed. 

    

    :param password: **The password to be analyzed.**  Minimum length is 4 characters; maximum length is 128 characters.  Beware that certain characters like &#39;&amp;#35;&#39;, &#39;&amp;#61;&#39; or &#39;&amp;#63;&#39; must be properly encoded.  For more information about this issue, please refer to RFC 3986 (\&quot;*Uniform Resource Identifier (URI): Generic Syntax*\&quot;), sections 2.1, 2.2 and 2.4. 
    :type password: str
    :param output_format: **The format of the returned analysis.**  Allowed values are *json*, *xml* and *yaml*.  The default value is *xml*. 
    :type output_format: str
    :param penalty: **The penalty applied to each character that is part of a word, number sequence, alphabet sequence, etc.**  The penalty is a float number in the range [0, 1]. Full penalty, 0; no penalty, 1.  The character used as decimal separator is always &#39;&amp;#46;&#39;. Hence, a parameter value like *0,33* would be illegal.  The default value is *0.25*. 
    :type penalty: 
    :param req_id: **An identifier for this request.**  The request identifier is a string that must match the regular expression */(?i)^[a-z0-9]{8,16}$/*.  This identifier is echoed in the returned response. Its value has no effect on the password analysis.  If this parameter is unset, a randomly generated identifier will be automatically assigned to this request. 
    :type req_id: str

    """
    return web.Response(status=200)
