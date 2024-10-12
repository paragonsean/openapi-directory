# ChartsRowColApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**chartRowcolGet**](ChartsRowColApi.md#chartRowcolGet) | **GET** /Charts/RowCol | RowCol: List All Possible Types |
| [**chartRowcolGetId**](ChartsRowColApi.md#chartRowcolGetId) | **GET** /Charts/RowCol/{id} | RowCol: Get by Id |
| [**chartRowcolTypeidGetTypeId**](ChartsRowColApi.md#chartRowcolTypeidGetTypeId) | **GET** /Charts/RowCol/TypeId/{type_id} | RowCol: Get By Type Id |


<a id="chartRowcolGet"></a>
# **chartRowcolGet**
> List&lt;ChartRowCol&gt; chartRowcolGet()

RowCol: List All Possible Types

List Types: Use this method to retreive a list of possible options for the RowCol type. Use the Id from oneof the returned elements on to make changes to elements in the Chart object space.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsRowColApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    ChartsRowColApi apiInstance = new ChartsRowColApi(defaultClient);
    try {
      List<ChartRowCol> result = apiInstance.chartRowcolGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsRowColApi#chartRowcolGet");
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

[**List&lt;ChartRowCol&gt;**](ChartRowCol.md)

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

<a id="chartRowcolGetId"></a>
# **chartRowcolGetId**
> ChartRowCol chartRowcolGetId(id)

RowCol: Get by Id

Get by Id: Use this method to retrieve a RowCol object by its primary key (id)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsRowColApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    ChartsRowColApi apiInstance = new ChartsRowColApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      ChartRowCol result = apiInstance.chartRowcolGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsRowColApi#chartRowcolGetId");
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

[**ChartRowCol**](ChartRowCol.md)

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

<a id="chartRowcolTypeidGetTypeId"></a>
# **chartRowcolTypeidGetTypeId**
> ChartRowCol chartRowcolTypeidGetTypeId(typeId)

RowCol: Get By Type Id

This endpoint returns Type metadata from an integer type_id that can found on objects throughout the api.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsRowColApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    ChartsRowColApi apiInstance = new ChartsRowColApi(defaultClient);
    Integer typeId = 56; // Integer | 
    try {
      ChartRowCol result = apiInstance.chartRowcolTypeidGetTypeId(typeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsRowColApi#chartRowcolTypeidGetTypeId");
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

[**ChartRowCol**](ChartRowCol.md)

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

