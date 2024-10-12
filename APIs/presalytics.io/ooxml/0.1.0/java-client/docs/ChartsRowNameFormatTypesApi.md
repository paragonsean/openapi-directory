# ChartsRowNameFormatTypesApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**chartRownameformattypesGet**](ChartsRowNameFormatTypesApi.md#chartRownameformattypesGet) | **GET** /Charts/RowNameFormatTypes | RowNameFormatTypes: List All Possible Types |
| [**chartRownameformattypesGetId**](ChartsRowNameFormatTypesApi.md#chartRownameformattypesGetId) | **GET** /Charts/RowNameFormatTypes/{id} | RowNameFormatTypes: Get by Id |
| [**chartRownameformattypesTypeidGetTypeId**](ChartsRowNameFormatTypesApi.md#chartRownameformattypesTypeidGetTypeId) | **GET** /Charts/RowNameFormatTypes/TypeId/{type_id} | RowNameFormatTypes: Get By Type Id |


<a id="chartRownameformattypesGet"></a>
# **chartRownameformattypesGet**
> List&lt;ChartRowNameFormatTypes&gt; chartRownameformattypesGet()

RowNameFormatTypes: List All Possible Types

List Types: Use this method to retreive a list of possible options for the RowNameFormatTypes type. Use the Id from oneof the returned elements on to make changes to elements in the Chart object space.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsRowNameFormatTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    ChartsRowNameFormatTypesApi apiInstance = new ChartsRowNameFormatTypesApi(defaultClient);
    try {
      List<ChartRowNameFormatTypes> result = apiInstance.chartRownameformattypesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsRowNameFormatTypesApi#chartRownameformattypesGet");
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

[**List&lt;ChartRowNameFormatTypes&gt;**](ChartRowNameFormatTypes.md)

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

<a id="chartRownameformattypesGetId"></a>
# **chartRownameformattypesGetId**
> ChartRowNameFormatTypes chartRownameformattypesGetId(id)

RowNameFormatTypes: Get by Id

Get by Id: Use this method to retrieve a RowNameFormatTypes object by its primary key (id)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsRowNameFormatTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    ChartsRowNameFormatTypesApi apiInstance = new ChartsRowNameFormatTypesApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      ChartRowNameFormatTypes result = apiInstance.chartRownameformattypesGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsRowNameFormatTypesApi#chartRownameformattypesGetId");
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

[**ChartRowNameFormatTypes**](ChartRowNameFormatTypes.md)

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

<a id="chartRownameformattypesTypeidGetTypeId"></a>
# **chartRownameformattypesTypeidGetTypeId**
> ChartRowNameFormatTypes chartRownameformattypesTypeidGetTypeId(typeId)

RowNameFormatTypes: Get By Type Id

This endpoint returns Type metadata from an integer type_id that can found on objects throughout the api.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsRowNameFormatTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    ChartsRowNameFormatTypesApi apiInstance = new ChartsRowNameFormatTypesApi(defaultClient);
    Integer typeId = 56; // Integer | 
    try {
      ChartRowNameFormatTypes result = apiInstance.chartRownameformattypesTypeidGetTypeId(typeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsRowNameFormatTypesApi#chartRownameformattypesTypeidGetTypeId");
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

[**ChartRowNameFormatTypes**](ChartRowNameFormatTypes.md)

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

