from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.error_limit import ErrorLimit
from openapi_server.models.password_error import PasswordError
from openapi_server.models.secret import Secret
from openapi_server.models.shopper import Shopper
from openapi_server.models.shopper_id import ShopperId
from openapi_server.models.shopper_status import ShopperStatus
from openapi_server.models.shopper_update import ShopperUpdate
from openapi_server.models.subaccount_create import SubaccountCreate
from openapi_server import util


async def change_password(request: web.Request, shopper_id, body) -> web.Response:
    """Set subaccount&#39;s password

    &lt;strong&gt;Notes:&lt;/strong&gt;&lt;ul&gt;&lt;li&gt;Password set is only supported by API Resellers setting subaccount passwords.&lt;/li&gt;&lt;li&gt;**shopperId** is **not the same** as **customerId**.  **shopperId** is a number of max length 10 digits (*ex:* 1234567890) whereas **customerId** is a UUIDv4 (*ex:* 295e3bc3-b3b9-4d95-aae5-ede41a994d13)&lt;/li&gt;&lt;/ul&gt;

    :param shopper_id: Shopper whose password will be set
    :type shopper_id: str
    :param body: The value to set the subaccount&#39;s password to
    :type body: dict | bytes

    """
    body = Secret.from_dict(body)
    return web.Response(status=200)


async def create_subaccount(request: web.Request, body) -> web.Response:
    """Create a Subaccount owned by the authenticated Reseller

    

    :param body: The subaccount to create
    :type body: dict | bytes

    """
    body = SubaccountCreate.from_dict(body)
    return web.Response(status=200)


async def delete(request: web.Request, shopper_id, audit_client_ip) -> web.Response:
    """Request the deletion of a shopper profile

    &lt;strong&gt;Notes:&lt;/strong&gt;&lt;ul&gt;&lt;li&gt;Shopper deletion is not supported in OTE&lt;/li&gt;&lt;li&gt;**shopperId** is **not the same** as **customerId**.  **shopperId** is a number of max length 10 digits (*ex:* 1234567890) whereas **customerId** is a UUIDv4 (*ex:* 295e3bc3-b3b9-4d95-aae5-ede41a994d13)&lt;/li&gt;&lt;/ul&gt;

    :param shopper_id: The ID of the shopper to delete. Must agree with the shopper id on the token or header, if present. *Note*: **shopperId** is **not the same** as **customerId**.  **shopperId** is a number of max length 10 digits (*ex:* 1234567890) whereas **customerId** is a UUIDv4 (*ex:* 295e3bc3-b3b9-4d95-aae5-ede41a994d13)
    :type shopper_id: str
    :param audit_client_ip: The client IP of the user who originated the request leading to this call.
    :type audit_client_ip: str

    """
    return web.Response(status=200)


async def get(request: web.Request, shopper_id, includes=None) -> web.Response:
    """Get details for the specified Shopper

    &lt;strong&gt;Notes:&lt;/strong&gt;&lt;ul&gt;&lt;li&gt;**shopperId** is **not the same** as **customerId**.  **shopperId** is a number of max length 10 digits (*ex:* 1234567890) whereas **customerId** is a UUIDv4 (*ex:* 295e3bc3-b3b9-4d95-aae5-ede41a994d13)&lt;/li&gt;&lt;/ul&gt;

    :param shopper_id: Shopper whose details are to be retrieved
    :type shopper_id: str
    :param includes: Additional properties to be included in the response shopper object
    :type includes: List[str]

    """
    return web.Response(status=200)


async def get_status(request: web.Request, shopper_id, audit_client_ip) -> web.Response:
    """Get details for the specified Shopper

    &lt;strong&gt;Notes:&lt;/strong&gt;&lt;ul&gt;&lt;li&gt;**shopperId** is **not the same** as **customerId**. **shopperId** is a number of max length 10 digits (*ex:* 1234567890) whereas **customerId** is a UUIDv4 (*ex:* 295e3bc3-b3b9-4d95-aae5-ede41a994d13)&lt;/li&gt;&lt;/ul&gt;

    :param shopper_id: The ID of the shopper to retrieve. Must agree with the shopper id on the token or header, if present
    :type shopper_id: str
    :param audit_client_ip: The client IP of the user who originated the request leading to this call.
    :type audit_client_ip: str

    """
    return web.Response(status=200)


async def update(request: web.Request, shopper_id, body) -> web.Response:
    """Update details for the specified Shopper

    &lt;strong&gt;Notes:&lt;/strong&gt;&lt;ul&gt;&lt;li&gt;**shopperId** is **not the same** as **customerId**.  **shopperId** is a number of max length 10 digits (*ex:* 1234567890) whereas **customerId** is a UUIDv4 (*ex:* 295e3bc3-b3b9-4d95-aae5-ede41a994d13)&lt;/li&gt;&lt;/ul&gt;

    :param shopper_id: The ID of the Shopper to update
    :type shopper_id: str
    :param body: The Shopper details to update
    :type body: dict | bytes

    """
    body = ShopperUpdate.from_dict(body)
    return web.Response(status=200)
