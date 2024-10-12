# SlidesApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**slidesSlidesChildobjectsGetId**](SlidesApi.md#slidesSlidesChildobjectsGetId) | **GET** /Slides/ChildObjects/{id} | Slides: Get Dependent Objects Tree |
| [**slidesSlidesDetailsGetId**](SlidesApi.md#slidesSlidesDetailsGetId) | **GET** /Slides/Details/{id} | Slides: Get Details |
| [**slidesSlidesGetId**](SlidesApi.md#slidesSlidesGetId) | **GET** /Slides/{id} | Slides: Get by Id |
| [**slidesSlidesOpenofficexmlGetIdUpdated**](SlidesApi.md#slidesSlidesOpenofficexmlGetIdUpdated) | **GET** /Slides/OpenOfficeXml/{id} | Slides: Get Underlying Xml |
| [**slidesSlidesOpenofficexmlPutId**](SlidesApi.md#slidesSlidesOpenofficexmlPutId) | **PUT** /Slides/OpenOfficeXml/{id} | Slides: Modify Underlying Xml |
| [**slidesSlidesSvgGetIdUseCache**](SlidesApi.md#slidesSlidesSvgGetIdUseCache) | **GET** /Slides/Svg/{id} | Slides: Get Svg file |


<a id="slidesSlidesChildobjectsGetId"></a>
# **slidesSlidesChildobjectsGetId**
> List&lt;ChildObjects&gt; slidesSlidesChildobjectsGetId(id)

Slides: Get Dependent Objects Tree

This endpoint is helpful for helping users and bots identify dependent objects to this Slide and retreive their corresponding metadata in order to make modifications to those objects in downstream operations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SlidesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    SlidesApi apiInstance = new SlidesApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      List<ChildObjects> result = apiInstance.slidesSlidesChildobjectsGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SlidesApi#slidesSlidesChildobjectsGetId");
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
| **id** | **UUID**|  | |

### Return type

[**List&lt;ChildObjects&gt;**](ChildObjects.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="slidesSlidesDetailsGetId"></a>
# **slidesSlidesDetailsGetId**
> SlideSlidesDetails slidesSlidesDetailsGetId(id)

Slides: Get Details

Returns object metadata and information about relative dependent objects 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SlidesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    SlidesApi apiInstance = new SlidesApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      SlideSlidesDetails result = apiInstance.slidesSlidesDetailsGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SlidesApi#slidesSlidesDetailsGetId");
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
| **id** | **UUID**|  | |

### Return type

[**SlideSlidesDetails**](SlideSlidesDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |

<a id="slidesSlidesGetId"></a>
# **slidesSlidesGetId**
> SlideSlides slidesSlidesGetId(id)

Slides: Get by Id

Get by Id: Use this method to retrieve a Slides object by its primary key (id)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SlidesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    SlidesApi apiInstance = new SlidesApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | An Id of the respository DTO elemennt
    try {
      SlideSlides result = apiInstance.slidesSlidesGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SlidesApi#slidesSlidesGetId");
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
| **id** | **UUID**| An Id of the respository DTO elemennt | |

### Return type

[**SlideSlides**](SlideSlides.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |

<a id="slidesSlidesOpenofficexmlGetIdUpdated"></a>
# **slidesSlidesOpenofficexmlGetIdUpdated**
> OoxmlDTO slidesSlidesOpenofficexmlGetIdUpdated(id, updated)

Slides: Get Underlying Xml

Return the subset of the xml content from within the latest edited version of the OpenXmlDocument from this Slide object.  The returned xml data conforms to the [Ecma-376 standard](http://www.ecma-international.org/publications/standards/Ecma-376.htm).  Use this endpoint a starting point for building client-side extensions that modify Presalytics widgets containing Slide objects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SlidesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    SlidesApi apiInstance = new SlidesApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    Boolean updated = true; // Boolean | Indicates whether API should return the orginal uploaded xml (false) or the actively updated version (true, default)
    try {
      OoxmlDTO result = apiInstance.slidesSlidesOpenofficexmlGetIdUpdated(id, updated);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SlidesApi#slidesSlidesOpenofficexmlGetIdUpdated");
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
| **id** | **UUID**|  | |
| **updated** | **Boolean**| Indicates whether API should return the orginal uploaded xml (false) or the actively updated version (true, default) | [optional] [default to true] |

### Return type

[**OoxmlDTO**](OoxmlDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="slidesSlidesOpenofficexmlPutId"></a>
# **slidesSlidesOpenofficexmlPutId**
> slidesSlidesOpenofficexmlPutId(id, ooxmlDTO)

Slides: Modify Underlying Xml

Directly eidt the underlying xml of a Slide object within an OpenOpenXml (e.g. Excel, Powerpoint) document. This endpoint will validatate the submitted xml against the [Ecma-376 standard](http://www.ecma-international.org/publications/standards/Ecma-376.htm) prior to saving modification.  Invalid xml will rejected by this endpoint and a (hopefully) helpful error message will be returned.  Use this endpoint for client-side automation of modifications ot Slide objects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SlidesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    SlidesApi apiInstance = new SlidesApi(defaultClient);
    String id = "id_example"; // String | 
    OoxmlDTO ooxmlDTO = new OoxmlDTO(); // OoxmlDTO | 
    try {
      apiInstance.slidesSlidesOpenofficexmlPutId(id, ooxmlDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling SlidesApi#slidesSlidesOpenofficexmlPutId");
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
| **id** | **String**|  | |
| **ooxmlDTO** | [**OoxmlDTO**](OoxmlDTO.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="slidesSlidesSvgGetIdUseCache"></a>
# **slidesSlidesSvgGetIdUseCache**
> File slidesSlidesSvgGetIdUseCache(id, useCache)

Slides: Get Svg file

This endpoint is helpful for rending this Slide as an svg or image object that can then be rendered in a story, dashboard or website.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SlidesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    SlidesApi apiInstance = new SlidesApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    Boolean useCache = false; // Boolean | Indicates whether API should retrieve content from a cache if aviable (true, default), or force an update (false)
    try {
      File result = apiInstance.slidesSlidesSvgGetIdUseCache(id, useCache);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SlidesApi#slidesSlidesSvgGetIdUseCache");
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
| **id** | **UUID**|  | |
| **useCache** | **Boolean**| Indicates whether API should retrieve content from a cache if aviable (true, default), or force an update (false) | [optional] [default to false] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/svg+xml, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an svg formatted-image of this object. |  -  |
| **400** | Bad Request |  -  |

