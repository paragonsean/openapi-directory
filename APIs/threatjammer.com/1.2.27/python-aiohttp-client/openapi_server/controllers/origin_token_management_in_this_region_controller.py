from typing import List, Dict
from aiohttp import web

from openapi_server.models.body_delete_token_v1_origin_token_delete import BodyDeleteTokenV1OriginTokenDelete
from openapi_server.models.body_disable_origin_token_v1_origin_token_disable_put import BodyDisableOriginTokenV1OriginTokenDisablePut
from openapi_server.models.body_enable_origin_token_v1_origin_token_enable_put import BodyEnableOriginTokenV1OriginTokenEnablePut
from openapi_server.models.body_query_origin_token_info_v1_origin_token_post import BodyQueryOriginTokenInfoV1OriginTokenPost
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.origin_token_collection_output import OriginTokenCollectionOutput
from openapi_server.models.origin_token_input import OriginTokenInput
from openapi_server.models.origin_token_output import OriginTokenOutput
from openapi_server import util


async def create_a_new_origin_token_v1_origin_token_new_post(request: web.Request, body) -> web.Response:
    """Create an origin token of the user in the region.

    ### What Creates a new origin token for the user passing as argument the origin. The origin parameter is the protocol and the domain where the origin token is valid.  The origin token is a special key used in conjunction with javascript library used for abuse detection. This key is owned by the user and is used to identify the origin of the request.  Hence, the protocol and domain of the origin must be the one where the javascript is loaded.  ### Parameters The origin with the protocol and domain is required in the body of the request in the parameter &#x60;&#x60;origin&#x60;&#x60;. The allowed protocols are &#x60;&#x60;https://&#x60;&#x60;, and &#x60;&#x60;http://&#x60;&#x60;.  ### Result The result is a JSON object with the new origin token and the following fields: - &#x60;&#x60;self&#x60;&#x60;: the URI to individual origin token information. - &#x60;&#x60;region_id&#x60;&#x60;: the name of the region where the origin token is valid. - &#x60;&#x60;origin&#x60;&#x60;: the protocol and the domain where the origin token is valid. - &#x60;&#x60;status&#x60;&#x60;: the status of the origin token. The only allowed values are &#x60;&#x60;ENABLED&#x60;&#x60; and &#x60;&#x60;DISABLED&#x60;&#x60;. - &#x60;&#x60;created_at&#x60;&#x60;: the date and time when the origin token was created in UNIX timestamp in milliseconds. - &#x60;&#x60;updated_at&#x60;&#x60;: the date and time when the origin token was last updated in UNIX timestamp in milliseconds.  ### Errors It will return the API Global errors described in the API description.  It will also return the following errors: - a &#x60;400 Bad Request&#x60; error if the origin does not have the correct format. - a &#x60;409 Conflict&#x60; error if the origin token already exists.

    :param body: 
    :type body: dict | bytes

    """
    body = OriginTokenInput.from_dict(body)
    return web.Response(status=200)


async def delete_token_v1_origin_token_delete(request: web.Request, body) -> web.Response:
    """Delete an origin token of the user in the region.

    ### What Deletes the origin token passed as argument of the user in the selected region. Once the token is deleted, it will no longer be valid and the protocol and domain of the origin will no longer be under protection.  To delete an origin token, the user must be the owner and the token must be &#x60;&#x60;DISABLED&#x60;&#x60; first.  ### Parameters The Origin Token is required in the body of the request in the parameter &#x60;origin_token_id&#x60;.  ### Result If successful, the result will be an empty response with a status code of &#x60;204 No Content&#x60;.  ### Errors It will return the API Global errors described in the API description.  It will also return the following errors: - a &#x60;404 Not Found&#x60; error if the origin token is not found. - a &#x60;409 Conflict&#x60; error if the origin token is not disabled.

    :param body: 
    :type body: dict | bytes

    """
    body = BodyDeleteTokenV1OriginTokenDelete.from_dict(body)
    return web.Response(status=200)


async def disable_origin_token_v1_origin_token_disable_put(request: web.Request, body) -> web.Response:
    """Disable a enabled origin token of the user in the region.

    ### What Disable an enabled origin token passed as argument of the user in the selected region. When a token is enabled, it will participate in the protection of the origin protocol and domain. If the token is disabled, it will not participate in the protection of the origin protocol and domain.  To disable an origin token, the user must be the owner. If the token is already disabled, the function will not perform any action. If the token is enabled, it will be disabled.  ### Parameters The Origin Token is required in the body of the request in the parameter &#x60;origin_token_id&#x60;.  ### Result If successful, the result will be an empty response with a status code of &#x60;204 No Content&#x60;.  ### Errors It will return the API Global errors described in the API description.  It will also return the following errors: - a &#x60;404 Not Found&#x60; error if the origin token is not found.

    :param body: 
    :type body: dict | bytes

    """
    body = BodyDisableOriginTokenV1OriginTokenDisablePut.from_dict(body)
    return web.Response(status=200)


