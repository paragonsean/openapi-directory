# ScheduleSeriesApi

All URIs are relative to *https://api.avaza.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**scheduleSeriesAddBooking**](ScheduleSeriesApi.md#scheduleSeriesAddBooking) | **POST** /ScheduleSeries/AddBooking | Create new Schedule Booking |
| [**scheduleSeriesAddLeave**](ScheduleSeriesApi.md#scheduleSeriesAddLeave) | **POST** /ScheduleSeries/AddLeave | Create new Leave Booking |
| [**scheduleSeriesEditBooking**](ScheduleSeriesApi.md#scheduleSeriesEditBooking) | **PUT** /ScheduleSeries/EditBooking | Edit Booking |
| [**scheduleSeriesEditLeave**](ScheduleSeriesApi.md#scheduleSeriesEditLeave) | **PUT** /ScheduleSeries/EditLeave | Edit Leave Booking |
| [**scheduleSeriesGet**](ScheduleSeriesApi.md#scheduleSeriesGet) | **GET** /api/ScheduleSeries | Gets list of Schedule Series |


<a id="scheduleSeriesAddBooking"></a>
# **scheduleSeriesAddBooking**
> ScheduleSeriesDetails scheduleSeriesAddBooking(model)

Create new Schedule Booking

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScheduleSeriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ScheduleSeriesApi apiInstance = new ScheduleSeriesApi(defaultClient);
    CreateBooking model = new CreateBooking(); // CreateBooking | 
    try {
      ScheduleSeriesDetails result = apiInstance.scheduleSeriesAddBooking(model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScheduleSeriesApi#scheduleSeriesAddBooking");
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
| **model** | [**CreateBooking**](CreateBooking.md)|  | |

### Return type

[**ScheduleSeriesDetails**](ScheduleSeriesDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="scheduleSeriesAddLeave"></a>
# **scheduleSeriesAddLeave**
> ScheduleSeriesDetails scheduleSeriesAddLeave(model)

Create new Leave Booking

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScheduleSeriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ScheduleSeriesApi apiInstance = new ScheduleSeriesApi(defaultClient);
    CreateLeave model = new CreateLeave(); // CreateLeave | 
    try {
      ScheduleSeriesDetails result = apiInstance.scheduleSeriesAddLeave(model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScheduleSeriesApi#scheduleSeriesAddLeave");
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
| **model** | [**CreateLeave**](CreateLeave.md)|  | |

### Return type

[**ScheduleSeriesDetails**](ScheduleSeriesDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="scheduleSeriesEditBooking"></a>
# **scheduleSeriesEditBooking**
> ScheduleSeriesDetails scheduleSeriesEditBooking(model)

Edit Booking

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScheduleSeriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ScheduleSeriesApi apiInstance = new ScheduleSeriesApi(defaultClient);
    EditBooking model = new EditBooking(); // EditBooking | 
    try {
      ScheduleSeriesDetails result = apiInstance.scheduleSeriesEditBooking(model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScheduleSeriesApi#scheduleSeriesEditBooking");
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
| **model** | [**EditBooking**](EditBooking.md)|  | |

### Return type

[**ScheduleSeriesDetails**](ScheduleSeriesDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="scheduleSeriesEditLeave"></a>
# **scheduleSeriesEditLeave**
> ScheduleSeriesDetails scheduleSeriesEditLeave(model)

Edit Leave Booking

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScheduleSeriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ScheduleSeriesApi apiInstance = new ScheduleSeriesApi(defaultClient);
    EditLeave model = new EditLeave(); // EditLeave | 
    try {
      ScheduleSeriesDetails result = apiInstance.scheduleSeriesEditLeave(model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScheduleSeriesApi#scheduleSeriesEditLeave");
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
| **model** | [**EditLeave**](EditLeave.md)|  | |

### Return type

[**ScheduleSeriesDetails**](ScheduleSeriesDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="scheduleSeriesGet"></a>
# **scheduleSeriesGet**
> ScheduleSeriesList scheduleSeriesGet(updatedAfter, scheduleStartDateFrom, scheduleStartDateTo, scheduleEndDateFrom, scheduleEndDateTo, userID, userEmail, timeSheetCategoryID, timeSheetCategoryName, leaveTypeID, projectID, companyID, pageSize, pageNumber, sort)

Gets list of Schedule Series

Schedule Series represents a strip of time assigned to a user over a date range, for a certain number of hours per day. They can be for Leave or for project work Bookings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScheduleSeriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ScheduleSeriesApi apiInstance = new ScheduleSeriesApi(defaultClient);
    OffsetDateTime updatedAfter = OffsetDateTime.now(); // OffsetDateTime | Limit results to records updated after the specified date
    OffsetDateTime scheduleStartDateFrom = OffsetDateTime.now(); // OffsetDateTime | Filter for schedules that start on or after a specific date
    OffsetDateTime scheduleStartDateTo = OffsetDateTime.now(); // OffsetDateTime | Filter for schedules that start on or before a specific date
    OffsetDateTime scheduleEndDateFrom = OffsetDateTime.now(); // OffsetDateTime | Filter for schedules that end on or after a specific date
    OffsetDateTime scheduleEndDateTo = OffsetDateTime.now(); // OffsetDateTime | Filter for schedules that end on or before a specific date
    Integer userID = 56; // Integer | The UserID of a schedule user to filter assignments for. Only api users with Admin role can see all schedules across all users. Users with ScheduleUser role can access their own ScheduleSeries.
    String userEmail = "userEmail_example"; // String | The email of the user who has been scheduled
    Integer timeSheetCategoryID = 56; // Integer | Filter for schedule records linked to a specific timesheeet category
    String timeSheetCategoryName = "timeSheetCategoryName_example"; // String | Filter for schedule records with a specific timesheeet category name (exact string match)
    Integer leaveTypeID = 56; // Integer | Filter to records of a particular leave type
    Integer projectID = 56; // Integer | Filter to only include books linked to a specific project
    Integer companyID = 56; // Integer | Filter to only include records linked to projects, where that project belongs to a specific customer company
    Integer pageSize = 56; // Integer | Number of items per page (max 1000)
    Integer pageNumber = 56; // Integer | Page to display. Starts from 1.
    String sort = "sort_example"; // String | Optional sorting instruction. Currently possible values: \"DateUpdated\", \"DateCreated\", \"DateUpdated desc\", \"DateCreated desc\"
    try {
      ScheduleSeriesList result = apiInstance.scheduleSeriesGet(updatedAfter, scheduleStartDateFrom, scheduleStartDateTo, scheduleEndDateFrom, scheduleEndDateTo, userID, userEmail, timeSheetCategoryID, timeSheetCategoryName, leaveTypeID, projectID, companyID, pageSize, pageNumber, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScheduleSeriesApi#scheduleSeriesGet");
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
| **updatedAfter** | **OffsetDateTime**| Limit results to records updated after the specified date | [optional] |
| **scheduleStartDateFrom** | **OffsetDateTime**| Filter for schedules that start on or after a specific date | [optional] |
| **scheduleStartDateTo** | **OffsetDateTime**| Filter for schedules that start on or before a specific date | [optional] |
| **scheduleEndDateFrom** | **OffsetDateTime**| Filter for schedules that end on or after a specific date | [optional] |
| **scheduleEndDateTo** | **OffsetDateTime**| Filter for schedules that end on or before a specific date | [optional] |
| **userID** | **Integer**| The UserID of a schedule user to filter assignments for. Only api users with Admin role can see all schedules across all users. Users with ScheduleUser role can access their own ScheduleSeries. | [optional] |
| **userEmail** | **String**| The email of the user who has been scheduled | [optional] |
| **timeSheetCategoryID** | **Integer**| Filter for schedule records linked to a specific timesheeet category | [optional] |
| **timeSheetCategoryName** | **String**| Filter for schedule records with a specific timesheeet category name (exact string match) | [optional] |
| **leaveTypeID** | **Integer**| Filter to records of a particular leave type | [optional] |
| **projectID** | **Integer**| Filter to only include books linked to a specific project | [optional] |
| **companyID** | **Integer**| Filter to only include records linked to projects, where that project belongs to a specific customer company | [optional] |
| **pageSize** | **Integer**| Number of items per page (max 1000) | [optional] |
| **pageNumber** | **Integer**| Page to display. Starts from 1. | [optional] |
| **sort** | **String**| Optional sorting instruction. Currently possible values: \&quot;DateUpdated\&quot;, \&quot;DateCreated\&quot;, \&quot;DateUpdated desc\&quot;, \&quot;DateCreated desc\&quot; | [optional] |

### Return type

[**ScheduleSeriesList**](ScheduleSeriesList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |

