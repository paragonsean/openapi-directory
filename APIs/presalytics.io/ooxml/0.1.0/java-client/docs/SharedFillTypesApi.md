# SharedFillTypesApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sharedFilltypesGet**](SharedFillTypesApi.md#sharedFilltypesGet) | **GET** /Shared/FillTypes | FillTypes: List All Possible Types |
| [**sharedFilltypesGetId**](SharedFillTypesApi.md#sharedFilltypesGetId) | **GET** /Shared/FillTypes/{id} | FillTypes: Get by Id |
| [**sharedFilltypesTypeidGetTypeId**](SharedFillTypesApi.md#sharedFilltypesTypeidGetTypeId) | **GET** /Shared/FillTypes/TypeId/{type_id} | FillTypes: Get By Type Id |


<a id="sharedFilltypesGet"></a>
# **sharedFilltypesGet**
> List&lt;SharedFillTypes&gt; sharedFilltypesGet()

FillTypes: List All Possible Types

List Types: Use this method to retreive a list of possible options for the FillTypes type. Use the Id from oneof the returned elements on to make changes to elements in the Shared object space.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedFillTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    SharedFillTypesApi apiInstance = new SharedFillTypesApi(defaultClient);
    try {
      List<SharedFillTypes> result = apiInstance.sharedFilltypesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedFillTypesApi#sharedFilltypesGet");
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

[**List&lt;SharedFillTypes&gt;**](SharedFillTypes.md)

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

<a id="sharedFilltypesGetId"></a>
# **sharedFilltypesGetId**
> SharedFillTypes sharedFilltypesGetId(id)

FillTypes: Get by Id

Get by Id: Use this method to retrieve a FillTypes object by its primary key (id)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedFillTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    SharedFillTypesApi apiInstance = new SharedFillTypesApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      SharedFillTypes result = apiInstance.sharedFilltypesGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedFillTypesApi#sharedFilltypesGetId");
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

[**SharedFillTypes**](SharedFillTypes.md)

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

<a id="sharedFilltypesTypeidGetTypeId"></a>
# **sharedFilltypesTypeidGetTypeId**
> SharedFillTypes sharedFilltypesTypeidGetTypeId(typeId)

FillTypes: Get By Type Id

This endpoint returns Type metadata from an integer type_id that can found on objects throughout the api.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedFillTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    SharedFillTypesApi apiInstance = new SharedFillTypesApi(defaultClient);
    Integer typeId = 56; // Integer | 
    try {
      SharedFillTypes result = apiInstance.sharedFilltypesTypeidGetTypeId(typeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedFillTypesApi#sharedFilltypesTypeidGetTypeId");
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

[**SharedFillTypes**](SharedFillTypes.md)

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

