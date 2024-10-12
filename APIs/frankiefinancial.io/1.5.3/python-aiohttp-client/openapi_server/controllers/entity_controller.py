from typing import List, Dict
from aiohttp import web

from openapi_server.models.accepted_entity_result_object import AcceptedEntityResultObject
from openapi_server.models.basic_status_result_object import BasicStatusResultObject
from openapi_server.models.check_entity_check_result_object import CheckEntityCheckResultObject
from openapi_server.models.check_result_update_object import CheckResultUpdateObject
from openapi_server.models.entity_check_details_object import EntityCheckDetailsObject
from openapi_server.models.entity_idv_details_object import EntityIDVDetailsObject
from openapi_server.models.entity_idv_result_object import EntityIDVResultObject
from openapi_server.models.entity_object import EntityObject
from openapi_server.models.entity_result_object import EntityResultObject
from openapi_server.models.entity_search_result_object import EntitySearchResultObject
from openapi_server.models.error_object import ErrorObject
from openapi_server import util


async def create_check_entity(request: web.Request, x_frankie_customer_id, check_type, result_level, entity_details, x_frankie_customer_child_id=None, x_frankie_background=None) -> web.Response:
    """Create and Verify Entity

    Create an entity object. An entity object can be used to simply store data around a given identity. You can attach ID documents, scans, PDFs, photos, videos, etc to the entity if you wish and these may be processed later (using the /scan function) to extract useful information. Or you can manually supply the  information if you choose.  If the entity is successfully created, take the details and documents provided, and set about verifying them all. So for example, you might extract:  * The name from the entity.name object * The address from the entity.address object * The DoB..  All documents that are attached to the entity will also be verified (if possible).  You can also specify the level of detail returned using the resultLevel parameter. You can choose \&quot;summary\&quot; or \&quot;full\&quot;. For the \&quot;profile\&quot; check type you can also select \&quot;simple\&quot; to only get the entity profile result.  SPECIAL NOTE: A \&quot;Full\&quot; response includes details of all checks and how they map against each element, along with all the details of pep/sanctions/etc checks too.  Your account also needs to be configured to support a full response too (talk to your account manager for more information). If you&#39;re not configured for full responses, we&#39;ll only return summary level data regardless. 

    :param x_frankie_customer_id: Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    :type x_frankie_customer_id: str
    :type x_frankie_customer_id: str
    :param check_type: When creating a new check, you need to define the checks you wish to run.    The checkType is make up of a comma separated list of the types of check you wish to run. The order of the requested checks is not important, they will be re-ordered by the service and in some cases, depending on your account configuration, may be skipped.    The validation that is performed on the requested checks is to:   - ensure the check type is known   - is suitable for the type of entity (no KYC for organisations)   - disallow manual (mKYC) check with any other kind of KYC   - disallow mixing the \&quot;profile\&quot; check with any other kind of check.  The supported check types are:  Profile:   - \&quot;profile\&quot;: By arrangement with Frankie we will create a \&quot;profile\&quot; check type that applies checks according to a recipe that you assign to the entity from a predefined set of profiles.      The profile to use will be taken from the entity.entityProfile field if set, or be run through a set of configurable rules to determine which one to use.      Profiles provide a pre-defined combination of individual checkTypes (see the list below). But they offer a lot more besides, including rules for determining default settings, inbuilt data aging and other configurable features.   They also allow for a new result set top be returned that provides a more detailed and useful breakdown of the check/verification process.      Entity Profiles are a recent feature (since v1.4.0) but are now the default checkType to use with Frankie Financial.  **Individual Check Types**  Whilst we strongly recommend the use of the \&quot;profile\&quot; checktype, it does map of any combination of the types below. If you wish to use these individually, please contact developer support for more details on how to use these effectively.  Entity Checks - One of:   - \&quot;one_plus\&quot;: Checks name, address and DoB against a minimum of 1 data source. (also known as a 1+1)   - \&quot;two_plus\&quot;: Checks name, address and DoB against a minimum of 2 independent data sources (also known as a 2+2)  ID Checks - One of:   - \&quot;id\&quot;: Checks all of the identity documents, but not necessarily the entity itself independently. Use this in conjunction with a one_plus or two_plus for more.   - \&quot;visa\&quot;:    ID Validate - One of:   - \&quot;idvalidate\&quot;: Checks to see if photo ID has had OCR scanning, ID document validation and photo comparison run against it. Can be used in conjunction with any of the KYC/ID/AML checks.    Manual Check:   - \&quot;manual\&quot;: (mKYC) Checks user has a sufficient amount of operator verified ID and will then \&quot;pass\&quot; all Entity and ID related checks.    Fraud Checks - One or more of:   - \&quot;fraudlist\&quot;: Checks to see if the identity appears on any known fraud lists. Should be run after KYC/ID checks have passed.   - \&quot;fraudcheck\&quot;: Checks external ID services to see if details appear in fraud detection services (e.g. EmailAge or FraudNet)    PEP Checks - One of:   - \&quot;pep\&quot;: Will only run PEP/Sanctions checks (no identity verification)   - \&quot;pep_media\&quot;: Will run PEP/Sanctions checks, as well as watchlist and adverse media checks. (no identity verification)      * NOTE: These checks will ONLY run if either the KYC/ID checks have been run prior, or it is the only check requested.    Custom:   - By arrangement with Frankie you can define your own KYC check type.      This will allow you to set the minimum number of matches for:     - name      - date of birth     - address     - government id      This allows for alternatives to the \&quot;standard\&quot; two_plus or one_plus (note, these can be overridden too). 
    :type check_type: str
    :param result_level: How much detail we return.   Acceptable values are:   * simple - Only available with \&quot;profile\&quot; check type. Returns just an EntityProfileResultObject (which is also included for \&quot;profile\&quot; checks at the other result levels), and a CheckEntityCheckResultObjectEntityResult with just the entity details but no separate results.   * summary   * full - You need to have your account configured for this. 
    :type result_level: str
    :param entity_details: The entity and any associated / additional information to be checked
    :type entity_details: dict | bytes
    :param x_frankie_customer_child_id: If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children. 
    :type x_frankie_customer_child_id: str
    :type x_frankie_customer_child_id: str
    :param x_frankie_background: If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
    :type x_frankie_background: int

    """
    entity_details = EntityCheckDetailsObject.from_dict(entity_details)
    return web.Response(status=200)


