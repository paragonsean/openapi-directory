from typing import List, Dict
from aiohttp import web

from openapi_server.models.appointment_reminder_view_model import AppointmentReminderViewModel
from openapi_server.models.appointment_reminders_input_model import AppointmentRemindersInputModel
from openapi_server.models.business_service_list_view_model import BusinessServiceListViewModel
from openapi_server.models.business_service_view_model import BusinessServiceViewModel
from openapi_server.models.content_result import ContentResult
from openapi_server.models.email_template_input_model import EmailTemplateInputModel
from openapi_server.models.email_template_list_view_model import EmailTemplateListViewModel
from openapi_server.models.google_service_account_creds import GoogleServiceAccountCreds
from openapi_server.models.location_input_model import LocationInputModel
from openapi_server.models.location_list_view_model import LocationListViewModel
from openapi_server.models.location_update_model import LocationUpdateModel
from openapi_server.models.location_view_model import LocationViewModel
from openapi_server.models.locations_input_model import LocationsInputModel
from openapi_server.models.master_email_template_settings_view_model import MasterEmailTemplateSettingsViewModel
from openapi_server.models.master_template_settings_input_model import MasterTemplateSettingsInputModel
from openapi_server.models.resource_image_input_model import ResourceImageInputModel
from openapi_server import util


async def setup_v1_locations_bulk_post(request: web.Request, body=None) -> web.Response:
    """Create Locations Bulk

    &lt;p&gt;Use this endpoint to &lt;b&gt;Create Bulk&lt;/b&gt; business locations. The posted list of locations cannot exceed 100 location objects per transaction for performance purposes. The result is a list of new business location objects with a GUID assigned to each location.&lt;/p&gt;  &lt;p&gt;The &lt;b&gt;name&lt;/b&gt; and &lt;b&gt;timezoneName&lt;/b&gt; fields are required. The &lt;b&gt;timezoneName&lt;/b&gt; must be expressed as an IANA Timezone e.g., &lt;i&gt;America/New_York&lt;/i&gt;. Refer to: &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/List_of_tz_database_time_zones\&quot;&gt;Timezone Wiki&lt;/a&gt; for a listing of IANA time zones.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Business hours&lt;/b&gt; are set by defining the &lt;b&gt;startTime&lt;/b&gt; and &lt;b&gt;endTime&lt;/b&gt; values for each day available/open. All days of the week must be provided when setting availability. Days are defined as &lt;b&gt;sun, mon, tue, wed, thu, fri and sat&lt;/b&gt;. Start and End Times are entered in &lt;b&gt;military format. e.g., 800 is 8:00am, 2230 is 10:30pm&lt;/b&gt;. If there is no physical location and the business hours are irrelevant, set the hours to open 24 hours by setting startTime&#x3D;0 and endTime&#x3D;2400. To set a whole day as unavailable, set both the startTime and endTime to 0. &lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Settings&lt;/b&gt; can be set here. Booking timer minutes, book ahead restrictions and customer bookings per day are all available here. Please read about the settings scope parameter before setting these values as it may simplify your process.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Settings Scope&lt;/b&gt; can be set to the company or the business location level. You can have all locations use the same company level settings or individual business locations can define their own, business location scope. If you want to use the company settings throughout all locations, do not pass in &lt;b&gt;settings element&lt;/b&gt;. To create business location scoped settings, pass in the &lt;b&gt;settings element&lt;/b&gt; with the field values defined in the post body. &lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Appointment Reminders&lt;/b&gt; Reminder values are used to define how many hours, days, or weeks (interval value) prior to the appointment to send the reminder. &lt;b&gt;Interval&lt;/b&gt; values are used to define the reminder interval: &lt;b&gt;1 &#x3D; Hours&lt;/b&gt;, &lt;b&gt;2 &#x3D; Days&lt;/b&gt; and &lt;b&gt;3 &#x3D; Weeks&lt;/b&gt;. The reminder fields are numbers. If you are using the hours interval, use a number from 1 to 24.&lt;/p&gt;  &lt;p&gt;Example 1: &lt;b&gt;emailFirstReminder:  1, emailFirstReminderInterval:  2&lt;/b&gt; - results in 1st reminder being sent &lt;b&gt;1 Day before&lt;/b&gt; the appointment time.&lt;/p&gt;  &lt;p&gt;Example 2: &lt;b&gt;emailSecondReminder: 3, emailSecondReminderInterval: 1&lt;/b&gt; - results in 2nd reminder being sent &lt;b&gt;3 Hours before&lt;/b&gt; the appointment time.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;IMPORTANT DEPRECATION NOTICE&lt;/b&gt;: The following online settings parameters were intended for internal use in our Portal application only. They will be deprecated on &lt;b&gt;OCTOBER 15, 2022&lt;/b&gt;. These fields are currently part of the &lt;b&gt;SETTINGS&lt;/b&gt; object in all location endpoints: &lt;b&gt;businessId, enabled, familyMembersEnabled, serviceLabel, resourceLabel, resourceAnyLabel, resourceSelection, liveMode, formFlow, availabilityForm, showServiceGroups, showOnSchedLogo, showBusinessLogo, disableAuthorization, hideNavBar, hideLocationNav, hideServiceGroupsNav, hideServicesNav, hideContinueBooking, returnToService, returnToAvailability, hideBreadCrumbNav.&lt;/b&gt; If you are using these fields, please adjust your code to handle the deprecation or let us know by submitting a ticket to: &lt;b&gt;&lt;i&gt;support@onsched.com&lt;/i&gt;&lt;/b&gt; as we do not want to interrupt your existing workflows.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes

    """
    body = LocationsInputModel.from_dict(body)
    return web.Response(status=200)


