from typing import List, Dict
from aiohttp import web

from openapi_server.models.company_domain_input_model import CompanyDomainInputModel
from openapi_server.models.company_domain_list_view_model import CompanyDomainListViewModel
from openapi_server.models.company_domain_update_model import CompanyDomainUpdateModel
from openapi_server.models.company_domain_view_model import CompanyDomainViewModel
from openapi_server.models.company_input_model import CompanyInputModel
from openapi_server.models.company_update_model import CompanyUpdateModel
from openapi_server.models.company_view_model import CompanyViewModel
from openapi_server.models.content_result import ContentResult
from openapi_server.models.email_template_list_view_model import EmailTemplateListViewModel
from openapi_server.models.master_email_template_settings_view_model import MasterEmailTemplateSettingsViewModel
from openapi_server.models.master_template_settings_input_model import MasterTemplateSettingsInputModel
from openapi_server.models.region_input_model import RegionInputModel
from openapi_server.models.region_list_view_model import RegionListViewModel
from openapi_server.models.region_update_model import RegionUpdateModel
from openapi_server.models.region_view_model import RegionViewModel
from openapi_server.models.timezone_view_model import TimezoneViewModel
from openapi_server import util


async def setup_v1_companies_domains_get(request: web.Request, ) -> web.Response:
    """List Company Domains

    &lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Company Domains&lt;/b&gt; for the authorized company. To share the OnSchedJS booking widget on your website or in your application your domain must be listed.&lt;/p&gt;


    """
    return web.Response(status=200)


async def setup_v1_companies_domains_id_delete(request: web.Request, id) -> web.Response:
    """Delete Company Domain

    &lt;p&gt;Use this endpoint to &lt;b&gt;Delete&lt;/b&gt; an OnSchedJs domain from your authorized company. A valid &lt;b&gt;companyDomain id&lt;/b&gt; is required.&lt;/p&gt;

    :param id: id of companyDomain object
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_companies_domains_id_get(request: web.Request, id) -> web.Response:
    """Get Company Domain

    &lt;p&gt;Use this endpoint to return a &lt;b&gt;Company Domain&lt;/b&gt; object. A valid &lt;b&gt;companyDomain id&lt;/b&gt; is required. &lt;/p&gt;

    :param id: id of companyDomain object
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_companies_domains_id_put(request: web.Request, id, body=None) -> web.Response:
    """Update Company Domain

    &lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; an OnSchedJs domain for your authorized company. A valid &lt;b&gt;companyDomain id&lt;/b&gt; is required.&lt;/p&gt;

    :param id: id of companyDomain object
    :type id: str
    :param body: Company Domain Update Model
    :type body: dict | bytes

    """
    body = CompanyDomainUpdateModel.from_dict(body)
    return web.Response(status=200)


async def setup_v1_companies_domains_post(request: web.Request, body=None) -> web.Response:
    """Create Company Domain

    &lt;p&gt;Use this endpoint to &lt;b&gt;Create&lt;/b&gt; an OnSchedJs domain for your authorized company. To share the OnSchedJS booking widget on your website or in your application you must add the domain.&lt;/p&gt;

    :param body: Company Domain Input Model
    :type body: dict | bytes

    """
    body = CompanyDomainInputModel.from_dict(body)
    return web.Response(status=200)


async def setup_v1_companies_email_templates_get(request: web.Request, ) -> web.Response:
    """List Email Templates

    &lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Email Templates&lt;/b&gt; that are provided and may be customized. If the template has been customized, the customized property is true. The scope parameter indicates if the email template has been customized at the Business Location level or Company level. This endpoint returns &lt;b&gt;only company level templates&lt;/b&gt;, so the scope is always company.&lt;/p&gt;


    """
    return web.Response(status=200)


async def setup_v1_companies_email_templates_master_delete(request: web.Request, ) -> web.Response:
    """Delete Master Template Settings

    &lt;p&gt;Use this endpoint to &lt;b&gt;Delete Custom Master Email Template Settings&lt;/b&gt;. Deleting a custom master email template setting will reactivate the original default OnSched template settings.&lt;/p&gt;


    """
    return web.Response(status=200)


async def setup_v1_companies_email_templates_master_get(request: web.Request, ) -> web.Response:
    """Get Master Template Settings

    &lt;p&gt;Use this endpoint to return the &lt;b&gt;Master Email Template Settings&lt;/b&gt;. Settings exist for showing or hiding email panels and for changing color schemes. &lt;/p&gt;


    """
    return web.Response(status=200)


async def setup_v1_companies_email_templates_master_post(request: web.Request, body=None) -> web.Response:
    """Create Master Template Settings

    &lt;p&gt;Use this endpoint to &lt;b&gt;Create Custom Master Email Template Settings&lt;/b&gt;. Settings exist for showing or hiding email panels and for changing color schemes. Use the &lt;i&gt;GET ​/setup​/v1​/companies​/email​/templates&lt;/i&gt; endpoint to display the settings offered. Changes to the Master Template Settings will be reflected in all business locations associated with this company. &lt;/p&gt;  &lt;p&gt;The email template endpoints work a little differently than most. There are no endpoints to update the templates, we use the post endpoint to create a custom template instead. This endpoint creates a new custom Master Template Settings file that will be used instead. If you delete it you are deleting the custom template settings you created and the original default Master Template created by OnSched would be reactivated.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes

    """
    body = MasterTemplateSettingsInputModel.from_dict(body)
    return web.Response(status=200)


