# ImagesApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sharedImagesChildobjectsGetId**](ImagesApi.md#sharedImagesChildobjectsGetId) | **GET** /Images/ChildObjects/{id} | Shared: Get Dependent Objects Tree |
| [**sharedImagesDetailsGetId**](ImagesApi.md#sharedImagesDetailsGetId) | **GET** /Images/Details/{id} | Shared: Get Details |
| [**sharedImagesGetId**](ImagesApi.md#sharedImagesGetId) | **GET** /Images/{id} | Images: Get by Id |
| [**sharedImagesGetimagePutId**](ImagesApi.md#sharedImagesGetimagePutId) | **PUT** /Images/GetImage/{Id} | Image: Download Image |
| [**sharedImagesOpenofficexmlGetIdUpdated**](ImagesApi.md#sharedImagesOpenofficexmlGetIdUpdated) | **GET** /Images/OpenOfficeXml/{id} | Shared: Get Underlying Xml |
| [**sharedImagesOpenofficexmlPutId**](ImagesApi.md#sharedImagesOpenofficexmlPutId) | **PUT** /Images/OpenOfficeXml/{id} | Shared: Modify Underlying Xml |
| [**sharedImagesSvgGetIdUseCache**](ImagesApi.md#sharedImagesSvgGetIdUseCache) | **GET** /Images/Svg/{id} | Shared: Get Svg file |


<a id="sharedImagesChildobjectsGetId"></a>
# **sharedImagesChildobjectsGetId**
> List&lt;ChildObjects&gt; sharedImagesChildobjectsGetId(id)

Shared: Get Dependent Objects Tree

This endpoint is helpful for helping users and bots identify dependent objects to this Shared and retreive their corresponding metadata in order to make modifications to those objects in downstream operations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      List<ChildObjects> result = apiInstance.sharedImagesChildobjectsGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#sharedImagesChildobjectsGetId");
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

<a id="sharedImagesDetailsGetId"></a>
# **sharedImagesDetailsGetId**
> SharedPicturesDetails sharedImagesDetailsGetId(id)

Shared: Get Details

Returns object metadata and information about relative dependent objects 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      SharedPicturesDetails result = apiInstance.sharedImagesDetailsGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#sharedImagesDetailsGetId");
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

[**SharedPicturesDetails**](SharedPicturesDetails.md)

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

<a id="sharedImagesGetId"></a>
# **sharedImagesGetId**
> SharedPictures sharedImagesGetId(id)

Images: Get by Id

Get by Id: Use this method to retrieve a Images object by its primary key (id)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | An Id of the respository DTO elemennt
    try {
      SharedPictures result = apiInstance.sharedImagesGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#sharedImagesGetId");
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

[**SharedPictures**](SharedPictures.md)

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

<a id="sharedImagesGetimagePutId"></a>
# **sharedImagesGetimagePutId**
> sharedImagesGetimagePutId(id)

Image: Download Image

Download Images extracted from Ooxml Documents

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | The Image Id
    try {
      apiInstance.sharedImagesGetimagePutId(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#sharedImagesGetimagePutId");
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
| **id** | **UUID**| The Image Id | |

### Return type

null (empty response body)

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
| **504** | Server Error |  -  |

<a id="sharedImagesOpenofficexmlGetIdUpdated"></a>
# **sharedImagesOpenofficexmlGetIdUpdated**
> OoxmlDTO sharedImagesOpenofficexmlGetIdUpdated(id, updated)

Shared: Get Underlying Xml

Return the subset of the xml content from within the latest edited version of the OpenXmlDocument from this Shared object.  The returned xml data conforms to the [Ecma-376 standard](http://www.ecma-international.org/publications/standards/Ecma-376.htm).  Use this endpoint a starting point for building client-side extensions that modify Presalytics widgets containing Shared objects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    Boolean updated = true; // Boolean | Indicates whether API should return the orginal uploaded xml (false) or the actively updated version (true, default)
    try {
      OoxmlDTO result = apiInstance.sharedImagesOpenofficexmlGetIdUpdated(id, updated);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#sharedImagesOpenofficexmlGetIdUpdated");
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

<a id="sharedImagesOpenofficexmlPutId"></a>
# **sharedImagesOpenofficexmlPutId**
> sharedImagesOpenofficexmlPutId(id, ooxmlDTO)

Shared: Modify Underlying Xml

Directly eidt the underlying xml of a Shared object within an OpenOpenXml (e.g. Excel, Powerpoint) document. This endpoint will validatate the submitted xml against the [Ecma-376 standard](http://www.ecma-international.org/publications/standards/Ecma-376.htm) prior to saving modification.  Invalid xml will rejected by this endpoint and a (hopefully) helpful error message will be returned.  Use this endpoint for client-side automation of modifications ot Shared objects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    String id = "id_example"; // String | 
    OoxmlDTO ooxmlDTO = new OoxmlDTO(); // OoxmlDTO | 
    try {
      apiInstance.sharedImagesOpenofficexmlPutId(id, ooxmlDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#sharedImagesOpenofficexmlPutId");
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

<a id="sharedImagesSvgGetIdUseCache"></a>
# **sharedImagesSvgGetIdUseCache**
> File sharedImagesSvgGetIdUseCache(id, useCache)

Shared: Get Svg file

This endpoint is helpful for rending this Shared as an svg or image object that can then be rendered in a story, dashboard or website.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    Boolean useCache = false; // Boolean | Indicates whether API should retrieve content from a cache if aviable (true, default), or force an update (false)
    try {
      File result = apiInstance.sharedImagesSvgGetIdUseCache(id, useCache);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#sharedImagesSvgGetIdUseCache");
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

