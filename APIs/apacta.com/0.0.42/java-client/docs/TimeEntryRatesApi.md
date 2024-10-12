# TimeEntryRatesApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**timeEntryRatesGet**](TimeEntryRatesApi.md#timeEntryRatesGet) | **GET** /time_entry_rates | List time entry rates |
| [**timeEntryRatesPost**](TimeEntryRatesApi.md#timeEntryRatesPost) | **POST** /time_entry_rates | Add new time entry rate |
| [**timeEntryRatesTimeEntryRateIdGet**](TimeEntryRatesApi.md#timeEntryRatesTimeEntryRateIdGet) | **GET** /time_entry_rates/{time_entry_rate_id} | View time entry rate |
| [**timeEntryRatesTimeEntryRateIdPut**](TimeEntryRatesApi.md#timeEntryRatesTimeEntryRateIdPut) | **PUT** /time_entry_rates/{time_entry_rate_id} | Edit time entry rate |


<a id="timeEntryRatesGet"></a>
# **timeEntryRatesGet**
> TimeEntryRatesGet200Response timeEntryRatesGet()

List time entry rates

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimeEntryRatesApi;

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

    TimeEntryRatesApi apiInstance = new TimeEntryRatesApi(defaultClient);
    try {
      TimeEntryRatesGet200Response result = apiInstance.timeEntryRatesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimeEntryRatesApi#timeEntryRatesGet");
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

[**TimeEntryRatesGet200Response**](TimeEntryRatesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="timeEntryRatesPost"></a>
# **timeEntryRatesPost**
> ClockingRecordsPost201Response timeEntryRatesPost(timeEntriesPostRequest)

Add new time entry rate

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimeEntryRatesApi;

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

    TimeEntryRatesApi apiInstance = new TimeEntryRatesApi(defaultClient);
    TimeEntriesPostRequest timeEntriesPostRequest = new TimeEntriesPostRequest(); // TimeEntriesPostRequest | 
    try {
      ClockingRecordsPost201Response result = apiInstance.timeEntryRatesPost(timeEntriesPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimeEntryRatesApi#timeEntryRatesPost");
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

<a id="timeEntryRatesTimeEntryRateIdGet"></a>
# **timeEntryRatesTimeEntryRateIdGet**
> TimeEntryRatesTimeEntryRateIdGet200Response timeEntryRatesTimeEntryRateIdGet(timeEntryRateId)

View time entry rate

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimeEntryRatesApi;

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

    TimeEntryRatesApi apiInstance = new TimeEntryRatesApi(defaultClient);
    UUID timeEntryRateId = UUID.randomUUID(); // UUID | 
    try {
      TimeEntryRatesTimeEntryRateIdGet200Response result = apiInstance.timeEntryRatesTimeEntryRateIdGet(timeEntryRateId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimeEntryRatesApi#timeEntryRatesTimeEntryRateIdGet");
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
| **timeEntryRateId** | **UUID**|  | |

### Return type

[**TimeEntryRatesTimeEntryRateIdGet200Response**](TimeEntryRatesTimeEntryRateIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="timeEntryRatesTimeEntryRateIdPut"></a>
# **timeEntryRatesTimeEntryRateIdPut**
> ClockingRecordsClockingRecordIdPut200Response timeEntryRatesTimeEntryRateIdPut(timeEntryRateId)

Edit time entry rate

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimeEntryRatesApi;

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

    TimeEntryRatesApi apiInstance = new TimeEntryRatesApi(defaultClient);
    UUID timeEntryRateId = UUID.randomUUID(); // UUID | 
    try {
      ClockingRecordsClockingRecordIdPut200Response result = apiInstance.timeEntryRatesTimeEntryRateIdPut(timeEntryRateId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimeEntryRatesApi#timeEntryRatesTimeEntryRateIdPut");
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
| **timeEntryRateId** | **UUID**|  | |

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

