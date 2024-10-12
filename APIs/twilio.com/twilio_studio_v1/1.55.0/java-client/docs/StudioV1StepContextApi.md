# StudioV1StepContextApi

All URIs are relative to *https://studio.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchStepContext**](StudioV1StepContextApi.md#fetchStepContext) | **GET** /v1/Flows/{FlowSid}/Engagements/{EngagementSid}/Steps/{StepSid}/Context |  |


<a id="fetchStepContext"></a>
# **fetchStepContext**
> StudioV1FlowEngagementStepStepContext fetchStepContext(flowSid, engagementSid, stepSid)



Retrieve the context for an Engagement Step.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StudioV1StepContextApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://studio.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    StudioV1StepContextApi apiInstance = new StudioV1StepContextApi(defaultClient);
    String flowSid = "flowSid_example"; // String | The SID of the Flow with the Step to fetch.
    String engagementSid = "engagementSid_example"; // String | The SID of the Engagement with the Step to fetch.
    String stepSid = "stepSid_example"; // String | The SID of the Step to fetch
    try {
      StudioV1FlowEngagementStepStepContext result = apiInstance.fetchStepContext(flowSid, engagementSid, stepSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StudioV1StepContextApi#fetchStepContext");
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
| **flowSid** | **String**| The SID of the Flow with the Step to fetch. | |
| **engagementSid** | **String**| The SID of the Engagement with the Step to fetch. | |
| **stepSid** | **String**| The SID of the Step to fetch | |

### Return type

[**StudioV1FlowEngagementStepStepContext**](StudioV1FlowEngagementStepStepContext.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

