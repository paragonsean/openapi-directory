from typing import List, Dict
from aiohttp import web

from openapi_server.models.active_directory_auth_info import ActiveDirectoryAuthInfo
from openapi_server.models.chunk_upload_response import ChunkUploadResponse
from openapi_server.models.complete_s3_share_upload_request import CompleteS3ShareUploadRequest
from openapi_server.models.create_share_upload_channel_request import CreateShareUploadChannelRequest
from openapi_server.models.create_share_upload_channel_response import CreateShareUploadChannelResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.generate_presigned_urls_request import GeneratePresignedUrlsRequest
from openapi_server.models.open_id_auth_info import OpenIdAuthInfo
from openapi_server.models.presigned_url_list import PresignedUrlList
from openapi_server.models.public_download_share import PublicDownloadShare
from openapi_server.models.public_download_token_generate_request import PublicDownloadTokenGenerateRequest
from openapi_server.models.public_download_token_generate_response import PublicDownloadTokenGenerateResponse
from openapi_server.models.public_upload_share import PublicUploadShare
from openapi_server.models.public_uploaded_file_data import PublicUploadedFileData
from openapi_server.models.s3_share_upload_status import S3ShareUploadStatus
from openapi_server.models.sds_server_time import SdsServerTime
from openapi_server.models.software_version_data import SoftwareVersionData
from openapi_server.models.system_info import SystemInfo
from openapi_server.models.third_party_dependencies_data import ThirdPartyDependenciesData
from openapi_server.models.user_file_key_list import UserFileKeyList
from openapi_server import util


async def cancel_file_upload_via_share(request: web.Request, access_key, upload_id) -> web.Response:
    """Cancel file upload

    ### Description: Abort (chunked) upload via Upload Share.  ### Precondition: Valid Upload ID.  ### Postcondition: Aborts upload and invalidates upload ID / token.  ### Further Information: None.

    :param access_key: Access key
    :type access_key: str
    :param upload_id: Upload channel ID
    :type upload_id: str

    """
    return web.Response(status=200)


async def check_public_download_share_password(request: web.Request, access_key, password=None) -> web.Response:
    """Check public Download Share password

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.36.0&lt;/h3&gt;  ### Description: Check password for a public Download Share  ### Precondition: None.  ### Postcondition: None.  ### Further Information: None.

    :param access_key: Access key
    :type access_key: str
    :param password: Download share password
    :type password: str

    """
    return web.Response(status=200)


async def complete_file_upload_via_share(request: web.Request, access_key, upload_id, x_sds_date_format=None, body=None) -> web.Response:
    """Complete file upload

    ### Description: Finalize (chunked) upload via Upload Share.  ### Precondition: Valid upload ID.   Only returns users that owns one of the following permissions: &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage&lt;/span&gt;, &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read&lt;/span&gt;, &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage download share&lt;/span&gt;, &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage upload share&lt;/span&gt;  ### Postcondition: Finalizes upload.  ### Further Information: Chunked uploads (range requests) are supported.    Please ensure that all chunks have been transferred correctly before finishing the upload.   If file hash has been created in time a &#x60;201 Created&#x60; will be responded and hash will be part of response, otherwise it will be a &#x60;202 Accepted&#x60; without it. 

    :param access_key: Access key
    :type access_key: str
    :param upload_id: Upload channel ID
    :type upload_id: str
    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str
    :param body: 
    :type body: dict | bytes

    """
    body = UserFileKeyList.from_dict(body)
    return web.Response(status=200)


