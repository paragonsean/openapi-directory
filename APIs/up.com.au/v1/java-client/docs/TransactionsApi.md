# TransactionsApi

All URIs are relative to *https://api.up.com.au/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**accountsAccountIdTransactionsGet**](TransactionsApi.md#accountsAccountIdTransactionsGet) | **GET** /accounts/{accountId}/transactions | List transactions by account |
| [**transactionsGet**](TransactionsApi.md#transactionsGet) | **GET** /transactions | List transactions |
| [**transactionsIdGet**](TransactionsApi.md#transactionsIdGet) | **GET** /transactions/{id} | Retrieve transaction |


<a id="accountsAccountIdTransactionsGet"></a>
# **accountsAccountIdTransactionsGet**
> ListTransactionsResponse accountsAccountIdTransactionsGet(accountId, pageSize, filterStatus, filterSince, filterUntil, filterCategory, filterTag)

List transactions by account

Retrieve a list of all transactions for a specific account. The returned list is [paginated](#pagination) and can be scrolled by following the &#x60;next&#x60; and &#x60;prev&#x60; links where present. To narrow the results to a specific date range pass one or both of &#x60;filter[since]&#x60; and &#x60;filter[until]&#x60; in the query string. These filter parameters **should not** be used for pagination. Results are ordered newest first to oldest last. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.up.com.au/api/v1");
    
    // Configure HTTP bearer authorization: bearer_auth
    HttpBearerAuth bearer_auth = (HttpBearerAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setBearerToken("BEARER TOKEN");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    String accountId = "b5544658-4bbd-4eb1-8f63-a9909e0f564b"; // String | The unique identifier for the account. 
    Integer pageSize = 30; // Integer | The number of records to return in each page. 
    TransactionStatusEnum filterStatus = TransactionStatusEnum.fromValue("HELD"); // TransactionStatusEnum | The transaction status for which to return records. This can be used to filter `HELD` transactions from those that are `SETTLED`. 
    OffsetDateTime filterSince = OffsetDateTime.parse("2020-01-01T01:02:03+10:00"); // OffsetDateTime | The start date-time from which to return records, formatted according to rfc-3339. Not to be used for pagination purposes. 
    OffsetDateTime filterUntil = OffsetDateTime.parse("2020-02-01T01:02:03+10:00"); // OffsetDateTime | The end date-time up to which to return records, formatted according to rfc-3339. Not to be used for pagination purposes. 
    String filterCategory = "good-life"; // String | The category identifier for which to filter transactions. Both parent and child categories can be filtered through this parameter. Providing an invalid category identifier results in a `404` response. 
    String filterTag = "Holiday"; // String | A transaction tag to filter for which to return records. If the tag does not exist, zero records are returned and a success response is given. 
    try {
      ListTransactionsResponse result = apiInstance.accountsAccountIdTransactionsGet(accountId, pageSize, filterStatus, filterSince, filterUntil, filterCategory, filterTag);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#accountsAccountIdTransactionsGet");
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
| **accountId** | **String**| The unique identifier for the account.  | |
| **pageSize** | **Integer**| The number of records to return in each page.  | [optional] |
| **filterStatus** | [**TransactionStatusEnum**](.md)| The transaction status for which to return records. This can be used to filter &#x60;HELD&#x60; transactions from those that are &#x60;SETTLED&#x60;.  | [optional] [enum: HELD, SETTLED] |
| **filterSince** | **OffsetDateTime**| The start date-time from which to return records, formatted according to rfc-3339. Not to be used for pagination purposes.  | [optional] |
| **filterUntil** | **OffsetDateTime**| The end date-time up to which to return records, formatted according to rfc-3339. Not to be used for pagination purposes.  | [optional] |
| **filterCategory** | **String**| The category identifier for which to filter transactions. Both parent and child categories can be filtered through this parameter. Providing an invalid category identifier results in a &#x60;404&#x60; response.  | [optional] |
| **filterTag** | **String**| A transaction tag to filter for which to return records. If the tag does not exist, zero records are returned and a success response is given.  | [optional] |

### Return type

[**ListTransactionsResponse**](ListTransactionsResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="transactionsGet"></a>
# **transactionsGet**
> ListTransactionsResponse transactionsGet(pageSize, filterStatus, filterSince, filterUntil, filterCategory, filterTag)

List transactions

Retrieve a list of all transactions across all accounts for the currently authenticated user. The returned list is [paginated](#pagination) and can be scrolled by following the &#x60;next&#x60; and &#x60;prev&#x60; links where present. To narrow the results to a specific date range pass one or both of &#x60;filter[since]&#x60; and &#x60;filter[until]&#x60; in the query string. These filter parameters **should not** be used for pagination. Results are ordered newest first to oldest last. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.up.com.au/api/v1");
    
    // Configure HTTP bearer authorization: bearer_auth
    HttpBearerAuth bearer_auth = (HttpBearerAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setBearerToken("BEARER TOKEN");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    Integer pageSize = 30; // Integer | The number of records to return in each page. 
    TransactionStatusEnum filterStatus = TransactionStatusEnum.fromValue("HELD"); // TransactionStatusEnum | The transaction status for which to return records. This can be used to filter `HELD` transactions from those that are `SETTLED`. 
    OffsetDateTime filterSince = OffsetDateTime.parse("2020-01-01T01:02:03+10:00"); // OffsetDateTime | The start date-time from which to return records, formatted according to rfc-3339. Not to be used for pagination purposes. 
    OffsetDateTime filterUntil = OffsetDateTime.parse("2020-02-01T01:02:03+10:00"); // OffsetDateTime | The end date-time up to which to return records, formatted according to rfc-3339. Not to be used for pagination purposes. 
    String filterCategory = "good-life"; // String | The category identifier for which to filter transactions. Both parent and child categories can be filtered through this parameter. Providing an invalid category identifier results in a `404` response. 
    String filterTag = "Holiday"; // String | A transaction tag to filter for which to return records. If the tag does not exist, zero records are returned and a success response is given. 
    try {
      ListTransactionsResponse result = apiInstance.transactionsGet(pageSize, filterStatus, filterSince, filterUntil, filterCategory, filterTag);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#transactionsGet");
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
| **pageSize** | **Integer**| The number of records to return in each page.  | [optional] |
| **filterStatus** | [**TransactionStatusEnum**](.md)| The transaction status for which to return records. This can be used to filter &#x60;HELD&#x60; transactions from those that are &#x60;SETTLED&#x60;.  | [optional] [enum: HELD, SETTLED] |
| **filterSince** | **OffsetDateTime**| The start date-time from which to return records, formatted according to rfc-3339. Not to be used for pagination purposes.  | [optional] |
| **filterUntil** | **OffsetDateTime**| The end date-time up to which to return records, formatted according to rfc-3339. Not to be used for pagination purposes.  | [optional] |
| **filterCategory** | **String**| The category identifier for which to filter transactions. Both parent and child categories can be filtered through this parameter. Providing an invalid category identifier results in a &#x60;404&#x60; response.  | [optional] |
| **filterTag** | **String**| A transaction tag to filter for which to return records. If the tag does not exist, zero records are returned and a success response is given.  | [optional] |

### Return type

[**ListTransactionsResponse**](ListTransactionsResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="transactionsIdGet"></a>
# **transactionsIdGet**
> GetTransactionResponse transactionsIdGet(id)

Retrieve transaction

Retrieve a specific transaction by providing its unique identifier. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.up.com.au/api/v1");
    
    // Configure HTTP bearer authorization: bearer_auth
    HttpBearerAuth bearer_auth = (HttpBearerAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setBearerToken("BEARER TOKEN");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    String id = "7a9d19f9-106c-4e29-8591-52fc5d8f09c5"; // String | The unique identifier for the transaction. 
    try {
      GetTransactionResponse result = apiInstance.transactionsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#transactionsIdGet");
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
| **id** | **String**| The unique identifier for the transaction.  | |

### Return type

[**GetTransactionResponse**](GetTransactionResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

