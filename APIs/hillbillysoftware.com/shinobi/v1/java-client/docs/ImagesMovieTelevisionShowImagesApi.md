# ImagesMovieTelevisionShowImagesApi

All URIs are relative to *https://api.hillbillysoftware.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**imageSearchGet**](ImagesMovieTelevisionShowImagesApi.md#imageSearchGet) | **GET** /Images/Search/{Accesstoken}/{Query} | Get images available for movie/tv show with passed query |
| [**imagesGet**](ImagesMovieTelevisionShowImagesApi.md#imagesGet) | **GET** /Images/ByID/{AccessToken}/{imdbID} | Get images available for movie/tv show with passed imdbID |


<a id="imageSearchGet"></a>
# **imageSearchGet**
> List&lt;ImdbImages&gt; imageSearchGet(accesstoken, query, strictmatch)

Get images available for movie/tv show with passed query

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagesMovieTelevisionShowImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    ImagesMovieTelevisionShowImagesApi apiInstance = new ImagesMovieTelevisionShowImagesApi(defaultClient);
    String accesstoken = "accesstoken_example"; // String | 
    String query = "query_example"; // String | Name or part of name from Movie or Show
    Boolean strictmatch = true; // Boolean | 
    try {
      List<ImdbImages> result = apiInstance.imageSearchGet(accesstoken, query, strictmatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesMovieTelevisionShowImagesApi#imageSearchGet");
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
| **accesstoken** | **String**|  | |
| **query** | **String**| Name or part of name from Movie or Show | |
| **strictmatch** | **Boolean**|  | [optional] |

### Return type

[**List&lt;ImdbImages&gt;**](ImdbImages.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of images |  -  |

<a id="imagesGet"></a>
# **imagesGet**
> List&lt;ImdbImages&gt; imagesGet(accessToken, imdbID)

Get images available for movie/tv show with passed imdbID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagesMovieTelevisionShowImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hillbillysoftware.com");

    ImagesMovieTelevisionShowImagesApi apiInstance = new ImagesMovieTelevisionShowImagesApi(defaultClient);
    String accessToken = "accessToken_example"; // String | 
    String imdbID = "imdbID_example"; // String | 
    try {
      List<ImdbImages> result = apiInstance.imagesGet(accessToken, imdbID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesMovieTelevisionShowImagesApi#imagesGet");
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
| **accessToken** | **String**|  | |
| **imdbID** | **String**|  | |

### Return type

[**List&lt;ImdbImages&gt;**](ImdbImages.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of images |  -  |

