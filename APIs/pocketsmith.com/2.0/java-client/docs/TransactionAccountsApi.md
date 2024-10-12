# TransactionAccountsApi

All URIs are relative to *https://api.pocketsmith.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**transactionAccountsIdGet**](TransactionAccountsApi.md#transactionAccountsIdGet) | **GET** /transaction_accounts/{id} | Get transaction account |
| [**transactionAccountsIdPut**](TransactionAccountsApi.md#transactionAccountsIdPut) | **PUT** /transaction_accounts/{id} | Update transaction account |
| [**usersIdTransactionAccountsGet**](TransactionAccountsApi.md#usersIdTransactionAccountsGet) | **GET** /users/{id}/transaction_accounts | List transaction accounts in user |


<a id="transactionAccountsIdGet"></a>
# **transactionAccountsIdGet**
> TransactionAccount transactionAccountsIdGet(id)

Get transaction account

Gets a transaction account by its ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    TransactionAccountsApi apiInstance = new TransactionAccountsApi(defaultClient);
    Integer id = 42; // Integer | The unique identifier of the transaction account.
    try {
      TransactionAccount result = apiInstance.transactionAccountsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionAccountsApi#transactionAccountsIdGet");
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
| **id** | **Integer**| The unique identifier of the transaction account. | |

### Return type

[**TransactionAccount**](TransactionAccount.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | Not Allowed |  -  |
| **404** | Not Found |  -  |

<a id="transactionAccountsIdPut"></a>
# **transactionAccountsIdPut**
> TransactionAccount transactionAccountsIdPut(id, transactionAccountsIdPutRequest)

Update transaction account

Updates the transaction account by its ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    TransactionAccountsApi apiInstance = new TransactionAccountsApi(defaultClient);
    Integer id = 42; // Integer | The unique identifier of the transaction account.
    TransactionAccountsIdPutRequest transactionAccountsIdPutRequest = new TransactionAccountsIdPutRequest(); // TransactionAccountsIdPutRequest | 
    try {
      TransactionAccount result = apiInstance.transactionAccountsIdPut(id, transactionAccountsIdPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionAccountsApi#transactionAccountsIdPut");
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
| **id** | **Integer**| The unique identifier of the transaction account. | |
| **transactionAccountsIdPutRequest** | [**TransactionAccountsIdPutRequest**](TransactionAccountsIdPutRequest.md)|  | [optional] |

### Return type

[**TransactionAccount**](TransactionAccount.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | Not Allowed |  -  |
| **404** | Not Found |  -  |
| **422** | Validation Error |  -  |

<a id="usersIdTransactionAccountsGet"></a>
# **usersIdTransactionAccountsGet**
> List&lt;TransactionAccount&gt; usersIdTransactionAccountsGet(id)

List transaction accounts in user

List all transaction accounts belonging to a user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    TransactionAccountsApi apiInstance = new TransactionAccountsApi(defaultClient);
    Integer id = 42; // Integer | The unique identifier of the user.
    try {
      List<TransactionAccount> result = apiInstance.usersIdTransactionAccountsGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionAccountsApi#usersIdTransactionAccountsGet");
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
| **id** | **Integer**| The unique identifier of the user. | |

### Return type

[**List&lt;TransactionAccount&gt;**](TransactionAccount.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | Not Allowed |  -  |
| **404** | Not Found |  -  |

