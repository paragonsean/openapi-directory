from typing import List, Dict
from aiohttp import web

from openapi_server.models.accepted_entity_result_object import AcceptedEntityResultObject
from openapi_server.models.business_report_response_details import BusinessReportResponseDetails
from openapi_server.models.entity_object import EntityObject
from openapi_server.models.error_object import ErrorObject
from openapi_server.models.international_business_profile_criteria import InternationalBusinessProfileCriteria
from openapi_server.models.international_business_profile_response import InternationalBusinessProfileResponse
from openapi_server.models.international_business_search_criteria import InternationalBusinessSearchCriteria
from openapi_server.models.international_business_search_response import InternationalBusinessSearchResponse
from openapi_server.models.organisation_check_response_object import OrganisationCheckResponseObject
from openapi_server.models.ownership_query import OwnershipQuery
from openapi_server import util


async def business_ownership_query(request: web.Request, x_frankie_customer_id, query, x_frankie_customer_child_id=None, check_type=None, entity_categories=None, result_level=None, validation=None, generate_report=None, include_historical=None, only_profile=None) -> web.Response:
    """Create Business Entity and Query UBO (AUS Only)

    Process a request for ownership details for an Australian organisation.  See below for more generic international queries.  At a minimum, you just need to supply an ACN or ABN and we can retrieve the rest. You also have the option of supplying company name, type (as per ABR types) and both ABN/ACN and we&#39;ll attempt to verfy that that data matches what is on record before attempting any further verification and validation.  KYC/AML for a selection of entities associated with an organisation and/or the organisation itself can optionally be run, but not by default. To enable KYC/AML checks one or more entity categories must be provided. If such a list of entity categories is given then default checks based on configuration will be run for those categories. If a check type is also provided in the request then that type will be used for entities representing individual entities, and the AML subset of that check will be used for organisations if any. Specifying a check type without an entity category will result in an error.  NOTE: This query will always run asynchronously and you will only ever be returned a 202 ACCEPT response, or an error. Results will be pushed using the Push Notification API below and you will be able to retrieve the results using the Retrieve API.  We have supplied the 200 response in the definition below only so what will be sent to you when you later retrieve the details.  More details on how to use this API and interpret the results can be found here:      https://apidocs.frankiefinancial.com/docs/which-function-to-use 

    :param x_frankie_customer_id: Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    :type x_frankie_customer_id: str
    :type x_frankie_customer_id: str
    :param query: The organisation to be queried. An entity object that must have an organisation object with at least one organisation number. 
    :type query: dict | bytes
    :param x_frankie_customer_child_id: If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children. 
    :type x_frankie_customer_child_id: str
    :type x_frankie_customer_child_id: str
    :param check_type: When creating a new check, we need to define the checks we wish to run. If this parameter is not supplied then the check will be based on a configured check type for each entity category.    The checkType is make up of a comma separated list of the types of check we wish to run.  The order is important, and must be of the form:   - Entity Check (if you&#39;re running this). Choose one from the available options   - ID Check (If you want this)   - PEP Checks (again if you want this, choose one of the options)  Entity Checks - One of:   - \&quot;one_plus\&quot;: Checks name, address and DoB against a minimum of 1 data source. (also known as a 1+1)   - \&quot;two_plus\&quot;: Checks name, address and DoB against a minimum of 2 independent data sources (also known as a 2+2)  ID Checks - One of:   - \&quot;id\&quot;: Checks all of the identity documents, but not necessarily the entity itself independently. Use this in conjunction with a one_plus or two_plus for more.    Fraud Checks - One or more  of:   - \&quot;fraudlist\&quot;: Checks to see if the identity appears on any known fraud lists. Should be run after KYC/ID checks have passed.   - \&quot;fraudid\&quot;: Checks external ID services to see if details appear in fraud detection services (e.g. EmailAge or FraudNet)    PEP Checks - One of:   - \&quot;pep\&quot;: Will only run PEP/Sanctions checks (no identity verification)   - \&quot;pep_media\&quot;: Will run PEP/Sanctions checks, as well as watchlist and adverse media checks. (no identity verification)      * NOTE: These checks will ONLY run if either the KYC/ID checks have been run prior, or it is the only check requested.    Pre-defined combinations:   - \&quot;full\&quot;: equivalent to \&quot;two_plus,id,pep_media\&quot; or \&quot;pep_media\&quot; if the target is an organisation.   - \&quot;default\&quot;: Currently defined as \&quot;two_plus,id\&quot; or \&quot;pep\&quot; if the target is an organisation.  Custom:   - By arrangement with Frankie you can define your own KYC check type.      This will allow you to set the minimum number of matches for:     - name      - date of birth     - address     - government id      This allows for alternatives to the \&quot;standard\&quot; two_plus or one_plus (note, these can be overridden too).    Profile:   - \&quot;profile\&quot;: By arrangement with Frankie you can have a \&quot;profile\&quot; check type that applies checks according to a profile that you assign to the entity from a predefined set of profiles.      The profile to use will be taken from the entity.entityProfile field if set, or be run through a set of configurable rules to determine which one to use.      Profiles act a little like the Pre-defined combinations above in that they can map to a defined list. But they offer a lot more besides, including rules for determining default settings, inbuild data aging and other configurable features.   They also allow for a new result set top be returned that provides a more detailed and useful breakdown of the check/verification process.      Entity Profiles are the future of checks with Frankie Financial. 
    :type check_type: List[str]
    :param entity_categories: A comma separated list that specifies the categories of entities associated with the target organisation that will be checked.    - organisation - Just the organisation itself.   - ubos - All ultimate beneficial owners.   - pseudo_ubos - Use an alterntive category when an organisation has no actual UBOs. The actual category to use is defined via configuration, default is no alterntive category.   - direct_owners - All direct owners of the company, both organisations and individuals, may include UBOs for for simple ownership.   - officers - All officers of the company   - officers_directors - All directors of the company   - officers_other - All non-director officers of the company   - all - All direct and indirect owners, both organisations and individuals (including UBOs), and officers of all organisations. 
    :type entity_categories: List[str]
    :param result_level: The result level allows you to specify the level of detail returned for the entity check. You can choose summary or full. 
    :type result_level: str
    :param validation: Should a validation check be run before the ownership query. The default is specified via configuration. The validation checks to see if the provided organisation is suitable for an ownership query by looking for the ACN in public data sources.  Options are: - \&quot;on\&quot;: Validate only when ACN is not provided. This is the typical default. - \&quot;acn\&quot;: Validate even if ACN is provided. - \&quot;only\&quot;: Like \&quot;acn\&quot; but only do validation query, don&#39;t proceed with ownership query. This option cannot be set as the default via configuration. - \&quot;off\&quot;: Never validate. The Ownership query will then fail if an ACN is not provided. 
    :type validation: str
    :param generate_report: The type of human readable report, if any, to generate based on the ownership query results. 
    :type generate_report: str
    :param include_historical: If set to true, historical ownership data will be requested. 
    :type include_historical: bool
    :param only_profile: If set to true, a full UBO report will not be requested. 
    :type only_profile: bool

    """
    query = OwnershipQuery.from_dict(query)
    return web.Response(status=200)


