# CrossBorderPaymentsConsentApi

All URIs are relative to */openbanking/sandbox/connect/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**paymentsCrossBorderCreditTransfersConsentsPost**](CrossBorderPaymentsConsentApi.md#paymentsCrossBorderCreditTransfersConsentsPost) | **POST** /payments/cross-border-credit-transfers/consents | Request consent initiation via redirect |


<a id="paymentsCrossBorderCreditTransfersConsentsPost"></a>
# **paymentsCrossBorderCreditTransfersConsentsPost**
> PostPaymentsCrossBorderCreditTransfersConsentsOKBody paymentsCrossBorderCreditTransfersConsentsPost(body)

Request consent initiation via redirect

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrossBorderPaymentsConsentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/openbanking/sandbox/connect/api");

    CrossBorderPaymentsConsentApi apiInstance = new CrossBorderPaymentsConsentApi(defaultClient);
    PostPaymentsCrossBorderCreditTransfersConsentsParamsBody body = new PostPaymentsCrossBorderCreditTransfersConsentsParamsBody(); // PostPaymentsCrossBorderCreditTransfersConsentsParamsBody | Cross border payment consent
    try {
      PostPaymentsCrossBorderCreditTransfersConsentsOKBody result = apiInstance.paymentsCrossBorderCreditTransfersConsentsPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrossBorderPaymentsConsentApi#paymentsCrossBorderCreditTransfersConsentsPost");
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
| **body** | [**PostPaymentsCrossBorderCreditTransfersConsentsParamsBody**](PostPaymentsCrossBorderCreditTransfersConsentsParamsBody.md)| Cross border payment consent | |

### Return type

[**PostPaymentsCrossBorderCreditTransfersConsentsOKBody**](PostPaymentsCrossBorderCreditTransfersConsentsOKBody.md)

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

