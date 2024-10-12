from typing import List, Dict
from aiohttp import web

from openapi_server.models.person import Person
from openapi_server import util


async def v2_people_id_json_delete(request: web.Request, id) -> web.Response:
    """Delete a person

    Deletes a person. This operation is not reversible without contacting support. This operation can be called multiple times successfully. 

    :param id: Person id
    :type id: str

    """
    return web.Response(status=200)


async def v2_people_id_json_get(request: web.Request, id) -> web.Response:
    """Fetch a person

    Fetches a person, by ID only. 

    :param id: Person ID
    :type id: str

    """
    return web.Response(status=200)


async def v2_people_id_json_put(request: web.Request, id, account_id=None, city=None, contact_restrictions=None, country=None, crm_id=None, crm_id_type=None, custom_fields=None, do_not_contact=None, email_address=None, first_name=None, home_phone=None, import_id=None, job_seniority=None, last_name=None, linkedin_url=None, locale=None, mobile_phone=None, owner_id=None, person_company_industry=None, person_company_name=None, person_company_website=None, person_stage_id=None, personal_email_address=None, personal_website=None, phone=None, phone_extension=None, secondary_email_address=None, state=None, tags=None, title=None, twitter_handle=None, work_city=None, work_country=None, work_state=None) -> web.Response:
    """Update a person

    Updates a person. 

    :param id: Person id
    :type id: str
    :param account_id: ID of the Account to link this person to
    :type account_id: int
    :param city: City
    :type city: str
    :param contact_restrictions: Specific methods of communication to prevent for this person. This will prevent individual execution of these communication types as well as automatically skip cadence steps of this communication type for this person in SalesLoft. Values currently accepted: call, email, message
    :type contact_restrictions: List[str]
    :param country: Country
    :type country: str
    :param crm_id: Requires Salesforce.  ID of the person in your external CRM. You must provide a crm_id_type if this is included.  Validations will be applied to the crm_id depending on the crm_id_type. A \\\&quot;salesforce\\\&quot; ID must be exactly 18 characters. A \\\&quot;salesforce\\\&quot; ID must be either a Lead (00Q) or Contact (003) object. The type will be validated using the 18 character ID.  This field can only be used if your application or API key has the \\\&quot;person:set_crm_id\\\&quot; scope.  
    :type crm_id: str
    :param crm_id_type: The CRM that the provided crm_id is for. Must be one of: salesforce
    :type crm_id_type: str
    :param custom_fields: Custom fields are defined by the user&#39;s team. Only fields with values are presented in the API.
    :type custom_fields: dict | bytes
    :param do_not_contact: Whether or not this person has opted out of all communication. Setting this value to true prevents this person from being called, emailed, or added to a cadence in SalesLoft. If this person is currently in a cadence, they will be removed.
    :type do_not_contact: bool
    :param email_address: Email address
    :type email_address: str
    :param first_name: First name
    :type first_name: str
    :param home_phone: Home phone without formatting
    :type home_phone: str
    :param import_id: ID of the Import this person is a part of. A person can be part of multiple imports, but this ID will always be the most recent Import
    :type import_id: int
    :param job_seniority: The Job Seniority of a Person, must be one of director, executive, individual_contributor, manager, vice_president, unknown
    :type job_seniority: str
    :param last_name: Last name
    :type last_name: str
    :param linkedin_url: Linkedin URL
    :type linkedin_url: str
    :param locale: Time locale of the person
    :type locale: str
    :param mobile_phone: Mobile phone without formatting
    :type mobile_phone: str
    :param owner_id: ID of the User that owns this person
    :type owner_id: int
    :param person_company_industry: Company industry. This property is specific to this person, unrelated to the company object. Updating the company object associated with this person is recommended
    :type person_company_industry: str
    :param person_company_name: Company name. This property is specific to this person, unrelated to the company object. Updating the company object associated with this person is recommended
    :type person_company_name: str
    :param person_company_website: Company website. This property is specific to this person, unrelated to the company object. Updating the company object associated with this person is recommended
    :type person_company_website: str
    :param person_stage_id: ID of the PersonStage of this person
    :type person_stage_id: int
    :param personal_email_address: Personal email address
    :type personal_email_address: str
    :param personal_website: The website of this person
    :type personal_website: str
    :param phone: Phone without formatting
    :type phone: str
    :param phone_extension: Phone extension without formatting
    :type phone_extension: str
    :param secondary_email_address: Alternate email address
    :type secondary_email_address: str
    :param state: State
    :type state: str
    :param tags: All tags applied to this person
    :type tags: List[str]
    :param title: Job title
    :type title: str
    :param twitter_handle: The twitter handle of this person
    :type twitter_handle: str
    :param work_city: Work location - city
    :type work_city: str
    :param work_country: Work location - country
    :type work_country: str
    :param work_state: Work location - state
    :type work_state: str

    """
    custom_fields = object.from_dict(custom_fields)
    return web.Response(status=200)


