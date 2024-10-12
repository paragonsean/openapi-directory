# TimeEntryValueTypesApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**timeEntryValueTypesGet**](TimeEntryValueTypesApi.md#timeEntryValueTypesGet) | **GET** /time_entry_value_types | List possible time entry value types |
| [**timeEntryValueTypesTimeEntryValueTypeIdGet**](TimeEntryValueTypesApi.md#timeEntryValueTypesTimeEntryValueTypeIdGet) | **GET** /time_entry_value_types/{time_entry_value_type_id} | View time entry value type |


<a id="timeEntryValueTypesGet"></a>
# **timeEntryValueTypesGet**
> TimeEntryValueTypesGet200Response timeEntryValueTypesGet()

List possible time entry value types

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimeEntryValueTypesApi;

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

    TimeEntryValueTypesApi apiInstance = new TimeEntryValueTypesApi(defaultClient);
    try {
      TimeEntryValueTypesGet200Response result = apiInstance.timeEntryValueTypesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimeEntryValueTypesApi#timeEntryValueTypesGet");
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

[**TimeEntryValueTypesGet200Response**](TimeEntryValueTypesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="timeEntryValueTypesTimeEntryValueTypeIdGet"></a>
# **timeEntryValueTypesTimeEntryValueTypeIdGet**
> TimeEntryValueTypesTimeEntryValueTypeIdGet200Response timeEntryValueTypesTimeEntryValueTypeIdGet(timeEntryValueTypeId)

View time entry value type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimeEntryValueTypesApi;

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

    TimeEntryValueTypesApi apiInstance = new TimeEntryValueTypesApi(defaultClient);
    UUID timeEntryValueTypeId = UUID.randomUUID(); // UUID | 
    try {
      TimeEntryValueTypesTimeEntryValueTypeIdGet200Response result = apiInstance.timeEntryValueTypesTimeEntryValueTypeIdGet(timeEntryValueTypeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimeEntryValueTypesApi#timeEntryValueTypesTimeEntryValueTypeIdGet");
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
| **timeEntryValueTypeId** | **UUID**|  | |

### Return type

[**TimeEntryValueTypesTimeEntryValueTypeIdGet200Response**](TimeEntryValueTypesTimeEntryValueTypeIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

