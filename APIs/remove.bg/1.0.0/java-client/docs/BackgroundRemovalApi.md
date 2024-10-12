# BackgroundRemovalApi

All URIs are relative to *https://api.remove.bg/v1.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**removebgPost**](BackgroundRemovalApi.md#removebgPost) | **POST** /removebg | Remove the background of an image |


<a id="removebgPost"></a>
# **removebgPost**
> RemoveBgJsonResponse removebgPost(removeBgJson)

Remove the background of an image

Removes the background of a JPG/PNG image.  * File size: up to 12 MB * Image source: File upload (binary or as base64 encoded string) or download from URL * Image Content: Any photo with a foreground [(e.g. people, products, animals, cars, etc.)](/supported-images) * Output resolutions available: Preview (up to 0.25 megapixels), Full (up to 25 megapixels)  Requires either an API Key to be provided in the &#x60;X-API-Key&#x60; request header or an OAuth 2.0 access token to be provided in the &#x60;Authorization&#x60; request header. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackgroundRemovalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.remove.bg/v1.0");
    
    // Configure API key authorization: APIKeyHeader
    ApiKeyAuth APIKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("APIKeyHeader");
    APIKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIKeyHeader.setApiKeyPrefix("Token");

    BackgroundRemovalApi apiInstance = new BackgroundRemovalApi(defaultClient);
    RemoveBgJson removeBgJson = new RemoveBgJson(); // RemoveBgJson | 
    try {
      RemoveBgJsonResponse result = apiInstance.removebgPost(removeBgJson);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackgroundRemovalApi#removebgPost");
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
| **removeBgJson** | [**RemoveBgJson**](RemoveBgJson.md)|  | |

### Return type

[**RemoveBgJsonResponse**](RemoveBgJsonResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json, image/*, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Image background removed |  * X-Credits-Charged - Amount of credits charged for this call <br>  * X-Foreground-Height - Height of the foreground image. In case the input image resolution is higher than the limit (&gt; 25 megapixels) this value is expressed with respect to the input image resolution. <br>  * X-Foreground-Left - Left position of the foreground image along the horizontal axis. In case the input image resolution is higher than the limit (&gt; 25 megapixels) this value is expressed with respect to the input image resolution. <br>  * X-Foreground-Top - Top position of the foreground image along the vertical axis. In case the input image resolution is higher than the limit (&gt; 25 megapixels) this value is expressed with respect to the input image resolution. <br>  * X-Foreground-Width - Width of the foreground image. In case the input image resolution is higher than the limit (&gt; 25 megapixels) this value is expressed with respect to the input image resolution. <br>  * X-Height - Height of the result image <br>  * X-Type - Detected foreground type (How specific this classification is depends on the type_level parameter sent in the request) <br>  * X-Width - Width of the result image <br>  |
| **400** | Error: Invalid parameters or input file unprocessable (no credits charged) |  -  |
| **402** | Error: Insufficient credits (no credits charged) |  -  |
| **403** | Error: Authentication failed (no credits charged) |  -  |
| **429** | Error: Rate limit exceeded (no credits charged) |  -  |

