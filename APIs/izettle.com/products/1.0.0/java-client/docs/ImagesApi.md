# ImagesApi

All URIs are relative to *https://products.izettle.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAllImageUrls**](ImagesApi.md#getAllImageUrls) | **GET** /organizations/{organizationUuid}/images | Retrieve all library item images |


<a id="getAllImageUrls"></a>
# **getAllImageUrls**
> LibraryImagesResponse getAllImageUrls(organizationUuid)

Retrieve all library item images

Retrieves all library items images used by the organization, sorted by updated date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://products.izettle.com");
    
    // Configure OAuth2 access token for authorization: ZettleOauth
    OAuth ZettleOauth = (OAuth) defaultClient.getAuthentication("ZettleOauth");
    ZettleOauth.setAccessToken("YOUR ACCESS TOKEN");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    UUID organizationUuid = UUID.randomUUID(); // UUID | 
    try {
      LibraryImagesResponse result = apiInstance.getAllImageUrls(organizationUuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#getAllImageUrls");
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
| **organizationUuid** | **UUID**|  | |

### Return type

[**LibraryImagesResponse**](LibraryImagesResponse.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of all image urls |  -  |

