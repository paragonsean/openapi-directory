# PaymentMethodsApi

All URIs are relative to *https://api.reverb.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**paymentMethodsGet**](PaymentMethodsApi.md#paymentMethodsGet) | **GET** /payment_methods | Get list of payment methods |


<a id="paymentMethodsGet"></a>
# **paymentMethodsGet**
> paymentMethodsGet()

Get list of payment methods

Get list of payment methods

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentMethodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    PaymentMethodsApi apiInstance = new PaymentMethodsApi(defaultClient);
    try {
      apiInstance.paymentMethodsGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentMethodsApi#paymentMethodsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

