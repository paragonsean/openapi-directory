# CaptionsApi

All URIs are relative to *https://ws.api.video*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dELETEVideosVideoIdCaptionsLanguage**](CaptionsApi.md#dELETEVideosVideoIdCaptionsLanguage) | **DELETE** /videos/{videoId}/captions/{language} | Delete a caption |
| [**gETVideosVideoIdCaptions**](CaptionsApi.md#gETVideosVideoIdCaptions) | **GET** /videos/{videoId}/captions | List video captions |
| [**gETVideosVideoIdCaptionsLanguage**](CaptionsApi.md#gETVideosVideoIdCaptionsLanguage) | **GET** /videos/{videoId}/captions/{language} | Show a caption |
| [**pATCHVideosVideoIdCaptionsLanguage**](CaptionsApi.md#pATCHVideosVideoIdCaptionsLanguage) | **PATCH** /videos/{videoId}/captions/{language} | Update caption |
| [**pOSTVideosVideoIdCaptionsLanguage**](CaptionsApi.md#pOSTVideosVideoIdCaptionsLanguage) | **POST** /videos/{videoId}/captions/{language} | Upload a caption |


<a id="dELETEVideosVideoIdCaptionsLanguage"></a>
# **dELETEVideosVideoIdCaptionsLanguage**
> dELETEVideosVideoIdCaptionsLanguage(videoId, language)

Delete a caption

Delete a caption in a specific language by providing the video ID for the video you want to delete the caption from and the language the caption is in.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CaptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ws.api.video");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    CaptionsApi apiInstance = new CaptionsApi(defaultClient);
    String videoId = "vi4k0jvEUuaTdRAEjQ4Prklgc"; // String | The unique identifier for the video you want to delete a caption from.
    String language = "en"; // String | A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation.
    try {
      apiInstance.dELETEVideosVideoIdCaptionsLanguage(videoId, language);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaptionsApi#dELETEVideosVideoIdCaptionsLanguage");
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
| **videoId** | **String**| The unique identifier for the video you want to delete a caption from. | |
| **language** | **String**| A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation. | |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **404** | Not Found |  -  |

<a id="gETVideosVideoIdCaptions"></a>
# **gETVideosVideoIdCaptions**
> CaptionsListResponse gETVideosVideoIdCaptions(videoId).currentPage(currentPage).pageSize(pageSize).execute();

List video captions

Retrieve a list of available captions for the videoId you provide.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CaptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ws.api.video");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    CaptionsApi apiInstance = new CaptionsApi(defaultClient);
    String videoId = "vi4k0jvEUuaTdRAEjQ4Prklg"; // String | The unique identifier for the video you want to retrieve a list of captions for.
    Integer currentPage = 1; // Integer | Choose the number of search results to return per page. Minimum value: 1
    Integer pageSize = 25; // Integer | Results per page. Allowed values 1-100, default is 25.
    try {
      CaptionsListResponse result = apiInstance.gETVideosVideoIdCaptions(videoId)
            .currentPage(currentPage)
            .pageSize(pageSize)
            .execute();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaptionsApi#gETVideosVideoIdCaptions");
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
| **videoId** | **String**| The unique identifier for the video you want to retrieve a list of captions for. | |
| **currentPage** | **Integer**| Choose the number of search results to return per page. Minimum value: 1 | [optional] [default to 1] |
| **pageSize** | **Integer**| Results per page. Allowed values 1-100, default is 25. | [optional] [default to 25] |

### Return type

[**CaptionsListResponse**](CaptionsListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Not Found |  -  |

<a id="gETVideosVideoIdCaptionsLanguage"></a>
# **gETVideosVideoIdCaptionsLanguage**
> Subtitle gETVideosVideoIdCaptionsLanguage(videoId, language)

Show a caption

Display a caption for a video in a specific language. If the language is available, the caption is returned. Otherwise, you will get a response indicating the caption was not found. Tutorials that use the [captions endpoint](https://api.video/blog/endpoints/captions).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CaptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ws.api.video");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    CaptionsApi apiInstance = new CaptionsApi(defaultClient);
    String videoId = "vi4k0jvEUuaTdRAEjQ4Prklg"; // String | The unique identifier for the video you want captions for.
    String language = "en"; // String | A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation
    try {
      Subtitle result = apiInstance.gETVideosVideoIdCaptionsLanguage(videoId, language);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaptionsApi#gETVideosVideoIdCaptionsLanguage");
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
| **videoId** | **String**| The unique identifier for the video you want captions for. | |
| **language** | **String**| A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation | |

### Return type

[**Subtitle**](Subtitle.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Not Found |  -  |

<a id="pATCHVideosVideoIdCaptionsLanguage"></a>
# **pATCHVideosVideoIdCaptionsLanguage**
> Subtitle pATCHVideosVideoIdCaptionsLanguage(videoId, language, captionsUpdatePayload)

Update caption

To have the captions on automatically, use this PATCH to set default: true.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CaptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ws.api.video");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    CaptionsApi apiInstance = new CaptionsApi(defaultClient);
    String videoId = "vi4k0jvEUuaTdRAEjQ4Prklg"; // String | The unique identifier for the video you want to have automatic captions for. 
    String language = "en"; // String | A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation.
    CaptionsUpdatePayload captionsUpdatePayload = new CaptionsUpdatePayload(); // CaptionsUpdatePayload | 
    try {
      Subtitle result = apiInstance.pATCHVideosVideoIdCaptionsLanguage(videoId, language, captionsUpdatePayload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaptionsApi#pATCHVideosVideoIdCaptionsLanguage");
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
| **videoId** | **String**| The unique identifier for the video you want to have automatic captions for.  | |
| **language** | **String**| A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation. | |
| **captionsUpdatePayload** | [**CaptionsUpdatePayload**](CaptionsUpdatePayload.md)|  | [optional] |

### Return type

[**Subtitle**](Subtitle.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="pOSTVideosVideoIdCaptionsLanguage"></a>
# **pOSTVideosVideoIdCaptionsLanguage**
> Subtitle pOSTVideosVideoIdCaptionsLanguage(videoId, language, _file)

Upload a caption

Upload a VTT file to add captions to your video.  Read our [captioning tutorial](https://api.video/blog/tutorials/adding-captions) for more details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CaptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ws.api.video");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    CaptionsApi apiInstance = new CaptionsApi(defaultClient);
    String videoId = "vi4k0jvEUuaTdRAEjQ4Prklg"; // String | The unique identifier for the video you want to add a caption to.
    String language = "en"; // String | A valid BCP 47 language representation.
    File _file = new File("/path/to/file"); // File | The video text track (VTT) you want to upload.
    try {
      Subtitle result = apiInstance.pOSTVideosVideoIdCaptionsLanguage(videoId, language, _file);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaptionsApi#pOSTVideosVideoIdCaptionsLanguage");
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
| **videoId** | **String**| The unique identifier for the video you want to add a caption to. | |
| **language** | **String**| A valid BCP 47 language representation. | |
| **_file** | **File**| The video text track (VTT) you want to upload. | |

### Return type

[**Subtitle**](Subtitle.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

