# SharedDashTypesApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sharedDashtypesGet**](SharedDashTypesApi.md#sharedDashtypesGet) | **GET** /Shared/DashTypes | DashTypes: List All Possible Types |
| [**sharedDashtypesGetId**](SharedDashTypesApi.md#sharedDashtypesGetId) | **GET** /Shared/DashTypes/{id} | DashTypes: Get by Id |
| [**sharedDashtypesTypeidGetTypeId**](SharedDashTypesApi.md#sharedDashtypesTypeidGetTypeId) | **GET** /Shared/DashTypes/TypeId/{type_id} | DashTypes: Get By Type Id |


<a id="sharedDashtypesGet"></a>
# **sharedDashtypesGet**
> List&lt;SharedDashTypes&gt; sharedDashtypesGet()

DashTypes: List All Possible Types

List Types: Use this method to retreive a list of possible options for the DashTypes type. Use the Id from oneof the returned elements on to make changes to elements in the Shared object space.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedDashTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    SharedDashTypesApi apiInstance = new SharedDashTypesApi(defaultClient);
    try {
      List<SharedDashTypes> result = apiInstance.sharedDashtypesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedDashTypesApi#sharedDashtypesGet");
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

[**List&lt;SharedDashTypes&gt;**](SharedDashTypes.md)

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

<a id="sharedDashtypesGetId"></a>
# **sharedDashtypesGetId**
> SharedDashTypes sharedDashtypesGetId(id)

DashTypes: Get by Id

Get by Id: Use this method to retrieve a DashTypes object by its primary key (id)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedDashTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    SharedDashTypesApi apiInstance = new SharedDashTypesApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      SharedDashTypes result = apiInstance.sharedDashtypesGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedDashTypesApi#sharedDashtypesGetId");
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

[**SharedDashTypes**](SharedDashTypes.md)

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

<a id="sharedDashtypesTypeidGetTypeId"></a>
# **sharedDashtypesTypeidGetTypeId**
> SharedDashTypes sharedDashtypesTypeidGetTypeId(typeId)

DashTypes: Get By Type Id

This endpoint returns Type metadata from an integer type_id that can found on objects throughout the api.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedDashTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    SharedDashTypesApi apiInstance = new SharedDashTypesApi(defaultClient);
    Integer typeId = 56; // Integer | 
    try {
      SharedDashTypes result = apiInstance.sharedDashtypesTypeidGetTypeId(typeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedDashTypesApi#sharedDashtypesTypeidGetTypeId");
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

[**SharedDashTypes**](SharedDashTypes.md)

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

