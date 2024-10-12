# ChartsAxisDataTypesApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**chartAxisdatatypesGet**](ChartsAxisDataTypesApi.md#chartAxisdatatypesGet) | **GET** /Charts/AxisDataTypes | AxisDataTypes: List All Possible Types |
| [**chartAxisdatatypesGetId**](ChartsAxisDataTypesApi.md#chartAxisdatatypesGetId) | **GET** /Charts/AxisDataTypes/{id} | AxisDataTypes: Get by Id |
| [**chartAxisdatatypesTypeidGetTypeId**](ChartsAxisDataTypesApi.md#chartAxisdatatypesTypeidGetTypeId) | **GET** /Charts/AxisDataTypes/TypeId/{type_id} | AxisDataTypes: Get By Type Id |


<a id="chartAxisdatatypesGet"></a>
# **chartAxisdatatypesGet**
> List&lt;ChartAxisDataTypes&gt; chartAxisdatatypesGet()

AxisDataTypes: List All Possible Types

List Types: Use this method to retreive a list of possible options for the AxisDataTypes type. Use the Id from oneof the returned elements on to make changes to elements in the Chart object space.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsAxisDataTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    ChartsAxisDataTypesApi apiInstance = new ChartsAxisDataTypesApi(defaultClient);
    try {
      List<ChartAxisDataTypes> result = apiInstance.chartAxisdatatypesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsAxisDataTypesApi#chartAxisdatatypesGet");
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

[**List&lt;ChartAxisDataTypes&gt;**](ChartAxisDataTypes.md)

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

<a id="chartAxisdatatypesGetId"></a>
# **chartAxisdatatypesGetId**
> ChartAxisDataTypes chartAxisdatatypesGetId(id)

AxisDataTypes: Get by Id

Get by Id: Use this method to retrieve a AxisDataTypes object by its primary key (id)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsAxisDataTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    ChartsAxisDataTypesApi apiInstance = new ChartsAxisDataTypesApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      ChartAxisDataTypes result = apiInstance.chartAxisdatatypesGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsAxisDataTypesApi#chartAxisdatatypesGetId");
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

[**ChartAxisDataTypes**](ChartAxisDataTypes.md)

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

<a id="chartAxisdatatypesTypeidGetTypeId"></a>
# **chartAxisdatatypesTypeidGetTypeId**
> ChartAxisDataTypes chartAxisdatatypesTypeidGetTypeId(typeId)

AxisDataTypes: Get By Type Id

This endpoint returns Type metadata from an integer type_id that can found on objects throughout the api.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsAxisDataTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    ChartsAxisDataTypesApi apiInstance = new ChartsAxisDataTypesApi(defaultClient);
    Integer typeId = 56; // Integer | 
    try {
      ChartAxisDataTypes result = apiInstance.chartAxisdatatypesTypeidGetTypeId(typeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsAxisDataTypesApi#chartAxisdatatypesTypeidGetTypeId");
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

[**ChartAxisDataTypes**](ChartAxisDataTypes.md)

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

