from typing import List, Dict
from aiohttp import web

from openapi_server.models.accepted_document_result_object import AcceptedDocumentResultObject
from openapi_server.models.basic_status_result_object import BasicStatusResultObject
from openapi_server.models.comparison_set import ComparisonSet
from openapi_server.models.document_checks_result_object import DocumentChecksResultObject
from openapi_server.models.document_compare_result_object import DocumentCompareResultObject
from openapi_server.models.document_result_object import DocumentResultObject
from openapi_server.models.document_scan_result_object import DocumentScanResultObject
from openapi_server.models.document_search_result_object import DocumentSearchResultObject
from openapi_server.models.document_verify import DocumentVerify
from openapi_server.models.document_verify_result_object import DocumentVerifyResultObject
from openapi_server.models.error_object import ErrorObject
from openapi_server.models.identity_document_object import IdentityDocumentObject
from openapi_server import util


async def compare_document(request: web.Request, x_frankie_customer_id, comparison_set, x_frankie_customer_child_id=None, x_frankie_background=None) -> web.Response:
    """Create Document and Compare to Original.

    Creates a new document from the \&quot;toDocument\&quot; parameter (usual rules apply in that it must be a valid document, with no existing documentId). The compareDocument can be an existing documentId, or it too can be new as well.   * If existing (i.e. a valid DocumentId is supplied), it will be updated with any new data supplied before being sent to the comparison process.   * If new, then a new document will be created too, and the ID returned in the result.    The document scans are then sent for processing and comparison, such as comparing a selfie-video against a drivers licence photo.  * NOTE: This is NOT the verification process (see /document/verify)  * NOTE: This is NOT the OCR data extraction process either (see /document/scan) 

    :param x_frankie_customer_id: Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    :type x_frankie_customer_id: str
    :type x_frankie_customer_id: str
    :param comparison_set: Contains the document (compareDocument) we want to compare (toDocument) 
    :type comparison_set: dict | bytes
    :param x_frankie_customer_child_id: If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children. 
    :type x_frankie_customer_child_id: str
    :type x_frankie_customer_child_id: str
    :param x_frankie_background: If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
    :type x_frankie_background: int

    """
    comparison_set = ComparisonSet.from_dict(comparison_set)
    return web.Response(status=200)


async def create_document(request: web.Request, x_frankie_customer_id, x_frankie_customer_child_id=None, document=None) -> web.Response:
    """Create New Document.

    Create a document object. A document object can be used to simply store data around a given identity or similar document. You can attach scans, PDFs, photos, videos, etc to the objectif you wish and these may be processed later (using the /scan function) to extract useful information. Or you can manually supply the extracted information if you choose. Document objects can be used to create an entity, based on extracted or supplied data; or it may be attached to an existing entity, either directly or through an ID check. 

    :param x_frankie_customer_id: Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    :type x_frankie_customer_id: str
    :type x_frankie_customer_id: str
    :param x_frankie_customer_child_id: If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children. 
    :type x_frankie_customer_child_id: str
    :type x_frankie_customer_child_id: str
    :param document: 
    :type document: dict | bytes

    """
    document = IdentityDocumentObject.from_dict(document)
    return web.Response(status=200)


async def create_scan_document(request: web.Request, x_frankie_customer_id, x_frankie_customer_child_id=None, x_frankie_background=None, document=None) -> web.Response:
    """Create and OCR Scan Document.

    Create a document object. This is then processed to extract useful information and create an entity; or it may be attached to an entity, either directly or through an ID check. The service will attempt to extract relevant data from any/all uploaded images/documents and will place those in the extraData KVP block. 

    :param x_frankie_customer_id: Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    :type x_frankie_customer_id: str
    :type x_frankie_customer_id: str
    :param x_frankie_customer_child_id: If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children. 
    :type x_frankie_customer_child_id: str
    :type x_frankie_customer_child_id: str
    :param x_frankie_background: If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
    :type x_frankie_background: int
    :param document: 
    :type document: dict | bytes

    """
    document = IdentityDocumentObject.from_dict(document)
    return web.Response(status=200)


async def delete_document(request: web.Request, x_frankie_customer_id, document_id, x_frankie_customer_child_id=None, x_frankie_background=None) -> web.Response:
    """Delete Document.

    Mark this document as deleted. It will then become effectively invisible to all queries, but will be available in anonymised form for a past check. 

    :param x_frankie_customer_id: Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    :type x_frankie_customer_id: str
    :type x_frankie_customer_id: str
    :param document_id: The documentId returned previously from an earlier call to /check or /entity or /document
    :type document_id: str
    :type document_id: str
    :param x_frankie_customer_child_id: If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children. 
    :type x_frankie_customer_child_id: str
    :type x_frankie_customer_child_id: str
    :param x_frankie_background: If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
    :type x_frankie_background: int

    """
    return web.Response(status=200)


