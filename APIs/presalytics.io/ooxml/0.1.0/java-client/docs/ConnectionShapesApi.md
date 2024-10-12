# ConnectionShapesApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**slidesConnectionshapesChildobjectsGetId**](ConnectionShapesApi.md#slidesConnectionshapesChildobjectsGetId) | **GET** /ConnectionShapes/ChildObjects/{id} | Slides: Get Dependent Objects Tree |
| [**slidesConnectionshapesDetailsGetId**](ConnectionShapesApi.md#slidesConnectionshapesDetailsGetId) | **GET** /ConnectionShapes/Details/{id} | Slides: Get Details |
| [**slidesConnectionshapesGetId**](ConnectionShapesApi.md#slidesConnectionshapesGetId) | **GET** /ConnectionShapes/{id} | ConnectionShapes: Get by Id |
| [**slidesConnectionshapesOpenofficexmlGetIdUpdated**](ConnectionShapesApi.md#slidesConnectionshapesOpenofficexmlGetIdUpdated) | **GET** /ConnectionShapes/OpenOfficeXml/{id} | Slides: Get Underlying Xml |
| [**slidesConnectionshapesOpenofficexmlPutId**](ConnectionShapesApi.md#slidesConnectionshapesOpenofficexmlPutId) | **PUT** /ConnectionShapes/OpenOfficeXml/{id} | Slides: Modify Underlying Xml |
| [**slidesConnectionshapesSvgGetIdUseCache**](ConnectionShapesApi.md#slidesConnectionshapesSvgGetIdUseCache) | **GET** /ConnectionShapes/Svg/{id} | Slides: Get Svg file |


<a id="slidesConnectionshapesChildobjectsGetId"></a>
# **slidesConnectionshapesChildobjectsGetId**
> List&lt;ChildObjects&gt; slidesConnectionshapesChildobjectsGetId(id)

Slides: Get Dependent Objects Tree

This endpoint is helpful for helping users and bots identify dependent objects to this Slide and retreive their corresponding metadata in order to make modifications to those objects in downstream operations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectionShapesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    ConnectionShapesApi apiInstance = new ConnectionShapesApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      List<ChildObjects> result = apiInstance.slidesConnectionshapesChildobjectsGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectionShapesApi#slidesConnectionshapesChildobjectsGetId");
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

<a id="slidesConnectionshapesDetailsGetId"></a>
# **slidesConnectionshapesDetailsGetId**
> SlideConnectorDetails slidesConnectionshapesDetailsGetId(id)

Slides: Get Details

Returns object metadata and information about relative dependent objects 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectionShapesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    ConnectionShapesApi apiInstance = new ConnectionShapesApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      SlideConnectorDetails result = apiInstance.slidesConnectionshapesDetailsGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectionShapesApi#slidesConnectionshapesDetailsGetId");
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

[**SlideConnectorDetails**](SlideConnectorDetails.md)

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

<a id="slidesConnectionshapesGetId"></a>
# **slidesConnectionshapesGetId**
> SlideConnector slidesConnectionshapesGetId(id)

ConnectionShapes: Get by Id

Get by Id: Use this method to retrieve a ConnectionShapes object by its primary key (id)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectionShapesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    ConnectionShapesApi apiInstance = new ConnectionShapesApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | An Id of the respository DTO elemennt
    try {
      SlideConnector result = apiInstance.slidesConnectionshapesGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectionShapesApi#slidesConnectionshapesGetId");
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

[**SlideConnector**](SlideConnector.md)

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

<a id="slidesConnectionshapesOpenofficexmlGetIdUpdated"></a>
# **slidesConnectionshapesOpenofficexmlGetIdUpdated**
> OoxmlDTO slidesConnectionshapesOpenofficexmlGetIdUpdated(id, updated)

Slides: Get Underlying Xml

Return the subset of the xml content from within the latest edited version of the OpenXmlDocument from this Slide object.  The returned xml data conforms to the [Ecma-376 standard](http://www.ecma-international.org/publications/standards/Ecma-376.htm).  Use this endpoint a starting point for building client-side extensions that modify Presalytics widgets containing Slide objects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectionShapesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    ConnectionShapesApi apiInstance = new ConnectionShapesApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    Boolean updated = true; // Boolean | Indicates whether API should return the orginal uploaded xml (false) or the actively updated version (true, default)
    try {
      OoxmlDTO result = apiInstance.slidesConnectionshapesOpenofficexmlGetIdUpdated(id, updated);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectionShapesApi#slidesConnectionshapesOpenofficexmlGetIdUpdated");
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

<a id="slidesConnectionshapesOpenofficexmlPutId"></a>
# **slidesConnectionshapesOpenofficexmlPutId**
> slidesConnectionshapesOpenofficexmlPutId(id, ooxmlDTO)

Slides: Modify Underlying Xml

Directly eidt the underlying xml of a Slide object within an OpenOpenXml (e.g. Excel, Powerpoint) document. This endpoint will validatate the submitted xml against the [Ecma-376 standard](http://www.ecma-international.org/publications/standards/Ecma-376.htm) prior to saving modification.  Invalid xml will rejected by this endpoint and a (hopefully) helpful error message will be returned.  Use this endpoint for client-side automation of modifications ot Slide objects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectionShapesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    ConnectionShapesApi apiInstance = new ConnectionShapesApi(defaultClient);
    String id = "id_example"; // String | 
    OoxmlDTO ooxmlDTO = new OoxmlDTO(); // OoxmlDTO | 
    try {
      apiInstance.slidesConnectionshapesOpenofficexmlPutId(id, ooxmlDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectionShapesApi#slidesConnectionshapesOpenofficexmlPutId");
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

<a id="slidesConnectionshapesSvgGetIdUseCache"></a>
# **slidesConnectionshapesSvgGetIdUseCache**
> File slidesConnectionshapesSvgGetIdUseCache(id, useCache)

Slides: Get Svg file

This endpoint is helpful for rending this Slide as an svg or image object that can then be rendered in a story, dashboard or website.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectionShapesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    ConnectionShapesApi apiInstance = new ConnectionShapesApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    Boolean useCache = false; // Boolean | Indicates whether API should retrieve content from a cache if aviable (true, default), or force an update (false)
    try {
      File result = apiInstance.slidesConnectionshapesSvgGetIdUseCache(id, useCache);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectionShapesApi#slidesConnectionshapesSvgGetIdUseCache");
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

