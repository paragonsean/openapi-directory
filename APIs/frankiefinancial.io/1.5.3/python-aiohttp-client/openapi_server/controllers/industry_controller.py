from typing import List, Dict
from aiohttp import web

from openapi_server.models.accepted_document_result_object import AcceptedDocumentResultObject
from openapi_server.models.document_industry_utility_consent_result_object import DocumentIndustryUtilityConsentResultObject
from openapi_server.models.document_industry_utility_process_result_object import DocumentIndustryUtilityProcessResultObject
from openapi_server.models.document_industry_utility_switch_result_object import DocumentIndustryUtilitySwitchResultObject
from openapi_server.models.eic_request import EICRequest
from openapi_server.models.error_object import ErrorObject
from openapi_server.models.identity_document_object import IdentityDocumentObject
from openapi_server.models.switch_request import SwitchRequest
from openapi_server import util


async def create_process_industry_utility_document(request: web.Request, x_frankie_customer_id, x_frankie_customer_child_id=None, x_frankie_background=None, plan_limit=None, document=None) -> web.Response:
    """Create Document and Run Utility Price Comparison.

    Create a document object. This is then processed to extract useful information, just like a normal OCR scan. The service will then push the document through an industry specific comparison process, where the details are used to find a better plan, based on the bill.  100&#39;s of datapoints are accurately extracted from the uploaded document. This data is then used to compare the bill against the whole market. A personalised comparison is returned that is a best fit for the customer&#39;s energy profile.  * NOTE: It is expected that the type of document being uploaded will be a PDF and the idType is UTILITY_BILL. (These values will be set automatically if not supplied).    You can optionally include the utility name (e.g. Origin Energy) in the idSubType if you wish. 

    :param x_frankie_customer_id: Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    :type x_frankie_customer_id: str
    :type x_frankie_customer_id: str
    :param x_frankie_customer_child_id: If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children. 
    :type x_frankie_customer_child_id: str
    :type x_frankie_customer_child_id: str
    :param x_frankie_background: If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
    :type x_frankie_background: int
    :param plan_limit: The maximum number of plans to return
    :type plan_limit: int
    :param document: 
    :type document: dict | bytes

    """
    document = IdentityDocumentObject.from_dict(document)
    return web.Response(status=200)


async def update_process_industry_utility_document(request: web.Request, x_frankie_customer_id, document_id, x_frankie_customer_child_id=None, x_frankie_background=None, plan_limit=None, document=None) -> web.Response:
    """Update Document and Run Utility Price Comparison.

    Using a previously uploaded but incomplete document, you can optionally supply updated details or simply request that the document be re-processed through the industry comparison service.   100&#39;s of datapoints are accurately extracted from the uploaded document. This data is then used to compare the bill against the whole market. A personalised comparison is returned that is a best fit for the customer&#39;s energy profile.  * NOTE: It is expected that the type of document being uploaded will be a PDF and the idType is UTILITY_BILL. (These values will be set automatically if not supplied).    You can optionally include the utility name (e.g. Origin Energy) in the idSubType if you wish. 

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
    :param plan_limit: The maximum number of plans to return
    :type plan_limit: int
    :param document: 
    :type document: dict | bytes

    """
    document = IdentityDocumentObject.from_dict(document)
    return web.Response(status=200)


async def update_process_industry_utility_document_consent(request: web.Request, x_frankie_customer_id, document_id, x_frankie_customer_child_id=None, x_frankie_background=None, consent_request=None) -> web.Response:
    """Provide Explicit Consent to Switch Utility Plans.

    Using a previously uploaded and processed document, the user must provide explicit consent before being able to call the /switch function.   Before entering into a contract with a new energy retailer, consumers are first obliged to review the retailer&#39;s contractual terms and conditions, confirm they understand these terms as well as give explicit, informed consent (EIC) for the switch to occur. This API call retrieves all information        that must be displayed in order for a compliant EIC to be captured from a consumer.  * NOTE: as part of this call, you must provide a previously returned corellationId that is associated with this document and the returned plan options. Failure to do so will result in an error response. 

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
    :param consent_request: 
    :type consent_request: dict | bytes

    """
    consent_request = EICRequest.from_dict(consent_request)
    return web.Response(status=200)


async def update_process_industry_utility_document_switch(request: web.Request, x_frankie_customer_id, document_id, x_frankie_customer_child_id=None, x_frankie_background=None, switch_request=None) -> web.Response:
    """Initiate Switching of Utility Plan.

    Using a previously uploaded and processed document, the user must provide explicit consent before being able to call the /switch function.   The bill payer has uploaded their current bill, selected a new plan, accepted the terms and conditions and given their consent for the switch to occur. This API call will finalise the switch request and send all the customers data along with the requested plan to the selected retailer.  * NOTE: as part of this call, you must provide a previously returned corellationId that is associated with this document and the returned plan options. Failure to do so will result in an error response. 

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
    :param switch_request: 
    :type switch_request: dict | bytes

    """
    switch_request = SwitchRequest.from_dict(switch_request)
    return web.Response(status=200)
