# SlidesGraphicTypesApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**slidesGraphictypesGet**](SlidesGraphicTypesApi.md#slidesGraphictypesGet) | **GET** /Slides/GraphicTypes | GraphicTypes: List All Possible Types |
| [**slidesGraphictypesGetId**](SlidesGraphicTypesApi.md#slidesGraphictypesGetId) | **GET** /Slides/GraphicTypes/{id} | GraphicTypes: Get by Id |
| [**slidesGraphictypesTypeidGetTypeId**](SlidesGraphicTypesApi.md#slidesGraphictypesTypeidGetTypeId) | **GET** /Slides/GraphicTypes/TypeId/{type_id} | GraphicTypes: Get By Type Id |


<a id="slidesGraphictypesGet"></a>
# **slidesGraphictypesGet**
> List&lt;SlideGraphicTypes&gt; slidesGraphictypesGet()

GraphicTypes: List All Possible Types

List Types: Use this method to retreive a list of possible options for the GraphicTypes type. Use the Id from oneof the returned elements on to make changes to elements in the Slides object space.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SlidesGraphicTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    SlidesGraphicTypesApi apiInstance = new SlidesGraphicTypesApi(defaultClient);
    try {
      List<SlideGraphicTypes> result = apiInstance.slidesGraphictypesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SlidesGraphicTypesApi#slidesGraphictypesGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;SlideGraphicTypes&gt;**](SlideGraphicTypes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |

<a id="slidesGraphictypesGetId"></a>
# **slidesGraphictypesGetId**
> SlideGraphicTypes slidesGraphictypesGetId(id)

GraphicTypes: Get by Id

Get by Id: Use this method to retrieve a GraphicTypes object by its primary key (id)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SlidesGraphicTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    SlidesGraphicTypesApi apiInstance = new SlidesGraphicTypesApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      SlideGraphicTypes result = apiInstance.slidesGraphictypesGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SlidesGraphicTypesApi#slidesGraphictypesGetId");
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

[**SlideGraphicTypes**](SlideGraphicTypes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |

<a id="slidesGraphictypesTypeidGetTypeId"></a>
# **slidesGraphictypesTypeidGetTypeId**
> SlideGraphicTypes slidesGraphictypesTypeidGetTypeId(typeId)

GraphicTypes: Get By Type Id

This endpoint returns Type metadata from an integer type_id that can found on objects throughout the api.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SlidesGraphicTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    SlidesGraphicTypesApi apiInstance = new SlidesGraphicTypesApi(defaultClient);
    Integer typeId = 56; // Integer | 
    try {
      SlideGraphicTypes result = apiInstance.slidesGraphictypesTypeidGetTypeId(typeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SlidesGraphicTypesApi#slidesGraphictypesTypeidGetTypeId");
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
| **typeId** | **Integer**|  | |

### Return type

[**SlideGraphicTypes**](SlideGraphicTypes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |

