# CrossBorderPaymentsStatusApi

All URIs are relative to */openbanking/sandbox/connect/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**paymentsCrossBorderCreditTransfersPaymentStatusPost**](CrossBorderPaymentsStatusApi.md#paymentsCrossBorderCreditTransfersPaymentStatusPost) | **POST** /payments/cross-border-credit-transfers/payment-status | Get payment status |


<a id="paymentsCrossBorderCreditTransfersPaymentStatusPost"></a>
# **paymentsCrossBorderCreditTransfersPaymentStatusPost**
> PostPaymentsCrossBorderCreditTransfersPaymentStatusOKBody paymentsCrossBorderCreditTransfersPaymentStatusPost(body)

Get payment status

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrossBorderPaymentsStatusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/openbanking/sandbox/connect/api");

    CrossBorderPaymentsStatusApi apiInstance = new CrossBorderPaymentsStatusApi(defaultClient);
    PostPaymentsCrossBorderCreditTransfersPaymentStatusParamsBody body = new PostPaymentsCrossBorderCreditTransfersPaymentStatusParamsBody(); // PostPaymentsCrossBorderCreditTransfersPaymentStatusParamsBody | Request Body
    try {
      PostPaymentsCrossBorderCreditTransfersPaymentStatusOKBody result = apiInstance.paymentsCrossBorderCreditTransfersPaymentStatusPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrossBorderPaymentsStatusApi#paymentsCrossBorderCreditTransfersPaymentStatusPost");
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
| **body** | [**PostPaymentsCrossBorderCreditTransfersPaymentStatusParamsBody**](PostPaymentsCrossBorderCreditTransfersPaymentStatusParamsBody.md)| Request Body | |

### Return type

[**PostPaymentsCrossBorderCreditTransfersPaymentStatusOKBody**](PostPaymentsCrossBorderCreditTransfersPaymentStatusOKBody.md)

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

