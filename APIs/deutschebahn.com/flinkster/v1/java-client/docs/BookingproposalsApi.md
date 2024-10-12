# BookingproposalsApi

All URIs are relative to *https://api.deutschebahn.com/flinkster-api-ng/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listBookingProposals**](BookingproposalsApi.md#listBookingProposals) | **GET** /bookingproposals | Query for available RentalObjects of a specific view |


<a id="listBookingProposals"></a>
# **listBookingProposals**
> RentalObjectJO listBookingProposals(lat, lon, radius, offset, limit, providernetwork, begin, end, expand, view)

Query for available RentalObjects of a specific view

Here you can query all bookable Rental Objects with different Parameters (Time, Location,...)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingproposalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.deutschebahn.com/flinkster-api-ng/v1");

    BookingproposalsApi apiInstance = new BookingproposalsApi(defaultClient);
    Double lat = 3.4D; // Double | 
    Double lon = 3.4D; // Double | 
    Integer radius = 56; // Integer | 
    Integer offset = 56; // Integer | 
    Integer limit = 56; // Integer | 
    String providernetwork = "providernetwork_example"; // String | 
    String begin = "begin_example"; // String | 
    String end = "end_example"; // String | 
    String expand = "expand_example"; // String | 
    String view = "view_example"; // String | 
    try {
      RentalObjectJO result = apiInstance.listBookingProposals(lat, lon, radius, offset, limit, providernetwork, begin, end, expand, view);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingproposalsApi#listBookingProposals");
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
| **lat** | **Double**|  | [optional] |
| **lon** | **Double**|  | [optional] |
| **radius** | **Integer**|  | [optional] |
| **offset** | **Integer**|  | [optional] |
| **limit** | **Integer**|  | [optional] |
| **providernetwork** | **String**|  | [optional] |
| **begin** | **String**|  | [optional] |
| **end** | **String**|  | [optional] |
| **expand** | **String**|  | [optional] |
| **view** | **String**|  | [optional] |

### Return type

[**RentalObjectJO**](RentalObjectJO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request One or more parameters have invalid values. |  -  |
| **403** | Forbidden Provider is not allowed to use this interface. |  -  |

