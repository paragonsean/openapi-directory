# TimeEntriesApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**timeEntriesGet**](TimeEntriesApi.md#timeEntriesGet) | **GET** /time_entries | List time entries |
| [**timeEntriesPost**](TimeEntriesApi.md#timeEntriesPost) | **POST** /time_entries | Add new time entry |
| [**timeEntriesTimeEntryIdDelete**](TimeEntriesApi.md#timeEntriesTimeEntryIdDelete) | **DELETE** /time_entries/{time_entry_id} | Delete time entry |
| [**timeEntriesTimeEntryIdGet**](TimeEntriesApi.md#timeEntriesTimeEntryIdGet) | **GET** /time_entries/{time_entry_id} | View time entry |
| [**timeEntriesTimeEntryIdPut**](TimeEntriesApi.md#timeEntriesTimeEntryIdPut) | **PUT** /time_entries/{time_entry_id} | Edit time entry |


<a id="timeEntriesGet"></a>
# **timeEntriesGet**
> TimeEntriesGet200Response timeEntriesGet(userId, formId, projectId, gtFromTime, ltFromTime, gtToTime, ltToTime, ltSum, gtSum)

List time entries

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimeEntriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    TimeEntriesApi apiInstance = new TimeEntriesApi(defaultClient);
    String userId = "userId_example"; // String | 
    String formId = "formId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    String gtFromTime = "gtFromTime_example"; // String | 
    String ltFromTime = "ltFromTime_example"; // String | 
    String gtToTime = "gtToTime_example"; // String | 
    String ltToTime = "ltToTime_example"; // String | 
    String ltSum = "ltSum_example"; // String | 
    String gtSum = "gtSum_example"; // String | 
    try {
      TimeEntriesGet200Response result = apiInstance.timeEntriesGet(userId, formId, projectId, gtFromTime, ltFromTime, gtToTime, ltToTime, ltSum, gtSum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimeEntriesApi#timeEntriesGet");
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
| **userId** | **String**|  | [optional] |
| **formId** | **String**|  | [optional] |
| **projectId** | **String**|  | [optional] |
| **gtFromTime** | **String**|  | [optional] |
| **ltFromTime** | **String**|  | [optional] |
| **gtToTime** | **String**|  | [optional] |
| **ltToTime** | **String**|  | [optional] |
| **ltSum** | **String**|  | [optional] |
| **gtSum** | **String**|  | [optional] |

### Return type

[**TimeEntriesGet200Response**](TimeEntriesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="timeEntriesPost"></a>
# **timeEntriesPost**
> ClockingRecordsPost201Response timeEntriesPost(timeEntriesPostRequest)

Add new time entry

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimeEntriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    TimeEntriesApi apiInstance = new TimeEntriesApi(defaultClient);
    TimeEntriesPostRequest timeEntriesPostRequest = new TimeEntriesPostRequest(); // TimeEntriesPostRequest | 
    try {
      ClockingRecordsPost201Response result = apiInstance.timeEntriesPost(timeEntriesPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimeEntriesApi#timeEntriesPost");
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
| **timeEntriesPostRequest** | [**TimeEntriesPostRequest**](TimeEntriesPostRequest.md)|  | [optional] |

### Return type

[**ClockingRecordsPost201Response**](ClockingRecordsPost201Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK |  -  |
| **422** | Validation error |  -  |

<a id="timeEntriesTimeEntryIdDelete"></a>
# **timeEntriesTimeEntryIdDelete**
> ClockingRecordsClockingRecordIdPut200Response timeEntriesTimeEntryIdDelete(timeEntryId)

Delete time entry

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimeEntriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    TimeEntriesApi apiInstance = new TimeEntriesApi(defaultClient);
    UUID timeEntryId = UUID.randomUUID(); // UUID | 
    try {
      ClockingRecordsClockingRecordIdPut200Response result = apiInstance.timeEntriesTimeEntryIdDelete(timeEntryId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimeEntriesApi#timeEntriesTimeEntryIdDelete");
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
| **timeEntryId** | **UUID**|  | |

### Return type

[**ClockingRecordsClockingRecordIdPut200Response**](ClockingRecordsClockingRecordIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="timeEntriesTimeEntryIdGet"></a>
# **timeEntriesTimeEntryIdGet**
> TimeEntriesTimeEntryIdGet200Response timeEntriesTimeEntryIdGet(timeEntryId)

View time entry

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimeEntriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    TimeEntriesApi apiInstance = new TimeEntriesApi(defaultClient);
    UUID timeEntryId = UUID.randomUUID(); // UUID | 
    try {
      TimeEntriesTimeEntryIdGet200Response result = apiInstance.timeEntriesTimeEntryIdGet(timeEntryId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimeEntriesApi#timeEntriesTimeEntryIdGet");
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
| **timeEntryId** | **UUID**|  | |

### Return type

[**TimeEntriesTimeEntryIdGet200Response**](TimeEntriesTimeEntryIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="timeEntriesTimeEntryIdPut"></a>
# **timeEntriesTimeEntryIdPut**
> ClockingRecordsClockingRecordIdPut200Response timeEntriesTimeEntryIdPut(timeEntryId)

Edit time entry

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimeEntriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    TimeEntriesApi apiInstance = new TimeEntriesApi(defaultClient);
    UUID timeEntryId = UUID.randomUUID(); // UUID | 
    try {
      ClockingRecordsClockingRecordIdPut200Response result = apiInstance.timeEntriesTimeEntryIdPut(timeEntryId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimeEntriesApi#timeEntriesTimeEntryIdPut");
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
| **timeEntryId** | **UUID**|  | |

### Return type

[**ClockingRecordsClockingRecordIdPut200Response**](ClockingRecordsClockingRecordIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

