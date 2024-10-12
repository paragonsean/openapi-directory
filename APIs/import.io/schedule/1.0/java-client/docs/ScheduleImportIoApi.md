# ScheduleImportIoApi

All URIs are relative to *https://schedule.import.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**extractorExtractorIdDelete**](ScheduleImportIoApi.md#extractorExtractorIdDelete) | **DELETE** /extractor/{extractorId}/ | Delete an existing schedule |
| [**extractorExtractorIdGet**](ScheduleImportIoApi.md#extractorExtractorIdGet) | **GET** /extractor/{extractorId}/ | Get the schedule of a particular extractor |
| [**extractorGet**](ScheduleImportIoApi.md#extractorGet) | **GET** /extractor | Get the list of schedules for all your extractors |
| [**extractorPost**](ScheduleImportIoApi.md#extractorPost) | **POST** /extractor | Schedule and extractor to run at a specific time |


<a id="extractorExtractorIdDelete"></a>
# **extractorExtractorIdDelete**
> extractorExtractorIdDelete(extractorId)

Delete an existing schedule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScheduleImportIoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://schedule.import.io");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ScheduleImportIoApi apiInstance = new ScheduleImportIoApi(defaultClient);
    String extractorId = "extractorId_example"; // String | the id of the extractor with a schedule
    try {
      apiInstance.extractorExtractorIdDelete(extractorId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScheduleImportIoApi#extractorExtractorIdDelete");
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
| **extractorId** | **String**| the id of the extractor with a schedule | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Empty object |  -  |
| **401** | User doesn&#39;t have a valid session. |  -  |
| **403** | User is not allowed to delete this schedule. |  -  |
| **404** | Unable to find supplied extractor ID. |  -  |

<a id="extractorExtractorIdGet"></a>
# **extractorExtractorIdGet**
> Schedule extractorExtractorIdGet(extractorId)

Get the schedule of a particular extractor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScheduleImportIoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://schedule.import.io");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ScheduleImportIoApi apiInstance = new ScheduleImportIoApi(defaultClient);
    String extractorId = "extractorId_example"; // String | the id of the extractor with a schedule
    try {
      Schedule result = apiInstance.extractorExtractorIdGet(extractorId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScheduleImportIoApi#extractorExtractorIdGet");
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
| **extractorId** | **String**| the id of the extractor with a schedule | |

### Return type

[**Schedule**](Schedule.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | crawl run schedule |  -  |

<a id="extractorGet"></a>
# **extractorGet**
> Schedule extractorGet()

Get the list of schedules for all your extractors

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScheduleImportIoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://schedule.import.io");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ScheduleImportIoApi apiInstance = new ScheduleImportIoApi(defaultClient);
    try {
      Schedule result = apiInstance.extractorGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScheduleImportIoApi#extractorGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Schedule**](Schedule.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | array of crawl run schedules |  -  |
| **401** | User doesn&#39;t have a valid session. |  -  |
| **404** | Unable to find supplied extractor ID. |  -  |

<a id="extractorPost"></a>
# **extractorPost**
> Schedule extractorPost(scheduleRequestBody)

Schedule and extractor to run at a specific time

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScheduleImportIoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://schedule.import.io");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ScheduleImportIoApi apiInstance = new ScheduleImportIoApi(defaultClient);
    ScheduleRequest scheduleRequestBody = new ScheduleRequest(); // ScheduleRequest | Request body with the schema defined on the left. Interval is a cron string.
    try {
      Schedule result = apiInstance.extractorPost(scheduleRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScheduleImportIoApi#extractorPost");
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
| **scheduleRequestBody** | [**ScheduleRequest**](ScheduleRequest.md)| Request body with the schema defined on the left. Interval is a cron string. | |

### Return type

[**Schedule**](Schedule.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | crawl run schedule |  -  |
| **400** | Validation errors on the request input. |  -  |
| **401** | User doesn&#39;t own this extractor, or doesn&#39;t have a valid session. |  -  |
| **403** | User is not allowed to create schedule for this extractor. |  -  |
| **404** | Unable to find supplied extractor ID. |  -  |

