from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_key_pair_request import CreateKeyPairRequest
from openapi_server.models.create_webhook_request import CreateWebhookRequest
from openapi_server.models.customer_settings_request import CustomerSettingsRequest
from openapi_server.models.customer_settings_response import CustomerSettingsResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.event_type_list import EventTypeList
from openapi_server.models.notification_channel_activation_request import NotificationChannelActivationRequest
from openapi_server.models.notification_channel_list import NotificationChannelList
from openapi_server.models.update_webhook_request import UpdateWebhookRequest
from openapi_server.models.user_key_pair_container import UserKeyPairContainer
from openapi_server.models.webhook import Webhook
from openapi_server.models.webhook_list import WebhookList
from openapi_server import util


async def create_and_preserve_key_pair(request: web.Request, body, x_sds_auth_token=None) -> web.Response:
    """Create system rescue key pair and preserve copy of old private key

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.24.0&lt;/h3&gt;  ### Description:   Create system rescue key pair and preserve copy of old private key.  ### Precondition: * Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change config&lt;/span&gt; * Existence of own key pair  ### Postcondition: System rescue key pair is created.   Copy of old private key is preserved.  ### Further Information: You can submit your old private key, encrypted with your current password.   This allows migrating file keys encrypted with your old key pair to the new one. 

    :param body: 
    :type body: dict | bytes
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = CreateKeyPairRequest.from_dict(body)
    return web.Response(status=200)


async def create_webhook(request: web.Request, body, x_sds_date_format=None, x_sds_auth_token=None) -> web.Response:
    """Create webhook

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.19.0&lt;/h3&gt;  ### Description:   Create a new webhook for the customer scope.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change config&lt;/span&gt; required.  ### Postcondition: Webhook is created for given event types.  ### Further Information: URL must begin with the &#x60;HTTPS&#x60; scheme.   Webhook names are limited to 150 characters.  ### Available event types: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Name | Description | Scope | | :--- | :--- | :--- | | **&#x60;user.created&#x60;** | Triggered when a new user is created | Customer Admin Webhook | | **&#x60;user.deleted&#x60;** | Triggered when a user is deleted | Customer Admin Webhook | | **&#x60;user.locked&#x60;** | Triggered when a user gets locked | Customer Admin Webhook | |  |  |  | | **&#x60;webhook.expiring&#x60;** | Triggered 30/20/10/1 days before a webhook expires |  Customer Admin Webhook | |  |  |  | | **&#x60;downloadshare.created&#x60;** | Triggered when a new download share is created in affected room | Node Webhook | | **&#x60;downloadshare.deleted&#x60;** | Triggered when a download share is deleted in affected room | Node Webhook | | **&#x60;downloadshare.used&#x60;** | Triggered when a download share is utilized in affected room | Node Webhook | | **&#x60;uploadshare.created&#x60;** | Triggered when a new upload share is created in affected room | Node Webhook | | **&#x60;uploadshare.deleted&#x60;** | Triggered when a upload share is deleted in affected room | Node Webhook | | **&#x60;uploadshare.used&#x60;** | Triggered when a new file is uploaded via the upload share in affected room | Node Webhook | | **&#x60;file.created&#x60;** | Triggered when a new file is uploaded in affected room | Node Webhook | | **&#x60;folder.created&#x60;** | Triggered when a new folder is created in affected room | Node Webhook | | **&#x60;room.created&#x60;** | Triggered when a new room is created (in affected room) | Node Webhook | | **&#x60;file.deleted&#x60;** | Triggered when a file is deleted in affected room | Node Webhook | | **&#x60;folder.deleted&#x60;** | Triggered when a folder is deleted in affected room | Node Webhook | | **&#x60;room.deleted&#x60;** | Triggered when a room is deleted in affected room | Node Webhook |  &lt;/details&gt;

    :param body: 
    :type body: dict | bytes
    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = CreateWebhookRequest.from_dict(body)
    return web.Response(status=200)


