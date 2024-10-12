# TimeEntryIntervalsApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**timeEntryIntervalsGet**](TimeEntryIntervalsApi.md#timeEntryIntervalsGet) | **GET** /time_entry_intervals | List possible time entry intervals |
| [**timeEntryIntervalsTimeEntryIntervalIdGet**](TimeEntryIntervalsApi.md#timeEntryIntervalsTimeEntryIntervalIdGet) | **GET** /time_entry_intervals/{time_entry_interval_id} | View time entry interval |


<a id="timeEntryIntervalsGet"></a>
# **timeEntryIntervalsGet**
> TimeEntryIntervalsGet200Response timeEntryIntervalsGet()

List possible time entry intervals

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimeEntryIntervalsApi;

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

    TimeEntryIntervalsApi apiInstance = new TimeEntryIntervalsApi(defaultClient);
    try {
      TimeEntryIntervalsGet200Response result = apiInstance.timeEntryIntervalsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimeEntryIntervalsApi#timeEntryIntervalsGet");
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

[**TimeEntryIntervalsGet200Response**](TimeEntryIntervalsGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="timeEntryIntervalsTimeEntryIntervalIdGet"></a>
# **timeEntryIntervalsTimeEntryIntervalIdGet**
> TimeEntryIntervalsTimeEntryIntervalIdGet200Response timeEntryIntervalsTimeEntryIntervalIdGet(timeEntryIntervalId)

View time entry interval

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimeEntryIntervalsApi;

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

    TimeEntryIntervalsApi apiInstance = new TimeEntryIntervalsApi(defaultClient);
    UUID timeEntryIntervalId = UUID.randomUUID(); // UUID | 
    try {
      TimeEntryIntervalsTimeEntryIntervalIdGet200Response result = apiInstance.timeEntryIntervalsTimeEntryIntervalIdGet(timeEntryIntervalId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimeEntryIntervalsApi#timeEntryIntervalsTimeEntryIntervalIdGet");
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
| **timeEntryIntervalId** | **UUID**|  | |

### Return type

[**TimeEntryIntervalsTimeEntryIntervalIdGet200Response**](TimeEntryIntervalsTimeEntryIntervalIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

