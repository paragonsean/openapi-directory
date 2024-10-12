from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_upsert import AccountUpsert
from openapi_server import util


async def v2_account_upserts_json_post(request: web.Request, domain, name, account_tier_id=None, city=None, company_stage_id=None, company_type=None, conversational_name=None, country=None, crm_id=None, crm_id_type=None, custom_fields=None, description=None, do_not_contact=None, founded=None, id=None, industry=None, linkedin_url=None, locale=None, owner_id=None, phone=None, postal_code=None, revenue_range=None, size=None, state=None, street=None, tags=None, twitter_handle=None, upsert_key=None, website=None) -> web.Response:
    """Upsert an account

    Upserts an account record. The upsert_key dictates how the upsert will be performed. The create and update behavior is exactly the same as the individual create and update endpoints. 

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
    :param id: ID of the account to update. Used if the upsert_key&#x3D;id. When id and another upsert_key are provided, the request will fail if the upsert record id and id parameter don&#39;t match. 
    :type id: int
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
    :param upsert_key: Name of the parameter to upsert on. The field must be provided in the input parameters, or the request will fail. The request will also fail if there are multiple records matched by the upsert field.  If upsert_key is not provided, this endpoint will not update an existing record.  Valid options are: id, crm_id, domain. If crm_id is provided, then a valid crm_id_type must be provided, as documented for the account create and update endpoints. 
    :type upsert_key: str
    :param website: Website
    :type website: str

    """
    return web.Response(status=200)
