from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_download_share_request import CreateDownloadShareRequest
from openapi_server.models.create_upload_share_request import CreateUploadShareRequest
from openapi_server.models.delete_download_shares_request import DeleteDownloadSharesRequest
from openapi_server.models.delete_upload_shares_request import DeleteUploadSharesRequest
from openapi_server.models.download_share import DownloadShare
from openapi_server.models.download_share_link_email import DownloadShareLinkEmail
from openapi_server.models.download_share_list import DownloadShareList
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.reset_password400_response import ResetPassword400Response
from openapi_server.models.update_download_share_request import UpdateDownloadShareRequest
from openapi_server.models.update_download_shares_bulk_request import UpdateDownloadSharesBulkRequest
from openapi_server.models.update_upload_share_request import UpdateUploadShareRequest
from openapi_server.models.update_upload_shares_bulk_request import UpdateUploadSharesBulkRequest
from openapi_server.models.upload_share import UploadShare
from openapi_server.models.upload_share_link_email import UploadShareLinkEmail
from openapi_server.models.upload_share_list import UploadShareList
from openapi_server import util


async def create_download_share(request: web.Request, body, x_sds_date_format=None, x_sds_auth_token=None) -> web.Response:
    """Create new Download Share

    ### Description: Create a new Download Share.  ### Precondition: User with &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage download share&lt;/span&gt; permissions on target node.  ### Postcondition: Download Share is created.  ### Further Information:  If the target node is a room: subordinary rooms are excluded from a Download Share.  * &#x60;name&#x60; is limited to **150** characters. * &#x60;notes&#x60; are limited to **255** characters. * &#x60;password&#x60; is limited to **1024** characters.  Use &#x60;POST /shares/downloads/{share_id}/email&#x60; API for sending emails.    Forbidden characters in passwords: [&#x60;&amp;&#x60;, &#x60;&#39;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;]  Please keep in mind that due to various restrictions of different telecommunication providers, non-ASCII characters may not be displayed correctly in short messages (SMS).

    :param body: 
    :type body: dict | bytes
    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = CreateDownloadShareRequest.from_dict(body)
    return web.Response(status=200)


async def create_upload_share(request: web.Request, body, x_sds_date_format=None, x_sds_auth_token=None) -> web.Response:
    """Create new Upload Share

    ### Description: Create a new Upload Share (aka File Request).  ### Precondition: User has &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage upload share&lt;/span&gt; permissions on target container.  ### Postcondition: Upload Share is created.  ### Further Information:  * &#x60;name&#x60; is limited to **150** characters. * &#x60;notes&#x60; are limited to **255** characters. * &#x60;password&#x60; is limited to **1024** characters.  Forbidden characters in passwords: [&#x60;&amp;&#x60;, &#x60;&#39;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;]    Use &#x60;POST /shares/uploads/{share_id}/email&#x60; API for sending emails.  Please keep in mind that due to various restrictions of different telecommunication providers, non-ASCII characters may not be displayed correctly in short messages (SMS).

    :param body: 
    :type body: dict | bytes
    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = CreateUploadShareRequest.from_dict(body)
    return web.Response(status=200)


async def delete_download_shares(request: web.Request, body, x_sds_auth_token=None) -> web.Response:
    """Remove Download Shares

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.21.0&lt;/h3&gt;  ### Functional Description: Delete multiple Download Shares.  ### Precondition: User with _\&quot;manage download share\&quot;_ permissions on target nodes.  ### Postcondition: Download Shares are deleted.  ### Further Information: Only the Download Shares are removed; the referenced files or containers persists.

    :param body: 
    :type body: dict | bytes
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = DeleteDownloadSharesRequest.from_dict(body)
    return web.Response(status=200)


async def delete_upload_shares(request: web.Request, body, x_sds_auth_token=None) -> web.Response:
    """Remove Upload Shares

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.21.0&lt;/h3&gt;  ### Functional Description: Delete multiple Upload Shares (aka Upload Accounts).  ### Precondition: User has _\&quot;manage upload share\&quot;_ permissions on target containers.  ### Postcondition: Upload Shares are deleted.  ### Further Information: Only the Upload Shares are removed; already uploaded files and the target container persist.

    :param body: 
    :type body: dict | bytes
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = DeleteUploadSharesRequest.from_dict(body)
    return web.Response(status=200)


