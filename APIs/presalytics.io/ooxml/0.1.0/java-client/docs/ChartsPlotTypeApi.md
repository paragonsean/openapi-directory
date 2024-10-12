# ChartsPlotTypeApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**chartPlottypeGet**](ChartsPlotTypeApi.md#chartPlottypeGet) | **GET** /Charts/PlotType | PlotType: List All Possible Types |
| [**chartPlottypeGetId**](ChartsPlotTypeApi.md#chartPlottypeGetId) | **GET** /Charts/PlotType/{id} | PlotType: Get by Id |
| [**chartPlottypeTypeidGetTypeId**](ChartsPlotTypeApi.md#chartPlottypeTypeidGetTypeId) | **GET** /Charts/PlotType/TypeId/{type_id} | PlotType: Get By Type Id |


<a id="chartPlottypeGet"></a>
# **chartPlottypeGet**
> List&lt;ChartPlotType&gt; chartPlottypeGet()

PlotType: List All Possible Types

List Types: Use this method to retreive a list of possible options for the PlotType type. Use the Id from oneof the returned elements on to make changes to elements in the Chart object space.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsPlotTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    ChartsPlotTypeApi apiInstance = new ChartsPlotTypeApi(defaultClient);
    try {
      List<ChartPlotType> result = apiInstance.chartPlottypeGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsPlotTypeApi#chartPlottypeGet");
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

[**List&lt;ChartPlotType&gt;**](ChartPlotType.md)

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

<a id="chartPlottypeGetId"></a>
# **chartPlottypeGetId**
> ChartPlotType chartPlottypeGetId(id)

PlotType: Get by Id

Get by Id: Use this method to retrieve a PlotType object by its primary key (id)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsPlotTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    ChartsPlotTypeApi apiInstance = new ChartsPlotTypeApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      ChartPlotType result = apiInstance.chartPlottypeGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsPlotTypeApi#chartPlottypeGetId");
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

[**ChartPlotType**](ChartPlotType.md)

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

<a id="chartPlottypeTypeidGetTypeId"></a>
# **chartPlottypeTypeidGetTypeId**
> ChartPlotType chartPlottypeTypeidGetTypeId(typeId)

PlotType: Get By Type Id

This endpoint returns Type metadata from an integer type_id that can found on objects throughout the api.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsPlotTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    ChartsPlotTypeApi apiInstance = new ChartsPlotTypeApi(defaultClient);
    Integer typeId = 56; // Integer | 
    try {
      ChartPlotType result = apiInstance.chartPlottypeTypeidGetTypeId(typeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsPlotTypeApi#chartPlottypeTypeidGetTypeId");
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

[**ChartPlotType**](ChartPlotType.md)

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

