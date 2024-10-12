from typing import List, Dict
from aiohttp import web

from openapi_server.models.document_upload_failure import DocumentUploadFailure
from openapi_server.models.document_upload_status_guid_list import DocumentUploadStatusGuidList
from openapi_server.models.get_benefits_document_upload_status200_response import GetBenefitsDocumentUploadStatus200Response
from openapi_server.models.get_benefits_document_upload_status404_response import GetBenefitsDocumentUploadStatus404Response
from openapi_server.models.get_benefits_document_upload_status_report200_response import GetBenefitsDocumentUploadStatusReport200Response
from openapi_server.models.post_benefits_document_upload202_response import PostBenefitsDocumentUpload202Response
from openapi_server.models.post_benefits_document_upload403_response import PostBenefitsDocumentUpload403Response
from openapi_server.models.post_benefits_document_upload_validate_document200_response import PostBenefitsDocumentUploadValidateDocument200Response
from openapi_server.models.post_benefits_document_upload_validate_document422_response import PostBenefitsDocumentUploadValidateDocument422Response
from openapi_server.models.put_benefits_document_upload401_response import PutBenefitsDocumentUpload401Response
from openapi_server.models.put_benefits_document_upload422_response import PutBenefitsDocumentUpload422Response
from openapi_server.models.put_benefits_document_upload429_response import PutBenefitsDocumentUpload429Response
from openapi_server.models.put_benefits_document_upload500_response import PutBenefitsDocumentUpload500Response
from openapi_server import util


async def get_benefits_document_upload_download(request: web.Request, id) -> web.Response:
    """Download zip of \&quot;what the server sees\&quot;

    An endpoint that will allow you to see exactly what the server sees. We split apart all submitted docs and metadata and zip the file to make it available to you to help with debugging purposes. Files are deleted after 10 days. Only available in testing environments, not production.

    :param id: ID as returned by a previous create upload request
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def get_benefits_document_upload_status(request: web.Request, id) -> web.Response:
    """Get status for a previous benefits document upload

    

    :param id: ID as returned by a previous create upload request
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def get_benefits_document_upload_status_report(request: web.Request, body) -> web.Response:
    """Get a bulk status report for a list of previous uploads

    

    :param body: List of GUIDs for which to retrieve current status
    :type body: dict | bytes

    """
    body = DocumentUploadStatusGuidList.from_dict(body)
    return web.Response(status=200)


async def post_benefits_document_upload(request: web.Request, ) -> web.Response:
    """Get a location for subsequent document upload PUT request

    


    """
    return web.Response(status=200)


async def post_benefits_document_upload_validate_document(request: web.Request, ) -> web.Response:
    """Validate an individual document against system file requirements

    Using this endpoint will decrease the likelihood of errors associated with individual documents during the submission process. Validations performed: * Document is a valid PDF (Note: &#x60;Content-Type&#x60; header value must be \&quot;application/pdf\&quot;) * Document does not have a user password (an owner password is acceptable) * File size does not exceed 100 MB * Page size does not exceed 21\&quot; x 21\&quot;  Each PDF document is sent as a direct file upload. The request body should contain nothing other than the document in binary format. Binary multipart/form-data encoding is not supported. This endpoint does NOT validate metadata in JSON format.  This endpoint does NOT initiate the claims intake process or submit data to that process. After using this endpoint, individual PDF documents can be combined and submitted as a payload using PUT &#x60;/path&#x60;.  A &#x60;200&#x60; response confirms that the individual document provided passes the system requirements.  A &#x60;422&#x60; response indicates one or more problems with the document that should be resolved before submitting it in the full document submission payload. 


    """
    return web.Response(status=200)


async def put_benefits_document_upload(request: web.Request, content_md5=None) -> web.Response:
    """Accepts document upload.

    Accepts document metadata, document binary, and attachment binaries. Full URL, including query parameters, provided from POST &#x60;/document_uploads&#x60;.  ## Example Payload  The following demonstrates a (redacted) multipart payload suitable for submitting to the PUT endpoint. Most programming languages should have provisions for assembling a multipart payload like this without having to do so manually.  &#x60;&#x60;&#x60; --17de1ed8f01442b2a2d7a93506314b76 Content-Disposition: form-data; name&#x3D;\&quot;metadata\&quot; Content-Type: application/json  {\&quot;veteranFirstName\&quot;: \&quot;Jane\&quot;, \&quot;veteranLastName\&quot;: \&quot;Doe\&quot;, \&quot;fileNumber\&quot;: \&quot;012345678\&quot;, \&quot;zipCode\&quot;: \&quot;97202\&quot;, \&quot;source\&quot;: \&quot;MyVSO\&quot;, \&quot;docType\&quot;: \&quot;21-22\&quot; \&quot;businessLine\&quot;: \&quot;CMP\&quot;} --17de1ed8f01442b2a2d7a93506314b76 Content-Disposition: form-data; name&#x3D;\&quot;content\&quot; Content-Type: application/pdf  &lt;Binary PDF contents&gt; --17de1ed8f01442b2a2d7a93506314b76 Content-Disposition: form-data; name&#x3D;\&quot;attachment1\&quot; Content-Type: application/pdf  &lt;Binary PDF attachment contents&gt; --17de1ed8f01442b2a2d7a93506314b76-- &#x60;&#x60;&#x60;  This PUT request would have an overall HTTP Content-Type header:  &#x60;&#x60;&#x60; Content-Type: multipart/form-data; boundary&#x3D;17de1ed8f01442b2a2d7a93506314b76 &#x60;&#x60;&#x60;  Note that the Content-Disposition parameter \&quot;name\&quot; in each part must be the expected values \&quot;metadata\&quot;, \&quot;content\&quot;, \&quot;attachment1\&quot;...\&quot;attachmentN\&quot;. The attachment attributes must be named  exactly as they are listed here (case sensitive), for example: \&quot;attachment_1\&quot; or \&quot;Attachment2\&quot; are invalid.  This is an example curl command:  &#x60;&#x60;&#x60; curl -v -L -X PUT &#39;&lt;Location from \\uploads&gt;&#39; -F &#39;metadata&#x3D;\&quot;{\\\&quot;veteranFirstName\\\&quot;: \\\&quot;Jane\\\&quot;,\\\&quot;veteranLastName\\\&quot;: \\\&quot;Doe\\\&quot;,\\\&quot;fileNumber\\\&quot;: \\\&quot;012345678\\\&quot;,\\\&quot;zipCode\\\&quot;: \\\&quot;97202\\\&quot;,\\\&quot;source\\\&quot;: \\\&quot;MyVSO\\\&quot;,\\\&quot;docType\\\&quot;: \\\&quot;21-22\\\&quot;,\\\&quot;businessLine\\\&quot;: \\\&quot;CMP\\\&quot;}\&quot;;type&#x3D;application/json&#39; -F &#39;content&#x3D;@\&quot;content.pdf\&quot;&#39; -F &#39;attachment1&#x3D;@\&quot;file1.pdf\&quot;&#39; -F &#39;attachment2&#x3D;@\&quot;another_file.pdf\&quot;&#39; &#x60;&#x60;&#x60; 

    :param content_md5: Base64-encoded 128-bit MD5 digest of the message. Use for integrity control
    :type content_md5: str

    """
    return web.Response(status=200)
