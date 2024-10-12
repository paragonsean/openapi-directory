# BuildLogMsgApi

All URIs are relative to *https://api.netlify.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**updateSiteBuildLog**](BuildLogMsgApi.md#updateSiteBuildLog) | **POST** /builds/{build_id}/log |  |


<a id="updateSiteBuildLog"></a>
# **updateSiteBuildLog**
> updateSiteBuildLog(buildId, msg)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildLogMsgApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    BuildLogMsgApi apiInstance = new BuildLogMsgApi(defaultClient);
    String buildId = "buildId_example"; // String | 
    BuildLogMsg msg = new BuildLogMsg(); // BuildLogMsg | 
    try {
      apiInstance.updateSiteBuildLog(buildId, msg);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildLogMsgApi#updateSiteBuildLog");
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
| **buildId** | **String**|  | |
| **msg** | [**BuildLogMsg**](BuildLogMsg.md)|  | |

### Return type

null (empty response body)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No content |  -  |
| **0** | error |  -  |

