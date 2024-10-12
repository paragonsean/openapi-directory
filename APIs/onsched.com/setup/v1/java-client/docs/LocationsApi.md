# LocationsApi

All URIs are relative to *https://sandbox-api.onsched.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**setupV1LocationsBulkPost**](LocationsApi.md#setupV1LocationsBulkPost) | **POST** /setup/v1/locations/bulk | Create Locations Bulk |
| [**setupV1LocationsGet**](LocationsApi.md#setupV1LocationsGet) | **GET** /setup/v1/locations | List Locations |
| [**setupV1LocationsIdAppointmentremindersGet**](LocationsApi.md#setupV1LocationsIdAppointmentremindersGet) | **GET** /setup/v1/locations/{id}/appointmentreminders | Get Reminders |
| [**setupV1LocationsIdAppointmentremindersPut**](LocationsApi.md#setupV1LocationsIdAppointmentremindersPut) | **PUT** /setup/v1/locations/{id}/appointmentreminders | Update Reminders |
| [**setupV1LocationsIdDelete**](LocationsApi.md#setupV1LocationsIdDelete) | **DELETE** /setup/v1/locations/{id} | Delete Location |
| [**setupV1LocationsIdDeleteallimagesDelete**](LocationsApi.md#setupV1LocationsIdDeleteallimagesDelete) | **DELETE** /setup/v1/locations/{id}/deleteallimages | Delete All Location Images |
| [**setupV1LocationsIdDeleteimageDelete**](LocationsApi.md#setupV1LocationsIdDeleteimageDelete) | **DELETE** /setup/v1/locations/{id}/deleteimage | Delete Location Image |
| [**setupV1LocationsIdEmailTemplatesGet**](LocationsApi.md#setupV1LocationsIdEmailTemplatesGet) | **GET** /setup/v1/locations/{id}/email/templates | List Email Templates |
| [**setupV1LocationsIdEmailTemplatesMasterDelete**](LocationsApi.md#setupV1LocationsIdEmailTemplatesMasterDelete) | **DELETE** /setup/v1/locations/{id}/email/templates/master | Delete Master Template Settings |
| [**setupV1LocationsIdEmailTemplatesMasterGet**](LocationsApi.md#setupV1LocationsIdEmailTemplatesMasterGet) | **GET** /setup/v1/locations/{id}/email/templates/master | Get Master Template Settings |
| [**setupV1LocationsIdEmailTemplatesMasterPost**](LocationsApi.md#setupV1LocationsIdEmailTemplatesMasterPost) | **POST** /setup/v1/locations/{id}/email/templates/master | Create Master Template Settings |
| [**setupV1LocationsIdEmailTemplatesPost**](LocationsApi.md#setupV1LocationsIdEmailTemplatesPost) | **POST** /setup/v1/locations/{id}/email/templates | Create Custom Template |
| [**setupV1LocationsIdEmailTemplatesTemplateNameDelete**](LocationsApi.md#setupV1LocationsIdEmailTemplatesTemplateNameDelete) | **DELETE** /setup/v1/locations/{id}/email/templates/{templateName} | Delete Custom Template |
| [**setupV1LocationsIdEmailTemplatesTemplateNameGet**](LocationsApi.md#setupV1LocationsIdEmailTemplatesTemplateNameGet) | **GET** /setup/v1/locations/{id}/email/templates/{templateName} | Get Email Template |
| [**setupV1LocationsIdGet**](LocationsApi.md#setupV1LocationsIdGet) | **GET** /setup/v1/locations/{id} | Get Location |
| [**setupV1LocationsIdGoogleServiceAccountDelete**](LocationsApi.md#setupV1LocationsIdGoogleServiceAccountDelete) | **DELETE** /setup/v1/locations/{id}/google/service/account | Delete Google Cal Access |
| [**setupV1LocationsIdGoogleServiceAccountPost**](LocationsApi.md#setupV1LocationsIdGoogleServiceAccountPost) | **POST** /setup/v1/locations/{id}/google/service/account | Create Google Cal Access |
| [**setupV1LocationsIdHolidaysHolidayIdClosedPut**](LocationsApi.md#setupV1LocationsIdHolidaysHolidayIdClosedPut) | **PUT** /setup/v1/locations/{id}/holidays/{holidayId}/{closed} | Update Location Holidays |
| [**setupV1LocationsIdPut**](LocationsApi.md#setupV1LocationsIdPut) | **PUT** /setup/v1/locations/{id} | Update Location |
| [**setupV1LocationsIdRecoverPut**](LocationsApi.md#setupV1LocationsIdRecoverPut) | **PUT** /setup/v1/locations/{id}/recover | Recover Location |
| [**setupV1LocationsIdServicesDelete**](LocationsApi.md#setupV1LocationsIdServicesDelete) | **DELETE** /setup/v1/locations/{id}/services | Delete Linked Services |
| [**setupV1LocationsIdServicesGet**](LocationsApi.md#setupV1LocationsIdServicesGet) | **GET** /setup/v1/locations/{id}/services | List Location Linked Services |
| [**setupV1LocationsIdServicesPost**](LocationsApi.md#setupV1LocationsIdServicesPost) | **POST** /setup/v1/locations/{id}/services | Create Linked Service |
| [**setupV1LocationsIdSettingsScopeSettingsScopePut**](LocationsApi.md#setupV1LocationsIdSettingsScopeSettingsScopePut) | **PUT** /setup/v1/locations/{id}/settings/scope/{settingsScope} | Update Location Scope |
| [**setupV1LocationsIdUploadimagePost**](LocationsApi.md#setupV1LocationsIdUploadimagePost) | **POST** /setup/v1/locations/{id}/uploadimage | Upload Location Image |
| [**setupV1LocationsPost**](LocationsApi.md#setupV1LocationsPost) | **POST** /setup/v1/locations | Create Location |
| [**setupV1LocationsServicesIdDelete**](LocationsApi.md#setupV1LocationsServicesIdDelete) | **DELETE** /setup/v1/locations/services/{id} | Unlink Service |
| [**setupV1LocationsServicesIdGet**](LocationsApi.md#setupV1LocationsServicesIdGet) | **GET** /setup/v1/locations/services/{id} | Get Linked Service |


<a id="setupV1LocationsBulkPost"></a>
# **setupV1LocationsBulkPost**
> List&lt;LocationViewModel&gt; setupV1LocationsBulkPost(locationsInputModel)

Create Locations Bulk

&lt;p&gt;Use this endpoint to &lt;b&gt;Create Bulk&lt;/b&gt; business locations. The posted list of locations cannot exceed 100 location objects per transaction for performance purposes. The result is a list of new business location objects with a GUID assigned to each location.&lt;/p&gt;  &lt;p&gt;The &lt;b&gt;name&lt;/b&gt; and &lt;b&gt;timezoneName&lt;/b&gt; fields are required. The &lt;b&gt;timezoneName&lt;/b&gt; must be expressed as an IANA Timezone e.g., &lt;i&gt;America/New_York&lt;/i&gt;. Refer to: &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/List_of_tz_database_time_zones\&quot;&gt;Timezone Wiki&lt;/a&gt; for a listing of IANA time zones.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Business hours&lt;/b&gt; are set by defining the &lt;b&gt;startTime&lt;/b&gt; and &lt;b&gt;endTime&lt;/b&gt; values for each day available/open. All days of the week must be provided when setting availability. Days are defined as &lt;b&gt;sun, mon, tue, wed, thu, fri and sat&lt;/b&gt;. Start and End Times are entered in &lt;b&gt;military format. e.g., 800 is 8:00am, 2230 is 10:30pm&lt;/b&gt;. If there is no physical location and the business hours are irrelevant, set the hours to open 24 hours by setting startTime&#x3D;0 and endTime&#x3D;2400. To set a whole day as unavailable, set both the startTime and endTime to 0. &lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Settings&lt;/b&gt; can be set here. Booking timer minutes, book ahead restrictions and customer bookings per day are all available here. Please read about the settings scope parameter before setting these values as it may simplify your process.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Settings Scope&lt;/b&gt; can be set to the company or the business location level. You can have all locations use the same company level settings or individual business locations can define their own, business location scope. If you want to use the company settings throughout all locations, do not pass in &lt;b&gt;settings element&lt;/b&gt;. To create business location scoped settings, pass in the &lt;b&gt;settings element&lt;/b&gt; with the field values defined in the post body. &lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Appointment Reminders&lt;/b&gt; Reminder values are used to define how many hours, days, or weeks (interval value) prior to the appointment to send the reminder. &lt;b&gt;Interval&lt;/b&gt; values are used to define the reminder interval: &lt;b&gt;1 &#x3D; Hours&lt;/b&gt;, &lt;b&gt;2 &#x3D; Days&lt;/b&gt; and &lt;b&gt;3 &#x3D; Weeks&lt;/b&gt;. The reminder fields are numbers. If you are using the hours interval, use a number from 1 to 24.&lt;/p&gt;  &lt;p&gt;Example 1: &lt;b&gt;emailFirstReminder:  1, emailFirstReminderInterval:  2&lt;/b&gt; - results in 1st reminder being sent &lt;b&gt;1 Day before&lt;/b&gt; the appointment time.&lt;/p&gt;  &lt;p&gt;Example 2: &lt;b&gt;emailSecondReminder: 3, emailSecondReminderInterval: 1&lt;/b&gt; - results in 2nd reminder being sent &lt;b&gt;3 Hours before&lt;/b&gt; the appointment time.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;IMPORTANT DEPRECATION NOTICE&lt;/b&gt;: The following online settings parameters were intended for internal use in our Portal application only. They will be deprecated on &lt;b&gt;OCTOBER 15, 2022&lt;/b&gt;. These fields are currently part of the &lt;b&gt;SETTINGS&lt;/b&gt; object in all location endpoints: &lt;b&gt;businessId, enabled, familyMembersEnabled, serviceLabel, resourceLabel, resourceAnyLabel, resourceSelection, liveMode, formFlow, availabilityForm, showServiceGroups, showOnSchedLogo, showBusinessLogo, disableAuthorization, hideNavBar, hideLocationNav, hideServiceGroupsNav, hideServicesNav, hideContinueBooking, returnToService, returnToAvailability, hideBreadCrumbNav.&lt;/b&gt; If you are using these fields, please adjust your code to handle the deprecation or let us know by submitting a ticket to: &lt;b&gt;&lt;i&gt;support@onsched.com&lt;/i&gt;&lt;/b&gt; as we do not want to interrupt your existing workflows.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    LocationsInputModel locationsInputModel = new LocationsInputModel(); // LocationsInputModel | 
    try {
      List<LocationViewModel> result = apiInstance.setupV1LocationsBulkPost(locationsInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#setupV1LocationsBulkPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **locationsInputModel** | [**LocationsInputModel**](LocationsInputModel.md)|  | [optional] |

### Return type

[**List&lt;LocationViewModel&gt;**](LocationViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1LocationsGet"></a>
# **setupV1LocationsGet**
> LocationListViewModel setupV1LocationsGet(name, serviceId, friendlyId, deleted, offset, limit)

List Locations

&lt;p&gt;Use this endpoint to &lt;b&gt;List Business Locations&lt;/b&gt; associated with your company. The results are returned in pages. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;IMPORTANT DEPRECATION NOTICE&lt;/b&gt;: The following online settings parameters were intended for internal use in our Portal application only. They will be deprecated on &lt;b&gt;OCTOBER 15, 2022&lt;/b&gt;. These fields are currently part of the &lt;b&gt;SETTINGS&lt;/b&gt; object in all location endpoints: &lt;b&gt;businessId, enabled, familyMembersEnabled, serviceLabel, resourceLabel, resourceAnyLabel, resourceSelection, liveMode, formFlow, availabilityForm, showServiceGroups, showOnSchedLogo, showBusinessLogo, disableAuthorization, hideNavBar, hideLocationNav, hideServiceGroupsNav, hideServicesNav, hideContinueBooking, returnToService, returnToAvailability, hideBreadCrumbNav.&lt;/b&gt; If you are using these fields, please adjust your code to handle the deprecation or let us know by submitting a ticket to: &lt;b&gt;&lt;i&gt;support@onsched.com&lt;/i&gt;&lt;/b&gt; as we do not want to interrupt your existing workflows.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String name = "name_example"; // String | Location name(full or partial) to filter on
    String serviceId = "serviceId_example"; // String | Find locations that offer this service
    String friendlyId = "friendlyId_example"; // String | friendlyId of location
    Boolean deleted = true; // Boolean | Filter locations on deleted status
    Integer offset = 56; // Integer | Starting row of page, default 0
    Integer limit = 56; // Integer | Page limit default 20, max 100
    try {
      LocationListViewModel result = apiInstance.setupV1LocationsGet(name, serviceId, friendlyId, deleted, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#setupV1LocationsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| Location name(full or partial) to filter on | [optional] |
| **serviceId** | **String**| Find locations that offer this service | [optional] |
| **friendlyId** | **String**| friendlyId of location | [optional] |
| **deleted** | **Boolean**| Filter locations on deleted status | [optional] |
| **offset** | **Integer**| Starting row of page, default 0 | [optional] |
| **limit** | **Integer**| Page limit default 20, max 100 | [optional] |

### Return type

[**LocationListViewModel**](LocationListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1LocationsIdAppointmentremindersGet"></a>
# **setupV1LocationsIdAppointmentremindersGet**
> AppointmentReminderViewModel setupV1LocationsIdAppointmentremindersGet(id)

Get Reminders

&lt;p&gt;Use this endpoint to &lt;b&gt;Get Email and SMS appointment reminder settings&lt;/b&gt; for the requested location. A valid business &lt;b&gt;location id&lt;/b&gt; is required. &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String id = "id_example"; // String | id of business location, defaults to primary business location
    try {
      AppointmentReminderViewModel result = apiInstance.setupV1LocationsIdAppointmentremindersGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#setupV1LocationsIdAppointmentremindersGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| id of business location, defaults to primary business location | |

### Return type

[**AppointmentReminderViewModel**](AppointmentReminderViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1LocationsIdAppointmentremindersPut"></a>
# **setupV1LocationsIdAppointmentremindersPut**
> LocationViewModel setupV1LocationsIdAppointmentremindersPut(id, appointmentRemindersInputModel)

Update Reminders

&lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; Email and SMS appointment reminder settings for the requested location. A valid business &lt;b&gt;location id&lt;/b&gt; is required. &lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Appointment Reminders&lt;/b&gt; Reminder values are used to define how many hours, days, or weeks (interval value) prior to the appointment to send the reminder. &lt;b&gt;Interval&lt;/b&gt; values are used to define the reminder interval: &lt;b&gt;1 &#x3D; Hours&lt;/b&gt;, &lt;b&gt;2 &#x3D; Days&lt;/b&gt; and &lt;b&gt;3 &#x3D; Weeks&lt;/b&gt;. The reminder fields are numbers. If you are using the hours interval, use a number from 1 to 24.&lt;/p&gt;  &lt;p&gt;Example 1: &lt;b&gt;emailFirstReminder:  1, emailFirstReminderInterval:  2&lt;/b&gt; - results in 1st reminder being sent &lt;b&gt;1 Day before&lt;/b&gt; the appointment time.&lt;/p&gt;  &lt;p&gt;Example 2: &lt;b&gt;emailSecondReminder: 3, emailSecondReminderInterval: 1&lt;/b&gt; - results in 2nd reminder being sent &lt;b&gt;3 Hours before&lt;/b&gt; the appointment time.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String id = "id_example"; // String | id of business location, defaults to primary business location
    AppointmentRemindersInputModel appointmentRemindersInputModel = new AppointmentRemindersInputModel(); // AppointmentRemindersInputModel | input model for reminders
    try {
      LocationViewModel result = apiInstance.setupV1LocationsIdAppointmentremindersPut(id, appointmentRemindersInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#setupV1LocationsIdAppointmentremindersPut");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| id of business location, defaults to primary business location | |
| **appointmentRemindersInputModel** | [**AppointmentRemindersInputModel**](AppointmentRemindersInputModel.md)| input model for reminders | [optional] |

### Return type

[**LocationViewModel**](LocationViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1LocationsIdDelete"></a>
# **setupV1LocationsIdDelete**
> LocationViewModel setupV1LocationsIdDelete(id)

Delete Location

&lt;p&gt;Use this endpoint to &lt;b&gt;Delete&lt;/b&gt; a business location. A valid business &lt;b&gt;location id&lt;/b&gt; is required. The location is not permanently deleted and can be recovered by using the &lt;i&gt;PUT /setup​/v1​/locations​/{id}​/recover&lt;/i&gt; endpoint.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String id = "id_example"; // String | id of business location, defaults to primary business location
    try {
      LocationViewModel result = apiInstance.setupV1LocationsIdDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#setupV1LocationsIdDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| id of business location, defaults to primary business location | |

### Return type

[**LocationViewModel**](LocationViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1LocationsIdDeleteallimagesDelete"></a>
# **setupV1LocationsIdDeleteallimagesDelete**
> Boolean setupV1LocationsIdDeleteallimagesDelete(id, uppercase)

Delete All Location Images

&lt;p&gt;Use this endpoint to &lt;b&gt;Delete All&lt;/b&gt; location images from the location blob storage container. An option exists to use upper case for matching the subdirectory name. Legacy apps stored pics using upper case while the API uses lower case names.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String id = "id_example"; // String | 
    Boolean uppercase = true; // Boolean | 
    try {
      Boolean result = apiInstance.setupV1LocationsIdDeleteallimagesDelete(id, uppercase);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#setupV1LocationsIdDeleteallimagesDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **uppercase** | **Boolean**|  | [optional] |

### Return type

**Boolean**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1LocationsIdDeleteimageDelete"></a>
# **setupV1LocationsIdDeleteimageDelete**
> LocationViewModel setupV1LocationsIdDeleteimageDelete(id)

Delete Location Image

&lt;p&gt;Use this endpoint to &lt;b&gt;Delete&lt;/b&gt; a previously uploaded location image. A valid business &lt;b&gt;location id&lt;/b&gt; is required.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String id = "id_example"; // String | id of business location, defaults to primary business location
    try {
      LocationViewModel result = apiInstance.setupV1LocationsIdDeleteimageDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#setupV1LocationsIdDeleteimageDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| id of business location, defaults to primary business location | |

### Return type

[**LocationViewModel**](LocationViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1LocationsIdEmailTemplatesGet"></a>
# **setupV1LocationsIdEmailTemplatesGet**
> EmailTemplateListViewModel setupV1LocationsIdEmailTemplatesGet(id)

List Email Templates

&lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Email Templates&lt;/b&gt; that are provided and may be customized. If the template has been customized, the customized property is true. The scope parameter indicates if the email template has been customized. This endpoint returns &lt;b&gt;only company level templates&lt;/b&gt;, so the scope is always company.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      EmailTemplateListViewModel result = apiInstance.setupV1LocationsIdEmailTemplatesGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#setupV1LocationsIdEmailTemplatesGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |

### Return type

[**EmailTemplateListViewModel**](EmailTemplateListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1LocationsIdEmailTemplatesMasterDelete"></a>
# **setupV1LocationsIdEmailTemplatesMasterDelete**
> MasterEmailTemplateSettingsViewModel setupV1LocationsIdEmailTemplatesMasterDelete(id)

Delete Master Template Settings

&lt;p&gt;Use this endpoint to &lt;b&gt;Delete Custom Master Email Template Settings&lt;/b&gt;. A valid business &lt;b&gt;location id&lt;/b&gt; is required. Deleting a custom master email template will reactivate the original default OnSched template settings.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String id = "id_example"; // String | id of business location, defaults to primary business location
    try {
      MasterEmailTemplateSettingsViewModel result = apiInstance.setupV1LocationsIdEmailTemplatesMasterDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#setupV1LocationsIdEmailTemplatesMasterDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| id of business location, defaults to primary business location | |

### Return type

[**MasterEmailTemplateSettingsViewModel**](MasterEmailTemplateSettingsViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1LocationsIdEmailTemplatesMasterGet"></a>
# **setupV1LocationsIdEmailTemplatesMasterGet**
> MasterEmailTemplateSettingsViewModel setupV1LocationsIdEmailTemplatesMasterGet(id)

Get Master Template Settings

&lt;p&gt;Use this endpoint to get &lt;b&gt;Master Email Template Settings&lt;/b&gt;. A valid business &lt;b&gt;location id&lt;/b&gt; is required. Settings exist for showing or hiding panels and for changing color schemes. &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String id = "id_example"; // String | id of business location, defaults to primary business location
    try {
      MasterEmailTemplateSettingsViewModel result = apiInstance.setupV1LocationsIdEmailTemplatesMasterGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#setupV1LocationsIdEmailTemplatesMasterGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| id of business location, defaults to primary business location | |

### Return type

[**MasterEmailTemplateSettingsViewModel**](MasterEmailTemplateSettingsViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1LocationsIdEmailTemplatesMasterPost"></a>
# **setupV1LocationsIdEmailTemplatesMasterPost**
> MasterEmailTemplateSettingsViewModel setupV1LocationsIdEmailTemplatesMasterPost(id, masterTemplateSettingsInputModel)

Create Master Template Settings

&lt;p&gt;Use this endpoint to &lt;b&gt;Create Custom Master Email Template Settings&lt;/b&gt;. A valid business &lt;b&gt;location id&lt;/b&gt; is required. Settings exist for showing or hiding email panels and for changing color schemes. Use the &lt;i&gt;GET ​/setup​/v1​/locations​/{id}​/email​/templates​/masterSettings&lt;/i&gt; endpoint to display the settings offered. Changes to the Master Template Settings will be reflected in all business locations associated with this company. &lt;/p&gt;  &lt;p&gt;The email template endpoints work a little differently than most. There are no endpoints to update the templates, we use the post endpoint to create a custom template instead. This endpoint creates a new custom Master Template Settings file that will be used instead. If you delete it, you are deleting the custom template settings you created and the original default Master Template created by OnSched would be reactivated.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String id = "id_example"; // String | id of business location, defaults to primary business location
    MasterTemplateSettingsInputModel masterTemplateSettingsInputModel = new MasterTemplateSettingsInputModel(); // MasterTemplateSettingsInputModel | Input model for master email template settings
    try {
      MasterEmailTemplateSettingsViewModel result = apiInstance.setupV1LocationsIdEmailTemplatesMasterPost(id, masterTemplateSettingsInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#setupV1LocationsIdEmailTemplatesMasterPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| id of business location, defaults to primary business location | |
| **masterTemplateSettingsInputModel** | [**MasterTemplateSettingsInputModel**](MasterTemplateSettingsInputModel.md)| Input model for master email template settings | [optional] |

### Return type

[**MasterEmailTemplateSettingsViewModel**](MasterEmailTemplateSettingsViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1LocationsIdEmailTemplatesPost"></a>
# **setupV1LocationsIdEmailTemplatesPost**
> ContentResult setupV1LocationsIdEmailTemplatesPost(id, emailTemplateInputModel)

Create Custom Template

&lt;p&gt;Use this endpoint to a &lt;b&gt;Create&lt;/b&gt; a Custom Email Template. You must convert the content to a base64 encoded string. Updates to the primary business location create company scoped custom templates. Updates to non-primary business locations create business location scoped custom templates. The master template cannot be updated with this endpoint.&lt;/p&gt;  &lt;p&gt;The email template endpoints work a little differently than most. There are no endpoints to update the templates, we use the post endpoint to create a custom template instead. This endpoint creates a new email template that will be used instead. If you delete it, you are deleting the custom template you created and the original default template created by OnSched will be reactivated.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String id = "id_example"; // String | id of business location, defaults to primary business location
    EmailTemplateInputModel emailTemplateInputModel = new EmailTemplateInputModel(); // EmailTemplateInputModel | Input model for email template
    try {
      ContentResult result = apiInstance.setupV1LocationsIdEmailTemplatesPost(id, emailTemplateInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#setupV1LocationsIdEmailTemplatesPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| id of business location, defaults to primary business location | |
| **emailTemplateInputModel** | [**EmailTemplateInputModel**](EmailTemplateInputModel.md)| Input model for email template | [optional] |

### Return type

[**ContentResult**](ContentResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1LocationsIdEmailTemplatesTemplateNameDelete"></a>
# **setupV1LocationsIdEmailTemplatesTemplateNameDelete**
> ContentResult setupV1LocationsIdEmailTemplatesTemplateNameDelete(id, templateName)

Delete Custom Template

&lt;p&gt;Use this endpoint to &lt;b&gt;Delete&lt;/b&gt; a Custom Email Template that was previously created. A valid business &lt;b&gt;location id&lt;/b&gt; and email &lt;b&gt;templateName&lt;/b&gt; are required. Deleting a custom email template will revert the template back to its default originally created by OnSched. Changes will be reflected in all business locations associated with this company.&lt;/p&gt;  &lt;p&gt;The email template endpoints work a little differently than most. When you delete you are deleting the custom template you created, and the original default Email Template created by OnSched will be reactivated.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String id = "id_example"; // String | id of business location, defaults to primary business location
    String templateName = "templateName_example"; // String | Name of the email template
    try {
      ContentResult result = apiInstance.setupV1LocationsIdEmailTemplatesTemplateNameDelete(id, templateName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#setupV1LocationsIdEmailTemplatesTemplateNameDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| id of business location, defaults to primary business location | |
| **templateName** | **String**| Name of the email template | |

### Return type

[**ContentResult**](ContentResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1LocationsIdEmailTemplatesTemplateNameGet"></a>
# **setupV1LocationsIdEmailTemplatesTemplateNameGet**
> ContentResult setupV1LocationsIdEmailTemplatesTemplateNameGet(id, templateName)

Get Email Template

&lt;p&gt;Use this endpoint to return the requested &lt;b&gt;Email Template&lt;/b&gt;. The template is from the primary business location. If it wasn&#39;t customized the default template is returned. The response content is in html format. A valid &lt;b&gt;emailTemplate name&lt;/b&gt; is required. Find template names by using the &lt;i&gt;GET ​/setup​/v1​/locations​/{id}​/email​/templates&lt;/i&gt; endpoint. Note: The master template cannot be accessed here. &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String id = "id_example"; // String | id of business location
    String templateName = "templateName_example"; // String | name of the email template
    try {
      ContentResult result = apiInstance.setupV1LocationsIdEmailTemplatesTemplateNameGet(id, templateName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#setupV1LocationsIdEmailTemplatesTemplateNameGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| id of business location | |
| **templateName** | **String**| name of the email template | |

### Return type

[**ContentResult**](ContentResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1LocationsIdGet"></a>
# **setupV1LocationsIdGet**
> LocationViewModel setupV1LocationsIdGet(id)

Get Location

&lt;p&gt;Use this endpoint to return a &lt;b&gt;Location&lt;/b&gt; object. A valid &lt;b&gt;location id&lt;/b&gt; is required. If not specified, the business location defaults to the primary business location. Find all business location id&#39;s, by using the &lt;i&gt;GET /consumer/v1/locations&lt;/i&gt; endpoint.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;IMPORTANT DEPRECATION NOTICE&lt;/b&gt;: The following online settings parameters were intended for internal use in our Portal application only. They will be deprecated on &lt;b&gt;OCTOBER 15, 2022&lt;/b&gt;. These fields are currently part of the &lt;b&gt;SETTINGS&lt;/b&gt; object in all location endpoints: &lt;b&gt;businessId, enabled, familyMembersEnabled, serviceLabel, resourceLabel, resourceAnyLabel, resourceSelection, liveMode, formFlow, availabilityForm, showServiceGroups, showOnSchedLogo, showBusinessLogo, disableAuthorization, hideNavBar, hideLocationNav, hideServiceGroupsNav, hideServicesNav, hideContinueBooking, returnToService, returnToAvailability, hideBreadCrumbNav.&lt;/b&gt; If you are using these fields, please adjust your code to handle the deprecation or let us know by submitting a ticket to: &lt;b&gt;&lt;i&gt;support@onsched.com&lt;/i&gt;&lt;/b&gt; as we do not want to interrupt your existing workflows.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String id = "id_example"; // String | id of business location, defaults to primary business location
    try {
      LocationViewModel result = apiInstance.setupV1LocationsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#setupV1LocationsIdGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| id of business location, defaults to primary business location | |

### Return type

[**LocationViewModel**](LocationViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1LocationsIdGoogleServiceAccountDelete"></a>
# **setupV1LocationsIdGoogleServiceAccountDelete**
> setupV1LocationsIdGoogleServiceAccountDelete(id)

Delete Google Cal Access

&lt;p&gt;Use this endpoint to &lt;b&gt;Delete&lt;/b&gt; authorized access to all google calendar users in your organization. Upon deletion Google Calendars will no longer be synced for resources.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String id = "id_example"; // String | id of business location, defaults to primary business location
    try {
      apiInstance.setupV1LocationsIdGoogleServiceAccountDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#setupV1LocationsIdGoogleServiceAccountDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| id of business location, defaults to primary business location | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1LocationsIdGoogleServiceAccountPost"></a>
# **setupV1LocationsIdGoogleServiceAccountPost**
> GoogleServiceAccountCreds setupV1LocationsIdGoogleServiceAccountPost(id, googleServiceAccountCreds)

Create Google Cal Access

&lt;p&gt;Use this endpoint to &lt;b&gt;Authorize Access&lt;/b&gt; to google calendar users in your organization. You must create/have a Google Service account as an admin of your GSuite, then save the credentials as a Json Key file. This &lt;b&gt;Json Key&lt;/b&gt; and a valid business &lt;b&gt;location id&lt;/b&gt; are required. &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String id = "id_example"; // String | id of business location, defaults to primary business location
    GoogleServiceAccountCreds googleServiceAccountCreds = new GoogleServiceAccountCreds(); // GoogleServiceAccountCreds | Generated Json Key file from Google
    try {
      GoogleServiceAccountCreds result = apiInstance.setupV1LocationsIdGoogleServiceAccountPost(id, googleServiceAccountCreds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#setupV1LocationsIdGoogleServiceAccountPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| id of business location, defaults to primary business location | |
| **googleServiceAccountCreds** | [**GoogleServiceAccountCreds**](GoogleServiceAccountCreds.md)| Generated Json Key file from Google | [optional] |

### Return type

[**GoogleServiceAccountCreds**](GoogleServiceAccountCreds.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1LocationsIdHolidaysHolidayIdClosedPut"></a>
# **setupV1LocationsIdHolidaysHolidayIdClosedPut**
> LocationViewModel setupV1LocationsIdHolidaysHolidayIdClosedPut(id, holidayId, closed)

Update Location Holidays

&lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; Business Holidays as Opened or Closed. A valid business &lt;b&gt;location id&lt;/b&gt; is required. If not specified, the business location defaults to the primary business location.&lt;/p&gt;  &lt;p&gt;Holidays are automatically defined with the initial Post Location endpoint and are based on country code. Find your location holiday codes by using the: &lt;i&gt;GET /setup​/v1​/locations​/{id}&lt;/i&gt; endpoint. Change your holidays to open or closed by passing in the &lt;b&gt;holidayId&lt;/b&gt; along with the &lt;b&gt;closed&lt;/b&gt; boolean value to change the status of a specific holiday. Pass in an &lt;b&gt;asterisk *&lt;/b&gt; for the holidayId then all business holidays will be set as defined.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String id = "id_example"; // String | 
    String holidayId = "holidayId_example"; // String | 
    Boolean closed = true; // Boolean | 
    try {
      LocationViewModel result = apiInstance.setupV1LocationsIdHolidaysHolidayIdClosedPut(id, holidayId, closed);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#setupV1LocationsIdHolidaysHolidayIdClosedPut");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **holidayId** | **String**|  | |
| **closed** | **Boolean**|  | |

### Return type

[**LocationViewModel**](LocationViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1LocationsIdPut"></a>
# **setupV1LocationsIdPut**
> LocationViewModel setupV1LocationsIdPut(id, removeRegion, locationUpdateModel)

Update Location

&lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; a business location object. A valid business &lt;b&gt;location id&lt;/b&gt; is required. The optional removeRegion query parameter can be used to remove the region relationship from the location.&lt;/p&gt;  &lt;p&gt;If the settings element is populated the scope will be set to the business location with the settings supplied. If your settings are uniform across all locations, then do not supply the settings element and the location will use the settings defined on the primary business location (company scoped). Company scoped settings cascade down to the locations. You can override any location that needs different settings by providing settings in the update model. Use the &lt;i&gt;PUT /setup/v1/locations/{id}/settings/scope/{settingsScope}&lt;/i&gt; endpoint to change the settings scope only. This is typically used when switching from business location scope back to company.&lt;/p&gt;  &lt;p&gt;Refer to: &lt;i&gt;&lt;b&gt;POST ​/setup​/v1​/locations&lt;/b&gt;&lt;/i&gt; endpoint for details.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String id = "id_example"; // String | 
    Boolean removeRegion = true; // Boolean | 
    LocationUpdateModel locationUpdateModel = new LocationUpdateModel(); // LocationUpdateModel | 
    try {
      LocationViewModel result = apiInstance.setupV1LocationsIdPut(id, removeRegion, locationUpdateModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#setupV1LocationsIdPut");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **removeRegion** | **Boolean**|  | [optional] |
| **locationUpdateModel** | [**LocationUpdateModel**](LocationUpdateModel.md)|  | [optional] |

### Return type

[**LocationViewModel**](LocationViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1LocationsIdRecoverPut"></a>
# **setupV1LocationsIdRecoverPut**
> LocationViewModel setupV1LocationsIdRecoverPut(id)

Recover Location

&lt;p&gt;Use this endpoint to &lt;b&gt;Recover&lt;/b&gt; a deleted business location. A valid business &lt;b&gt;location id&lt;/b&gt; is required.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      LocationViewModel result = apiInstance.setupV1LocationsIdRecoverPut(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#setupV1LocationsIdRecoverPut");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |

### Return type

[**LocationViewModel**](LocationViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1LocationsIdServicesDelete"></a>
# **setupV1LocationsIdServicesDelete**
> LocationViewModel setupV1LocationsIdServicesDelete(id)

Delete Linked Services

&lt;p&gt;Use this endpoint to &lt;b&gt;Delete All&lt;/b&gt; location linked services from a business location. A valid business &lt;b&gt;location id&lt;/b&gt; is required. &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String id = "id_example"; // String | id of business location, defaults to primary business location
    try {
      LocationViewModel result = apiInstance.setupV1LocationsIdServicesDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#setupV1LocationsIdServicesDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| id of business location, defaults to primary business location | |

### Return type

[**LocationViewModel**](LocationViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1LocationsIdServicesGet"></a>
# **setupV1LocationsIdServicesGet**
> BusinessServiceListViewModel setupV1LocationsIdServicesGet(id, offset, limit)

List Location Linked Services

&lt;p&gt;Use this endpoint to return a list of &lt;b&gt;Location Linked Services&lt;/b&gt;. A valid business &lt;b&gt;location id&lt;/b&gt; is required. By default, there are no location linked services attached to a location. Refer to the: &lt;i&gt;POST /setup​/v1​/locations​/{id}​/services&lt;/i&gt; for details. The results are returned in pages. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String id = "id_example"; // String | id of business location, defaults to primary business location
    Integer offset = 56; // Integer | Starting row of page, default 0
    Integer limit = 56; // Integer | Page limit default 20, max 100
    try {
      BusinessServiceListViewModel result = apiInstance.setupV1LocationsIdServicesGet(id, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#setupV1LocationsIdServicesGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| id of business location, defaults to primary business location | |
| **offset** | **Integer**| Starting row of page, default 0 | [optional] |
| **limit** | **Integer**| Page limit default 20, max 100 | [optional] |

### Return type

[**BusinessServiceListViewModel**](BusinessServiceListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | location service objects |  -  |
| **400** | Missing or invalid values in the request |  -  |
| **401** | Authorization error |  -  |
| **404** | Location was not found |  -  |

<a id="setupV1LocationsIdServicesPost"></a>
# **setupV1LocationsIdServicesPost**
> LocationViewModel setupV1LocationsIdServicesPost(id, requestBody)

Create Linked Service

&lt;p&gt;Use this endpoint to &lt;b&gt;Link Services&lt;/b&gt; to a location object. A valid business &lt;b&gt;location id&lt;/b&gt; is required. By default, there are &lt;i&gt;no services linked&lt;/i&gt; to a location. &lt;/p&gt;  &lt;p&gt;Services are definable globally at the Company level and associated with the Primary Business Location, or at a Secondary Business Location. When accessing the Services endpoints, by default, API consumers are provided with a &lt;b&gt;combined&lt;/b&gt; list of Services defined from both the Primary and Secondary Business Location.&lt;/p&gt;  &lt;p&gt;If necessary, the list of Service(s) provided can be cherry-picked/linked to &lt;b&gt;only include specific Service(s)&lt;/b&gt; by using this endpoint. This allows for a subset of defined Services to be provided for a location.&lt;/p&gt;  &lt;p&gt;Supplying the list of services ids to cherry-pick/link to the location in the request body will explicitly define which Primary Location Services are offered by the specified business location.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String id = "id_example"; // String | id of business location, defaults to primary business location
    List<String> requestBody = Arrays.asList(); // List<String> | array of valid service object id's
    try {
      LocationViewModel result = apiInstance.setupV1LocationsIdServicesPost(id, requestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#setupV1LocationsIdServicesPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| id of business location, defaults to primary business location | |
| **requestBody** | [**List&lt;String&gt;**](String.md)| array of valid service object id&#39;s | [optional] |

### Return type

[**LocationViewModel**](LocationViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1LocationsIdSettingsScopeSettingsScopePut"></a>
# **setupV1LocationsIdSettingsScopeSettingsScopePut**
> LocationViewModel setupV1LocationsIdSettingsScopeSettingsScopePut(id, settingsScope)

Update Location Scope

&lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; a business locations online booking settings scope. A valid business &lt;b&gt;location id&lt;/b&gt; is required.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;settingsScope&lt;/b&gt; values are &lt;b&gt;0 &#x3D; company scope, 1 &#x3D; business location scope&lt;/b&gt;. To inherit the online settings defined in the primary business location, then use value &#x3D; 0 for company scope. Otherwise, to override the settings for a specific location then use value &#x3D; 1 for business location scope. &lt;b&gt;Note&lt;/b&gt;: You cannot change the settings scope of the Primary Business Location.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String id = "id_example"; // String | 
    String settingsScope = "settingsScope_example"; // String | 
    try {
      LocationViewModel result = apiInstance.setupV1LocationsIdSettingsScopeSettingsScopePut(id, settingsScope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#setupV1LocationsIdSettingsScopeSettingsScopePut");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **settingsScope** | **String**|  | |

### Return type

[**LocationViewModel**](LocationViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1LocationsIdUploadimagePost"></a>
# **setupV1LocationsIdUploadimagePost**
> LocationViewModel setupV1LocationsIdUploadimagePost(id, resourceImageInputModel)

Upload Location Image

&lt;p&gt;Use this endpoint to &lt;b&gt;Upload&lt;/b&gt; an image to a location object. A valid business &lt;b&gt;location id&lt;/b&gt; is required. You must convert the image to a &lt;b&gt;base64 encoded string&lt;/b&gt; and pass that string as input along with your &lt;b&gt;filename&lt;/b&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String id = "id_example"; // String | id of business location, defaults to primary business location
    ResourceImageInputModel resourceImageInputModel = new ResourceImageInputModel(); // ResourceImageInputModel | Input model for image upload
    try {
      LocationViewModel result = apiInstance.setupV1LocationsIdUploadimagePost(id, resourceImageInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#setupV1LocationsIdUploadimagePost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| id of business location, defaults to primary business location | |
| **resourceImageInputModel** | [**ResourceImageInputModel**](ResourceImageInputModel.md)| Input model for image upload | [optional] |

### Return type

[**LocationViewModel**](LocationViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1LocationsPost"></a>
# **setupV1LocationsPost**
> LocationViewModel setupV1LocationsPost(locationInputModel)

Create Location

&lt;p&gt;Use this endpoint to &lt;b&gt;Create&lt;/b&gt; a new business location. The result is a business location object with a GUID assigned to the location.&lt;/p&gt;  &lt;p&gt;The &lt;b&gt;name&lt;/b&gt; and &lt;b&gt;timezoneName&lt;/b&gt; fields are required. The &lt;b&gt;timezoneName&lt;/b&gt; must be expressed as an IANA Timezone e.g., &lt;i&gt;America/New_York&lt;/i&gt;. Refer to: &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/List_of_tz_database_time_zones\&quot;&gt;Timezone Wiki&lt;/a&gt; for a listing of IANA time zones.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Business hours&lt;/b&gt; are set by defining the &lt;b&gt;startTime&lt;/b&gt; and &lt;b&gt;endTime&lt;/b&gt; values for each day available/open. All days of the week must be provided when setting availability. Days are defined as &lt;b&gt;sun, mon, tue, wed, thu, fri and sat&lt;/b&gt;. Start and End Times are entered in &lt;b&gt;military format. e.g., 800 is 8:00am, 2230 is 10:30pm&lt;/b&gt;. If there is no physical location and the business hours are irrelevant, set the hours to open 24 hours by setting startTime&#x3D;0 and endTime&#x3D;2400. To set a whole day as unavailable, set both the startTime and endTime to 0. &lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Settings&lt;/b&gt; can be set here. Booking timer minutes, book ahead restrictions and customer bookings per day are all available here. Please read about the settings scope parameter before setting these values as it may simplify your process.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Settings Scope&lt;/b&gt; can be set to the company or the business location level. You can have all locations use the same company level settings or individual business locations can define their own, business location scope. If you want to use the company settings throughout all locations, do not pass in &lt;b&gt;settings element&lt;/b&gt;. To create business location scoped settings, pass in the &lt;b&gt;settings element&lt;/b&gt; with the field values defined in the post body. &lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Appointment Reminders&lt;/b&gt; Reminder values are used to define how many hours, days, or weeks (interval value) prior to the appointment to send the reminder. &lt;b&gt;Interval&lt;/b&gt; values are used to define the reminder interval: &lt;b&gt;1 &#x3D; Hours&lt;/b&gt;, &lt;b&gt;2 &#x3D; Days&lt;/b&gt; and &lt;b&gt;3 &#x3D; Weeks&lt;/b&gt;. The reminder fields are numbers. If you are using the hours interval, use a number from 1 to 24.&lt;/p&gt;  &lt;p&gt;Example 1: &lt;b&gt;emailFirstReminder:  1, emailFirstReminderInterval:  2&lt;/b&gt; - results in 1st reminder being sent &lt;b&gt;1 Day before&lt;/b&gt; the appointment time.&lt;/p&gt;  &lt;p&gt;Example 2: &lt;b&gt;emailSecondReminder: 3, emailSecondReminderInterval: 1&lt;/b&gt; - results in 2nd reminder being sent &lt;b&gt;3 Hours before&lt;/b&gt; the appointment time.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;IMPORTANT DEPRECATION NOTICE&lt;/b&gt;: The following online settings parameters were intended for internal use in our Portal application only. They will be deprecated on &lt;b&gt;OCTOBER 15, 2022&lt;/b&gt;. These fields are currently part of the &lt;b&gt;SETTINGS&lt;/b&gt; object in all location endpoints: &lt;b&gt;businessId, enabled, familyMembersEnabled, serviceLabel, resourceLabel, resourceAnyLabel, resourceSelection, liveMode, formFlow, availabilityForm, showServiceGroups, showOnSchedLogo, showBusinessLogo, disableAuthorization, hideNavBar, hideLocationNav, hideServiceGroupsNav, hideServicesNav, hideContinueBooking, returnToService, returnToAvailability, hideBreadCrumbNav.&lt;/b&gt; If you are using these fields, please adjust your code to handle the deprecation or let us know by submitting a ticket to: &lt;b&gt;&lt;i&gt;support@onsched.com&lt;/i&gt;&lt;/b&gt; as we do not want to interrupt your existing workflows.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    LocationInputModel locationInputModel = new LocationInputModel(); // LocationInputModel | 
    try {
      LocationViewModel result = apiInstance.setupV1LocationsPost(locationInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#setupV1LocationsPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **locationInputModel** | [**LocationInputModel**](LocationInputModel.md)|  | [optional] |

### Return type

[**LocationViewModel**](LocationViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1LocationsServicesIdDelete"></a>
# **setupV1LocationsServicesIdDelete**
> LocationViewModel setupV1LocationsServicesIdDelete(id)

Unlink Service

&lt;p&gt;Use this endpoint to &lt;b&gt;Unlink&lt;/b&gt; a location service from a business location. A valid &lt;b&gt;locationService id&lt;/b&gt; is required. Find location services by using the &lt;i&gt;GET ​/setup​/v1​/locations​/{id}​/services&lt;/i&gt; endpoint. &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String id = "id_example"; // String | id of locationService object
    try {
      LocationViewModel result = apiInstance.setupV1LocationsServicesIdDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#setupV1LocationsServicesIdDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| id of locationService object | |

### Return type

[**LocationViewModel**](LocationViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1LocationsServicesIdGet"></a>
# **setupV1LocationsServicesIdGet**
> BusinessServiceViewModel setupV1LocationsServicesIdGet(id)

Get Linked Service

&lt;p&gt;Use this endpoint to &lt;b&gt;Get a Linked Service&lt;/b&gt;. A valid &lt;b&gt;locationService id&lt;/b&gt; is required.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String id = "id_example"; // String | id of locationService object
    try {
      BusinessServiceViewModel result = apiInstance.setupV1LocationsServicesIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#setupV1LocationsServicesIdGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| id of locationService object | |

### Return type

[**BusinessServiceViewModel**](BusinessServiceViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | location service objects |  -  |
| **400** | Missing or invalid values in the request |  -  |
| **401** | Authorization error. |  -  |
| **404** | Location was not found |  -  |

