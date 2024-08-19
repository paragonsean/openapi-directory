# FilesApi

All URIs are relative to *https://presentation.s.xtrf.eu/home-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**uploadFile**](FilesApi.md#uploadFile) | **POST** /files | Uploads a temporary file (ie. for XML import). Returns token which can be used in other API calls. |


<a id="uploadFile"></a>
# **uploadFile**
> uploadFile(_file)

Uploads a temporary file (ie. for XML import). Returns token which can be used in other API calls.

When a file is required by an operation (ie. task creation) it must be uploaded previously to the API. Uploading a file will result in a file token, which can be used to reference this file in other API calls.  Each file must be uploaded separately.  Keep in mind that file token has limited validity (ie. 10 minutes).  Therefore files must be uploaded just before issuing API call which reference them. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    FilesApi apiInstance = new FilesApi(defaultClient);
    File _file = new File("/path/to/file"); // File | 
    try {
      apiInstance.uploadFile(_file);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#uploadFile");
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
| **_file** | **File**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | default response |  -  |

