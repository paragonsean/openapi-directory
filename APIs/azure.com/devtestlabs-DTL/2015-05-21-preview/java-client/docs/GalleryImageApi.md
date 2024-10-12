# GalleryImageApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**galleryImageList**](GalleryImageApi.md#galleryImageList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/galleryimages |  |


<a id="galleryImageList"></a>
# **galleryImageList**
> ResponseWithContinuationGalleryImage galleryImageList(subscriptionId, resourceGroupName, labName, apiVersion, $filter, $top, $orderBy)



List gallery images.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GalleryImageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GalleryImageApi apiInstance = new GalleryImageApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String apiVersion = "2015-05-21-preview"; // String | Client API version.
    String $filter = "$filter_example"; // String | The filter to apply on the operation.
    Integer $top = 56; // Integer | 
    String $orderBy = "$orderBy_example"; // String | 
    try {
      ResponseWithContinuationGalleryImage result = apiInstance.galleryImageList(subscriptionId, resourceGroupName, labName, apiVersion, $filter, $top, $orderBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GalleryImageApi#galleryImageList");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labName** | **String**| The name of the lab. | |
| **apiVersion** | **String**| Client API version. | [default to 2015-05-21-preview] |
| **$filter** | **String**| The filter to apply on the operation. | [optional] |
| **$top** | **Integer**|  | [optional] |
| **$orderBy** | **String**|  | [optional] |

### Return type

[**ResponseWithContinuationGalleryImage**](ResponseWithContinuationGalleryImage.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

