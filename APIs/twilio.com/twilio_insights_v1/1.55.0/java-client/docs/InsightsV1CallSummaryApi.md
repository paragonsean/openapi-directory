# InsightsV1CallSummaryApi

All URIs are relative to *https://insights.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchSummary**](InsightsV1CallSummaryApi.md#fetchSummary) | **GET** /v1/Voice/{CallSid}/Summary |  |


<a id="fetchSummary"></a>
# **fetchSummary**
> InsightsV1CallSummary fetchSummary(callSid, processingState)



Get a specific Call Summary.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightsV1CallSummaryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://insights.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    InsightsV1CallSummaryApi apiInstance = new InsightsV1CallSummaryApi(defaultClient);
    String callSid = "callSid_example"; // String | The unique SID identifier of the Call.
    SummaryEnumProcessingState processingState = SummaryEnumProcessingState.fromValue("complete"); // SummaryEnumProcessingState | The Processing State of this Call Summary. One of `complete`, `partial` or `all`.
    try {
      InsightsV1CallSummary result = apiInstance.fetchSummary(callSid, processingState);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightsV1CallSummaryApi#fetchSummary");
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
| **processingState** | **SummaryEnumProcessingState**| The Processing State of this Call Summary. One of &#x60;complete&#x60;, &#x60;partial&#x60; or &#x60;all&#x60;. | [optional] [enum: complete, partial] |

### Return type

[**InsightsV1CallSummary**](InsightsV1CallSummary.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