async def enable_origin_token_v1_origin_token_enable_put(request: web.Request, body) -> web.Response:
    """Enable a disabled origin token of the user in the region.

    ### What Enable a disabled origin token passed as argument of the user in the selected region. When a token is enabled, it will participate in the protection of the origin protocol and domain. If the token is disabled, it will not participate in the protection of the origin protocol and domain.  To enable an origin token, the user must be the owner. If the token is already enabled, the function will not perform any action. If the token is disabled, it will be enabled.  ### Parameters The Origin Token is required in the body of the request in the parameter &#x60;origin_token_id&#x60;.  ### Result If successful, the result will be an empty response with a status code of &#x60;204 No Content&#x60;.  ### Errors It will return the API Global errors described in the API description.  It will also return the following errors: - a &#x60;404 Not Found&#x60; error if the origin token is not found.

    :param body: 
    :type body: dict | bytes

    """
    body = BodyEnableOriginTokenV1OriginTokenEnablePut.from_dict(body)
    return web.Response(status=200)


async def query_all_origin_tokens_in_the_region_v1_origin_token_all_get(request: web.Request, ) -> web.Response:
    """Get the information of the origin tokens of the user in the region.

    ### What Obtain the attributes of all the origin tokens of the user in the selected region. The purpose of this function is to show what protocol and domain is linked to all the tokens.  The origin token is a special key used in conjunction with javascript library used for abuse detection. This key is owned by the user and is used to identify the origin of the request.  Hence, the protocol and domain of the origin must be the one where the javascript is loaded.  ### Parameters No parameters are required.  ### Result The result is a list of JSON objects with the following fields: - &#x60;&#x60;self&#x60;&#x60;: the URI to individual origin token information. - &#x60;&#x60;region_id&#x60;&#x60;: the name of the region where the origin token is valid. - &#x60;&#x60;origin&#x60;&#x60;: the protocol and the domain where the origin token is valid. - &#x60;&#x60;status&#x60;&#x60;: the status of the origin token. The only allowed values are &#x60;&#x60;ENABLED&#x60;&#x60; and &#x60;&#x60;DISABLED&#x60;&#x60;. - &#x60;&#x60;created_at&#x60;&#x60;: the date and time when the origin token was created in UNIX timestamp in milliseconds. - &#x60;&#x60;updated_at&#x60;&#x60;: the date and time when the origin token was last updated in UNIX timestamp in milliseconds.  ### Errors It will return the API Global errors described in the API description.


    """
    return web.Response(status=200)


async def query_origin_token_info_v1_origin_token_post(request: web.Request, body) -> web.Response:
    """Get the information of an origin token of the user in the region.

    ### What Obtain the attributes of the given origin token of the user in the selected region. The purpose of this function is to show what protocol and domain is linked to the token.  The origin token is a special key used in conjunction with javascript library used for abuse detection. This key is owned by the user and is used to identify the origin of the request.  Hence, the protocol and domain of the origin must be the one where the javascript is loaded.  ### Parameters The Origin Token is required in the body of the request in the parameter &#x60;origin_token_id&#x60;.  ### Result The result is a JSON object with the following fields: - &#x60;&#x60;self&#x60;&#x60;: the URI to individual origin token information. - &#x60;&#x60;region_id&#x60;&#x60;: the name of the region where the origin token is valid. - &#x60;&#x60;origin&#x60;&#x60;: the protocol and the domain where the origin token is valid. - &#x60;&#x60;status&#x60;&#x60;: the status of the origin token. The only allowed values are &#x60;&#x60;ENABLED&#x60;&#x60; and &#x60;&#x60;DISABLED&#x60;&#x60;. - &#x60;&#x60;created_at&#x60;&#x60;: the date and time when the origin token was created in UNIX timestamp in milliseconds. - &#x60;&#x60;updated_at&#x60;&#x60;: the date and time when the origin token was last updated in UNIX timestamp in milliseconds.  ### Errors It will return the API Global errors described in the API description.

    :param body: 
    :type body: dict | bytes

    """
    body = BodyQueryOriginTokenInfoV1OriginTokenPost.from_dict(body)
    return web.Response(status=200)
