# DomesticPaymentsStatusApi

All URIs are relative to */openbanking/sandbox/connect/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**paymentsDomesticCreditTransfersPaymentStatusPost**](DomesticPaymentsStatusApi.md#paymentsDomesticCreditTransfersPaymentStatusPost) | **POST** /payments/domestic-credit-transfers/payment-status | Get payment status |


<a id="paymentsDomesticCreditTransfersPaymentStatusPost"></a>
# **paymentsDomesticCreditTransfersPaymentStatusPost**
> PostPaymentsDomesticCreditTransfersPaymentStatusOKBody paymentsDomesticCreditTransfersPaymentStatusPost(body)

Get payment status

Get the status for an existing domestic credit transfer payment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomesticPaymentsStatusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/openbanking/sandbox/connect/api");

    DomesticPaymentsStatusApi apiInstance = new DomesticPaymentsStatusApi(defaultClient);
    PostPaymentsDomesticCreditTransfersPaymentStatusParamsBody body = new PostPaymentsDomesticCreditTransfersPaymentStatusParamsBody(); // PostPaymentsDomesticCreditTransfersPaymentStatusParamsBody | Request Body
    try {
      PostPaymentsDomesticCreditTransfersPaymentStatusOKBody result = apiInstance.paymentsDomesticCreditTransfersPaymentStatusPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomesticPaymentsStatusApi#paymentsDomesticCreditTransfersPaymentStatusPost");
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
| **body** | [**PostPaymentsDomesticCreditTransfersPaymentStatusParamsBody**](PostPaymentsDomesticCreditTransfersPaymentStatusParamsBody.md)| Request Body | |

### Return type

[**PostPaymentsDomesticCreditTransfersPaymentStatusOKBody**](PostPaymentsDomesticCreditTransfersPaymentStatusOKBody.md)

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

