from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_system_information200_response import GetSystemInformation200Response
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server import util


async def get_system_information(request: web.Request, ) -> web.Response:
    """Get system information

    This endpoint allows you to get the version and the edition of the PIM. Example of what you can get &lt;table class&#x3D;\&quot;description-table\&quot;&gt; &lt;thead&gt; &lt;tr&gt; &lt;th align&#x3D;\&quot;center\&quot;&gt;Environment&lt;/th&gt; &lt;th align&#x3D;\&quot;center\&quot;&gt;Edition&lt;/th&gt; &lt;th align&#x3D;\&quot;center\&quot;&gt;Version&lt;/th&gt; &lt;/tr&gt; &lt;/thead&gt; &lt;tbody&gt; &lt;tr&gt; &lt;td align&#x3D;\&quot;center\&quot;&gt;SaaS EE&lt;/td&gt; &lt;td align&#x3D;\&quot;center\&quot;&gt;Serenity&lt;/td&gt; &lt;td align&#x3D;\&quot;center\&quot;&gt;v20230112013744&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt; &lt;td align&#x3D;\&quot;center\&quot;&gt;SaaS CE&lt;/td&gt; &lt;td align&#x3D;\&quot;center\&quot;&gt;GE&lt;/td&gt; &lt;td align&#x3D;\&quot;center\&quot;&gt;v20210526040645&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt; &lt;td align&#x3D;\&quot;center\&quot;&gt;PaaS or onPrem EE&lt;/td&gt; &lt;td align&#x3D;\&quot;center\&quot;&gt;EE&lt;/td&gt; &lt;td align&#x3D;\&quot;center\&quot;&gt;5.0.28&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt; &lt;td align&#x3D;\&quot;center\&quot;&gt;PaaS or onPrem CE&lt;/td&gt; &lt;td align&#x3D;\&quot;center\&quot;&gt;CE&lt;/td&gt; &lt;td align&#x3D;\&quot;center\&quot;&gt;5.0.28&lt;/td&gt; &lt;/tr&gt; &lt;/tbody&gt; &lt;/table&gt;


    """
    return web.Response(status=200)
