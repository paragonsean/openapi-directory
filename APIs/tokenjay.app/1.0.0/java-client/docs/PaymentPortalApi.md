# PaymentPortalApi

All URIs are relative to *https://api.tokenjay.app*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addPaymentRequest**](PaymentPortalApi.md#addPaymentRequest) | **POST** /payment/addrequest | Creates a new payment request. Will return request id to check for transaction state and ergopay url to show the user as QR code |
| [**getPaymentState**](PaymentPortalApi.md#getPaymentState) | **GET** /payment/state/{requestId} | Returns the state of a payment request. Please note that payment requests are purged after some time, so persist the state at your side when needed |


<a id="addPaymentRequest"></a>
# **addPaymentRequest**
> AddRequestResponse addPaymentRequest(createPaymentRequest)

Creates a new payment request. Will return request id to check for transaction state and ergopay url to show the user as QR code

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentPortalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tokenjay.app");

    PaymentPortalApi apiInstance = new PaymentPortalApi(defaultClient);
    CreatePaymentRequest createPaymentRequest = new CreatePaymentRequest(); // CreatePaymentRequest | 
    try {
      AddRequestResponse result = apiInstance.addPaymentRequest(createPaymentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentPortalApi#addPaymentRequest");
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
| **createPaymentRequest** | [**CreatePaymentRequest**](CreatePaymentRequest.md)|  | |

### Return type

[**AddRequestResponse**](AddRequestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |

<a id="getPaymentState"></a>
# **getPaymentState**
> PaymentRequestStateResponse getPaymentState(requestId)

Returns the state of a payment request. Please note that payment requests are purged after some time, so persist the state at your side when needed

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentPortalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tokenjay.app");

    PaymentPortalApi apiInstance = new PaymentPortalApi(defaultClient);
    String requestId = "requestId_example"; // String | 
    try {
      PaymentRequestStateResponse result = apiInstance.getPaymentState(requestId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentPortalApi#getPaymentState");
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
| **requestId** | **String**|  | |

### Return type

[**PaymentRequestStateResponse**](PaymentRequestStateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |

