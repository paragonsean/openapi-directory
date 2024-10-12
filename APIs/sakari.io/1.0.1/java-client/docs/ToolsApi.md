# ToolsApi

All URIs are relative to *https://api.sakari.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**toolsShareFile**](ToolsApi.md#toolsShareFile) | **POST** /v1/tools/sharefile | Share file - use to host a file and generate a short link to be used directly in a message or as a link to media for a MMS |


<a id="toolsShareFile"></a>
# **toolsShareFile**
> ShareFileResponse toolsShareFile(body)

Share file - use to host a file and generate a short link to be used directly in a message or as a link to media for a MMS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ToolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sakari.io");
    
    // Configure OAuth2 access token for authorization: sakari_auth
    OAuth sakari_auth = (OAuth) defaultClient.getAuthentication("sakari_auth");
    sakari_auth.setAccessToken("YOUR ACCESS TOKEN");

    ToolsApi apiInstance = new ToolsApi(defaultClient);
    File body = new File("/path/to/file"); // File | 
    try {
      ShareFileResponse result = apiInstance.toolsShareFile(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ToolsApi#toolsShareFile");
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
| **body** | **File**|  | |

### Return type

[**ShareFileResponse**](ShareFileResponse.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

 - **Content-Type**: application/octet-stream, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **4XX** | invalid request |  -  |
| **5XX** | invalid request |  -  |

