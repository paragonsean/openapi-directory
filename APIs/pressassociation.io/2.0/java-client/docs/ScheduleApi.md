# ScheduleApi

All URIs are relative to *https://tv.api.pressassociation.io/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listSchedule**](ScheduleApi.md#listSchedule) | **GET** /schedule | Schedule Collection |


<a id="listSchedule"></a>
# **listSchedule**
> Object listSchedule(channelId, start, end, aliases)

Schedule Collection

The schedule endpoint produces a linear TV schedule for a given channel and date range.   - The date range supplied must be no larger than 21 days.  - If no end data is passed the API will default to start date + 24 hours.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScheduleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tv.api.pressassociation.io/v2");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    ScheduleApi apiInstance = new ScheduleApi(defaultClient);
    String channelId = "channelId_example"; // String | The identifier for the selected channel.
    String start = "2015-05-05T00:00:00"; // String | The Start Date for the schedule.
    String end = "2015-05-06T00:00:00"; // String | The End Date for the schedule.
    Boolean aliases = true; // Boolean | Flag to display Legacy and Provider Ids.
    try {
      Object result = apiInstance.listSchedule(channelId, start, end, aliases);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScheduleApi#listSchedule");
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
| **channelId** | **String**| The identifier for the selected channel. | |
| **start** | **String**| The Start Date for the schedule. | [default to 2015-05-05T00:00:00] |
| **end** | **String**| The End Date for the schedule. | [optional] [default to 2015-05-06T00:00:00] |
| **aliases** | **Boolean**| Flag to display Legacy and Provider Ids. | [optional] [default to true] |

### Return type

**Object**

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