async def create_check_entity_push_to_mobile(request: web.Request, x_frankie_customer_id, entity_details, x_frankie_customer_child_id=None, x_frankie_background=None, nopush=None) -> web.Response:
    """Create Entity and Push Self-Verification Link

    Create an entity object and begin the process of verification after pushing a message to a mobile number.  The entity will receive a link on their mobile and will then be guided through a series of steps to capture and OCR scan their ID, and perform a selfie comparison. We&#39;ll then attempt to verify the data received and push a notification back to the calling customer.  At a minimum, you will need to supply the name and a MOBILE_PHONE document type.   SPECIAL NOTE: This will only ever return a 202 response if successfully accepted. You will need to ensure your account is configured for push notifications. Contact developer supprt to arrange this. 

    :param x_frankie_customer_id: Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    :type x_frankie_customer_id: str
    :type x_frankie_customer_id: str
    :param entity_details: The entity and any associated / additional information to be checked
    :type entity_details: dict | bytes
    :param x_frankie_customer_child_id: If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children. 
    :type x_frankie_customer_child_id: str
    :type x_frankie_customer_child_id: str
    :param x_frankie_background: If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
    :type x_frankie_background: int
    :param nopush: If set to true, then no SMS/email will be pushed. It will be up to the API caller to manage the delivery of the link. 
    :type nopush: bool

    """
    entity_details = EntityCheckDetailsObject.from_dict(entity_details)
    return web.Response(status=200)


