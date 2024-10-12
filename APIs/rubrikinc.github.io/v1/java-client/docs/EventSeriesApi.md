# EventSeriesApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**queryEventSeriesByIdV1**](EventSeriesApi.md#queryEventSeriesByIdV1) | **GET** /event_series/{id} | Get all events and relevant information associated with an event series ID |


<a id="queryEventSeriesByIdV1"></a>
# **queryEventSeriesByIdV1**
> EventSeriesSummaryV1 queryEventSeriesByIdV1(id)

Get all events and relevant information associated with an event series ID

Gets all events, event series, SLA Domain, and object information that is associated with a specified event series ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventSeriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    EventSeriesApi apiInstance = new EventSeriesApi(defaultClient);
    String id = "id_example"; // String | The ID of the event series.
    try {
      EventSeriesSummaryV1 result = apiInstance.queryEventSeriesByIdV1(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventSeriesApi#queryEventSeriesByIdV1");
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
| **id** | **String**| The ID of the event series. | |

### Return type

[**EventSeriesSummaryV1**](EventSeriesSummaryV1.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the list of events by event series ID and a summary of the event series. |  -  |

