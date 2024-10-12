# StudioV2ExecutionStepContextApi

All URIs are relative to *https://studio.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchExecutionStepContext**](StudioV2ExecutionStepContextApi.md#fetchExecutionStepContext) | **GET** /v2/Flows/{FlowSid}/Executions/{ExecutionSid}/Steps/{StepSid}/Context |  |


<a id="fetchExecutionStepContext"></a>
# **fetchExecutionStepContext**
> StudioV2FlowExecutionExecutionStepExecutionStepContext fetchExecutionStepContext(flowSid, executionSid, stepSid)



Retrieve the context for an Execution Step.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StudioV2ExecutionStepContextApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://studio.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    StudioV2ExecutionStepContextApi apiInstance = new StudioV2ExecutionStepContextApi(defaultClient);
    String flowSid = "flowSid_example"; // String | The SID of the Flow with the Step to fetch.
    String executionSid = "executionSid_example"; // String | The SID of the Execution resource with the Step to fetch.
    String stepSid = "stepSid_example"; // String | The SID of the Step to fetch.
    try {
      StudioV2FlowExecutionExecutionStepExecutionStepContext result = apiInstance.fetchExecutionStepContext(flowSid, executionSid, stepSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StudioV2ExecutionStepContextApi#fetchExecutionStepContext");
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
| **executionSid** | **String**| The SID of the Execution resource with the Step to fetch. | |
| **stepSid** | **String**| The SID of the Step to fetch. | |

### Return type

[**StudioV2FlowExecutionExecutionStepExecutionStepContext**](StudioV2FlowExecutionExecutionStepExecutionStepContext.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