async def setup_v1_companies_email_templates_template_name_get(request: web.Request, template_name) -> web.Response:
    """Get Email Template

    &lt;p&gt;Use this endpoint to return the requested &lt;b&gt;Email Template&lt;/b&gt;. If it wasn&#39;t customized the default template is returned. The response content is in html format. A valid emailTemplate &lt;b&gt;name&lt;/b&gt; is required. Find template names by using the: &lt;i&gt;GET ​/setup​/v1​/companies​/email​/templates&lt;/i&gt; endpoint. Note: The master template cannot be accessed here. &lt;/p&gt;  &lt;p&gt;To create custom company email templates, go to the &lt;i&gt;POST ​/setup​/v1​/locations​/{id}​/email​/templates&lt;/i&gt; endpoint and create a template using the Primary Business Location Id.&lt;/p&gt;

    :param template_name: Email template name
    :type template_name: str

    """
    return web.Response(status=200)


async def setup_v1_companies_get(request: web.Request, ) -> web.Response:
    """Get Company

    &lt;p&gt;Use this endpoint to return the &lt;b&gt;Authorized Company&lt;/b&gt; information. The company is the main entity that oversees all business locations defined below it, hierarchically. &lt;/p&gt;  &lt;p&gt;Access to the company credentials gives you access to all business locations defined in the authorized company. Client credentials resolve to a single company and are purposely hidden from this endpoint.&lt;/p&gt;


    """
    return web.Response(status=200)


async def setup_v1_companies_post(request: web.Request, body=None) -> web.Response:
    """Create Company

    &lt;p&gt;Use this endpoint to &lt;b&gt;Create&lt;/b&gt; a new authorized company.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Note: Special API Partner credentials are required to access this endpoint.&lt;/b&gt;  &lt;/p&gt;  &lt;p&gt;The &lt;b&gt;name, registrationEmail, phone, country&lt;/b&gt; and &lt;b&gt;timezoneName&lt;/b&gt; are required fields. For &lt;b&gt;country&lt;/b&gt; use the standard ISO 3166 2-character country code.&lt;/p&gt;  &lt;p&gt;The &lt;b&gt;timezoneName&lt;/b&gt; must be expressed as an IANA Timezone e.g., &lt;i&gt;America/New_York&lt;/i&gt;.&lt;/p&gt;  &lt;p&gt;For more information: &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/List_of_tz_database_time_zones\&quot;&gt;Timezone IANA Wiki&lt;/a&gt;&lt;/p&gt;

    :param body: Company Input Model
    :type body: dict | bytes

    """
    body = CompanyInputModel.from_dict(body)
    return web.Response(status=200)


async def setup_v1_companies_put(request: web.Request, body=None) -> web.Response:
    """Update Company

    &lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; the authorized company information. Your client credentials resolve to a single company. The timezoneName must be expressed as an IANA Timezone, e.g., &lt;i&gt;America/New_York&lt;/i&gt;. &lt;/p&gt;  &lt;p&gt;For more information: &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/List_of_tz_database_time_zones\&quot;&gt;Timezone IANA Wiki&lt;/a&gt;&lt;/p&gt;

    :param body: Company Update Model
    :type body: dict | bytes

    """
    body = CompanyUpdateModel.from_dict(body)
    return web.Response(status=200)


async def setup_v1_companies_regions_get(request: web.Request, offset=None, limit=None) -> web.Response:
    """List Regions

    &lt;p&gt;Use this endpoint to return a list of &lt;b&gt;Regions&lt;/b&gt; in the authorized company. The results are returned in pages. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further. &lt;/p&gt;

    :param offset: Starting row of page, default 0
    :type offset: int
    :param limit: Page limit default 20, max 100
    :type limit: int

    """
    return web.Response(status=200)


async def setup_v1_companies_regions_id_delete(request: web.Request, id) -> web.Response:
    """Delete Region

    &lt;p&gt;Use this endpoint to &lt;b&gt;Delete&lt;/b&gt; a region object. A valid &lt;b&gt;region id&lt;/b&gt; is required. If the region is related to any business locations it won&#39;t be deleted. You must first remove any references to region id from the business locations prior to deleting.&lt;/p&gt;

    :param id: id of Region
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_companies_regions_id_get(request: web.Request, id) -> web.Response:
    """Get Region

    &lt;p&gt;Use this endpoint to return a &lt;b&gt;Region&lt;/b&gt; object. A valid &lt;b&gt;region id&lt;/b&gt; is required.&lt;/p&gt;

    :param id: id of a region object
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_companies_regions_id_put(request: web.Request, id, body=None) -> web.Response:
    """Update Region

    &lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; a region object. A valid &lt;b&gt;region id&lt;/b&gt; is required.&lt;/p&gt;

    :param id: id of Region
    :type id: str
    :param body: Region Update Model
    :type body: dict | bytes

    """
    body = RegionUpdateModel.from_dict(body)
    return web.Response(status=200)


async def setup_v1_companies_regions_post(request: web.Request, body=None) -> web.Response:
    """Create Region

    &lt;p&gt;Use this endpoint to &lt;b&gt;Create&lt;/b&gt; a region object. Regions can be mapped to business locations. They can be used by the locations endpoints to filter locations by region id.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes

    """
    body = RegionInputModel.from_dict(body)
    return web.Response(status=200)


async def setup_v1_companies_timezones_date_get(request: web.Request, _date) -> web.Response:
    """List Time Zones

    &lt;p&gt;Use this endpoint to return a &lt;b&gt;List of timezone names, timezoneIana and tzOffset values&lt;/b&gt; calculated for the date requested. Daylight Savings may or may not apply depending on the date specified.&lt;/p&gt;

    :param _date: \&quot;YYYY-MM-DD: Date for timezone info\&quot;
    :type _date: str

    """
    _date = util.deserialize_datetime(_date)
    return web.Response(status=200)
