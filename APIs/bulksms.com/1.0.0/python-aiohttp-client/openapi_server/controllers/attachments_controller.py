from typing import List, Dict
from aiohttp import web

from openapi_server.models.pre_sign_info import PreSignInfo
from openapi_server.models.pre_sign_request import PreSignRequest
from openapi_server import util


async def rmm_pre_sign_attachment_post(request: web.Request, body) -> web.Response:
    """Upload an attachment via a signed URL

    When composing an SMS, you can add SMS attachments by adding a URL to your text. When the recipient clicks on the URL, the attached file will be downloaded and opened on their mobile device.    The best way to do this is to store the file on a web server you own and use that URL in the SMS text. This URL will be easily recognisable to your message recipient and ties your message back to your brand or company.   If that’s not possible, you can use BulkSMS storage to keep the files that you want to attach to your SMS. These files will be deleted after 30 days as per our fair use policy.    We recommend you keep this file size below 20 MB, as larger files may be deleted without warning.   To use the BulkSMS storage, follow these three steps:  **Step 1**: Use your BulkSMS credentials (or your API Token) to request a pre-signed URL.  This is what this &#x60;pre-sign-attachment&#x60; method is for.  It returns a PreSignInfo object that you will use in the other two steps.  **Step 2**: Upload the file using a standard HTTP &#x60;PUT&#x60; request. For your &#x60;PUT&#x60; request, use the value of &#x60;putURL&#x60; from the PreSignInfo object as the request address.  You also have to add the entries from the &#x60;fields&#x60; property (of the PreSignInfo object) to the headers of your &#39;PUT&#39; request. You send the file content as the body of the &#x60;PUT&#x60; request.  **Step 3**: Now you can use the value of &#x60;fetchURL&#x60; from the PreSignInfo object in the body of your SMS messages and send those using the usual messaging API (described elsewhere in this document).  If you send the same file to many recipients, it is safe to use the same URL for all of them.  If you need to, take a closer look at the example program (on the right-hand side) to get a better idea of how to implement this process. 

    :param body: Describes the file to upload
    :type body: dict | bytes

    """
    body = PreSignRequest.from_dict(body)
    return web.Response(status=200)
