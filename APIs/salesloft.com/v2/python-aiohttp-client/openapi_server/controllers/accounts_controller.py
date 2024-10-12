from typing import List, Dict
from aiohttp import web

from openapi_server.models.account import Account
from openapi_server import util


async def v2_accounts_id_json_delete(request: web.Request, id) -> web.Response:
    """Delete an account

    Deletes an account. This operation is not reversible without contacting support. This operation can be called multiple times successfully.  Deleting an account will remove all connected people from that account. 

    :param id: Account ID
    :type id: str

    """
    return web.Response(status=200)


async def v2_accounts_id_json_get(request: web.Request, id) -> web.Response:
    """Fetch an account

    Fetches an account, by ID only. 

    :param id: Account ID
    :type id: str

    """
    return web.Response(status=200)


async def v2_accounts_id_json_put(request: web.Request, id, domain, name, account_tier_id=None, archived=None, city=None, company_stage_id=None, company_type=None, conversational_name=None, country=None, crm_id=None, crm_id_type=None, custom_fields=None, description=None, do_not_contact=None, founded=None, industry=None, linkedin_url=None, locale=None, owner_id=None, phone=None, postal_code=None, revenue_range=None, size=None, state=None, street=None, tags=None, twitter_handle=None, website=None) -> web.Response:
    """Update an existing Account

    Updates an account.  \&quot;domain\&quot; must be unique on the current team. 

    :param id: Account ID
    :type id: str
    :param domain: Website domain, not a fully qualified URI
    :type domain: str
    :param name: Account Full Name
    :type name: str
    :param account_tier_id: ID of the Account Tier for this Account
    :type account_tier_id: int
    :param archived: Whether this Account should be archived or not. Setting this to true sets archived_at to the current time if it&#39;s not already set. Setting this to false will set archived_at to null
    :type archived: bool
    :param city: City
    :type city: str
    :param company_stage_id: ID of the CompanyStage assigned to this Account
    :type company_stage_id: int
    :param company_type: Type of the Account&#39;s company
    :type company_type: str
    :param conversational_name: Conversational name of the Account
    :type conversational_name: str
    :param country: Country
    :type country: str
    :param crm_id: Requires Salesforce.  ID of the person in your external CRM. You must provide a crm_id_type if this is included.  Validations will be applied to the crm_id depending on the crm_id_type. A \\\&quot;salesforce\\\&quot; ID must be exactly 18 characters. A \\\&quot;salesforce\\\&quot; ID must be either an Account (001) object. The type will be validated using the 18 character ID.  This field can only be used if your application or API key has the \\\&quot;account:set_crm_id\\\&quot; scope.  
    :type crm_id: str
    :param crm_id_type: The CRM that the provided crm_id is for. Must be one of: salesforce
    :type crm_id_type: str
    :param custom_fields: Custom fields are defined by the user&#39;s team. Only fields with values are presented in the API.
    :type custom_fields: List[]
    :param description: Description
    :type description: str
    :param do_not_contact: Whether this company can not be contacted. Values are either true or false. Setting this to true will remove all associated people from all active communications
    :type do_not_contact: bool
    :param founded: Date or year of founding
    :type founded: str
    :param industry: Industry
    :type industry: str
    :param linkedin_url: Full LinkedIn url
    :type linkedin_url: str
    :param locale: Time locale
    :type locale: str
    :param owner_id: ID of the User that owns this Account
    :type owner_id: int
    :param phone: Phone number without formatting
    :type phone: str
    :param postal_code: Postal code
    :type postal_code: str
    :param revenue_range: Estimated revenue range
    :type revenue_range: str
    :param size: Estimated number of people in employment
    :type size: str
    :param state: State
    :type state: str
    :param street: Street name and number
    :type street: str
    :param tags: All tags applied to this Account
    :type tags: List[str]
    :param twitter_handle: Twitter handle, with @
    :type twitter_handle: str
    :param website: Website
    :type website: str

    """
    return web.Response(status=200)


