from typing import List, Dict
from aiohttp import web

from openapi_server.models.entity_result_object import EntityResultObject
from openapi_server.models.error_object import ErrorObject
from openapi_server import util


async def blacklist_entity(request: web.Request, x_frankie_customer_id, entity_id, set, x_frankie_customer_child_id=None, reason=None, blocked_by=None, attribute=None, original_id=None) -> web.Response:
    """Set Entity Blacklist State.

    Mark the entity as blacklisted or not with the &#39;?set&#x3D;&#39; query parameter as &#39;true&#39; or &#39;false&#39;. 

    :param x_frankie_customer_id: Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    :type x_frankie_customer_id: str
    :type x_frankie_customer_id: str
    :param entity_id: The entityId returned previously from an earlier call to /check or /entity
    :type entity_id: str
    :type entity_id: str
    :param set: Set the value of an entity flag. 
    :type set: bool
    :param x_frankie_customer_child_id: If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children. 
    :type x_frankie_customer_child_id: str
    :type x_frankie_customer_child_id: str
    :param reason: Set the reason for blacklisting. Valid values are:   - \&quot;NO_REASON_SUPPLIED\&quot;   - \&quot;FABRICATED_IDENTITY\&quot;   - \&quot;IDENTITY_TAKEOVER\&quot;   - \&quot;FALSIFIED_ID_DOCUMENTS\&quot;   - \&quot;STOLEN_ID_DOCUMENTS\&quot;   - \&quot;MERCHANT_FRAUD\&quot;   - \&quot;NEVER_PAY_BUST_OUT\&quot;   - \&quot;CONFLICTING_DATA_PROVIDED\&quot;   - \&quot;MONEY_MULE\&quot;   - \&quot;FALSE_FRAUD_CLAIM\&quot;   - \&quot;FRAUDULENT_3RD_PARTY\&quot;   - \&quot;COMPANY_TAKEOVER\&quot;   - \&quot;FICTITIOUS_EMPLOYER\&quot;   - \&quot;COLLUSIVE_EMPLOYER\&quot;   - \&quot;OVER_VALUATION_OF_ASSETS\&quot;   - \&quot;FALSIFIED_EMPLOYMENT_DETAILS\&quot;   - \&quot;MANIPULATED_IDENTITY\&quot;   - \&quot;SYNDICATED_FRAUD\&quot;   - \&quot;INTERNAL_FRAUD\&quot;   - \&quot;BANK_FRAUD\&quot;   - \&quot;UNDISCLOSED_DATA\&quot;   - \&quot;FALSE_HARDSHIP\&quot;   - \&quot;SMR_REPORT_LODGED\&quot;   - \&quot;2X_SMR_REPORTS_LODGED\&quot; 
    :type reason: str
    :param blocked_by: Specify who is setting the entity as blacklisted. 
    :type blocked_by: str
    :param attribute: Specify the blacklisted attribute. Valid values are:   - \&quot;ENTIRE_PROFILE\&quot;   - \&quot;FULL_NAME\&quot;   - \&quot;EMAIL_ADDRESS\&quot;   - \&quot;PHONE_NUMBER\&quot;   - \&quot;ID_DOCUMENT\&quot;   - \&quot;MAILING_ADDRESS\&quot;   - \&quot;RESIDENTIAL_ADDRESS\&quot;    
    :type attribute: str
    :param original_id: Specify the Id of the matching blacklisted entity or single data-point. 
    :type original_id: str

    """
    return web.Response(status=200)


async def entity_monitoring(request: web.Request, x_frankie_customer_id, entity_id, set, x_frankie_customer_child_id=None) -> web.Response:
    """Set Entity Ongoing AML Monitoring Status.

    Mark the entity as being monitored or not with the &#39;?set&#x3D;&#39; query parameter as &#39;true&#39; or &#39;false&#39;. 

    :param x_frankie_customer_id: Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    :type x_frankie_customer_id: str
    :type x_frankie_customer_id: str
    :param entity_id: The entityId returned previously from an earlier call to /check or /entity
    :type entity_id: str
    :type entity_id: str
    :param set: Set the value of an entity flag. 
    :type set: bool
    :param x_frankie_customer_child_id: If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children. 
    :type x_frankie_customer_child_id: str
    :type x_frankie_customer_child_id: str

    """
    return web.Response(status=200)


async def flag_duplicate_entity(request: web.Request, x_frankie_customer_id, entity_id, other_id, set, x_frankie_customer_child_id=None) -> web.Response:
    """Resolve Duplicate States.

    Resolve the state of a pair of duplicate entities with the &#39;?set&#x3D;&#39; query parameter as &#39;true&#39; or &#39;false&#39;. Setting duplicate to &#39;true&#39; will make entityId invisible for most purposes and otherId will continue to function as normal. Setting duplicate to &#39;false&#39; means the two entities are in fact separate but similar and they will both continue to exist independently but will no longer be identified as duplicates of eachother. 

    :param x_frankie_customer_id: Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    :type x_frankie_customer_id: str
    :type x_frankie_customer_id: str
    :param entity_id: The entityId returned previously from an earlier call to /check or /entity
    :type entity_id: str
    :type entity_id: str
    :param other_id: An entityId returned previously from an earlier call to /check or /entity. Used when an operation requires two entityIds
    :type other_id: str
    :type other_id: str
    :param set: Set the value of an entity flag. 
    :type set: bool
    :param x_frankie_customer_child_id: If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children. 
    :type x_frankie_customer_child_id: str
    :type x_frankie_customer_child_id: str

    """
    return web.Response(status=200)


async def watchlist_entity(request: web.Request, x_frankie_customer_id, entity_id, set, x_frankie_customer_child_id=None, reason=None, comment=None) -> web.Response:
    """Set Entity Watchlist State.

    Mark the entity as watchlisted or not with the &#39;?set&#x3D;&#39; query parameter as &#39;true&#39; or &#39;false&#39;. 

    :param x_frankie_customer_id: Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    :type x_frankie_customer_id: str
    :type x_frankie_customer_id: str
    :param entity_id: The entityId returned previously from an earlier call to /check or /entity
    :type entity_id: str
    :type entity_id: str
    :param set: Set the value of an entity flag. 
    :type set: bool
    :param x_frankie_customer_child_id: If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children. 
    :type x_frankie_customer_child_id: str
    :type x_frankie_customer_child_id: str
    :param reason: Set the reason for watchlisting. Valid values are:  - \&quot;WAS_BLACKLISTED\&quot; 
    :type reason: str
    :param comment: A comment describing the reason for a request. 
    :type comment: str

    """
    return web.Response(status=200)
