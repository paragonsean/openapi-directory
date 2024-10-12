# StudioV2FlowRevisionApi

All URIs are relative to *https://studio.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchFlowRevision**](StudioV2FlowRevisionApi.md#fetchFlowRevision) | **GET** /v2/Flows/{Sid}/Revisions/{Revision} |  |
| [**listFlowRevision**](StudioV2FlowRevisionApi.md#listFlowRevision) | **GET** /v2/Flows/{Sid}/Revisions |  |


<a id="fetchFlowRevision"></a>
# **fetchFlowRevision**
> StudioV2FlowFlowRevision fetchFlowRevision(sid, revision)



Retrieve a specific Flow revision.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StudioV2FlowRevisionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://studio.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    StudioV2FlowRevisionApi apiInstance = new StudioV2FlowRevisionApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the Flow resource to fetch.
    String revision = "revision_example"; // String | Specific Revision number or can be `LatestPublished` and `LatestRevision`.
    try {
      StudioV2FlowFlowRevision result = apiInstance.fetchFlowRevision(sid, revision);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StudioV2FlowRevisionApi#fetchFlowRevision");
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
| **sid** | **String**| The SID of the Flow resource to fetch. | |
| **revision** | **String**| Specific Revision number or can be &#x60;LatestPublished&#x60; and &#x60;LatestRevision&#x60;. | |

### Return type

[**StudioV2FlowFlowRevision**](StudioV2FlowFlowRevision.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listFlowRevision"></a>
# **listFlowRevision**
> ListFlowRevisionResponse listFlowRevision(sid, pageSize, page, pageToken)



Retrieve a list of all Flows revisions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StudioV2FlowRevisionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://studio.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    StudioV2FlowRevisionApi apiInstance = new StudioV2FlowRevisionApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the Flow resource to fetch.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListFlowRevisionResponse result = apiInstance.listFlowRevision(sid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StudioV2FlowRevisionApi#listFlowRevision");
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
| **sid** | **String**| The SID of the Flow resource to fetch. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListFlowRevisionResponse**](ListFlowRevisionResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