async def remove_system_rescue_key_pair(request: web.Request, version=None, x_sds_auth_token=None) -> web.Response:
    """Remove system rescue key pair

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.24.0&lt;/h3&gt;  ### Description:   Remove the system rescue key pair.  ### Precondition: * Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change config&lt;/span&gt; * Existence of own key pair  ### Postcondition: Key pair is removed (cf. further information below).  ### Further Information: Please set a new system rescue key pair first and re-encrypt file keys with it.   If no version is set, deleted key pair with lowest preference value.   Although, &#x60;version&#x60; **SHOULD** be set. 

    :param version: Version (NEW)
    :type version: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def remove_webhook(request: web.Request, webhook_id, x_sds_auth_token=None) -> web.Response:
    """Remove webhook

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.19.0&lt;/h3&gt;  ### Description:   Delete a webhook for the customer scope.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change config&lt;/span&gt; required.  ### Postcondition: Webhook is deleted.  ### Further Information: None.

    :param webhook_id: Webhook ID
    :type webhook_id: int
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_all_system_rescue_key_pairs(request: web.Request, x_sds_date_format=None, x_sds_auth_token=None) -> web.Response:
    """Request all system rescue key pairs

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.24.0&lt;/h3&gt;  ### Description:   Retrieve all system rescue key pairs to allow migrating system-rescue-key-encrypted file keys.  ### Precondition: * Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change config&lt;/span&gt; * Existence of own key pair  ### Postcondition: List of key pairs is returned.  ### Further Information: In the case of an algorithm migration of a system rescue key, one should create the new key pair before deleting the old one.   This allows re-encrypting file keys with the new key pair, using the old one.    This API allows to retrieve both key pairs, in contrast to &#x60;GET /settings/keypair&#x60;, which only delivers the preferred one. 

    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_list_of_event_types_for_config_manager(request: web.Request, x_sds_auth_token=None) -> web.Response:
    """Request list of event types

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.19.0&lt;/h3&gt;  ### Description:   Get a list of available (for &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt;) event types.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change config&lt;/span&gt; required.  ### Postcondition: List of available event types is returned.  ### Further Information: None. 

    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_list_of_webhooks(request: web.Request, x_sds_date_format=None, offset=None, limit=None, filter=None, sort=None, x_sds_auth_token=None) -> web.Response:
    """Request list of webhooks

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.19.0&lt;/h3&gt;  ### Description:   Get a list of webhooks for the customer scope.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change config&lt;/span&gt; required.  ### Postcondition: List of webhooks is returned.  ### Filtering: All filter fields are connected via logical conjunction (**AND**)   Filter string syntax: &#x60;FIELD_NAME:OPERATOR:VALUE[:VALUE...]&#x60;    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;name:cn:goo|createdAt:ge:2015-01-01&#x60;   Get webhooks where name contains &#x60;goo&#x60; **AND** webhook creation date is **&gt;&#x3D;** &#x60;2015-01-01&#x60;.  &lt;/details&gt;  ### Filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | **&#x60;id&#x60;** | Webhook id filter | &#x60;eq&#x60; | Webhook id equals value.&lt;br&gt;Multiple values are allowed and will be connected via logical disjunction (**OR**). |&#x60;positive number&#x60;| | **&#x60;name&#x60;** | Webhook type name| &#x60;cn, eq&#x60; | Webhook name contains / equals value. | &#x60;search String&#x60; | | **&#x60;isEnabled&#x60;** | Webhook isEnabled filter | &#x60;eq&#x60; |  | &#x60;true or false&#x60; | | **&#x60;createdAt&#x60;** | Creation date filter | &#x60;ge, le&#x60; | Creation date is greater / less equals than value.&lt;br&gt;Multiple operator values are allowed and will be connected via logical conjunction (**AND**).&lt;br&gt;e.g. &#x60;createdAt:ge:2016-12-31&#x60;&amp;#124;&#x60;createdAt:le:2018-01-01&#x60; | &#x60;Date (yyyy-MM-dd)&#x60; | | **&#x60;updatedAt&#x60;** | Last modification date filter | &#x60;ge, le&#x60; | Last modification date is greater / less equals than value.&lt;br&gt;Multiple operator values are allowed and will be connected via logical conjunction (**AND**).&lt;br&gt;e.g. &#x60;updatedAt:ge:2016-12-31&#x60;&amp;#124;&#x60;updatedAt:le:2018-01-01&#x60; | &#x60;Date (yyyy-MM-dd)&#x60; | | **&#x60;expiration&#x60;** | Expiration date filter | &#x60;ge, le, eq&#x60; | Expiration date is greater / less equals than value.&lt;br&gt;Multiple operator values are allowed and will be connected via logical conjunction (**AND**).&lt;br&gt;e.g. &#x60;expiration:ge:2016-12-31&#x60;&amp;#124;&#x60;expiration:le:2018-01-01&#x60; | &#x60;Date (yyyy-MM-dd)&#x60; | | **&#x60;lastFailStatus&#x60;** | Failure status filter | &#x60;eq&#x60; | Last HTTP status code. Set when a webhook is auto-disabled due to repeated delivery failures |&#x60;positive number&#x60;|  &lt;/details&gt;  ---  ### Sorting: Sort string syntax: &#x60;FIELD_NAME:ORDER&#x60;   &#x60;ORDER&#x60; can be &#x60;asc&#x60; or &#x60;desc&#x60;.   Multiple sort criteria are possible.   Fields are connected via logical conjunction **AND**.  &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;name:desc|isEnabled:asc&#x60;   Sort by &#x60;name&#x60; descending and &#x60;isEnabled&#x60; ascending.  &lt;/details&gt;  ### Sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | **&#x60;id&#x60;** | Webhook id | | **&#x60;name&#x60;** | Webhook name | | **&#x60;isEnabled&#x60;** | Webhook isEnabled | | **&#x60;createdAt&#x60;** | Creation date | | **&#x60;updatedAt&#x60;** | Last modification date | | **&#x60;expiration&#x60;** | Expiration date |  &lt;/details&gt; 

    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str
    :param offset: Range offset
    :type offset: int
    :param limit: Range limit.  Maximum 500.   For more results please use paging (&#x60;offset&#x60; + &#x60;limit&#x60;).
    :type limit: int
    :param filter: Filter string
    :type filter: str
    :param sort: Sort string
    :type sort: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_notification_channels(request: web.Request, x_sds_auth_token=None) -> web.Response:
    """Request list of notification channels

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.20.0&lt;/h3&gt;  ### Description:   Retrieve a list of configured notification channels.  ### Precondition: Right _\&quot;change config\&quot;_ required.  ### Postcondition: List of notification channels is returned.  ### Further Information: None. 

    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_settings(request: web.Request, x_sds_auth_token=None) -> web.Response:
    """Request customer settings

    ### Description:   Retrieve customer related settings.   ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read config&lt;/span&gt; required.  ### Postcondition: List of available settings is returned.  ### Further Information: None.  ### Configurable customer settings: &lt;details open style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Setting | Description                                                                                                                                                           | Value | | :--- |:----------------------------------------------------------------------------------------------------------------------------------------------------------------------| :--- | | &#x60;homeRoomParentName&#x60; | Name of the container in which all user&#39;s home rooms are located.&lt;br&gt;&#x60;null&#x60; if &#x60;homeRoomsActive&#x60; is &#x60;false&#x60;.                                                          | &#x60;String&#x60; | | &#x60;homeRoomQuota&#x60; | Refers to the quota of each single user&#39;s home room.&lt;br&gt;&#x60;0&#x60; represents no quota.&lt;br&gt;&#x60;null&#x60; if &#x60;homeRoomsActive&#x60; is &#x60;false&#x60;.                                           | &#x60;positive Long&#x60; | | &#x60;homeRoomsActive&#x60; | If set to &#x60;true&#x60;, every user with an Active Directory account or OpenID Connect account gets a personal homeroom.&lt;br&gt;Once activated, this **CANNOT** be deactivated. | &#x60;true or false&#x60; |   &lt;/details&gt;

    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_system_rescue_key_pair(request: web.Request, x_sds_date_format=None, version=None, x_sds_auth_token=None) -> web.Response:
    """Request system rescue key pair

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.24.0&lt;/h3&gt;  ### Description:   Retrieve the system rescue key pair.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change config&lt;/span&gt;  ### Postcondition: Key pair is returned.  ### Further Information: If more than one key pair exists the one with highest preference value is returned. 

    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str
    :param version: Version (NEW)
    :type version: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_webhook(request: web.Request, webhook_id, x_sds_date_format=None, x_sds_auth_token=None) -> web.Response:
    """Request webhook

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.19.0&lt;/h3&gt;  ### Description:   Get a specific webhook for the customer scope.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change config&lt;/span&gt; required.  ### Postcondition: Webhook is returned.  ### Further Information: None.

    :param webhook_id: Webhook ID
    :type webhook_id: int
    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def reset_webhook_lifetime(request: web.Request, webhook_id, x_sds_date_format=None, x_sds_auth_token=None) -> web.Response:
    """Reset webhook lifetime

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.19.0&lt;/h3&gt;  ### Description:   Reset the lifetime of a webhook for the customer scope.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change config&lt;/span&gt; required.  ### Postcondition: Lifetime of the webhook is reset.  ### Further Information: None.

    :param webhook_id: Webhook ID
    :type webhook_id: int
    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def set_settings(request: web.Request, body, x_sds_auth_token=None) -> web.Response:
    """Set customer settings

    ### Description:   Set customer related settings.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; required.  ### Postcondition: Provided settings are updated.  ### Further Information: None.  ### Configurable customer settings &lt;details open style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Setting | Description                                                                                                                                                          | Value | | :--- |:---------------------------------------------------------------------------------------------------------------------------------------------------------------------| :--- | | &#x60;homeRoomParentName&#x60; | Name of the container in which all user&#39;s home rooms are located.&lt;br&gt;&#x60;null&#x60; if &#x60;homeRoomsActive&#x60; is &#x60;false&#x60;.                                                         | &#x60;String&#x60; | | &#x60;homeRoomQuota&#x60; | Refers to the quota of each single user&#39;s home room.&lt;br&gt;&#x60;0&#x60; represents no quota.&lt;br&gt;&#x60;null&#x60; if &#x60;homeRoomsActive&#x60; is &#x60;false&#x60;.                                          | &#x60;positive Long&#x60; | | &#x60;homeRoomsActive&#x60; | If set to &#x60;true&#x60;, every user with an Active Directory account or OpenID Connect account gets a personal homeroom.&lt;br&gt;Once activated, this **CANNOT** be deactivated. | &#x60;true or false&#x60; |  &lt;/details&gt;  ### Node naming convention: * Node (room, folder, file) names are limited to **150** characters. * Illegal names:   &#x60;&#39;CON&#39;, &#39;PRN&#39;, &#39;AUX&#39;, &#39;NUL&#39;, &#39;COM1&#39;, &#39;COM2&#39;, &#39;COM3&#39;, &#39;COM4&#39;, &#39;COM5&#39;, &#39;COM6&#39;, &#39;COM7&#39;, &#39;COM8&#39;, &#39;COM9&#39;, &#39;LPT1&#39;, &#39;LPT2&#39;, &#39;LPT3&#39;, &#39;LPT4&#39;, &#39;LPT5&#39;, &#39;LPT6&#39;, &#39;LPT7&#39;, &#39;LPT8&#39;, &#39;LPT9&#39;, (and any of those with an extension)&#x60; * Illegal characters in names:   &#x60;&#39;\\\\&#39;, &#39;&lt;&#39;,&#39;&gt;&#39;, &#39;:&#39;, &#39;\\\&quot;&#39;, &#39;|&#39;, &#39;?&#39;, &#39;*&#39;, &#39;/&#39;, leading &#39;-&#39;, trailing &#39;.&#39; &#x60; 

    :param body: 
    :type body: dict | bytes
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = CustomerSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def set_system_rescue_key_pair(request: web.Request, body, x_sds_auth_token=None) -> web.Response:
    """Activate client-side encryption for customer

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.24.0&lt;/h3&gt;  ### Description:   Set the system rescue key pair and activate client-side encryption for according customer.  ### Precondition: * Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change config&lt;/span&gt; * Existence of own key pair  ### Postcondition: System rescue key pair is set and client-side encryption is enabled.  ### Further Information: Sets the ability for this customer to encrypt rooms.   Once enabled on customer level, it **CANNOT** be unset.   On activation, a customer rescue key pair **MUST** be set. 

    :param body: 
    :type body: dict | bytes
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = UserKeyPairContainer.from_dict(body)
    return web.Response(status=200)


