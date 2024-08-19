# OccupancyApi

All URIs are relative to *https://api.digital.tfl.gov.uk*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**occupancyCarParkGet**](OccupancyApi.md#occupancyCarParkGet) | **GET** /Occupancy/CarPark | Gets the occupancy for all car parks that have occupancy data |
| [**occupancyGet**](OccupancyApi.md#occupancyGet) | **GET** /Occupancy/CarPark/{id} | Gets the occupancy for a car park with a given id |
| [**occupancyGetAllChargeConnectorStatus**](OccupancyApi.md#occupancyGetAllChargeConnectorStatus) | **GET** /Occupancy/ChargeConnector | Gets the occupancy for all charge connectors |
| [**occupancyGetBikePointsOccupancies**](OccupancyApi.md#occupancyGetBikePointsOccupancies) | **GET** /Occupancy/BikePoints/{ids} | Get the occupancy for bike points. |
| [**occupancyGetChargeConnectorStatus**](OccupancyApi.md#occupancyGetChargeConnectorStatus) | **GET** /Occupancy/ChargeConnector/{ids} | Gets the occupancy for a charge connectors with a given id (sourceSystemPlaceId) |


<a id="occupancyCarParkGet"></a>
# **occupancyCarParkGet**
> List&lt;TflApiPresentationEntitiesCarParkOccupancy&gt; occupancyCarParkGet()

Gets the occupancy for all car parks that have occupancy data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OccupancyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    OccupancyApi apiInstance = new OccupancyApi(defaultClient);
    try {
      List<TflApiPresentationEntitiesCarParkOccupancy> result = apiInstance.occupancyCarParkGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OccupancyApi#occupancyCarParkGet");
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

[**List&lt;TflApiPresentationEntitiesCarParkOccupancy&gt;**](TflApiPresentationEntitiesCarParkOccupancy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="occupancyGet"></a>
# **occupancyGet**
> TflApiPresentationEntitiesCarParkOccupancy occupancyGet(id)

Gets the occupancy for a car park with a given id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OccupancyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    OccupancyApi apiInstance = new OccupancyApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      TflApiPresentationEntitiesCarParkOccupancy result = apiInstance.occupancyGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OccupancyApi#occupancyGet");
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

### Return type

[**TflApiPresentationEntitiesCarParkOccupancy**](TflApiPresentationEntitiesCarParkOccupancy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="occupancyGetAllChargeConnectorStatus"></a>
# **occupancyGetAllChargeConnectorStatus**
> List&lt;TflApiPresentationEntitiesChargeConnectorOccupancy&gt; occupancyGetAllChargeConnectorStatus()

Gets the occupancy for all charge connectors

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OccupancyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    OccupancyApi apiInstance = new OccupancyApi(defaultClient);
    try {
      List<TflApiPresentationEntitiesChargeConnectorOccupancy> result = apiInstance.occupancyGetAllChargeConnectorStatus();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OccupancyApi#occupancyGetAllChargeConnectorStatus");
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

[**List&lt;TflApiPresentationEntitiesChargeConnectorOccupancy&gt;**](TflApiPresentationEntitiesChargeConnectorOccupancy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="occupancyGetBikePointsOccupancies"></a>
# **occupancyGetBikePointsOccupancies**
> List&lt;TflApiPresentationEntitiesBikePointOccupancy&gt; occupancyGetBikePointsOccupancies(ids)

Get the occupancy for bike points.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OccupancyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    OccupancyApi apiInstance = new OccupancyApi(defaultClient);
    List<String> ids = Arrays.asList(); // List<String> | 
    try {
      List<TflApiPresentationEntitiesBikePointOccupancy> result = apiInstance.occupancyGetBikePointsOccupancies(ids);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OccupancyApi#occupancyGetBikePointsOccupancies");
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
| **ids** | [**List&lt;String&gt;**](String.md)|  | |

### Return type

[**List&lt;TflApiPresentationEntitiesBikePointOccupancy&gt;**](TflApiPresentationEntitiesBikePointOccupancy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="occupancyGetChargeConnectorStatus"></a>
# **occupancyGetChargeConnectorStatus**
> List&lt;TflApiPresentationEntitiesChargeConnectorOccupancy&gt; occupancyGetChargeConnectorStatus(ids)

Gets the occupancy for a charge connectors with a given id (sourceSystemPlaceId)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OccupancyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    OccupancyApi apiInstance = new OccupancyApi(defaultClient);
    List<String> ids = Arrays.asList(); // List<String> | 
    try {
      List<TflApiPresentationEntitiesChargeConnectorOccupancy> result = apiInstance.occupancyGetChargeConnectorStatus(ids);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OccupancyApi#occupancyGetChargeConnectorStatus");
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
| **ids** | [**List&lt;String&gt;**](String.md)|  | |

### Return type

[**List&lt;TflApiPresentationEntitiesChargeConnectorOccupancy&gt;**](TflApiPresentationEntitiesChargeConnectorOccupancy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

