# CarCachedImageApi

All URIs are relative to *https://marketcheck-prod.apigee.net/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCachedImage**](CarCachedImageApi.md#getCachedImage) | **GET** /image/cache/car/{listingID}/{imageID} | Fetch cached image |


<a id="getCachedImage"></a>
# **getCachedImage**
> File getCachedImage(listingID, imageID, apiKey)

Fetch cached image

Fetch the cached car image

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CarCachedImageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    CarCachedImageApi apiInstance = new CarCachedImageApi(defaultClient);
    String listingID = "listingID_example"; // String | ID of the listing to fetch cached images for
    String imageID = "imageID_example"; // String | ID of the image to fetch
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    try {
      File result = apiInstance.getCachedImage(listingID, imageID, apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CarCachedImageApi#getCachedImage");
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
| **listingID** | **String**| ID of the listing to fetch cached images for | |
| **imageID** | **String**| ID of the image to fetch | |
| **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] |

### Return type

[**File**](File.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Cached image of the car |  -  |
| **0** | Error |  -  |

