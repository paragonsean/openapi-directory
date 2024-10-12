# SharedEffectTypesApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sharedEffecttypesGet**](SharedEffectTypesApi.md#sharedEffecttypesGet) | **GET** /Shared/EffectTypes | EffectTypes: List All Possible Types |
| [**sharedEffecttypesGetId**](SharedEffectTypesApi.md#sharedEffecttypesGetId) | **GET** /Shared/EffectTypes/{id} | EffectTypes: Get by Id |
| [**sharedEffecttypesTypeidGetTypeId**](SharedEffectTypesApi.md#sharedEffecttypesTypeidGetTypeId) | **GET** /Shared/EffectTypes/TypeId/{type_id} | EffectTypes: Get By Type Id |


<a id="sharedEffecttypesGet"></a>
# **sharedEffecttypesGet**
> List&lt;SharedEffectTypes&gt; sharedEffecttypesGet()

EffectTypes: List All Possible Types

List Types: Use this method to retreive a list of possible options for the EffectTypes type. Use the Id from oneof the returned elements on to make changes to elements in the Shared object space.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedEffectTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    SharedEffectTypesApi apiInstance = new SharedEffectTypesApi(defaultClient);
    try {
      List<SharedEffectTypes> result = apiInstance.sharedEffecttypesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedEffectTypesApi#sharedEffecttypesGet");
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

[**List&lt;SharedEffectTypes&gt;**](SharedEffectTypes.md)

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

<a id="sharedEffecttypesGetId"></a>
# **sharedEffecttypesGetId**
> SharedEffectTypes sharedEffecttypesGetId(id)

EffectTypes: Get by Id

Get by Id: Use this method to retrieve a EffectTypes object by its primary key (id)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedEffectTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    SharedEffectTypesApi apiInstance = new SharedEffectTypesApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      SharedEffectTypes result = apiInstance.sharedEffecttypesGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedEffectTypesApi#sharedEffecttypesGetId");
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

[**SharedEffectTypes**](SharedEffectTypes.md)

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

<a id="sharedEffecttypesTypeidGetTypeId"></a>
# **sharedEffecttypesTypeidGetTypeId**
> SharedEffectTypes sharedEffecttypesTypeidGetTypeId(typeId)

EffectTypes: Get By Type Id

This endpoint returns Type metadata from an integer type_id that can found on objects throughout the api.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedEffectTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    SharedEffectTypesApi apiInstance = new SharedEffectTypesApi(defaultClient);
    Integer typeId = 56; // Integer | 
    try {
      SharedEffectTypes result = apiInstance.sharedEffecttypesTypeidGetTypeId(typeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedEffectTypesApi#sharedEffecttypesTypeidGetTypeId");
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

[**SharedEffectTypes**](SharedEffectTypes.md)

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