async def setup_v1_locations_get(request: web.Request, name=None, service_id=None, friendly_id=None, deleted=None, offset=None, limit=None) -> web.Response:
    """List Locations

    &lt;p&gt;Use this endpoint to &lt;b&gt;List Business Locations&lt;/b&gt; associated with your company. The results are returned in pages. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;IMPORTANT DEPRECATION NOTICE&lt;/b&gt;: The following online settings parameters were intended for internal use in our Portal application only. They will be deprecated on &lt;b&gt;OCTOBER 15, 2022&lt;/b&gt;. These fields are currently part of the &lt;b&gt;SETTINGS&lt;/b&gt; object in all location endpoints: &lt;b&gt;businessId, enabled, familyMembersEnabled, serviceLabel, resourceLabel, resourceAnyLabel, resourceSelection, liveMode, formFlow, availabilityForm, showServiceGroups, showOnSchedLogo, showBusinessLogo, disableAuthorization, hideNavBar, hideLocationNav, hideServiceGroupsNav, hideServicesNav, hideContinueBooking, returnToService, returnToAvailability, hideBreadCrumbNav.&lt;/b&gt; If you are using these fields, please adjust your code to handle the deprecation or let us know by submitting a ticket to: &lt;b&gt;&lt;i&gt;support@onsched.com&lt;/i&gt;&lt;/b&gt; as we do not want to interrupt your existing workflows.&lt;/p&gt;

    :param name: Location name(full or partial) to filter on
    :type name: str
    :param service_id: Find locations that offer this service
    :type service_id: str
    :param friendly_id: friendlyId of location
    :type friendly_id: str
    :param deleted: Filter locations on deleted status
    :type deleted: bool
    :param offset: Starting row of page, default 0
    :type offset: int
    :param limit: Page limit default 20, max 100
    :type limit: int

    """
    return web.Response(status=200)


