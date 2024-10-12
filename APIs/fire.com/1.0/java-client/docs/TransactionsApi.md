# TransactionsApi

All URIs are relative to *https://api.fire.com/business*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getTransactionsByAccountIdFiltered**](TransactionsApi.md#getTransactionsByAccountIdFiltered) | **GET** /v1/accounts/{ican}/transactions/filter | Filtered list of transactions for an account (v1) |
| [**getTransactionsByAccountIdv1**](TransactionsApi.md#getTransactionsByAccountIdv1) | **GET** /v1/accounts/{ican}/transactions | List transactions for an account (v1) |
| [**getTransactionsByAccountIdv3**](TransactionsApi.md#getTransactionsByAccountIdv3) | **GET** /v3/accounts/{ican}/transactions | List transactions for an account (v3) |


<a id="getTransactionsByAccountIdFiltered"></a>
# **getTransactionsByAccountIdFiltered**
> CardTransactionsv1 getTransactionsByAccountIdFiltered(ican, dateRangeFrom, dateRangeTo, searchKeyword, transactionTypes, offset)

Filtered list of transactions for an account (v1)

Retrieve a filtered list of transactions against an account. Recommended to use the v3 endpoint instead. * &#x60;dateRangeFrom&#x60; - A millisecond epoch time specifying the date range start date. * &#x60;dateRangeTo&#x60; - A millisecond epoch time specifying the date range end date. * &#x60;searchKeyword&#x60; - Search term to filter by from the reference field (&#x60;myRef&#x60;). * &#x60;transactionTypes&#x60; - One or more of the transaction types above. This field can be repeated multiple times to allow for multiple transaction types. * &#x60;offset&#x60; - The page offset. Defaults to 0. This is the record number that the returned list will start at. E.g. offset &#x3D; 40 and limit &#x3D; 20 will return records 40 to 59. 

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
    defaultClient.setBasePath("https://api.fire.com/business");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    Long ican = 56L; // Long | 
    Long dateRangeFrom = 56L; // Long | 
    Long dateRangeTo = 56L; // Long | 
    String searchKeyword = "searchKeyword_example"; // String | 
    List<String> transactionTypes = Arrays.asList(); // List<String> | 
    Long offset = 56L; // Long | 
    try {
      CardTransactionsv1 result = apiInstance.getTransactionsByAccountIdFiltered(ican, dateRangeFrom, dateRangeTo, searchKeyword, transactionTypes, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#getTransactionsByAccountIdFiltered");
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
| **ican** | **Long**|  | |
| **dateRangeFrom** | **Long**|  | |
| **dateRangeTo** | **Long**|  | |
| **searchKeyword** | **String**|  | |
| **transactionTypes** | [**List&lt;String&gt;**](String.md)|  | |
| **offset** | **Long**|  | |

### Return type

[**CardTransactionsv1**](CardTransactionsv1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of transaction objects for the account with a count (&#x60;total&#x60;) filtered by the specified query parameter. |  -  |

<a id="getTransactionsByAccountIdv1"></a>
# **getTransactionsByAccountIdv1**
> CardTransactionsv1 getTransactionsByAccountIdv1(ican, limit, offset)

List transactions for an account (v1)

Retrieve a list of transactions against an account. Recommended to use the v3 endpoint instead.

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
    defaultClient.setBasePath("https://api.fire.com/business");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    Long ican = 56L; // Long | 
    Long limit = 56L; // Long | 
    Long offset = 56L; // Long | 
    try {
      CardTransactionsv1 result = apiInstance.getTransactionsByAccountIdv1(ican, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#getTransactionsByAccountIdv1");
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
| **ican** | **Long**|  | |
| **limit** | **Long**|  | |
| **offset** | **Long**|  | |

### Return type

[**CardTransactionsv1**](CardTransactionsv1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of transaction objects for the account with a count (&#x60;total&#x60;). |  -  |

<a id="getTransactionsByAccountIdv3"></a>
# **getTransactionsByAccountIdv3**
> CardTransactionsv3 getTransactionsByAccountIdv3(ican, limit, dateRangeFrom, dateRangeTo, startAfter)

List transactions for an account (v3)

Retrieve a list of transactions against an account. Initially, use the optional &#x60;limit&#x60;, &#x60;dateRangeFrom&#x60; and &#x60;dateRangeTo&#x60; query params to limit your query, then use the embedded &#x60;next&#x60; or &#x60;prev&#x60; links in the response to get newer or older pages. 

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
    defaultClient.setBasePath("https://api.fire.com/business");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    Long ican = 56L; // Long | 
    Long limit = 56L; // Long | 
    Long dateRangeFrom = 56L; // Long | 
    Long dateRangeTo = 56L; // Long | 
    String startAfter = "startAfter_example"; // String | 
    try {
      CardTransactionsv3 result = apiInstance.getTransactionsByAccountIdv3(ican, limit, dateRangeFrom, dateRangeTo, startAfter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#getTransactionsByAccountIdv3");
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
| **ican** | **Long**|  | |
| **limit** | **Long**|  | [optional] |
| **dateRangeFrom** | **Long**|  | [optional] |
| **dateRangeTo** | **Long**|  | [optional] |
| **startAfter** | **String**|  | [optional] |

### Return type

[**CardTransactionsv3**](CardTransactionsv3.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of transaction objects for the account with a count (&#x60;total&#x60;). |  -  |