async def remove_download_share(request: web.Request, share_id, x_sds_auth_token=None) -> web.Response:
    """Remove Download Share

    ### Description: Delete a Download Share.  ### Precondition: User with &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage download share&lt;/span&gt; permissions on target node.  ### Postcondition: Download Share is deleted.  ### Further Information: Only the Download Share is removed; the referenced file or container persists.

    :param share_id: Share ID
    :type share_id: int
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def remove_upload_share(request: web.Request, share_id, x_sds_auth_token=None) -> web.Response:
    """Remove Upload Share

    ### Description: Delete an Upload Share (aka File Request).  ### Precondition: User has &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage upload share&lt;/span&gt; permissions on target container.  ### Postcondition: Upload Share is deleted.  ### Further Information: Only the Upload Share is removed; already uploaded files and the target container persist.

    :param share_id: Share ID
    :type share_id: int
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_download_share(request: web.Request, share_id, x_sds_date_format=None, x_sds_auth_token=None) -> web.Response:
    """Request Download Share

    ### Description:   Retrieve detailed information about one Download Share.  ### Precondition: User with &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage download share&lt;/span&gt; permissions on target node.  ### Postcondition: Download Share is returned  ### Further Information: None.

    :param share_id: Share ID
    :type share_id: int
    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_download_share_qr(request: web.Request, share_id, x_sds_date_format=None, x_sds_auth_token=None) -> web.Response:
    """Request Download Share via QR Code

    ### Description:   Retrieve detailed information about one Download Share.  ### Precondition: User with &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage download share&lt;/span&gt; permissions on target node.  ### Postcondition: Download Share is returned  ### Further Information: None.

    :param share_id: Share ID
    :type share_id: int
    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_download_shares(request: web.Request, x_sds_date_format=None, filter=None, sort=None, offset=None, limit=None, x_sds_auth_token=None) -> web.Response:
    """Request list of Download Shares

    ### Description:   Retrieve a list of Download Shares.  ### Precondition: Authenticated user.  ### Postcondition: List of available Download Shares is returned.  ### Further Information:  ### Filtering: All filter fields are connected via logical (**AND**). createdBy and updatedBy searches several user-related attributes.  Filter string syntax: &#x60;FIELD_NAME:OPERATOR:VALUE[:VALUE...]&#x60;    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;name:cn:searchString_1|createdBy:cn:searchString_2&#x60; Filter by file name contains &#x60;searchString_1&#x60; **AND** creator info (&#x60;firstName&#x60; **OR** &#x60;lastName&#x60; **OR** &#x60;email&#x60; **OR** &#x60;username&#x60;) contains &#x60;searchString_2&#x60;.  &lt;/details&gt;  ### Filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | &#x60;name&#x60; | Alias or node name filter | &#x60;cn&#x60; | Alias or node name contains value. | &#x60;search String&#x60; | | &#x60;createdAt&#x60; | Creation date filter | &#x60;ge, le&#x60; | Creation date is greater / less equals than value.&lt;br&gt;Multiple operator values are allowed and will be connected via logical conjunction (**AND**).&lt;br&gt;e.g. &#x60;createdAt:ge:2016-12-31&#x60;&amp;#124;&#x60;createdAt:le:2018-01-01&#x60; | &#x60;Date (yyyy-MM-dd)&#x60; | | &#x60;createdBy&#x60; | Creator info filter | &#x60;cn, eq&#x60; | Creator info (&#x60;firstName&#x60; **OR** &#x60;lastName&#x60; **OR** &#x60;email&#x60; **OR** &#x60;username&#x60;) contains value. | &#x60;search String&#x60; | | &#x60;createdById&#x60; | Creator ID filter | &#x60;eq&#x60; | Creator ID equals value. | &#x60;positive Integer&#x60; | | &#x60;accessKey&#x60; | Share access key filter | &#x60;cn&#x60; | Share access key contains values. | &#x60;search String&#x60; | | &#x60;nodeId&#x60; | Source node ID | &#x60;eq&#x60; | Source node (room, folder, file) ID equals value. | &#x60;positive Integer&#x60; | | &#x60;updatedBy&#x60; | Modifier info filter | &#x60;cn, eq&#x60; | Modifier info (&#x60;firstName&#x60; **OR** &#x60;lastName&#x60; **OR** &#x60;email&#x60; **OR** &#x60;username&#x60;) contains value. | &#x60;search String&#x60; | | &#x60;updatedById&#x60; | Modifier ID filter | &#x60;eq&#x60; | Modifier ID equals value. | &#x60;positive Integer&#x60; |  &lt;/details&gt;  ### Deprecated filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | &lt;del&gt;&#x60;userId&#x60;&lt;/del&gt;  | Creator user ID | &#x60;eq&#x60; | Creator user ID equals value. Use &#x60;createdById&#x60; instead | &#x60;positive Integer&#x60; |  &lt;/details&gt;  ---  ### Sorting: Sort string syntax: &#x60;FIELD_NAME:ORDER&#x60;   &#x60;ORDER&#x60; can be &#x60;asc&#x60; or &#x60;desc&#x60;.   Multiple sort fields are supported.    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;name:asc|expireAt:desc&#x60;   Sort by &#x60;name&#x60; ascending **AND** by &#x60;expireAt&#x60; descending.  &lt;/details&gt;  ### Sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | &#x60;name&#x60; | Alias or node name | | &#x60;notifyCreator&#x60; | Notify creator on every download | | &#x60;expireAt&#x60; | Expiration date | | &#x60;createdAt&#x60; | Creation date | | &#x60;createdBy&#x60; | Creator first name, last name | | &#x60;classification&#x60; | Classification ID:&lt;ul&gt;&lt;li&gt;1 - public&lt;/li&gt;&lt;li&gt;2 - internal&lt;/li&gt;&lt;li&gt;3 - confidential&lt;/li&gt;&lt;li&gt;4 - strictly confidential&lt;/li&gt;&lt;/ul&gt; |  &lt;/details&gt; 

    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str
    :param filter: Filter string
    :type filter: str
    :param sort: Sort string
    :type sort: str
    :param offset: Range offset
    :type offset: int
    :param limit: Range limit.  Maximum 500.   For more results please use paging (&#x60;offset&#x60; + &#x60;limit&#x60;).
    :type limit: int
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_upload_share(request: web.Request, share_id, x_sds_date_format=None, x_sds_auth_token=None) -> web.Response:
    """Request Upload Share

    ### Description:   Retrieve detailed information about one Upload Share (aka File Request).  ### Precondition: User has &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage upload share&lt;/span&gt; permissions on target container.  ### Postcondition: Upload Share is returned.  ### Further Information: None.

    :param share_id: Share ID
    :type share_id: int
    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_upload_share_qr(request: web.Request, share_id, x_sds_date_format=None, x_sds_auth_token=None) -> web.Response:
    """Request Upload Share via QR Code

    ### Description:   Retrieve detailed information about one Upload Share (aka File Request).  ### Precondition: User has &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage upload share&lt;/span&gt; permissions on target container.  ### Postcondition: Upload Share is returned.  ### Further Information: None.

    :param share_id: Share ID
    :type share_id: int
    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_upload_shares(request: web.Request, x_sds_date_format=None, filter=None, sort=None, offset=None, limit=None, x_sds_auth_token=None) -> web.Response:
    """Request list of Upload Shares

    ### Description:   Retrieve a list of Upload Shares (aka File Requests).  ### Precondition: Authenticated user.  ### Postcondition: List of available Upload Shares is returned.  ### Further Information:  ### Filtering: All filter fields are connected via logical (**AND**). createdBy and updatedBy searches several user-related attributes. Filter string syntax: &#x60;FIELD_NAME:OPERATOR:VALUE[:VALUE...]&#x60;    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;name:cn:searchString_1|createdBy:cn:searchString_2&#x60;   Filter by alias name contains &#x60;searchString_1&#x60; **AND** creator info (&#x60;firstName&#x60; **OR** &#x60;lastName&#x60; **OR** &#x60;email&#x60; **OR** &#x60;username&#x60;) contains &#x60;searchString_2&#x60;.  &lt;/details&gt;  ### Filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | &#x60;name&#x60; | Alias name filter | &#x60;cn&#x60; | Alias name contains value. | &#x60;search String&#x60; | | &#x60;createdAt&#x60; | Creation date filter | &#x60;ge, le&#x60; | Creation date is greater / less equals than value.&lt;br&gt;Multiple operator values are allowed and will be connected via logical conjunction (**AND**).&lt;br&gt;e.g. &#x60;createdAt:ge:2016-12-31&#x60;&amp;#124;&#x60;createdAt:le:2018-01-01&#x60; | &#x60;Date (yyyy-MM-dd)&#x60; | | &#x60;createdBy&#x60; | Creator info filter | &#x60;cn, eq&#x60; | Creator info (&#x60;firstName&#x60; **OR** &#x60;lastName&#x60; **OR** &#x60;email&#x60; **OR** &#x60;username&#x60;) contains value. | &#x60;search String&#x60; | | &#x60;createdById&#x60; | Creator ID filter | &#x60;eq&#x60; | Creator ID equals value. | &#x60;positive Integer&#x60; | | &#x60;accessKey&#x60; | Share access key filter | &#x60;cn&#x60; | Share access key contains values. | &#x60;search String&#x60; | | &#x60;userId&#x60; | Creator user ID | &#x60;eq&#x60; | Creator user ID equals value. | &#x60;positive Integer&#x60; | | &#x60;targetId&#x60; | Target node ID | &#x60;eq&#x60; | Target node (room, folder) ID equals value. | &#x60;positive Integer&#x60; | | &#x60;updatedBy&#x60; | Modifier info filter | &#x60;cn, eq&#x60; | Modifier info (&#x60;firstName&#x60; **OR** &#x60;lastName&#x60; **OR** &#x60;email&#x60; **OR** &#x60;username&#x60;) contains value. | &#x60;search String&#x60; | | &#x60;updatedById&#x60; | Modifier ID filter | &#x60;eq&#x60; | Modifier ID equals value. | &#x60;positive Integer&#x60; |  &lt;/details&gt;  ### Deprecated filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | &lt;del&gt;&#x60;targetId&#x60;&lt;/del&gt; | Target node ID | &#x60;cn&#x60; | Target node (room, folder) ID equals value. | &#x60;positive Integer&#x60; | | &lt;del&gt;&#x60;userId&#x60; &lt;/del&gt;| Creator user ID | &#x60;eq&#x60; | Creator user ID equals value. Use &#x60;createdById&#x60; instead. | &#x60;positive Integer&#x60; |  &lt;/details&gt;  ---  Sort string syntax: &#x60;FIELD_NAME:ORDER&#x60;   &#x60;ORDER&#x60; can be &#x60;asc&#x60; or &#x60;desc&#x60;.   Multiple sort fields are supported.    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;name:asc|expireAt:desc&#x60;   Sort by &#x60;name&#x60; ascending **AND** by &#x60;expireAt&#x60; descending.  &lt;/details&gt;  ### Sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | &#x60;name&#x60; | Alias name | | &#x60;notifyCreator&#x60; | Notify creator on every upload | | &#x60;expireAt&#x60; | Expiration date | | &#x60;createdAt&#x60; | Creation date | | &#x60;createdBy&#x60; | Creator first name, last name |  &lt;/details&gt;

    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str
    :param filter: Filter string
    :type filter: str
    :param sort: Sort string
    :type sort: str
    :param offset: Range offset
    :type offset: int
    :param limit: Range limit.  Maximum 500.   For more results please use paging (&#x60;offset&#x60; + &#x60;limit&#x60;).
    :type limit: int
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def send_download_share_link_via_email(request: web.Request, share_id, body, x_sds_auth_token=None) -> web.Response:
    """Send an existing Download Share link via email

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.11.0&lt;/h3&gt;  ### Description: Send an email to specific recipients for existing Download Share.  ### Precondition: User with &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage download share&lt;/span&gt; permissions on target node.  ### Postcondition: Download Share link successfully sent.  ### Further Information:  * Forbidden characters in the email body: [&#x60;&lt;&#x60;, &#x60;&gt;&#x60;] 

    :param share_id: Share ID
    :type share_id: int
    :param body: 
    :type body: dict | bytes
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = DownloadShareLinkEmail.from_dict(body)
    return web.Response(status=200)


async def send_upload_share_link_via_email(request: web.Request, share_id, body, x_sds_auth_token=None) -> web.Response:
    """Send an existing Upload Share link via email

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.11.0&lt;/h3&gt;  ### Description: Send an email to specific recipients for existing Upload Share.  ### Precondition: User with &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage upload share&lt;/span&gt; permissions on target container.  ### Postcondition: Upload Share link successfully sent.  ### Further Information:  * Forbidden characters in the email body: [&#x60;&lt;&#x60;, &#x60;&gt;&#x60;] 

    :param share_id: Share ID
    :type share_id: int
    :param body: 
    :type body: dict | bytes
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = UploadShareLinkEmail.from_dict(body)
    return web.Response(status=200)


async def update_download_share(request: web.Request, share_id, body, x_sds_date_format=None, x_sds_auth_token=None) -> web.Response:
    """Update Download Share

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.11.0&lt;/h3&gt;  ### Description: Update an existing Download Share.  ### Precondition: User with &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage download share&lt;/span&gt; permissions on target node.  ### Postcondition: Download Share is successfully updated.  ### Further Information: * &#x60;name&#x60; is limited to **150** characters. * &#x60;notes&#x60; are limited to **255** characters. * &#x60;password&#x60; is limited to **1024** characters.  Forbidden characters in passwords: [&#x60;&amp;&#x60;, &#x60;&#39;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;]  Please keep in mind that due to various restrictions of different telecommunication providers, non-ASCII characters may not be displayed correctly in short messages (SMS).

    :param share_id: Share ID
    :type share_id: int
    :param body: 
    :type body: dict | bytes
    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = UpdateDownloadShareRequest.from_dict(body)
    return web.Response(status=200)


async def update_download_shares(request: web.Request, body, x_sds_auth_token=None) -> web.Response:
    """Update a list of Download Shares

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.25.0&lt;/h3&gt;  ### Description: Update a list of existing Download Shares.  ### Precondition: User with &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage download share&lt;/span&gt; permissions on target node.  ### Postcondition: Download Shares are successfully updated.  ### Further Information: Maximum number of shares is 200

    :param body: 
    :type body: dict | bytes
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = UpdateDownloadSharesBulkRequest.from_dict(body)
    return web.Response(status=200)


async def update_upload_share(request: web.Request, share_id, body, x_sds_date_format=None, x_sds_auth_token=None) -> web.Response:
    """Update Upload Share

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.11.0&lt;/h3&gt;  ### Description: Update existing Upload Share (aka File Request).  ### Precondition: User has &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage upload share&lt;/span&gt; permissions on target container.  ### Postcondition: Upload Share successfully updated.  ### Further Information:  * &#x60;name&#x60; is limited to **150** characters. * &#x60;notes&#x60; are limited to **255** characters. * &#x60;password&#x60; is limited to **1024** characters.  Forbidden characters in passwords: [&#x60;&amp;&#x60;, &#x60;&#39;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;]  Please keep in mind that due to various restrictions of different telecommunication providers, non-ASCII characters may not be displayed correctly in short messages (SMS).

    :param share_id: Share ID
    :type share_id: int
    :param body: 
    :type body: dict | bytes
    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = UpdateUploadShareRequest.from_dict(body)
    return web.Response(status=200)


async def update_upload_shares(request: web.Request, body, x_sds_date_format=None, x_sds_auth_token=None) -> web.Response:
    """Update List of Upload Shares

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.25.0&lt;/h3&gt;  ### Description: Update a list of existing Upload Shares (aka File Request).  ### Precondition: User has &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage upload share&lt;/span&gt; permissions on target container.  ### Postcondition: Upload Shares successfully updated.  ### Further Information: Maximum number of shares is 200

    :param body: 
    :type body: dict | bytes
    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = UpdateUploadSharesBulkRequest.from_dict(body)
    return web.Response(status=200)