async def v2_people_json_get(request: web.Request, ids=None, updated_at=None, email_addresses=None, owned_by_guid=None, person_stage_id=None, crm_id=None, owner_crm_id=None, do_not_contact=None, can_email=None, can_call=None, can_text=None, account_id=None, custom_fields=None, import_id=None, job_seniority=None, tag_id=None, owner_is_active=None, cadence_id=None, starred_by_guid=None, replied=None, bounced=None, success=None, eu_resident=None, title=None, country=None, state=None, city=None, last_contacted=None, created_at=None, new=None, phone_number=None, locales=None, owner_id=None, query=None, sort_by=None, sort_direction=None, per_page=None, page=None, include_paging_counts=None, limit_paging_counts=None) -> web.Response:
    """List people

    Fetches multiple person records. The records can be filtered, paged, and sorted according to the respective parameters. 

    :param ids: IDs of people to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful
    :type ids: List[int]
    :param updated_at: Equality filters that are applied to the updated_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]} 
    :type updated_at: List[str]
    :param email_addresses: Filters people by email address. Multiple emails can be applied. An additional value of \&quot;_is_null\&quot; can be passed to filter people that do not have an email address.
    :type email_addresses: List[str]
    :param owned_by_guid: Filters people by the owner&#39;s guid. Multiple owner guids can be applied
    :type owned_by_guid: List[str]
    :param person_stage_id: Includes people that have a given person_stage. Multiple person stage ids can be applied. An additional value of \&quot;_is_null\&quot; can be passed to filter people that do not have a stage set.
    :type person_stage_id: List[int]
    :param crm_id: Filters people by crm_id. Multiple crm ids can be applied
    :type crm_id: List[str]
    :param owner_crm_id: Filters people by owner_crm_id. Multiple owner_crm_ids can be applied. An additional value of \&quot;_is_null\&quot; can be passed to filter people that are unowned. A \&quot;_not_in\&quot; modifier can be used to exclude specific owner_crm_ids. Example: v2/people?owner_crm_id[_not_in]&#x3D;id
    :type owner_crm_id: List[str]
    :param do_not_contact: Includes people that have a given do_not_contact property
    :type do_not_contact: bool
    :param can_email: Includes people that can be emailed given do_not_contact and contact_restrictions property
    :type can_email: bool
    :param can_call: Includes people that can be called given do_not_contact and contact_restrictions property
    :type can_call: bool
    :param can_text: Includes people that can be sent a text message given do_not_contact and contact_restrictions property
    :type can_text: bool
    :param account_id: Filters people by the account they are linked to. Multiple account ids can be applied
    :type account_id: List[int]
    :param custom_fields: Filters by people matching all given custom fields. The custom field names are case-sensitive, but the provided values are case-insensitive. Example: v2/people?custom_fields[custom_field_name]&#x3D;custom_field_value
    :type custom_fields: dict | bytes
    :param import_id: Filters people that were imported by the given import ids. Multiple import ids can be applied. An additional value of \&quot;_is_null\&quot; can be passed to filter people that were not imported.
    :type import_id: List[int]
    :param job_seniority: Filters people by job seniorty. Multiple job seniorities can be applied. An additional value of \&quot;_is_null\&quot; can be passed to filter people do not have a job_seniority.
    :type job_seniority: List[str]
    :param tag_id: Filters people by the tag ids applied to the person. Multiple tag ids can be applied.
    :type tag_id: List[int]
    :param owner_is_active: Filters people by whether the owner is active or not.
    :type owner_is_active: bool
    :param cadence_id: Filters people by the cadence that they are currently on. Multiple cadence_ids can be applied. An additional value of \&quot;_is_null\&quot; can be passed to filter people that are not on a cadence.
    :type cadence_id: List[int]
    :param starred_by_guid: Filters people who have been starred by the user guids given.
    :type starred_by_guid: List[str]
    :param replied: Filters people by whether or not they have replied to an email or not.
    :type replied: bool
    :param bounced: Filters people by whether an email that was sent to them bounced or not.
    :type bounced: bool
    :param success: Filters people by whether or not they have been marked as a success or not.
    :type success: bool
    :param eu_resident: Filters people by whether or not they are marked as an European Union Resident or not.
    :type eu_resident: bool
    :param title: Filters people by their title by exact match. Supports partial matching
    :type title: List[str]
    :param country: Filters people by their country by exact match. Supports partial matching
    :type country: List[str]
    :param state: Filters people by their state by exact match. Supports partial matching
    :type state: List[str]
    :param city: Filters people by their city by exact match. Supports partial matching
    :type city: List[str]
    :param last_contacted: Equality filters that are applied to the last_contacted field. A single filter can be used by itself or combined with other filters to create a range. Additional values of \&quot;_is_null\&quot; or \&quot;_is_not_null\&quot; can be passed to filter records that either have no timestamp value or any timestamp value. ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]} 
    :type last_contacted: dict | bytes
    :param created_at: Equality filters that are applied to the last_contacted field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]} 
    :type created_at: dict | bytes
    :param new: Filters people by whether or not that person is on a cadence or if they have been contacted in any way.
    :type new: bool
    :param phone_number: Filter people by whether or not they have a phone number or not
    :type phone_number: bool
    :param locales: Filters people by locales. Multiple locales can be applied. An additional value of \&quot;Null\&quot; can be passed to filter people that do not have a locale.
    :type locales: List[str]
    :param owner_id: Filters people by owner_id. Multiple owner_ids can be applied.
    :type owner_id: List[int]
    :param query: For internal use only. This field does not comply with our backwards compatibility policies. This filter is for authenticated users of Salesloft only and will not work for OAuth Applications. Filters people by the string provided. Can search and filter by name, title, industry, email_address and linked account name.
    :type query: str
    :param sort_by: Key to sort on, must be one of: created_at, updated_at, last_contacted_at, name, title, job_seniority, call_count, sent_emails, clicked_emails, replied_emails, viewed_emails, account, cadence_stage_name. Defaults to updated_at
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
    custom_fields = .from_dict(custom_fields)
    last_contacted = .from_dict(last_contacted)
    created_at = .from_dict(created_at)
    return web.Response(status=200)


async def v2_people_json_post(request: web.Request, account_id=None, autotag_date=None, city=None, contact_restrictions=None, country=None, crm_id=None, crm_id_type=None, custom_fields=None, do_not_contact=None, email_address=None, first_name=None, home_phone=None, import_id=None, job_seniority=None, last_name=None, linkedin_url=None, locale=None, mobile_phone=None, owner_id=None, person_company_industry=None, person_company_name=None, person_company_website=None, person_stage_id=None, personal_email_address=None, personal_website=None, phone=None, phone_extension=None, secondary_email_address=None, state=None, tags=None, title=None, twitter_handle=None, work_city=None, work_country=None, work_state=None) -> web.Response:
    """Create a person

    Creates a person. Either email_address or phone/last_name must be provided as a unique lookup on the team. 

    :param account_id: ID of the Account to link this person to
    :type account_id: int
    :param autotag_date: Whether the date should be added to this person as a tag. Default is false. The tag will be Y-m-d format.
    :type autotag_date: bool
    :param city: City
    :type city: str
    :param contact_restrictions: Specific methods of communication to prevent for this person. This will prevent individual execution of these communication types as well as automatically skip cadence steps of this communication type for this person in SalesLoft. Values currently accepted: call, email, message
    :type contact_restrictions: List[str]
    :param country: Country
    :type country: str
    :param crm_id: Requires Salesforce.  ID of the person in your external CRM. You must provide a crm_id_type if this is included.  Validations will be applied to the crm_id depending on the crm_id_type. A \\\&quot;salesforce\\\&quot; ID must be exactly 18 characters. A \\\&quot;salesforce\\\&quot; ID must be either a Lead (00Q) or Contact (003) object. The type will be validated using the 18 character ID.  This field can only be used if your application or API key has the \\\&quot;person:set_crm_id\\\&quot; scope.  
    :type crm_id: str
    :param crm_id_type: The CRM that the provided crm_id is for. Must be one of: salesforce
    :type crm_id_type: str
    :param custom_fields: Custom fields are defined by the user&#39;s team. Only fields with values are presented in the API.
    :type custom_fields: dict | bytes
    :param do_not_contact: Whether or not this person has opted out of all communication. Setting this value to true prevents this person from being called, emailed, or added to a cadence in SalesLoft. If this person is currently in a cadence, they will be removed.
    :type do_not_contact: bool
    :param email_address: Email address
    :type email_address: str
    :param first_name: First name
    :type first_name: str
    :param home_phone: Home phone without formatting
    :type home_phone: str
    :param import_id: ID of the Import this person is a part of. A person can be part of multiple imports, but this ID will always be the most recent Import
    :type import_id: int
    :param job_seniority: The Job Seniority of a Person, must be one of director, executive, individual_contributor, manager, vice_president, unknown
    :type job_seniority: str
    :param last_name: Last name
    :type last_name: str
    :param linkedin_url: Linkedin URL
    :type linkedin_url: str
    :param locale: Time locale of the person
    :type locale: str
    :param mobile_phone: Mobile phone without formatting
    :type mobile_phone: str
    :param owner_id: ID of the User that owns this person
    :type owner_id: int
    :param person_company_industry: Company industry. This property is specific to this person, unrelated to the company object. Updating the company object associated with this person is recommended
    :type person_company_industry: str
    :param person_company_name: Company name. This property is specific to this person, unrelated to the company object. Updating the company object associated with this person is recommended
    :type person_company_name: str
    :param person_company_website: Company website. This property is specific to this person, unrelated to the company object. Updating the company object associated with this person is recommended
    :type person_company_website: str
    :param person_stage_id: ID of the PersonStage of this person
    :type person_stage_id: int
    :param personal_email_address: Personal email address
    :type personal_email_address: str
    :param personal_website: The website of this person
    :type personal_website: str
    :param phone: Phone without formatting
    :type phone: str
    :param phone_extension: Phone extension without formatting
    :type phone_extension: str
    :param secondary_email_address: Alternate email address
    :type secondary_email_address: str
    :param state: State
    :type state: str
    :param tags: All tags applied to this person
    :type tags: List[str]
    :param title: Job title
    :type title: str
    :param twitter_handle: The twitter handle of this person
    :type twitter_handle: str
    :param work_city: Work location - city
    :type work_city: str
    :param work_country: Work location - country
    :type work_country: str
    :param work_state: Work location - state
    :type work_state: str

    """
    custom_fields = object.from_dict(custom_fields)
    return web.Response(status=200)