async def setup_v1_locations_id_appointmentreminders_get(request: web.Request, id) -> web.Response:
    """Get Reminders

    &lt;p&gt;Use this endpoint to &lt;b&gt;Get Email and SMS appointment reminder settings&lt;/b&gt; for the requested location. A valid business &lt;b&gt;location id&lt;/b&gt; is required. &lt;/p&gt;

    :param id: id of business location, defaults to primary business location
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_locations_id_appointmentreminders_put(request: web.Request, id, body=None) -> web.Response:
    """Update Reminders

    &lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; Email and SMS appointment reminder settings for the requested location. A valid business &lt;b&gt;location id&lt;/b&gt; is required. &lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Appointment Reminders&lt;/b&gt; Reminder values are used to define how many hours, days, or weeks (interval value) prior to the appointment to send the reminder. &lt;b&gt;Interval&lt;/b&gt; values are used to define the reminder interval: &lt;b&gt;1 &#x3D; Hours&lt;/b&gt;, &lt;b&gt;2 &#x3D; Days&lt;/b&gt; and &lt;b&gt;3 &#x3D; Weeks&lt;/b&gt;. The reminder fields are numbers. If you are using the hours interval, use a number from 1 to 24.&lt;/p&gt;  &lt;p&gt;Example 1: &lt;b&gt;emailFirstReminder:  1, emailFirstReminderInterval:  2&lt;/b&gt; - results in 1st reminder being sent &lt;b&gt;1 Day before&lt;/b&gt; the appointment time.&lt;/p&gt;  &lt;p&gt;Example 2: &lt;b&gt;emailSecondReminder: 3, emailSecondReminderInterval: 1&lt;/b&gt; - results in 2nd reminder being sent &lt;b&gt;3 Hours before&lt;/b&gt; the appointment time.&lt;/p&gt;

    :param id: id of business location, defaults to primary business location
    :type id: str
    :param body: input model for reminders
    :type body: dict | bytes

    """
    body = AppointmentRemindersInputModel.from_dict(body)
    return web.Response(status=200)


async def setup_v1_locations_id_delete(request: web.Request, id) -> web.Response:
    """Delete Location

    &lt;p&gt;Use this endpoint to &lt;b&gt;Delete&lt;/b&gt; a business location. A valid business &lt;b&gt;location id&lt;/b&gt; is required. The location is not permanently deleted and can be recovered by using the &lt;i&gt;PUT /setup​/v1​/locations​/{id}​/recover&lt;/i&gt; endpoint.&lt;/p&gt;

    :param id: id of business location, defaults to primary business location
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_locations_id_deleteallimages_delete(request: web.Request, id, uppercase=None) -> web.Response:
    """Delete All Location Images

    &lt;p&gt;Use this endpoint to &lt;b&gt;Delete All&lt;/b&gt; location images from the location blob storage container. An option exists to use upper case for matching the subdirectory name. Legacy apps stored pics using upper case while the API uses lower case names.&lt;/p&gt;

    :param id: 
    :type id: str
    :param uppercase: 
    :type uppercase: bool

    """
    return web.Response(status=200)


