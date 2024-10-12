# SharedLineEndTypesApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sharedLineendtypesGet**](SharedLineEndTypesApi.md#sharedLineendtypesGet) | **GET** /Shared/LineEndTypes | LineEndTypes: List All Possible Types |
| [**sharedLineendtypesGetId**](SharedLineEndTypesApi.md#sharedLineendtypesGetId) | **GET** /Shared/LineEndTypes/{id} | LineEndTypes: Get by Id |
| [**sharedLineendtypesTypeidGetTypeId**](SharedLineEndTypesApi.md#sharedLineendtypesTypeidGetTypeId) | **GET** /Shared/LineEndTypes/TypeId/{type_id} | LineEndTypes: Get By Type Id |


<a id="sharedLineendtypesGet"></a>
# **sharedLineendtypesGet**
> List&lt;SharedLineEndTypes&gt; sharedLineendtypesGet()

LineEndTypes: List All Possible Types

List Types: Use this method to retreive a list of possible options for the LineEndTypes type. Use the Id from oneof the returned elements on to make changes to elements in the Shared object space.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedLineEndTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    SharedLineEndTypesApi apiInstance = new SharedLineEndTypesApi(defaultClient);
    try {
      List<SharedLineEndTypes> result = apiInstance.sharedLineendtypesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedLineEndTypesApi#sharedLineendtypesGet");
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

[**List&lt;SharedLineEndTypes&gt;**](SharedLineEndTypes.md)

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

<a id="sharedLineendtypesGetId"></a>
# **sharedLineendtypesGetId**
> SharedLineEndTypes sharedLineendtypesGetId(id)

LineEndTypes: Get by Id

Get by Id: Use this method to retrieve a LineEndTypes object by its primary key (id)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedLineEndTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    SharedLineEndTypesApi apiInstance = new SharedLineEndTypesApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      SharedLineEndTypes result = apiInstance.sharedLineendtypesGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedLineEndTypesApi#sharedLineendtypesGetId");
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

[**SharedLineEndTypes**](SharedLineEndTypes.md)

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

<a id="sharedLineendtypesTypeidGetTypeId"></a>
# **sharedLineendtypesTypeidGetTypeId**
> SharedLineEndTypes sharedLineendtypesTypeidGetTypeId(typeId)

LineEndTypes: Get By Type Id

This endpoint returns Type metadata from an integer type_id that can found on objects throughout the api.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedLineEndTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    SharedLineEndTypesApi apiInstance = new SharedLineEndTypesApi(defaultClient);
    Integer typeId = 56; // Integer | 
    try {
      SharedLineEndTypes result = apiInstance.sharedLineendtypesTypeidGetTypeId(typeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedLineEndTypesApi#sharedLineendtypesTypeidGetTypeId");
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

[**SharedLineEndTypes**](SharedLineEndTypes.md)

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

