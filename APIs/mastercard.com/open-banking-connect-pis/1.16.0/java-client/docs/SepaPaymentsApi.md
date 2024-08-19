# SepaPaymentsApi

All URIs are relative to */openbanking/sandbox/connect/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**paymentsSepaCreditTransfersPost**](SepaPaymentsApi.md#paymentsSepaCreditTransfersPost) | **POST** /payments/sepa-credit-transfers | Redeem the payment |


<a id="paymentsSepaCreditTransfersPost"></a>
# **paymentsSepaCreditTransfersPost**
> PostPaymentsSepaCreditTransfersOKBody paymentsSepaCreditTransfersPost(body)

Redeem the payment

Redeem a SEPA credit transfer previously consented by the PSU.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SepaPaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/openbanking/sandbox/connect/api");

    SepaPaymentsApi apiInstance = new SepaPaymentsApi(defaultClient);
    PostPaymentsSepaCreditTransfersParamsBody body = new PostPaymentsSepaCreditTransfersParamsBody(); // PostPaymentsSepaCreditTransfersParamsBody | Request Body
    try {
      PostPaymentsSepaCreditTransfersOKBody result = apiInstance.paymentsSepaCreditTransfersPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SepaPaymentsApi#paymentsSepaCreditTransfersPost");
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
| **body** | [**PostPaymentsSepaCreditTransfersParamsBody**](PostPaymentsSepaCreditTransfersParamsBody.md)| Request Body | |

### Return type

[**PostPaymentsSepaCreditTransfersOKBody**](PostPaymentsSepaCreditTransfersOKBody.md)

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