async def setup_v1_locations_id_deleteimage_delete(request: web.Request, id) -> web.Response:
    """Delete Location Image

    &lt;p&gt;Use this endpoint to &lt;b&gt;Delete&lt;/b&gt; a previously uploaded location image. A valid business &lt;b&gt;location id&lt;/b&gt; is required.&lt;/p&gt;

    :param id: id of business location, defaults to primary business location
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_locations_id_email_templates_get(request: web.Request, id) -> web.Response:
    """List Email Templates

    &lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Email Templates&lt;/b&gt; that are provided and may be customized. If the template has been customized, the customized property is true. The scope parameter indicates if the email template has been customized. This endpoint returns &lt;b&gt;only company level templates&lt;/b&gt;, so the scope is always company.&lt;/p&gt;

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_locations_id_email_templates_master_delete(request: web.Request, id) -> web.Response:
    """Delete Master Template Settings

    &lt;p&gt;Use this endpoint to &lt;b&gt;Delete Custom Master Email Template Settings&lt;/b&gt;. A valid business &lt;b&gt;location id&lt;/b&gt; is required. Deleting a custom master email template will reactivate the original default OnSched template settings.&lt;/p&gt;

    :param id: id of business location, defaults to primary business location
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_locations_id_email_templates_master_get(request: web.Request, id) -> web.Response:
    """Get Master Template Settings

    &lt;p&gt;Use this endpoint to get &lt;b&gt;Master Email Template Settings&lt;/b&gt;. A valid business &lt;b&gt;location id&lt;/b&gt; is required. Settings exist for showing or hiding panels and for changing color schemes. &lt;/p&gt;

    :param id: id of business location, defaults to primary business location
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_locations_id_email_templates_master_post(request: web.Request, id, body=None) -> web.Response:
    """Create Master Template Settings

    &lt;p&gt;Use this endpoint to &lt;b&gt;Create Custom Master Email Template Settings&lt;/b&gt;. A valid business &lt;b&gt;location id&lt;/b&gt; is required. Settings exist for showing or hiding email panels and for changing color schemes. Use the &lt;i&gt;GET ​/setup​/v1​/locations​/{id}​/email​/templates​/masterSettings&lt;/i&gt; endpoint to display the settings offered. Changes to the Master Template Settings will be reflected in all business locations associated with this company. &lt;/p&gt;  &lt;p&gt;The email template endpoints work a little differently than most. There are no endpoints to update the templates, we use the post endpoint to create a custom template instead. This endpoint creates a new custom Master Template Settings file that will be used instead. If you delete it, you are deleting the custom template settings you created and the original default Master Template created by OnSched would be reactivated.&lt;/p&gt;

    :param id: id of business location, defaults to primary business location
    :type id: str
    :param body: Input model for master email template settings
    :type body: dict | bytes

    """
    body = MasterTemplateSettingsInputModel.from_dict(body)
    return web.Response(status=200)


async def setup_v1_locations_id_email_templates_post(request: web.Request, id, body=None) -> web.Response:
    """Create Custom Template

    &lt;p&gt;Use this endpoint to a &lt;b&gt;Create&lt;/b&gt; a Custom Email Template. You must convert the content to a base64 encoded string. Updates to the primary business location create company scoped custom templates. Updates to non-primary business locations create business location scoped custom templates. The master template cannot be updated with this endpoint.&lt;/p&gt;  &lt;p&gt;The email template endpoints work a little differently than most. There are no endpoints to update the templates, we use the post endpoint to create a custom template instead. This endpoint creates a new email template that will be used instead. If you delete it, you are deleting the custom template you created and the original default template created by OnSched will be reactivated.&lt;/p&gt;

    :param id: id of business location, defaults to primary business location
    :type id: str
    :param body: Input model for email template
    :type body: dict | bytes

    """
    body = EmailTemplateInputModel.from_dict(body)
    return web.Response(status=200)


async def setup_v1_locations_id_email_templates_template_name_delete(request: web.Request, id, template_name) -> web.Response:
    """Delete Custom Template

    &lt;p&gt;Use this endpoint to &lt;b&gt;Delete&lt;/b&gt; a Custom Email Template that was previously created. A valid business &lt;b&gt;location id&lt;/b&gt; and email &lt;b&gt;templateName&lt;/b&gt; are required. Deleting a custom email template will revert the template back to its default originally created by OnSched. Changes will be reflected in all business locations associated with this company.&lt;/p&gt;  &lt;p&gt;The email template endpoints work a little differently than most. When you delete you are deleting the custom template you created, and the original default Email Template created by OnSched will be reactivated.&lt;/p&gt;

    :param id: id of business location, defaults to primary business location
    :type id: str
    :param template_name: Name of the email template
    :type template_name: str

    """
    return web.Response(status=200)


