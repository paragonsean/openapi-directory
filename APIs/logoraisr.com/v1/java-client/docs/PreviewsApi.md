# PreviewsApi

All URIs are relative to *https://api.logoraisr.com/rest-v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**previewsRead**](PreviewsApi.md#previewsRead) | **GET** /previews/{file_id}/ | Get preview image of uploaded file |


<a id="previewsRead"></a>
# **previewsRead**
> PreviewResponse previewsRead(fileId)

Get preview image of uploaded file

This GET-Method returns the URL where the preview image of uploaded file can downloaded from.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.logoraisr.com/rest-v1");
    
    // Configure API key authorization: Token
    ApiKeyAuth Token = (ApiKeyAuth) defaultClient.getAuthentication("Token");
    Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token.setApiKeyPrefix("Token");

    PreviewsApi apiInstance = new PreviewsApi(defaultClient);
    String fileId = "fileId_example"; // String | Id of the file for which the preview_img_url is generated.
    try {
      PreviewResponse result = apiInstance.previewsRead(fileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewsApi#previewsRead");
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
| **fileId** | **String**| Id of the file for which the preview_img_url is generated. | |

### Return type

[**PreviewResponse**](PreviewResponse.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | BAD REQUEST |  -  |
| **403** | FORBIDDEN |  -  |

