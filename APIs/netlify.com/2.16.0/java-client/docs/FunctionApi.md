# FunctionApi

All URIs are relative to *https://api.netlify.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**uploadDeployFunction**](FunctionApi.md#uploadDeployFunction) | **PUT** /deploys/{deploy_id}/functions/{name} |  |


<a id="uploadDeployFunction"></a>
# **uploadDeployFunction**
> Function uploadDeployFunction(deployId, name, fileBody, runtime, size, xNfRetryCount)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FunctionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    FunctionApi apiInstance = new FunctionApi(defaultClient);
    String deployId = "deployId_example"; // String | 
    String name = "name_example"; // String | 
    File fileBody = new File("/path/to/file"); // File | 
    String runtime = "runtime_example"; // String | 
    Integer size = 56; // Integer | 
    Integer xNfRetryCount = 56; // Integer | 
    try {
      Function result = apiInstance.uploadDeployFunction(deployId, name, fileBody, runtime, size, xNfRetryCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FunctionApi#uploadDeployFunction");
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
| **deployId** | **String**|  | |
| **name** | **String**|  | |
| **fileBody** | **File**|  | |
| **runtime** | **String**|  | [optional] |
| **size** | **Integer**|  | [optional] |
| **xNfRetryCount** | **Integer**|  | [optional] |

### Return type

[**Function**](Function.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | error |  -  |

