# CalendarsApi

All URIs are relative to *https://sandbox-api.onsched.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**setupV1CalendarsBlockIdDelete**](CalendarsApi.md#setupV1CalendarsBlockIdDelete) | **DELETE** /setup/v1/calendars/block/{id} | Delete Calendar Block |
| [**setupV1CalendarsBlockIdPut**](CalendarsApi.md#setupV1CalendarsBlockIdPut) | **PUT** /setup/v1/calendars/block/{id} | Update Calendar Block |
| [**setupV1CalendarsBlocksIdGet**](CalendarsApi.md#setupV1CalendarsBlocksIdGet) | **GET** /setup/v1/calendars/blocks/{id} | Get Calendar Block |
| [**setupV1CalendarsGet**](CalendarsApi.md#setupV1CalendarsGet) | **GET** /setup/v1/calendars | List Calendars |
| [**setupV1CalendarsIdBlockPost**](CalendarsApi.md#setupV1CalendarsIdBlockPost) | **POST** /setup/v1/calendars/{id}/block | Create Calendar Block |
| [**setupV1CalendarsIdBlocksGet**](CalendarsApi.md#setupV1CalendarsIdBlocksGet) | **GET** /setup/v1/calendars/{id}/blocks | List Calendar Blocks |
| [**setupV1CalendarsIdDelete**](CalendarsApi.md#setupV1CalendarsIdDelete) | **DELETE** /setup/v1/calendars/{id} | Delete Calendar |
| [**setupV1CalendarsIdGet**](CalendarsApi.md#setupV1CalendarsIdGet) | **GET** /setup/v1/calendars/{id} | Get Calendar |
| [**setupV1CalendarsIdPut**](CalendarsApi.md#setupV1CalendarsIdPut) | **PUT** /setup/v1/calendars/{id} | Update Calendar |
| [**setupV1CalendarsIdRecoverPut**](CalendarsApi.md#setupV1CalendarsIdRecoverPut) | **PUT** /setup/v1/calendars/{id}/recover | Recover Calendar |
| [**setupV1CalendarsIdServicesGet**](CalendarsApi.md#setupV1CalendarsIdServicesGet) | **GET** /setup/v1/calendars/{id}/services | List Calendar Services |
| [**setupV1CalendarsPost**](CalendarsApi.md#setupV1CalendarsPost) | **POST** /setup/v1/calendars | DEPRECATING: Create |


<a id="setupV1CalendarsBlockIdDelete"></a>
# **setupV1CalendarsBlockIdDelete**
> CalendarBlockViewModel setupV1CalendarsBlockIdDelete(id)

Delete Calendar Block

&lt;p&gt;Use this endpoint to permanently &lt;b&gt;Delete&lt;/b&gt; a calendar block. A valid &lt;b&gt;calendarBlock id&lt;/b&gt; is required.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CalendarsApi apiInstance = new CalendarsApi(defaultClient);
    String id = "id_example"; // String | id of a calendarBlock object
    try {
      CalendarBlockViewModel result = apiInstance.setupV1CalendarsBlockIdDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarsApi#setupV1CalendarsBlockIdDelete");
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
| **id** | **String**| id of a calendarBlock object | |

### Return type

[**CalendarBlockViewModel**](CalendarBlockViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1CalendarsBlockIdPut"></a>
# **setupV1CalendarsBlockIdPut**
> CalendarBlockViewModel setupV1CalendarsBlockIdPut(id, calendarBlockUpdateModel)

Update Calendar Block

&lt;p&gt;Use this endpoint to &lt;b&gt;Create&lt;/b&gt; a Calendar Block. A valid &lt;b&gt;calendarBlock id&lt;/b&gt; is required. Refer to the &lt;i&gt;POST ​/setup​/v1​/calendars​/{id}​/block&lt;/i&gt; endpoint for fieldnames and details.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CalendarsApi apiInstance = new CalendarsApi(defaultClient);
    String id = "id_example"; // String | id of calendarBlock object
    CalendarBlockUpdateModel calendarBlockUpdateModel = new CalendarBlockUpdateModel(); // CalendarBlockUpdateModel | Resource Block input model
    try {
      CalendarBlockViewModel result = apiInstance.setupV1CalendarsBlockIdPut(id, calendarBlockUpdateModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarsApi#setupV1CalendarsBlockIdPut");
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
| **id** | **String**| id of calendarBlock object | |
| **calendarBlockUpdateModel** | [**CalendarBlockUpdateModel**](CalendarBlockUpdateModel.md)| Resource Block input model | [optional] |

### Return type

[**CalendarBlockViewModel**](CalendarBlockViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1CalendarsBlocksIdGet"></a>
# **setupV1CalendarsBlocksIdGet**
> CalendarBlockViewModel setupV1CalendarsBlocksIdGet(id)

Get Calendar Block

&lt;p&gt;Use this endpoint to return a &lt;b&gt;Calendar Block&lt;/b&gt;. A valid &lt;b&gt;calendarBlock id&lt;/b&gt; is required. &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CalendarsApi apiInstance = new CalendarsApi(defaultClient);
    String id = "id_example"; // String | id of calendarBlock object
    try {
      CalendarBlockViewModel result = apiInstance.setupV1CalendarsBlocksIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarsApi#setupV1CalendarsBlocksIdGet");
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
| **id** | **String**| id of calendarBlock object | |

### Return type

[**CalendarBlockViewModel**](CalendarBlockViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1CalendarsGet"></a>
# **setupV1CalendarsGet**
> ScheduleListViewModel setupV1CalendarsGet(locationId, deleted, offset, limit)

List Calendars

&lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Calendars&lt;/b&gt; from the requested location. If not specified, the business location defaults to the primary business location. &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CalendarsApi apiInstance = new CalendarsApi(defaultClient);
    String locationId = "locationId_example"; // String | id of business location, defaults to primary business location
    Boolean deleted = true; // Boolean | Filter by deleted status
    Integer offset = 56; // Integer | Starting row of page, default 0
    Integer limit = 56; // Integer | Page limit default 20, max 100
    try {
      ScheduleListViewModel result = apiInstance.setupV1CalendarsGet(locationId, deleted, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarsApi#setupV1CalendarsGet");
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
| **deleted** | **Boolean**| Filter by deleted status | [optional] |
| **offset** | **Integer**| Starting row of page, default 0 | [optional] |
| **limit** | **Integer**| Page limit default 20, max 100 | [optional] |

### Return type

[**ScheduleListViewModel**](ScheduleListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1CalendarsIdBlockPost"></a>
# **setupV1CalendarsIdBlockPost**
> ResourceBlockViewModel setupV1CalendarsIdBlockPost(id, calendarBlockInputModel)

Create Calendar Block

&lt;p&gt;Use this endpoint to &lt;b&gt;Create&lt;/b&gt; a Calendar Block. A valid &lt;b&gt;calendar id&lt;/b&gt; is required.&lt;/p&gt;  &lt;p&gt;Required fields: &lt;b&gt;startDate, endDate, startTime, endTime&lt;/b&gt; and &lt;b&gt;reason&lt;/b&gt;.&lt;/p&gt;  &lt;p&gt;Calendar blocks can be set to specific time ranges or for the whole day. Th block a whole day set the startTime to 0 and endTime to 2400.&lt;/p&gt;  &lt;p&gt;Calendar blocks can be for a specific date range instance or set to repeat at a specified frequency.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Repeat object: (repeats &#x3D; true)&lt;/b&gt;  &lt;/p&gt;  &lt;p&gt;The &lt;b&gt;frequency&lt;/b&gt; can be set to a value of &lt;b&gt;D, W or M&lt;/b&gt; for &lt;b&gt;Day, Week&lt;/b&gt; or &lt;b&gt;Month&lt;/b&gt; respectively.&lt;/p&gt;  &lt;p&gt;Use the &lt;b&gt;interval&lt;/b&gt; property to specify the interval that the block repeats. For example, an interval of 2 for a weekly block means that the block will repeat every 2nd week beginning at the day specified. A daily block with an interval of 10 means the block will repeat every 10 days. The interval property applies to all repeat frequencies. &lt;b&gt;If using the repeat functionality an interval value is required&lt;/b&gt;.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;DAILY BLOCKS&lt;/b&gt;: Will repeat for each day of the week for the date range specified for the interval specified.  An interval value of “1” repeats every day, and an interval value of “3” is every 3rd day.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;WEEKLY BLOCKS&lt;/b&gt;: Will repeat only on the specified days of the week for the date range specified. For weekly the &lt;b&gt;frequency&lt;/b&gt;  is required and should be set to &lt;b&gt;“W”&lt;/b&gt;.  You must specify the &lt;b&gt;weekdays&lt;/b&gt; parameter. Weekdays are expressed as a string of digits with each single digit in the string representing a day of the week. The possible values are &lt;b&gt;0,1,2,3,4,5,6&lt;/b&gt; where &lt;b&gt;0&#x3D;Sunday, 1&#x3D;Monday, 2&#x3D;Tuesday, 3&#x3D;Wednesday, 4&#x3D;Thursday, 5&#x3D;Friday, 6&#x3D;Saturday&lt;/b&gt;. For example, a weekly frequency with an interval of “1”, and an entry of weekdays &#x3D; “24”, will repeat each week on Tuesday and Thursday for the duration of the block date range.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;MONTHLY BLOCKS&lt;/b&gt;: Will repeat either on the day of the month specified in the &lt;b&gt;monthDay&lt;/b&gt; property or on the day of the week and week of the month specified by the &lt;b&gt;monthType&lt;/b&gt; property.  In both cases &lt;b&gt;frequency&lt;/b&gt; is required and should be set to &lt;b&gt;“M”&lt;/b&gt;, monthly, &lt;b&gt;monthDay&lt;/b&gt; is the day of the month you want blocked.  If monthDay&#x3D;’15’ this means to block the 15th of every month in the date range requested. Using monthDay in conjunction with monthType addresses “day of the week and week of the month” scenario.  There are two possible values for monthType: &lt;b&gt;D for Day of Month&lt;/b&gt; or &lt;b&gt;W for Week of Month.&lt;/b&gt; For &lt;b&gt;monthType D&lt;/b&gt;, monthDay value must be between 1 and 31. It is the day of the month to repeat on. For &lt;b&gt;monthType M&lt;/b&gt;, monthDay value contains 2 digits: day of week (0-6), (0,1,2,3,4,5,6 where 0&#x3D;Sunday, 1&#x3D;Monday, 2&#x3D;Tuesday, 3&#x3D;Wednesday, 4&#x3D;Thursday, 5&#x3D;Friday, 6&#x3D;Saturday) and week of month (1-5). 1 being the first week, 2 being the second. The third Thursday of the month is depicted as a monthType&#x3D;”M” and monthDay&#x3D;”43”.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Repeats will end on the date specified by the end date.&lt;/b&gt;  &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CalendarsApi apiInstance = new CalendarsApi(defaultClient);
    String id = "id_example"; // String | id of calendar object
    CalendarBlockInputModel calendarBlockInputModel = new CalendarBlockInputModel(); // CalendarBlockInputModel | 
    try {
      ResourceBlockViewModel result = apiInstance.setupV1CalendarsIdBlockPost(id, calendarBlockInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarsApi#setupV1CalendarsIdBlockPost");
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
| **id** | **String**| id of calendar object | |
| **calendarBlockInputModel** | [**CalendarBlockInputModel**](CalendarBlockInputModel.md)|  | [optional] |

### Return type

[**ResourceBlockViewModel**](ResourceBlockViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1CalendarsIdBlocksGet"></a>
# **setupV1CalendarsIdBlocksGet**
> CalendarBlockListViewModel setupV1CalendarsIdBlocksGet(id, offset, limit)

List Calendar Blocks

&lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Calendar Blocks&lt;/b&gt; for the requested calendar. A valid &lt;b&gt;calendar id&lt;/b&gt; is required. &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CalendarsApi apiInstance = new CalendarsApi(defaultClient);
    String id = "id_example"; // String | id of calendar to list blocks
    Integer offset = 56; // Integer | Starting row of page, default 0
    Integer limit = 56; // Integer | Page limit default 20, max 100
    try {
      CalendarBlockListViewModel result = apiInstance.setupV1CalendarsIdBlocksGet(id, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarsApi#setupV1CalendarsIdBlocksGet");
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
| **id** | **String**| id of calendar to list blocks | |
| **offset** | **Integer**| Starting row of page, default 0 | [optional] |
| **limit** | **Integer**| Page limit default 20, max 100 | [optional] |

### Return type

[**CalendarBlockListViewModel**](CalendarBlockListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid response |  -  |
| **400** | Missing or invalid values in the request |  -  |
| **401** | Authorization error. |  -  |
| **404** | Resource was not found |  -  |

<a id="setupV1CalendarsIdDelete"></a>
# **setupV1CalendarsIdDelete**
> ScheduleViewModel setupV1CalendarsIdDelete(id)

Delete Calendar

&lt;p&gt;Use this endpoint to &lt;b&gt;Delete&lt;/b&gt; a calendar object. A valid &lt;b&gt;calendar id&lt;/b&gt; is required. The calendar is not permanently deleted and can be recovered by using the &lt;i&gt;PUT ​/setup​/v1​/calendars​/{id}​/recover &lt;/i&gt;endpoint.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CalendarsApi apiInstance = new CalendarsApi(defaultClient);
    String id = "id_example"; // String | id of calendar object
    try {
      ScheduleViewModel result = apiInstance.setupV1CalendarsIdDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarsApi#setupV1CalendarsIdDelete");
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
| **id** | **String**| id of calendar object | |

### Return type

[**ScheduleViewModel**](ScheduleViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1CalendarsIdGet"></a>
# **setupV1CalendarsIdGet**
> ScheduleViewModel setupV1CalendarsIdGet(id)

Get Calendar

&lt;p&gt;Use this endpoint to return a &lt;b&gt;Calendar&lt;/b&gt; object. A valid &lt;b&gt;calendar id&lt;/b&gt; is required.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CalendarsApi apiInstance = new CalendarsApi(defaultClient);
    String id = "id_example"; // String | id of calendar object
    try {
      ScheduleViewModel result = apiInstance.setupV1CalendarsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarsApi#setupV1CalendarsIdGet");
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
| **id** | **String**| id of calendar object | |

### Return type

[**ScheduleViewModel**](ScheduleViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1CalendarsIdPut"></a>
# **setupV1CalendarsIdPut**
> ScheduleViewModel setupV1CalendarsIdPut(id, scheduleUpdateModel)

Update Calendar

&lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; a calendar object. A valid &lt;b&gt;calendar id&lt;/b&gt; is required. When your company was created a calendar object was automatically created with 24-hour weekly availability. Its &lt;b&gt;name &#x3D; Main&lt;/b&gt;, the &lt;b&gt;type &#x3D; resource&lt;/b&gt; and by default the &lt;b&gt;interval &#x3D; 30 mins&lt;/b&gt;. We are currently supporting resource calendar type. Other types were part of our Legacy Application and has no relevance in the API product.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CalendarsApi apiInstance = new CalendarsApi(defaultClient);
    String id = "id_example"; // String | id of calendar object
    ScheduleUpdateModel scheduleUpdateModel = new ScheduleUpdateModel(); // ScheduleUpdateModel | Input model for the calendar object
    try {
      ScheduleViewModel result = apiInstance.setupV1CalendarsIdPut(id, scheduleUpdateModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarsApi#setupV1CalendarsIdPut");
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
| **id** | **String**| id of calendar object | |
| **scheduleUpdateModel** | [**ScheduleUpdateModel**](ScheduleUpdateModel.md)| Input model for the calendar object | [optional] |

### Return type

[**ScheduleViewModel**](ScheduleViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1CalendarsIdRecoverPut"></a>
# **setupV1CalendarsIdRecoverPut**
> ScheduleViewModel setupV1CalendarsIdRecoverPut(id)

Recover Calendar

&lt;p&gt;Use this endpoint to &lt;b&gt;Recover&lt;/b&gt; a previously deleted calendar object. A valid &lt;b&gt;calendar id&lt;/b&gt; is required.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CalendarsApi apiInstance = new CalendarsApi(defaultClient);
    String id = "id_example"; // String | id of calendar object
    try {
      ScheduleViewModel result = apiInstance.setupV1CalendarsIdRecoverPut(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarsApi#setupV1CalendarsIdRecoverPut");
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
| **id** | **String**| id of calendar object | |

### Return type

[**ScheduleViewModel**](ScheduleViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1CalendarsIdServicesGet"></a>
# **setupV1CalendarsIdServicesGet**
> ServiceListViewModel setupV1CalendarsIdServicesGet(id, offset, limit)

List Calendar Services

&lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Linked Services&lt;/b&gt; of a calendar object. A valid &lt;b&gt;calendar id&lt;/b&gt; is required. Find calendar id&#39;s by using the &lt;i&gt;GET /setup/v1/calendars&lt;/i&gt; endpoint.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CalendarsApi apiInstance = new CalendarsApi(defaultClient);
    String id = "id_example"; // String | id of calendar object
    Integer offset = 56; // Integer | Starting row of page, default 0
    Integer limit = 56; // Integer | Page limit default 20, max 100
    try {
      ServiceListViewModel result = apiInstance.setupV1CalendarsIdServicesGet(id, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarsApi#setupV1CalendarsIdServicesGet");
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
| **id** | **String**| id of calendar object | |
| **offset** | **Integer**| Starting row of page, default 0 | [optional] |
| **limit** | **Integer**| Page limit default 20, max 100 | [optional] |

### Return type

[**ServiceListViewModel**](ServiceListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1CalendarsPost"></a>
# **setupV1CalendarsPost**
> ScheduleViewModel setupV1CalendarsPost(scheduleInputModel)

DEPRECATING: Create

&lt;p&gt;    &lt;b&gt;DEPRECATING:&lt;/b&gt; Create Calendar&lt;/p&gt;  &lt;p&gt;We are no longer supporting Multiple Calendar Functionality as it is part of our Legacy Application and has no relevance in the API.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CalendarsApi apiInstance = new CalendarsApi(defaultClient);
    ScheduleInputModel scheduleInputModel = new ScheduleInputModel(); // ScheduleInputModel | 
    try {
      ScheduleViewModel result = apiInstance.setupV1CalendarsPost(scheduleInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarsApi#setupV1CalendarsPost");
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
| **scheduleInputModel** | [**ScheduleInputModel**](ScheduleInputModel.md)|  | [optional] |

### Return type

[**ScheduleViewModel**](ScheduleViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

