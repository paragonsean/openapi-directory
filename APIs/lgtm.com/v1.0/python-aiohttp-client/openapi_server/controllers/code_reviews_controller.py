from typing import List, Dict
from aiohttp import web

from openapi_server.models.code_review import CodeReview
from openapi_server.models.operation import Operation
from openapi_server import util


async def get_code_review(request: web.Request, review_id) -> web.Response:
    """Get results of code review

    Get the results of a code review using the review identifier for the task.  When you request a code review, the response includes a task result URL of the form: &#x60;/codereviews/{review-id}&#x60;.  This endpoint reports the results of a complete code review, or the status of a review  that&#39;s still in progress. 

    :param review_id: The identifier for the review (from the &#x60;task-result-url&#x60;).
    :type review_id: str

    """
    return web.Response(status=200)


async def request_review(request: web.Request, project_id, base, external_id, body, review_url=None, callback_url=None, callback_secret=None) -> web.Response:
    """Run code review for a patch

    Trigger the code review of a patch. This is available for projects with Git repositories.  Your request must include:    * Identifier for the base commit   * Patch generated using &#x60;git diff --binary&#x60; (see [git diff](https://git-scm.com/docs/git-diff))   * Header &#x60;Content-Type: application/octet-stream&#x60;   * For both LGTM.com and LGTM Enterprise, an access token with the &#x60;codereviews:write&#x60; scope  Note that if you make a request using Curl, you&#39;ll also need to add &#x60;--data-binary&#x60; to the request to ensure that the patch you supply in the body is sent with newlines unchanged. You can track the progress of the review using the task result URL returned on creation of the task, or by calling the &#x60;/operations&#x60; endpoint with the operations identifier returned by the request. For more information, see [Get operation status](https://lgtm.com/help/lgtm/api/api-v1#opIdgetOperation). Alternatively, if you supply a callback URL you&#39;ll get a post-back automatically on completion of the review.  When the review is complete, you can access the results using the task result URL. 

    :param project_id: The numeric project identifier.
    :type project_id: int
    :param base: The identifier for the base commit.
    :type base: str
    :param external_id: Your reference number for the code review.
    :type external_id: int
    :param body: The patch containing the code changes for review.
    :type body: str
    :param review_url: An informative back-link to an external system.
    :type review_url: str
    :param callback_url: The callback URL for LGTM to post to on completion of the review. When the code review is complete, the API sends an HTTP POST request to the callback URL with the result of the code review in the request body. The code review results in the request body are identical to the results accessed through the [&#x60;/codereviews/{review-id}&#x60;](https://lgtm.com/help/lgtm/api/api-v1#opIdgetCodeReview) end-point. If you specify a &#x60;callback-secret&#x60;, the request also includes an &#x60;x-lgtm-signature&#x60; header with a digital signature of the request&#39;s contents. 
    :type callback_url: str
    :param callback_secret: The &#x60;callback-secret&#x60; is used to compute a signature which is included in the &#x60;x-lgtm-signature&#x60; header of the callback response. The receiver of the callback can check the validity of the response by computing the signature using HMAC-SHA1 and verifying that it matches the &#x60;x-lgtm-signature&#x60; header value. The HMAC algorithm requires byte sequences as inputs for both the secret and the message. The callback secret string must be converted to bytes using UTF-8 encoding. The response body should ideally be read as a plain byte sequence. Conversion to, for example a JSON object, and back to a byte sequence might change the formatting, and would invalidate the signature. 
    :type callback_secret: str

    """
    return web.Response(status=200)
