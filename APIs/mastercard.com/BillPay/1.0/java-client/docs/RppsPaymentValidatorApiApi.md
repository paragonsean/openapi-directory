# RppsPaymentValidatorApiApi

All URIs are relative to *https://api.mastercard.com/billpayAPI/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**isRoutingValidPost**](RppsPaymentValidatorApiApi.md#isRoutingValidPost) | **POST** /isRoutingValid | Bill Payment Validator service returns the processing status for a potential RPPS transaction |


<a id="isRoutingValidPost"></a>
# **isRoutingValidPost**
> BillPayResponse isRoutingValidPost(billPayRequest)

Bill Payment Validator service returns the processing status for a potential RPPS transaction

Bill Payment Validator performs real time transaction validation against the specified Biller ID&#39;s account masks, account check digits and all other registered RPPS processing parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RppsPaymentValidatorApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com/billpayAPI/v1");

    RppsPaymentValidatorApiApi apiInstance = new RppsPaymentValidatorApiApi(defaultClient);
    BillPayRequest billPayRequest = new BillPayRequest(); // BillPayRequest | Contains the details of the get PAR API request message.
    try {
      BillPayResponse result = apiInstance.isRoutingValidPost(billPayRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RppsPaymentValidatorApiApi#isRoutingValidPost");
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
| **billPayRequest** | [**BillPayRequest**](BillPayRequest.md)| Contains the details of the get PAR API request message. | [optional] |

### Return type

[**BillPayResponse**](BillPayResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/JSON
 - **Accept**: application/JSON

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Bill Payment Validator response. |  -  |
| **0** | unexpected error |  -  |