async def complete_s3_file_upload_via_share(request: web.Request, access_key, upload_id, body) -> web.Response:
    """Complete S3 file upload

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.15.0&lt;/h3&gt;  ### Description: Finishes a S3 file upload and closes the corresponding upload channel.  ### Precondition: Valid upload ID.   Only returns users that owns one of the following permissions: &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage&lt;/span&gt;, &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read&lt;/span&gt;, &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage download share&lt;/span&gt;, &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage upload share&lt;/span&gt;  ### Postcondition: Upload channel is closed. S3 multipart upload request is completed.  ### Further Information: None. 

    :param access_key: Access key
    :type access_key: str
    :param upload_id: Upload channel ID
    :type upload_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CompleteS3ShareUploadRequest.from_dict(body)
    return web.Response(status=200)


async def create_share_upload_channel(request: web.Request, access_key, body) -> web.Response:
    """Create new file upload channel

    ### Description:   Create a new upload channel.  ### Precondition: None.  ### Postcondition: Upload channel is created and corresponding upload URL, token &amp; upload ID are returned.  ### Further Information: Use &#x60;uploadUrl&#x60; the upload &#x60;token&#x60; is deprecated.    Please provide the size of the intended upload so that the quota can be checked in advanced and no data is transferred unnecessarily.  ### Node naming convention: * Node (room, folder, file) names are limited to **150** characters. * Illegal names:   &#x60;&#39;CON&#39;, &#39;PRN&#39;, &#39;AUX&#39;, &#39;NUL&#39;, &#39;COM1&#39;, &#39;COM2&#39;, &#39;COM3&#39;, &#39;COM4&#39;, &#39;COM5&#39;, &#39;COM6&#39;, &#39;COM7&#39;, &#39;COM8&#39;, &#39;COM9&#39;, &#39;LPT1&#39;, &#39;LPT2&#39;, &#39;LPT3&#39;, &#39;LPT4&#39;, &#39;LPT5&#39;, &#39;LPT6&#39;, &#39;LPT7&#39;, &#39;LPT8&#39;, &#39;LPT9&#39;, (and any of those with an extension)&#x60; * Illegal characters in names:   &#x60;&#39;\\\\&#39;, &#39;&lt;&#39;,&#39;&gt;&#39;, &#39;:&#39;, &#39;\\\&quot;&#39;, &#39;|&#39;, &#39;?&#39;, &#39;*&#39;, &#39;/&#39;, leading &#39;-&#39;, trailing &#39;.&#39; &#x60; 

    :param access_key: Access key
    :type access_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateShareUploadChannelRequest.from_dict(body)
    return web.Response(status=200)


async def download_file_via_token_public(request: web.Request, access_key, token, range=None, generic_mimetype=None, inline=None) -> web.Response:
    """Download file with token

    ### Description:   Download a file (or zip archive if target is a folder or room).  ### Precondition: Valid download token.  ### Postcondition: Stream is returned.  ### Further Information: Range requests are supported.   Range requests are illegal for zip archive download.

    :param access_key: Access key
    :type access_key: str
    :param token: Download token
    :type token: str
    :param range: Range   e.g. &#x60;bytes&#x3D;0-999&#x60;
    :type range: str
    :param generic_mimetype: Always return &#x60;application/octet-stream&#x60; instead of specific mimetype
    :type generic_mimetype: bool
    :param inline: Use Content-Disposition: &#x60;inline&#x60; instead of &#x60;attachment&#x60;
    :type inline: bool

    """
    return web.Response(status=200)


async def download_file_via_token_public1(request: web.Request, access_key, token, range=None, generic_mimetype=None, inline=None) -> web.Response:
    """Download file with token

    ### Description:   Download a file (or zip archive if target is a folder or room).  ### Precondition: Valid download token.  ### Postcondition: Stream is returned.  ### Further Information: Range requests are supported.   Range requests are illegal for zip archive download.

    :param access_key: Access key
    :type access_key: str
    :param token: Download token
    :type token: str
    :param range: Range   e.g. &#x60;bytes&#x3D;0-999&#x60;
    :type range: str
    :param generic_mimetype: Always return &#x60;application/octet-stream&#x60; instead of specific mimetype
    :type generic_mimetype: bool
    :param inline: Use Content-Disposition: &#x60;inline&#x60; instead of &#x60;attachment&#x60;
    :type inline: bool

    """
    return web.Response(status=200)


