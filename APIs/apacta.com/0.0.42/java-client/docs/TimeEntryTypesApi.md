# TimeEntryTypesApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bulkActivateTimeEntryTypes**](TimeEntryTypesApi.md#bulkActivateTimeEntryTypes) | **POST** /time_entry_types/bulkActivate | Bulk activate time entry types |
| [**bulkDeactivateTimeEntryTypes**](TimeEntryTypesApi.md#bulkDeactivateTimeEntryTypes) | **POST** /time_entry_types/bulkDeactivate | Bulk deactivate time entry types |
| [**bulkDeleteTimeEntryTypes**](TimeEntryTypesApi.md#bulkDeleteTimeEntryTypes) | **DELETE** /time_entry_types/bulkDelete | Bulk delete time entry types |
| [**timeEntryTypesGet**](TimeEntryTypesApi.md#timeEntryTypesGet) | **GET** /time_entry_types | List time entries types |
| [**timeEntryTypesPost**](TimeEntryTypesApi.md#timeEntryTypesPost) | **POST** /time_entry_types | Add new time entry type |
| [**timeEntryTypesTimeEntryTypeIdDelete**](TimeEntryTypesApi.md#timeEntryTypesTimeEntryTypeIdDelete) | **DELETE** /time_entry_types/{time_entry_type_id} | Delete time entry type |
| [**timeEntryTypesTimeEntryTypeIdGet**](TimeEntryTypesApi.md#timeEntryTypesTimeEntryTypeIdGet) | **GET** /time_entry_types/{time_entry_type_id} | View time entry type |
| [**timeEntryTypesTimeEntryTypeIdPut**](TimeEntryTypesApi.md#timeEntryTypesTimeEntryTypeIdPut) | **PUT** /time_entry_types/{time_entry_type_id} | Edit time entry type |


<a id="bulkActivateTimeEntryTypes"></a>
# **bulkActivateTimeEntryTypes**
> EmptySuccessResponse bulkActivateTimeEntryTypes(bulkActionRequestBody)

Bulk activate time entry types

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimeEntryTypesApi;

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

    TimeEntryTypesApi apiInstance = new TimeEntryTypesApi(defaultClient);
    BulkActionRequestBody bulkActionRequestBody = new BulkActionRequestBody(); // BulkActionRequestBody | Time entry types ids
    try {
      EmptySuccessResponse result = apiInstance.bulkActivateTimeEntryTypes(bulkActionRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimeEntryTypesApi#bulkActivateTimeEntryTypes");
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
| **bulkActionRequestBody** | [**BulkActionRequestBody**](BulkActionRequestBody.md)| Time entry types ids | |

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |

<a id="bulkDeactivateTimeEntryTypes"></a>
# **bulkDeactivateTimeEntryTypes**
> EmptySuccessResponse bulkDeactivateTimeEntryTypes(bulkActionRequestBody)

Bulk deactivate time entry types

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimeEntryTypesApi;

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

    TimeEntryTypesApi apiInstance = new TimeEntryTypesApi(defaultClient);
    BulkActionRequestBody bulkActionRequestBody = new BulkActionRequestBody(); // BulkActionRequestBody | Time entry types ids
    try {
      EmptySuccessResponse result = apiInstance.bulkDeactivateTimeEntryTypes(bulkActionRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimeEntryTypesApi#bulkDeactivateTimeEntryTypes");
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
| **bulkActionRequestBody** | [**BulkActionRequestBody**](BulkActionRequestBody.md)| Time entry types ids | |

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |

<a id="bulkDeleteTimeEntryTypes"></a>
# **bulkDeleteTimeEntryTypes**
> EmptySuccessResponse bulkDeleteTimeEntryTypes(bulkActionRequestBody)

Bulk delete time entry types

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimeEntryTypesApi;

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

    TimeEntryTypesApi apiInstance = new TimeEntryTypesApi(defaultClient);
    BulkActionRequestBody bulkActionRequestBody = new BulkActionRequestBody(); // BulkActionRequestBody | Time entry types ids
    try {
      EmptySuccessResponse result = apiInstance.bulkDeleteTimeEntryTypes(bulkActionRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimeEntryTypesApi#bulkDeleteTimeEntryTypes");
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
| **bulkActionRequestBody** | [**BulkActionRequestBody**](BulkActionRequestBody.md)| Time entry types ids | |

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |

<a id="timeEntryTypesGet"></a>
# **timeEntryTypesGet**
> TimeEntryTypesGet200Response timeEntryTypesGet()

List time entries types

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimeEntryTypesApi;

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

    TimeEntryTypesApi apiInstance = new TimeEntryTypesApi(defaultClient);
    try {
      TimeEntryTypesGet200Response result = apiInstance.timeEntryTypesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimeEntryTypesApi#timeEntryTypesGet");
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

[**TimeEntryTypesGet200Response**](TimeEntryTypesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="timeEntryTypesPost"></a>
# **timeEntryTypesPost**
> ClockingRecordsPost201Response timeEntryTypesPost(timeEntryTypesPostRequest)

Add new time entry type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimeEntryTypesApi;

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

    TimeEntryTypesApi apiInstance = new TimeEntryTypesApi(defaultClient);
    TimeEntryTypesPostRequest timeEntryTypesPostRequest = new TimeEntryTypesPostRequest(); // TimeEntryTypesPostRequest | 
    try {
      ClockingRecordsPost201Response result = apiInstance.timeEntryTypesPost(timeEntryTypesPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimeEntryTypesApi#timeEntryTypesPost");
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
| **timeEntryTypesPostRequest** | [**TimeEntryTypesPostRequest**](TimeEntryTypesPostRequest.md)|  | [optional] |

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

<a id="timeEntryTypesTimeEntryTypeIdDelete"></a>
# **timeEntryTypesTimeEntryTypeIdDelete**
> ClockingRecordsClockingRecordIdPut200Response timeEntryTypesTimeEntryTypeIdDelete(timeEntryTypeId)

Delete time entry type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimeEntryTypesApi;

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

    TimeEntryTypesApi apiInstance = new TimeEntryTypesApi(defaultClient);
    UUID timeEntryTypeId = UUID.randomUUID(); // UUID | 
    try {
      ClockingRecordsClockingRecordIdPut200Response result = apiInstance.timeEntryTypesTimeEntryTypeIdDelete(timeEntryTypeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimeEntryTypesApi#timeEntryTypesTimeEntryTypeIdDelete");
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
| **timeEntryTypeId** | **UUID**|  | |

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

<a id="timeEntryTypesTimeEntryTypeIdGet"></a>
# **timeEntryTypesTimeEntryTypeIdGet**
> TimeEntryTypesTimeEntryTypeIdGet200Response timeEntryTypesTimeEntryTypeIdGet(timeEntryTypeId)

View time entry type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimeEntryTypesApi;

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

    TimeEntryTypesApi apiInstance = new TimeEntryTypesApi(defaultClient);
    UUID timeEntryTypeId = UUID.randomUUID(); // UUID | 
    try {
      TimeEntryTypesTimeEntryTypeIdGet200Response result = apiInstance.timeEntryTypesTimeEntryTypeIdGet(timeEntryTypeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimeEntryTypesApi#timeEntryTypesTimeEntryTypeIdGet");
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
| **timeEntryTypeId** | **UUID**|  | |

### Return type

[**TimeEntryTypesTimeEntryTypeIdGet200Response**](TimeEntryTypesTimeEntryTypeIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="timeEntryTypesTimeEntryTypeIdPut"></a>
# **timeEntryTypesTimeEntryTypeIdPut**
> ClockingRecordsClockingRecordIdPut200Response timeEntryTypesTimeEntryTypeIdPut(timeEntryTypeId)

Edit time entry type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimeEntryTypesApi;

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

    TimeEntryTypesApi apiInstance = new TimeEntryTypesApi(defaultClient);
    UUID timeEntryTypeId = UUID.randomUUID(); // UUID | 
    try {
      ClockingRecordsClockingRecordIdPut200Response result = apiInstance.timeEntryTypesTimeEntryTypeIdPut(timeEntryTypeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimeEntryTypesApi#timeEntryTypesTimeEntryTypeIdPut");
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
| **timeEntryTypeId** | **UUID**|  | |

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