async def setup_v1_locations_id_email_templates_template_name_get(request: web.Request, id, template_name) -> web.Response:
    """Get Email Template

    &lt;p&gt;Use this endpoint to return the requested &lt;b&gt;Email Template&lt;/b&gt;. The template is from the primary business location. If it wasn&#39;t customized the default template is returned. The response content is in html format. A valid &lt;b&gt;emailTemplate name&lt;/b&gt; is required. Find template names by using the &lt;i&gt;GET ​/setup​/v1​/locations​/{id}​/email​/templates&lt;/i&gt; endpoint. Note: The master template cannot be accessed here. &lt;/p&gt;

    :param id: id of business location
    :type id: str
    :param template_name: name of the email template
    :type template_name: str

    """
    return web.Response(status=200)


async def setup_v1_locations_id_get(request: web.Request, id) -> web.Response:
    """Get Location

    &lt;p&gt;Use this endpoint to return a &lt;b&gt;Location&lt;/b&gt; object. A valid &lt;b&gt;location id&lt;/b&gt; is required. If not specified, the business location defaults to the primary business location. Find all business location id&#39;s, by using the &lt;i&gt;GET /consumer/v1/locations&lt;/i&gt; endpoint.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;IMPORTANT DEPRECATION NOTICE&lt;/b&gt;: The following online settings parameters were intended for internal use in our Portal application only. They will be deprecated on &lt;b&gt;OCTOBER 15, 2022&lt;/b&gt;. These fields are currently part of the &lt;b&gt;SETTINGS&lt;/b&gt; object in all location endpoints: &lt;b&gt;businessId, enabled, familyMembersEnabled, serviceLabel, resourceLabel, resourceAnyLabel, resourceSelection, liveMode, formFlow, availabilityForm, showServiceGroups, showOnSchedLogo, showBusinessLogo, disableAuthorization, hideNavBar, hideLocationNav, hideServiceGroupsNav, hideServicesNav, hideContinueBooking, returnToService, returnToAvailability, hideBreadCrumbNav.&lt;/b&gt; If you are using these fields, please adjust your code to handle the deprecation or let us know by submitting a ticket to: &lt;b&gt;&lt;i&gt;support@onsched.com&lt;/i&gt;&lt;/b&gt; as we do not want to interrupt your existing workflows.&lt;/p&gt;

    :param id: id of business location, defaults to primary business location
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_locations_id_google_service_account_delete(request: web.Request, id) -> web.Response:
    """Delete Google Cal Access

    &lt;p&gt;Use this endpoint to &lt;b&gt;Delete&lt;/b&gt; authorized access to all google calendar users in your organization. Upon deletion Google Calendars will no longer be synced for resources.&lt;/p&gt;

    :param id: id of business location, defaults to primary business location
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_locations_id_google_service_account_post(request: web.Request, id, body=None) -> web.Response:
    """Create Google Cal Access

    &lt;p&gt;Use this endpoint to &lt;b&gt;Authorize Access&lt;/b&gt; to google calendar users in your organization. You must create/have a Google Service account as an admin of your GSuite, then save the credentials as a Json Key file. This &lt;b&gt;Json Key&lt;/b&gt; and a valid business &lt;b&gt;location id&lt;/b&gt; are required. &lt;/p&gt;

    :param id: id of business location, defaults to primary business location
    :type id: str
    :param body: Generated Json Key file from Google
    :type body: dict | bytes

    """
    body = GoogleServiceAccountCreds.from_dict(body)
    return web.Response(status=200)