async def generate_download_url_public(request: web.Request, access_key, body=None) -> web.Response:
    """Generate download URL

    ### Description: Generate a download URL to retrieve a shared file.  ### Precondition: None.  ### Postcondition: Download URL and token are generated and returned.  ### Further Information: Use &#x60;downloadUrl&#x60; the download &#x60;token&#x60; is deprecated.

    :param access_key: Access key
    :type access_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = PublicDownloadTokenGenerateRequest.from_dict(body)
    return web.Response(status=200)


async def generate_presigned_urls_public(request: web.Request, access_key, upload_id, body, x_sds_date_format=None) -> web.Response:
    """Generate presigned URLs for S3 file upload

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.15.0&lt;/h3&gt;  ### Description: Generate presigned URLs for S3 file upload.  ### Precondition: Valid upload ID  ### Postcondition: List of presigned URLs is returned.  ### Further Information: The size for each part must be &gt;&#x3D; 5 MB, except for the last part.   The part number of the first part in S3 is 1 (not 0).   Use HTTP method &#x60;PUT&#x60; for uploading bytes via presigned URL.

    :param access_key: Access key
    :type access_key: str
    :param upload_id: Upload channel ID
    :type upload_id: str
    :param body: 
    :type body: dict | bytes
    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str

    """
    body = GeneratePresignedUrlsRequest.from_dict(body)
    return web.Response(status=200)


async def request_active_directory_auth_info(request: web.Request, is_global_available=None) -> web.Response:
    """Request Active Directory authentication information

    ### Description:   Provides information about Active Directory authentication options.  ### Precondition: None.  ### Postcondition: Active Directory authentication options information is returned.  ### Further Information: None.

    :param is_global_available: Show only global available items
    :type is_global_available: bool

    """
    return web.Response(status=200)


async def request_open_id_auth_info(request: web.Request, is_global_available=None) -> web.Response:
    """Request OpenID Connect provider authentication information

    ### Description:   Provides information about OpenID Connect authentication options.  ### Precondition: None.  ### Postcondition: OpenID Connect authentication options information is returned.  ### Further Information: None.

    :param is_global_available: Show only global available items
    :type is_global_available: bool

    """
    return web.Response(status=200)


async def request_public_download_share_info(request: web.Request, access_key, x_sds_date_format=None) -> web.Response:
    """Request public Download Share information

    ### Description:   Retrieve the public information of a Download Share.  ### Precondition: None.  ### Postcondition: Download Share information is returned.  ### Further Information: None.

    :param access_key: Access key
    :type access_key: str
    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str

    """
    return web.Response(status=200)


async def request_public_upload_share_info(request: web.Request, access_key, x_sds_share_password=None, x_sds_date_format=None) -> web.Response:
    """Request public Upload Share information

    ### Description:   Provides information about the desired Upload Share.  ### Precondition: Only &#x60;userUserPublicKeyList&#x60; is returned to the users who owns one of the following permissions: &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage&lt;/span&gt;, &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read&lt;/span&gt;, &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage download share&lt;/span&gt;, &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage upload share&lt;/span&gt;  ### Postcondition: None.  ### Further Information: If no password is set, the returned information is reduced to the following attributes (if available):  * &#x60;name&#x60; * &#x60;createdAt&#x60; * &#x60;isProtected&#x60; * &#x60;isEncrypted&#x60; * &#x60;showUploadedFiles&#x60; * &#x60;userUserPublicKeyList&#x60; (if parent is end-to-end encrypted)  Only if the password is transmitted as &#x60;X-Sds-Share-Password&#x60; header, all values are returned. 

    :param access_key: Access key
    :type access_key: str
    :param x_sds_share_password: Upload share password. Should be base64-encoded.  Plain X-Sds-Share-Passwords are *deprecated* and will be removed in the future
    :type x_sds_share_password: str
    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str

    """
    return web.Response(status=200)


async def request_software_version(request: web.Request, x_sds_date_format=None) -> web.Response:
    """Request software version information

    ### Description:   Public software version information.  ### Precondition: None.  ### Postcondition: Sofware version information is returned.  ### Further Information: The version of DRACOON Server consists of two components: * **API** * **Core** (referred to as _\&quot;Server\&quot;_)  which are versioned individually.

    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str

    """
    return web.Response(status=200)


async def request_system_info(request: web.Request, is_enabled=None) -> web.Response:
    """Request system information

    ### Description:   Provides information about system.  ### Precondition: None.  ### Postcondition: System information is returned.  ### Further Information: Authentication methods are sorted by **priority** attribute.   Smaller values have higher priority.   Authentication method with highest priority is considered as default.  ### System information: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Setting | Description | Value | | :--- | :--- | :--- | | &#x60;languageDefault&#x60; | Defines which language should be default. | &#x60;ISO 639-1 code&#x60; | | &#x60;hideLoginInputFields&#x60; | Defines if login fields should be hidden. | &#x60;true or false&#x60; | | &#x60;s3Hosts&#x60; | List of available S3 hosts. | &#x60;String array&#x60; | | &#x60;s3EnforceDirectUpload&#x60; | Determines whether S3 direct upload is enforced or not. | &#x60;true or false&#x60; | | &#x60;useS3Storage&#x60; | Determines whether S3 Storage enabled and used. | &#x60;true or false&#x60; |  &lt;/details&gt;  ### Authentication methods: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Authentication Method | Description | | :--- | :--- | | &#x60;basic&#x60; | **Basic** authentication globally allowed.&lt;br&gt;This option **MUST** be activated to allow users to log in with their credentials stored in the database.&lt;br&gt;Formerly known as &#x60;sql&#x60;. | | &#x60;active_directory&#x60; | **Active Directory** authentication globally allowed.&lt;br&gt;This option **MUST** be activated to allow users to log in with their Active Directory credentials. | | &#x60;radius&#x60; | **RADIUS** authentication globally allowed.&lt;br&gt;This option **MUST** be activated to allow users to log in with their RADIUS username, their PIN and a token password. | | &#x60;openid&#x60; | **OpenID Connect** authentication globally allowed.This option **MUST** be activated to allow users to log in with their OpenID Connect identity. | | &#x60;hideLoginInputFields&#x60; | Determines whether input fields for login should be enabled | &#x60;true or false&#x60; |  &lt;/details&gt;

    :param is_enabled: Show only enabled authentication methods
    :type is_enabled: bool

    """
    return web.Response(status=200)


async def request_system_time(request: web.Request, x_sds_date_format=None) -> web.Response:
    """Request system time

    ### Description:   Retrieve the actual server time.  ### Precondition: None.  ### Postcondition: Server time is returned.  ### Further Information: None.

    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str

    """
    return web.Response(status=200)


async def request_third_party_dependencies(request: web.Request, ) -> web.Response:
    """Request third-party software dependencies

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.9.0&lt;/h3&gt;  ### Description:   Provides information about used third-party software dependencies.  ### Precondition: None.  ### Postcondition: List of the third-party software dependencies used by **DRACOON Core** (referred to as _\&quot;Server\&quot;_) is returned.  ### Further Information: None.  


    """
    return web.Response(status=200)


async def request_upload_status_public(request: web.Request, access_key, upload_id) -> web.Response:
    """Request status of S3 file upload

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.15.0&lt;/h3&gt;  ### Description: Request status of a S3 file upload.  ### Precondition: An upload channel has been created and the user has &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; create&lt;/span&gt; permissions in the parent container (room or folder).  ### Postcondition: Status of S3 multipart upload request is returned.  ### Further Information: None.  ### Possible errors: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Http Status | Error Code | Description | | :--- | :--- | :--- | | &#x60;400 Bad Request&#x60; | &#x60;-80000&#x60; | Mandatory fields cannot be empty | | &#x60;400 Bad Request&#x60; | &#x60;-80001&#x60; | Invalid positive number | | &#x60;400 Bad Request&#x60; | &#x60;-80002&#x60; | Invalid number | | &#x60;400 Bad Request&#x60; | &#x60;-40001&#x60; | (Target) room is not encrypted | | &#x60;400 Bad Request&#x60; | &#x60;-40755&#x60; | Bad file name | | &#x60;400 Bad Request&#x60; | &#x60;-40763&#x60; | File key must be set for an upload into encrypted room | | &#x60;400 Bad Request&#x60; | &#x60;-50506&#x60; | Exceeds the number of files for this Upload Share | | &#x60;403 Forbidden&#x60; |  | Access denied | | &#x60;404 Not Found&#x60; | &#x60;-20501&#x60; | Upload not found | | &#x60;404 Not Found&#x60; | &#x60;-40000&#x60; | Container not found | | &#x60;404 Not Found&#x60; | &#x60;-41000&#x60; | Node not found | | &#x60;404 Not Found&#x60; | &#x60;-70501&#x60; | User not found | | &#x60;409 Conflict&#x60; | &#x60;-40010&#x60; | Container cannot be overwritten | | &#x60;409 Conflict&#x60; |  | File cannot be overwritten | | &#x60;500 Internal Server Error&#x60; |  | System Error | | &#x60;502 Bad Gateway&#x60; |  | S3 Error | | &#x60;502 Insufficient Storage&#x60; | &#x60;-50504&#x60; | Exceeds the quota for this Upload Share | | &#x60;502 Insufficient Storage&#x60; | &#x60;-40200&#x60; | Exceeds the free node quota in room | | &#x60;502 Insufficient Storage&#x60; | &#x60;-90200&#x60; | Exceeds the free customer quota | | &#x60;502 Insufficient Storage&#x60; | &#x60;-90201&#x60; | Exceeds the free customer physical disk space |  &lt;/details&gt;

    :param access_key: Access key
    :type access_key: str
    :param upload_id: Upload channel ID
    :type upload_id: str

    """
    return web.Response(status=200)


async def upload_file_as_multipart_public1(request: web.Request, access_key, upload_id, file, content_range=None, x_sds_date_format=None) -> web.Response:
    """Upload file

    ### Description:   Chunked upload of files via Upload Share.  ### Precondition: Valid upload ID.  ### Postcondition: Chunk of file is uploaded.  ### Further Information: Chunked uploads (range requests) are supported.  Following &#x60;Content-Types&#x60; are supported by this API: * &#x60;multipart/form-data&#x60; * provided &#x60;Content-Type&#x60;    For both file upload types set the correct &#x60;Content-Type&#x60; header and body.    ### Examples:    * &#x60;multipart/form-data&#x60; &#x60;&#x60;&#x60; POST /api/v4/public/shares/uploads/{access_key}{upload_id} HTTP/1.1  Header: ... Content-Type: multipart/form-data; boundary&#x3D;----WebKitFormBoundary7MA4YWxkTrZu0gW ...  Body: ------WebKitFormBoundary7MA4YWxkTrZu0gW Content-Disposition: form-data; name&#x3D;\&quot;file\&quot;; filename&#x3D;\&quot;file.txt\&quot; Content-Type: text/plain  Content of file.txt ------WebKitFormBoundary7MA4YWxkTrZu0gW-- &#x60;&#x60;&#x60;  * any other &#x60;Content-Type&#x60;   &#x60;&#x60;&#x60; POST /api/v4/public/shares/uploads/{access_key}{upload_id} HTTP/1.1  Header: ... Content-Type: { ... } ...  Body: raw content &#x60;&#x60;&#x60;

    :param access_key: Access key
    :type access_key: str
    :param upload_id: Upload channel ID
    :type upload_id: str
    :param file: File
    :type file: str
    :param content_range: Content-Range   e.g. &#x60;bytes 0-999/3980&#x60;
    :type content_range: str
    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str

    """
    return web.Response(status=200)
