# SepaPaymentsStatusApi

All URIs are relative to */openbanking/sandbox/connect/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**paymentsSepaCreditTransfersPaymentStatusPost**](SepaPaymentsStatusApi.md#paymentsSepaCreditTransfersPaymentStatusPost) | **POST** /payments/sepa-credit-transfers/payment-status | Get payment status |


<a id="paymentsSepaCreditTransfersPaymentStatusPost"></a>
# **paymentsSepaCreditTransfersPaymentStatusPost**
> PostPaymentsSepaCreditTransfersPaymentStatusOKBody paymentsSepaCreditTransfersPaymentStatusPost(body)

Get payment status

Get the status of an existing SEPA credit transfer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SepaPaymentsStatusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/openbanking/sandbox/connect/api");

    SepaPaymentsStatusApi apiInstance = new SepaPaymentsStatusApi(defaultClient);
    PostPaymentsSepaCreditTransfersPaymentStatusParamsBody body = new PostPaymentsSepaCreditTransfersPaymentStatusParamsBody(); // PostPaymentsSepaCreditTransfersPaymentStatusParamsBody | Request Body
    try {
      PostPaymentsSepaCreditTransfersPaymentStatusOKBody result = apiInstance.paymentsSepaCreditTransfersPaymentStatusPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SepaPaymentsStatusApi#paymentsSepaCreditTransfersPaymentStatusPost");
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
| **body** | [**PostPaymentsSepaCreditTransfersPaymentStatusParamsBody**](PostPaymentsSepaCreditTransfersPaymentStatusParamsBody.md)| Request Body | |

### Return type

[**PostPaymentsSepaCreditTransfersPaymentStatusOKBody**](PostPaymentsSepaCreditTransfersPaymentStatusOKBody.md)

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

