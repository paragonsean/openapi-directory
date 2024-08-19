# PaymentsApiApi

All URIs are relative to *https://api.nowpayments.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getEstimatedPrice**](PaymentsApiApi.md#getEstimatedPrice) | **GET** /v1/estimate | Get estimated price |
| [**getListOfPayments**](PaymentsApiApi.md#getListOfPayments) | **GET** /v1/payment/ | Get list of payments |
| [**getPaymentStatus**](PaymentsApiApi.md#getPaymentStatus) | **GET** /v1/payment/{payment_id} | Get payment status |
| [**getTheMinimumPaymentAmount**](PaymentsApiApi.md#getTheMinimumPaymentAmount) | **GET** /v1/min-amount | Get the minimum payment amount |
| [**getUpdatePaymentEstimate**](PaymentsApiApi.md#getUpdatePaymentEstimate) | **POST** /v1/payment/{id}/update-merchant-estimate | Get/Update payment estimate |


<a id="getEstimatedPrice"></a>
# **getEstimatedPrice**
> GetEstimatedPrice200Response getEstimatedPrice(amount, currencyFrom, currencyTo, xApiKey)

Get estimated price

This is a method for calculating the approximate price in cryptocurrency for a given value in Fiat currency. You will need to provide the initial cost in the Fiat currency (amount, currency_from) and the necessary cryptocurrency (currency_to) Currently following fiat currencies are available: usd, eur, nzd, brl, gbp.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nowpayments.io");

    PaymentsApiApi apiInstance = new PaymentsApiApi(defaultClient);
    String amount = "3999.5000"; // String | 
    String currencyFrom = "usd"; // String | 
    String currencyTo = "btc"; // String | 
    String xApiKey = "{{your_api_key}}"; // String | 
    try {
      GetEstimatedPrice200Response result = apiInstance.getEstimatedPrice(amount, currencyFrom, currencyTo, xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApiApi#getEstimatedPrice");
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
| **amount** | **String**|  | [optional] |
| **currencyFrom** | **String**|  | [optional] |
| **currencyTo** | **String**|  | [optional] |
| **xApiKey** | **String**|  | [optional] |

### Return type

[**GetEstimatedPrice200Response**](GetEstimatedPrice200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 |  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Expect-CT -  <br>  * NEL -  <br>  * Report-To -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Download-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  * cf-request-id -  <br>  |

<a id="getListOfPayments"></a>
# **getListOfPayments**
> GetListOfPayments200Response getListOfPayments(limit, page, sortBy, orderBy, dateFrom, dateTo, xApiKey)

Get list of payments

Returns the entire list of all transactions, created with certain API key. The list of optional parameters: - limit - number of records in one page. (possible values: from 1 to 500) - page - the page number you want to get (possible values: from 0 to **page count - 1**) - sortBy - sort the received list by a paramenter. Set to **created_at** by default (possible values: payment_id, payment_status, pay_address, price_amount, price_currency, pay_amount, actually_paid, pay_currency, order_id, order_description, purchase_id, outcome_amount, outcome_currency) - orderBy - display the list in ascending or descending order. Set to **asc** by default (possible values: asc, desc) - dateFrom - select the displayed period start date (date format: YYYY-MM-DD or yy-MM-ddTHH:mm:ss.SSSZ). - dateTo - select the displayed period end date (date format: YYYY-MM-DD or yy-MM-ddTHH:mm:ss.SSSZ).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nowpayments.io");

    PaymentsApiApi apiInstance = new PaymentsApiApi(defaultClient);
    String limit = "10"; // String | 
    String page = "0"; // String | 
    String sortBy = "created_at"; // String | 
    String orderBy = "asc"; // String | 
    String dateFrom = "2020-01-01"; // String | 
    String dateTo = "2021-01-01"; // String | 
    String xApiKey = "{{your_api_key}}"; // String | 
    try {
      GetListOfPayments200Response result = apiInstance.getListOfPayments(limit, page, sortBy, orderBy, dateFrom, dateTo, xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApiApi#getListOfPayments");
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
| **limit** | **String**|  | [optional] |
| **page** | **String**|  | [optional] |
| **sortBy** | **String**|  | [optional] |
| **orderBy** | **String**|  | [optional] |
| **dateFrom** | **String**|  | [optional] |
| **dateTo** | **String**|  | [optional] |
| **xApiKey** | **String**|  | [optional] |

### Return type

[**GetListOfPayments200Response**](GetListOfPayments200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 |  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Expect-CT -  <br>  * NEL -  <br>  * Report-To -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Download-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  * cf-request-id -  <br>  |

<a id="getPaymentStatus"></a>
# **getPaymentStatus**
> GetPaymentStatus200Response getPaymentStatus(paymentId, xApiKey)

Get payment status

Get the actual information about the payment. You need to provide the ID of the payment in the request.  NOTE! You should make the get payment status request with the same API key that you used in the create payment request. Here is the list of avalable statuses: - waiting - waiting for the customer to send the payment. The initial status of each payment. - confirming - the transaction is being processed on the blockchain. Appears when NOWPayments detect the funds from the user on the blockchain. - confirmed -  the process is confirmed by the blockchain. Customer’s funds have accumulated enough confirmations. - sending - the funds are being sent to your personal wallet. We are in the process of sending the funds to you. - partially_paid -  it shows that the customer sent the less than the actual price. Appears when the funds have arrived in your wallet. - finished - the funds have reached your personal address and the payment is finished. - failed -  the payment wasn&#39;t completed due to the error of some kind. - refunded -  the funds were refunded back to the user. - expired - the user didn&#39;t send the funds to the specified address in the 24 hour time window.  Additional info: - outcome_amount - this parameter shows the amount that will be (or is already) received on your Outcome Wallet once the transaction is settled. - outcome_currency - this parameter shows the currency in which the transaction will be settled. - invoice_id - this parameter shows invoice ID from which the payment was created

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nowpayments.io");

    PaymentsApiApi apiInstance = new PaymentsApiApi(defaultClient);
    String paymentId = "paymentId_example"; // String | 
    String xApiKey = "{{your_api_key}}"; // String | 
    try {
      GetPaymentStatus200Response result = apiInstance.getPaymentStatus(paymentId, xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApiApi#getPaymentStatus");
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
| **xApiKey** | **String**|  | [optional] |

### Return type

[**GetPaymentStatus200Response**](GetPaymentStatus200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 |  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Expect-CT -  <br>  * NEL -  <br>  * Report-To -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Download-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  * cf-request-id -  <br>  |

<a id="getTheMinimumPaymentAmount"></a>
# **getTheMinimumPaymentAmount**
> GetTheMinimumPaymentAmount200Response getTheMinimumPaymentAmount(currencyFrom, currencyTo, xApiKey)

Get the minimum payment amount

Get the minimum payment amount for a specific pair.  You can provide both currencies in the pair or just currency\\_from, and we will calculate the minimum payment amount for currency\\_from and currency which you have specified as the outcome in the Store Settings.  You can also specify one of the fiat currencies in the currency\\_from. In this case, the minimum payment will be calculated in this fiat currency.  You can also add field fiat\\_equivalent (optional field) to get the fiat equivalent of the minimum amount.  In the case of several outcome wallets we will calculate the minimum amount in the same way we route your payment to a specific wallet.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nowpayments.io");

    PaymentsApiApi apiInstance = new PaymentsApiApi(defaultClient);
    String currencyFrom = "eth"; // String | 
    String currencyTo = "trx"; // String | 
    String xApiKey = "{{your_api_key}}"; // String | 
    try {
      GetTheMinimumPaymentAmount200Response result = apiInstance.getTheMinimumPaymentAmount(currencyFrom, currencyTo, xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApiApi#getTheMinimumPaymentAmount");
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
| **currencyFrom** | **String**|  | [optional] |
| **currencyTo** | **String**|  | [optional] |
| **xApiKey** | **String**|  | [optional] |

### Return type

[**GetTheMinimumPaymentAmount200Response**](GetTheMinimumPaymentAmount200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 |  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Expect-CT -  <br>  * NEL -  <br>  * Report-To -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Download-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  * cf-request-id -  <br>  |

<a id="getUpdatePaymentEstimate"></a>
# **getUpdatePaymentEstimate**
> GetUpdatePaymentEstimate200Response getUpdatePaymentEstimate(id, xApiKey)

Get/Update payment estimate

This endpoint is required to get the current estimate on the payment, and update the current estimate.   Please note! Calling this estimate before &#x60;expiration_estimate_date&#x60; will return the current estimate, it won’t be updated.  &#x60;:id&#x60; \\- payment ID, for which you want to get the estimate  Response:   &#x60;id&#x60; \\- payment ID   &#x60;token_id&#x60; - id of api key used to create this payment (please discard this parameter)   &#x60;pay_amount&#x60; - payment estimate, the exact amount the user will have to send to complete the payment   &#x60;expiration_estimate_date&#x60; - expiration date of this estimate

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nowpayments.io");

    PaymentsApiApi apiInstance = new PaymentsApiApi(defaultClient);
    String id = "id_example"; // String | payment ID, for which you want to get the estimate
    String xApiKey = "{{your_api_key}}"; // String | 
    try {
      GetUpdatePaymentEstimate200Response result = apiInstance.getUpdatePaymentEstimate(id, xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApiApi#getUpdatePaymentEstimate");
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
| **id** | **String**| payment ID, for which you want to get the estimate | |
| **xApiKey** | **String**|  | [optional] |

### Return type

[**GetUpdatePaymentEstimate200Response**](GetUpdatePaymentEstimate200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 |  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Expect-CT -  <br>  * NEL -  <br>  * Report-To -  <br>  * Server -  <br>  * Transfer-Encoding -  <br>  * alt-svc -  <br>  * strict-transport-security -  <br>  * vary -  <br>  * x-content-type-options -  <br>  * x-dns-prefetch-control -  <br>  * x-download-options -  <br>  * x-frame-options -  <br>  * x-xss-protection -  <br>  |

