# ThemesIntensityApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**themesIntensityGet**](ThemesIntensityApi.md#themesIntensityGet) | **GET** /Themes/Intensity | Intensity: List All Possible Types |
| [**themesIntensityGetId**](ThemesIntensityApi.md#themesIntensityGetId) | **GET** /Themes/Intensity/{id} | Intensity: Get by Id |
| [**themesIntensityTypeidGetTypeId**](ThemesIntensityApi.md#themesIntensityTypeidGetTypeId) | **GET** /Themes/Intensity/TypeId/{type_id} | Intensity: Get By Type Id |


<a id="themesIntensityGet"></a>
# **themesIntensityGet**
> List&lt;ThemeIntensity&gt; themesIntensityGet()

Intensity: List All Possible Types

List Types: Use this method to retreive a list of possible options for the Intensity type. Use the Id from oneof the returned elements on to make changes to elements in the Themes object space.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ThemesIntensityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    ThemesIntensityApi apiInstance = new ThemesIntensityApi(defaultClient);
    try {
      List<ThemeIntensity> result = apiInstance.themesIntensityGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ThemesIntensityApi#themesIntensityGet");
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

[**List&lt;ThemeIntensity&gt;**](ThemeIntensity.md)

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

<a id="themesIntensityGetId"></a>
# **themesIntensityGetId**
> ThemeIntensity themesIntensityGetId(id)

Intensity: Get by Id

Get by Id: Use this method to retrieve a Intensity object by its primary key (id)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ThemesIntensityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    ThemesIntensityApi apiInstance = new ThemesIntensityApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      ThemeIntensity result = apiInstance.themesIntensityGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ThemesIntensityApi#themesIntensityGetId");
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

[**ThemeIntensity**](ThemeIntensity.md)

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

<a id="themesIntensityTypeidGetTypeId"></a>
# **themesIntensityTypeidGetTypeId**
> ThemeIntensity themesIntensityTypeidGetTypeId(typeId)

Intensity: Get By Type Id

This endpoint returns Type metadata from an integer type_id that can found on objects throughout the api.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ThemesIntensityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    ThemesIntensityApi apiInstance = new ThemesIntensityApi(defaultClient);
    Integer typeId = 56; // Integer | 
    try {
      ThemeIntensity result = apiInstance.themesIntensityTypeidGetTypeId(typeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ThemesIntensityApi#themesIntensityTypeidGetTypeId");
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

[**ThemeIntensity**](ThemeIntensity.md)

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

