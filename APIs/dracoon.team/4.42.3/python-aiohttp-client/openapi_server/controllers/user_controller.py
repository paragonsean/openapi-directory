from typing import List, Dict
from aiohttp import web

from openapi_server.models.attributes_response import AttributesResponse
from openapi_server.models.avatar import Avatar
from openapi_server.models.change_user_password_request import ChangeUserPasswordRequest
from openapi_server.models.create_key_pair_request import CreateKeyPairRequest
from openapi_server.models.customer_data import CustomerData
from openapi_server.models.enable_customer_encryption_request import EnableCustomerEncryptionRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.mfa_totp_confirmation_request import MfaTotpConfirmationRequest
from openapi_server.models.notification_config import NotificationConfig
from openapi_server.models.notification_config_change_request import NotificationConfigChangeRequest
from openapi_server.models.notification_config_list import NotificationConfigList
from openapi_server.models.o_auth_approval import OAuthApproval
from openapi_server.models.o_auth_authorization import OAuthAuthorization
from openapi_server.models.profile_attributes import ProfileAttributes
from openapi_server.models.profile_attributes_request import ProfileAttributesRequest
from openapi_server.models.reset_password400_response import ResetPassword400Response
from openapi_server.models.subscribed_download_share import SubscribedDownloadShare
from openapi_server.models.subscribed_download_share_list import SubscribedDownloadShareList
from openapi_server.models.subscribed_node import SubscribedNode
from openapi_server.models.subscribed_node_list import SubscribedNodeList
from openapi_server.models.subscribed_upload_share import SubscribedUploadShare
from openapi_server.models.subscribed_upload_share_list import SubscribedUploadShareList
from openapi_server.models.totp_setup_response import TotpSetupResponse
from openapi_server.models.update_subscriptions_bulk_request import UpdateSubscriptionsBulkRequest
from openapi_server.models.update_user_account_request import UpdateUserAccountRequest
from openapi_server.models.user_account import UserAccount
from openapi_server.models.user_key_pair_container import UserKeyPairContainer
from openapi_server.models.user_mfa_status_response import UserMfaStatusResponse
from openapi_server import util


async def change_user_password(request: web.Request, body, x_sds_auth_token=None) -> web.Response:
    """Change user&#39;s password

    ### Description: Change the user&#39;s password.  ### Precondition: Authenticated user.  ### Postcondition: User&#39;s password is changed.  ### Further Information: The password **MUST** comply to configured password policies.    Forbidden characters in passwords: [&#x60;&amp;&#x60;, &#x60;&#39;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;]

    :param body: 
    :type body: dict | bytes
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = ChangeUserPasswordRequest.from_dict(body)
    return web.Response(status=200)


async def confirm_totp_setup(request: web.Request, body, x_sds_auth_token=None) -> web.Response:
    """Confirm second factor TOTP setup with a generated OTP

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.37.0&lt;/h3&gt;  ### Description: Confirm second factor TOTP setup with a generated OTP.  ### Precondition: Authenticated user    ### Postcondition: Second factor TOTP is enabled.  ### Further Information: None.

    :param body: 
    :type body: dict | bytes
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = MfaTotpConfirmationRequest.from_dict(body)
    return web.Response(status=200)


