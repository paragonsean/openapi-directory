# GeoCalculateApi

All URIs are relative to *https://wyjyt-geo-calculate.azurewebsites.net/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**convert**](GeoCalculateApi.md#convert) | **POST** /Convert | Convert the list of geo coordinates to a standard format - (latlon | utm | mgrs | ecef | epsg3857 | georef | cartesian) |
| [**distance**](GeoCalculateApi.md#distance) | **POST** /Distance | Calculate the distance between two geo coordinates. |
| [**fence**](GeoCalculateApi.md#fence) | **POST** /Fence | Check if a list of coordinates are inside of a fence of coordinates. |
| [**sky**](GeoCalculateApi.md#sky) | **POST** /Sky | Calculate sun, moon, eclipse and sky information for the date and location. |


<a id="convert"></a>
# **convert**
> GeoConvertResponse convert(geoConvertRequest)

Convert the list of geo coordinates to a standard format - (latlon | utm | mgrs | ecef | epsg3857 | georef | cartesian)

Convert the list of geo coordinates to a standard format - (latlon | utm | mgrs | ecef | epsg3857 | georef | cartesian)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeoCalculateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wyjyt-geo-calculate.azurewebsites.net/api");

    GeoCalculateApi apiInstance = new GeoCalculateApi(defaultClient);
    GeoConvertRequest geoConvertRequest = new GeoConvertRequest(); // GeoConvertRequest | 
    try {
      GeoConvertResponse result = apiInstance.convert(geoConvertRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeoCalculateApi#convert");
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
| **geoConvertRequest** | [**GeoConvertRequest**](GeoConvertRequest.md)|  | |

### Return type

[**GeoConvertResponse**](GeoConvertResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad request |  -  |
| **500** | Error |  -  |

<a id="distance"></a>
# **distance**
> GeoDistanceResponse distance(geoDistanceRequest)

Calculate the distance between two geo coordinates.

Calculate the distance between two geo coordinates.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeoCalculateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wyjyt-geo-calculate.azurewebsites.net/api");

    GeoCalculateApi apiInstance = new GeoCalculateApi(defaultClient);
    GeoDistanceRequest geoDistanceRequest = new GeoDistanceRequest(); // GeoDistanceRequest | 
    try {
      GeoDistanceResponse result = apiInstance.distance(geoDistanceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeoCalculateApi#distance");
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
| **geoDistanceRequest** | [**GeoDistanceRequest**](GeoDistanceRequest.md)|  | |

### Return type

[**GeoDistanceResponse**](GeoDistanceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad request |  -  |
| **500** | Error |  -  |

<a id="fence"></a>
# **fence**
> GeoFenceResponse fence(geoFenceRequest)

Check if a list of coordinates are inside of a fence of coordinates.

Check if a list of coordinates are inside of a fence of coordinates.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeoCalculateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wyjyt-geo-calculate.azurewebsites.net/api");

    GeoCalculateApi apiInstance = new GeoCalculateApi(defaultClient);
    GeoFenceRequest geoFenceRequest = new GeoFenceRequest(); // GeoFenceRequest | 
    try {
      GeoFenceResponse result = apiInstance.fence(geoFenceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeoCalculateApi#fence");
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
| **geoFenceRequest** | [**GeoFenceRequest**](GeoFenceRequest.md)|  | |

### Return type

[**GeoFenceResponse**](GeoFenceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad request |  -  |
| **500** | Error |  -  |

<a id="sky"></a>
# **sky**
> GeoSkyResponse sky(geoSkyRequest)

Calculate sun, moon, eclipse and sky information for the date and location.

Calculate sun, moon, eclipse and sky information for the date and location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeoCalculateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wyjyt-geo-calculate.azurewebsites.net/api");

    GeoCalculateApi apiInstance = new GeoCalculateApi(defaultClient);
    GeoSkyRequest geoSkyRequest = new GeoSkyRequest(); // GeoSkyRequest | 
    try {
      GeoSkyResponse result = apiInstance.sky(geoSkyRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeoCalculateApi#sky");
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
| **geoSkyRequest** | [**GeoSkyRequest**](GeoSkyRequest.md)|  | |

### Return type

[**GeoSkyResponse**](GeoSkyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad request |  -  |
| **500** | Error |  -  |

