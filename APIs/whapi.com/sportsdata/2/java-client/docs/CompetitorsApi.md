# CompetitorsApi

All URIs are relative to *https://sandbox.whapi.com/v2/sportsdata*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getEventCompetitors**](CompetitorsApi.md#getEventCompetitors) | **GET** /events/{eventId}/competitors | Retrieves competitors for a single event by ID. |


<a id="getEventCompetitors"></a>
# **getEventCompetitors**
> EventCompetitorsWrapper getEventCompetitors(apiKey, eventId, fields, include, exclude)

Retrieves competitors for a single event by ID.

Retrieves competitors for a single event by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompetitorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox.whapi.com/v2/sportsdata");

    CompetitorsApi apiInstance = new CompetitorsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | Your API Key available from your developer portal
    String eventId = "eventId_example"; // String | The event ID to retrieve information for.
    List<String> fields = Arrays.asList(); // List<String> | Specify an absolute field list to return (Comma-Separated List)
    List<String> include = Arrays.asList(); // List<String> | Specify fields in addition to the default to return (Comma-Separated List)
    List<String> exclude = Arrays.asList(); // List<String> | Specify fields from the default to exclude (Comma-Separated List)
    try {
      EventCompetitorsWrapper result = apiInstance.getEventCompetitors(apiKey, eventId, fields, include, exclude);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompetitorsApi#getEventCompetitors");
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
| **apiKey** | **String**| Your API Key available from your developer portal | |
| **eventId** | **String**| The event ID to retrieve information for. | |
| **fields** | [**List&lt;String&gt;**](String.md)| Specify an absolute field list to return (Comma-Separated List) | [optional] |
| **include** | [**List&lt;String&gt;**](String.md)| Specify fields in addition to the default to return (Comma-Separated List) | [optional] |
| **exclude** | [**List&lt;String&gt;**](String.md)| Specify fields from the default to exclude (Comma-Separated List) | [optional] |

### Return type

[**EventCompetitorsWrapper**](EventCompetitorsWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Incorrect or Missing Parameter |  -  |
| **404** | No data found for request |  -  |

