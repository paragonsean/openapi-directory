# DomesticPaymentsApi

All URIs are relative to */openbanking/sandbox/connect/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**paymentsDomesticCreditTransfersPost**](DomesticPaymentsApi.md#paymentsDomesticCreditTransfersPost) | **POST** /payments/domestic-credit-transfers | Redeem the payment |


<a id="paymentsDomesticCreditTransfersPost"></a>
# **paymentsDomesticCreditTransfersPost**
> PostPaymentsDomesticCreditTransfersOKBody paymentsDomesticCreditTransfersPost(body)

Redeem the payment

Redeem the payment which was previously consented by the PSU.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomesticPaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/openbanking/sandbox/connect/api");

    DomesticPaymentsApi apiInstance = new DomesticPaymentsApi(defaultClient);
    PostPaymentsDomesticCreditTransfersParamsBody body = new PostPaymentsDomesticCreditTransfersParamsBody(); // PostPaymentsDomesticCreditTransfersParamsBody | Request Body
    try {
      PostPaymentsDomesticCreditTransfersOKBody result = apiInstance.paymentsDomesticCreditTransfersPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomesticPaymentsApi#paymentsDomesticCreditTransfersPost");
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
| **body** | [**PostPaymentsDomesticCreditTransfersParamsBody**](PostPaymentsDomesticCreditTransfersParamsBody.md)| Request Body | |

### Return type

[**PostPaymentsDomesticCreditTransfersOKBody**](PostPaymentsDomesticCreditTransfersOKBody.md)

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
| **504** | Server while acting as a gateway or proxy, cannot get a response in time. |  -  |

