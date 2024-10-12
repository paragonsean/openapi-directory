# CategoryRatedAreasApi

All URIs are relative to *https://test.api.amadeus.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCategoryRatedAreas**](CategoryRatedAreasApi.md#getCategoryRatedAreas) | **GET** /location/analytics/category-rated-areas | GET category rated areas |


<a id="getCategoryRatedAreas"></a>
# **getCategoryRatedAreas**
> GetCategoryRatedAreas200Response getCategoryRatedAreas(latitude, longitude)

GET category rated areas



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoryRatedAreasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://test.api.amadeus.com/v1");

    CategoryRatedAreasApi apiInstance = new CategoryRatedAreasApi(defaultClient);
    BigDecimal latitude = new BigDecimal("41.397158"); // BigDecimal | Latitude in decimal coordinates
    BigDecimal longitude = new BigDecimal("2.160873"); // BigDecimal | Longitude in decimal coordinates
    try {
      GetCategoryRatedAreas200Response result = apiInstance.getCategoryRatedAreas(latitude, longitude);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryRatedAreasApi#getCategoryRatedAreas");
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
| **latitude** | **BigDecimal**| Latitude in decimal coordinates | |
| **longitude** | **BigDecimal**| Longitude in decimal coordinates | |

### Return type

[**GetCategoryRatedAreas200Response**](GetCategoryRatedAreas200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.amadeus+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Reply |  -  |
| **400** | code    | title                                  ------- | -------------------------------------  477     | INVALID FORMAT 572     | INVALID OPTION                             32171   | MANDATORY DATA MISSING  |  -  |
| **500** | Internal Server Error |  -  |

