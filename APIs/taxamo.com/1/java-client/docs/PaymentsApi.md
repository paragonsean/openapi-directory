# PaymentsApi

All URIs are relative to *https://api.taxamo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**capturePayment**](PaymentsApi.md#capturePayment) | **POST** /api/v1/transactions/{key}/payments/capture | Capture payment |
| [**createPayment**](PaymentsApi.md#createPayment) | **POST** /api/v1/transactions/{key}/payments | Register a payment |
| [**listPayments**](PaymentsApi.md#listPayments) | **GET** /api/v1/transactions/{key}/payments | List payments |


<a id="capturePayment"></a>
# **capturePayment**
> CapturePaymentOut capturePayment(key)

Capture payment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taxamo.com");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    String key = "key_example"; // String | Transaction key.
    try {
      CapturePaymentOut result = apiInstance.capturePayment(key);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#capturePayment");
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
| **key** | **String**| Transaction key. | |

### Return type

[**CapturePaymentOut**](CapturePaymentOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Validation failed, see JSON body response for details. |  -  |
| **401** | Incorrect token |  -  |

<a id="createPayment"></a>
# **createPayment**
> CreatePaymentOut createPayment(key, input)

Register a payment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taxamo.com");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    String key = "key_example"; // String | Transaction key.
    CreatePaymentIn input = new CreatePaymentIn(); // CreatePaymentIn | Input
    try {
      CreatePaymentOut result = apiInstance.createPayment(key, input);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#createPayment");
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
| **key** | **String**| Transaction key. | |
| **input** | [**CreatePaymentIn**](CreatePaymentIn.md)| Input | |

### Return type

[**CreatePaymentOut**](CreatePaymentOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Validation failed, see JSON body response for details. |  -  |
| **401** | Incorrect token |  -  |

<a id="listPayments"></a>
# **listPayments**
> ListPaymentsOut listPayments(key, limit, offset)

List payments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taxamo.com");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    String key = "key_example"; // String | Transaction key.
    String limit = "limit_example"; // String | Max record count (no more than 100, defaults to 10).
    String offset = "offset_example"; // String | How many records need to be skipped, defaults to 0.
    try {
      ListPaymentsOut result = apiInstance.listPayments(key, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#listPayments");
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
| **key** | **String**| Transaction key. | |
| **limit** | **String**| Max record count (no more than 100, defaults to 10). | [optional] |
| **offset** | **String**| How many records need to be skipped, defaults to 0. | [optional] |

### Return type

[**ListPaymentsOut**](ListPaymentsOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Validation failed, see JSON body response for details. |  -  |
| **401** | Incorrect token |  -  |

