# ContentV1ApprovalFetchApi

All URIs are relative to *https://content.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchApprovalFetch**](ContentV1ApprovalFetchApi.md#fetchApprovalFetch) | **GET** /v1/Content/{Sid}/ApprovalRequests |  |


<a id="fetchApprovalFetch"></a>
# **fetchApprovalFetch**
> ContentV1ContentApprovalFetch fetchApprovalFetch(sid)



Fetch a Content resource&#39;s approval status by its unique Content Sid

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentV1ApprovalFetchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://content.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ContentV1ApprovalFetchApi apiInstance = new ContentV1ApprovalFetchApi(defaultClient);
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Content resource whose approval information to fetch.
    try {
      ContentV1ContentApprovalFetch result = apiInstance.fetchApprovalFetch(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentV1ApprovalFetchApi#fetchApprovalFetch");
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
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Content resource whose approval information to fetch. | |

### Return type

[**ContentV1ContentApprovalFetch**](ContentV1ContentApprovalFetch.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

