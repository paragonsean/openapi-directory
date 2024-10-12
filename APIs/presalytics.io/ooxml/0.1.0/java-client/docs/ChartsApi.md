# ChartsApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**chartsChartsChartupdateGetId**](ChartsApi.md#chartsChartsChartupdateGetId) | **GET** /Charts/ChartUpdate/{id} | Charts: Get Chart Data |
| [**chartsChartsChartupdatePutId**](ChartsApi.md#chartsChartsChartupdatePutId) | **PUT** /Charts/ChartUpdate/{id} | Charts: Update Chart Data |
| [**chartsChartsChildobjectsGetId**](ChartsApi.md#chartsChartsChildobjectsGetId) | **GET** /Charts/ChildObjects/{id} | Charts: Get Dependent Objects Tree |
| [**chartsChartsDetailsGetId**](ChartsApi.md#chartsChartsDetailsGetId) | **GET** /Charts/Details/{id} | Charts: Get Details |
| [**chartsChartsGetId**](ChartsApi.md#chartsChartsGetId) | **GET** /Charts/{id} | Charts: Get by Id |
| [**chartsChartsOpenofficexmlGetIdUpdated**](ChartsApi.md#chartsChartsOpenofficexmlGetIdUpdated) | **GET** /Charts/OpenOfficeXml/{id} | Charts: Get Underlying Xml |
| [**chartsChartsOpenofficexmlPutId**](ChartsApi.md#chartsChartsOpenofficexmlPutId) | **PUT** /Charts/OpenOfficeXml/{id} | Charts: Modify Underlying Xml |
| [**chartsChartsSvgGetIdUseCache**](ChartsApi.md#chartsChartsSvgGetIdUseCache) | **GET** /Charts/Svg/{id} | Charts: Get Svg file |


<a id="chartsChartsChartupdateGetId"></a>
# **chartsChartsChartupdateGetId**
> ChartChartDataDTO chartsChartsChartupdateGetId(id)

Charts: Get Chart Data

Gets a ChartDataDTO object, usually used for downstream analytics and chart updates

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    ChartsApi apiInstance = new ChartsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      ChartChartDataDTO result = apiInstance.chartsChartsChartupdateGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsApi#chartsChartsChartupdateGetId");
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

[**ChartChartDataDTO**](ChartChartDataDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |

<a id="chartsChartsChartupdatePutId"></a>
# **chartsChartsChartupdatePutId**
> chartsChartsChartupdatePutId(id, chartChartDataDTO)

Charts: Update Chart Data

Simplifies chart update by allowing users to supply data via ChartDataDTO

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    ChartsApi apiInstance = new ChartsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | The Chart Id
    ChartChartDataDTO chartChartDataDTO = new ChartChartDataDTO(); // ChartChartDataDTO | The ChartDataDto Object
    try {
      apiInstance.chartsChartsChartupdatePutId(id, chartChartDataDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsApi#chartsChartsChartupdatePutId");
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
| **id** | **UUID**| The Chart Id | |
| **chartChartDataDTO** | [**ChartChartDataDTO**](ChartChartDataDTO.md)| The ChartDataDto Object | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="chartsChartsChildobjectsGetId"></a>
# **chartsChartsChildobjectsGetId**
> List&lt;ChildObjects&gt; chartsChartsChildobjectsGetId(id)

Charts: Get Dependent Objects Tree

This endpoint is helpful for helping users and bots identify dependent objects to this Chart and retreive their corresponding metadata in order to make modifications to those objects in downstream operations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    ChartsApi apiInstance = new ChartsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      List<ChildObjects> result = apiInstance.chartsChartsChildobjectsGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsApi#chartsChartsChildobjectsGetId");
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

[**List&lt;ChildObjects&gt;**](ChildObjects.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="chartsChartsDetailsGetId"></a>
# **chartsChartsDetailsGetId**
> ChartChartsDetails chartsChartsDetailsGetId(id)

Charts: Get Details

Returns object metadata and information about relative dependent objects 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    ChartsApi apiInstance = new ChartsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      ChartChartsDetails result = apiInstance.chartsChartsDetailsGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsApi#chartsChartsDetailsGetId");
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

[**ChartChartsDetails**](ChartChartsDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |

<a id="chartsChartsGetId"></a>
# **chartsChartsGetId**
> ChartCharts chartsChartsGetId(id)

Charts: Get by Id

Get by Id: Use this method to retrieve a Charts object by its primary key (id)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    ChartsApi apiInstance = new ChartsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | An Id of the respository DTO elemennt
    try {
      ChartCharts result = apiInstance.chartsChartsGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsApi#chartsChartsGetId");
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
| **id** | **UUID**| An Id of the respository DTO elemennt | |

### Return type

[**ChartCharts**](ChartCharts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |

<a id="chartsChartsOpenofficexmlGetIdUpdated"></a>
# **chartsChartsOpenofficexmlGetIdUpdated**
> OoxmlDTO chartsChartsOpenofficexmlGetIdUpdated(id, updated)

Charts: Get Underlying Xml

Return the subset of the xml content from within the latest edited version of the OpenXmlDocument from this Chart object.  The returned xml data conforms to the [Ecma-376 standard](http://www.ecma-international.org/publications/standards/Ecma-376.htm).  Use this endpoint a starting point for building client-side extensions that modify Presalytics widgets containing Chart objects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    ChartsApi apiInstance = new ChartsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    Boolean updated = true; // Boolean | Indicates whether API should return the orginal uploaded xml (false) or the actively updated version (true, default)
    try {
      OoxmlDTO result = apiInstance.chartsChartsOpenofficexmlGetIdUpdated(id, updated);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsApi#chartsChartsOpenofficexmlGetIdUpdated");
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
| **updated** | **Boolean**| Indicates whether API should return the orginal uploaded xml (false) or the actively updated version (true, default) | [optional] [default to true] |

### Return type

[**OoxmlDTO**](OoxmlDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="chartsChartsOpenofficexmlPutId"></a>
# **chartsChartsOpenofficexmlPutId**
> chartsChartsOpenofficexmlPutId(id, ooxmlDTO)

Charts: Modify Underlying Xml

Directly eidt the underlying xml of a Chart object within an OpenOpenXml (e.g. Excel, Powerpoint) document. This endpoint will validatate the submitted xml against the [Ecma-376 standard](http://www.ecma-international.org/publications/standards/Ecma-376.htm) prior to saving modification.  Invalid xml will rejected by this endpoint and a (hopefully) helpful error message will be returned.  Use this endpoint for client-side automation of modifications ot Chart objects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    ChartsApi apiInstance = new ChartsApi(defaultClient);
    String id = "id_example"; // String | 
    OoxmlDTO ooxmlDTO = new OoxmlDTO(); // OoxmlDTO | 
    try {
      apiInstance.chartsChartsOpenofficexmlPutId(id, ooxmlDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsApi#chartsChartsOpenofficexmlPutId");
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
| **id** | **String**|  | |
| **ooxmlDTO** | [**OoxmlDTO**](OoxmlDTO.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="chartsChartsSvgGetIdUseCache"></a>
# **chartsChartsSvgGetIdUseCache**
> File chartsChartsSvgGetIdUseCache(id, useCache)

Charts: Get Svg file

This endpoint is helpful for rending this Chart as an svg or image object that can then be rendered in a story, dashboard or website.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    ChartsApi apiInstance = new ChartsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    Boolean useCache = false; // Boolean | Indicates whether API should retrieve content from a cache if aviable (true, default), or force an update (false)
    try {
      File result = apiInstance.chartsChartsSvgGetIdUseCache(id, useCache);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsApi#chartsChartsSvgGetIdUseCache");
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
| **useCache** | **Boolean**| Indicates whether API should retrieve content from a cache if aviable (true, default), or force an update (false) | [optional] [default to false] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/svg+xml, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an svg formatted-image of this object. |  -  |
| **400** | Bad Request |  -  |

