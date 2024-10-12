# FilesWriteApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**keywordsLinkKeywordToFile**](FilesWriteApi.md#keywordsLinkKeywordToFile) | **POST** /v1/files/{fileGuid}/keywords/{guid} | Link existing keyword to file |


<a id="keywordsLinkKeywordToFile"></a>
# **keywordsLinkKeywordToFile**
> FileKeywordModel keywordsLinkKeywordToFile(fileGuid, guid)

Link existing keyword to file

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesWriteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FilesWriteApi apiInstance = new FilesWriteApi(defaultClient);
    String fileGuid = "fileGuid_example"; // String | 
    String guid = "guid_example"; // String | 
    try {
      FileKeywordModel result = apiInstance.keywordsLinkKeywordToFile(fileGuid, guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesWriteApi#keywordsLinkKeywordToFile");
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
| **fileGuid** | **String**|  | |
| **guid** | **String**|  | |

### Return type

[**FileKeywordModel**](FileKeywordModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created file keyword link. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