async def create_entity(request: web.Request, x_frankie_customer_id, x_frankie_customer_child_id=None, entity=None) -> web.Response:
    """Create New Entity.

    Create an entity object. An entity object can be used to simply store data around a given identity. You can attach ID documents, scans, PDFs, photos, videos, etc to the entity if you wish and these may be processed later (using the /scan function) to extract useful information. Or you can manually supply the  information if you choose.  Entity objects can be used to run a check, using the data held in the records. 

    :param x_frankie_customer_id: Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    :type x_frankie_customer_id: str
    :type x_frankie_customer_id: str
    :param x_frankie_customer_child_id: If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children. 
    :type x_frankie_customer_child_id: str
    :type x_frankie_customer_child_id: str
    :param entity: 
    :type entity: dict | bytes

    """
    entity = EntityObject.from_dict(entity)
    return web.Response(status=200)


async def create_entity_get_idv_token(request: web.Request, x_frankie_customer_id, entity_idv_details, x_frankie_customer_child_id=None) -> web.Response:
    """Create Entity and Get IDV Token

    Create an entity object and if successful, obtain a token for use in an ID Validation service SDK (web or native app)   At a minimum, you will need to supply:  - the entity familyName.   - the entity givenName    For best results, you should gather the DoB, address, ID document details as well before  calling the initProcess function.  SPECIAL NOTE 1: Tokens have a limited lifespan, typically only 1 hour. Make sure you&#39;ve used it or you will need to create another using update version of this function.   SPECIAL NOTE 2: This function will need to be followed up with a call to /entity/{id}/idvalidate/initProcess once you&#39;ve collected all your data in your app/web capture process. 

    :param x_frankie_customer_id: Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    :type x_frankie_customer_id: str
    :type x_frankie_customer_id: str
    :param entity_idv_details: The entity and required data to generate an IDV token
    :type entity_idv_details: dict | bytes
    :param x_frankie_customer_child_id: If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children. 
    :type x_frankie_customer_child_id: str
    :type x_frankie_customer_child_id: str

    """
    entity_idv_details = EntityIDVDetailsObject.from_dict(entity_idv_details)
    return web.Response(status=200)


async def delete_entity(request: web.Request, x_frankie_customer_id, entity_id, x_frankie_customer_child_id=None, x_frankie_background=None) -> web.Response:
    """Delete Entity

    Marks the entity as deleted in the system, and no further operations or general queries may be executed against it by the Customer. If another customer is presently relying on this data, it will still be available to them (but only in the partially anonymised form they originally had.  An entity and its related data is only completely deleted from the database when either:    - a) There are no more references to it (i.e. it has been DELETEd by all Customers relying on the data), and 12 months have passed.      - b) The actual consumer who owns the data makes a direct request. If this occurs, then all subscribing Customers will be notified that this entity has been removed and they will need to contact them if needed in order to update their own records again. 

    :param x_frankie_customer_id: Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    :type x_frankie_customer_id: str
    :type x_frankie_customer_id: str
    :param entity_id: The entityId returned previously from an earlier call to /check or /entity
    :type entity_id: str
    :type entity_id: str
    :param x_frankie_customer_child_id: If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children. 
    :type x_frankie_customer_child_id: str
    :type x_frankie_customer_child_id: str
    :param x_frankie_background: If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
    :type x_frankie_background: int

    """
    return web.Response(status=200)


async def query_entity(request: web.Request, x_frankie_customer_id, entity_id, x_frankie_customer_child_id=None) -> web.Response:
    """Retrieve Entity Details

    Query the current status and details of a given entityId. 

    :param x_frankie_customer_id: Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    :type x_frankie_customer_id: str
    :type x_frankie_customer_id: str
    :param entity_id: The entityId returned previously from an earlier call to /check or /entity
    :type entity_id: str
    :type entity_id: str
    :param x_frankie_customer_child_id: If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children. 
    :type x_frankie_customer_child_id: str
    :type x_frankie_customer_child_id: str

    """
    return web.Response(status=200)


