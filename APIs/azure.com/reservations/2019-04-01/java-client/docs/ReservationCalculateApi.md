# ReservationCalculateApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**reservationOrderCalculate**](ReservationCalculateApi.md#reservationOrderCalculate) | **POST** /providers/Microsoft.Capacity/calculatePrice | Calculate price for a &#x60;ReservationOrder&#x60;. |


<a id="reservationOrderCalculate"></a>
# **reservationOrderCalculate**
> CalculatePriceResponse reservationOrderCalculate(apiVersion, body)

Calculate price for a &#x60;ReservationOrder&#x60;.

Calculate price for placing a &#x60;ReservationOrder&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReservationCalculateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ReservationCalculateApi apiInstance = new ReservationCalculateApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Supported version for this document is 2019-04-01
    PurchaseRequest body = new PurchaseRequest(); // PurchaseRequest | Information needed for calculate or purchase reservation
    try {
      CalculatePriceResponse result = apiInstance.reservationOrderCalculate(apiVersion, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReservationCalculateApi#reservationOrderCalculate");
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
| **apiVersion** | **String**| Supported version for this document is 2019-04-01 | |
| **body** | [**PurchaseRequest**](PurchaseRequest.md)| Information needed for calculate or purchase reservation | |

### Return type

[**CalculatePriceResponse**](CalculatePriceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Detailed price info for purchasing &#x60;ReservationOrder&#x60; |  -  |
| **0** | Unexpected error |  -  |

