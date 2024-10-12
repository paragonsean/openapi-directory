# PayoutsApi

All URIs are relative to *https://api.sandbox.velopayments.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createQuoteForPayoutV3**](PayoutsApi.md#createQuoteForPayoutV3) | **POST** /v3/payouts/{payoutId}/quote | Create a quote for the payout |
| [**deschedulePayout**](PayoutsApi.md#deschedulePayout) | **DELETE** /v3/payouts/{payoutId}/schedule | Deschedule a payout |
| [**getPaymentsForPayoutV3**](PayoutsApi.md#getPaymentsForPayoutV3) | **GET** /v3/payouts/{payoutId}/payments | Retrieve payments for a payout |
| [**getPayoutSummaryV3**](PayoutsApi.md#getPayoutSummaryV3) | **GET** /v3/payouts/{payoutId} | Get Payout Summary |
| [**instructPayoutV3**](PayoutsApi.md#instructPayoutV3) | **POST** /v3/payouts/{payoutId} | Instruct Payout |
| [**scheduleForPayout**](PayoutsApi.md#scheduleForPayout) | **POST** /v3/payouts/{payoutId}/schedule | Schedule a payout |
| [**submitPayoutV3**](PayoutsApi.md#submitPayoutV3) | **POST** /v3/payouts | Submit Payout |
| [**withdrawPayment**](PayoutsApi.md#withdrawPayment) | **POST** /v1/payments/{paymentId}/withdraw | Withdraw a Payment |
| [**withdrawPayoutV3**](PayoutsApi.md#withdrawPayoutV3) | **DELETE** /v3/payouts/{payoutId} | Withdraw Payout |


<a id="createQuoteForPayoutV3"></a>
# **createQuoteForPayoutV3**
> QuoteResponseV3 createQuoteForPayoutV3(payoutId)

Create a quote for the payout

Create quote for a payout

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayoutsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayoutsApi apiInstance = new PayoutsApi(defaultClient);
    UUID payoutId = UUID.randomUUID(); // UUID | Id of the payout
    try {
      QuoteResponseV3 result = apiInstance.createQuoteForPayoutV3(payoutId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayoutsApi#createQuoteForPayoutV3");
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
| **payoutId** | **UUID**| Id of the payout | |

### Return type

[**QuoteResponseV3**](QuoteResponseV3.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Quote for payout |  -  |
| **404** | The resource was not found or is no longer available  |  -  |
| **409** | The request contained data that would result in a duplicate value  |  -  |

<a id="deschedulePayout"></a>
# **deschedulePayout**
> deschedulePayout(payoutId)

Deschedule a payout

Remove the schedule for a scheduled payout

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayoutsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayoutsApi apiInstance = new PayoutsApi(defaultClient);
    UUID payoutId = UUID.randomUUID(); // UUID | Id of the payout
    try {
      apiInstance.deschedulePayout(payoutId);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayoutsApi#deschedulePayout");
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
| **payoutId** | **UUID**| Id of the payout | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Descheduled payout successfully |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |
| **409** | The request contained data that would result in a duplicate value  |  -  |

<a id="getPaymentsForPayoutV3"></a>
# **getPaymentsForPayoutV3**
> PagedPaymentsResponseV3 getPaymentsForPayoutV3(payoutId, status, remoteId, payorPaymentId, sourceAccountName, transmissionType, paymentMemo, pageSize, page)

Retrieve payments for a payout

Retrieve payments for a payout

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayoutsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayoutsApi apiInstance = new PayoutsApi(defaultClient);
    UUID payoutId = UUID.randomUUID(); // UUID | Id of the payout
    String status = "ACCEPTED"; // String | Payment Status * ACCEPTED: any payment which was accepted at submission time (status may have changed since) * REJECTED: any payment rejected by initial submission processing * WITHDRAWN: any payment which has been withdrawn * WITHDRAWABLE: any payment eligible for withdrawal 
    String remoteId = "remoteId_example"; // String | The remote id of the payees.
    String payorPaymentId = "payorPaymentId_example"; // String | Payor's Id of the Payment
    String sourceAccountName = "sourceAccountName_example"; // String | Physical Account Name
    String transmissionType = "ACH"; // String | Transmission Type * ACH * SAME_DAY_ACH * WIRE 
    String paymentMemo = "paymentMemo_example"; // String | Payment Memo of the Payment
    Integer pageSize = 25; // Integer | The number of results to return in a page
    Integer page = 1; // Integer | Page number. Default is 1.
    try {
      PagedPaymentsResponseV3 result = apiInstance.getPaymentsForPayoutV3(payoutId, status, remoteId, payorPaymentId, sourceAccountName, transmissionType, paymentMemo, pageSize, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayoutsApi#getPaymentsForPayoutV3");
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
| **payoutId** | **UUID**| Id of the payout | |
| **status** | **String**| Payment Status * ACCEPTED: any payment which was accepted at submission time (status may have changed since) * REJECTED: any payment rejected by initial submission processing * WITHDRAWN: any payment which has been withdrawn * WITHDRAWABLE: any payment eligible for withdrawal  | [optional] [enum: ACCEPTED, REJECTED, WITHDRAWN, WITHDRAWABLE] |
| **remoteId** | **String**| The remote id of the payees. | [optional] |
| **payorPaymentId** | **String**| Payor&#39;s Id of the Payment | [optional] |
| **sourceAccountName** | **String**| Physical Account Name | [optional] |
| **transmissionType** | **String**| Transmission Type * ACH * SAME_DAY_ACH * WIRE  | [optional] [enum: ACH, SAME_DAY_ACH, WIRE] |
| **paymentMemo** | **String**| Payment Memo of the Payment | [optional] |
| **pageSize** | **Integer**| The number of results to return in a page | [optional] [default to 25] |
| **page** | **Integer**| Page number. Default is 1. | [optional] [default to 1] |

### Return type

[**PagedPaymentsResponseV3**](PagedPaymentsResponseV3.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Payments for payout |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

<a id="getPayoutSummaryV3"></a>
# **getPayoutSummaryV3**
> PayoutSummaryResponseV3 getPayoutSummaryV3(payoutId)

Get Payout Summary

Get payout summary - returns the current state of the payout.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayoutsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayoutsApi apiInstance = new PayoutsApi(defaultClient);
    UUID payoutId = UUID.randomUUID(); // UUID | Id of the payout
    try {
      PayoutSummaryResponseV3 result = apiInstance.getPayoutSummaryV3(payoutId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayoutsApi#getPayoutSummaryV3");
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
| **payoutId** | **UUID**| Id of the payout | |

### Return type

[**PayoutSummaryResponseV3**](PayoutSummaryResponseV3.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of Payout |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

<a id="instructPayoutV3"></a>
# **instructPayoutV3**
> instructPayoutV3(payoutId, instructPayoutRequestV3)

Instruct Payout

Instruct a payout to be made for the specified payoutId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayoutsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayoutsApi apiInstance = new PayoutsApi(defaultClient);
    UUID payoutId = UUID.randomUUID(); // UUID | Id of the payout
    InstructPayoutRequestV3 instructPayoutRequestV3 = new InstructPayoutRequestV3(); // InstructPayoutRequestV3 | Additional instruct payout parameters
    try {
      apiInstance.instructPayoutV3(payoutId, instructPayoutRequestV3);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayoutsApi#instructPayoutV3");
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
| **payoutId** | **UUID**| Id of the payout | |
| **instructPayoutRequestV3** | [**InstructPayoutRequestV3**](InstructPayoutRequestV3.md)| Additional instruct payout parameters | [optional] |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | HTTP 202 Accepted |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |
| **409** | The request contained data that would result in a duplicate value  |  -  |

<a id="scheduleForPayout"></a>
# **scheduleForPayout**
> scheduleForPayout(payoutId, schedulePayoutRequestV3)

Schedule a payout

&lt;p&gt;Schedule a payout for auto-instruction in the future or update existing payout schedule if the payout has been scheduled before.&lt;/p&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayoutsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayoutsApi apiInstance = new PayoutsApi(defaultClient);
    UUID payoutId = UUID.randomUUID(); // UUID | Id of the payout
    SchedulePayoutRequestV3 schedulePayoutRequestV3 = new SchedulePayoutRequestV3(); // SchedulePayoutRequestV3 | schedule payout parameters
    try {
      apiInstance.scheduleForPayout(payoutId, schedulePayoutRequestV3);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayoutsApi#scheduleForPayout");
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
| **payoutId** | **UUID**| Id of the payout | |
| **schedulePayoutRequestV3** | [**SchedulePayoutRequestV3**](SchedulePayoutRequestV3.md)| schedule payout parameters | [optional] |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Payout is scheduled successfully |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |
| **409** | The request contained data that would result in a duplicate value  |  -  |

<a id="submitPayoutV3"></a>
# **submitPayoutV3**
> submitPayoutV3(createPayoutRequestV3)

Submit Payout

&lt;p&gt;Create a new payout and return a location header with a link to the payout&lt;/p&gt; &lt;p&gt;Basic validation of the payout is performed before returning but more comprehensive validation is done asynchronously&lt;/p&gt; &lt;p&gt;The results can be obtained by issuing a HTTP GET to the URL returned in the location header&lt;/p&gt; &lt;p&gt;**NOTE:** amount values in payments must be in &#39;minor units&#39; format. E.g. cents for USD, pence for GBP etc with no decimal places&lt;/p&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayoutsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayoutsApi apiInstance = new PayoutsApi(defaultClient);
    CreatePayoutRequestV3 createPayoutRequestV3 = new CreatePayoutRequestV3(); // CreatePayoutRequestV3 | Post amount to transfer using stored funding account details.
    try {
      apiInstance.submitPayoutV3(createPayoutRequestV3);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayoutsApi#submitPayoutV3");
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
| **createPayoutRequestV3** | [**CreatePayoutRequestV3**](CreatePayoutRequestV3.md)| Post amount to transfer using stored funding account details. | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Successful submission of the payout |  * Location - Reference to created payout <br>  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

<a id="withdrawPayment"></a>
# **withdrawPayment**
> withdrawPayment(paymentId, withdrawPaymentRequest)

Withdraw a Payment

&lt;p&gt;withdraw a payment &lt;/p&gt; &lt;p&gt;There are a variety of reasons why this can fail&lt;/p&gt; &lt;ul&gt;     &lt;li&gt;the payment must be in a state of &#39;accepted&#39; or &#39;unfunded&#39;&lt;/li&gt;     &lt;li&gt;the payout must not be in a state of &#39;instructed&#39;&lt;/li&gt; &lt;/ul&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayoutsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayoutsApi apiInstance = new PayoutsApi(defaultClient);
    UUID paymentId = UUID.randomUUID(); // UUID | Id of the Payment
    WithdrawPaymentRequest withdrawPaymentRequest = new WithdrawPaymentRequest(); // WithdrawPaymentRequest | details for withdrawal
    try {
      apiInstance.withdrawPayment(paymentId, withdrawPaymentRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayoutsApi#withdrawPayment");
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
| **paymentId** | **UUID**| Id of the Payment | |
| **withdrawPaymentRequest** | [**WithdrawPaymentRequest**](WithdrawPaymentRequest.md)| details for withdrawal | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The payment was withdrawn |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

<a id="withdrawPayoutV3"></a>
# **withdrawPayoutV3**
> withdrawPayoutV3(payoutId)

Withdraw Payout

Withdraw Payout will remove the payout details from the rails but the payout will still be accessible in payout service in WITHDRAWN status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayoutsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayoutsApi apiInstance = new PayoutsApi(defaultClient);
    UUID payoutId = UUID.randomUUID(); // UUID | Id of the payout
    try {
      apiInstance.withdrawPayoutV3(payoutId);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayoutsApi#withdrawPayoutV3");
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
| **payoutId** | **UUID**| Id of the payout | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | HTTP 202 Accepted |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

