# PaymentsApi

All URIs are relative to *https://connect.squareup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelPayment**](PaymentsApi.md#cancelPayment) | **POST** /v2/payments/{payment_id}/cancel | CancelPayment |
| [**cancelPaymentByIdempotencyKey**](PaymentsApi.md#cancelPaymentByIdempotencyKey) | **POST** /v2/payments/cancel | CancelPaymentByIdempotencyKey |
| [**completePayment**](PaymentsApi.md#completePayment) | **POST** /v2/payments/{payment_id}/complete | CompletePayment |
| [**createPayment**](PaymentsApi.md#createPayment) | **POST** /v2/payments | CreatePayment |
| [**getPayment**](PaymentsApi.md#getPayment) | **GET** /v2/payments/{payment_id} | GetPayment |
| [**updatePayment**](PaymentsApi.md#updatePayment) | **PUT** /v2/payments/{payment_id} | UpdatePayment |
| [**v2PaymentsGet**](PaymentsApi.md#v2PaymentsGet) | **GET** /v2/payments | ListPayments |


<a id="cancelPayment"></a>
# **cancelPayment**
> CancelPaymentResponse cancelPayment(paymentId)

CancelPayment

Cancels (voids) a payment. You can use this endpoint to cancel a payment with  the APPROVED &#x60;status&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    String paymentId = "paymentId_example"; // String | The ID of the payment to cancel.
    try {
      CancelPaymentResponse result = apiInstance.cancelPayment(paymentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#cancelPayment");
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
| **paymentId** | **String**| The ID of the payment to cancel. | |

### Return type

[**CancelPaymentResponse**](CancelPaymentResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="cancelPaymentByIdempotencyKey"></a>
# **cancelPaymentByIdempotencyKey**
> CancelPaymentByIdempotencyKeyResponse cancelPaymentByIdempotencyKey(cancelPaymentByIdempotencyKeyRequest)

CancelPaymentByIdempotencyKey

Cancels (voids) a payment identified by the idempotency key that is specified in the request.  Use this method when the status of a &#x60;CreatePayment&#x60; request is unknown (for example, after you send a &#x60;CreatePayment&#x60; request, a network error occurs and you do not get a response). In this case, you can direct Square to cancel the payment using this endpoint. In the request, you provide the same idempotency key that you provided in your &#x60;CreatePayment&#x60; request that you want to cancel. After canceling the payment, you can submit your &#x60;CreatePayment&#x60; request again.  Note that if no payment with the specified idempotency key is found, no action is taken and the endpoint returns successfully.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    CancelPaymentByIdempotencyKeyRequest cancelPaymentByIdempotencyKeyRequest = new CancelPaymentByIdempotencyKeyRequest(); // CancelPaymentByIdempotencyKeyRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      CancelPaymentByIdempotencyKeyResponse result = apiInstance.cancelPaymentByIdempotencyKey(cancelPaymentByIdempotencyKeyRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#cancelPaymentByIdempotencyKey");
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
| **cancelPaymentByIdempotencyKeyRequest** | [**CancelPaymentByIdempotencyKeyRequest**](CancelPaymentByIdempotencyKeyRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**CancelPaymentByIdempotencyKeyResponse**](CancelPaymentByIdempotencyKeyResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="completePayment"></a>
# **completePayment**
> CompletePaymentResponse completePayment(paymentId)

CompletePayment

Completes (captures) a payment. By default, payments are set to complete immediately after they are created.  You can use this endpoint to complete a payment with the APPROVED &#x60;status&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    String paymentId = "paymentId_example"; // String | The unique ID identifying the payment to be completed.
    try {
      CompletePaymentResponse result = apiInstance.completePayment(paymentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#completePayment");
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
| **paymentId** | **String**| The unique ID identifying the payment to be completed. | |

### Return type

[**CompletePaymentResponse**](CompletePaymentResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="createPayment"></a>
# **createPayment**
> CreatePaymentResponse createPayment(createPaymentRequest)

CreatePayment

Creates a payment using the provided source. You can use this endpoint  to charge a card (credit/debit card or     Square gift card) or record a payment that the seller received outside of Square  (cash payment from a buyer or a payment that an external entity  processed on behalf of the seller).  The endpoint creates a  &#x60;Payment&#x60; object and returns it in the response.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    CreatePaymentRequest createPaymentRequest = new CreatePaymentRequest(); // CreatePaymentRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      CreatePaymentResponse result = apiInstance.createPayment(createPaymentRequest);
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
| **createPaymentRequest** | [**CreatePaymentRequest**](CreatePaymentRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**CreatePaymentResponse**](CreatePaymentResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getPayment"></a>
# **getPayment**
> GetPaymentResponse getPayment(paymentId)

GetPayment

Retrieves details for a specific payment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    String paymentId = "paymentId_example"; // String | A unique ID for the desired payment.
    try {
      GetPaymentResponse result = apiInstance.getPayment(paymentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#getPayment");
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
| **paymentId** | **String**| A unique ID for the desired payment. | |

### Return type

[**GetPaymentResponse**](GetPaymentResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="updatePayment"></a>
# **updatePayment**
> UpdatePaymentResponse updatePayment(paymentId, updatePaymentRequest)

UpdatePayment

Updates a payment with the APPROVED status. You can update the &#x60;amount_money&#x60; and &#x60;tip_money&#x60; using this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    String paymentId = "paymentId_example"; // String | The ID of the payment to update.
    UpdatePaymentRequest updatePaymentRequest = new UpdatePaymentRequest(); // UpdatePaymentRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      UpdatePaymentResponse result = apiInstance.updatePayment(paymentId, updatePaymentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#updatePayment");
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
| **paymentId** | **String**| The ID of the payment to update. | |
| **updatePaymentRequest** | [**UpdatePaymentRequest**](UpdatePaymentRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**UpdatePaymentResponse**](UpdatePaymentResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2PaymentsGet"></a>
# **v2PaymentsGet**
> ListPaymentsResponse v2PaymentsGet(beginTime, endTime, sortOrder, cursor, locationId, total, last4, cardBrand, limit)

ListPayments

Retrieves a list of payments taken by the account making the request.  Results are eventually consistent, and new payments or changes to payments might take several seconds to appear.  The maximum results per page is 100.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    String beginTime = "beginTime_example"; // String | The timestamp for the beginning of the reporting period, in RFC 3339 format. Inclusive. Default: The current time minus one year.
    String endTime = "endTime_example"; // String | The timestamp for the end of the reporting period, in RFC 3339 format.  Default: The current time.
    String sortOrder = "sortOrder_example"; // String | The order in which results are listed: - `ASC` - Oldest to newest. - `DESC` - Newest to oldest (default).
    String cursor = "cursor_example"; // String | A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of results for the original query.  For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).
    String locationId = "locationId_example"; // String | Limit results to the location supplied. By default, results are returned for the default (main) location associated with the seller.
    Long total = 56L; // Long | The exact amount in the `total_money` for a payment.
    String last4 = "last4_example"; // String | The last four digits of a payment card.
    String cardBrand = "cardBrand_example"; // String | The brand of the payment card (for example, VISA).
    Integer limit = 56; // Integer | The maximum number of results to be returned in a single page. It is possible to receive fewer results than the specified limit on a given page.  The default value of 100 is also the maximum allowed value. If the provided value is  greater than 100, it is ignored and the default value is used instead.  Default: `100`
    try {
      ListPaymentsResponse result = apiInstance.v2PaymentsGet(beginTime, endTime, sortOrder, cursor, locationId, total, last4, cardBrand, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#v2PaymentsGet");
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
| **beginTime** | **String**| The timestamp for the beginning of the reporting period, in RFC 3339 format. Inclusive. Default: The current time minus one year. | [optional] |
| **endTime** | **String**| The timestamp for the end of the reporting period, in RFC 3339 format.  Default: The current time. | [optional] |
| **sortOrder** | **String**| The order in which results are listed: - &#x60;ASC&#x60; - Oldest to newest. - &#x60;DESC&#x60; - Newest to oldest (default). | [optional] |
| **cursor** | **String**| A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of results for the original query.  For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination). | [optional] |
| **locationId** | **String**| Limit results to the location supplied. By default, results are returned for the default (main) location associated with the seller. | [optional] |
| **total** | **Long**| The exact amount in the &#x60;total_money&#x60; for a payment. | [optional] |
| **last4** | **String**| The last four digits of a payment card. | [optional] |
| **cardBrand** | **String**| The brand of the payment card (for example, VISA). | [optional] |
| **limit** | **Integer**| The maximum number of results to be returned in a single page. It is possible to receive fewer results than the specified limit on a given page.  The default value of 100 is also the maximum allowed value. If the provided value is  greater than 100, it is ignored and the default value is used instead.  Default: &#x60;100&#x60; | [optional] |

### Return type

[**ListPaymentsResponse**](ListPaymentsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

