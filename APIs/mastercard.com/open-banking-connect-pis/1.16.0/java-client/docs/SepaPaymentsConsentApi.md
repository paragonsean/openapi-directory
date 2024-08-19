# SepaPaymentsConsentApi

All URIs are relative to */openbanking/sandbox/connect/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**paymentsSepaCreditTransfersConsentsPost**](SepaPaymentsConsentApi.md#paymentsSepaCreditTransfersConsentsPost) | **POST** /payments/sepa-credit-transfers/consents | Request consent initiation via redirect |


<a id="paymentsSepaCreditTransfersConsentsPost"></a>
# **paymentsSepaCreditTransfersConsentsPost**
> PostPaymentsSepaCreditTransfersConsentsOKBody paymentsSepaCreditTransfersConsentsPost(body)

Request consent initiation via redirect

Request a SEPA credit transfer consent on behalf of the PSU via a URL redirect to the ASPSP.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SepaPaymentsConsentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/openbanking/sandbox/connect/api");

    SepaPaymentsConsentApi apiInstance = new SepaPaymentsConsentApi(defaultClient);
    PostPaymentsSepaCreditTransfersConsentsParamsBody body = new PostPaymentsSepaCreditTransfersConsentsParamsBody(); // PostPaymentsSepaCreditTransfersConsentsParamsBody | 
    try {
      PostPaymentsSepaCreditTransfersConsentsOKBody result = apiInstance.paymentsSepaCreditTransfersConsentsPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SepaPaymentsConsentApi#paymentsSepaCreditTransfersConsentsPost");
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
| **body** | [**PostPaymentsSepaCreditTransfersConsentsParamsBody**](PostPaymentsSepaCreditTransfersConsentsParamsBody.md)|  | |

### Return type

[**PostPaymentsSepaCreditTransfersConsentsOKBody**](PostPaymentsSepaCreditTransfersConsentsOKBody.md)

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