async def v2_accounts_json_get(request: web.Request, ids=None, crm_id=None, tag=None, tag_id=None, created_at=None, updated_at=None, domain=None, website=None, archived=None, name=None, account_stage_id=None, account_tier_id=None, owner_id=None, owner_is_active=None, last_contacted=None, custom_fields=None, industry=None, country=None, state=None, city=None, owner_crm_id=None, locales=None, user_relationships=None, sort_by=None, sort_direction=None, per_page=None, page=None, include_paging_counts=None, limit_paging_counts=None) -> web.Response:
    """List accounts

    Fetches multiple account records. The records can be filtered, paged, and sorted according to the respective parameters. 

    :param ids: IDs of accounts to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful
    :type ids: List[int]
    :param crm_id: Filters accounts by crm_id. Multiple crm ids can be applied
    :type crm_id: List[str]
    :param tag: Filters accounts by the tags applied to the account. Multiple tags can be applied
    :type tag: List[str]
    :param tag_id: Filters accounts by the tag id&#39;s applied to the account. Multiple tag id&#39;s can be applied
    :type tag_id: List[int]
    :param created_at: Equality filters that are applied to the created_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]} 
    :type created_at: List[str]
    :param updated_at: Equality filters that are applied to the updated_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]} 
    :type updated_at: List[str]
    :param domain: Domain of the accounts to fetch. Domains are unique and lowercase
    :type domain: str
    :param website: Filters accounts by website. Multiple websites can be applied. An additional value of \&quot;_is_null\&quot; can be passed to filter accounts that do not have a website.
    :type website: List[str]
    :param archived: Filters accounts by archived_at status. Returns only accounts where archived_at is not null if this field is true. Returns only accounts where archived_at is null if this field is false. Do not pass this parameter to return both archived and unarchived accounts. This filter is not applied if any value other than \&quot;true\&quot; or \&quot;false\&quot; is passed.
    :type archived: bool
    :param name: Names of accounts to fetch. Name matches are exact and case sensitive. Multiple names can be fetched.
    :type name: List[str]
    :param account_stage_id: Filters accounts by account_stage_id. Multiple account_stage_ids can be applied. An additional value of \&quot;_is_null\&quot; can be passed to filter accounts that do not have account_stage_id
    :type account_stage_id: List[int]
    :param account_tier_id: Filters accounts by account_tier_id. Multiple account tier ids can be applied
    :type account_tier_id: List[int]
    :param owner_id: Filters accounts by owner_id. Multiple owner_ids can be applied. An additional value of \&quot;_is_null\&quot; can be passed to filter accounts that are unowned
    :type owner_id: List[str]
    :param owner_is_active: Filters accounts by whether the owner is active or not.
    :type owner_is_active: bool
    :param last_contacted: Equality filters that are applied to the last_contacted field. A single filter can be used by itself or combined with other filters to create a range. Additional values of \&quot;_is_null\&quot; or \&quot;_is_not_null\&quot; can be passed to filter records that either have no timestamp value or any timestamp value. ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]} 
    :type last_contacted: dict | bytes
    :param custom_fields: Filters by accounts matching all given custom fields. The custom field names are case-sensitive, but the provided values are case-insensitive. Example: v2/accounts?custom_fields[custom_field_name]&#x3D;custom_field_value
    :type custom_fields: dict | bytes
    :param industry: Filters accounts by industry by exact match. Supports partial matching
    :type industry: List[str]
    :param country: Filters accounts by country by exact match. Supports partial matching
    :type country: List[str]
    :param state: Filters accounts by state by exact match. Supports partial matching
    :type state: List[str]
    :param city: Filters accounts by city by exact match. Supports partial matching
    :type city: List[str]
    :param owner_crm_id: Filters accounts by owner_crm_id. Multiple owner_crm_ids can be applied. An additional value of \&quot;_is_null\&quot; can be passed to filter accounts that are unowned. A \&quot;_not_in\&quot; modifier can be used to exclude specific owner_crm_ids. Example: v2/accounts?owner_crm_id[_not_in]&#x3D;id
    :type owner_crm_id: List[str]
    :param locales: Filters accounts by locale. Multiple locales are allowed
    :type locales: List[str]
    :param user_relationships: Filters by accounts matching all given user relationship fields, _is_null or _unmapped can be passed to filter accounts with null or unmapped user relationship values. Example: v2/accounts?user_relationships[name]&#x3D;value
    :type user_relationships: dict | bytes
    :param sort_by: Key to sort on, must be one of: created_at, updated_at, last_contacted_at, account_stage, account_stage_name, account_tier, account_tier_name, name, counts_people. Defaults to updated_at
    :type sort_by: str
    :param sort_direction: Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
    :type sort_direction: str
    :param per_page: How many records to show per page in the range [1, 100]. Defaults to 25
    :type per_page: int
    :param page: The current page to fetch results from. Defaults to 1
    :type page: int
    :param include_paging_counts: Whether to include total_pages and total_count in the metadata. Defaults to false
    :type include_paging_counts: bool
    :param limit_paging_counts: Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
    :type limit_paging_counts: bool

    """
    last_contacted = .from_dict(last_contacted)
    custom_fields = .from_dict(custom_fields)
    user_relationships = .from_dict(user_relationships)
    return web.Response(status=200)


