# HotelRatingsApi

All URIs are relative to *https://test.api.amadeus.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSentimentsByHotelIds**](HotelRatingsApi.md#getSentimentsByHotelIds) | **GET** /e-reputation/hotel-sentiments | Get sentiments by Amadeus Hotel Ids |


<a id="getSentimentsByHotelIds"></a>
# **getSentimentsByHotelIds**
> SuccessSentiments getSentimentsByHotelIds(hotelIds)

Get sentiments by Amadeus Hotel Ids

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HotelRatingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://test.api.amadeus.com/v2");

    HotelRatingsApi apiInstance = new HotelRatingsApi(defaultClient);
    List<String> hotelIds = Arrays.asList(); // List<String> | Comma-separated list of Amadeus Hotel Ids (max. 3) . Amadeus Hotel Ids are found in the Hotel Search response (parameter name is 'hotelId').
    try {
      SuccessSentiments result = apiInstance.getSentimentsByHotelIds(hotelIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HotelRatingsApi#getSentimentsByHotelIds");
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
| **hotelIds** | [**List&lt;String&gt;**](String.md)| Comma-separated list of Amadeus Hotel Ids (max. 3) . Amadeus Hotel Ids are found in the Hotel Search response (parameter name is &#39;hotelId&#39;). | |

### Return type

[**SuccessSentiments**](SuccessSentiments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.amadeus+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Not Found |  -  |
| **401** | Unauthorized |  -  |
| **0** | Unexpected Error |  -  |

