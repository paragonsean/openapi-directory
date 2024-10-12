# SharedColorTypesApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sharedColortypesGet**](SharedColorTypesApi.md#sharedColortypesGet) | **GET** /Shared/ColorTypes | ColorTypes: List All Possible Types |
| [**sharedColortypesGetId**](SharedColorTypesApi.md#sharedColortypesGetId) | **GET** /Shared/ColorTypes/{id} | ColorTypes: Get by Id |
| [**sharedColortypesTypeidGetTypeId**](SharedColorTypesApi.md#sharedColortypesTypeidGetTypeId) | **GET** /Shared/ColorTypes/TypeId/{type_id} | ColorTypes: Get By Type Id |


<a id="sharedColortypesGet"></a>
# **sharedColortypesGet**
> List&lt;SharedColorTypes&gt; sharedColortypesGet()

ColorTypes: List All Possible Types

List Types: Use this method to retreive a list of possible options for the ColorTypes type. Use the Id from oneof the returned elements on to make changes to elements in the Shared object space.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedColorTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    SharedColorTypesApi apiInstance = new SharedColorTypesApi(defaultClient);
    try {
      List<SharedColorTypes> result = apiInstance.sharedColortypesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedColorTypesApi#sharedColortypesGet");
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

[**List&lt;SharedColorTypes&gt;**](SharedColorTypes.md)

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

<a id="sharedColortypesGetId"></a>
# **sharedColortypesGetId**
> SharedColorTypes sharedColortypesGetId(id)

ColorTypes: Get by Id

Get by Id: Use this method to retrieve a ColorTypes object by its primary key (id)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedColorTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    SharedColorTypesApi apiInstance = new SharedColorTypesApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      SharedColorTypes result = apiInstance.sharedColortypesGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedColorTypesApi#sharedColortypesGetId");
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

[**SharedColorTypes**](SharedColorTypes.md)

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

<a id="sharedColortypesTypeidGetTypeId"></a>
# **sharedColortypesTypeidGetTypeId**
> SharedColorTypes sharedColortypesTypeidGetTypeId(typeId)

ColorTypes: Get By Type Id

This endpoint returns Type metadata from an integer type_id that can found on objects throughout the api.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedColorTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    SharedColorTypesApi apiInstance = new SharedColorTypesApi(defaultClient);
    Integer typeId = 56; // Integer | 
    try {
      SharedColorTypes result = apiInstance.sharedColortypesTypeidGetTypeId(typeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedColorTypesApi#sharedColortypesTypeidGetTypeId");
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

[**SharedColorTypes**](SharedColorTypes.md)

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