async def v2_accounts_json_post(request: web.Request, domain, name, account_tier_id=None, city=None, company_stage_id=None, company_type=None, conversational_name=None, country=None, crm_id=None, crm_id_type=None, custom_fields=None, description=None, do_not_contact=None, founded=None, industry=None, linkedin_url=None, locale=None, owner_id=None, phone=None, postal_code=None, revenue_range=None, size=None, state=None, street=None, tags=None, twitter_handle=None, website=None) -> web.Response:
    """Create an account

    Creates an account.  \&quot;domain\&quot; must be unique on the current team. 

    :param domain: Website domain, not a fully qualified URI
    :type domain: str
    :param name: Account Full Name
    :type name: str
    :param account_tier_id: ID of the Account Tier for this Account
    :type account_tier_id: int
    :param city: City
    :type city: str
    :param company_stage_id: ID of the CompanyStage assigned to this Account
    :type company_stage_id: int
    :param company_type: Type of the Account&#39;s company
    :type company_type: str
    :param conversational_name: Conversational name of the Account
    :type conversational_name: str
    :param country: Country
    :type country: str
    :param crm_id: Requires Salesforce.  ID of the person in your external CRM. You must provide a crm_id_type if this is included.  Validations will be applied to the crm_id depending on the crm_id_type. A \\\&quot;salesforce\\\&quot; ID must be exactly 18 characters. A \\\&quot;salesforce\\\&quot; ID must be either an Account (001) object. The type will be validated using the 18 character ID.  This field can only be used if your application or API key has the \\\&quot;account:set_crm_id\\\&quot; scope.  
    :type crm_id: str
    :param crm_id_type: The CRM that the provided crm_id is for. Must be one of: salesforce
    :type crm_id_type: str
    :param custom_fields: Custom fields are defined by the user&#39;s team. Only fields with values are presented in the API.
    :type custom_fields: List[]
    :param description: Description
    :type description: str
    :param do_not_contact: Whether this company can not be contacted. Values are either true or false. Setting this to true will remove all associated people from all active communications
    :type do_not_contact: bool
    :param founded: Date or year of founding
    :type founded: str
    :param industry: Industry
    :type industry: str
    :param linkedin_url: Full LinkedIn url
    :type linkedin_url: str
    :param locale: Time locale
    :type locale: str
    :param owner_id: ID of the User that owns this Account
    :type owner_id: int
    :param phone: Phone number without formatting
    :type phone: str
    :param postal_code: Postal code
    :type postal_code: str
    :param revenue_range: Estimated revenue range
    :type revenue_range: str
    :param size: Estimated number of people in employment
    :type size: str
    :param state: State
    :type state: str
    :param street: Street name and number
    :type street: str
    :param tags: All tags applied to this Account
    :type tags: List[str]
    :param twitter_handle: Twitter handle, with @
    :type twitter_handle: str
    :param website: Website
    :type website: str

    """
    return web.Response(status=200)
