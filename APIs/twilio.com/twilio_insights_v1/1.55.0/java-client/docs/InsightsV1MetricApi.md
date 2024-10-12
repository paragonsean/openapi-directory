# InsightsV1MetricApi

All URIs are relative to *https://insights.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listMetric**](InsightsV1MetricApi.md#listMetric) | **GET** /v1/Voice/{CallSid}/Metrics |  |


<a id="listMetric"></a>
# **listMetric**
> ListMetricResponse listMetric(callSid, edge, direction, pageSize, page, pageToken)



Get a list of Call Metrics for a Call.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightsV1MetricApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://insights.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    InsightsV1MetricApi apiInstance = new InsightsV1MetricApi(defaultClient);
    String callSid = "callSid_example"; // String | The unique SID identifier of the Call.
    MetricEnumTwilioEdge edge = MetricEnumTwilioEdge.fromValue("unknown_edge"); // MetricEnumTwilioEdge | The Edge of this Metric. One of `unknown_edge`, `carrier_edge`, `sip_edge`, `sdk_edge` or `client_edge`.
    MetricEnumStreamDirection direction = MetricEnumStreamDirection.fromValue("unknown"); // MetricEnumStreamDirection | The Direction of this Metric. One of `unknown`, `inbound`, `outbound` or `both`.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListMetricResponse result = apiInstance.listMetric(callSid, edge, direction, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightsV1MetricApi#listMetric");
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
| **callSid** | **String**| The unique SID identifier of the Call. | |
| **edge** | **MetricEnumTwilioEdge**| The Edge of this Metric. One of &#x60;unknown_edge&#x60;, &#x60;carrier_edge&#x60;, &#x60;sip_edge&#x60;, &#x60;sdk_edge&#x60; or &#x60;client_edge&#x60;. | [optional] [enum: unknown_edge, carrier_edge, sip_edge, sdk_edge, client_edge] |
| **direction** | **MetricEnumStreamDirection**| The Direction of this Metric. One of &#x60;unknown&#x60;, &#x60;inbound&#x60;, &#x60;outbound&#x60; or &#x60;both&#x60;. | [optional] [enum: unknown, inbound, outbound, both] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListMetricResponse**](ListMetricResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

