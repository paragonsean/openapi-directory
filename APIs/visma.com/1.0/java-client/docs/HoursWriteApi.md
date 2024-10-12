# HoursWriteApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**timeEntriesPatchTimeEntry**](HoursWriteApi.md#timeEntriesPatchTimeEntry) | **PATCH** /v1/timeentries/{guid} | Update (Patch) a time entry or a part of it. |
| [**timeEntriesPostTimeEntry**](HoursWriteApi.md#timeEntriesPostTimeEntry) | **POST** /v1/timeentries | Insert a time entry. |
| [**workHoursPatchWorkHour**](HoursWriteApi.md#workHoursPatchWorkHour) | **PATCH** /v1/workhours/{guid} | Update (Patch) a work hour or a part of it |
| [**workHoursPostWorkHour**](HoursWriteApi.md#workHoursPostWorkHour) | **POST** /v1/workhours | Insert a work hour |


<a id="timeEntriesPatchTimeEntry"></a>
# **timeEntriesPatchTimeEntry**
> List&lt;TimeEntryModel&gt; timeEntriesPatchTimeEntry(guid, patchOperation)

Update (Patch) a time entry or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HoursWriteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    HoursWriteApi apiInstance = new HoursWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the time entry.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON Patch document of TimeEntryModel.
    try {
      List<TimeEntryModel> result = apiInstance.timeEntriesPatchTimeEntry(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HoursWriteApi#timeEntriesPatchTimeEntry");
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
| **guid** | **String**| ID of the time entry. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON Patch document of TimeEntryModel. | [optional] |

### Return type

[**List&lt;TimeEntryModel&gt;**](TimeEntryModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated time entries. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="timeEntriesPostTimeEntry"></a>
# **timeEntriesPostTimeEntry**
> List&lt;TimeEntryModel&gt; timeEntriesPostTimeEntry(timeEntryModel)

Insert a time entry.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HoursWriteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    HoursWriteApi apiInstance = new HoursWriteApi(defaultClient);
    TimeEntryModel timeEntryModel = new TimeEntryModel(); // TimeEntryModel | TimeEntryModel.
    try {
      List<TimeEntryModel> result = apiInstance.timeEntriesPostTimeEntry(timeEntryModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HoursWriteApi#timeEntriesPostTimeEntry");
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
| **timeEntryModel** | [**TimeEntryModel**](TimeEntryModel.md)| TimeEntryModel. | [optional] |

### Return type

[**List&lt;TimeEntryModel&gt;**](TimeEntryModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created time entry. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="workHoursPatchWorkHour"></a>
# **workHoursPatchWorkHour**
> List&lt;WorkHourOutputModel&gt; workHoursPatchWorkHour(guid, patchOperation)

Update (Patch) a work hour or a part of it

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HoursWriteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    HoursWriteApi apiInstance = new HoursWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the work hour. Can also be comma separate list of IDs to patch multiple work hours with one call. When multiple IDs are given, returns model which has list of succeeded work hours and list of errors.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON Patch document of WorkHourInputModel
    try {
      List<WorkHourOutputModel> result = apiInstance.workHoursPatchWorkHour(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HoursWriteApi#workHoursPatchWorkHour");
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
| **guid** | **String**| ID of the work hour. Can also be comma separate list of IDs to patch multiple work hours with one call. When multiple IDs are given, returns model which has list of succeeded work hours and list of errors. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON Patch document of WorkHourInputModel | [optional] |

### Return type

[**List&lt;WorkHourOutputModel&gt;**](WorkHourOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated work hours |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="workHoursPostWorkHour"></a>
# **workHoursPostWorkHour**
> WorkHourOutputModel workHoursPostWorkHour(workHourInputModel)

Insert a work hour

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HoursWriteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    HoursWriteApi apiInstance = new HoursWriteApi(defaultClient);
    WorkHourInputModel workHourInputModel = new WorkHourInputModel(); // WorkHourInputModel | WorkHourInputModel
    try {
      WorkHourOutputModel result = apiInstance.workHoursPostWorkHour(workHourInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HoursWriteApi#workHoursPostWorkHour");
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
| **workHourInputModel** | [**WorkHourInputModel**](WorkHourInputModel.md)| WorkHourInputModel | [optional] |

### Return type

[**WorkHourOutputModel**](WorkHourOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created work hour |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

