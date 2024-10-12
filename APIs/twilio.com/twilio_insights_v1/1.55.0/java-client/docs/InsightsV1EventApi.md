# InsightsV1EventApi

All URIs are relative to *https://insights.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listEvent**](InsightsV1EventApi.md#listEvent) | **GET** /v1/Voice/{CallSid}/Events |  |


<a id="listEvent"></a>
# **listEvent**
> ListEventResponse listEvent(callSid, edge, pageSize, page, pageToken)



Get a list of Call Insight Events for a Call.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightsV1EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://insights.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    InsightsV1EventApi apiInstance = new InsightsV1EventApi(defaultClient);
    String callSid = "callSid_example"; // String | The unique SID identifier of the Call.
    EventEnumTwilioEdge edge = EventEnumTwilioEdge.fromValue("unknown_edge"); // EventEnumTwilioEdge | The Edge of this Event. One of `unknown_edge`, `carrier_edge`, `sip_edge`, `sdk_edge` or `client_edge`.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListEventResponse result = apiInstance.listEvent(callSid, edge, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightsV1EventApi#listEvent");
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
| **edge** | **EventEnumTwilioEdge**| The Edge of this Event. One of &#x60;unknown_edge&#x60;, &#x60;carrier_edge&#x60;, &#x60;sip_edge&#x60;, &#x60;sdk_edge&#x60; or &#x60;client_edge&#x60;. | [optional] [enum: unknown_edge, carrier_edge, sip_edge, sdk_edge, client_edge] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListEventResponse**](ListEventResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

