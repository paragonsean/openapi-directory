# StudioV1ExecutionStepApi

All URIs are relative to *https://studio.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchExecutionStep**](StudioV1ExecutionStepApi.md#fetchExecutionStep) | **GET** /v1/Flows/{FlowSid}/Executions/{ExecutionSid}/Steps/{Sid} |  |
| [**listExecutionStep**](StudioV1ExecutionStepApi.md#listExecutionStep) | **GET** /v1/Flows/{FlowSid}/Executions/{ExecutionSid}/Steps |  |


<a id="fetchExecutionStep"></a>
# **fetchExecutionStep**
> StudioV1FlowExecutionExecutionStep fetchExecutionStep(flowSid, executionSid, sid)



Retrieve a Step.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StudioV1ExecutionStepApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://studio.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    StudioV1ExecutionStepApi apiInstance = new StudioV1ExecutionStepApi(defaultClient);
    String flowSid = "flowSid_example"; // String | The SID of the Flow with the Step to fetch.
    String executionSid = "executionSid_example"; // String | The SID of the Execution resource with the Step to fetch.
    String sid = "sid_example"; // String | The SID of the ExecutionStep resource to fetch.
    try {
      StudioV1FlowExecutionExecutionStep result = apiInstance.fetchExecutionStep(flowSid, executionSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StudioV1ExecutionStepApi#fetchExecutionStep");
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
| **sid** | **String**| The SID of the ExecutionStep resource to fetch. | |

### Return type

[**StudioV1FlowExecutionExecutionStep**](StudioV1FlowExecutionExecutionStep.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listExecutionStep"></a>
# **listExecutionStep**
> ListExecutionStepResponse listExecutionStep(flowSid, executionSid, pageSize, page, pageToken)



Retrieve a list of all Steps for an Execution.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StudioV1ExecutionStepApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://studio.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    StudioV1ExecutionStepApi apiInstance = new StudioV1ExecutionStepApi(defaultClient);
    String flowSid = "flowSid_example"; // String | The SID of the Flow with the Steps to read.
    String executionSid = "executionSid_example"; // String | The SID of the Execution with the Steps to read.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListExecutionStepResponse result = apiInstance.listExecutionStep(flowSid, executionSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StudioV1ExecutionStepApi#listExecutionStep");
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
| **flowSid** | **String**| The SID of the Flow with the Steps to read. | |
| **executionSid** | **String**| The SID of the Execution with the Steps to read. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListExecutionStepResponse**](ListExecutionStepResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

