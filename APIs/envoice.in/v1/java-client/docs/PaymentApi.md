# PaymentApi

All URIs are relative to *https://www.envoice.in*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**paymentApiSupported**](PaymentApi.md#paymentApiSupported) | **GET** /api/payment/supported | Return all supported payment gateways (no currencies means all are supported) |


<a id="paymentApiSupported"></a>
# **paymentApiSupported**
> List&lt;PaymentGatewayDetailsApiModel&gt; paymentApiSupported(xAuthKey, xAuthSecret)

Return all supported payment gateways (no currencies means all are supported)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    PaymentApi apiInstance = new PaymentApi(defaultClient);
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    try {
      List<PaymentGatewayDetailsApiModel> result = apiInstance.paymentApiSupported(xAuthKey, xAuthSecret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentApi#paymentApiSupported");
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
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |

### Return type

[**List&lt;PaymentGatewayDetailsApiModel&gt;**](PaymentGatewayDetailsApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

