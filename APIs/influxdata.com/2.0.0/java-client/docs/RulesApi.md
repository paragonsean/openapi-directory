# RulesApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNotificationRulesIDQuery**](RulesApi.md#getNotificationRulesIDQuery) | **GET** /notificationRules/{ruleID}/query | Retrieve a notification rule query |


<a id="getNotificationRulesIDQuery"></a>
# **getNotificationRulesIDQuery**
> FluxResponse getNotificationRulesIDQuery(ruleID, zapTraceSpan)

Retrieve a notification rule query

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    RulesApi apiInstance = new RulesApi(defaultClient);
    String ruleID = "ruleID_example"; // String | The notification rule ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      FluxResponse result = apiInstance.getNotificationRulesIDQuery(ruleID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RulesApi#getNotificationRulesIDQuery");
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
| **ruleID** | **String**| The notification rule ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**FluxResponse**](FluxResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The notification rule query requested |  -  |
| **400** | Invalid request |  -  |
| **404** | Notification rule not found |  -  |
| **0** | Unexpected error |  -  |