async def toggle_notification_channels(request: web.Request, body, x_sds_auth_token=None) -> web.Response:
    """Toggle notification channels

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.20.0&lt;/h3&gt;  ### Description:   Toggle configured notification channels.  ### Precondition: Right _\&quot;change config\&quot;_ required.  ### Postcondition: Channel status is switched.  ### Further Information: None. 

    :param body: 
    :type body: dict | bytes
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = NotificationChannelActivationRequest.from_dict(body)
    return web.Response(status=200)


async def update_webhook(request: web.Request, webhook_id, body, x_sds_date_format=None, x_sds_auth_token=None) -> web.Response:
    """Update webhook

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.19.0&lt;/h3&gt;  ### Description:   Update an existing webhook for the customer scope.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change config&lt;/span&gt; required.  ### Postcondition: Webhook is updated.  ### Further Information: URL must begin with the &#x60;HTTPS&#x60; scheme. Webhook names are limited to 150 characters. Webhook event types can not be changed from Customer Admin Webhook types to Node Webhook types and vice versa    ### Available event types: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Name | Description | Scope | | :--- | :--- | :--- | | **&#x60;user.created&#x60;** | Triggered when a new user is created | Customer Admin Webhook | | **&#x60;user.deleted&#x60;** | Triggered when a user is deleted | Customer Admin Webhook | | **&#x60;user.locked&#x60;** | Triggered when a user gets locked | Customer Admin Webhook | |  |  |  | | **&#x60;webhook.expiring&#x60;** | Triggered 30/20/10/1 days before a webhook expires |  Customer Admin Webhook | |  |  |  | | **&#x60;downloadshare.created&#x60;** | Triggered when a new download share is created in affected room | Node Webhook | | **&#x60;downloadshare.deleted&#x60;** | Triggered when a download share is deleted in affected room | Node Webhook | | **&#x60;downloadshare.used&#x60;** | Triggered when a download share is utilized in affected room | Node Webhook | | **&#x60;uploadshare.created&#x60;** | Triggered when a new upload share is created in affected room | Node Webhook | | **&#x60;uploadshare.deleted&#x60;** | Triggered when a upload share is deleted in affected room | Node Webhook | | **&#x60;uploadshare.used&#x60;** | Triggered when a new file is uploaded via the upload share in affected room | Node Webhook | | **&#x60;file.created&#x60;** | Triggered when a new file is uploaded in affected room | Node Webhook | | **&#x60;folder.created&#x60;** | Triggered when a new folder is created in affected room | Node Webhook | | **&#x60;room.created&#x60;** | Triggered when a new room is created (in affected room) | Node Webhook | | **&#x60;file.deleted&#x60;** | Triggered when a file is deleted in affected room | Node Webhook | | **&#x60;folder.deleted&#x60;** | Triggered when a folder is deleted in affected room | Node Webhook | | **&#x60;room.deleted&#x60;** | Triggered when a room is deleted in affected room | Node Webhook |  &lt;/details&gt;

    :param webhook_id: Webhook ID
    :type webhook_id: int
    :param body: 
    :type body: dict | bytes
    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = UpdateWebhookRequest.from_dict(body)
    return web.Response(status=200)
