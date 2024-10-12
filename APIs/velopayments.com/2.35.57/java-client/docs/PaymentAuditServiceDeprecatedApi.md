# PaymentAuditServiceDeprecatedApi

All URIs are relative to *https://api.sandbox.velopayments.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**exportTransactionsCSVV3**](PaymentAuditServiceDeprecatedApi.md#exportTransactionsCSVV3) | **GET** /v3/paymentaudit/transactions | V3 Export Transactions |
| [**getFundingsV1**](PaymentAuditServiceDeprecatedApi.md#getFundingsV1) | **GET** /v1/paymentaudit/fundings | V1 Get Fundings for Payor |
| [**getPaymentDetailsV3**](PaymentAuditServiceDeprecatedApi.md#getPaymentDetailsV3) | **GET** /v3/paymentaudit/payments/{paymentId} | V3 Get Payment |
| [**getPaymentsForPayoutPAV3**](PaymentAuditServiceDeprecatedApi.md#getPaymentsForPayoutPAV3) | **GET** /v3/paymentaudit/payouts/{payoutId} | V3 Get Payments for Payout |
| [**getPayoutStatsV1**](PaymentAuditServiceDeprecatedApi.md#getPayoutStatsV1) | **GET** /v1/paymentaudit/payoutStatistics | V1 Get Payout Statistics |
| [**getPayoutsForPayorV3**](PaymentAuditServiceDeprecatedApi.md#getPayoutsForPayorV3) | **GET** /v3/paymentaudit/payouts | V3 Get Payouts for Payor |
| [**listPaymentChanges**](PaymentAuditServiceDeprecatedApi.md#listPaymentChanges) | **GET** /v1/deltas/payments | V1 List Payment Changes |
| [**listPaymentsAuditV3**](PaymentAuditServiceDeprecatedApi.md#listPaymentsAuditV3) | **GET** /v3/paymentaudit/payments | V3 Get List of Payments |


<a id="exportTransactionsCSVV3"></a>
# **exportTransactionsCSVV3**
> PayorAmlTransactionV3 exportTransactionsCSVV3(payorId, startDate, endDate)

V3 Export Transactions

Deprecated (use /v4/paymentaudit/transactions instead)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentAuditServiceDeprecatedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PaymentAuditServiceDeprecatedApi apiInstance = new PaymentAuditServiceDeprecatedApi(defaultClient);
    UUID payorId = UUID.randomUUID(); // UUID | The Payor ID for whom you wish to run the report. For a Payor requesting the report, this could be their exact Payor, or it could be a child/descendant Payor. 
    LocalDate startDate = LocalDate.now(); // LocalDate | Start date, inclusive. Format is YYYY-MM-DD
    LocalDate endDate = LocalDate.now(); // LocalDate | End date, inclusive. Format is YYYY-MM-DD
    try {
      PayorAmlTransactionV3 result = apiInstance.exportTransactionsCSVV3(payorId, startDate, endDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentAuditServiceDeprecatedApi#exportTransactionsCSVV3");
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
| **payorId** | **UUID**| The Payor ID for whom you wish to run the report. For a Payor requesting the report, this could be their exact Payor, or it could be a child/descendant Payor.  | [optional] |
| **startDate** | **LocalDate**| Start date, inclusive. Format is YYYY-MM-DD | [optional] |
| **endDate** | **LocalDate**| End date, inclusive. Format is YYYY-MM-DD | [optional] |

### Return type

[**PayorAmlTransactionV3**](PayorAmlTransactionV3.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/csv, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Export Transactions response |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

<a id="getFundingsV1"></a>
# **getFundingsV1**
> GetFundingsResponse getFundingsV1(payorId, page, pageSize, sort)

V1 Get Fundings for Payor

Deprecated (use /v4/paymentaudit/fundings)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentAuditServiceDeprecatedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PaymentAuditServiceDeprecatedApi apiInstance = new PaymentAuditServiceDeprecatedApi(defaultClient);
    UUID payorId = UUID.randomUUID(); // UUID | The account owner Payor ID
    Integer page = 1; // Integer | Page number. Default is 1.
    Integer pageSize = 25; // Integer | The number of results to return in a page
    String sort = "sort_example"; // String | List of sort fields. Example: ```?sort=destinationCurrency:asc,destinationAmount:asc``` Default is no sort. The supported sort fields are: dateTime and amount. 
    try {
      GetFundingsResponse result = apiInstance.getFundingsV1(payorId, page, pageSize, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentAuditServiceDeprecatedApi#getFundingsV1");
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
| **payorId** | **UUID**| The account owner Payor ID | |
| **page** | **Integer**| Page number. Default is 1. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of results to return in a page | [optional] [default to 25] |
| **sort** | **String**| List of sort fields. Example: &#x60;&#x60;&#x60;?sort&#x3D;destinationCurrency:asc,destinationAmount:asc&#x60;&#x60;&#x60; Default is no sort. The supported sort fields are: dateTime and amount.  | [optional] |

### Return type

[**GetFundingsResponse**](GetFundingsResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get Fundings normal response |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

<a id="getPaymentDetailsV3"></a>
# **getPaymentDetailsV3**
> PaymentResponseV3 getPaymentDetailsV3(paymentId, sensitive)

V3 Get Payment

Deprecated (use /v4/paymentaudit/payments/&lt;paymentId&gt; instead)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentAuditServiceDeprecatedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PaymentAuditServiceDeprecatedApi apiInstance = new PaymentAuditServiceDeprecatedApi(defaultClient);
    UUID paymentId = UUID.randomUUID(); // UUID | Payment Id
    Boolean sensitive = true; // Boolean | Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values. 
    try {
      PaymentResponseV3 result = apiInstance.getPaymentDetailsV3(paymentId, sensitive);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentAuditServiceDeprecatedApi#getPaymentDetailsV3");
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
| **paymentId** | **UUID**| Payment Id | |
| **sensitive** | **Boolean**| Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values.  | [optional] |

### Return type

[**PaymentResponseV3**](PaymentResponseV3.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 response, request completed okay |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

<a id="getPaymentsForPayoutPAV3"></a>
# **getPaymentsForPayoutPAV3**
> GetPaymentsForPayoutResponseV3 getPaymentsForPayoutPAV3(payoutId, remoteId, status, sourceAmountFrom, sourceAmountTo, paymentAmountFrom, paymentAmountTo, submittedDateFrom, submittedDateTo, page, pageSize, sort, sensitive)

V3 Get Payments for Payout

Deprecated (use /v4/paymentaudit/payouts/&lt;payoutId&gt; instead)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentAuditServiceDeprecatedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PaymentAuditServiceDeprecatedApi apiInstance = new PaymentAuditServiceDeprecatedApi(defaultClient);
    UUID payoutId = UUID.randomUUID(); // UUID | The id (UUID) of the payout.
    String remoteId = "remoteId_example"; // String | The remote id of the payees.
    String status = "ACCEPTED"; // String | Payment Status
    Integer sourceAmountFrom = 56; // Integer | The source amount from range filter. Filters for sourceAmount >= sourceAmountFrom
    Integer sourceAmountTo = 56; // Integer | The source amount to range filter. Filters for sourceAmount ⇐ sourceAmountTo
    Integer paymentAmountFrom = 56; // Integer | The payment amount from range filter. Filters for paymentAmount >= paymentAmountFrom
    Integer paymentAmountTo = 56; // Integer | The payment amount to range filter. Filters for paymentAmount ⇐ paymentAmountTo
    LocalDate submittedDateFrom = LocalDate.now(); // LocalDate | The submitted date from range filter. Format is yyyy-MM-dd.
    LocalDate submittedDateTo = LocalDate.now(); // LocalDate | The submitted date to range filter. Format is yyyy-MM-dd.
    Integer page = 1; // Integer | Page number. Default is 1.
    Integer pageSize = 25; // Integer | The number of results to return in a page
    String sort = "sort_example"; // String | <p>List of sort fields (e.g. ?sort=submittedDateTime:asc,status:asc). Default is sort by remoteId</p> <p>The supported sort fields are: sourceAmount, sourceCurrency, paymentAmount, paymentCurrency, routingNumber, accountNumber, remoteId, submittedDateTime and status</p> 
    Boolean sensitive = true; // Boolean | Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values. 
    try {
      GetPaymentsForPayoutResponseV3 result = apiInstance.getPaymentsForPayoutPAV3(payoutId, remoteId, status, sourceAmountFrom, sourceAmountTo, paymentAmountFrom, paymentAmountTo, submittedDateFrom, submittedDateTo, page, pageSize, sort, sensitive);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentAuditServiceDeprecatedApi#getPaymentsForPayoutPAV3");
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
| **payoutId** | **UUID**| The id (UUID) of the payout. | |
| **remoteId** | **String**| The remote id of the payees. | [optional] |
| **status** | **String**| Payment Status | [optional] [enum: ACCEPTED, AWAITING_FUNDS, FUNDED, UNFUNDED, BANK_PAYMENT_REQUESTED, REJECTED, ACCEPTED_BY_RAILS, CONFIRMED, FAILED, RETURNED, WITHDRAWN] |
| **sourceAmountFrom** | **Integer**| The source amount from range filter. Filters for sourceAmount &gt;&#x3D; sourceAmountFrom | [optional] |
| **sourceAmountTo** | **Integer**| The source amount to range filter. Filters for sourceAmount ⇐ sourceAmountTo | [optional] |
| **paymentAmountFrom** | **Integer**| The payment amount from range filter. Filters for paymentAmount &gt;&#x3D; paymentAmountFrom | [optional] |
| **paymentAmountTo** | **Integer**| The payment amount to range filter. Filters for paymentAmount ⇐ paymentAmountTo | [optional] |
| **submittedDateFrom** | **LocalDate**| The submitted date from range filter. Format is yyyy-MM-dd. | [optional] |
| **submittedDateTo** | **LocalDate**| The submitted date to range filter. Format is yyyy-MM-dd. | [optional] |
| **page** | **Integer**| Page number. Default is 1. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of results to return in a page | [optional] [default to 25] |
| **sort** | **String**| &lt;p&gt;List of sort fields (e.g. ?sort&#x3D;submittedDateTime:asc,status:asc). Default is sort by remoteId&lt;/p&gt; &lt;p&gt;The supported sort fields are: sourceAmount, sourceCurrency, paymentAmount, paymentCurrency, routingNumber, accountNumber, remoteId, submittedDateTime and status&lt;/p&gt;  | [optional] |
| **sensitive** | **Boolean**| Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values.  | [optional] |

### Return type

[**GetPaymentsForPayoutResponseV3**](GetPaymentsForPayoutResponseV3.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 response, data found okay |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

<a id="getPayoutStatsV1"></a>
# **getPayoutStatsV1**
> GetPayoutStatistics getPayoutStatsV1(payorId)

V1 Get Payout Statistics

Deprecated (Use /v4/paymentaudit/payoutStatistics)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentAuditServiceDeprecatedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PaymentAuditServiceDeprecatedApi apiInstance = new PaymentAuditServiceDeprecatedApi(defaultClient);
    UUID payorId = UUID.randomUUID(); // UUID | The account owner Payor ID. Required for external users.
    try {
      GetPayoutStatistics result = apiInstance.getPayoutStatsV1(payorId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentAuditServiceDeprecatedApi#getPayoutStatsV1");
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
| **payorId** | **UUID**| The account owner Payor ID. Required for external users. | [optional] |

### Return type

[**GetPayoutStatistics**](GetPayoutStatistics.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Payout Statistics response |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

<a id="getPayoutsForPayorV3"></a>
# **getPayoutsForPayorV3**
> GetPayoutsResponseV3 getPayoutsForPayorV3(payorId, payoutMemo, status, submittedDateFrom, submittedDateTo, page, pageSize, sort)

V3 Get Payouts for Payor

Deprecated (use /v4/paymentaudit/payouts instead)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentAuditServiceDeprecatedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PaymentAuditServiceDeprecatedApi apiInstance = new PaymentAuditServiceDeprecatedApi(defaultClient);
    UUID payorId = UUID.randomUUID(); // UUID | The account owner Payor ID
    String payoutMemo = "payoutMemo_example"; // String | Payout Memo filter - case insensitive sub-string match
    String status = "ACCEPTED"; // String | Payout Status
    LocalDate submittedDateFrom = LocalDate.now(); // LocalDate | The submitted date from range filter. Format is yyyy-MM-dd.
    LocalDate submittedDateTo = LocalDate.now(); // LocalDate | The submitted date to range filter. Format is yyyy-MM-dd.
    Integer page = 1; // Integer | Page number. Default is 1.
    Integer pageSize = 25; // Integer | The number of results to return in a page
    String sort = "sort_example"; // String | List of sort fields (e.g. ?sort=submittedDateTime:asc,instructedDateTime:asc,status:asc) Default is submittedDateTime:asc The supported sort fields are: submittedDateTime, instructedDateTime, status. 
    try {
      GetPayoutsResponseV3 result = apiInstance.getPayoutsForPayorV3(payorId, payoutMemo, status, submittedDateFrom, submittedDateTo, page, pageSize, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentAuditServiceDeprecatedApi#getPayoutsForPayorV3");
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
| **payorId** | **UUID**| The account owner Payor ID | |
| **payoutMemo** | **String**| Payout Memo filter - case insensitive sub-string match | [optional] |
| **status** | **String**| Payout Status | [optional] [enum: ACCEPTED, REJECTED, SUBMITTED, QUOTED, INSTRUCTED, COMPLETED, INCOMPLETE, CONFIRMED, WITHDRAWN] |
| **submittedDateFrom** | **LocalDate**| The submitted date from range filter. Format is yyyy-MM-dd. | [optional] |
| **submittedDateTo** | **LocalDate**| The submitted date to range filter. Format is yyyy-MM-dd. | [optional] |
| **page** | **Integer**| Page number. Default is 1. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of results to return in a page | [optional] [default to 25] |
| **sort** | **String**| List of sort fields (e.g. ?sort&#x3D;submittedDateTime:asc,instructedDateTime:asc,status:asc) Default is submittedDateTime:asc The supported sort fields are: submittedDateTime, instructedDateTime, status.  | [optional] |

### Return type

[**GetPayoutsResponseV3**](GetPayoutsResponseV3.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Payor data found |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

<a id="listPaymentChanges"></a>
# **listPaymentChanges**
> PaymentDeltaResponseV1 listPaymentChanges(payorId, updatedSince, page, pageSize)

V1 List Payment Changes

Deprecated (use /v4/payments/deltas instead)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentAuditServiceDeprecatedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PaymentAuditServiceDeprecatedApi apiInstance = new PaymentAuditServiceDeprecatedApi(defaultClient);
    UUID payorId = UUID.randomUUID(); // UUID | The Payor ID to find associated Payments
    OffsetDateTime updatedSince = OffsetDateTime.now(); // OffsetDateTime | The updatedSince filter in the format YYYY-MM-DDThh:mm:ss+hh:mm
    Integer page = 1; // Integer | Page number. Default is 1.
    Integer pageSize = 100; // Integer | The number of results to return in a page
    try {
      PaymentDeltaResponseV1 result = apiInstance.listPaymentChanges(payorId, updatedSince, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentAuditServiceDeprecatedApi#listPaymentChanges");
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
| **payorId** | **UUID**| The Payor ID to find associated Payments | |
| **updatedSince** | **OffsetDateTime**| The updatedSince filter in the format YYYY-MM-DDThh:mm:ss+hh:mm | |
| **page** | **Integer**| Page number. Default is 1. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of results to return in a page | [optional] [default to 100] |

### Return type

[**PaymentDeltaResponseV1**](PaymentDeltaResponseV1.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of Payment Changes |  -  |
| **400** | Bad Request |  -  |

<a id="listPaymentsAuditV3"></a>
# **listPaymentsAuditV3**
> ListPaymentsResponseV3 listPaymentsAuditV3(payeeId, payorId, payorName, remoteId, status, sourceAccountName, sourceAmountFrom, sourceAmountTo, sourceCurrency, paymentAmountFrom, paymentAmountTo, paymentCurrency, submittedDateFrom, submittedDateTo, paymentMemo, page, pageSize, sort, sensitive)

V3 Get List of Payments

Deprecated (use /v4/paymentaudit/payments instead)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentAuditServiceDeprecatedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PaymentAuditServiceDeprecatedApi apiInstance = new PaymentAuditServiceDeprecatedApi(defaultClient);
    UUID payeeId = UUID.randomUUID(); // UUID | The UUID of the payee.
    UUID payorId = UUID.randomUUID(); // UUID | The account owner Payor Id. Required for external users.
    String payorName = "payorName_example"; // String | The payor’s name. This filters via a case insensitive substring match.
    String remoteId = "remoteId_example"; // String | The remote id of the payees.
    String status = "ACCEPTED"; // String | Payment Status
    String sourceAccountName = "sourceAccountName_example"; // String | The source account name filter. This filters via a case insensitive substring match.
    Integer sourceAmountFrom = 56; // Integer | The source amount from range filter. Filters for sourceAmount >= sourceAmountFrom
    Integer sourceAmountTo = 56; // Integer | The source amount to range filter. Filters for sourceAmount ⇐ sourceAmountTo
    String sourceCurrency = "sourceCurrency_example"; // String | The source currency filter. Filters based on an exact match on the currency.
    Integer paymentAmountFrom = 56; // Integer | The payment amount from range filter. Filters for paymentAmount >= paymentAmountFrom
    Integer paymentAmountTo = 56; // Integer | The payment amount to range filter. Filters for paymentAmount ⇐ paymentAmountTo
    String paymentCurrency = "paymentCurrency_example"; // String | The payment currency filter. Filters based on an exact match on the currency.
    LocalDate submittedDateFrom = LocalDate.now(); // LocalDate | The submitted date from range filter. Format is yyyy-MM-dd.
    LocalDate submittedDateTo = LocalDate.now(); // LocalDate | The submitted date to range filter. Format is yyyy-MM-dd.
    String paymentMemo = "paymentMemo_example"; // String | The payment memo filter. This filters via a case insensitive substring match.
    Integer page = 1; // Integer | Page number. Default is 1.
    Integer pageSize = 25; // Integer | The number of results to return in a page
    String sort = "sort_example"; // String | List of sort fields (e.g. ?sort=submittedDateTime:asc,status:asc). Default is sort by remoteId The supported sort fields are: sourceAmount, sourceCurrency, paymentAmount, paymentCurrency, routingNumber, accountNumber, remoteId, submittedDateTime and status 
    Boolean sensitive = true; // Boolean | Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values. 
    try {
      ListPaymentsResponseV3 result = apiInstance.listPaymentsAuditV3(payeeId, payorId, payorName, remoteId, status, sourceAccountName, sourceAmountFrom, sourceAmountTo, sourceCurrency, paymentAmountFrom, paymentAmountTo, paymentCurrency, submittedDateFrom, submittedDateTo, paymentMemo, page, pageSize, sort, sensitive);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentAuditServiceDeprecatedApi#listPaymentsAuditV3");
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
| **payeeId** | **UUID**| The UUID of the payee. | [optional] |
| **payorId** | **UUID**| The account owner Payor Id. Required for external users. | [optional] |
| **payorName** | **String**| The payor’s name. This filters via a case insensitive substring match. | [optional] |
| **remoteId** | **String**| The remote id of the payees. | [optional] |
| **status** | **String**| Payment Status | [optional] [enum: ACCEPTED, AWAITING_FUNDS, FUNDED, UNFUNDED, BANK_PAYMENT_REQUESTED, REJECTED, ACCEPTED_BY_RAILS, CONFIRMED, FAILED, RETURNED, WITHDRAWN] |
| **sourceAccountName** | **String**| The source account name filter. This filters via a case insensitive substring match. | [optional] |
| **sourceAmountFrom** | **Integer**| The source amount from range filter. Filters for sourceAmount &gt;&#x3D; sourceAmountFrom | [optional] |
| **sourceAmountTo** | **Integer**| The source amount to range filter. Filters for sourceAmount ⇐ sourceAmountTo | [optional] |
| **sourceCurrency** | **String**| The source currency filter. Filters based on an exact match on the currency. | [optional] |
| **paymentAmountFrom** | **Integer**| The payment amount from range filter. Filters for paymentAmount &gt;&#x3D; paymentAmountFrom | [optional] |
| **paymentAmountTo** | **Integer**| The payment amount to range filter. Filters for paymentAmount ⇐ paymentAmountTo | [optional] |
| **paymentCurrency** | **String**| The payment currency filter. Filters based on an exact match on the currency. | [optional] |
| **submittedDateFrom** | **LocalDate**| The submitted date from range filter. Format is yyyy-MM-dd. | [optional] |
| **submittedDateTo** | **LocalDate**| The submitted date to range filter. Format is yyyy-MM-dd. | [optional] |
| **paymentMemo** | **String**| The payment memo filter. This filters via a case insensitive substring match. | [optional] |
| **page** | **Integer**| Page number. Default is 1. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of results to return in a page | [optional] [default to 25] |
| **sort** | **String**| List of sort fields (e.g. ?sort&#x3D;submittedDateTime:asc,status:asc). Default is sort by remoteId The supported sort fields are: sourceAmount, sourceCurrency, paymentAmount, paymentCurrency, routingNumber, accountNumber, remoteId, submittedDateTime and status  | [optional] |
| **sensitive** | **Boolean**| Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values.  | [optional] |

### Return type

[**ListPaymentsResponseV3**](ListPaymentsResponseV3.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Paginated list of payments |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

