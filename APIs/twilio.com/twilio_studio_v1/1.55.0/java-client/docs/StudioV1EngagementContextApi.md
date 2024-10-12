# StudioV1EngagementContextApi

All URIs are relative to *https://studio.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchEngagementContext**](StudioV1EngagementContextApi.md#fetchEngagementContext) | **GET** /v1/Flows/{FlowSid}/Engagements/{EngagementSid}/Context |  |


<a id="fetchEngagementContext"></a>
# **fetchEngagementContext**
> StudioV1FlowEngagementEngagementContext fetchEngagementContext(flowSid, engagementSid)



Retrieve the most recent context for an Engagement.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StudioV1EngagementContextApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://studio.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    StudioV1EngagementContextApi apiInstance = new StudioV1EngagementContextApi(defaultClient);
    String flowSid = "flowSid_example"; // String | The SID of the Flow.
    String engagementSid = "engagementSid_example"; // String | The SID of the Engagement.
    try {
      StudioV1FlowEngagementEngagementContext result = apiInstance.fetchEngagementContext(flowSid, engagementSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StudioV1EngagementContextApi#fetchEngagementContext");
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
| **flowSid** | **String**| The SID of the Flow. | |
| **engagementSid** | **String**| The SID of the Engagement. | |

### Return type

[**StudioV1FlowEngagementEngagementContext**](StudioV1FlowEngagementEngagementContext.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

