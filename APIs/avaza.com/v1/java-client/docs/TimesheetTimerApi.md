# TimesheetTimerApi

All URIs are relative to *https://api.avaza.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**timesheetTimerGetRunningTimer**](TimesheetTimerApi.md#timesheetTimerGetRunningTimer) | **GET** /api/TimesheetTimer | Gets the  Running Timer if there is one for a user. |
| [**timesheetTimerStartTimer**](TimesheetTimerApi.md#timesheetTimerStartTimer) | **POST** /api/TimesheetTimer/{id} | Starts a Timer running on an existing Timesheet Entry |
| [**timesheetTimerStopTimer**](TimesheetTimerApi.md#timesheetTimerStopTimer) | **DELETE** /api/TimesheetTimer/{id} | Stop the timer running on an existing Timesheet Entry |


<a id="timesheetTimerGetRunningTimer"></a>
# **timesheetTimerGetRunningTimer**
> Object timesheetTimerGetRunningTimer(userID)

Gets the  Running Timer if there is one for a user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimesheetTimerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TimesheetTimerApi apiInstance = new TimesheetTimerApi(defaultClient);
    Integer userID = 56; // Integer | Optional - User ID number if impersonating a different user. Otherwise assumes the current user. Only users with certain security roles have permission to impersonate other users
    try {
      Object result = apiInstance.timesheetTimerGetRunningTimer(userID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimesheetTimerApi#timesheetTimerGetRunningTimer");
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
| **userID** | **Integer**| Optional - User ID number if impersonating a different user. Otherwise assumes the current user. Only users with certain security roles have permission to impersonate other users | [optional] |

### Return type

**Object**

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
| **404** | Not Found |  -  |

<a id="timesheetTimerStartTimer"></a>
# **timesheetTimerStartTimer**
> Object timesheetTimerStartTimer(id, userID)

Starts a Timer running on an existing Timesheet Entry

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimesheetTimerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TimesheetTimerApi apiInstance = new TimesheetTimerApi(defaultClient);
    Long id = 56L; // Long | id of timesheet entry that should be used as the basis for running a timer. If the existing timesheet is not on the current day, or you have start/end times enabled, then a new timesheet will be created for the timer.
    Integer userID = 56; // Integer | Optional - User ID number if impersonating a different user. Otherwise assumes the current user. Only users with certain security roles have permission to impersonate other users
    try {
      Object result = apiInstance.timesheetTimerStartTimer(id, userID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimesheetTimerApi#timesheetTimerStartTimer");
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
| **id** | **Long**| id of timesheet entry that should be used as the basis for running a timer. If the existing timesheet is not on the current day, or you have start/end times enabled, then a new timesheet will be created for the timer. | |
| **userID** | **Integer**| Optional - User ID number if impersonating a different user. Otherwise assumes the current user. Only users with certain security roles have permission to impersonate other users | [optional] |

### Return type

**Object**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="timesheetTimerStopTimer"></a>
# **timesheetTimerStopTimer**
> Object timesheetTimerStopTimer(id, userID)

Stop the timer running on an existing Timesheet Entry

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimesheetTimerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TimesheetTimerApi apiInstance = new TimesheetTimerApi(defaultClient);
    Long id = 56L; // Long | The ID of the existing timesheet entry that needs its timer stopped
    Integer userID = 56; // Integer | Optional - User ID number if impersonating a different user. Otherwise assumes the current user. Only users with certain security roles have permission to impersonate other users
    try {
      Object result = apiInstance.timesheetTimerStopTimer(id, userID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimesheetTimerApi#timesheetTimerStopTimer");
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
| **id** | **Long**| The ID of the existing timesheet entry that needs its timer stopped | |
| **userID** | **Integer**| Optional - User ID number if impersonating a different user. Otherwise assumes the current user. Only users with certain security roles have permission to impersonate other users | [optional] |

### Return type

**Object**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