async def query_entity_checks(request: web.Request, x_frankie_customer_id, entity_id, x_frankie_customer_child_id=None, alldata=None) -> web.Response:
    """Retrieve Entity Verication Check Details 

    Get the complete list of all checks that have been performed upon a given entity and its documents, including the checks that have been performed by others (in those cases you just get the id, status and date run, none of the details). 

    :param x_frankie_customer_id: Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    :type x_frankie_customer_id: str
    :type x_frankie_customer_id: str
    :param entity_id: The entityId returned previously from an earlier call to /check or /entity
    :type entity_id: str
    :type entity_id: str
    :param x_frankie_customer_child_id: If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children. 
    :type x_frankie_customer_child_id: str
    :type x_frankie_customer_child_id: str
    :param alldata: Requests that literally all data should be included in the response to a \&quot;get checks\&quot; request. This is as opposed to a filtered view where expired results are by default not included for entities that have an assigned profile. 
    :type alldata: bool

    """
    return web.Response(status=200)


async def query_entity_full(request: web.Request, x_frankie_customer_id, entity_id, x_frankie_customer_child_id=None) -> web.Response:
    """Retrieve Entity Details and Document Scan Data 

    Query the current status and details of a given entityId. Also returns all attached document file data, not just the metadata. Equivalent to a get /document/{documentId}/full) 

    :param x_frankie_customer_id: Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    :type x_frankie_customer_id: str
    :type x_frankie_customer_id: str
    :param entity_id: The entityId returned previously from an earlier call to /check or /entity
    :type entity_id: str
    :type entity_id: str
    :param x_frankie_customer_child_id: If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children. 
    :type x_frankie_customer_child_id: str
    :type x_frankie_customer_child_id: str

    """
    return web.Response(status=200)


async def search_entity(request: web.Request, x_frankie_customer_id, search_entity, x_frankie_customer_child_id=None) -> web.Response:
    """Search for Entity

     Search for an existing entity that matches the criteria supplied  Criteria are supplied in the form of a populated entity object, with the name/address/DoB details supplied. You can also include documents that can be used to further refine your search (see the /document/search function for minimum requirements for a document search)  At an absolute minimum, you must supply one of the following combinations:    * name.familyName +   * name.givenNames      or      * name.familyName +   * one identityDocument object (that meets minimum criteria)    Obviously, the more data you provide, the better search results we can provide.  The service will return a list of matching entities with confidence levels.  If you are the \&quot;owner\&quot; of the entity - i.e. the same CustomerID and CustomerChildID (if relevant) - then the full details of the entity and any owned documents will be returned, except for the contents of any attached scans.  If you are not the owner of the entity (or linked documents), then just the ID and confidence level is returned. You can still use this ID to retrieve any check results (see GET  /entity/{entityId}/checks and GET /document/{documentId}/checks)  Note: This functionality must be enabled by Frankie administrators. Please contact your sales representative if you wish to discuss this. 

    :param x_frankie_customer_id: Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    :type x_frankie_customer_id: str
    :type x_frankie_customer_id: str
    :param search_entity: An entity object with the parameters you wish to search on. 
    :type search_entity: dict | bytes
    :param x_frankie_customer_child_id: If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children. 
    :type x_frankie_customer_child_id: str
    :type x_frankie_customer_child_id: str

    """
    search_entity = EntityObject.from_dict(search_entity)
    return web.Response(status=200)


