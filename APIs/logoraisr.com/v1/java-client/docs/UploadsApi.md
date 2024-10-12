# UploadsApi

All URIs are relative to *https://api.logoraisr.com/rest-v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**uploadsCreate**](UploadsApi.md#uploadsCreate) | **POST** /uploads/ | Upload a new image |


<a id="uploadsCreate"></a>
# **uploadsCreate**
> FileResponse uploadsCreate(_file)

Upload a new image

This POST-Method uploads a new file on the server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UploadsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.logoraisr.com/rest-v1");
    
    // Configure API key authorization: Token
    ApiKeyAuth Token = (ApiKeyAuth) defaultClient.getAuthentication("Token");
    Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token.setApiKeyPrefix("Token");

    UploadsApi apiInstance = new UploadsApi(defaultClient);
    File _file = new File("/path/to/file"); // File | File which should be uploaded. Supported file types are: JPEG and PNG
    try {
      FileResponse result = apiInstance.uploadsCreate(_file);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UploadsApi#uploadsCreate");
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
| **_file** | **File**| File which should be uploaded. Supported file types are: JPEG and PNG | |

### Return type

[**FileResponse**](FileResponse.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |
| **400** | BAD REQUEST |  -  |