async def query_document(request: web.Request, x_frankie_customer_id, document_id, x_frankie_customer_child_id=None) -> web.Response:
    """Retrieve Document Details

    Query the current status and details of a given documentId. 

    :param x_frankie_customer_id: Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    :type x_frankie_customer_id: str
    :type x_frankie_customer_id: str
    :param document_id: The documentId returned previously from an earlier call to /check or /entity or /document
    :type document_id: str
    :type document_id: str
    :param x_frankie_customer_child_id: If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children. 
    :type x_frankie_customer_child_id: str
    :type x_frankie_customer_child_id: str

    """
    return web.Response(status=200)


async def query_document_checks(request: web.Request, x_frankie_customer_id, document_id, x_frankie_customer_child_id=None, x_frankie_background=None) -> web.Response:
    """Retrieve Document Verification Check Details. 

    Get the complete list of all checks that have been performed upon a given document, including the checks that have been performed by others (in those cases you just get the id, status and date run, none of the details). 

    :param x_frankie_customer_id: Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    :type x_frankie_customer_id: str
    :type x_frankie_customer_id: str
    :param document_id: The documentId returned previously from an earlier call to /check or /entity or /document
    :type document_id: str
    :type document_id: str
    :param x_frankie_customer_child_id: If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children. 
    :type x_frankie_customer_child_id: str
    :type x_frankie_customer_child_id: str
    :param x_frankie_background: If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
    :type x_frankie_background: int

    """
    return web.Response(status=200)


async def query_document_full(request: web.Request, x_frankie_customer_id, document_id, x_frankie_customer_child_id=None) -> web.Response:
    """Retrieve Document and Scan Data

    Query the current status and details of a given documentId. Also returns all document file data, not just the metadata. 

    :param x_frankie_customer_id: Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    :type x_frankie_customer_id: str
    :type x_frankie_customer_id: str
    :param document_id: The documentId returned previously from an earlier call to /check or /entity or /document
    :type document_id: str
    :type document_id: str
    :param x_frankie_customer_child_id: If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children. 
    :type x_frankie_customer_child_id: str
    :type x_frankie_customer_child_id: str

    """
    return web.Response(status=200)


async def search_document(request: web.Request, x_frankie_customer_id, search_document, x_frankie_customer_child_id=None) -> web.Response:
    """Search For a Document !! EXPERIMENTAL !!

     Search for an existing document that matches the criteria supplied  There are of course limits to what can be searched upon. For a document search to work, you must supply at a minimum:    * idType   * country   * idNumber  The service will return a list of matching documents with confidence levels.  If you are the \&quot;owner\&quot; of the document - i.e. the same CustomerID and CustomerChildID (if relevant) - then the full details of the document will be returned, except for the contents of any attached scans. If you are not the owner of the document, then just the ID and confidence level is returned. You can still use this ID to retrieve any check results (see GET /document/{documentId}/checks)  Note: At this time, we cannot perform searches on document scans. But, you can supply extraData KVPs if they&#39;re known. These will help doublecheck search results with ambiguous results. 

    :param x_frankie_customer_id: Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    :type x_frankie_customer_id: str
    :type x_frankie_customer_id: str
    :param search_document: A document object with the parameters you wish to search on. 
    :type search_document: dict | bytes
    :param x_frankie_customer_child_id: If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children. 
    :type x_frankie_customer_child_id: str
    :type x_frankie_customer_child_id: str

    """
    search_document = IdentityDocumentObject.from_dict(search_document)
    return web.Response(status=200)


async def update_compare_document(request: web.Request, x_frankie_customer_id, document_id, comparison_set, x_frankie_customer_child_id=None, x_frankie_background=None) -> web.Response:
    """Update Document and Compare to Original.

    Send the attached document scans to an external service for processing and comparison, such as comparing a selfie-video against a drivers licence photo.  * NOTE: This is NOT the verification process (see /document/verify)  * NOTE: This is NOT the OCR data extraction process either (see /document/scan) 

    :param x_frankie_customer_id: Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    :type x_frankie_customer_id: str
    :type x_frankie_customer_id: str
    :param document_id: The documentId returned previously from an earlier call to /check or /entity or /document
    :type document_id: str
    :type document_id: str
    :param comparison_set: Contains the document (compareDocument) we want to compare (toDocument).  In this case, the toDocument should be left blank, and is assumed to be \&quot;this\&quot; document 
    :type comparison_set: dict | bytes
    :param x_frankie_customer_child_id: If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children. 
    :type x_frankie_customer_child_id: str
    :type x_frankie_customer_child_id: str
    :param x_frankie_background: If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
    :type x_frankie_background: int

    """
    comparison_set = ComparisonSet.from_dict(comparison_set)
    return web.Response(status=200)


