# CardPaymentsApi

All URIs are relative to *https://publicapi.payments.service.gov.uk*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelAPayment**](CardPaymentsApi.md#cancelAPayment) | **POST** /v1/payments/{paymentId}/cancel | Cancel payment |
| [**captureAPayment**](CardPaymentsApi.md#captureAPayment) | **POST** /v1/payments/{paymentId}/capture | Capture payment |
| [**createAPayment**](CardPaymentsApi.md#createAPayment) | **POST** /v1/payments | Create new payment |
| [**getAPayment**](CardPaymentsApi.md#getAPayment) | **GET** /v1/payments/{paymentId} | Find payment by ID |
| [**getEventsForAPayment**](CardPaymentsApi.md#getEventsForAPayment) | **GET** /v1/payments/{paymentId}/events | Return payment events by ID |
| [**searchPayments**](CardPaymentsApi.md#searchPayments) | **GET** /v1/payments | Search payments |


<a id="cancelAPayment"></a>
# **cancelAPayment**
> cancelAPayment(paymentId)

Cancel payment

Cancel a payment based on the provided payment ID and the Authorisation token. The Authorisation token needs to be specified in the &#39;authorization&#39; header as &#39;authorization: Bearer YOUR_API_KEY_HERE&#39;. A payment can only be cancelled if it&#39;s in a state that isn&#39;t finished.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CardPaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://publicapi.payments.service.gov.uk");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    CardPaymentsApi apiInstance = new CardPaymentsApi(defaultClient);
    String paymentId = "hu20sqlact5260q2nanm0q8u93"; // String | Payment identifier
    try {
      apiInstance.cancelAPayment(paymentId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CardPaymentsApi#cancelAPayment");
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
| **paymentId** | **String**| Payment identifier | |

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Cancellation of payment failed |  -  |
| **401** | Credentials are required to access this resource |  -  |
| **404** | Not found |  -  |
| **409** | Conflict |  -  |
| **429** | Too many requests |  -  |
| **500** | Downstream system error |  -  |

<a id="captureAPayment"></a>
# **captureAPayment**
> captureAPayment(paymentId)

Capture payment

Capture a payment based on the provided payment ID and the Authorisation token. The Authorisation token needs to be specified in the &#39;authorization&#39; header as &#39;authorization: Bearer YOUR_API_KEY_HERE&#39;. A payment can only be captured if it&#39;s in &#39;submitted&#39; state

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CardPaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://publicapi.payments.service.gov.uk");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    CardPaymentsApi apiInstance = new CardPaymentsApi(defaultClient);
    String paymentId = "hu20sqlact5260q2nanm0q8u93"; // String | Payment identifier
    try {
      apiInstance.captureAPayment(paymentId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CardPaymentsApi#captureAPayment");
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
| **paymentId** | **String**| Payment identifier | |

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Capture of payment failed |  -  |
| **401** | Credentials are required to access this resource |  -  |
| **404** | Not found |  -  |
| **409** | Conflict |  -  |
| **429** | Too many requests |  -  |
| **500** | Downstream system error |  -  |

<a id="createAPayment"></a>
# **createAPayment**
> CreatePaymentResult createAPayment(body)

Create new payment

Create a new payment for the account associated to the Authorisation token. The Authorisation token needs to be specified in the &#39;authorization&#39; header as &#39;authorization: Bearer YOUR_API_KEY_HERE&#39;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CardPaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://publicapi.payments.service.gov.uk");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    CardPaymentsApi apiInstance = new CardPaymentsApi(defaultClient);
    CreateCardPaymentRequest body = new CreateCardPaymentRequest(); // CreateCardPaymentRequest | requestPayload
    try {
      CreatePaymentResult result = apiInstance.createAPayment(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CardPaymentsApi#createAPayment");
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
| **body** | [**CreateCardPaymentRequest**](CreateCardPaymentRequest.md)| requestPayload | |

### Return type

[**CreatePaymentResult**](CreatePaymentResult.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Bad request |  -  |
| **401** | Credentials are required to access this resource |  -  |
| **422** | Invalid attribute value: description. Must be less than or equal to 255 characters length |  -  |
| **429** | Too many requests |  -  |
| **500** | Downstream system error |  -  |

<a id="getAPayment"></a>
# **getAPayment**
> GetPaymentResult getAPayment(paymentId)

Find payment by ID

Return information about the payment The Authorisation token needs to be specified in the &#39;authorization&#39; header as &#39;authorization: Bearer YOUR_API_KEY_HERE&#39;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CardPaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://publicapi.payments.service.gov.uk");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    CardPaymentsApi apiInstance = new CardPaymentsApi(defaultClient);
    String paymentId = "hu20sqlact5260q2nanm0q8u93"; // String | Payment identifier
    try {
      GetPaymentResult result = apiInstance.getAPayment(paymentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CardPaymentsApi#getAPayment");
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
| **paymentId** | **String**| Payment identifier | |

### Return type

[**GetPaymentResult**](GetPaymentResult.md)

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

<a id="getEventsForAPayment"></a>
# **getEventsForAPayment**
> PaymentEvents getEventsForAPayment(paymentId)

Return payment events by ID

Return payment events information about a certain payment The Authorisation token needs to be specified in the &#39;authorization&#39; header as &#39;authorization: Bearer YOUR_API_KEY_HERE&#39;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CardPaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://publicapi.payments.service.gov.uk");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    CardPaymentsApi apiInstance = new CardPaymentsApi(defaultClient);
    String paymentId = "hu20sqlact5260q2nanm0q8u93"; // String | Payment identifier
    try {
      PaymentEvents result = apiInstance.getEventsForAPayment(paymentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CardPaymentsApi#getEventsForAPayment");
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
| **paymentId** | **String**| Payment identifier | |

### Return type

[**PaymentEvents**](PaymentEvents.md)

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

<a id="searchPayments"></a>
# **searchPayments**
> PaymentSearchResults searchPayments(reference, email, state, cardBrand, fromDate, toDate, page, displaySize, cardholderName, firstDigitsCardNumber, lastDigitsCardNumber, fromSettledDate, toSettledDate)

Search payments

Search payments by reference, state, &#39;from&#39; and &#39;to&#39; date. The Authorisation token needs to be specified in the &#39;authorization&#39; header as &#39;authorization: Bearer YOUR_API_KEY_HERE&#39;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CardPaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://publicapi.payments.service.gov.uk");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    CardPaymentsApi apiInstance = new CardPaymentsApi(defaultClient);
    String reference = "reference_example"; // String | Your payment reference to search (exact match, case insensitive)
    String email = "email_example"; // String | The user email used in the payment to be searched
    String state = "created"; // String | State of payments to be searched. Example=success
    String cardBrand = "cardBrand_example"; // String | Card brand used for payment. Example=master-card
    String fromDate = "fromDate_example"; // String | From date of payments to be searched (this date is inclusive). Example=2015-08-13T12:35:00Z
    String toDate = "toDate_example"; // String | To date of payments to be searched (this date is exclusive). Example=2015-08-14T12:35:00Z
    String page = "page_example"; // String | Page number requested for the search, should be a positive integer (optional, defaults to 1)
    String displaySize = "displaySize_example"; // String | Number of results to be shown per page, should be a positive integer (optional, defaults to 500, max 500)
    String cardholderName = "cardholderName_example"; // String | Name on card used to make payment
    String firstDigitsCardNumber = "firstDigitsCardNumber_example"; // String | First six digits of the card used to make payment
    String lastDigitsCardNumber = "lastDigitsCardNumber_example"; // String | Last four digits of the card used to make payment
    String fromSettledDate = "fromSettledDate_example"; // String | From settled date of payment to be searched (this date is inclusive). Example=2015-08-13
    String toSettledDate = "toSettledDate_example"; // String | To settled date of payment to be searched (this date is inclusive). Example=2015-08-14
    try {
      PaymentSearchResults result = apiInstance.searchPayments(reference, email, state, cardBrand, fromDate, toDate, page, displaySize, cardholderName, firstDigitsCardNumber, lastDigitsCardNumber, fromSettledDate, toSettledDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CardPaymentsApi#searchPayments");
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
| **reference** | **String**| Your payment reference to search (exact match, case insensitive) | [optional] |
| **email** | **String**| The user email used in the payment to be searched | [optional] |
| **state** | **String**| State of payments to be searched. Example&#x3D;success | [optional] [enum: created, started, submitted, success, failed, cancelled, error] |
| **cardBrand** | **String**| Card brand used for payment. Example&#x3D;master-card | [optional] |
| **fromDate** | **String**| From date of payments to be searched (this date is inclusive). Example&#x3D;2015-08-13T12:35:00Z | [optional] |
| **toDate** | **String**| To date of payments to be searched (this date is exclusive). Example&#x3D;2015-08-14T12:35:00Z | [optional] |
| **page** | **String**| Page number requested for the search, should be a positive integer (optional, defaults to 1) | [optional] |
| **displaySize** | **String**| Number of results to be shown per page, should be a positive integer (optional, defaults to 500, max 500) | [optional] |
| **cardholderName** | **String**| Name on card used to make payment | [optional] |
| **firstDigitsCardNumber** | **String**| First six digits of the card used to make payment | [optional] |
| **lastDigitsCardNumber** | **String**| Last four digits of the card used to make payment | [optional] |
| **fromSettledDate** | **String**| From settled date of payment to be searched (this date is inclusive). Example&#x3D;2015-08-13 | [optional] |
| **toSettledDate** | **String**| To settled date of payment to be searched (this date is inclusive). Example&#x3D;2015-08-14 | [optional] |

### Return type

[**PaymentSearchResults**](PaymentSearchResults.md)

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
| **422** | Invalid parameters: from_date, to_date, status, display_size. See Public API documentation for the correct data formats |  -  |
| **429** | Too many requests |  -  |
| **500** | Downstream system error |  -  |