async def update_check_class_result(request: web.Request, x_frankie_customer_id, entity_id, check_id, check_class, check_class_id, status, x_frankie_customer_child_id=None, undo=None) -> web.Response:
    """Update Check Result State

    Internal only  Update a given KYC or AML check result status in order to force a re-evaluation of the overall check result. 

    :param x_frankie_customer_id: Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    :type x_frankie_customer_id: str
    :type x_frankie_customer_id: str
    :param entity_id: The entityId returned previously from an earlier call to /check or /entity
    :type entity_id: str
    :type entity_id: str
    :param check_id: The checkId returned previously from an earlier call to */verify
    :type check_id: str
    :type check_id: str
    :param check_class: Specify which check Class this action will apply to (PRO, BCRO etc.). Valid values are:   - \&quot;pro\&quot;: Update a Process Result Object   - \&quot;bcro\&quot;: Update a Background Check Result Object. The class IDs in the request must be the IDs from Background Check Result Object Containers.   - \&quot;fraudlist\&quot;: Update a fraud list Process Result Object. The class IDs in the request must be check sources from fraudlist Process Result Objects. 
    :type check_class: str
    :param check_class_id: A PRO/BCRO ID 
    :type check_class_id: str
    :param status: Set the new status of the Check Class (PRO/BCRO). Valid values are:   - \&quot;unknown\&quot;   - \&quot;true_positive\&quot;   - \&quot;true_positive_accept\&quot;   - \&quot;true_positive_reject\&quot;   - \&quot;false_positive\&quot;   - \&quot;stale\&quot; 
    :type status: str
    :param x_frankie_customer_child_id: If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children. 
    :type x_frankie_customer_child_id: str
    :type x_frankie_customer_child_id: str
    :param undo: Undo a prior operation. 
    :type undo: bool

    """
    return web.Response(status=200)


async def update_check_class_results(request: web.Request, x_frankie_customer_id, entity_id, check_id, check_class, check_result_update, x_frankie_customer_child_id=None) -> web.Response:
    """Update Check Result States (Batch)

    Internal only  Update a given set of KYC and/or AML check result statuses in order to force a re-evaluation of the overall check result. 

    :param x_frankie_customer_id: Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    :type x_frankie_customer_id: str
    :type x_frankie_customer_id: str
    :param entity_id: The entityId returned previously from an earlier call to /check or /entity
    :type entity_id: str
    :type entity_id: str
    :param check_id: The checkId returned previously from an earlier call to */verify
    :type check_id: str
    :type check_id: str
    :param check_class: Specify which check Class this action will apply to (PRO, BCRO etc.). Valid values are:   - \&quot;pro\&quot;: Update a Process Result Object   - \&quot;bcro\&quot;: Update a Background Check Result Object. The class IDs in the request must be the IDs from Background Check Result Object Containers.   - \&quot;fraudlist\&quot;: Update a fraud list Process Result Object. The class IDs in the request must be check sources from fraudlist Process Result Objects. 
    :type check_class: str
    :param check_result_update: The check result status change details to apply
    :type check_result_update: dict | bytes
    :param x_frankie_customer_child_id: If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children. 
    :type x_frankie_customer_child_id: str
    :type x_frankie_customer_child_id: str

    """
    check_result_update = CheckResultUpdateObject.from_dict(check_result_update)
    return web.Response(status=200)


async def update_check_entity(request: web.Request, x_frankie_customer_id, entity_id, check_type, result_level, entity_details, x_frankie_customer_child_id=None, x_frankie_background=None, force=None, no_invalidate=None) -> web.Response:
    """Update Entity and Verify Details

    Take the details and documents provided in the entity, and set about verifying them all. So for example, you might extract:  * The name from the entity.name object * The address from the entity.address object * The DoB..  All documents that are presently attached to the entity will also be verified (if requested)  You can also specify the level of detail returned using the resultLevel parameter. You can choose \&quot;summary\&quot; or \&quot;full\&quot;. For the \&quot;profile\&quot; check type you can also select \&quot;simple\&quot; to only get the entity profile result.  SPECIAL NOTE: A \&quot;Full\&quot; response includes details of all checks and how they map against each element, along with all the details of pep/sanctions/etc checks too.  Your account also needs to be configured to support a full response too (talk to your account manager for more information). If you&#39;re not configured for full responses, we&#39;ll only return summary level data regardless. 

    :param x_frankie_customer_id: Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    :type x_frankie_customer_id: str
    :type x_frankie_customer_id: str
    :param entity_id: The entityId returned previously from an earlier call to /check or /entity
    :type entity_id: str
    :type entity_id: str
    :param check_type: When creating a new check, you need to define the checks you wish to run.    The checkType is make up of a comma separated list of the types of check you wish to run. The order of the requested checks is not important, they will be re-ordered by the service and in some cases, depending on your account configuration, may be skipped.    The validation that is performed on the requested checks is to:   - ensure the check type is known   - is suitable for the type of entity (no KYC for organisations)   - disallow manual (mKYC) check with any other kind of KYC   - disallow mixing the \&quot;profile\&quot; check with any other kind of check.  The supported check types are:  Profile:   - \&quot;profile\&quot;: By arrangement with Frankie we will create a \&quot;profile\&quot; check type that applies checks according to a recipe that you assign to the entity from a predefined set of profiles.      The profile to use will be taken from the entity.entityProfile field if set, or be run through a set of configurable rules to determine which one to use.      Profiles provide a pre-defined combination of individual checkTypes (see the list below). But they offer a lot more besides, including rules for determining default settings, inbuilt data aging and other configurable features.   They also allow for a new result set top be returned that provides a more detailed and useful breakdown of the check/verification process.      Entity Profiles are a recent feature (since v1.4.0) but are now the default checkType to use with Frankie Financial.  **Individual Check Types**  Whilst we strongly recommend the use of the \&quot;profile\&quot; checktype, it does map of any combination of the types below. If you wish to use these individually, please contact developer support for more details on how to use these effectively.  Entity Checks - One of:   - \&quot;one_plus\&quot;: Checks name, address and DoB against a minimum of 1 data source. (also known as a 1+1)   - \&quot;two_plus\&quot;: Checks name, address and DoB against a minimum of 2 independent data sources (also known as a 2+2)  ID Checks - One of:   - \&quot;id\&quot;: Checks all of the identity documents, but not necessarily the entity itself independently. Use this in conjunction with a one_plus or two_plus for more.   - \&quot;visa\&quot;:    ID Validate - One of:   - \&quot;idvalidate\&quot;: Checks to see if photo ID has had OCR scanning, ID document validation and photo comparison run against it. Can be used in conjunction with any of the KYC/ID/AML checks.    Manual Check:   - \&quot;manual\&quot;: (mKYC) Checks user has a sufficient amount of operator verified ID and will then \&quot;pass\&quot; all Entity and ID related checks.    Fraud Checks - One or more of:   - \&quot;fraudlist\&quot;: Checks to see if the identity appears on any known fraud lists. Should be run after KYC/ID checks have passed.   - \&quot;fraudcheck\&quot;: Checks external ID services to see if details appear in fraud detection services (e.g. EmailAge or FraudNet)    PEP Checks - One of:   - \&quot;pep\&quot;: Will only run PEP/Sanctions checks (no identity verification)   - \&quot;pep_media\&quot;: Will run PEP/Sanctions checks, as well as watchlist and adverse media checks. (no identity verification)      * NOTE: These checks will ONLY run if either the KYC/ID checks have been run prior, or it is the only check requested.    Custom:   - By arrangement with Frankie you can define your own KYC check type.      This will allow you to set the minimum number of matches for:     - name      - date of birth     - address     - government id      This allows for alternatives to the \&quot;standard\&quot; two_plus or one_plus (note, these can be overridden too). 
    :type check_type: str
    :param result_level: How much detail we return.   Acceptable values are:   * simple - Only available with \&quot;profile\&quot; check type. Returns just an EntityProfileResultObject (which is also included for \&quot;profile\&quot; checks at the other result levels), and a CheckEntityCheckResultObjectEntityResult with just the entity details but no separate results.   * summary   * full - You need to have your account configured for this. 
    :type result_level: str
    :param entity_details: The entity to be checked
    :type entity_details: dict | bytes
    :param x_frankie_customer_child_id: If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children. 
    :type x_frankie_customer_child_id: str
    :type x_frankie_customer_child_id: str
    :param x_frankie_background: If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
    :type x_frankie_background: int
    :param force: Force the verification to run, overriding any data aging or past check 
    :type force: bool
    :param no_invalidate: Disable check result invalidation for this update request. 
    :type no_invalidate: bool

    """
    entity_details = EntityCheckDetailsObject.from_dict(entity_details)
    return web.Response(status=200)


