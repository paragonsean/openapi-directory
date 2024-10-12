# PhotoControllerApi

All URIs are relative to *https://live-api.letmc.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**photoControllerGetPhotoDownload**](PhotoControllerApi.md#photoControllerGetPhotoDownload) | **GET** /v2/customer/{shortName}/photo/download | Downloads the photo of a property given the photo ID. |


<a id="photoControllerGetPhotoDownload"></a>
# **photoControllerGetPhotoDownload**
> Object photoControllerGetPhotoDownload(shortName, token, photoID, width, height)

Downloads the photo of a property given the photo ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PhotoControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    PhotoControllerApi apiInstance = new PhotoControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String token = "token_example"; // String | The login token returned from the /session POST call
    String photoID = "photoID_example"; // String | The unique ID of the photo on the property
    Integer width = 56; // Integer | An optional parameter specifying the image width
    Integer height = 56; // Integer | An optional parameter specifying the image height
    try {
      Object result = apiInstance.photoControllerGetPhotoDownload(shortName, token, photoID, width, height);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PhotoControllerApi#photoControllerGetPhotoDownload");
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
| **shortName** | **String**| The unique client short-name | |
| **token** | **String**| The login token returned from the /session POST call | |
| **photoID** | **String**| The unique ID of the photo on the property | |
| **width** | **Integer**| An optional parameter specifying the image width | [optional] |
| **height** | **Integer**| An optional parameter specifying the image height | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