async def setup_v1_locations_id_holidays_holiday_id_closed_put(request: web.Request, id, holiday_id, closed) -> web.Response:
    """Update Location Holidays

    &lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; Business Holidays as Opened or Closed. A valid business &lt;b&gt;location id&lt;/b&gt; is required. If not specified, the business location defaults to the primary business location.&lt;/p&gt;  &lt;p&gt;Holidays are automatically defined with the initial Post Location endpoint and are based on country code. Find your location holiday codes by using the: &lt;i&gt;GET /setup​/v1​/locations​/{id}&lt;/i&gt; endpoint. Change your holidays to open or closed by passing in the &lt;b&gt;holidayId&lt;/b&gt; along with the &lt;b&gt;closed&lt;/b&gt; boolean value to change the status of a specific holiday. Pass in an &lt;b&gt;asterisk *&lt;/b&gt; for the holidayId then all business holidays will be set as defined.&lt;/p&gt;

    :param id: 
    :type id: str
    :param holiday_id: 
    :type holiday_id: str
    :param closed: 
    :type closed: bool

    """
    return web.Response(status=200)


async def setup_v1_locations_id_put(request: web.Request, id, remove_region=None, body=None) -> web.Response:
    """Update Location

    &lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; a business location object. A valid business &lt;b&gt;location id&lt;/b&gt; is required. The optional removeRegion query parameter can be used to remove the region relationship from the location.&lt;/p&gt;  &lt;p&gt;If the settings element is populated the scope will be set to the business location with the settings supplied. If your settings are uniform across all locations, then do not supply the settings element and the location will use the settings defined on the primary business location (company scoped). Company scoped settings cascade down to the locations. You can override any location that needs different settings by providing settings in the update model. Use the &lt;i&gt;PUT /setup/v1/locations/{id}/settings/scope/{settingsScope}&lt;/i&gt; endpoint to change the settings scope only. This is typically used when switching from business location scope back to company.&lt;/p&gt;  &lt;p&gt;Refer to: &lt;i&gt;&lt;b&gt;POST ​/setup​/v1​/locations&lt;/b&gt;&lt;/i&gt; endpoint for details.&lt;/p&gt;

    :param id: 
    :type id: str
    :param remove_region: 
    :type remove_region: bool
    :param body: 
    :type body: dict | bytes

    """
    body = LocationUpdateModel.from_dict(body)
    return web.Response(status=200)


async def setup_v1_locations_id_recover_put(request: web.Request, id) -> web.Response:
    """Recover Location

    &lt;p&gt;Use this endpoint to &lt;b&gt;Recover&lt;/b&gt; a deleted business location. A valid business &lt;b&gt;location id&lt;/b&gt; is required.&lt;/p&gt;

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_locations_id_services_delete(request: web.Request, id) -> web.Response:
    """Delete Linked Services

    &lt;p&gt;Use this endpoint to &lt;b&gt;Delete All&lt;/b&gt; location linked services from a business location. A valid business &lt;b&gt;location id&lt;/b&gt; is required. &lt;/p&gt;

    :param id: id of business location, defaults to primary business location
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_locations_id_services_get(request: web.Request, id, offset=None, limit=None) -> web.Response:
    """List Location Linked Services

    &lt;p&gt;Use this endpoint to return a list of &lt;b&gt;Location Linked Services&lt;/b&gt;. A valid business &lt;b&gt;location id&lt;/b&gt; is required. By default, there are no location linked services attached to a location. Refer to the: &lt;i&gt;POST /setup​/v1​/locations​/{id}​/services&lt;/i&gt; for details. The results are returned in pages. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.&lt;/p&gt;

    :param id: id of business location, defaults to primary business location
    :type id: str
    :param offset: Starting row of page, default 0
    :type offset: int
    :param limit: Page limit default 20, max 100
    :type limit: int

    """
    return web.Response(status=200)


