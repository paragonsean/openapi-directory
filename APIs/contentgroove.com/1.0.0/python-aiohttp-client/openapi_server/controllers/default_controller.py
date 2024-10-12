from typing import List, Dict
from aiohttp import web

from openapi_server.models.clip_response_object import ClipResponseObject
from openapi_server.models.clips_response_object import ClipsResponseObject
from openapi_server.models.create_clip_request import CreateClipRequest
from openapi_server.models.create_media_request import CreateMediaRequest
from openapi_server.models.create_webhook_subscription_request import CreateWebhookSubscriptionRequest
from openapi_server.models.direct_upload_response_object import DirectUploadResponseObject
from openapi_server.models.media_response_object import MediaResponseObject
from openapi_server.models.medias_response_object import MediasResponseObject
from openapi_server.models.payment_required_error_response_object import PaymentRequiredErrorResponseObject
from openapi_server.models.too_many_requests_error_response_object import TooManyRequestsErrorResponseObject
from openapi_server.models.unauthorized_error_response_object import UnauthorizedErrorResponseObject
from openapi_server.models.update_clip_by_id_request import UpdateClipByIdRequest
from openapi_server.models.update_media_by_id_request import UpdateMediaByIdRequest
from openapi_server.models.webhook_subscription_response_object import WebhookSubscriptionResponseObject
from openapi_server.models.webhook_subscriptions_response_object import WebhookSubscriptionsResponseObject
from openapi_server import util


async def create_clip(request: web.Request, body) -> web.Response:
    """create clip

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateClipRequest.from_dict(body)
    return web.Response(status=200)


async def create_media(request: web.Request, body) -> web.Response:
    """create media

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateMediaRequest.from_dict(body)
    return web.Response(status=200)


async def create_webhook_subscription(request: web.Request, body) -> web.Response:
    """create webhook subscription

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateWebhookSubscriptionRequest.from_dict(body)
    return web.Response(status=200)


async def delete_clip_by_id(request: web.Request, id) -> web.Response:
    """delete clip

    

    :param id: The id of the clip to be retrieved
    :type id: str

    """
    return web.Response(status=200)


async def delete_media_by_id(request: web.Request, id) -> web.Response:
    """delete media

    

    :param id: id
    :type id: str

    """
    return web.Response(status=200)


async def delete_webhook_subscription_by_id(request: web.Request, id) -> web.Response:
    """delete webhook subscription

    

    :param id: The id of the webhook subscription to be retrieved
    :type id: str

    """
    return web.Response(status=200)


async def get_clip_by_id(request: web.Request, id) -> web.Response:
    """show clip

    

    :param id: The id of the clip to be retrieved
    :type id: str

    """
    return web.Response(status=200)


async def get_clips(request: web.Request, filter=None, page=None, sort=None) -> web.Response:
    """list clips

    

    :param filter: Filters to be applied to the query.  Query params in the url must look like this: \&quot;filter[attributeName_*matcher*]\&quot;  (i.e. filter[name_eq]&#x3D;chimp%20into%20space)  Available matchers can be found here: https://activerecord-hackery.github.io/ransack/getting-started/search-matches/  
    :type filter: dict | bytes
    :type filter: Dict[str, ]
    :param page: Specify page number and page size for the query
    :type page: dict | bytes
    :type page: Dict[str, ]
    :param sort: Sorting to be applied to the query. For more info: https://jsonapi.org/format/#fetching-sorting
    :type sort: str

    """
    filter = .from_dict(filter)
    page = .from_dict(page)
    return web.Response(status=200)


async def get_media_by_id(request: web.Request, id) -> web.Response:
    """show media

    

    :param id: id
    :type id: str

    """
    return web.Response(status=200)


async def get_medias(request: web.Request, filter=None, page=None, sort=None) -> web.Response:
    """list medias

    

    :param filter: Filters to be applied to the query.  Query params in the url must look like this: \&quot;filter[attributeName_*matcher*]\&quot;  (i.e. filter[name_eq]&#x3D;chimp%20into%20space)  Available matchers can be found here: https://activerecord-hackery.github.io/ransack/getting-started/search-matches/  
    :type filter: dict | bytes
    :type filter: Dict[str, ]
    :param page: Specify page number and page size for the query
    :type page: dict | bytes
    :type page: Dict[str, ]
    :param sort: Sorting to be applied to the query. For more info: https://jsonapi.org/format/#fetching-sorting
    :type sort: str

    """
    filter = .from_dict(filter)
    page = .from_dict(page)
    return web.Response(status=200)


async def get_upload_url(request: web.Request, ) -> web.Response:
    """prepare presigned upload url

    


    """
    return web.Response(status=200)


async def get_webhook_subscription_by_id(request: web.Request, id) -> web.Response:
    """show webhook subscription

    

    :param id: The id of the webhook subscription to be retrieved
    :type id: str

    """
    return web.Response(status=200)


async def get_webhook_subscriptions(request: web.Request, filter=None, sort=None) -> web.Response:
    """list webhook subscriptions

    

    :param filter: Filters to be applied to the query.  Query params in the url must look like this: \&quot;filter[attributeName_*matcher*]\&quot;  (i.e. filter[name_eq]&#x3D;chimp%20into%20space)  Available matchers can be found here: https://activerecord-hackery.github.io/ransack/getting-started/search-matches/  
    :type filter: dict | bytes
    :type filter: Dict[str, ]
    :param sort: Sorting to be applied to the query. For more info: https://jsonapi.org/format/#fetching-sorting
    :type sort: str

    """
    filter = .from_dict(filter)
    return web.Response(status=200)


async def update_clip_by_id(request: web.Request, id, body) -> web.Response:
    """update clip

    

    :param id: The id of the clip to be retrieved
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateClipByIdRequest.from_dict(body)
    return web.Response(status=200)


async def update_media_by_id(request: web.Request, id, body) -> web.Response:
    """update media

    

    :param id: id
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateMediaByIdRequest.from_dict(body)
    return web.Response(status=200)
