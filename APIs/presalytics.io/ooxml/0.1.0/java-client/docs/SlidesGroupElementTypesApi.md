# SlidesGroupElementTypesApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**slidesGroupelementtypesGet**](SlidesGroupElementTypesApi.md#slidesGroupelementtypesGet) | **GET** /Slides/GroupElementTypes | GroupElementTypes: List All Possible Types |
| [**slidesGroupelementtypesGetId**](SlidesGroupElementTypesApi.md#slidesGroupelementtypesGetId) | **GET** /Slides/GroupElementTypes/{id} | GroupElementTypes: Get by Id |
| [**slidesGroupelementtypesTypeidGetTypeId**](SlidesGroupElementTypesApi.md#slidesGroupelementtypesTypeidGetTypeId) | **GET** /Slides/GroupElementTypes/TypeId/{type_id} | GroupElementTypes: Get By Type Id |


<a id="slidesGroupelementtypesGet"></a>
# **slidesGroupelementtypesGet**
> List&lt;SlideGroupElementTypes&gt; slidesGroupelementtypesGet()

GroupElementTypes: List All Possible Types

List Types: Use this method to retreive a list of possible options for the GroupElementTypes type. Use the Id from oneof the returned elements on to make changes to elements in the Slides object space.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SlidesGroupElementTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    SlidesGroupElementTypesApi apiInstance = new SlidesGroupElementTypesApi(defaultClient);
    try {
      List<SlideGroupElementTypes> result = apiInstance.slidesGroupelementtypesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SlidesGroupElementTypesApi#slidesGroupelementtypesGet");
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

[**List&lt;SlideGroupElementTypes&gt;**](SlideGroupElementTypes.md)

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

<a id="slidesGroupelementtypesGetId"></a>
# **slidesGroupelementtypesGetId**
> SlideGroupElementTypes slidesGroupelementtypesGetId(id)

GroupElementTypes: Get by Id

Get by Id: Use this method to retrieve a GroupElementTypes object by its primary key (id)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SlidesGroupElementTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    SlidesGroupElementTypesApi apiInstance = new SlidesGroupElementTypesApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      SlideGroupElementTypes result = apiInstance.slidesGroupelementtypesGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SlidesGroupElementTypesApi#slidesGroupelementtypesGetId");
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

[**SlideGroupElementTypes**](SlideGroupElementTypes.md)

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

<a id="slidesGroupelementtypesTypeidGetTypeId"></a>
# **slidesGroupelementtypesTypeidGetTypeId**
> SlideGroupElementTypes slidesGroupelementtypesTypeidGetTypeId(typeId)

GroupElementTypes: Get By Type Id

This endpoint returns Type metadata from an integer type_id that can found on objects throughout the api.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SlidesGroupElementTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    SlidesGroupElementTypesApi apiInstance = new SlidesGroupElementTypesApi(defaultClient);
    Integer typeId = 56; // Integer | 
    try {
      SlideGroupElementTypes result = apiInstance.slidesGroupelementtypesTypeidGetTypeId(typeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SlidesGroupElementTypesApi#slidesGroupelementtypesTypeidGetTypeId");
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

[**SlideGroupElementTypes**](SlideGroupElementTypes.md)

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

