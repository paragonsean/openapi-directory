# TimeEntryUnitTypesApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**timeEntryUnitTypesGet**](TimeEntryUnitTypesApi.md#timeEntryUnitTypesGet) | **GET** /time_entry_unit_types | List possible time entry unit types |
| [**timeEntryUnitTypesTimeEntryUnitTypeIdGet**](TimeEntryUnitTypesApi.md#timeEntryUnitTypesTimeEntryUnitTypeIdGet) | **GET** /time_entry_unit_types/{time_entry_unit_type_id} | View time entry unit type |


<a id="timeEntryUnitTypesGet"></a>
# **timeEntryUnitTypesGet**
> TimeEntryUnitTypesGet200Response timeEntryUnitTypesGet()

List possible time entry unit types

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimeEntryUnitTypesApi;

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

    TimeEntryUnitTypesApi apiInstance = new TimeEntryUnitTypesApi(defaultClient);
    try {
      TimeEntryUnitTypesGet200Response result = apiInstance.timeEntryUnitTypesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimeEntryUnitTypesApi#timeEntryUnitTypesGet");
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

[**TimeEntryUnitTypesGet200Response**](TimeEntryUnitTypesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="timeEntryUnitTypesTimeEntryUnitTypeIdGet"></a>
# **timeEntryUnitTypesTimeEntryUnitTypeIdGet**
> TimeEntryUnitTypesTimeEntryUnitTypeIdGet200Response timeEntryUnitTypesTimeEntryUnitTypeIdGet(timeEntryUnitTypeId)

View time entry unit type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimeEntryUnitTypesApi;

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

    TimeEntryUnitTypesApi apiInstance = new TimeEntryUnitTypesApi(defaultClient);
    UUID timeEntryUnitTypeId = UUID.randomUUID(); // UUID | 
    try {
      TimeEntryUnitTypesTimeEntryUnitTypeIdGet200Response result = apiInstance.timeEntryUnitTypesTimeEntryUnitTypeIdGet(timeEntryUnitTypeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimeEntryUnitTypesApi#timeEntryUnitTypesTimeEntryUnitTypeIdGet");
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
| **timeEntryUnitTypeId** | **UUID**|  | |

### Return type

[**TimeEntryUnitTypesTimeEntryUnitTypeIdGet200Response**](TimeEntryUnitTypesTimeEntryUnitTypeIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