async def setup_v1_locations_id_services_post(request: web.Request, id, body=None) -> web.Response:
    """Create Linked Service

    &lt;p&gt;Use this endpoint to &lt;b&gt;Link Services&lt;/b&gt; to a location object. A valid business &lt;b&gt;location id&lt;/b&gt; is required. By default, there are &lt;i&gt;no services linked&lt;/i&gt; to a location. &lt;/p&gt;  &lt;p&gt;Services are definable globally at the Company level and associated with the Primary Business Location, or at a Secondary Business Location. When accessing the Services endpoints, by default, API consumers are provided with a &lt;b&gt;combined&lt;/b&gt; list of Services defined from both the Primary and Secondary Business Location.&lt;/p&gt;  &lt;p&gt;If necessary, the list of Service(s) provided can be cherry-picked/linked to &lt;b&gt;only include specific Service(s)&lt;/b&gt; by using this endpoint. This allows for a subset of defined Services to be provided for a location.&lt;/p&gt;  &lt;p&gt;Supplying the list of services ids to cherry-pick/link to the location in the request body will explicitly define which Primary Location Services are offered by the specified business location.&lt;/p&gt;

    :param id: id of business location, defaults to primary business location
    :type id: str
    :param body: array of valid service object id&#39;s
    :type body: List[str]

    """
    return web.Response(status=200)


async def setup_v1_locations_id_settings_scope_settings_scope_put(request: web.Request, id, settings_scope) -> web.Response:
    """Update Location Scope

    &lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; a business locations online booking settings scope. A valid business &lt;b&gt;location id&lt;/b&gt; is required.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;settingsScope&lt;/b&gt; values are &lt;b&gt;0 &#x3D; company scope, 1 &#x3D; business location scope&lt;/b&gt;. To inherit the online settings defined in the primary business location, then use value &#x3D; 0 for company scope. Otherwise, to override the settings for a specific location then use value &#x3D; 1 for business location scope. &lt;b&gt;Note&lt;/b&gt;: You cannot change the settings scope of the Primary Business Location.&lt;/p&gt;

    :param id: 
    :type id: str
    :param settings_scope: 
    :type settings_scope: str

    """
    return web.Response(status=200)


async def setup_v1_locations_id_uploadimage_post(request: web.Request, id, body=None) -> web.Response:
    """Upload Location Image

    &lt;p&gt;Use this endpoint to &lt;b&gt;Upload&lt;/b&gt; an image to a location object. A valid business &lt;b&gt;location id&lt;/b&gt; is required. You must convert the image to a &lt;b&gt;base64 encoded string&lt;/b&gt; and pass that string as input along with your &lt;b&gt;filename&lt;/b&gt;.&lt;/p&gt;

    :param id: id of business location, defaults to primary business location
    :type id: str
    :param body: Input model for image upload
    :type body: dict | bytes

    """
    body = ResourceImageInputModel.from_dict(body)
    return web.Response(status=200)