async def check_organisation(request: web.Request, x_frankie_customer_id, entity_id, x_frankie_customer_child_id=None, check_type=None, entity_categories=None, result_level=None, generate_report=None) -> web.Response:
    """Run KYC/AML Checks on Organisation and/or Associated Individuals.

    Run KYC/AML for a selection of entities associated with an organisation and/or the organisation itself based on a previous ownership query. By default AML will be checked for just the organisation itself. If a list of entity categories is given then default checks based on configuration will be run for those categories. If a check type is also provided in the request then that type will be used for entities representing individual entities, and the AML subset of that check will be used for organisations if any. If no ownership query has been run, then this operation will return an error. 

    :param x_frankie_customer_id: Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    :type x_frankie_customer_id: str
    :type x_frankie_customer_id: str
    :param entity_id: The entityId returned previously from an earlier call to /check or /entity
    :type entity_id: str
    :type entity_id: str
    :param x_frankie_customer_child_id: If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children. 
    :type x_frankie_customer_child_id: str
    :type x_frankie_customer_child_id: str
    :param check_type: When creating a new check, we need to define the checks we wish to run. If this parameter is not supplied then the check will be based on a configured check type for each entity category.    The checkType is make up of a comma separated list of the types of check we wish to run.  The order is important, and must be of the form:   - Entity Check (if you&#39;re running this). Choose one from the available options   - ID Check (If you want this)   - PEP Checks (again if you want this, choose one of the options)  Entity Checks - One of:   - \&quot;one_plus\&quot;: Checks name, address and DoB against a minimum of 1 data source. (also known as a 1+1)   - \&quot;two_plus\&quot;: Checks name, address and DoB against a minimum of 2 independent data sources (also known as a 2+2)  ID Checks - One of:   - \&quot;id\&quot;: Checks all of the identity documents, but not necessarily the entity itself independently. Use this in conjunction with a one_plus or two_plus for more.    Fraud Checks - One or more  of:   - \&quot;fraudlist\&quot;: Checks to see if the identity appears on any known fraud lists. Should be run after KYC/ID checks have passed.   - \&quot;fraudid\&quot;: Checks external ID services to see if details appear in fraud detection services (e.g. EmailAge or FraudNet)    PEP Checks - One of:   - \&quot;pep\&quot;: Will only run PEP/Sanctions checks (no identity verification)   - \&quot;pep_media\&quot;: Will run PEP/Sanctions checks, as well as watchlist and adverse media checks. (no identity verification)      * NOTE: These checks will ONLY run if either the KYC/ID checks have been run prior, or it is the only check requested.    Pre-defined combinations:   - \&quot;full\&quot;: equivalent to \&quot;two_plus,id,pep_media\&quot; or \&quot;pep_media\&quot; if the target is an organisation.   - \&quot;default\&quot;: Currently defined as \&quot;two_plus,id\&quot; or \&quot;pep\&quot; if the target is an organisation.  Custom:   - By arrangement with Frankie you can define your own KYC check type.      This will allow you to set the minimum number of matches for:     - name      - date of birth     - address     - government id      This allows for alternatives to the \&quot;standard\&quot; two_plus or one_plus (note, these can be overridden too).    Profile:   - \&quot;profile\&quot;: By arrangement with Frankie you can have a \&quot;profile\&quot; check type that applies checks according to a profile that you assign to the entity from a predefined set of profiles.      The profile to use will be taken from the entity.entityProfile field if set, or be run through a set of configurable rules to determine which one to use.      Profiles act a little like the Pre-defined combinations above in that they can map to a defined list. But they offer a lot more besides, including rules for determining default settings, inbuild data aging and other configurable features.   They also allow for a new result set top be returned that provides a more detailed and useful breakdown of the check/verification process.      Entity Profiles are the future of checks with Frankie Financial. 
    :type check_type: List[str]
    :param entity_categories: A comma separated list that specifies the categories of entities associated with the target organisation that will be checked.    - organisation - Just the organisation itself.   - ubos - All ultimate beneficial owners.   - pseudo_ubos - Use an alterntive category when an organisation has no actual UBOs. The actual category to use is defined via configuration, default is no alterntive category.   - direct_owners - All direct owners of the company, both organisations and individuals, may include UBOs for for simple ownership.   - officers - All officers of the company   - officers_directors - All directors of the company   - officers_other - All non-director officers of the company   - all - All direct and indirect owners, both organisations and individuals (including UBOs), and officers of all organisations. 
    :type entity_categories: List[str]
    :param result_level: The result level allows you to specify the level of detail returned for the entity check. You can choose summary or full. 
    :type result_level: str
    :param generate_report: The type of human readable report, if any, to generate based on the ownership query results. 
    :type generate_report: str

    """
    return web.Response(status=200)