async def update_document(request: web.Request, x_frankie_customer_id, document_id, document, x_frankie_customer_child_id=None, x_frankie_background=None, no_invalidate=None) -> web.Response:
    """Update Existing Document.

    Using a previously uploaded but incomplete document, you can optionally supply updated details (such as corrections on a previous scan), along with one or more additional ID scans (e.g. additional pages). 

    :param x_frankie_customer_id: Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    :type x_frankie_customer_id: str
    :type x_frankie_customer_id: str
    :param document_id: The documentId returned previously from an earlier call to /check or /entity or /document
    :type document_id: str
    :type document_id: str
    :param document: The document to be updated
    :type document: dict | bytes
    :param x_frankie_customer_child_id: If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children. 
    :type x_frankie_customer_child_id: str
    :type x_frankie_customer_child_id: str
    :param x_frankie_background: If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
    :type x_frankie_background: int
    :param no_invalidate: Disable check result invalidation for this update request. 
    :type no_invalidate: bool

    """
    document = IdentityDocumentObject.from_dict(document)
    return web.Response(status=200)


async def update_scan_document(request: web.Request, x_frankie_customer_id, document_id, document, x_frankie_customer_child_id=None, x_frankie_background=None) -> web.Response:
    """Update and OCR Scan Document

    Using a previously uploaded but potentially incomplete document, you can optionally supply updated details (such as corrections on a previous scan), along with one or more additional ID scans (e.g. additional pages). Includes a follow-on action as well initiating OCR processing proceedures immediately. The service will attempt to extract relevant data from any/all uploaded images/documents and will place those in the extraData KVP block. 

    :param x_frankie_customer_id: Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    :type x_frankie_customer_id: str
    :type x_frankie_customer_id: str
    :param document_id: The documentId returned previously from an earlier call to /check or /entity or /document
    :type document_id: str
    :type document_id: str
    :param document: The entity to be optionally updated, then processed. If updating a document, you only need to populate the fields you&#39;re actually adding/updating. 
    :type document: dict | bytes
    :param x_frankie_customer_child_id: If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children. 
    :type x_frankie_customer_child_id: str
    :type x_frankie_customer_child_id: str
    :param x_frankie_background: If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
    :type x_frankie_background: int

    """
    document = IdentityDocumentObject.from_dict(document)
    return web.Response(status=200)


async def update_verify_document(request: web.Request, x_frankie_customer_id, document_id, process_document, x_frankie_customer_child_id=None, x_frankie_background=None) -> web.Response:
    """Update and Verify Document.

    Using a previously uploaded but potentially incomplete document, you can optionally supply updated details (such as corrections on a previous scan), along with one or more additional ID scans (e.g. additional pages). Includes a follow-on action as well initiating verification proceedures immediately.  Sends the updated document to an external service to have the detailed verified.  For example, we could send through the details of a drivers licence to be checked against a national database.  * NOTE: This is NOT the OCR data extraction process (see /document/scan) * NOTE: This is NOT the comparison process (see /document/compare) 

    :param x_frankie_customer_id: Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    :type x_frankie_customer_id: str
    :type x_frankie_customer_id: str
    :param document_id: The documentId returned previously from an earlier call to /check or /entity or /document
    :type document_id: str
    :type document_id: str
    :param process_document: The document and (possibly) its associated scans to be verified.  There is also an optional entity object (normally stripped back to it&#39;s bare minimum) that can be used to provide supporting data, such as name, address, etc. The entity object may be empty, and is not processed or stored in any way. 
    :type process_document: dict | bytes
    :param x_frankie_customer_child_id: If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children. 
    :type x_frankie_customer_child_id: str
    :type x_frankie_customer_child_id: str
    :param x_frankie_background: If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
    :type x_frankie_background: int

    """
    process_document = DocumentVerify.from_dict(process_document)
    return web.Response(status=200)


async def verify_document(request: web.Request, x_frankie_customer_id, process_document, x_frankie_customer_child_id=None, x_frankie_background=None) -> web.Response:
    """Create and Verify Document.

    Send the document to an external service to have the detailed verified.  For example, we could send through the details of a drivers licence to be checked against a national database.  * NOTE: This is NOT the OCR data extraction process (see /document/scan) * NOTE: This is NOT the comparison process (see /document/compare) 

    :param x_frankie_customer_id: Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    :type x_frankie_customer_id: str
    :type x_frankie_customer_id: str
    :param process_document: The document and (possibly) its associated scans to be verified.  There is also an entity object (normally stripped back to it&#39;s bare minimum) that can be used to provide supporting data, such as name, address, etc. The entity object may be empty/ 
    :type process_document: dict | bytes
    :param x_frankie_customer_child_id: If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children. 
    :type x_frankie_customer_child_id: str
    :type x_frankie_customer_child_id: str
    :param x_frankie_background: If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
    :type x_frankie_background: int

    """
    process_document = DocumentVerify.from_dict(process_document)
    return web.Response(status=200)
