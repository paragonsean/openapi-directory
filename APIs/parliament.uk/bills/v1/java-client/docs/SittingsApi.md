# SittingsApi

All URIs are relative to *https://bills-api.parliament.uk*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSittings**](SittingsApi.md#getSittings) | **GET** /api/v1/Sittings | Returns a list of Sittings. |


<a id="getSittings"></a>
# **getSittings**
> BillStageSittingSearchResult getSittings(house, dateFrom, dateTo, skip, take)

Returns a list of Sittings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SittingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://bills-api.parliament.uk");

    SittingsApi apiInstance = new SittingsApi(defaultClient);
    House house = House.fromValue("All"); // House | 
    OffsetDateTime dateFrom = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime dateTo = OffsetDateTime.now(); // OffsetDateTime | 
    Integer skip = 56; // Integer | 
    Integer take = 56; // Integer | 
    try {
      BillStageSittingSearchResult result = apiInstance.getSittings(house, dateFrom, dateTo, skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SittingsApi#getSittings");
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
| **house** | [**House**](.md)|  | [optional] [enum: All, Commons, Lords, Unassigned] |
| **dateFrom** | **OffsetDateTime**|  | [optional] |
| **dateTo** | **OffsetDateTime**|  | [optional] |
| **skip** | **Integer**|  | [optional] |
| **take** | **Integer**|  | [optional] |

### Return type

[**BillStageSittingSearchResult**](BillStageSittingSearchResult.md)

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