async def update_check_entity_push_to_mobile(request: web.Request, x_frankie_customer_id, entity_id, entity_details, x_frankie_customer_child_id=None, x_frankie_background=None, nopush=None, phase=None) -> web.Response:
    """Update Entity and Push Self-Verification Link

    Update an existing entity object and begin the process of verification after pushing a message to a mobile number.  The entity will receive a link on their mobile and will then be guided through a series of steps to capture and OCR scan their ID, and perform a selfie comparison. We&#39;ll then attempt to verify the data received and push a notification back to the calling customer.  At a minimum, you will need to supply the name and a MOBILE_PHONE document type.         If you wish to skip the detail capture and jump straight to the ID and selfie capture, the append the call with the ?phase&#x3D;2 parameter.   SPECIAL NOTE: This will only ever return a 202 response if successfully accepted. You will need to ensure your account is configured for push notifications. Contact developer supprt to arrange this. 

    :param x_frankie_customer_id: Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    :type x_frankie_customer_id: str
    :type x_frankie_customer_id: str
    :param entity_id: The entityId returned previously from an earlier call to /check or /entity
    :type entity_id: str
    :type entity_id: str
    :param entity_details: The entity and any associated / additional information to be checked
    :type entity_details: dict | bytes
    :param x_frankie_customer_child_id: If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children. 
    :type x_frankie_customer_child_id: str
    :type x_frankie_customer_child_id: str
    :param x_frankie_background: If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
    :type x_frankie_background: int
    :param nopush: If set to true, then no SMS/email will be pushed. It will be up to the API caller to manage the delivery of the link. 
    :type nopush: bool
    :param phase: Set the Push To Mobile phase.  Currently supported values: - 2 
    :type phase: int

    """
    entity_details = EntityCheckDetailsObject.from_dict(entity_details)
    return web.Response(status=200)


async def update_entity(request: web.Request, x_frankie_customer_id, entity_id, entity, x_frankie_customer_child_id=None, x_frankie_background=None, no_invalidate=None) -> web.Response:
    """Update Existing Entity.

    Using a previously uploaded but incomplete Entity, you can optionally supply updated details (such as corrections on a previous address), along with one or more additional ID docs/scans (e.g. new documents to parse, etc). 

    :param x_frankie_customer_id: Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    :type x_frankie_customer_id: str
    :type x_frankie_customer_id: str
    :param entity_id: The entityId returned previously from an earlier call to /check or /entity
    :type entity_id: str
    :type entity_id: str
    :param entity: The entity to be updated
    :type entity: dict | bytes
    :param x_frankie_customer_child_id: If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children. 
    :type x_frankie_customer_child_id: str
    :type x_frankie_customer_child_id: str
    :param x_frankie_background: If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
    :type x_frankie_background: int
    :param no_invalidate: Disable check result invalidation for this update request. 
    :type no_invalidate: bool

    """
    entity = EntityObject.from_dict(entity)
    return web.Response(status=200)


