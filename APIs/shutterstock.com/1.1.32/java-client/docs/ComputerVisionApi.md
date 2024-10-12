# ComputerVisionApi

All URIs are relative to *https://api.shutterstock.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getKeywords**](ComputerVisionApi.md#getKeywords) | **GET** /v2/cv/keywords | List suggested keywords |
| [**getSimilarImages**](ComputerVisionApi.md#getSimilarImages) | **GET** /v2/cv/similar/images | List similar images |
| [**getSimilarVideos**](ComputerVisionApi.md#getSimilarVideos) | **GET** /v2/cv/similar/videos | List similar videos |
| [**uploadEphemeralImage**](ComputerVisionApi.md#uploadEphemeralImage) | **POST** /v2/images | Upload ephemeral images |
| [**uploadImage**](ComputerVisionApi.md#uploadImage) | **POST** /v2/cv/images | Upload images |


<a id="getKeywords"></a>
# **getKeywords**
> KeywordDataList getKeywords(assetId)

List suggested keywords

This endpoint returns a list of suggested keywords for a media item that you specify or upload.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComputerVisionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    ComputerVisionApi apiInstance = new ComputerVisionApi(defaultClient);
    GetKeywordsAssetIdParameter assetId = new GetKeywordsAssetIdParameter(); // GetKeywordsAssetIdParameter | The asset ID or upload ID to suggest keywords for
    try {
      KeywordDataList result = apiInstance.getKeywords(assetId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComputerVisionApi#getKeywords");
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
| **assetId** | [**GetKeywordsAssetIdParameter**](.md)| The asset ID or upload ID to suggest keywords for | |

### Return type

[**KeywordDataList**](KeywordDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **415** | Unsupported Media Type |  -  |

<a id="getSimilarImages"></a>
# **getSimilarImages**
> ImageSearchResults getSimilarImages(assetId, license, safe, language, page, perPage, view)

List similar images

This endpoint returns images that are visually similar to an image that you specify or upload.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComputerVisionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    ComputerVisionApi apiInstance = new ComputerVisionApi(defaultClient);
    String assetId = "U6ba16262e3bc2db470b8e3cfa8aaab25"; // String | The asset ID or upload ID to find similar images for
    List<String> license = Arrays.asList(); // List<String> | Show only images with the specified license
    Boolean safe = true; // Boolean | Enable or disable safe search
    Language language = Language.fromValue("ar"); // Language | Language for the keywords and categories in the response
    Integer page = 1; // Integer | Page number
    Integer perPage = 20; // Integer | Number of results per page
    String view = "minimal"; // String | Amount of detail to render in the response
    try {
      ImageSearchResults result = apiInstance.getSimilarImages(assetId, license, safe, language, page, perPage, view);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComputerVisionApi#getSimilarImages");
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
| **assetId** | **String**| The asset ID or upload ID to find similar images for | |
| **license** | [**List&lt;String&gt;**](String.md)| Show only images with the specified license | [optional] [enum: commercial, editorial] |
| **safe** | **Boolean**| Enable or disable safe search | [optional] [default to true] |
| **language** | [**Language**](.md)| Language for the keywords and categories in the response | [optional] [enum: ar, bg, bn, cs, da, de, el, en, es, fi, fr, gu, he, hi, hr, hu, id, it, ja, kn, ko, ml, mr, nb, nl, or, pl, pt, ro, ru, sk, sl, sv, ta, te, th, tr, uk, ur, vi, zh, zh-Hant] |
| **page** | **Integer**| Page number | [optional] [default to 1] |
| **perPage** | **Integer**| Number of results per page | [optional] [default to 20] |
| **view** | **String**| Amount of detail to render in the response | [optional] [default to minimal] [enum: minimal, full] |

### Return type

[**ImageSearchResults**](ImageSearchResults.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="getSimilarVideos"></a>
# **getSimilarVideos**
> VideoSearchResults getSimilarVideos(assetId, license, safe, language, page, perPage, view)

List similar videos

This endpoint returns videos that are visually similar to an image that you specify or upload.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComputerVisionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    ComputerVisionApi apiInstance = new ComputerVisionApi(defaultClient);
    String assetId = "U6ba16262e3bc2db470b8e3cfa8aaab25"; // String | The asset ID or upload ID to find similar videos for
    List<String> license = Arrays.asList(); // List<String> | Show only videos with the specified license
    Boolean safe = true; // Boolean | Enable or disable safe search
    Language language = Language.fromValue("ar"); // Language | Language for the keywords and categories in the response
    Integer page = 1; // Integer | Page number
    Integer perPage = 20; // Integer | Number of results per page
    String view = "minimal"; // String | Amount of detail to render in the response
    try {
      VideoSearchResults result = apiInstance.getSimilarVideos(assetId, license, safe, language, page, perPage, view);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComputerVisionApi#getSimilarVideos");
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
| **assetId** | **String**| The asset ID or upload ID to find similar videos for | |
| **license** | [**List&lt;String&gt;**](String.md)| Show only videos with the specified license | [optional] [enum: commercial, editorial] |
| **safe** | **Boolean**| Enable or disable safe search | [optional] [default to true] |
| **language** | [**Language**](.md)| Language for the keywords and categories in the response | [optional] [enum: ar, bg, bn, cs, da, de, el, en, es, fi, fr, gu, he, hi, hr, hu, id, it, ja, kn, ko, ml, mr, nb, nl, or, pl, pt, ro, ru, sk, sl, sv, ta, te, th, tr, uk, ur, vi, zh, zh-Hant] |
| **page** | **Integer**| Page number | [optional] [default to 1] |
| **perPage** | **Integer**| Number of results per page | [optional] [default to 20] |
| **view** | **String**| Amount of detail to render in the response | [optional] [default to minimal] [enum: minimal, full] |

### Return type

[**VideoSearchResults**](VideoSearchResults.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="uploadEphemeralImage"></a>
# **uploadEphemeralImage**
> ImageCreateResponse uploadEphemeralImage(imageCreateRequest)

Upload ephemeral images

Deprecated; use &#x60;POST /v2/cv/images&#x60; instead. This endpoint uploads an image for reverse image search. The image must be in JPEG or PNG format. To get the search results, pass the ID that this endpoint returns to the &#x60;GET /v2/images/{id}/similar&#x60; endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComputerVisionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    ComputerVisionApi apiInstance = new ComputerVisionApi(defaultClient);
    ImageCreateRequest imageCreateRequest = new ImageCreateRequest(); // ImageCreateRequest | The image data in JPEG or PNG format
    try {
      ImageCreateResponse result = apiInstance.uploadEphemeralImage(imageCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComputerVisionApi#uploadEphemeralImage");
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
| **imageCreateRequest** | [**ImageCreateRequest**](ImageCreateRequest.md)| The image data in JPEG or PNG format | |

### Return type

[**ImageCreateResponse**](ImageCreateResponse.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **413** | Payload Too Large |  -  |

<a id="uploadImage"></a>
# **uploadImage**
> ComputerVisionImageCreateResponse uploadImage(imageCreateRequest)

Upload images

This endpoint uploads an image for reverse image or video search. Images must be in JPEG or PNG format. To get the search results, pass the upload ID that this endpoint returns to the GET /v2/cv/similar/images or GET /v2/cv/similar/videos endpoints. Contact us for access to this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComputerVisionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    ComputerVisionApi apiInstance = new ComputerVisionApi(defaultClient);
    ImageCreateRequest imageCreateRequest = new ImageCreateRequest(); // ImageCreateRequest | A Base 64 encoded jpeg or png; images can be no larger than 10mb and can be no larger than 10,000 pixels in width or height
    try {
      ComputerVisionImageCreateResponse result = apiInstance.uploadImage(imageCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComputerVisionApi#uploadImage");
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
| **imageCreateRequest** | [**ImageCreateRequest**](ImageCreateRequest.md)| A Base 64 encoded jpeg or png; images can be no larger than 10mb and can be no larger than 10,000 pixels in width or height | |

### Return type

[**ComputerVisionImageCreateResponse**](ComputerVisionImageCreateResponse.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **413** | Payload Too Large |  -  |
| **415** | Unsupported Media Type |  -  |

