# TransactionsApi

All URIs are relative to *https://api.nextauth.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createTransaction**](TransactionsApi.md#createTransaction) | **POST** /servers/{serverid}/sessions/transactions | Create a transaction to be approved within the current session. |
| [**getTransactionResult**](TransactionsApi.md#getTransactionResult) | **GET** /servers/{serverid}/transactions/{transactionid} | Get transaction result for a given transaction. |


<a id="createTransaction"></a>
# **createTransaction**
> TransactionId createTransaction(serverid, xNonce, msg)

Create a transaction to be approved within the current session.

Create a transaction for approval within the current session. Required permission: &#39;sessions&#39;.

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
    defaultClient.setBasePath("https://api.nextauth.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: role_id
    ApiKeyAuth role_id = (ApiKeyAuth) defaultClient.getAuthentication("role_id");
    role_id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //role_id.setApiKeyPrefix("Token");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    String serverid = "serverid_example"; // String | Base64 encoded server id
    String xNonce = "xNonce_example"; // String | Nonce to identify the browser/webserver session
    Transaction msg = new Transaction(); // Transaction | 
    try {
      TransactionId result = apiInstance.createTransaction(serverid, xNonce, msg);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#createTransaction");
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
| **serverid** | **String**| Base64 encoded server id | |
| **xNonce** | **String**| Nonce to identify the browser/webserver session | |
| **msg** | [**Transaction**](Transaction.md)|  | |

### Return type

[**TransactionId**](TransactionId.md)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ok |  -  |
| **403** | no account associated with this session |  -  |

<a id="getTransactionResult"></a>
# **getTransactionResult**
> TransactionResult getTransactionResult(serverid, transactionid)

Get transaction result for a given transaction.

Get transaction result for a given transaction id. Required permission: &#39;sessions&#39;.

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
    defaultClient.setBasePath("https://api.nextauth.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: role_id
    ApiKeyAuth role_id = (ApiKeyAuth) defaultClient.getAuthentication("role_id");
    role_id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //role_id.setApiKeyPrefix("Token");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    String serverid = "serverid_example"; // String | Base64 encoded server id
    String transactionid = "transactionid_example"; // String | Base64 encoded transaction id
    try {
      TransactionResult result = apiInstance.getTransactionResult(serverid, transactionid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#getTransactionResult");
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
| **serverid** | **String**| Base64 encoded server id | |
| **transactionid** | **String**| Base64 encoded transaction id | |

### Return type

[**TransactionResult**](TransactionResult.md)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ok |  -  |
| **404** | no transaction with given id found |  -  |

