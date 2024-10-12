from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_object_response import GetObjectResponse
from openapi_server.models.list_items_response import ListItemsResponse
from openapi_server.models.put_object_request import PutObjectRequest
from openapi_server.models.put_object_response import PutObjectResponse
from openapi_server import util


async def delete_object(request: web.Request, path, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_object

    Deletes an object at the specified path.

    :param path: The path (including the file name) where the object is stored in the container. Format: &amp;lt;folder name&amp;gt;/&amp;lt;folder name&amp;gt;/&amp;lt;file name&amp;gt;
    :type path: str
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


async def describe_object(request: web.Request, path, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_object

    Gets the headers for an object at the specified path.

    :param path: The path (including the file name) where the object is stored in the container. Format: &amp;lt;folder name&amp;gt;/&amp;lt;folder name&amp;gt;/&amp;lt;file name&amp;gt;
    :type path: str
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


async def get_object(request: web.Request, path, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, range=None) -> web.Response:
    """get_object

    Downloads the object at the specified path. If the object’s upload availability is set to &lt;code&gt;streaming&lt;/code&gt;, AWS Elemental MediaStore downloads the object even if it’s still uploading the object.

    :param path: &lt;p&gt;The path (including the file name) where the object is stored in the container. Format: &amp;lt;folder name&amp;gt;/&amp;lt;folder name&amp;gt;/&amp;lt;file name&amp;gt;&lt;/p&gt; &lt;p&gt;For example, to upload the file &lt;code&gt;mlaw.avi&lt;/code&gt; to the folder path &lt;code&gt;premium\\canada&lt;/code&gt; in the container &lt;code&gt;movies&lt;/code&gt;, enter the path &lt;code&gt;premium/canada/mlaw.avi&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Do not include the container name in this path.&lt;/p&gt; &lt;p&gt;If the path includes any folders that don&#39;t exist yet, the service creates them. For example, suppose you have an existing &lt;code&gt;premium/usa&lt;/code&gt; subfolder. If you specify &lt;code&gt;premium/canada&lt;/code&gt;, the service creates a &lt;code&gt;canada&lt;/code&gt; subfolder in the &lt;code&gt;premium&lt;/code&gt; folder. You then have two subfolders, &lt;code&gt;usa&lt;/code&gt; and &lt;code&gt;canada&lt;/code&gt;, in the &lt;code&gt;premium&lt;/code&gt; folder. &lt;/p&gt; &lt;p&gt;There is no correlation between the path to the source and the path (folders) in the container in AWS Elemental MediaStore.&lt;/p&gt; &lt;p&gt;For more information about folders and how they exist in a container, see the &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/mediastore/latest/ug/\&quot;&gt;AWS Elemental MediaStore User Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;The file name is the name that is assigned to the file that you upload. The file can have the same name inside and outside of AWS Elemental MediaStore, or it can have the same name. The file name can include or omit an extension. &lt;/p&gt;
    :type path: str
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
    :param range: The range bytes of an object to retrieve. For more information about the &lt;code&gt;Range&lt;/code&gt; header, see &lt;a href&#x3D;\&quot;http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35\&quot;&gt;http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35&lt;/a&gt;. AWS Elemental MediaStore ignores this header for partially uploaded objects that have streaming upload availability.
    :type range: str

    """
    return web.Response(status=200)


async def list_items(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, path=None, max_results=None, next_token=None) -> web.Response:
    """list_items

    Provides a list of metadata entries about folders and objects in the specified folder.

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
    :param path: The path in the container from which to retrieve items. Format: &amp;lt;folder name&amp;gt;/&amp;lt;folder name&amp;gt;/&amp;lt;file name&amp;gt;
    :type path: str
    :param max_results: &lt;p&gt;The maximum number of results to return per API request. For example, you submit a &lt;code&gt;ListItems&lt;/code&gt; request with &lt;code&gt;MaxResults&lt;/code&gt; set at 500. Although 2,000 items match your request, the service returns no more than the first 500 items. (The service also returns a &lt;code&gt;NextToken&lt;/code&gt; value that you can use to fetch the next batch of results.) The service might return fewer results than the &lt;code&gt;MaxResults&lt;/code&gt; value.&lt;/p&gt; &lt;p&gt;If &lt;code&gt;MaxResults&lt;/code&gt; is not included in the request, the service defaults to pagination with a maximum of 1,000 results per page.&lt;/p&gt;
    :type max_results: int
    :param next_token: &lt;p&gt;The token that identifies which batch of results that you want to see. For example, you submit a &lt;code&gt;ListItems&lt;/code&gt; request with &lt;code&gt;MaxResults&lt;/code&gt; set at 500. The service returns the first batch of results (up to 500) and a &lt;code&gt;NextToken&lt;/code&gt; value. To see the next batch of results, you can submit the &lt;code&gt;ListItems&lt;/code&gt; request a second time and specify the &lt;code&gt;NextToken&lt;/code&gt; value.&lt;/p&gt; &lt;p&gt;Tokens expire after 15 minutes.&lt;/p&gt;
    :type next_token: str

    """
    return web.Response(status=200)


async def put_object(request: web.Request, path, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, content_type=None, cache_control=None, x_amz_storage_class=None, x_amz_upload_availability=None) -> web.Response:
    """put_object

    Uploads an object to the specified path. Object sizes are limited to 25 MB for standard upload availability and 10 MB for streaming upload availability.

    :param path: &lt;p&gt;The path (including the file name) where the object is stored in the container. Format: &amp;lt;folder name&amp;gt;/&amp;lt;folder name&amp;gt;/&amp;lt;file name&amp;gt;&lt;/p&gt; &lt;p&gt;For example, to upload the file &lt;code&gt;mlaw.avi&lt;/code&gt; to the folder path &lt;code&gt;premium\\canada&lt;/code&gt; in the container &lt;code&gt;movies&lt;/code&gt;, enter the path &lt;code&gt;premium/canada/mlaw.avi&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Do not include the container name in this path.&lt;/p&gt; &lt;p&gt;If the path includes any folders that don&#39;t exist yet, the service creates them. For example, suppose you have an existing &lt;code&gt;premium/usa&lt;/code&gt; subfolder. If you specify &lt;code&gt;premium/canada&lt;/code&gt;, the service creates a &lt;code&gt;canada&lt;/code&gt; subfolder in the &lt;code&gt;premium&lt;/code&gt; folder. You then have two subfolders, &lt;code&gt;usa&lt;/code&gt; and &lt;code&gt;canada&lt;/code&gt;, in the &lt;code&gt;premium&lt;/code&gt; folder. &lt;/p&gt; &lt;p&gt;There is no correlation between the path to the source and the path (folders) in the container in AWS Elemental MediaStore.&lt;/p&gt; &lt;p&gt;For more information about folders and how they exist in a container, see the &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/mediastore/latest/ug/\&quot;&gt;AWS Elemental MediaStore User Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;The file name is the name that is assigned to the file that you upload. The file can have the same name inside and outside of AWS Elemental MediaStore, or it can have the same name. The file name can include or omit an extension. &lt;/p&gt;
    :type path: str
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
    :param content_type: The content type of the object.
    :type content_type: str
    :param cache_control: &lt;p&gt;An optional &lt;code&gt;CacheControl&lt;/code&gt; header that allows the caller to control the object&#39;s cache behavior. Headers can be passed in as specified in the HTTP at &lt;a href&#x3D;\&quot;https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9\&quot;&gt;https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Headers with a custom user-defined value are also accepted.&lt;/p&gt;
    :type cache_control: str
    :param x_amz_storage_class: Indicates the storage class of a &lt;code&gt;Put&lt;/code&gt; request. Defaults to high-performance temporal storage class, and objects are persisted into durable storage shortly after being received.
    :type x_amz_storage_class: str
    :param x_amz_upload_availability: &lt;p&gt;Indicates the availability of an object while it is still uploading. If the value is set to &lt;code&gt;streaming&lt;/code&gt;, the object is available for downloading after some initial buffering but before the object is uploaded completely. If the value is set to &lt;code&gt;standard&lt;/code&gt;, the object is available for downloading only when it is uploaded completely. The default value for this header is &lt;code&gt;standard&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;To use this header, you must also set the HTTP &lt;code&gt;Transfer-Encoding&lt;/code&gt; header to &lt;code&gt;chunked&lt;/code&gt;.&lt;/p&gt;
    :type x_amz_upload_availability: str

    """
    body = PutObjectRequest.from_dict(body)
    return web.Response(status=200)
