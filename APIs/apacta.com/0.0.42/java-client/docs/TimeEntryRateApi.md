# TimeEntryRateApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**timeEntryRatesTimeEntryRateIdDelete**](TimeEntryRateApi.md#timeEntryRatesTimeEntryRateIdDelete) | **DELETE** /time_entry_rates/{time_entry_rate_id} | Delete time entry rate |


<a id="timeEntryRatesTimeEntryRateIdDelete"></a>
# **timeEntryRatesTimeEntryRateIdDelete**
> ClockingRecordsClockingRecordIdPut200Response timeEntryRatesTimeEntryRateIdDelete(timeEntryRateId)

Delete time entry rate

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimeEntryRateApi;

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

    TimeEntryRateApi apiInstance = new TimeEntryRateApi(defaultClient);
    UUID timeEntryRateId = UUID.randomUUID(); // UUID | 
    try {
      ClockingRecordsClockingRecordIdPut200Response result = apiInstance.timeEntryRatesTimeEntryRateIdDelete(timeEntryRateId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimeEntryRateApi#timeEntryRatesTimeEntryRateIdDelete");
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

