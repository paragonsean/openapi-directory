from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_custom_class_request import CreateCustomClassRequest
from openapi_server.models.create_phrase_set_request import CreatePhraseSetRequest
from openapi_server.models.custom_class import CustomClass
from openapi_server.models.list_custom_classes_response import ListCustomClassesResponse
from openapi_server.models.list_phrase_set_response import ListPhraseSetResponse
from openapi_server.models.phrase_set import PhraseSet
from openapi_server import util


async def speech_projects_locations_custom_classes_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """speech_projects_locations_custom_classes_create

    Create a custom class.

    :param parent: Required. The parent resource where this custom class will be created. Format: &#x60;projects/{project}/locations/{location}/customClasses&#x60; Speech-to-Text supports three locations: &#x60;global&#x60;, &#x60;us&#x60; (US North America), and &#x60;eu&#x60; (Europe). If you are calling the &#x60;speech.googleapis.com&#x60; endpoint, use the &#x60;global&#x60; location. To specify a region, use a [regional endpoint](https://cloud.google.com/speech-to-text/docs/endpoints) with matching &#x60;us&#x60; or &#x60;eu&#x60; location value.
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateCustomClassRequest.from_dict(body)
    return web.Response(status=200)


async def speech_projects_locations_custom_classes_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """speech_projects_locations_custom_classes_list

    List custom classes.

    :param parent: Required. The parent, which owns this collection of custom classes. Format: &#x60;projects/{project}/locations/{location}/customClasses&#x60; Speech-to-Text supports three locations: &#x60;global&#x60;, &#x60;us&#x60; (US North America), and &#x60;eu&#x60; (Europe). If you are calling the &#x60;speech.googleapis.com&#x60; endpoint, use the &#x60;global&#x60; location. To specify a region, use a [regional endpoint](https://cloud.google.com/speech-to-text/docs/endpoints) with matching &#x60;us&#x60; or &#x60;eu&#x60; location value.
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param page_size: The maximum number of custom classes to return. The service may return fewer than this value. If unspecified, at most 50 custom classes will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.
    :type page_size: int
    :param page_token: A page token, received from a previous &#x60;ListCustomClass&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListCustomClass&#x60; must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def speech_projects_locations_phrase_sets_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """speech_projects_locations_phrase_sets_create

    Create a set of phrase hints. Each item in the set can be a single word or a multi-word phrase. The items in the PhraseSet are favored by the recognition model when you send a call that includes the PhraseSet.

    :param parent: Required. The parent resource where this phrase set will be created. Format: &#x60;projects/{project}/locations/{location}&#x60; Speech-to-Text supports three locations: &#x60;global&#x60;, &#x60;us&#x60; (US North America), and &#x60;eu&#x60; (Europe). If you are calling the &#x60;speech.googleapis.com&#x60; endpoint, use the &#x60;global&#x60; location. To specify a region, use a [regional endpoint](https://cloud.google.com/speech-to-text/docs/endpoints) with matching &#x60;us&#x60; or &#x60;eu&#x60; location value.
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreatePhraseSetRequest.from_dict(body)
    return web.Response(status=200)


async def speech_projects_locations_phrase_sets_delete(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """speech_projects_locations_phrase_sets_delete

    Delete a phrase set.

    :param name: Required. The name of the phrase set to delete. Format: &#x60;projects/{project}/locations/{location}/phraseSets/{phrase_set}&#x60;
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def speech_projects_locations_phrase_sets_get(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """speech_projects_locations_phrase_sets_get

    Get a phrase set.

    :param name: Required. The name of the phrase set to retrieve. Format: &#x60;projects/{project}/locations/{location}/phraseSets/{phrase_set}&#x60; Speech-to-Text supports three locations: &#x60;global&#x60;, &#x60;us&#x60; (US North America), and &#x60;eu&#x60; (Europe). If you are calling the &#x60;speech.googleapis.com&#x60; endpoint, use the &#x60;global&#x60; location. To specify a region, use a [regional endpoint](https://cloud.google.com/speech-to-text/docs/endpoints) with matching &#x60;us&#x60; or &#x60;eu&#x60; location value.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def speech_projects_locations_phrase_sets_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """speech_projects_locations_phrase_sets_list

    List phrase sets.

    :param parent: Required. The parent, which owns this collection of phrase set. Format: &#x60;projects/{project}/locations/{location}&#x60; Speech-to-Text supports three locations: &#x60;global&#x60;, &#x60;us&#x60; (US North America), and &#x60;eu&#x60; (Europe). If you are calling the &#x60;speech.googleapis.com&#x60; endpoint, use the &#x60;global&#x60; location. To specify a region, use a [regional endpoint](https://cloud.google.com/speech-to-text/docs/endpoints) with matching &#x60;us&#x60; or &#x60;eu&#x60; location value.
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param page_size: The maximum number of phrase sets to return. The service may return fewer than this value. If unspecified, at most 50 phrase sets will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.
    :type page_size: int
    :param page_token: A page token, received from a previous &#x60;ListPhraseSet&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListPhraseSet&#x60; must match the call that provided the page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def speech_projects_locations_phrase_sets_patch(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, update_mask=None, body=None) -> web.Response:
    """speech_projects_locations_phrase_sets_patch

    Update a phrase set.

    :param name: The resource name of the phrase set.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param update_mask: The list of fields to be updated.
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = PhraseSet.from_dict(body)
    return web.Response(status=200)
