# PhotoControllerApi

All URIs are relative to *https://live-api.letmc.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**photoControllerGetPhotoDownload**](PhotoControllerApi.md#photoControllerGetPhotoDownload) | **GET** /v2/tier1/{shortName}/photos/photo/{photoID}/download | Downloads the photo of a property given the property and photo ID. |
| [**v2Tier1ShortNamePhotoPhotosGet**](PhotoControllerApi.md#v2Tier1ShortNamePhotoPhotosGet) | **GET** /v2/tier1/{shortName}/photo/photos | A collection of all photos in the company |
| [**v2Tier1ShortNamePhotoPhotosPhotoIDGet**](PhotoControllerApi.md#v2Tier1ShortNamePhotoPhotosPhotoIDGet) | **GET** /v2/tier1/{shortName}/photo/photos/{photoID} | Get a specific photo given its unique Object ID (OID) |


<a id="photoControllerGetPhotoDownload"></a>
# **photoControllerGetPhotoDownload**
> Object photoControllerGetPhotoDownload(shortName, photoID, width, height)

Downloads the photo of a property given the property and photo ID.

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
    String photoID = "photoID_example"; // String | The unique ID of the photo on the property
    Integer width = 56; // Integer | An optional parameter specifying the image width
    Integer height = 56; // Integer | An optional parameter specifying the image height
    try {
      Object result = apiInstance.photoControllerGetPhotoDownload(shortName, photoID, width, height);
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
| **photoID** | **String**| The unique ID of the photo on the property | |
| **width** | **Integer**| An optional parameter specifying the image width | [optional] |
| **height** | **Integer**| An optional parameter specifying the image height | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="v2Tier1ShortNamePhotoPhotosGet"></a>
# **v2Tier1ShortNamePhotoPhotosGet**
> PhotoModelResults v2Tier1ShortNamePhotoPhotosGet(shortName, offset, count)

A collection of all photos in the company

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
    Integer offset = 56; // Integer | The index of the first item to return
    Integer count = 56; // Integer | The maximum number of items to return (up to 1000 per request)
    try {
      PhotoModelResults result = apiInstance.v2Tier1ShortNamePhotoPhotosGet(shortName, offset, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PhotoControllerApi#v2Tier1ShortNamePhotoPhotosGet");
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
| **offset** | **Integer**| The index of the first item to return | |
| **count** | **Integer**| The maximum number of items to return (up to 1000 per request) | |

### Return type

[**PhotoModelResults**](PhotoModelResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="v2Tier1ShortNamePhotoPhotosPhotoIDGet"></a>
# **v2Tier1ShortNamePhotoPhotosPhotoIDGet**
> PhotoModel v2Tier1ShortNamePhotoPhotosPhotoIDGet(shortName, photoID)

Get a specific photo given its unique Object ID (OID)

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
    String photoID = "photoID_example"; // String | The unique ID of the Photo
    try {
      PhotoModel result = apiInstance.v2Tier1ShortNamePhotoPhotosPhotoIDGet(shortName, photoID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PhotoControllerApi#v2Tier1ShortNamePhotoPhotosPhotoIDGet");
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
| **photoID** | **String**| The unique ID of the Photo | |

### Return type

[**PhotoModel**](PhotoModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