async def create_and_preserve_user_key_pair(request: web.Request, body, x_sds_auth_token=None) -> web.Response:
    """Create key pair and preserve copy of old private key

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.24.0&lt;/h3&gt;  ### Description:   Create user key pair and preserve copy of old private key.  ### Precondition: Authenticated user.  ### Postcondition: Key pair is created.   Copy of old private key is preserved.  ### Further Information: You can submit your old private key, encrypted with your current password.   This allows migrating file keys encrypted with your old key pair to the new one.

    :param body: 
    :type body: dict | bytes
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = CreateKeyPairRequest.from_dict(body)
    return web.Response(status=200)


async def delete_mfa_totp_setup(request: web.Request, id, valid_otp, x_sds_auth_token=None) -> web.Response:
    """Disable a MFA TOTP setup with generated OTP

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.37.0&lt;/h3&gt;  ### Description:   Delete multi-factor authentication TOTP setup with a valid OTP code.  ### Precondition: Authenticated user   Multi-factor authentication is **NOT** enforced  ### Postcondition: Second factor TOTP is disabled.  ### Further Information: None.

    :param id: 
    :type id: int
    :param valid_otp: 
    :type valid_otp: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def enable_customer_encryption(request: web.Request, body, x_sds_auth_token=None) -> web.Response:
    """Activate client-side encryption for customer

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128679; Deprecated since v4.24.0&lt;/h3&gt;  ### Use &#x60;POST /settings/keypair&#x60; API  ### Description:   Activate client-side encryption for according customer.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change config&lt;/span&gt; required.  ### Postcondition: Client-side encryption is enabled.  ### Further Information: Sets the ability for this customer to encrypt rooms.   Once enabled on customer level, it **CANNOT** be unset.   On activation, a customer rescue key pair **MUST** be set.

    :param body: 
    :type body: dict | bytes
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = EnableCustomerEncryptionRequest.from_dict(body)
    return web.Response(status=200)


async def get_mfa_status_for_user(request: web.Request, x_sds_auth_token=None) -> web.Response:
    """Request information about the user&#39;s mfa status

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.37.0&lt;/h3&gt;  ### Description: Request information about the user&#39;s mfa status  ### Precondition: Authenticated user.  ### Postcondition: None.  ### Further Information: None.

    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def get_totp_setup_information(request: web.Request, x_sds_auth_token=None) -> web.Response:
    """Request information to setup TOTP as second authentication factor

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.37.0&lt;/h3&gt;  ### Description:   Get setup information for multi-factor authentication (TOTP).  ### Precondition: Authenticated user.  ### Postcondition: None.   ### Further Information: None.

    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def list_download_share_subscriptions(request: web.Request, filter=None, limit=None, offset=None, sort=None, x_sds_auth_token=None) -> web.Response:
    """List Download Share subscriptions

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.20.0&lt;/h3&gt;  ### Description:   Retrieve a list of subscribed Download Shares for current user.   ### Precondition: Authenticated user.  ### Postcondition: List of subscribed Download Shares is returned.  ### Further Information: None.  ### Filtering All filter fields are connected via logical conjunction (**AND**)   Filter string syntax: &#x60;FIELD_NAME:OPERATOR:VALUE[:VALUE...]&#x60;    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;authParentId:eq:#&#x60;   Get download shares where &#x60;authParentId&#x60; equals &#x60;#&#x60;.  &lt;/details&gt;  ### Filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | **&#x60;downloadShareId&#x60;** | Download Share ID filter | &#x60;eq&#x60; | Download Share ID equals value. | &#x60;long value&#x60; | | **&#x60;authParentId&#x60;** | Auth parent ID filter | &#x60;eq&#x60; | Auth parent ID equals value. | &#x60;long value&#x60; |  &lt;/details&gt;  ---  ### Sorting: Sort string syntax: &#x60;FIELD_NAME:ORDER&#x60;   &#x60;ORDER&#x60; can be &#x60;asc&#x60; or &#x60;desc&#x60;.   Multiple sort criteria are possible.   Fields are connected via logical conjunction **AND**.  &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;downloadShareId:desc|authParentId:asc&#x60;   Sort by &#x60;downloadShareId&#x60; descending **AND** &#x60;authParentId&#x60; ascending.  &lt;/details&gt;  ### Sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | **&#x60;downloadShareId&#x60;** | Download Share ID | | **&#x60;authParentId&#x60;** | Auth parent ID |  &lt;/details&gt;

    :param filter: Filter string
    :type filter: str
    :param limit: Range limit.  Maximum 500.   For more results please use paging (&#x60;offset&#x60; + &#x60;limit&#x60;).
    :type limit: int
    :param offset: Range offset
    :type offset: int
    :param sort: Sort string
    :type sort: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def list_node_subscriptions(request: web.Request, filter=None, limit=None, offset=None, sort=None, x_sds_auth_token=None) -> web.Response:
    """List node subscriptions

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.20.0&lt;/h3&gt;  ### Description:   Retrieve a list of subscribed nodes for current user.   ### Precondition: Authenticated user.  ### Postcondition: List of subscribed nodes is returned.  ### Further Information: None.  ### Filtering: All filter fields are connected via logical conjunction (**AND**)   Filter string syntax: &#x60;FIELD_NAME:OPERATOR:VALUE[:VALUE...]&#x60;    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;authParentId:eq:#&#x60;   Get nodes where &#x60;authParentId&#x60; equals &#x60;#&#x60;.  &lt;/details&gt;  ### Filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | **&#x60;nodeId&#x60;** | Node ID filter | &#x60;eq&#x60; | Node ID equals value. | &#x60;long value&#x60; | | **&#x60;authParentId&#x60;** | Auth parent ID filter | &#x60;eq&#x60; | Auth parent ID equals value. | &#x60;long value&#x60; |  &lt;/details&gt;  ---  ### Sorting: Sort string syntax: &#x60;FIELD_NAME:ORDER&#x60;   &#x60;ORDER&#x60; can be &#x60;asc&#x60; or &#x60;desc&#x60;.   Multiple sort criteria are possible.   Fields are connected via logical conjunction **AND**.  &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;nodeId:desc|authParentId:asc&#x60;   Sort by &#x60;nodeId&#x60; descending **AND** &#x60;authParentId&#x60; ascending.  &lt;/details&gt;  ### Sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | **&#x60;nodeId&#x60;** | Node ID | | **&#x60;authParentId&#x60;** | Auth parent ID |  &lt;/details&gt;

    :param filter: Filter string
    :type filter: str
    :param limit: Range limit.  Maximum 500.   For more results please use paging (&#x60;offset&#x60; + &#x60;limit&#x60;).
    :type limit: int
    :param offset: Range offset
    :type offset: int
    :param sort: Sort string
    :type sort: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def list_upload_share_subscriptions(request: web.Request, filter=None, limit=None, offset=None, sort=None, x_sds_auth_token=None) -> web.Response:
    """List Upload Share subscriptions

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.24.0&lt;/h3&gt;  ### Description:   Retrieve a list of subscribed Upload Shares for current user.   ### Precondition: Authenticated user.  ### Postcondition: List of subscribed Upload Shares is returned.  ### Further Information: None.  ### Filtering All filter fields are connected via logical conjunction (**AND**)   Filter string syntax: &#x60;FIELD_NAME:OPERATOR:VALUE[:VALUE...]&#x60;    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;targetNodeId:eq:#&#x60;   Get upload shares where &#x60;targetNodeId&#x60; equals &#x60;#&#x60;.  &lt;/details&gt;  ### Filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | **&#x60;uploadShareId&#x60;** | Upload Share ID filter | &#x60;eq&#x60; | Upload Share ID equals value. | &#x60;long value&#x60; | | **&#x60;targetNodeId&#x60;** | Target node ID filter | &#x60;eq&#x60; | Target node ID equals value. | &#x60;long value&#x60; |  &lt;/details&gt;  ---  ### Sorting: Sort string syntax: &#x60;FIELD_NAME:ORDER&#x60;   &#x60;ORDER&#x60; can be &#x60;asc&#x60; or &#x60;desc&#x60;.   Multiple sort criteria are possible.   Fields are connected via logical conjunction **AND**.  &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;uploadShareId:desc|targetNodeId:asc&#x60;   Sort by &#x60;uploadShareId&#x60; descending **AND** &#x60;targetNodeId&#x60; ascending.  &lt;/details&gt;  ### Sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | **&#x60;uploadShareId&#x60;** | Upload Share ID | | **&#x60;targetNodeId&#x60;** | Target node ID |  &lt;/details&gt;

    :param filter: Filter string
    :type filter: str
    :param limit: Range limit.  Maximum 500.   For more results please use paging (&#x60;offset&#x60; + &#x60;limit&#x60;).
    :type limit: int
    :param offset: Range offset
    :type offset: int
    :param sort: Sort string
    :type sort: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def logout(request: web.Request, everywhere=None, x_sds_auth_token=None) -> web.Response:
    """Invalidate authentication token

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128679; Deprecated since v4.12.0&lt;/h3&gt;  ### Description:   Log out a user.  ### Precondition: Authenticated user.  ### Postcondition: * User is logged out   * Authentication token gets invalidated.  ### Further Information: None.

    :param everywhere: Invalidate all tokens
    :type everywhere: bool
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def ping_user(request: web.Request, x_sds_auth_token=None) -> web.Response:
    """(authenticated) Ping

    ### Description: Test connection to DRACOON Server (while authenticated).  ### Precondition: Authenticated user.  ### Postcondition: &#x60;200 OK&#x60; with principal information is returned if successful.  ### Further Information: None.

    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def remove_o_auth_approval(request: web.Request, client_id, x_sds_auth_token=None) -> web.Response:
    """Remove OAuth client approval

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.22.0&lt;/h3&gt;  ### Functional Description: Delete an OAuth client approval.  ### Precondition: Authenticated user and valid client ID  ### Postcondition: OAuth Client approval is revoked.  ### Further Information: None.

    :param client_id: OAuth client ID
    :type client_id: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def remove_o_auth_authorization(request: web.Request, client_id, authorization_id, x_sds_auth_token=None) -> web.Response:
    """Remove a OAuth authorization

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.12.0&lt;/h3&gt;  ### Description: Delete an authorization.  ### Precondition: Authenticated user and valid client ID, authorization ID  ### Postcondition: Authorization is revoked.  ### Further Information: None.

    :param client_id: OAuth client ID
    :type client_id: str
    :param authorization_id: OAuth authorization ID
    :type authorization_id: int
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def remove_o_auth_authorizations(request: web.Request, client_id, x_sds_auth_token=None) -> web.Response:
    """Remove all OAuth authorizations of a client

    ### Description: Delete all authorizations of a client.  ### Precondition: Authenticated user and valid client ID  ### Postcondition: All authorizations for the client are revoked.  ### Further Information: None.

    :param client_id: OAuth client ID
    :type client_id: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def remove_profile_attribute(request: web.Request, key, x_sds_auth_token=None) -> web.Response:
    """Remove user profile attribute

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.7.0&lt;/h3&gt;  ### Description:   Delete custom user profile attribute.  ### Precondition: None.  ### Postcondition: Custom user profile attribute is deleted.  ### Further Information: Allowed characters for keys are: &#x60;[a-zA-Z0-9_-]&#x60;

    :param key: Key
    :type key: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def remove_user_key_pair(request: web.Request, version=None, x_sds_auth_token=None) -> web.Response:
    """Remove user&#39;s key pair

    ### Description:   Delete user key pair.  ### Precondition: Authenticated user.  ### Postcondition: Key pair is deleted.  ### Further Information: If parameter &#x60;version&#x60; is not set and two key versions exist, this API deletes version A.       If two keys with the same version are set, this API deletes the older one.  This will also remove all file keys that were encrypted with the user public key. If the user had exclusive access to some files, those are removed as well since decrypting them became impossible.

    :param version: Version (NEW)
    :type version: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_avatar(request: web.Request, x_sds_auth_token=None) -> web.Response:
    """Request avatar

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.11.0&lt;/h3&gt;  ### Description: Get the avatar.  ### Precondition: Authenticated user.  ### Postcondition: Avatar is returned.  ### Further Information: None.

    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_customer_info(request: web.Request, x_sds_auth_token=None) -> web.Response:
    """Request customer information for user

    ### Description:   Use this API to get:  * customer name * used / free space * used / available * user account info  of the according customer.  ### Precondition: Authenticated user.  ### Postcondition: Customer information is returned.  ### Further Information: None.

    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_customer_key_pair(request: web.Request, x_sds_auth_token=None) -> web.Response:
    """Request customer&#39;s key pair

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128679; Deprecated since v4.24.0&lt;/h3&gt;  ### Use &#x60;GET /settings/keypair&#x60; API  ### Description:   Retrieve the customer rescue key pair.  ### Precondition: Authenticated user.  ### Postcondition: Key pair is returned.  ### Further Information: The private key is password-based encrypted with &#x60;AES256&#x60; / &#x60;PBKDF2&#x60;.

    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_list_of_notification_configs(request: web.Request, x_sds_auth_token=None) -> web.Response:
    """Request list of notification configurations

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.20.0&lt;/h3&gt;  ### Description:   Retrieve a list of notification configurations for current user.   ### Precondition: Authenticated user.  ### Postcondition: List of available notification configurations is returned.  ### Further Information: None.

    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_o_auth_approvals(request: web.Request, x_sds_date_format=None, sort=None, x_sds_auth_token=None) -> web.Response:
    """Request list of OAuth client approvals

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.22.0&lt;/h3&gt;  ### Functional Description:   Retrieve information about all OAuth client approvals.  ### Precondition: Authenticated user.  ### Postcondition: None.  ### Further Information: None.  ### Sorting: Sort string syntax: &#x60;FIELD_NAME:ORDER&#x60;   &#x60;ORDER&#x60; can be &#x60;asc&#x60; or &#x60;desc&#x60;.   Multiple sort criteria are possible.   Fields are connected via logical conjunction **AND**.  &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;clientName:desc&#x60;   Sort by &#x60;clientName&#x60; descending.  &lt;/details&gt;  ### Sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | &#x60;clientName&#x60; | Client name |  &lt;/details&gt;

    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str
    :param sort: Sort string
    :type sort: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_o_auth_authorizations(request: web.Request, x_sds_date_format=None, filter=None, sort=None, x_sds_auth_token=None) -> web.Response:
    """Request list of OAuth client authorizations

    ### Description:   Retrieve information about all OAuth client authorizations.  ### Precondition: Authenticated user.  ### Postcondition: List of OAuth client authorizations is returned.  ### Further Information:  ### Filtering: Filter string syntax: &#x60;FIELD_NAME:OPERATOR:VALUE[:VALUE...]&#x60;    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;isStandard:eq:true&#x60;   Get standard OAuth clients.  &lt;/details&gt;  ### Filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | &#x60;isStandard&#x60; | Standard client filter | &#x60;eq&#x60; |  | &#x60;true or false&#x60; |  &lt;/details&gt;  ---  ### Sorting: Sort string syntax: &#x60;FIELD_NAME:ORDER&#x60;   &#x60;ORDER&#x60; can be &#x60;asc&#x60; or &#x60;desc&#x60;.   Multiple sort criteria are possible.   Fields are connected via logical conjunction **AND**.  &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;clientName:desc&#x60;   Sort by &#x60;clientName&#x60; descending.  &lt;/details&gt;  ### Sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | &#x60;clientName&#x60; | Client name |  &lt;/details&gt;

    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str
    :param filter: Filter string
    :type filter: str
    :param sort: Sort string
    :type sort: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_profile_attributes(request: web.Request, offset=None, limit=None, filter=None, sort=None, x_sds_auth_token=None) -> web.Response:
    """Request user profile attributes

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.7.0&lt;/h3&gt;  ### Description:   Retrieve a list of user profile attributes.  ### Precondition: None.  ### Postcondition: List of attributes is returned.  ### Further Information:  ### Filtering: All filter fields are connected via logical conjunction (**AND**)   Filter string syntax: &#x60;FIELD_NAME:OPERATOR:VALUE[:VALUE...]&#x60;    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;key:cn:searchString_1|value:cn:searchString_2&#x60;   Filter by attribute key contains &#x60;searchString_1&#x60; **AND** attribute value contains &#x60;searchString_2&#x60;.  &lt;/details&gt;  ### Filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | &#x60;key&#x60; | User profile attribute key filter | &#x60;cn, eq, sw&#x60; | Attribute key contains / equals / starts with value. | &#x60;search String&#x60; | | &#x60;value&#x60; | User profile attribute value filter | &#x60;cn, eq, sw&#x60; | Attribute value contains / equals / starts with value. | &#x60;search String&#x60; |  &lt;/details&gt;  ---  ### Sorting: Sort string syntax: &#x60;FIELD_NAME:ORDER&#x60;   &#x60;ORDER&#x60; can be &#x60;asc&#x60; or &#x60;desc&#x60;.   Multiple sort fields are supported.    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;key:asc|value:desc&#x60;   Sort by &#x60;key&#x60; ascending **AND** by &#x60;value&#x60; descending.  &lt;/details&gt;  ### Sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | &#x60;key&#x60; | User profile attribute key | | &#x60;value&#x60; | User profile attribute value |  &lt;/details&gt;

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


async def request_user_info(request: web.Request, x_sds_date_format=None, more_info=None, x_sds_auth_token=None) -> web.Response:
    """Request user account information

    ### Description:   Retrieves all information regarding the current user&#39;s account.  ### Precondition: Authenticated user.  ### Postcondition: User information is returned.  ### Further Information: Setting the query parameter &#x60;more_info&#x60; to &#x60;true&#x60;, causes the API to return more details e.g. the user&#39;s groups.    &#x60;customer&#x60; (&#x60;CustomerData&#x60;) attribute in &#x60;UserAccount&#x60; response model is deprecated. Please use response from &#x60;GET /user/account/customer&#x60; instead.

    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str
    :param more_info: Get more info for this user  e.g. list of user groups
    :type more_info: bool
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_user_key_pair(request: web.Request, x_sds_date_format=None, version=None, x_sds_auth_token=None) -> web.Response:
    """Request user&#39;s key pair

    ### Description:   Retrieve the user key pair.  ### Precondition: Authenticated user.  ### Postcondition: Key pair is returned.   ### Further Information: The private key is password-based encrypted with &#x60;AES256&#x60; / &#x60;PBKDF2&#x60;.

    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str
    :param version: Version (NEW)
    :type version: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_user_key_pairs(request: web.Request, x_sds_date_format=None, x_sds_auth_token=None) -> web.Response:
    """Request all user key pairs

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.24.0&lt;/h3&gt;  ### Description:   Retrieve all user key pairs to allow re-encrypting file keys without need for a second distributor.  ### Precondition: Authenticated user.  ### Postcondition: List of key pairs is returned.   ### Further Information: None.

    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def reset_avatar(request: web.Request, x_sds_auth_token=None) -> web.Response:
    """Reset avatar

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.11.0&lt;/h3&gt;  ### Description:   Reset (custom) avatar to default avatar.  ### Precondition: Authenticated user.  ### Postcondition: * User&#39;s avatar gets deleted.   * Default avatar is set.  ### Further Information: None.

    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def set_profile_attributes(request: web.Request, body, x_sds_auth_token=None) -> web.Response:
    """Set user profile attributes

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128679; Deprecated since v4.12.0&lt;/h3&gt;  ### Description:   Set custom user profile attributes.  ### Precondition: None.  ### Postcondition: Custom user profile attributes are set.  ### Further Information: Batch function.   All existing user profile attributes will be deleted.    * Allowed characters for keys are: &#x60;[a-zA-Z0-9_-]&#x60;   * Characters are **case-insensitive**   * Maximum key length is **255**   * Maximum value length is **4096**

    :param body: 
    :type body: dict | bytes
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = ProfileAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def set_user_key_pair(request: web.Request, body, x_sds_auth_token=None) -> web.Response:
    """Set user&#39;s key pair

    ### Description:   Set the user key pair.  ### Precondition: Authenticated user.  ### Postcondition: Key pair is set.  ### Further Information: Overwriting an existing key pair is **NOT** possible.   Please delete the existing key pair first.   The private key is password-based encrypted with &#x60;AES256&#x60; / &#x60;PBKDF2&#x60;.

    :param body: 
    :type body: dict | bytes
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = UserKeyPairContainer.from_dict(body)
    return web.Response(status=200)


async def subscribe_download_share(request: web.Request, share_id, x_sds_auth_token=None) -> web.Response:
    """Subscribe Download Share for notifications

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.20.0&lt;/h3&gt;  ### Description:   Subscribe Download Share for notifications.  ### Precondition: User with _\&quot;manage download share\&quot;_ permissions on target node.  ### Postcondition: Download Share is subscribed.   Notifications for this Download Share will be triggered in the future.  ### Further Information: None.

    :param share_id: Share ID
    :type share_id: int
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def subscribe_download_shares(request: web.Request, body, x_sds_auth_token=None) -> web.Response:
    """Subscribe or Unsubscribe a List of Download Shares for notifications

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.25.0&lt;/h3&gt;  ### Description:   Subscribe/Unsubscribe download shares for notifications.  ### Precondition: User with _\&quot;manage download share\&quot;_ permissions on target node.    ### Postcondition: Download shares are subscribed or unsubscribed. Notifications for these download shares will be triggered in the future.  ### Further Information: Maximum number of subscriptions is 200.

    :param body: 
    :type body: dict | bytes
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = UpdateSubscriptionsBulkRequest.from_dict(body)
    return web.Response(status=200)


async def subscribe_node(request: web.Request, node_id, x_sds_auth_token=None) -> web.Response:
    """Subscribe node for notifications

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.20.0&lt;/h3&gt;  ### Description: Subscribe node for notifications.  ### Precondition: User has _\&quot;read\&quot;_ permissions in auth parent room.  ### Postcondition: Node is subscribed. Notifications for this node will be triggered in the future.  ### Further Information: None.

    :param node_id: Node ID
    :type node_id: int
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def subscribe_upload_share(request: web.Request, share_id, x_sds_auth_token=None) -> web.Response:
    """Subscribe Upload Share for notifications

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.24.0&lt;/h3&gt;  ### Description:   Subscribe Upload Share for notifications.  ### Precondition: User with _\&quot;manage upload share\&quot;_ permissions on target node.  ### Postcondition: Upload Share is subscribed.   Notifications for this Upload Share will be triggered in the future.  ### Further Information: None.

    :param share_id: Share ID
    :type share_id: int
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def subscribe_upload_shares(request: web.Request, body, x_sds_auth_token=None) -> web.Response:
    """Subscribe or Unsubscribe a List of Upload Shares for notifications

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.25.0&lt;/h3&gt;  ### Description:   Subscribe/Unsubscribe upload shares for notifications.  ### Precondition: User with _\&quot;manage upload share\&quot;_ permissions on target node.    ### Postcondition: Upload shares are subscribed or unsubscribed. Notifications for these upload shares will be triggered in the future.  ### Further Information: Maximum number of subscriptions is 200.

    :param body: 
    :type body: dict | bytes
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = UpdateSubscriptionsBulkRequest.from_dict(body)
    return web.Response(status=200)


async def unsubscribe_download_share(request: web.Request, share_id, x_sds_auth_token=None) -> web.Response:
    """Unsubscribe Download Share from notifications

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.20.0&lt;/h3&gt;  ### Description:   Unsubscribe Download Share from notifications.  ### Precondition: User with _\&quot;manage download share\&quot;_ permissions on target node.  ### Postcondition: Download Share is unsubscribed.   Notifications for this Download Share are disabled.  ### Further Information: None.

    :param share_id: Share ID
    :type share_id: int
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def unsubscribe_node(request: web.Request, node_id, x_sds_auth_token=None) -> web.Response:
    """Unsubscribe node from notifications

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.20.0&lt;/h3&gt;  ### Description:   Unsubscribe node from notifications.  ### Precondition: User has _\&quot;read\&quot;_ permissions in auth parent room.  ### Postcondition: Node is unsubscribed.   Notifications for this node are disabled.  ### Further Information: None.

    :param node_id: Node ID
    :type node_id: int
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def unsubscribe_upload_share(request: web.Request, share_id, x_sds_auth_token=None) -> web.Response:
    """Unsubscribe Upload Share from notifications

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.24.0&lt;/h3&gt;  ### Description:   Unsubscribe Upload Share from notifications.  ### Precondition: User with _\&quot;manage upload share\&quot;_ permissions on target node.  ### Postcondition: Upload Share is unsubscribed.   Notifications for this Upload Share are disabled.  ### Further Information: None.

    :param share_id: Share ID
    :type share_id: int
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def update_node_subscriptions(request: web.Request, body, x_sds_auth_token=None) -> web.Response:
    """Subscribe or Unsubscribe a List of nodes for notifications

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.25.0&lt;/h3&gt;  ### Description:   Subscribe/Unsubscribe nodes for notifications.  ### Precondition: User has _\&quot;read\&quot;_ permissions in auth parent room.  ### Postcondition: Nodes are subscribed or unsubscribed. Notifications for these nodes will be triggered in the future.  ### Further Information: Maximum number of subscriptions is 200.

    :param body: 
    :type body: dict | bytes
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = UpdateSubscriptionsBulkRequest.from_dict(body)
    return web.Response(status=200)


async def update_notification_config(request: web.Request, id, body, x_sds_auth_token=None) -> web.Response:
    """Update notification configuration

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.20.0&lt;/h3&gt;  ### Description:   Update notification configuration for current user.   ### Precondition: Authenticated user.  ### Postcondition: Notification configuration is updated.  ### Further Information: Leave &#x60;channelIds&#x60; empty to disable notifications.

    :param id: Unique identifier for a notification configuration
    :type id: int
    :param body: 
    :type body: dict | bytes
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = NotificationConfigChangeRequest.from_dict(body)
    return web.Response(status=200)


async def update_profile_attributes(request: web.Request, body, x_sds_auth_token=None) -> web.Response:
    """Add or edit user profile attributes

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.7.0&lt;/h3&gt;  ### Description:   Add or edit custom user profile attributes. &lt;br/&gt;&lt;br/&gt;&lt;span style&#x3D;\&quot;font-weight: bold; color: red;\&quot;&gt; &amp;#128679; **Warning: Please note that the response with HTTP status code 200 (OK) is deprecated and will be replaced with HTTP status code 204 (No content)!**&lt;/span&gt;&lt;br/&gt;  ### Precondition: None.  ### Postcondition: Custom user profile attributes are added or edited.  ### Further Information: Batch function.   If an entry existed before, it will be overwritten.   Range submodel is never returned.  * Allowed characters for keys are: &#x60;[a-zA-Z0-9_-]&#x60;   * Characters are **case-insensitive**   * Maximum key length is **255**   * Maximum value length is **4096**

    :param body: 
    :type body: dict | bytes
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = ProfileAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def update_user_account(request: web.Request, body, x_sds_date_format=None, x_sds_auth_token=None) -> web.Response:
    """Update user account

    ### Description:   Update current user&#39;s account.  ### Precondition: Authenticated user.  ### Postcondition: User&#39;s account is updated.  ### Further Information: * All input fields are limited to **150** characters.   * **All** characters are allowed.    &#x60;customer&#x60; (&#x60;CustomerData&#x60;) attribute in &#x60;UserAccount&#x60; response model is deprecated. Please use response from &#x60;GET /user/account/customer&#x60; instead.

    :param body: 
    :type body: dict | bytes
    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = UpdateUserAccountRequest.from_dict(body)
    return web.Response(status=200)


async def upload_avatar_as_multipart(request: web.Request, file, x_sds_auth_token=None) -> web.Response:
    """Change avatar

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.11.0&lt;/h3&gt;  ### Description: Change the avatar.  ### Precondition: Authenticated user.  ### Postcondition: Avatar is changed.  ### Further Information: * Media type **MUST** be &#x60;jpeg&#x60; or &#x60;png&#x60; * File size **MUST** bei less than &#x60;5 MB&#x60; * Dimensions **MUST** be &#x60;256x256 px&#x60;

    :param file: File
    :type file: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def use_emergency_code(request: web.Request, emergency_code, x_sds_auth_token=None) -> web.Response:
    """Using emergency-code

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.37.0&lt;/h3&gt;  ### Description: Using emergency code for login  ### Precondition: User has MFA enabled and is already logged in with account/pw (aka pre-Auth-Role)  ### Postcondition: All MFA-setups for the user are deleted.  ### Further Information:   

    :param emergency_code: 
    :type emergency_code: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)