async def update_entity_get_idv_token(request: web.Request, x_frankie_customer_id, entity_id, entity_idv_details, x_frankie_customer_child_id=None) -> web.Response:
    """Update Entity and Get IDV Token

    Update an entity object and if successful, obtain a token for use in an ID Validation service SDK (web or native app)   At a minimum, the entity will need to have a name. For best results, you should gather the DoB, address, ID document details as well before calling the initProcess function.  SPECIAL NOTE 1: Tokens have a limited lifespan, typically only 1 hour. Make sure you&#39;ve used it or you will need to create another using update version of this function.   SPECIAL NOTE 2: This function will need to be followed up with a call to /entity/{id}/idvalidate/initProcess once you&#39;ve collected all your data in your app/web capture process. 

    :param x_frankie_customer_id: Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    :type x_frankie_customer_id: str
    :type x_frankie_customer_id: str
    :param entity_id: The entityId returned previously from an earlier call to /check or /entity
    :type entity_id: str
    :type entity_id: str
    :param entity_idv_details: The entity to update and required data to generate an IDV token
    :type entity_idv_details: dict | bytes
    :param x_frankie_customer_child_id: If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children. 
    :type x_frankie_customer_child_id: str
    :type x_frankie_customer_child_id: str

    """
    entity_idv_details = EntityIDVDetailsObject.from_dict(entity_idv_details)
    return web.Response(status=200)


async def update_entity_init_idv_process(request: web.Request, x_frankie_customer_id, entity_id, entity_details, x_frankie_customer_child_id=None) -> web.Response:
    """Update Entity and Initiate IDV Process

    Update an entity object and if successful, start the process of downloading the captured data and processing the reports and results of the ID validation process.   At a minimum, the entity will need to have a name. For best results, you should gather the DoB, address, ID document details as well before calling this initProcess function, or supply the details as part of this update. 

    :param x_frankie_customer_id: Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    :type x_frankie_customer_id: str
    :type x_frankie_customer_id: str
    :param entity_id: The entityId returned previously from an earlier call to /check or /entity
    :type entity_id: str
    :type entity_id: str
    :param entity_details: The entity to update
    :type entity_details: dict | bytes
    :param x_frankie_customer_child_id: If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children. 
    :type x_frankie_customer_child_id: str
    :type x_frankie_customer_child_id: str

    """
    entity_details = EntityCheckDetailsObject.from_dict(entity_details)
    return web.Response(status=200)


async def update_entity_state(request: web.Request, x_frankie_customer_id, entity_id, x_frankie_customer_child_id=None, set=None, risk=None, comment=None) -> web.Response:
    """Update Entity States

    Internal only  Add a special internal &#39;entity result&#39; to superceed any previous real checks until the next one. 

    :param x_frankie_customer_id: Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    :type x_frankie_customer_id: str
    :type x_frankie_customer_id: str
    :param entity_id: The entityId returned previously from an earlier call to /check or /entity
    :type entity_id: str
    :type entity_id: str
    :param x_frankie_customer_child_id: If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children. 
    :type x_frankie_customer_child_id: str
    :type x_frankie_customer_child_id: str
    :param set: The status of an entity. Valid values are:   - \&quot;wait\&quot;: Waiting for new details from entity.   - \&quot;fail\&quot;: Manually fail the onboarding process.   - \&quot;archived\&quot;: Hide entity from on onboarding.   - \&quot;clear\&quot;: Remove any of the above manual states as well as any manual risk.   - \&quot;inactive\&quot;: Hide entity and prevent any further operations on it. Cannot be cleared. 
    :type set: str
    :param risk: The risk override setting for an entity. This value will be used until a verify result updates a real risk factor. Valid values are:   - \&quot;low\&quot;   - \&quot;medium\&quot;   - \&quot;high\&quot;   - \&quot;unacceptable\&quot;   - \&quot;significant\&quot; 
    :type risk: str
    :param comment: A comment describing the reason for a request. 
    :type comment: str

    """
    return web.Response(status=200)