async def international_business_profile(request: web.Request, x_frankie_customer_id, organisation, x_frankie_customer_child_id=None) -> web.Response:
    """Retrieve a business profile from any country (AUS included).

    Using the Company Code retrieved from the search response (see above) you can pull back the details of the company.  The Frankie platform will save the details of the response as an ORGANISATION type entity with the profile attached as a report which you can potentially re-retrieve later if you wish. 

    :param x_frankie_customer_id: Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    :type x_frankie_customer_id: str
    :type x_frankie_customer_id: str
    :param organisation: The country, cxompany code and optional registry of the organisation to be queried. 
    :type organisation: dict | bytes
    :param x_frankie_customer_child_id: If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children. 
    :type x_frankie_customer_child_id: str
    :type x_frankie_customer_child_id: str

    """
    organisation = InternationalBusinessProfileCriteria.from_dict(organisation)
    return web.Response(status=200)


async def international_business_search(request: web.Request, x_frankie_customer_id, organisation, x_frankie_customer_child_id=None) -> web.Response:
    """Search for a business from any country (AUS included).

    Search for a given business name or business number across international business registers.  The search will return a list of matching companies that you can then potentially query using the international profile query (see below). Each search result will have a CompanyCode that you use to retrieve the specific company details using the profile function.  This process will not save any details from the search results. 

    :param x_frankie_customer_id: Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    :type x_frankie_customer_id: str
    :type x_frankie_customer_id: str
    :param organisation: The country, name or business number of the organisation to be queried. 
    :type organisation: dict | bytes
    :param x_frankie_customer_child_id: If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children. 
    :type x_frankie_customer_child_id: str
    :type x_frankie_customer_child_id: str

    """
    organisation = InternationalBusinessSearchCriteria.from_dict(organisation)
    return web.Response(status=200)


