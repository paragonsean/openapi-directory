# TransactionsFindPaymentsAndRefundsApi

All URIs are relative to *https://market.openchannel.io/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**transactionsGet**](TransactionsFindPaymentsAndRefundsApi.md#transactionsGet) | **GET** /transactions | Returns a paginated list of transactions |
| [**transactionsTransactionIdDelete**](TransactionsFindPaymentsAndRefundsApi.md#transactionsTransactionIdDelete) | **DELETE** /transactions/{transactionId} | Deleted a transaction |
| [**transactionsTransactionIdGet**](TransactionsFindPaymentsAndRefundsApi.md#transactionsTransactionIdGet) | **GET** /transactions/{transactionId} | Returns a transaction |
| [**transactionsTransactionIdPost**](TransactionsFindPaymentsAndRefundsApi.md#transactionsTransactionIdPost) | **POST** /transactions/{transactionId} | Updates a transaction |


<a id="transactionsGet"></a>
# **transactionsGet**
> TransactionPages transactionsGet(query, sort, pageNumber, limit)

Returns a paginated list of transactions

- Results are paginated and the default is value is 100 if no limit is provided 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsFindPaymentsAndRefundsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TransactionsFindPaymentsAndRefundsApi apiInstance = new TransactionsFindPaymentsAndRefundsApi(defaultClient);
    String query = "query_example"; // String | A query document. Example: {'userId':'1'} matches all the transactions that have the userId '1'.
    String sort = "sort_example"; // String | A sort document. Example: {'date':1} sorts the results by total in ascending order
    Integer pageNumber = 56; // Integer | The result set page number to be returned
    Integer limit = 56; // Integer | The maximum number of results to return per page
    try {
      TransactionPages result = apiInstance.transactionsGet(query, sort, pageNumber, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsFindPaymentsAndRefundsApi#transactionsGet");
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
| **query** | **String**| A query document. Example: {&#39;userId&#39;:&#39;1&#39;} matches all the transactions that have the userId &#39;1&#39;. | [optional] |
| **sort** | **String**| A sort document. Example: {&#39;date&#39;:1} sorts the results by total in ascending order | [optional] |
| **pageNumber** | **Integer**| The result set page number to be returned | [optional] |
| **limit** | **Integer**| The maximum number of results to return per page | [optional] |

### Return type

[**TransactionPages**](TransactionPages.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **0** | OK |  -  |

<a id="transactionsTransactionIdDelete"></a>
# **transactionsTransactionIdDelete**
> transactionsTransactionIdDelete(transactionId)

Deleted a transaction

- Results are returned for the market provided within the basic authentication credentials 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsFindPaymentsAndRefundsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TransactionsFindPaymentsAndRefundsApi apiInstance = new TransactionsFindPaymentsAndRefundsApi(defaultClient);
    String transactionId = "transactionId_example"; // String | The id of the transaction to be deleted
    try {
      apiInstance.transactionsTransactionIdDelete(transactionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsFindPaymentsAndRefundsApi#transactionsTransactionIdDelete");
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
| **transactionId** | **String**| The id of the transaction to be deleted | |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |

<a id="transactionsTransactionIdGet"></a>
# **transactionsTransactionIdGet**
> transactionsTransactionIdGet(transactionId)

Returns a transaction

- Results are returned for the market provided within the basic authentication credentials 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsFindPaymentsAndRefundsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TransactionsFindPaymentsAndRefundsApi apiInstance = new TransactionsFindPaymentsAndRefundsApi(defaultClient);
    String transactionId = "transactionId_example"; // String | The id of the transaction to return
    try {
      apiInstance.transactionsTransactionIdGet(transactionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsFindPaymentsAndRefundsApi#transactionsTransactionIdGet");
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
| **transactionId** | **String**| The id of the transaction to return | |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |

<a id="transactionsTransactionIdPost"></a>
# **transactionsTransactionIdPost**
> Transaction transactionsTransactionIdPost(transactionId, customData)

Updates a transaction

- Results are returned for the market provided within the basic authentication credentials 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsFindPaymentsAndRefundsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TransactionsFindPaymentsAndRefundsApi apiInstance = new TransactionsFindPaymentsAndRefundsApi(defaultClient);
    String transactionId = "transactionId_example"; // String | The id of the transaction to be updated
    String customData = "customData_example"; // String | A custom JSON object that you can create and attach to this record
    try {
      Transaction result = apiInstance.transactionsTransactionIdPost(transactionId, customData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsFindPaymentsAndRefundsApi#transactionsTransactionIdPost");
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
| **transactionId** | **String**| The id of the transaction to be updated | |
| **customData** | **String**| A custom JSON object that you can create and attach to this record | [optional] |

### Return type

[**Transaction**](Transaction.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **0** | OK |  -  |

