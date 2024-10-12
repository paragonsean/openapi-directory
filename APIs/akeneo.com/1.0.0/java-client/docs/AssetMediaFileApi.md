# AssetMediaFileApi

All URIs are relative to *http://demo.akeneo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAssetMediaFilesCode**](AssetMediaFileApi.md#getAssetMediaFilesCode) | **GET** /api/rest/v1/asset-media-files/{code} | Download the media file associated to an asset |
| [**postAssetMediaFiles**](AssetMediaFileApi.md#postAssetMediaFiles) | **POST** /api/rest/v1/asset-media-files | Create a new media file for an asset |


<a id="getAssetMediaFilesCode"></a>
# **getAssetMediaFilesCode**
> getAssetMediaFilesCode(code)

Download the media file associated to an asset

This endpoint allows you to download a given media file that is associated with an asset.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetMediaFileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    AssetMediaFileApi apiInstance = new AssetMediaFileApi(defaultClient);
    String code = "code_example"; // String | Code of the resource
    try {
      apiInstance.getAssetMediaFilesCode(code);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetMediaFileApi#getAssetMediaFilesCode");
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
| **code** | **String**| Code of the resource | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Authentication required |  -  |
| **404** | Resource not found |  -  |

<a id="postAssetMediaFiles"></a>
# **postAssetMediaFiles**
> postAssetMediaFiles(contentType, body)

Create a new media file for an asset

This endpoint allows you to create a new media file and associate it to a media file attribute value of an asset.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetMediaFileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    AssetMediaFileApi apiInstance = new AssetMediaFileApi(defaultClient);
    String contentType = "contentType_example"; // String | Equal to 'multipart/form-data', no other value allowed
    PostAssetMediaFilesRequest body = new PostAssetMediaFilesRequest(); // PostAssetMediaFilesRequest | 
    try {
      apiInstance.postAssetMediaFiles(contentType, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetMediaFileApi#postAssetMediaFiles");
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
| **contentType** | **String**| Equal to &#39;multipart/form-data&#39;, no other value allowed | |
| **body** | [**PostAssetMediaFilesRequest**](PostAssetMediaFilesRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message, _links

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  * Asset-media-file-code - Code of the media file <br>  * Location - URI of the created resource <br>  |
| **401** | Authentication required |  -  |
| **415** | Unsupported Media type |  -  |
| **422** | Unprocessable entity |  -  |

