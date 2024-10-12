# SearchApi

All URIs are relative to *https://test.api.amadeus.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSafetyRankBySquare**](SearchApi.md#getSafetyRankBySquare) | **GET** /safety/safety-rated-locations/by-square | Returns the safety rating of a given area |
| [**getSafetyRanking**](SearchApi.md#getSafetyRanking) | **GET** /safety/safety-rated-locations | Returns safety rating for a given location and radius. |


<a id="getSafetyRankBySquare"></a>
# **getSafetyRankBySquare**
> Success getSafetyRankBySquare(north, west, south, east, pageLimit, pageOffset)

Returns the safety rating of a given area

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
    Double north = 41.397158D; // Double | Latitude north of bounding box (decimal coordinates)
    Double west = 2.160873D; // Double | Longitude west of bounding box (decimal coordinates)
    Double south = 41.394582D; // Double | Latitude south of bounding box (decimal coordinates)
    Double east = 2.177181D; // Double | Longitude east of bounding box (decimal coordinates)
    Integer pageLimit = 10; // Integer | maximum items in one page
    Integer pageOffset = 0; // Integer | start index of the requested page
    try {
      Success result = apiInstance.getSafetyRankBySquare(north, west, south, east, pageLimit, pageOffset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#getSafetyRankBySquare");
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
| **north** | **Double**| Latitude north of bounding box (decimal coordinates) | |
| **west** | **Double**| Longitude west of bounding box (decimal coordinates) | |
| **south** | **Double**| Latitude south of bounding box (decimal coordinates) | |
| **east** | **Double**| Longitude east of bounding box (decimal coordinates) | |
| **pageLimit** | **Integer**| maximum items in one page | [optional] [default to 10] |
| **pageOffset** | **Integer**| start index of the requested page | [optional] [default to 0] |

### Return type

[**Success**](Success.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.amadeus+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |
| **400** | code    | title                                  ------- | -------------------------------------  477     | INVALID FORMAT 572     | INVALID OPTION 4926    | INVALID DATA RECEIVED                32171   | MANDATORY DATA MISSING         |  -  |
| **0** | Unexpected Error |  -  |

<a id="getSafetyRanking"></a>
# **getSafetyRanking**
> Success getSafetyRanking(latitude, longitude, radius, pageLimit, pageOffset)

Returns safety rating for a given location and radius.

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
    Double latitude = 41.397158D; // Double | Latitude (decimal coordinates)
    Double longitude = 2.160873D; // Double | Longitude (decimal coordinates)
    Integer radius = 1; // Integer | radius of the search in Kilometer. Can be from 0 to 20, default value is 1 Km.
    Integer pageLimit = 10; // Integer | maximum items in one page
    Integer pageOffset = 0; // Integer | start index of the requested page
    try {
      Success result = apiInstance.getSafetyRanking(latitude, longitude, radius, pageLimit, pageOffset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#getSafetyRanking");
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
| **latitude** | **Double**| Latitude (decimal coordinates) | |
| **longitude** | **Double**| Longitude (decimal coordinates) | |
| **radius** | **Integer**| radius of the search in Kilometer. Can be from 0 to 20, default value is 1 Km. | [optional] [default to 1] |
| **pageLimit** | **Integer**| maximum items in one page | [optional] [default to 10] |
| **pageOffset** | **Integer**| start index of the requested page | [optional] [default to 0] |

### Return type

[**Success**](Success.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.amadeus+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |
| **400** | code    | title                                  ------- | -------------------------------------  477     | INVALID FORMAT 572     | INVALID OPTION 4926    | INVALID DATA RECEIVED                32171   | MANDATORY DATA MISSING         |  -  |
| **0** | Unexpected Error |  -  |

