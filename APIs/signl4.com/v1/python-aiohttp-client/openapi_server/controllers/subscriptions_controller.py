from typing import List, Dict
from aiohttp import web

from openapi_server.models.channel_price_info import ChannelPriceInfo
from openapi_server.models.error_response_content import ErrorResponseContent
from openapi_server.models.subscription_feature import SubscriptionFeature
from openapi_server.models.subscription_info import SubscriptionInfo
from openapi_server.models.subscription_profile import SubscriptionProfile
from openapi_server.models.user_license_info import UserLicenseInfo
from openapi_server import util


async def subscriptions_get(request: web.Request, ) -> web.Response:
    """Get infos of all available/managed subscriptions.

    


    """
    return web.Response(status=200)


async def subscriptions_subscription_id_channel_prices_get(request: web.Request, subscription_id) -> web.Response:
    """Returns the subscription&#39;s channel price information.

    

    :param subscription_id: Id of the subscription that needs to be retrieved.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def subscriptions_subscription_id_features_get(request: web.Request, subscription_id) -> web.Response:
    """Returns the features of a specified subscription.

    

    :param subscription_id: Id of the subscription from which the features need to be retrieved.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def subscriptions_subscription_id_get(request: web.Request, subscription_id) -> web.Response:
    """Get infos of a specific subscription.

    

    :param subscription_id: Id of the subscription that&#39;s to be retrieved.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def subscriptions_subscription_id_profile_put(request: web.Request, subscription_id, body=None) -> web.Response:
    """Updates a subscriptions profile.

    

    :param subscription_id: ID of the subscription to be updated
    :type subscription_id: str
    :param body: Profile data to update subscription with
    :type body: dict | bytes

    """
    body = SubscriptionProfile.from_dict(body)
    return web.Response(status=200)


async def subscriptions_subscription_id_user_licenses_get(request: web.Request, subscription_id) -> web.Response:
    """Gets a subscription&#39;s user licenses.

    

    :param subscription_id: ID of the subscription
    :type subscription_id: str

    """
    return web.Response(status=200)
