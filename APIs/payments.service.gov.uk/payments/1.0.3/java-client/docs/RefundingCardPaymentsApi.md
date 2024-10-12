# RefundingCardPaymentsApi

All URIs are relative to *https://publicapi.payments.service.gov.uk*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAPaymentRefund**](RefundingCardPaymentsApi.md#getAPaymentRefund) | **GET** /v1/payments/{paymentId}/refunds/{refundId} | Find payment refund by ID |
| [**getAllRefundsForAPayment**](RefundingCardPaymentsApi.md#getAllRefundsForAPayment) | **GET** /v1/payments/{paymentId}/refunds | Get all refunds for a payment |
| [**searchRefunds**](RefundingCardPaymentsApi.md#searchRefunds) | **GET** /v1/refunds | Search refunds |
| [**submitARefundForAPayment**](RefundingCardPaymentsApi.md#submitARefundForAPayment) | **POST** /v1/payments/{paymentId}/refunds | Submit a refund for a payment |


<a id="getAPaymentRefund"></a>
# **getAPaymentRefund**
> Refund getAPaymentRefund(paymentId, refundId)

Find payment refund by ID

Return payment refund information by Refund ID The Authorisation token needs to be specified in the &#39;authorization&#39; header as &#39;authorization: Bearer YOUR_API_KEY_HERE&#39;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RefundingCardPaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://publicapi.payments.service.gov.uk");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    RefundingCardPaymentsApi apiInstance = new RefundingCardPaymentsApi(defaultClient);
    String paymentId = "paymentId_example"; // String | 
    String refundId = "refundId_example"; // String | 
    try {
      Refund result = apiInstance.getAPaymentRefund(paymentId, refundId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RefundingCardPaymentsApi#getAPaymentRefund");
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
| **paymentId** | **String**|  | |
| **refundId** | **String**|  | |

### Return type

[**Refund**](Refund.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Credentials are required to access this resource |  -  |
| **404** | Not found |  -  |
| **429** | Too many requests |  -  |
| **500** | Downstream system error |  -  |

<a id="getAllRefundsForAPayment"></a>
# **getAllRefundsForAPayment**
> RefundForSearchResult getAllRefundsForAPayment(paymentId)

Get all refunds for a payment

Return refunds for a payment. The Authorisation token needs to be specified in the &#39;authorization&#39; header as &#39;authorization: Bearer YOUR_API_KEY_HERE&#39;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RefundingCardPaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://publicapi.payments.service.gov.uk");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    RefundingCardPaymentsApi apiInstance = new RefundingCardPaymentsApi(defaultClient);
    String paymentId = "paymentId_example"; // String | 
    try {
      RefundForSearchResult result = apiInstance.getAllRefundsForAPayment(paymentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RefundingCardPaymentsApi#getAllRefundsForAPayment");
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
| **paymentId** | **String**|  | |

### Return type

[**RefundForSearchResult**](RefundForSearchResult.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Credentials are required to access this resource |  -  |
| **404** | Not found |  -  |
| **429** | Too many requests |  -  |
| **500** | Downstream system error |  -  |

<a id="searchRefunds"></a>
# **searchRefunds**
> RefundSearchResults searchRefunds(fromDate, toDate, fromSettledDate, toSettledDate, page, displaySize)

Search refunds

Search refunds by &#39;from&#39; and &#39;to&#39; date. The Authorisation token needs to be specified in the &#39;authorization&#39; header as &#39;authorization: Bearer YOUR_API_KEY_HERE&#39;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RefundingCardPaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://publicapi.payments.service.gov.uk");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    RefundingCardPaymentsApi apiInstance = new RefundingCardPaymentsApi(defaultClient);
    String fromDate = "fromDate_example"; // String | From date of refunds to be searched (this date is inclusive). Example=2015-08-13T12:35:00Z
    String toDate = "toDate_example"; // String | To date of refunds to be searched (this date is exclusive). Example=2015-08-14T12:35:00Z
    String fromSettledDate = "fromSettledDate_example"; // String | From settled date of refund to be searched (this date is inclusive). Example=2015-08-13
    String toSettledDate = "toSettledDate_example"; // String | To settled date of refund to be searched (this date is inclusive). Example=2015-08-13
    String page = "page_example"; // String | Page number requested for the search, should be a positive integer (optional, defaults to 1)
    String displaySize = "displaySize_example"; // String | Number of results to be shown per page, should be a positive integer (optional, defaults to 500, max 500)
    try {
      RefundSearchResults result = apiInstance.searchRefunds(fromDate, toDate, fromSettledDate, toSettledDate, page, displaySize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RefundingCardPaymentsApi#searchRefunds");
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
| **fromDate** | **String**| From date of refunds to be searched (this date is inclusive). Example&#x3D;2015-08-13T12:35:00Z | [optional] |
| **toDate** | **String**| To date of refunds to be searched (this date is exclusive). Example&#x3D;2015-08-14T12:35:00Z | [optional] |
| **fromSettledDate** | **String**| From settled date of refund to be searched (this date is inclusive). Example&#x3D;2015-08-13 | [optional] |
| **toSettledDate** | **String**| To settled date of refund to be searched (this date is inclusive). Example&#x3D;2015-08-13 | [optional] |
| **page** | **String**| Page number requested for the search, should be a positive integer (optional, defaults to 1) | [optional] |
| **displaySize** | **String**| Number of results to be shown per page, should be a positive integer (optional, defaults to 500, max 500) | [optional] |

### Return type

[**RefundSearchResults**](RefundSearchResults.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Credentials are required to access this resource |  -  |
| **422** | Invalid parameters. See Public API documentation for the correct data formats |  -  |
| **500** | Downstream system error |  -  |

<a id="submitARefundForAPayment"></a>
# **submitARefundForAPayment**
> Refund submitARefundForAPayment(paymentId, body)

Submit a refund for a payment

Return issued refund information. The Authorisation token needs to be specified in the &#39;authorization&#39; header as &#39;authorization: Bearer YOUR_API_KEY_HERE&#39;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RefundingCardPaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://publicapi.payments.service.gov.uk");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    RefundingCardPaymentsApi apiInstance = new RefundingCardPaymentsApi(defaultClient);
    String paymentId = "paymentId_example"; // String | paymentId
    PaymentRefundRequest body = new PaymentRefundRequest(); // PaymentRefundRequest | requestPayload
    try {
      Refund result = apiInstance.submitARefundForAPayment(paymentId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RefundingCardPaymentsApi#submitARefundForAPayment");
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
| **paymentId** | **String**| paymentId | |
| **body** | [**PaymentRefundRequest**](PaymentRefundRequest.md)| requestPayload | |

### Return type

[**Refund**](Refund.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **202** | ACCEPTED |  -  |
| **401** | Credentials are required to access this resource |  -  |
| **404** | Not found |  -  |
| **412** | Refund amount available mismatch |  -  |
| **429** | Too many requests |  -  |
| **500** | Downstream system error |  -  |

