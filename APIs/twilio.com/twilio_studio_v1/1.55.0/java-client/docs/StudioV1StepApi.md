# StudioV1StepApi

All URIs are relative to *https://studio.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchStep**](StudioV1StepApi.md#fetchStep) | **GET** /v1/Flows/{FlowSid}/Engagements/{EngagementSid}/Steps/{Sid} |  |
| [**listStep**](StudioV1StepApi.md#listStep) | **GET** /v1/Flows/{FlowSid}/Engagements/{EngagementSid}/Steps |  |


<a id="fetchStep"></a>
# **fetchStep**
> StudioV1FlowEngagementStep fetchStep(flowSid, engagementSid, sid)



Retrieve a Step.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StudioV1StepApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://studio.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    StudioV1StepApi apiInstance = new StudioV1StepApi(defaultClient);
    String flowSid = "flowSid_example"; // String | The SID of the Flow with the Step to fetch.
    String engagementSid = "engagementSid_example"; // String | The SID of the Engagement with the Step to fetch.
    String sid = "sid_example"; // String | The SID of the Step resource to fetch.
    try {
      StudioV1FlowEngagementStep result = apiInstance.fetchStep(flowSid, engagementSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StudioV1StepApi#fetchStep");
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
| **sid** | **String**| The SID of the Step resource to fetch. | |

### Return type

[**StudioV1FlowEngagementStep**](StudioV1FlowEngagementStep.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listStep"></a>
# **listStep**
> ListStepResponse listStep(flowSid, engagementSid, pageSize, page, pageToken)



Retrieve a list of all Steps for an Engagement.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StudioV1StepApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://studio.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    StudioV1StepApi apiInstance = new StudioV1StepApi(defaultClient);
    String flowSid = "flowSid_example"; // String | The SID of the Flow with the Step to read.
    String engagementSid = "engagementSid_example"; // String | The SID of the Engagement with the Step to read.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListStepResponse result = apiInstance.listStep(flowSid, engagementSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StudioV1StepApi#listStep");
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
| **flowSid** | **String**| The SID of the Flow with the Step to read. | |
| **engagementSid** | **String**| The SID of the Engagement with the Step to read. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListStepResponse**](ListStepResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

