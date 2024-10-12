# AppointmentsApi

All URIs are relative to *https://sandbox-api.onsched.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**setupV1AppointmentsGet**](AppointmentsApi.md#setupV1AppointmentsGet) | **GET** /setup/v1/appointments | List Appointments |
| [**setupV1AppointmentsIdGet**](AppointmentsApi.md#setupV1AppointmentsIdGet) | **GET** /setup/v1/appointments/{id} | Get Appointment |
| [**setupV1AppointmentsIdReassignResourceResourceIdPut**](AppointmentsApi.md#setupV1AppointmentsIdReassignResourceResourceIdPut) | **PUT** /setup/v1/appointments/{id}/reassign/resource/{resourceId} | Reassign Appointment |


<a id="setupV1AppointmentsGet"></a>
# **setupV1AppointmentsGet**
> AppointmentListViewModel setupV1AppointmentsGet(locationId, email, lastname, serviceId, calendarId, resourceId, customerId, serviceAllocationId, startDate, endDate, status, bookedBy, offset, limit)

List Appointments

&lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Appointments&lt;/b&gt;. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further. For more information: &lt;a href&#x3D;\&quot;https://onsched.readme.io/docs/appointments-overview\&quot;&gt;Appointments Overview&lt;/a&gt;&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppointmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AppointmentsApi apiInstance = new AppointmentsApi(defaultClient);
    String locationId = "locationId_example"; // String | id of business location, defaults to primary business location
    String email = "email_example"; // String | Filter appointments by email address
    String lastname = "lastname_example"; // String | Filter appointments by lastname or part of
    String serviceId = "serviceId_example"; // String | Filter appointments by service
    String calendarId = "calendarId_example"; // String | Filter appointments by calendar
    String resourceId = "resourceId_example"; // String | Filter appointments by resource
    String customerId = "customerId_example"; // String | Filter appointments by customer
    String serviceAllocationId = "serviceAllocationId_example"; // String | Filter appointments by service allocation
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | Format YYYY-MM-DD: Filter appointments by on/after startDate
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | Format YYYY-MM-DD: Filter appointments on/before endDate
    String status = "status_example"; // String | Filter appointments by status: IN, BK, CN, RE, RS
    String bookedBy = "bookedBy_example"; // String | Filter appointments by user email who booked
    Integer offset = 56; // Integer | Starting row of page, default 0
    Integer limit = 56; // Integer | Page limit default 20, max 100
    try {
      AppointmentListViewModel result = apiInstance.setupV1AppointmentsGet(locationId, email, lastname, serviceId, calendarId, resourceId, customerId, serviceAllocationId, startDate, endDate, status, bookedBy, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppointmentsApi#setupV1AppointmentsGet");
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
| **locationId** | **String**| id of business location, defaults to primary business location | [optional] |
| **email** | **String**| Filter appointments by email address | [optional] |
| **lastname** | **String**| Filter appointments by lastname or part of | [optional] |
| **serviceId** | **String**| Filter appointments by service | [optional] |
| **calendarId** | **String**| Filter appointments by calendar | [optional] |
| **resourceId** | **String**| Filter appointments by resource | [optional] |
| **customerId** | **String**| Filter appointments by customer | [optional] |
| **serviceAllocationId** | **String**| Filter appointments by service allocation | [optional] |
| **startDate** | **OffsetDateTime**| Format YYYY-MM-DD: Filter appointments by on/after startDate | [optional] |
| **endDate** | **OffsetDateTime**| Format YYYY-MM-DD: Filter appointments on/before endDate | [optional] |
| **status** | **String**| Filter appointments by status: IN, BK, CN, RE, RS | [optional] |
| **bookedBy** | **String**| Filter appointments by user email who booked | [optional] |
| **offset** | **Integer**| Starting row of page, default 0 | [optional] |
| **limit** | **Integer**| Page limit default 20, max 100 | [optional] |

### Return type

[**AppointmentListViewModel**](AppointmentListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1AppointmentsIdGet"></a>
# **setupV1AppointmentsIdGet**
> AppointmentViewModel setupV1AppointmentsIdGet(id)

Get Appointment

&lt;p&gt;Use this endpoint to return an &lt;b&gt;Appointment&lt;/b&gt; object. A valid &lt;b&gt;appointment id&lt;/b&gt; is required. Find appointment id&#39;s by using the &lt;i&gt;GET​/setup​/v1​/appointments&lt;/i&gt; endpoint.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppointmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AppointmentsApi apiInstance = new AppointmentsApi(defaultClient);
    String id = "id_example"; // String | id of appointment object
    try {
      AppointmentViewModel result = apiInstance.setupV1AppointmentsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppointmentsApi#setupV1AppointmentsIdGet");
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
| **id** | **String**| id of appointment object | |

### Return type

[**AppointmentViewModel**](AppointmentViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1AppointmentsIdReassignResourceResourceIdPut"></a>
# **setupV1AppointmentsIdReassignResourceResourceIdPut**
> AppointmentViewModel setupV1AppointmentsIdReassignResourceResourceIdPut(id, resourceId)

Reassign Appointment

&lt;p&gt;Use this endpoint to &lt;b&gt;Reassign&lt;/b&gt; an appointment from one resource to another. The result returned is a single appointment that was reassigned to the target resource. A valid &lt;b&gt;appointment id&lt;/b&gt; and &lt;b&gt;resource id&lt;/b&gt; is required. Find appointment id&#39;s by using the &lt;i&gt;GET /setup/v1/appointments&lt;/i&gt; endpoint, find resource id&#39;s by using the &lt;i&gt;GET ​/setup​/v1​/resources&lt;/i&gt; endpoint.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppointmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AppointmentsApi apiInstance = new AppointmentsApi(defaultClient);
    String id = "id_example"; // String | id of appointment object
    String resourceId = "resourceId_example"; // String | id of target resource
    try {
      AppointmentViewModel result = apiInstance.setupV1AppointmentsIdReassignResourceResourceIdPut(id, resourceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppointmentsApi#setupV1AppointmentsIdReassignResourceResourceIdPut");
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
| **id** | **String**| id of appointment object | |
| **resourceId** | **String**| id of target resource | |

### Return type

[**AppointmentViewModel**](AppointmentViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

