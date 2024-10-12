# FlexV1InsightsSegmentsApi

All URIs are relative to *https://flex-api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listInsightsSegments**](FlexV1InsightsSegmentsApi.md#listInsightsSegments) | **GET** /v1/Insights/Segments |  |


<a id="listInsightsSegments"></a>
# **listInsightsSegments**
> ListInsightsSegmentsResponse listInsightsSegments(authorization, segmentId, reservationId, pageSize, page, pageToken)



To get segments for given reservation Ids

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1InsightsSegmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1InsightsSegmentsApi apiInstance = new FlexV1InsightsSegmentsApi(defaultClient);
    String authorization = "authorization_example"; // String | The Authorization HTTP request header
    String segmentId = "segmentId_example"; // String | To unique id of the segment
    List<String> reservationId = Arrays.asList(); // List<String> | The list of reservation Ids
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListInsightsSegmentsResponse result = apiInstance.listInsightsSegments(authorization, segmentId, reservationId, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1InsightsSegmentsApi#listInsightsSegments");
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
| **authorization** | **String**| The Authorization HTTP request header | [optional] |
| **segmentId** | **String**| To unique id of the segment | [optional] |
| **reservationId** | [**List&lt;String&gt;**](String.md)| The list of reservation Ids | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListInsightsSegmentsResponse**](ListInsightsSegmentsResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

