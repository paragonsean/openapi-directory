from typing import List, Dict
from aiohttp import web

from openapi_server.models.person_upsert import PersonUpsert
from openapi_server import util


async def v2_person_upserts_json_post(request: web.Request, account_id=None, city=None, contact_restrictions=None, country=None, crm_id=None, crm_id_type=None, custom_fields=None, do_not_contact=None, email_address=None, first_name=None, home_phone=None, id=None, import_id=None, job_seniority=None, last_name=None, linkedin_url=None, locale=None, mobile_phone=None, owner_id=None, person_company_industry=None, person_company_name=None, person_company_website=None, person_stage_id=None, personal_email_address=None, personal_website=None, phone=None, phone_extension=None, secondary_email_address=None, state=None, tags=None, title=None, twitter_handle=None, upsert_key=None, work_city=None, work_country=None, work_state=None) -> web.Response:
    """Upsert a person

    Upserts a person record. The upsert_key dictates how the upsert will be performed. The create and update behavior is exactly the same as the individual create and update endpoints. 

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
    :param id: ID of the person to update. Used if the upsert_key&#x3D;id. When id and another upsert_key are provided, the request will fail if the upsert record id and id parameter don&#39;t match. 
    :type id: int
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
    :param upsert_key: Name of the parameter to upsert on. The field must be provided in the input parameters, or the request will fail. The request will also fail if there are multiple records matched by the upsert field. This can occur if intentional duplicates by email address is enabled.  If upsert_key is not provided, this endpoint will not update an existing record.  Valid options are: id, crm_id, email_address. If crm_id is provided, then a valid crm_id_type must be provided, as documented for the person create and update endpoints. 
    :type upsert_key: str
    :param work_city: Work location - city
    :type work_city: str
    :param work_country: Work location - country
    :type work_country: str
    :param work_state: Work location - state
    :type work_state: str

    """
    custom_fields = object.from_dict(custom_fields)
    return web.Response(status=200)
