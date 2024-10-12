# DefaultApi

All URIs are relative to *https://api.faretrotter.com/v2.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**gETPlaces**](DefaultApi.md#gETPlaces) | **GET** /places | Returns possible modes of transportation between two cities. |
| [**gETRoutes**](DefaultApi.md#gETRoutes) | **GET** /routes |  |


<a id="gETPlaces"></a>
# **gETPlaces**
> PlaceResponse gETPlaces()

Returns possible modes of transportation between two cities.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.faretrotter.com/v2.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      PlaceResponse result = apiInstance.gETPlaces();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#gETPlaces");
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

[**PlaceResponse**](PlaceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Everything worked as expected. |  -  |
| **400** | Parameters did not match the endpoint requirements. Check that all required fields are present and spelt correctly. |  -  |
| **401** | Authentication Failed. |  -  |
| **402** | All parameters are correct but the request failed. |  -  |
| **403** | Request IP does not match IP address registered with key. |  -  |
| **404** | The endpoint doesn&#39;t exist. |  -  |
| **429** | Too many requests hit the API too quickly. |  -  |
| **501** | Server error |  -  |
| **502** | Server error |  -  |

<a id="gETRoutes"></a>
# **gETRoutes**
> RoutesResponse gETRoutes(originLat, originLng, destinationLat, destinationLng)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.faretrotter.com/v2.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    BigDecimal originLat = new BigDecimal(78); // BigDecimal | 
    BigDecimal originLng = new BigDecimal(78); // BigDecimal | 
    BigDecimal destinationLat = new BigDecimal(78); // BigDecimal | 
    BigDecimal destinationLng = new BigDecimal(78); // BigDecimal | 
    try {
      RoutesResponse result = apiInstance.gETRoutes(originLat, originLng, destinationLat, destinationLng);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#gETRoutes");
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
| **originLat** | **BigDecimal**|  | |
| **originLng** | **BigDecimal**|  | |
| **destinationLat** | **BigDecimal**|  | |
| **destinationLng** | **BigDecimal**|  | |

### Return type

[**RoutesResponse**](RoutesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Everything worked as expected. |  -  |
| **400** | Parameters did not match the endpoint requirements. Check that all required fields are present and spelt correctly. |  -  |
| **401** | Authentication Failed. |  -  |
| **402** | All parameters are correct but the request failed. |  -  |
| **403** | Request IP does not match IP address registered with key. |  -  |
| **404** | The endpoint doesn&#39;t exist. |  -  |
| **429** | Too many requests hit the API too quickly. |  -  |
| **501** | Server error |  -  |
| **502** | Server error |  -  |

