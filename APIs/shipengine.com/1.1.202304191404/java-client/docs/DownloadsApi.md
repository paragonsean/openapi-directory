# DownloadsApi

All URIs are relative to *https://api.shipengine.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**downloadFile**](DownloadsApi.md#downloadFile) | **GET** /v1/downloads/{dir}/{subdir}/{filename} | Download File |


<a id="downloadFile"></a>
# **downloadFile**
> File downloadFile(subdir, filename, dir, download, rotation)

Download File

Get File

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DownloadsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DownloadsApi apiInstance = new DownloadsApi(defaultClient);
    String subdir = "subdir_example"; // String | 
    String filename = "filename_example"; // String | 
    String dir = "dir_example"; // String | 
    String download = "download_example"; // String | 
    Integer rotation = 56; // Integer | 
    try {
      File result = apiInstance.downloadFile(subdir, filename, dir, download, rotation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DownloadsApi#downloadFile");
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
| **subdir** | **String**|  | |
| **filename** | **String**|  | |
| **dir** | **String**|  | |
| **download** | **String**|  | [optional] |
| **rotation** | **Integer**|  | [optional] |

### Return type

[**File**](File.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, application/zpl, image/png, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was a success |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

