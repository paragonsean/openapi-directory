# SearchApi

All URIs are relative to *https://test.api.amadeus.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listActivities**](SearchApi.md#listActivities) | **GET** /shopping/activities | Returns Activities around a given location |
| [**listActivitiesBySquare**](SearchApi.md#listActivitiesBySquare) | **GET** /shopping/activities/by-square | Returns Activities around a given location |


<a id="listActivities"></a>
# **listActivities**
> SuccessfulSearch listActivities(latitude, longitude, radius)

Returns Activities around a given location

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://test.api.amadeus.com/v1");

    SearchApi apiInstance = new SearchApi(defaultClient);
    BigDecimal latitude = new BigDecimal("41.397158"); // BigDecimal | Latitude (decimal coordinates)
    BigDecimal longitude = new BigDecimal("2.160873"); // BigDecimal | Longitude (decimal coordinates)
    Integer radius = 1; // Integer | radius of the search in Kilometer. Can be from 0 to 20, default value is 1 Km.
    try {
      SuccessfulSearch result = apiInstance.listActivities(latitude, longitude, radius);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#listActivities");
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
| **latitude** | **BigDecimal**| Latitude (decimal coordinates) | |
| **longitude** | **BigDecimal**| Longitude (decimal coordinates) | |
| **radius** | **Integer**| radius of the search in Kilometer. Can be from 0 to 20, default value is 1 Km. | [optional] [default to 1] |

### Return type

[**SuccessfulSearch**](SuccessfulSearch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.amadeus+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |
| **400** | Code   | Title -------|---------------- 477    | INVALID FORMAT 572    | INVALID OPTION 4926   | INVALID DATA RECEIVED 32171  | MANDATORY DATA MISSING        |  -  |
| **0** | Unexpected Error |  -  |

<a id="listActivitiesBySquare"></a>
# **listActivitiesBySquare**
> SuccessfulSearch listActivitiesBySquare(north, west, south, east)

Returns Activities around a given location

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://test.api.amadeus.com/v1");

    SearchApi apiInstance = new SearchApi(defaultClient);
    BigDecimal north = new BigDecimal("41.397158"); // BigDecimal | Latitude north of bounding box (decimal coordinates)
    BigDecimal west = new BigDecimal("2.160873"); // BigDecimal | Longitude west of bounding box (decimal coordinates)
    BigDecimal south = new BigDecimal("41.394582"); // BigDecimal | Latitude south of bounding box (decimal coordinates)
    BigDecimal east = new BigDecimal("2.177181"); // BigDecimal | Longitude east of bounding box (decimal coordinates)
    try {
      SuccessfulSearch result = apiInstance.listActivitiesBySquare(north, west, south, east);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#listActivitiesBySquare");
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
| **north** | **BigDecimal**| Latitude north of bounding box (decimal coordinates) | |
| **west** | **BigDecimal**| Longitude west of bounding box (decimal coordinates) | |
| **south** | **BigDecimal**| Latitude south of bounding box (decimal coordinates) | |
| **east** | **BigDecimal**| Longitude east of bounding box (decimal coordinates) | |

### Return type

[**SuccessfulSearch**](SuccessfulSearch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.amadeus+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |
| **400** | Code   | Title -------|---------------- 477    | INVALID FORMAT 572    | INVALID OPTION 4926   | INVALID DATA RECEIVED 32171  | MANDATORY DATA MISSING        |  -  |
| **0** | Unexpected Error |  -  |

