# ServerlessV1BuildStatusApi

All URIs are relative to *https://serverless.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchBuildStatus**](ServerlessV1BuildStatusApi.md#fetchBuildStatus) | **GET** /v1/Services/{ServiceSid}/Builds/{Sid}/Status |  |


<a id="fetchBuildStatus"></a>
# **fetchBuildStatus**
> ServerlessV1ServiceBuildBuildStatus fetchBuildStatus(serviceSid, sid)



Retrieve a specific Build resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerlessV1BuildStatusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://serverless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ServerlessV1BuildStatusApi apiInstance = new ServerlessV1BuildStatusApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the Service to fetch the Build resource from.
    String sid = "sid_example"; // String | The SID of the Build resource to fetch.
    try {
      ServerlessV1ServiceBuildBuildStatus result = apiInstance.fetchBuildStatus(serviceSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerlessV1BuildStatusApi#fetchBuildStatus");
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
| **serviceSid** | **String**| The SID of the Service to fetch the Build resource from. | |
| **sid** | **String**| The SID of the Build resource to fetch. | |

### Return type

[**ServerlessV1ServiceBuildBuildStatus**](ServerlessV1ServiceBuildBuildStatus.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

