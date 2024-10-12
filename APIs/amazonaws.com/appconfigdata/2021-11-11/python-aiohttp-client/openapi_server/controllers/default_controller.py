from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_latest_configuration_response import GetLatestConfigurationResponse
from openapi_server.models.start_configuration_session_request import StartConfigurationSessionRequest
from openapi_server.models.start_configuration_session_response import StartConfigurationSessionResponse
from openapi_server import util


async def get_latest_configuration(request: web.Request, configuration_token, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_latest_configuration

    &lt;p&gt;Retrieves the latest deployed configuration. This API may return empty configuration data if the client already has the latest version. For more information about this API action and to view example CLI commands that show how to use it with the &lt;a&gt;StartConfigurationSession&lt;/a&gt; API action, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-retrieving-the-configuration\&quot;&gt;Retrieving the configuration&lt;/a&gt; in the &lt;i&gt;AppConfig User Guide&lt;/i&gt;. &lt;/p&gt; &lt;important&gt; &lt;p&gt;Note the following important information.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Each configuration token is only valid for one call to &lt;code&gt;GetLatestConfiguration&lt;/code&gt;. The &lt;code&gt;GetLatestConfiguration&lt;/code&gt; response includes a &lt;code&gt;NextPollConfigurationToken&lt;/code&gt; that should always replace the token used for the just-completed call in preparation for the next one. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GetLatestConfiguration&lt;/code&gt; is a priced call. For more information, see &lt;a href&#x3D;\&quot;https://aws.amazon.com/systems-manager/pricing/\&quot;&gt;Pricing&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/important&gt;

    :param configuration_token: &lt;p&gt;Token describing the current state of the configuration session. To obtain a token, first call the &lt;a&gt;StartConfigurationSession&lt;/a&gt; API. Note that every call to &lt;code&gt;GetLatestConfiguration&lt;/code&gt; will return a new &lt;code&gt;ConfigurationToken&lt;/code&gt; (&lt;code&gt;NextPollConfigurationToken&lt;/code&gt; in the response) and &lt;i&gt;must&lt;/i&gt; be provided to subsequent &lt;code&gt;GetLatestConfiguration&lt;/code&gt; API calls.&lt;/p&gt; &lt;important&gt; &lt;p&gt;This token should only be used once. To support long poll use cases, the token is valid for up to 24 hours. If a &lt;code&gt;GetLatestConfiguration&lt;/code&gt; call uses an expired token, the system returns &lt;code&gt;BadRequestException&lt;/code&gt;.&lt;/p&gt; &lt;/important&gt;
    :type configuration_token: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def start_configuration_session(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_configuration_session

    Starts a configuration session used to retrieve a deployed configuration. For more information about this API action and to view example CLI commands that show how to use it with the &lt;a&gt;GetLatestConfiguration&lt;/a&gt; API action, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-retrieving-the-configuration\&quot;&gt;Retrieving the configuration&lt;/a&gt; in the &lt;i&gt;AppConfig User Guide&lt;/i&gt;. 

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StartConfigurationSessionRequest.from_dict(body)
    return web.Response(status=200)
