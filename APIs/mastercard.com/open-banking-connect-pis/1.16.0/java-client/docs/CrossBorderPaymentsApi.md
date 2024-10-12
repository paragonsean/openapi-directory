# CrossBorderPaymentsApi

All URIs are relative to */openbanking/sandbox/connect/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**paymentsCrossBorderCreditTransfersPost**](CrossBorderPaymentsApi.md#paymentsCrossBorderCreditTransfersPost) | **POST** /payments/cross-border-credit-transfers | Redeem the payment |


<a id="paymentsCrossBorderCreditTransfersPost"></a>
# **paymentsCrossBorderCreditTransfersPost**
> PostPaymentsCrossBorderCreditTransfersOKBody paymentsCrossBorderCreditTransfersPost(body)

Redeem the payment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrossBorderPaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/openbanking/sandbox/connect/api");

    CrossBorderPaymentsApi apiInstance = new CrossBorderPaymentsApi(defaultClient);
    PostPaymentsCrossBorderCreditTransfersParamsBody body = new PostPaymentsCrossBorderCreditTransfersParamsBody(); // PostPaymentsCrossBorderCreditTransfersParamsBody | Request Body
    try {
      PostPaymentsCrossBorderCreditTransfersOKBody result = apiInstance.paymentsCrossBorderCreditTransfersPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrossBorderPaymentsApi#paymentsCrossBorderCreditTransfersPost");
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
| **body** | [**PostPaymentsCrossBorderCreditTransfersParamsBody**](PostPaymentsCrossBorderCreditTransfersParamsBody.md)| Request Body | |

### Return type

[**PostPaymentsCrossBorderCreditTransfersOKBody**](PostPaymentsCrossBorderCreditTransfersOKBody.md)

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