async def setup_v1_locations_post(request: web.Request, body=None) -> web.Response:
    """Create Location

    &lt;p&gt;Use this endpoint to &lt;b&gt;Create&lt;/b&gt; a new business location. The result is a business location object with a GUID assigned to the location.&lt;/p&gt;  &lt;p&gt;The &lt;b&gt;name&lt;/b&gt; and &lt;b&gt;timezoneName&lt;/b&gt; fields are required. The &lt;b&gt;timezoneName&lt;/b&gt; must be expressed as an IANA Timezone e.g., &lt;i&gt;America/New_York&lt;/i&gt;. Refer to: &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/List_of_tz_database_time_zones\&quot;&gt;Timezone Wiki&lt;/a&gt; for a listing of IANA time zones.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Business hours&lt;/b&gt; are set by defining the &lt;b&gt;startTime&lt;/b&gt; and &lt;b&gt;endTime&lt;/b&gt; values for each day available/open. All days of the week must be provided when setting availability. Days are defined as &lt;b&gt;sun, mon, tue, wed, thu, fri and sat&lt;/b&gt;. Start and End Times are entered in &lt;b&gt;military format. e.g., 800 is 8:00am, 2230 is 10:30pm&lt;/b&gt;. If there is no physical location and the business hours are irrelevant, set the hours to open 24 hours by setting startTime&#x3D;0 and endTime&#x3D;2400. To set a whole day as unavailable, set both the startTime and endTime to 0. &lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Settings&lt;/b&gt; can be set here. Booking timer minutes, book ahead restrictions and customer bookings per day are all available here. Please read about the settings scope parameter before setting these values as it may simplify your process.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Settings Scope&lt;/b&gt; can be set to the company or the business location level. You can have all locations use the same company level settings or individual business locations can define their own, business location scope. If you want to use the company settings throughout all locations, do not pass in &lt;b&gt;settings element&lt;/b&gt;. To create business location scoped settings, pass in the &lt;b&gt;settings element&lt;/b&gt; with the field values defined in the post body. &lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Appointment Reminders&lt;/b&gt; Reminder values are used to define how many hours, days, or weeks (interval value) prior to the appointment to send the reminder. &lt;b&gt;Interval&lt;/b&gt; values are used to define the reminder interval: &lt;b&gt;1 &#x3D; Hours&lt;/b&gt;, &lt;b&gt;2 &#x3D; Days&lt;/b&gt; and &lt;b&gt;3 &#x3D; Weeks&lt;/b&gt;. The reminder fields are numbers. If you are using the hours interval, use a number from 1 to 24.&lt;/p&gt;  &lt;p&gt;Example 1: &lt;b&gt;emailFirstReminder:  1, emailFirstReminderInterval:  2&lt;/b&gt; - results in 1st reminder being sent &lt;b&gt;1 Day before&lt;/b&gt; the appointment time.&lt;/p&gt;  &lt;p&gt;Example 2: &lt;b&gt;emailSecondReminder: 3, emailSecondReminderInterval: 1&lt;/b&gt; - results in 2nd reminder being sent &lt;b&gt;3 Hours before&lt;/b&gt; the appointment time.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;IMPORTANT DEPRECATION NOTICE&lt;/b&gt;: The following online settings parameters were intended for internal use in our Portal application only. They will be deprecated on &lt;b&gt;OCTOBER 15, 2022&lt;/b&gt;. These fields are currently part of the &lt;b&gt;SETTINGS&lt;/b&gt; object in all location endpoints: &lt;b&gt;businessId, enabled, familyMembersEnabled, serviceLabel, resourceLabel, resourceAnyLabel, resourceSelection, liveMode, formFlow, availabilityForm, showServiceGroups, showOnSchedLogo, showBusinessLogo, disableAuthorization, hideNavBar, hideLocationNav, hideServiceGroupsNav, hideServicesNav, hideContinueBooking, returnToService, returnToAvailability, hideBreadCrumbNav.&lt;/b&gt; If you are using these fields, please adjust your code to handle the deprecation or let us know by submitting a ticket to: &lt;b&gt;&lt;i&gt;support@onsched.com&lt;/i&gt;&lt;/b&gt; as we do not want to interrupt your existing workflows.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes

    """
    body = LocationInputModel.from_dict(body)
    return web.Response(status=200)


async def setup_v1_locations_services_id_delete(request: web.Request, id) -> web.Response:
    """Unlink Service

    &lt;p&gt;Use this endpoint to &lt;b&gt;Unlink&lt;/b&gt; a location service from a business location. A valid &lt;b&gt;locationService id&lt;/b&gt; is required. Find location services by using the &lt;i&gt;GET ​/setup​/v1​/locations​/{id}​/services&lt;/i&gt; endpoint. &lt;/p&gt;

    :param id: id of locationService object
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_locations_services_id_get(request: web.Request, id) -> web.Response:
    """Get Linked Service

    &lt;p&gt;Use this endpoint to &lt;b&gt;Get a Linked Service&lt;/b&gt;. A valid &lt;b&gt;locationService id&lt;/b&gt; is required.&lt;/p&gt;

    :param id: id of locationService object
    :type id: str

    """
    return web.Response(status=200)
