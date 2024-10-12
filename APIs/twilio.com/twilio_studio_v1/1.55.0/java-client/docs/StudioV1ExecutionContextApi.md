# StudioV1ExecutionContextApi

All URIs are relative to *https://studio.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchExecutionContext**](StudioV1ExecutionContextApi.md#fetchExecutionContext) | **GET** /v1/Flows/{FlowSid}/Executions/{ExecutionSid}/Context |  |


<a id="fetchExecutionContext"></a>
# **fetchExecutionContext**
> StudioV1FlowExecutionExecutionContext fetchExecutionContext(flowSid, executionSid)



Retrieve the most recent context for an Execution.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StudioV1ExecutionContextApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://studio.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    StudioV1ExecutionContextApi apiInstance = new StudioV1ExecutionContextApi(defaultClient);
    String flowSid = "flowSid_example"; // String | The SID of the Flow with the Execution context to fetch.
    String executionSid = "executionSid_example"; // String | The SID of the Execution context to fetch.
    try {
      StudioV1FlowExecutionExecutionContext result = apiInstance.fetchExecutionContext(flowSid, executionSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StudioV1ExecutionContextApi#fetchExecutionContext");
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
| **flowSid** | **String**| The SID of the Flow with the Execution context to fetch. | |
| **executionSid** | **String**| The SID of the Execution context to fetch. | |

### Return type

[**StudioV1FlowExecutionExecutionContext**](StudioV1FlowExecutionExecutionContext.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