async def run_business_reports(request: web.Request, x_frankie_customer_id, report_types, organisation, x_frankie_customer_child_id=None) -> web.Response:
    """Run Report(s) against a new or existing organisation entity (AUS Only).

    NOTE: Australian companies ONLY. Create or find and update an ORGANISATION type entity, then run the requested reports. Reports include:  - Credit Report  - Credit Score  At a minimum, you just need to supply an ACN and/or ABN and an entity type set to ORGANISATION. Alternatively the entity ID of an existing ORGANISATION entity gan be given in the request body  Note: these reports are different to the Ultimate Beneficial Owner and Business Detail requests - these reports are independent data and analysis over and above company information and verification details.  You can request multiple reports to be run at once and they will be returned as a group (where feasible).  If a report can only be generated over time, then a temporary response will be returned and a webhook notification will be pushed later once the report has been completed. 

    :param x_frankie_customer_id: Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    :type x_frankie_customer_id: str
    :type x_frankie_customer_id: str
    :param report_types: Define the report(s) you wish to run.  You can request more than one as a comma separated list.  Duplicates will be ignored.  Note: These reports are different to the business details and UBO queries and are meant to provide deeper detail and background on a business or organisation.    Current valid report types are:   - creditScore   - creditReport 
    :type report_types: str
    :param organisation: The organisation to be queried. An entity object that must have be an ORGANISATION type with at least one organisation number (ABN or ACN). 
    :type organisation: dict | bytes
    :param x_frankie_customer_child_id: If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children. 
    :type x_frankie_customer_child_id: str
    :type x_frankie_customer_child_id: str

    """
    organisation = EntityObject.from_dict(organisation)
    return web.Response(status=200)
