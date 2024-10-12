# PaymentAuditServiceApi

All URIs are relative to *https://api.sandbox.velopayments.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**exportTransactionsCSVV4**](PaymentAuditServiceApi.md#exportTransactionsCSVV4) | **GET** /v4/paymentaudit/transactions | Export Transactions |
| [**getFundingsV4**](PaymentAuditServiceApi.md#getFundingsV4) | **GET** /v4/paymentaudit/fundings | Get Fundings for Payor |
| [**getPaymentDetailsV4**](PaymentAuditServiceApi.md#getPaymentDetailsV4) | **GET** /v4/paymentaudit/payments/{paymentId} | Get Payment |
| [**getPaymentsForPayoutV4**](PaymentAuditServiceApi.md#getPaymentsForPayoutV4) | **GET** /v4/paymentaudit/payouts/{payoutId} | Get Payments for Payout |
| [**getPayoutStatsV4**](PaymentAuditServiceApi.md#getPayoutStatsV4) | **GET** /v4/paymentaudit/payoutStatistics | Get Payout Statistics |
| [**getPayoutsForPayorV4**](PaymentAuditServiceApi.md#getPayoutsForPayorV4) | **GET** /v4/paymentaudit/payouts | Get Payouts for Payor |
| [**listPaymentChangesV4**](PaymentAuditServiceApi.md#listPaymentChangesV4) | **GET** /v4/payments/deltas | List Payment Changes |
| [**listPaymentsAuditV4**](PaymentAuditServiceApi.md#listPaymentsAuditV4) | **GET** /v4/paymentaudit/payments | Get List of Payments |


<a id="exportTransactionsCSVV4"></a>
# **exportTransactionsCSVV4**
> PayorAmlTransaction exportTransactionsCSVV4(payorId, startDate, endDate, include)

Export Transactions

Download a CSV file containing payments in a date range. Uses Transfer-Encoding - chunked to stream to the client. Date range is inclusive of both the start and end dates.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentAuditServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PaymentAuditServiceApi apiInstance = new PaymentAuditServiceApi(defaultClient);
    UUID payorId = UUID.randomUUID(); // UUID | <p>The Payor ID for whom you wish to run the report.</p> <p>For a Payor requesting the report, this could be their exact Payor, or it could be a child/descendant Payor.</p> 
    LocalDate startDate = LocalDate.now(); // LocalDate | Start date, inclusive. Format is YYYY-MM-DD
    LocalDate endDate = LocalDate.now(); // LocalDate | End date, inclusive. Format is YYYY-MM-DD
    String include = "payorOnly"; // String | <p>Mode to determine whether to include other Payor's data in the results.</p> <p>May only be used if payorId is specified.</p> <p>Can be omitted or set to 'payorOnly' or 'payorAndDescendants'.</p> <p>payorOnly: Only include results for the specified Payor. This is the default if 'include' is omitted.</p> <p>payorAndDescendants: Aggregate results for all descendant Payors of the specified Payor. Should only be used if the Payor with the specified payorId has at least one child Payor.</p> <p>Note when a Payor requests the report and include=payorAndDescendants is used, the following additional columns are included in the CSV: Payor Name, Payor Id</p> 
    try {
      PayorAmlTransaction result = apiInstance.exportTransactionsCSVV4(payorId, startDate, endDate, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentAuditServiceApi#exportTransactionsCSVV4");
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
| **payorId** | **UUID**| &lt;p&gt;The Payor ID for whom you wish to run the report.&lt;/p&gt; &lt;p&gt;For a Payor requesting the report, this could be their exact Payor, or it could be a child/descendant Payor.&lt;/p&gt;  | [optional] |
| **startDate** | **LocalDate**| Start date, inclusive. Format is YYYY-MM-DD | [optional] |
| **endDate** | **LocalDate**| End date, inclusive. Format is YYYY-MM-DD | [optional] |
| **include** | **String**| &lt;p&gt;Mode to determine whether to include other Payor&#39;s data in the results.&lt;/p&gt; &lt;p&gt;May only be used if payorId is specified.&lt;/p&gt; &lt;p&gt;Can be omitted or set to &#39;payorOnly&#39; or &#39;payorAndDescendants&#39;.&lt;/p&gt; &lt;p&gt;payorOnly: Only include results for the specified Payor. This is the default if &#39;include&#39; is omitted.&lt;/p&gt; &lt;p&gt;payorAndDescendants: Aggregate results for all descendant Payors of the specified Payor. Should only be used if the Payor with the specified payorId has at least one child Payor.&lt;/p&gt; &lt;p&gt;Note when a Payor requests the report and include&#x3D;payorAndDescendants is used, the following additional columns are included in the CSV: Payor Name, Payor Id&lt;/p&gt;  | [optional] [enum: payorOnly, payorAndDescendants] |

### Return type

[**PayorAmlTransaction**](PayorAmlTransaction.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Export Transactions response |  -  |
| **400** | invalid Request |  -  |
| **401** | Not Authorized |  -  |
| **403** | Forbidden |  -  |

<a id="getFundingsV4"></a>
# **getFundingsV4**
> GetFundingsResponse getFundingsV4(payorId, sourceAccountName, page, pageSize, sort)

Get Fundings for Payor

&lt;p&gt;Get a list of Fundings for a payor.&lt;/p&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentAuditServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PaymentAuditServiceApi apiInstance = new PaymentAuditServiceApi(defaultClient);
    UUID payorId = UUID.randomUUID(); // UUID | The account owner Payor ID
    String sourceAccountName = "sourceAccountName_example"; // String | The source account name
    Integer page = 1; // Integer | Page number. Default is 1.
    Integer pageSize = 25; // Integer | The number of results to return in a page
    String sort = "sort_example"; // String | List of sort fields. Example: ```?sort=destinationCurrency:asc,destinationAmount:asc``` Default is no sort. The supported sort fields are: dateTime and amount. 
    try {
      GetFundingsResponse result = apiInstance.getFundingsV4(payorId, sourceAccountName, page, pageSize, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentAuditServiceApi#getFundingsV4");
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
| **sourceAccountName** | **String**| The source account name | [optional] |
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

<a id="getPaymentDetailsV4"></a>
# **getPaymentDetailsV4**
> PaymentResponseV4 getPaymentDetailsV4(paymentId, sensitive)

Get Payment

Get the payment with the given id. This contains the payment history. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentAuditServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PaymentAuditServiceApi apiInstance = new PaymentAuditServiceApi(defaultClient);
    UUID paymentId = UUID.randomUUID(); // UUID | Payment Id
    Boolean sensitive = true; // Boolean | Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values. 
    try {
      PaymentResponseV4 result = apiInstance.getPaymentDetailsV4(paymentId, sensitive);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentAuditServiceApi#getPaymentDetailsV4");
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

[**PaymentResponseV4**](PaymentResponseV4.md)

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

<a id="getPaymentsForPayoutV4"></a>
# **getPaymentsForPayoutV4**
> GetPaymentsForPayoutResponseV4 getPaymentsForPayoutV4(payoutId, railsId, remoteId, remoteSystemId, status, sourceAmountFrom, sourceAmountTo, paymentAmountFrom, paymentAmountTo, submittedDateFrom, submittedDateTo, transmissionType, page, pageSize, sort, sensitive)

Get Payments for Payout

Get List of payments for Payout, allowing for RETURNED status 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentAuditServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PaymentAuditServiceApi apiInstance = new PaymentAuditServiceApi(defaultClient);
    UUID payoutId = UUID.randomUUID(); // UUID | The id (UUID) of the payout.
    String railsId = "railsId_example"; // String | Payout Rails ID filter - case insensitive match. Any value is allowed, but you should use one of the supported railsId values. To get this list of values, you should call the 'Get Supported Rails' endpoint. 
    String remoteId = "remoteId_example"; // String | The remote id of the payees.
    String remoteSystemId = "remoteSystemId_example"; // String | The id of the remote system that is orchestrating payments
    String status = "ACCEPTED"; // String | Payment Status
    Integer sourceAmountFrom = 56; // Integer | The source amount from range filter. Filters for sourceAmount >= sourceAmountFrom
    Integer sourceAmountTo = 56; // Integer | The source amount to range filter. Filters for sourceAmount ⇐ sourceAmountTo
    Integer paymentAmountFrom = 56; // Integer | The payment amount from range filter. Filters for paymentAmount >= paymentAmountFrom
    Integer paymentAmountTo = 56; // Integer | The payment amount to range filter. Filters for paymentAmount ⇐ paymentAmountTo
    LocalDate submittedDateFrom = LocalDate.now(); // LocalDate | The submitted date from range filter. Format is yyyy-MM-dd.
    LocalDate submittedDateTo = LocalDate.now(); // LocalDate | The submitted date to range filter. Format is yyyy-MM-dd.
    String transmissionType = "ACH"; // String | Transmission Type * ACH * SAME_DAY_ACH * WIRE * GACHO 
    Integer page = 1; // Integer | Page number. Default is 1.
    Integer pageSize = 25; // Integer | The number of results to return in a page
    String sort = "sort_example"; // String | List of sort fields (e.g. ?sort=submittedDateTime:asc,status:asc). Default is sort by remoteId The supported sort fields are: sourceAmount, sourceCurrency, paymentAmount, paymentCurrency, routingNumber, accountNumber, remoteId, submittedDateTime and status 
    Boolean sensitive = true; // Boolean | Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values. 
    try {
      GetPaymentsForPayoutResponseV4 result = apiInstance.getPaymentsForPayoutV4(payoutId, railsId, remoteId, remoteSystemId, status, sourceAmountFrom, sourceAmountTo, paymentAmountFrom, paymentAmountTo, submittedDateFrom, submittedDateTo, transmissionType, page, pageSize, sort, sensitive);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentAuditServiceApi#getPaymentsForPayoutV4");
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
| **railsId** | **String**| Payout Rails ID filter - case insensitive match. Any value is allowed, but you should use one of the supported railsId values. To get this list of values, you should call the &#39;Get Supported Rails&#39; endpoint.  | [optional] |
| **remoteId** | **String**| The remote id of the payees. | [optional] |
| **remoteSystemId** | **String**| The id of the remote system that is orchestrating payments | [optional] |
| **status** | **String**| Payment Status | [optional] [enum: ACCEPTED, AWAITING_FUNDS, FUNDED, UNFUNDED, BANK_PAYMENT_REQUESTED, REJECTED, ACCEPTED_BY_RAILS, CONFIRMED, FAILED, RETURNED, WITHDRAWN] |
| **sourceAmountFrom** | **Integer**| The source amount from range filter. Filters for sourceAmount &gt;&#x3D; sourceAmountFrom | [optional] |
| **sourceAmountTo** | **Integer**| The source amount to range filter. Filters for sourceAmount ⇐ sourceAmountTo | [optional] |
| **paymentAmountFrom** | **Integer**| The payment amount from range filter. Filters for paymentAmount &gt;&#x3D; paymentAmountFrom | [optional] |
| **paymentAmountTo** | **Integer**| The payment amount to range filter. Filters for paymentAmount ⇐ paymentAmountTo | [optional] |
| **submittedDateFrom** | **LocalDate**| The submitted date from range filter. Format is yyyy-MM-dd. | [optional] |
| **submittedDateTo** | **LocalDate**| The submitted date to range filter. Format is yyyy-MM-dd. | [optional] |
| **transmissionType** | **String**| Transmission Type * ACH * SAME_DAY_ACH * WIRE * GACHO  | [optional] [enum: ACH, SAME_DAY_ACH, WIRE, LOCAL, GACHO] |
| **page** | **Integer**| Page number. Default is 1. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of results to return in a page | [optional] [default to 25] |
| **sort** | **String**| List of sort fields (e.g. ?sort&#x3D;submittedDateTime:asc,status:asc). Default is sort by remoteId The supported sort fields are: sourceAmount, sourceCurrency, paymentAmount, paymentCurrency, routingNumber, accountNumber, remoteId, submittedDateTime and status  | [optional] |
| **sensitive** | **Boolean**| Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values.  | [optional] |

### Return type

[**GetPaymentsForPayoutResponseV4**](GetPaymentsForPayoutResponseV4.md)

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

<a id="getPayoutStatsV4"></a>
# **getPayoutStatsV4**
> GetPayoutStatistics getPayoutStatsV4(payorId)

Get Payout Statistics

&lt;p&gt;Get payout statistics for a payor.&lt;/p&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentAuditServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PaymentAuditServiceApi apiInstance = new PaymentAuditServiceApi(defaultClient);
    UUID payorId = UUID.randomUUID(); // UUID | The account owner Payor ID. Required for external users.
    try {
      GetPayoutStatistics result = apiInstance.getPayoutStatsV4(payorId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentAuditServiceApi#getPayoutStatsV4");
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

<a id="getPayoutsForPayorV4"></a>
# **getPayoutsForPayorV4**
> GetPayoutsResponse getPayoutsForPayorV4(payorId, payoutMemo, status, submittedDateFrom, submittedDateTo, fromPayorName, scheduledForDateFrom, scheduledForDateTo, scheduleStatus, page, pageSize, sort)

Get Payouts for Payor

Get List of payouts for payor 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentAuditServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PaymentAuditServiceApi apiInstance = new PaymentAuditServiceApi(defaultClient);
    UUID payorId = UUID.randomUUID(); // UUID | The id (UUID) of the payor funding the payout or the payor whose payees are being paid.
    String payoutMemo = "payoutMemo_example"; // String | Payout Memo filter - case insensitive sub-string match
    String status = "ACCEPTED"; // String | Payout Status
    LocalDate submittedDateFrom = LocalDate.now(); // LocalDate | The submitted date from range filter. Format is yyyy-MM-dd.
    LocalDate submittedDateTo = LocalDate.now(); // LocalDate | The submitted date to range filter. Format is yyyy-MM-dd.
    String fromPayorName = "fromPayorName_example"; // String | The name of the payor whose payees are being paid. This filters via a case insensitive substring match.
    LocalDate scheduledForDateFrom = LocalDate.now(); // LocalDate | Filter payouts scheduled to run on or after the given date. Format is yyyy-MM-dd.
    LocalDate scheduledForDateTo = LocalDate.now(); // LocalDate | Filter payouts scheduled to run on or before the given date. Format is yyyy-MM-dd.
    String scheduleStatus = "ANY"; // String | Payout Schedule Status
    Integer page = 1; // Integer | Page number. Default is 1.
    Integer pageSize = 25; // Integer | The number of results to return in a page
    String sort = "sort_example"; // String | List of sort fields (e.g. ?sort=submittedDateTime:asc,instructedDateTime:asc,status:asc) Default is submittedDateTime:asc The supported sort fields are: submittedDateTime, instructedDateTime, status, totalPayments, payoutId, scheduledFor 
    try {
      GetPayoutsResponse result = apiInstance.getPayoutsForPayorV4(payorId, payoutMemo, status, submittedDateFrom, submittedDateTo, fromPayorName, scheduledForDateFrom, scheduledForDateTo, scheduleStatus, page, pageSize, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentAuditServiceApi#getPayoutsForPayorV4");
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
| **payorId** | **UUID**| The id (UUID) of the payor funding the payout or the payor whose payees are being paid. | [optional] |
| **payoutMemo** | **String**| Payout Memo filter - case insensitive sub-string match | [optional] |
| **status** | **String**| Payout Status | [optional] [enum: ACCEPTED, REJECTED, SUBMITTED, QUOTED, INSTRUCTED, COMPLETED, INCOMPLETE, CONFIRMED, WITHDRAWN] |
| **submittedDateFrom** | **LocalDate**| The submitted date from range filter. Format is yyyy-MM-dd. | [optional] |
| **submittedDateTo** | **LocalDate**| The submitted date to range filter. Format is yyyy-MM-dd. | [optional] |
| **fromPayorName** | **String**| The name of the payor whose payees are being paid. This filters via a case insensitive substring match. | [optional] |
| **scheduledForDateFrom** | **LocalDate**| Filter payouts scheduled to run on or after the given date. Format is yyyy-MM-dd. | [optional] |
| **scheduledForDateTo** | **LocalDate**| Filter payouts scheduled to run on or before the given date. Format is yyyy-MM-dd. | [optional] |
| **scheduleStatus** | **String**| Payout Schedule Status | [optional] [enum: ANY, SCHEDULED, EXECUTED, FAILED] |
| **page** | **Integer**| Page number. Default is 1. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of results to return in a page | [optional] [default to 25] |
| **sort** | **String**| List of sort fields (e.g. ?sort&#x3D;submittedDateTime:asc,instructedDateTime:asc,status:asc) Default is submittedDateTime:asc The supported sort fields are: submittedDateTime, instructedDateTime, status, totalPayments, payoutId, scheduledFor  | [optional] |

### Return type

[**GetPayoutsResponse**](GetPayoutsResponse.md)

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

<a id="listPaymentChangesV4"></a>
# **listPaymentChangesV4**
> PaymentDeltaResponse listPaymentChangesV4(payorId, updatedSince, page, pageSize)

List Payment Changes

Get a paginated response listing payment changes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentAuditServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PaymentAuditServiceApi apiInstance = new PaymentAuditServiceApi(defaultClient);
    UUID payorId = UUID.randomUUID(); // UUID | The Payor ID to find associated Payments
    OffsetDateTime updatedSince = OffsetDateTime.now(); // OffsetDateTime | The updatedSince filter in the format YYYY-MM-DDThh:mm:ss+hh:mm
    Integer page = 1; // Integer | Page number. Default is 1.
    Integer pageSize = 100; // Integer | The number of results to return in a page
    try {
      PaymentDeltaResponse result = apiInstance.listPaymentChangesV4(payorId, updatedSince, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentAuditServiceApi#listPaymentChangesV4");
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

[**PaymentDeltaResponse**](PaymentDeltaResponse.md)

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

<a id="listPaymentsAuditV4"></a>
# **listPaymentsAuditV4**
> ListPaymentsResponseV4 listPaymentsAuditV4(payeeId, payorId, payorName, remoteId, remoteSystemId, status, transmissionType, sourceAccountName, sourceAmountFrom, sourceAmountTo, sourceCurrency, paymentAmountFrom, paymentAmountTo, paymentCurrency, submittedDateFrom, submittedDateTo, paymentMemo, railsId, scheduledForDateFrom, scheduledForDateTo, scheduleStatus, postInstructFxStatus, page, pageSize, sort, sensitive)

Get List of Payments

Get payments for the given payor Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentAuditServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PaymentAuditServiceApi apiInstance = new PaymentAuditServiceApi(defaultClient);
    UUID payeeId = UUID.randomUUID(); // UUID | The UUID of the payee.
    UUID payorId = UUID.randomUUID(); // UUID | The account owner Payor Id. Required for external users.
    String payorName = "payorName_example"; // String | The payor’s name. This filters via a case insensitive substring match.
    String remoteId = "remoteId_example"; // String | The remote id of the payees.
    String remoteSystemId = "remoteSystemId_example"; // String | The id of the remote system that is orchestrating payments
    String status = "ACCEPTED"; // String | Payment Status
    String transmissionType = "ACH"; // String | Transmission Type * ACH * SAME_DAY_ACH * WIRE * GACHO 
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
    String railsId = "railsId_example"; // String | Payout Rails ID filter - case insensitive match. Any value is allowed, but you should use one of the supported railsId values. To get this list of values, you should call the 'Get Supported Rails' endpoint. 
    LocalDate scheduledForDateFrom = LocalDate.now(); // LocalDate | Filter payouts scheduled to run on or after the given date. Format is yyyy-MM-dd.
    LocalDate scheduledForDateTo = LocalDate.now(); // LocalDate | Filter payouts scheduled to run on or before the given date. Format is yyyy-MM-dd.
    String scheduleStatus = "ANY"; // String | Payout Schedule Status
    String postInstructFxStatus = "ANY"; // String | The status of the post instruct FX step if one was required for the payment
    Integer page = 1; // Integer | Page number. Default is 1.
    Integer pageSize = 25; // Integer | The number of results to return in a page
    String sort = "sort_example"; // String | List of sort fields (e.g. ?sort=submittedDateTime:asc,status:asc). Default is sort by submittedDateTime:desc,paymentId:asc The supported sort fields are: sourceAmount, sourceCurrency, paymentAmount, paymentCurrency, routingNumber, accountNumber, remoteId, submittedDateTime, status and paymentId 
    Boolean sensitive = true; // Boolean | Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values. 
    try {
      ListPaymentsResponseV4 result = apiInstance.listPaymentsAuditV4(payeeId, payorId, payorName, remoteId, remoteSystemId, status, transmissionType, sourceAccountName, sourceAmountFrom, sourceAmountTo, sourceCurrency, paymentAmountFrom, paymentAmountTo, paymentCurrency, submittedDateFrom, submittedDateTo, paymentMemo, railsId, scheduledForDateFrom, scheduledForDateTo, scheduleStatus, postInstructFxStatus, page, pageSize, sort, sensitive);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentAuditServiceApi#listPaymentsAuditV4");
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
| **remoteSystemId** | **String**| The id of the remote system that is orchestrating payments | [optional] |
| **status** | **String**| Payment Status | [optional] [enum: ACCEPTED, AWAITING_FUNDS, FUNDED, UNFUNDED, BANK_PAYMENT_REQUESTED, REJECTED, ACCEPTED_BY_RAILS, CONFIRMED, FAILED, RETURNED, WITHDRAWN] |
| **transmissionType** | **String**| Transmission Type * ACH * SAME_DAY_ACH * WIRE * GACHO  | [optional] [enum: ACH, SAME_DAY_ACH, WIRE, LOCAL, GACHO] |
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
| **railsId** | **String**| Payout Rails ID filter - case insensitive match. Any value is allowed, but you should use one of the supported railsId values. To get this list of values, you should call the &#39;Get Supported Rails&#39; endpoint.  | [optional] |
| **scheduledForDateFrom** | **LocalDate**| Filter payouts scheduled to run on or after the given date. Format is yyyy-MM-dd. | [optional] |
| **scheduledForDateTo** | **LocalDate**| Filter payouts scheduled to run on or before the given date. Format is yyyy-MM-dd. | [optional] |
| **scheduleStatus** | **String**| Payout Schedule Status | [optional] [enum: ANY, SCHEDULED, EXECUTED, FAILED] |
| **postInstructFxStatus** | **String**| The status of the post instruct FX step if one was required for the payment | [optional] [enum: ANY, INITIATED, CANCELLED, EXECUTED, COMPLETED, RETURNED, RESUBMITTED, REFUNDED] |
| **page** | **Integer**| Page number. Default is 1. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of results to return in a page | [optional] [default to 25] |
| **sort** | **String**| List of sort fields (e.g. ?sort&#x3D;submittedDateTime:asc,status:asc). Default is sort by submittedDateTime:desc,paymentId:asc The supported sort fields are: sourceAmount, sourceCurrency, paymentAmount, paymentCurrency, routingNumber, accountNumber, remoteId, submittedDateTime, status and paymentId  | [optional] |
| **sensitive** | **Boolean**| Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values.  | [optional] |

### Return type

[**ListPaymentsResponseV4**](ListPaymentsResponseV4.md)

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

