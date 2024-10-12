# DutiesApi

All URIs are relative to *https://connect.signl4.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**teamsTeamIdDutyReportsFileNameGet**](DutiesApi.md#teamsTeamIdDutyReportsFileNameGet) | **GET** /teams/{teamId}/dutyReports/{fileName} | Download duty report with a specific fileName |
| [**teamsTeamIdDutyReportsGet**](DutiesApi.md#teamsTeamIdDutyReportsGet) | **GET** /teams/{teamId}/dutyReports | Get Information about downloadable reports |
| [**teamsTeamIdDutysummaryGet**](DutiesApi.md#teamsTeamIdDutysummaryGet) | **GET** /teams/{teamId}/dutysummary | Get duty assistant info for a team |
| [**teamsTeamIdSchedulesDeleteRangePost**](DutiesApi.md#teamsTeamIdSchedulesDeleteRangePost) | **POST** /teams/{teamId}/schedules/deleteRange | Delete duty schedules in range |
| [**teamsTeamIdSchedulesDutyIdDelete**](DutiesApi.md#teamsTeamIdSchedulesDutyIdDelete) | **DELETE** /teams/{teamId}/schedules/{dutyId} | Delete a specific duty. |
| [**teamsTeamIdSchedulesGet**](DutiesApi.md#teamsTeamIdSchedulesGet) | **GET** /teams/{teamId}/schedules | Returns information about all duties that belong to the team. |
| [**teamsTeamIdSchedulesMultiplePost**](DutiesApi.md#teamsTeamIdSchedulesMultiplePost) | **POST** /teams/{teamId}/schedules/multiple | Save multiple schedules. It is possible to override existing schedules if you wish |
| [**teamsTeamIdSchedulesPost**](DutiesApi.md#teamsTeamIdSchedulesPost) | **POST** /teams/{teamId}/schedules | Create/Update given duty schedule. |
| [**teamsTeamIdSchedulesScheduleIdGet**](DutiesApi.md#teamsTeamIdSchedulesScheduleIdGet) | **GET** /teams/{teamId}/schedules/{scheduleId} | Returns information of the duty schedule with the specified Id. |


<a id="teamsTeamIdDutyReportsFileNameGet"></a>
# **teamsTeamIdDutyReportsFileNameGet**
> File teamsTeamIdDutyReportsFileNameGet(teamId, fileName)

Download duty report with a specific fileName

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DutiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    DutiesApi apiInstance = new DutiesApi(defaultClient);
    String teamId = "teamId_example"; // String | ID of team you want to download the duty report for.
    String fileName = "fileName_example"; // String | Filename of the csv to download.
    try {
      File result = apiInstance.teamsTeamIdDutyReportsFileNameGet(teamId, fileName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DutiesApi#teamsTeamIdDutyReportsFileNameGet");
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
| **teamId** | **String**| ID of team you want to download the duty report for. | |
| **fileName** | **String**| Filename of the csv to download. | |

### Return type

[**File**](File.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="teamsTeamIdDutyReportsGet"></a>
# **teamsTeamIdDutyReportsGet**
> List&lt;Object&gt; teamsTeamIdDutyReportsGet(teamId)

Get Information about downloadable reports

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DutiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    DutiesApi apiInstance = new DutiesApi(defaultClient);
    String teamId = "teamId_example"; // String | ID of team you want to get the duty report file infos for.
    try {
      List<Object> result = apiInstance.teamsTeamIdDutyReportsGet(teamId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DutiesApi#teamsTeamIdDutyReportsGet");
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
| **teamId** | **String**| ID of team you want to get the duty report file infos for. | |

### Return type

**List&lt;Object&gt;**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="teamsTeamIdDutysummaryGet"></a>
# **teamsTeamIdDutysummaryGet**
> TeamDutySummaryInfo teamsTeamIdDutysummaryGet(teamId, lastTwoDuties)

Get duty assistant info for a team

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DutiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    DutiesApi apiInstance = new DutiesApi(defaultClient);
    String teamId = "teamId_example"; // String | ID of the team the duty belongs to.
    Boolean lastTwoDuties = true; // Boolean | 
    try {
      TeamDutySummaryInfo result = apiInstance.teamsTeamIdDutysummaryGet(teamId, lastTwoDuties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DutiesApi#teamsTeamIdDutysummaryGet");
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
| **teamId** | **String**| ID of the team the duty belongs to. | |
| **lastTwoDuties** | **Boolean**|  | [optional] |

### Return type

[**TeamDutySummaryInfo**](TeamDutySummaryInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **500** | Server Error |  -  |

<a id="teamsTeamIdSchedulesDeleteRangePost"></a>
# **teamsTeamIdSchedulesDeleteRangePost**
> List&lt;ScheduleInfo&gt; teamsTeamIdSchedulesDeleteRangePost(teamId, deleteRangeInfo)

Delete duty schedules in range

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DutiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    DutiesApi apiInstance = new DutiesApi(defaultClient);
    String teamId = "teamId_example"; // String | Team ID you want to delete
    DeleteRangeInfo deleteRangeInfo = new DeleteRangeInfo(); // DeleteRangeInfo | Information with date range to delete from to
    try {
      List<ScheduleInfo> result = apiInstance.teamsTeamIdSchedulesDeleteRangePost(teamId, deleteRangeInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DutiesApi#teamsTeamIdSchedulesDeleteRangePost");
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
| **teamId** | **String**| Team ID you want to delete | |
| **deleteRangeInfo** | [**DeleteRangeInfo**](DeleteRangeInfo.md)| Information with date range to delete from to | [optional] |

### Return type

[**List&lt;ScheduleInfo&gt;**](ScheduleInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |
| **500** | Server Error |  -  |

<a id="teamsTeamIdSchedulesDutyIdDelete"></a>
# **teamsTeamIdSchedulesDutyIdDelete**
> teamsTeamIdSchedulesDutyIdDelete(teamId, dutyId)

Delete a specific duty.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DutiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    DutiesApi apiInstance = new DutiesApi(defaultClient);
    String teamId = "teamId_example"; // String | ID of the team the duty belongs to.
    String dutyId = "dutyId_example"; // String | ID of the duty to be deleted.
    try {
      apiInstance.teamsTeamIdSchedulesDutyIdDelete(teamId, dutyId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DutiesApi#teamsTeamIdSchedulesDutyIdDelete");
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
| **teamId** | **String**| ID of the team the duty belongs to. | |
| **dutyId** | **String**| ID of the duty to be deleted. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="teamsTeamIdSchedulesGet"></a>
# **teamsTeamIdSchedulesGet**
> List&lt;ScheduleInfo&gt; teamsTeamIdSchedulesGet(teamId, userId, minDate, limit)

Returns information about all duties that belong to the team.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DutiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    DutiesApi apiInstance = new DutiesApi(defaultClient);
    String teamId = "teamId_example"; // String | Id of the team the schedules user belongs to
    String userId = "userId_example"; // String | 
    OffsetDateTime minDate = OffsetDateTime.now(); // OffsetDateTime | 
    Integer limit = 56; // Integer | 
    try {
      List<ScheduleInfo> result = apiInstance.teamsTeamIdSchedulesGet(teamId, userId, minDate, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DutiesApi#teamsTeamIdSchedulesGet");
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
| **teamId** | **String**| Id of the team the schedules user belongs to | |
| **userId** | **String**|  | [optional] |
| **minDate** | **OffsetDateTime**|  | [optional] |
| **limit** | **Integer**|  | [optional] |

### Return type

[**List&lt;ScheduleInfo&gt;**](ScheduleInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="teamsTeamIdSchedulesMultiplePost"></a>
# **teamsTeamIdSchedulesMultiplePost**
> List&lt;ScheduleInfo&gt; teamsTeamIdSchedulesMultiplePost(teamId, overrideExisting, scheduleInfo)

Save multiple schedules. It is possible to override existing schedules if you wish

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DutiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    DutiesApi apiInstance = new DutiesApi(defaultClient);
    String teamId = "teamId_example"; // String | Team ID to set
    Boolean overrideExisting = true; // Boolean | Override or cut existing schedules if set to true.
    List<ScheduleInfo> scheduleInfo = Arrays.asList(); // List<ScheduleInfo> | List of schedules to save
    try {
      List<ScheduleInfo> result = apiInstance.teamsTeamIdSchedulesMultiplePost(teamId, overrideExisting, scheduleInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DutiesApi#teamsTeamIdSchedulesMultiplePost");
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
| **teamId** | **String**| Team ID to set | |
| **overrideExisting** | **Boolean**| Override or cut existing schedules if set to true. | [optional] |
| **scheduleInfo** | [**List&lt;ScheduleInfo&gt;**](ScheduleInfo.md)| List of schedules to save | [optional] |

### Return type

[**List&lt;ScheduleInfo&gt;**](ScheduleInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |
| **500** | Server Error |  -  |

<a id="teamsTeamIdSchedulesPost"></a>
# **teamsTeamIdSchedulesPost**
> ScheduleInfo teamsTeamIdSchedulesPost(teamId, scheduleInfo)

Create/Update given duty schedule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DutiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    DutiesApi apiInstance = new DutiesApi(defaultClient);
    String teamId = "teamId_example"; // String | Id of the team the duty is to be assigned to.
    ScheduleInfo scheduleInfo = new ScheduleInfo(); // ScheduleInfo | information about the duty schedule to be created
    try {
      ScheduleInfo result = apiInstance.teamsTeamIdSchedulesPost(teamId, scheduleInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DutiesApi#teamsTeamIdSchedulesPost");
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
| **teamId** | **String**| Id of the team the duty is to be assigned to. | |
| **scheduleInfo** | [**ScheduleInfo**](ScheduleInfo.md)| information about the duty schedule to be created | [optional] |

### Return type

[**ScheduleInfo**](ScheduleInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |
| **500** | Server Error |  -  |

<a id="teamsTeamIdSchedulesScheduleIdGet"></a>
# **teamsTeamIdSchedulesScheduleIdGet**
> ScheduleInfo teamsTeamIdSchedulesScheduleIdGet(teamId, scheduleId)

Returns information of the duty schedule with the specified Id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DutiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    DutiesApi apiInstance = new DutiesApi(defaultClient);
    String teamId = "teamId_example"; // String | Id of the team the duty belongs to
    String scheduleId = "scheduleId_example"; // String | Id of the requested duty schedule.
    try {
      ScheduleInfo result = apiInstance.teamsTeamIdSchedulesScheduleIdGet(teamId, scheduleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DutiesApi#teamsTeamIdSchedulesScheduleIdGet");
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
| **teamId** | **String**| Id of the team the duty belongs to | |
| **scheduleId** | **String**| Id of the requested duty schedule. | |

### Return type

[**ScheduleInfo**](ScheduleInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

