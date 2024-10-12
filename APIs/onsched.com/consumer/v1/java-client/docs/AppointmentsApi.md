# AppointmentsApi

All URIs are relative to *https://sandbox-api.onsched.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**consumerV1AppointmentsBookingfieldsGet**](AppointmentsApi.md#consumerV1AppointmentsBookingfieldsGet) | **GET** /consumer/v1/appointments/bookingfields | Get Custom Fields Labels |
| [**consumerV1AppointmentsCustomfieldsGet**](AppointmentsApi.md#consumerV1AppointmentsCustomfieldsGet) | **GET** /consumer/v1/appointments/customfields | Get Custom Fields List |
| [**consumerV1AppointmentsGet**](AppointmentsApi.md#consumerV1AppointmentsGet) | **GET** /consumer/v1/appointments | Get Appointments |
| [**consumerV1AppointmentsIdBookPut**](AppointmentsApi.md#consumerV1AppointmentsIdBookPut) | **PUT** /consumer/v1/appointments/{id}/book | Book Appointment |
| [**consumerV1AppointmentsIdCancelPut**](AppointmentsApi.md#consumerV1AppointmentsIdCancelPut) | **PUT** /consumer/v1/appointments/{id}/cancel | Cancel Appointment |
| [**consumerV1AppointmentsIdConfirmPut**](AppointmentsApi.md#consumerV1AppointmentsIdConfirmPut) | **PUT** /consumer/v1/appointments/{id}/confirm | Confirm Appointment |
| [**consumerV1AppointmentsIdDelete**](AppointmentsApi.md#consumerV1AppointmentsIdDelete) | **DELETE** /consumer/v1/appointments/{id} | Delete Appointment |
| [**consumerV1AppointmentsIdGet**](AppointmentsApi.md#consumerV1AppointmentsIdGet) | **GET** /consumer/v1/appointments/{id} | Get Appointment |
| [**consumerV1AppointmentsIdNoshowPut**](AppointmentsApi.md#consumerV1AppointmentsIdNoshowPut) | **PUT** /consumer/v1/appointments/{id}/noshow | Set NoShow Status |
| [**consumerV1AppointmentsIdReschedulePut**](AppointmentsApi.md#consumerV1AppointmentsIdReschedulePut) | **PUT** /consumer/v1/appointments/{id}/reschedule | Reschedule Appointment |
| [**consumerV1AppointmentsIdReservePut**](AppointmentsApi.md#consumerV1AppointmentsIdReservePut) | **PUT** /consumer/v1/appointments/{id}/reserve | Reserve Appointment |
| [**consumerV1AppointmentsPost**](AppointmentsApi.md#consumerV1AppointmentsPost) | **POST** /consumer/v1/appointments | Create Appointment |


<a id="consumerV1AppointmentsBookingfieldsGet"></a>
# **consumerV1AppointmentsBookingfieldsGet**
> BookingFieldListViewModel consumerV1AppointmentsBookingfieldsGet(locationId)

Get Custom Fields Labels

&lt;p&gt;Use this endpoint to return a locations &lt;b&gt;Appointment Booking Fields&lt;/b&gt;. Appointment booking fields are stored with each Appointment record. They are used when you need additional information collected during your booking process. It is tied to an appointment/visit and will be stored in the appointment record. Use the field name, type, and length to determine how to update these field values when posting an appointment.&lt;/p&gt;

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
    String locationId = "locationId_example"; // String | id of business location
    try {
      BookingFieldListViewModel result = apiInstance.consumerV1AppointmentsBookingfieldsGet(locationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppointmentsApi#consumerV1AppointmentsBookingfieldsGet");
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
| **locationId** | **String**| id of business location | [optional] |

### Return type

[**BookingFieldListViewModel**](BookingFieldListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="consumerV1AppointmentsCustomfieldsGet"></a>
# **consumerV1AppointmentsCustomfieldsGet**
> CustomFieldDefinitionListViewModel consumerV1AppointmentsCustomfieldsGet(locationId)

Get Custom Fields List

&lt;p&gt;Use this endpoint to return a locations &lt;b&gt;Appointment Custom Field&lt;/b&gt; definitions. Appointment custom fields are stored with each appointment. They are used when the information collected during the booking is specific to a particular appointment/visit. The response will list the custom fields used (customField1 - 10), the field type (string, number, date, boolean) and the length of each one.&lt;/p&gt;

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
    String locationId = "locationId_example"; // String | id of business location
    try {
      CustomFieldDefinitionListViewModel result = apiInstance.consumerV1AppointmentsCustomfieldsGet(locationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppointmentsApi#consumerV1AppointmentsCustomfieldsGet");
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
| **locationId** | **String**| id of business location | [optional] |

### Return type

[**CustomFieldDefinitionListViewModel**](CustomFieldDefinitionListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="consumerV1AppointmentsGet"></a>
# **consumerV1AppointmentsGet**
> AppointmentListViewModel consumerV1AppointmentsGet(locationId, email, lastname, phone, serviceId, calendarId, resourceId, customerId, serviceAllocationId, startDate, endDate, status, bookedBy, offset, limit)

Get Appointments

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
    String locationId = "locationId_example"; // String | id of business location
    String email = "email_example"; // String | Filter by email address
    String lastname = "lastname_example"; // String | Filter by lastname or part of it
    String phone = "phone_example"; // String | Filter by phone number or part of it
    String serviceId = "serviceId_example"; // String | Filter by service
    String calendarId = "calendarId_example"; // String | Filter by calendar
    String resourceId = "resourceId_example"; // String | Filter by resource
    String customerId = "customerId_example"; // String | Filter by customer
    String serviceAllocationId = "serviceAllocationId_example"; // String | Filter by service allocation
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | Format YYYY-MM-DD. Filter by on/after startDate
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | Format YYYY-MM-DD. Filter on/before endDate
    String status = "status_example"; // String | Filter by status: IN, BK, CN, RE, RS
    String bookedBy = "bookedBy_example"; // String | Filter by the email of who booked
    Integer offset = 56; // Integer | Starting row of page, default 0
    Integer limit = 56; // Integer | Page limit, default 20, max 100
    try {
      AppointmentListViewModel result = apiInstance.consumerV1AppointmentsGet(locationId, email, lastname, phone, serviceId, calendarId, resourceId, customerId, serviceAllocationId, startDate, endDate, status, bookedBy, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppointmentsApi#consumerV1AppointmentsGet");
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
| **locationId** | **String**| id of business location | [optional] |
| **email** | **String**| Filter by email address | [optional] |
| **lastname** | **String**| Filter by lastname or part of it | [optional] |
| **phone** | **String**| Filter by phone number or part of it | [optional] |
| **serviceId** | **String**| Filter by service | [optional] |
| **calendarId** | **String**| Filter by calendar | [optional] |
| **resourceId** | **String**| Filter by resource | [optional] |
| **customerId** | **String**| Filter by customer | [optional] |
| **serviceAllocationId** | **String**| Filter by service allocation | [optional] |
| **startDate** | **OffsetDateTime**| Format YYYY-MM-DD. Filter by on/after startDate | [optional] |
| **endDate** | **OffsetDateTime**| Format YYYY-MM-DD. Filter on/before endDate | [optional] |
| **status** | **String**| Filter by status: IN, BK, CN, RE, RS | [optional] |
| **bookedBy** | **String**| Filter by the email of who booked | [optional] |
| **offset** | **Integer**| Starting row of page, default 0 | [optional] |
| **limit** | **Integer**| Page limit, default 20, max 100 | [optional] |

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

<a id="consumerV1AppointmentsIdBookPut"></a>
# **consumerV1AppointmentsIdBookPut**
> AppointmentViewModel consumerV1AppointmentsIdBookPut(id, appointmentBookModel)

Book Appointment

&lt;p&gt;Use this endpoint to &lt;b&gt;Book&lt;/b&gt; an appointment. Only appointments with an \&quot;IN\&quot; status, Initial, can be booked. A valid &lt;b&gt;appointment id&lt;/b&gt; is required. Use the appointment id returned from the initial &lt;i&gt;POST /consumer/v1/appointments&lt;/i&gt; endpoint. Other pertinent fields can also be updated at the time of booking by including them in the post body. &lt;b&gt;Note: If no name or email address was provided in the initial Post Appointment, it will be required in the post body.&lt;/b&gt;&lt;/p&gt;  &lt;p&gt;For more information: &lt;a href&#x3D;\&quot;https://onsched.readme.io/docs/appointments-overview\&quot;&gt;Appointments Overview&lt;/a&gt;&lt;/p&gt;

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
    String id = "id_example"; // String | appointment id to book
    AppointmentBookModel appointmentBookModel = new AppointmentBookModel(); // AppointmentBookModel | 
    try {
      AppointmentViewModel result = apiInstance.consumerV1AppointmentsIdBookPut(id, appointmentBookModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppointmentsApi#consumerV1AppointmentsIdBookPut");
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
| **id** | **String**| appointment id to book | |
| **appointmentBookModel** | [**AppointmentBookModel**](AppointmentBookModel.md)|  | [optional] |

### Return type

[**AppointmentViewModel**](AppointmentViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="consumerV1AppointmentsIdCancelPut"></a>
# **consumerV1AppointmentsIdCancelPut**
> AppointmentViewModel consumerV1AppointmentsIdCancelPut(id)

Cancel Appointment

&lt;p&gt;Use this endpoint to &lt;b&gt;Cancel&lt;/b&gt; an appointment booking or reservation. Only appointments with a \&quot;BK\&quot;, booked or \&quot;RS\&quot;, reserved status can be cancelled. Past dated appointments cannot be cancelled. A valid &lt;b&gt;appointment id&lt;/b&gt; is required. For more information: &lt;a href&#x3D;\&quot;https://onsched.readme.io/docs/appointments-overview\&quot;&gt;Appointment Overview&lt;/a&gt;&lt;/p&gt;

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
    String id = "id_example"; // String | appointment id to cancel
    try {
      AppointmentViewModel result = apiInstance.consumerV1AppointmentsIdCancelPut(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppointmentsApi#consumerV1AppointmentsIdCancelPut");
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
| **id** | **String**| appointment id to cancel | |

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

<a id="consumerV1AppointmentsIdConfirmPut"></a>
# **consumerV1AppointmentsIdConfirmPut**
> consumerV1AppointmentsIdConfirmPut(id, undo)

Confirm Appointment

&lt;p&gt;Use this endpoint to &lt;b&gt;Confirm&lt;/b&gt; an appointment. This updates the boolean confirmed field to TRUE. &lt;b&gt;NOTE:&lt;/b&gt; If the appointment status is set to \&quot;RS\&quot;, Reserved, it also updates the status of the appointment to \&quot;BK\&quot;, Booked. &lt;/p&gt;  &lt;p&gt;For more information: &lt;a href&#x3D;\&quot;https://onsched.readme.io/docs/appointments-overview\&quot;&gt;Appointment Overview&lt;/a&gt;&lt;/p&gt;

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
    Integer id = 56; // Integer | appointment id to confirm
    Boolean undo = true; // Boolean | Use this parameter to undo the confirmed status
    try {
      apiInstance.consumerV1AppointmentsIdConfirmPut(id, undo);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppointmentsApi#consumerV1AppointmentsIdConfirmPut");
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
| **id** | **Integer**| appointment id to confirm | |
| **undo** | **Boolean**| Use this parameter to undo the confirmed status | [optional] |

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

<a id="consumerV1AppointmentsIdDelete"></a>
# **consumerV1AppointmentsIdDelete**
> AppointmentViewModel consumerV1AppointmentsIdDelete(id)

Delete Appointment

&lt;p&gt;Use this endpoint to permanently &lt;b&gt;Delete&lt;/b&gt; an appointment. Only appointments with a of \&quot;IN\&quot; status, initial, can be deleted. Past dated appointments cannot be deleted. A valid &lt;b&gt;appointment id&lt;/b&gt; is required. Use the appointment id returned from the initial &lt;i&gt;POST /consumer/v1/appointments&lt;/i&gt; endpoint.&lt;/p&gt;  &lt;p&gt;For more information: &lt;a href&#x3D;\&quot;https://onsched.readme.io/docs/appointments-overview\&quot;&gt;Appointment Overview&lt;/a&gt;&lt;/p&gt;

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
    String id = "id_example"; // String | appointment id to delete
    try {
      AppointmentViewModel result = apiInstance.consumerV1AppointmentsIdDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppointmentsApi#consumerV1AppointmentsIdDelete");
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
| **id** | **String**| appointment id to delete | |

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

<a id="consumerV1AppointmentsIdGet"></a>
# **consumerV1AppointmentsIdGet**
> AppointmentViewModel consumerV1AppointmentsIdGet(id)

Get Appointment

&lt;p&gt;Use this endpoint to return an &lt;b&gt;Appointment&lt;/b&gt; object. A valid &lt;b&gt;appointment id&lt;/b&gt; is required. For more information: &lt;a href&#x3D;\&quot;https://onsched.readme.io/docs/appointments-overview\&quot;&gt;Appointments Overview&lt;/a&gt;&lt;/p&gt;

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
    String id = "id_example"; // String | id of appointment requested
    try {
      AppointmentViewModel result = apiInstance.consumerV1AppointmentsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppointmentsApi#consumerV1AppointmentsIdGet");
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
| **id** | **String**| id of appointment requested | |

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

<a id="consumerV1AppointmentsIdNoshowPut"></a>
# **consumerV1AppointmentsIdNoshowPut**
> consumerV1AppointmentsIdNoshowPut(id, body)

Set NoShow Status

&lt;p&gt;Use this endpoint to change the status of an appointment from \&quot;BK\&quot;, Booked to &lt;b&gt;\&quot;NS\&quot;, NoShow&lt;/b&gt;. This gives API consumers a way to internally track No Show appointments. It provides no added functionality in OnSched.&lt;/p&gt;  &lt;p&gt;For more information: &lt;a href&#x3D;\&quot;https://onsched.readme.io/docs/appointments-overview\&quot;&gt;Appointment Overview&lt;/a&gt;&lt;/p&gt;

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
    Integer id = 56; // Integer | appointment id to mark as NoShow
    Object body = null; // Object | 
    try {
      apiInstance.consumerV1AppointmentsIdNoshowPut(id, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppointmentsApi#consumerV1AppointmentsIdNoshowPut");
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
| **id** | **Integer**| appointment id to mark as NoShow | |
| **body** | **Object**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="consumerV1AppointmentsIdReschedulePut"></a>
# **consumerV1AppointmentsIdReschedulePut**
> AppointmentViewModel consumerV1AppointmentsIdReschedulePut(id, appointmentRescheduleModel)

Reschedule Appointment

&lt;p&gt;Use this endpoint to &lt;b&gt;Reschedule&lt;/b&gt; an appointment booking. Only appointments in \&quot;BK\&quot;, booked status, can be Rescheduled. Past dated appointments cannot be rescheduled. A valid &lt;b&gt;appointment id&lt;/b&gt; is required.&lt;/p&gt;  &lt;p&gt;The &lt;b&gt;StartDateTime&lt;/b&gt; and &lt;b&gt;EndDateTime&lt;/b&gt; are required. Use the ISO 8601 format for DateTime Timezone, e.g., &lt;b&gt;2016-10-30T09:00:00-5:00&lt;/b&gt;.&lt;/p&gt;  &lt;p&gt;The serviceId is optional. If changing the &lt;b&gt;serviceId&lt;/b&gt;, the new service id&#39;s duration must match the original service&#39;s duration.&lt;/p&gt;  &lt;p&gt;The resourceId is optional. If changing the &lt;b&gt;resourceId&lt;/b&gt;, verify the availability of the new resource prior to rescheduling.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;IMPORTANT:&lt;/b&gt; Always run availability before rescheduling an appointment to verify the timeslot is open and available for the new time, service and/or resource requested. This is the only way to assure the slot is available. You cannot reschedule an appointment to a different location. If necessary, you should cancel and then book an appointment in the other location.&lt;/p&gt;  &lt;p&gt;For more information: &lt;a href&#x3D;\&quot;https://onsched.readme.io/docs/appointments-overview\&quot;&gt;Appointment Overview&lt;/a&gt;&lt;/p&gt;

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
    String id = "id_example"; // String | appointment id to reschedule
    AppointmentRescheduleModel appointmentRescheduleModel = new AppointmentRescheduleModel(); // AppointmentRescheduleModel | 
    try {
      AppointmentViewModel result = apiInstance.consumerV1AppointmentsIdReschedulePut(id, appointmentRescheduleModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppointmentsApi#consumerV1AppointmentsIdReschedulePut");
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
| **id** | **String**| appointment id to reschedule | |
| **appointmentRescheduleModel** | [**AppointmentRescheduleModel**](AppointmentRescheduleModel.md)|  | [optional] |

### Return type

[**AppointmentViewModel**](AppointmentViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="consumerV1AppointmentsIdReservePut"></a>
# **consumerV1AppointmentsIdReservePut**
> consumerV1AppointmentsIdReservePut(id, sendNotifications, appointmentReserveModel)

Reserve Appointment

&lt;p&gt;Use this endpoint to &lt;b&gt;Reserve&lt;/b&gt; an appointment. Only appointments with an \&quot;IN\&quot; status, Initial, can be reserved. A valid &lt;b&gt;appointment id&lt;/b&gt; is required. Use the appointment id returned from the initial &lt;i&gt;POST /consumer/v1/appointments&lt;/i&gt; endpoint.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;NOTE: Reservations are different from Bookings as reservations are a two-step booking process that must be managed by the API consumer.&lt;/b&gt; An appointment that is reserved is not completely booked until other business conditions have been met. For example, an appointment may be reserved if it is not yet assigned to a resource or until the customer or resource explicitly confirms it.&lt;/p&gt;  &lt;p&gt;With reservations you have the ability to notify the customer of a reservation prior to officially booking and the workflow can be designed to indicate what conditions will need to be met in order to convert the reservation to a complete booking. A reservation converts to a complete booking when it is either Confirmed or Booked. &lt;/p&gt;  &lt;p&gt;    &lt;b&gt;IMPORTANT: A reserved appointment time will not be released, i.e., become available to others, until it is Cancelled. The booking timer is not used with reserved appointments.&lt;/b&gt;  &lt;/p&gt;  &lt;p&gt;For more information: &lt;a href&#x3D;\&quot;https://onsched.readme.io/docs/appointments-overview\&quot;&gt;Appointments Overview&lt;/a&gt;&lt;/p&gt;

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
    String id = "id_example"; // String | appointment id to reserve
    Boolean sendNotifications = true; // Boolean | 
    AppointmentReserveModel appointmentReserveModel = new AppointmentReserveModel(); // AppointmentReserveModel | 
    try {
      apiInstance.consumerV1AppointmentsIdReservePut(id, sendNotifications, appointmentReserveModel);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppointmentsApi#consumerV1AppointmentsIdReservePut");
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
| **id** | **String**| appointment id to reserve | |
| **sendNotifications** | **Boolean**|  | [optional] |
| **appointmentReserveModel** | [**AppointmentReserveModel**](AppointmentReserveModel.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="consumerV1AppointmentsPost"></a>
# **consumerV1AppointmentsPost**
> AppointmentInitialViewModel consumerV1AppointmentsPost(completeBooking, appointmentInitialModel)

Create Appointment

&lt;p&gt;Use this endpoint to &lt;b&gt;Create&lt;/b&gt; a new appointment. The appointment will be created with an \&quot;IN\&quot;, Initial status. Posting an appointment with \&quot;IN\&quot; status requires minimal information and requires a \&quot;PUT book\&quot; call to complete the booking transaction, &lt;i&gt;PUT ​/consumer​/v1​/appointments​/{id}​/book&lt;/i&gt;. Alternatively, you can post an appointment using the &lt;b&gt;completeBooking&lt;/b&gt; option which completes the booking in one transaction, but it will require more data. The method you choose depends on your solutions workflow. &lt;/p&gt;  &lt;p&gt;    &lt;b&gt;StartDateTime&lt;/b&gt; and &lt;b&gt;EndDateTime&lt;/b&gt; are required. Use the ISO 8601 format for DateTime Timezone, e.g., &lt;b&gt;2016-10-30T09:00:00-5:00&lt;/b&gt;&lt;/p&gt;  &lt;p&gt;A valid &lt;b&gt;serviceId&lt;/b&gt; is required. The serviceId provided must be valid for the location being booked. A valid serviceId is one that is scoped to a Primary Company Location or is associated with a Business Location&lt;/p&gt;  &lt;p&gt;OPTIONAL FIELDS INCLUDE: &lt;/p&gt;  &lt;p&gt;    &lt;b&gt;locationId&lt;/b&gt; - if not supplied, the appointment will be posted to the primary business location. If you support multiple location, we recommend always supplying the locationId. &lt;/p&gt;  &lt;p&gt;    &lt;b&gt;resourceId&lt;/b&gt; - not required when posting with an \&quot;IN\&quot; status but is required when the appointment is booked. Use &lt;i&gt;GET /consumer/v1/resources&lt;/i&gt; for a list of resources. &lt;/p&gt;  &lt;p&gt;    &lt;b&gt;customerId&lt;/b&gt; - if supplied the name and email will be retrieved from the customer record. &lt;/p&gt;  &lt;p&gt;    &lt;b&gt;BookedBy&lt;/b&gt; - if not supplied the email address of the booked appointment is used or the ip address if no email address is provided. BookedBy is used in the Appointment Audit trail which can be viewed in the appointment object.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Location&lt;/b&gt; - is a string value representing the location of the appointment. It provides no added functionality in OnSched and should not be confused with locationId.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;TimezoneName&lt;/b&gt; - if used timezoneName must be in IANA format, &lt;i&gt;America/New_York&lt;/i&gt;. This is the timezone the appointment was booked in. Populating this information can help later in situations where appointments are booked before a Daylight Savings change. If no timezoneName is supplied, the Business Locations timezone will be used.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;COMPLETE BOOKING:&lt;/b&gt; This parameter provides a mechanism for immediate booking with the POST appointment endpoint. To complete the booking in one transaction, populate the &lt;b&gt;completeBooking&lt;/b&gt; parameter with a \&quot;BK\&quot;, booked or an \&quot;RS\&quot;, reserved status and provide an (&lt;b&gt;email&lt;/b&gt; and &lt;b&gt;name&lt;/b&gt;) or a &lt;b&gt;customerId&lt;/b&gt; in the post body. Doing so will book the appointment and send notifications all in one transaction. &lt;b&gt;Note:&lt;/b&gt; \&quot;IN\&quot; can also be used as a completeBooking option to support payment flows. With the \&quot;IN\&quot; option, notifications are NOT sent.&lt;/p&gt;  &lt;p&gt;For more information: &lt;a href&#x3D;\&quot;https://onsched.readme.io/docs/appointments-overview\&quot;&gt;Appointments Overview&lt;/a&gt;&lt;/p&gt;

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
    String completeBooking = "completeBooking_example"; // String | Options are \"BK\", \"RS\" or \"IN\"
    AppointmentInitialModel appointmentInitialModel = new AppointmentInitialModel(); // AppointmentInitialModel | 
    try {
      AppointmentInitialViewModel result = apiInstance.consumerV1AppointmentsPost(completeBooking, appointmentInitialModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppointmentsApi#consumerV1AppointmentsPost");
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
| **completeBooking** | **String**| Options are \&quot;BK\&quot;, \&quot;RS\&quot; or \&quot;IN\&quot; | [optional] |
| **appointmentInitialModel** | [**AppointmentInitialModel**](AppointmentInitialModel.md)|  | [optional] |

### Return type

[**AppointmentInitialViewModel**](AppointmentInitialViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

