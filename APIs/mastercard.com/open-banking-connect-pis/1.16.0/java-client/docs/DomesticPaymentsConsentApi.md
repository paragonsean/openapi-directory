# DomesticPaymentsConsentApi

All URIs are relative to */openbanking/sandbox/connect/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**paymentsDomesticCreditTransfersConsentsPost**](DomesticPaymentsConsentApi.md#paymentsDomesticCreditTransfersConsentsPost) | **POST** /payments/domestic-credit-transfers/consents | Request consent initiation via redirect |


<a id="paymentsDomesticCreditTransfersConsentsPost"></a>
# **paymentsDomesticCreditTransfersConsentsPost**
> PostPaymentsDomesticCreditTransfersConsentsOKBody paymentsDomesticCreditTransfersConsentsPost(body)

Request consent initiation via redirect

Request Payment Initiation Consent for a domestic credit transfer on behalf of the PSU.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomesticPaymentsConsentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/openbanking/sandbox/connect/api");

    DomesticPaymentsConsentApi apiInstance = new DomesticPaymentsConsentApi(defaultClient);
    PostPaymentsDomesticCreditTransfersConsentsParamsBody body = new PostPaymentsDomesticCreditTransfersConsentsParamsBody(); // PostPaymentsDomesticCreditTransfersConsentsParamsBody | Domestic Payment consent to be wired via Faster Payment System
    try {
      PostPaymentsDomesticCreditTransfersConsentsOKBody result = apiInstance.paymentsDomesticCreditTransfersConsentsPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomesticPaymentsConsentApi#paymentsDomesticCreditTransfersConsentsPost");
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
| **body** | [**PostPaymentsDomesticCreditTransfersConsentsParamsBody**](PostPaymentsDomesticCreditTransfersConsentsParamsBody.md)| Domestic Payment consent to be wired via Faster Payment System | |

### Return type

[**PostPaymentsDomesticCreditTransfersConsentsOKBody**](PostPaymentsDomesticCreditTransfersConsentsOKBody.md)

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

