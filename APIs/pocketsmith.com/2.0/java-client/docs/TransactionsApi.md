# TransactionsApi

All URIs are relative to *https://api.pocketsmith.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**accountsIdTransactionsGet**](TransactionsApi.md#accountsIdTransactionsGet) | **GET** /accounts/{id}/transactions | List transactions in account |
| [**categoriesIdTransactionsGet**](TransactionsApi.md#categoriesIdTransactionsGet) | **GET** /categories/{id}/transactions | List transactions in categories |
| [**transactionAccountsIdTransactionsGet**](TransactionsApi.md#transactionAccountsIdTransactionsGet) | **GET** /transaction_accounts/{id}/transactions | List transactions in transaction account |
| [**transactionAccountsIdTransactionsPost**](TransactionsApi.md#transactionAccountsIdTransactionsPost) | **POST** /transaction_accounts/{id}/transactions | Create a transaction in transaction account |
| [**transactionsIdDelete**](TransactionsApi.md#transactionsIdDelete) | **DELETE** /transactions/{id} | Delete transaction |
| [**transactionsIdGet**](TransactionsApi.md#transactionsIdGet) | **GET** /transactions/{id} | Get a transaction |
| [**transactionsIdPut**](TransactionsApi.md#transactionsIdPut) | **PUT** /transactions/{id} | Update a transaction |
| [**usersIdTransactionsGet**](TransactionsApi.md#usersIdTransactionsGet) | **GET** /users/{id}/transactions | List transactions in user |


<a id="accountsIdTransactionsGet"></a>
# **accountsIdTransactionsGet**
> List&lt;Transaction&gt; accountsIdTransactionsGet(id, startDate, endDate, updatedSince, uncategorised, type, needsReview, search, page)

List transactions in account

Lists transactions belonging to an account by its ID.

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
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    Integer id = 42; // Integer | The unique identifier of the account.
    String startDate = "2016-11-01"; // String | Limit to transactions on or after this date. Required if end_date is provided. If not provided, defaults to the furtherest date allowed by the user's subscription.
    String endDate = "2016-11-30"; // String | Limit to transactions on or before this date. Required if start_date is provided. If not provided, defaults to today's date.
    String updatedSince = "2020-10-14T09:20:33+13:00"; // String | Limit to transactions updated since an ISO 8601 timestamp.
    Integer uncategorised = 1; // Integer | Limit to uncategorised transactions.
    String type = "debit"; // String | Limit to transactions of this type.
    Integer needsReview = 1; // Integer | Limit to transactions that need to be reviewed.
    String search = "Paypal"; // String | Limit to transactions matching a keyword search string. The provided string is matched against the transaction amount, account name, payee, category title, note, labels, and the date in ISO 8601 format.
    Integer page = 3; // Integer | Choose a particular page of the results.
    try {
      List<Transaction> result = apiInstance.accountsIdTransactionsGet(id, startDate, endDate, updatedSince, uncategorised, type, needsReview, search, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#accountsIdTransactionsGet");
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
| **id** | **Integer**| The unique identifier of the account. | |
| **startDate** | **String**| Limit to transactions on or after this date. Required if end_date is provided. If not provided, defaults to the furtherest date allowed by the user&#39;s subscription. | [optional] |
| **endDate** | **String**| Limit to transactions on or before this date. Required if start_date is provided. If not provided, defaults to today&#39;s date. | [optional] |
| **updatedSince** | **String**| Limit to transactions updated since an ISO 8601 timestamp. | [optional] |
| **uncategorised** | **Integer**| Limit to uncategorised transactions. | [optional] |
| **type** | **String**| Limit to transactions of this type. | [optional] [enum: debit, credit] |
| **needsReview** | **Integer**| Limit to transactions that need to be reviewed. | [optional] |
| **search** | **String**| Limit to transactions matching a keyword search string. The provided string is matched against the transaction amount, account name, payee, category title, note, labels, and the date in ISO 8601 format. | [optional] |
| **page** | **Integer**| Choose a particular page of the results. | [optional] |

### Return type

[**List&lt;Transaction&gt;**](Transaction.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **403** | Not Allowed |  -  |
| **404** | Not Found |  -  |

<a id="categoriesIdTransactionsGet"></a>
# **categoriesIdTransactionsGet**
> List&lt;Transaction&gt; categoriesIdTransactionsGet(id, startDate, endDate, updatedSince, uncategorised, type, needsReview, search, page)

List transactions in categories

Lists transactions belonging to one or more categories by their IDs.

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
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    String id = "42,43"; // String | A comma-separated list of category IDs.
    String startDate = "2016-11-01"; // String | Limit to transactions on or after this date. Required if end_date is provided. If not provided, defaults to the furtherest date allowed by the user's subscription.
    String endDate = "2016-11-30"; // String | Limit to transactions on or before this date. Required if start_date is provided. If not provided, defaults to today's date.
    String updatedSince = "2020-10-14T09:20:33+13:00"; // String | Limit to transactions updated since an ISO 8601 timestamp.
    Integer uncategorised = 1; // Integer | Limit to uncategorised transactions.
    String type = "debit"; // String | Limit to transactions of this type.
    Integer needsReview = 1; // Integer | Limit to transactions that need to be reviewed.
    String search = "Paypal"; // String | Limit to transactions matching a keyword search string. The provided string is matched against the transaction amount, account name, payee, category title, note, labels, and the date in ISO 8601 format.
    Integer page = 3; // Integer | Choose a particular page of the results.
    try {
      List<Transaction> result = apiInstance.categoriesIdTransactionsGet(id, startDate, endDate, updatedSince, uncategorised, type, needsReview, search, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#categoriesIdTransactionsGet");
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
| **id** | **String**| A comma-separated list of category IDs. | |
| **startDate** | **String**| Limit to transactions on or after this date. Required if end_date is provided. If not provided, defaults to the furtherest date allowed by the user&#39;s subscription. | [optional] |
| **endDate** | **String**| Limit to transactions on or before this date. Required if start_date is provided. If not provided, defaults to today&#39;s date. | [optional] |
| **updatedSince** | **String**| Limit to transactions updated since an ISO 8601 timestamp. | [optional] |
| **uncategorised** | **Integer**| Limit to uncategorised transactions. | [optional] |
| **type** | **String**| Limit to transactions of this type. | [optional] [enum: debit, credit] |
| **needsReview** | **Integer**| Limit to transactions that need to be reviewed. | [optional] |
| **search** | **String**| Limit to transactions matching a keyword search string. The provided string is matched against the transaction amount, account name, payee, category title, note, labels, and the date in ISO 8601 format. | [optional] |
| **page** | **Integer**| Choose a particular page of the results. | [optional] |

### Return type

[**List&lt;Transaction&gt;**](Transaction.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **403** | Not Allowed |  -  |
| **404** | Not Found |  -  |

<a id="transactionAccountsIdTransactionsGet"></a>
# **transactionAccountsIdTransactionsGet**
> List&lt;Transaction&gt; transactionAccountsIdTransactionsGet(id, startDate, endDate, updatedSince, uncategorised, type, needsReview, search, page)

List transactions in transaction account

Lists transactions belonging to a transaction account by its ID.

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
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    Integer id = 42; // Integer | The unique identifier of the transaction account.
    String startDate = "2016-11-01"; // String | Limit to transactions on or after this date. Required if end_date is provided. If not provided, defaults to the furtherest date allowed by the user's subscription.
    String endDate = "2016-11-30"; // String | Limit to transactions on or before this date. Required if start_date is provided. If not provided, defaults to today's date.
    String updatedSince = "2020-10-14T09:20:33+13:00"; // String | Limit to transactions updated since an ISO 8601 timestamp.
    Integer uncategorised = 1; // Integer | Limit to uncategorised transactions.
    String type = "debit"; // String | Limit to transactions of this type.
    Integer needsReview = 1; // Integer | Limit to transactions that need to be reviewed.
    String search = "Paypal"; // String | Limit to transactions matching a keyword search string. The provided string is matched against the transaction amount, account name, payee, category title, note, labels, and the date in ISO 8601 format.
    Integer page = 3; // Integer | Choose a particular page of the results.
    try {
      List<Transaction> result = apiInstance.transactionAccountsIdTransactionsGet(id, startDate, endDate, updatedSince, uncategorised, type, needsReview, search, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#transactionAccountsIdTransactionsGet");
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
| **startDate** | **String**| Limit to transactions on or after this date. Required if end_date is provided. If not provided, defaults to the furtherest date allowed by the user&#39;s subscription. | [optional] |
| **endDate** | **String**| Limit to transactions on or before this date. Required if start_date is provided. If not provided, defaults to today&#39;s date. | [optional] |
| **updatedSince** | **String**| Limit to transactions updated since an ISO 8601 timestamp. | [optional] |
| **uncategorised** | **Integer**| Limit to uncategorised transactions. | [optional] |
| **type** | **String**| Limit to transactions of this type. | [optional] [enum: debit, credit] |
| **needsReview** | **Integer**| Limit to transactions that need to be reviewed. | [optional] |
| **search** | **String**| Limit to transactions matching a keyword search string. The provided string is matched against the transaction amount, account name, payee, category title, note, labels, and the date in ISO 8601 format. | [optional] |
| **page** | **Integer**| Choose a particular page of the results. | [optional] |

### Return type

[**List&lt;Transaction&gt;**](Transaction.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **403** | Not Allowed |  -  |
| **404** | Not Found |  -  |

<a id="transactionAccountsIdTransactionsPost"></a>
# **transactionAccountsIdTransactionsPost**
> Transaction transactionAccountsIdTransactionsPost(id, transactionAccountsIdTransactionsPostRequest)

Create a transaction in transaction account

Creates a transaction in a transaction account by its ID.

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
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    Integer id = 42; // Integer | The unique identifier of the transaction account.
    TransactionAccountsIdTransactionsPostRequest transactionAccountsIdTransactionsPostRequest = new TransactionAccountsIdTransactionsPostRequest(); // TransactionAccountsIdTransactionsPostRequest | 
    try {
      Transaction result = apiInstance.transactionAccountsIdTransactionsPost(id, transactionAccountsIdTransactionsPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#transactionAccountsIdTransactionsPost");
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
| **transactionAccountsIdTransactionsPostRequest** | [**TransactionAccountsIdTransactionsPostRequest**](TransactionAccountsIdTransactionsPostRequest.md)|  | [optional] |

### Return type

[**Transaction**](Transaction.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **403** | Not Allowed |  -  |
| **404** | Not Found |  -  |
| **422** | Validation Error |  -  |

<a id="transactionsIdDelete"></a>
# **transactionsIdDelete**
> transactionsIdDelete(id)

Delete transaction

Deletes a transaction and all its data by ID.

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
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    Integer id = 42; // Integer | The unique identifier of the transaction.
    try {
      apiInstance.transactionsIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#transactionsIdDelete");
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
| **id** | **Integer**| The unique identifier of the transaction. | |

### Return type

null (empty response body)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **403** | Not Allowed |  -  |
| **404** | Not Found |  -  |

<a id="transactionsIdGet"></a>
# **transactionsIdGet**
> Transaction transactionsIdGet(id)

Get a transaction

Gets a transaction by its ID.

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
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    Integer id = 42; // Integer | The unique identifier of the transaction.
    try {
      Transaction result = apiInstance.transactionsIdGet(id);
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
| **id** | **Integer**| The unique identifier of the transaction. | |

### Return type

[**Transaction**](Transaction.md)

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

<a id="transactionsIdPut"></a>
# **transactionsIdPut**
> Transaction transactionsIdPut(id, transactionsIdPutRequest)

Update a transaction

Updates a transaction by its ID.

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
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    Integer id = 42; // Integer | The unique identifier of the transaction.
    TransactionsIdPutRequest transactionsIdPutRequest = new TransactionsIdPutRequest(); // TransactionsIdPutRequest | 
    try {
      Transaction result = apiInstance.transactionsIdPut(id, transactionsIdPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#transactionsIdPut");
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
| **id** | **Integer**| The unique identifier of the transaction. | |
| **transactionsIdPutRequest** | [**TransactionsIdPutRequest**](TransactionsIdPutRequest.md)|  | [optional] |

### Return type

[**Transaction**](Transaction.md)

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

<a id="usersIdTransactionsGet"></a>
# **usersIdTransactionsGet**
> List&lt;Transaction&gt; usersIdTransactionsGet(id, startDate, endDate, updatedSince, uncategorised, type, needsReview, search, page)

List transactions in user

Lists transactions belonging to a user by their ID.

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
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    Integer id = 42; // Integer | The unique identifier of the account.
    String startDate = "2016-11-01"; // String | Limit to transactions on or after this date. Required if end_date is provided. If not provided, defaults to the furtherest date allowed by the user's subscription.
    String endDate = "2016-11-30"; // String | Limit to transactions on or before this date. Required if start_date is provided. If not provided, defaults to today's date.
    String updatedSince = "2020-10-14T09:20:33+13:00"; // String | Limit to transactions updated since an ISO 8601 timestamp.
    Integer uncategorised = 1; // Integer | Limit to uncategorised transactions.
    String type = "debit"; // String | Limit to transactions of this type.
    Integer needsReview = 1; // Integer | Limit to transactions that need to be reviewed.
    String search = "Paypal"; // String | Limit to transactions matching a keyword search string. The provided string is matched against the transaction amount, account name, payee, category title, note, labels, and the date in ISO 8601 format.
    Integer page = 3; // Integer | Choose a particular page of the results.
    try {
      List<Transaction> result = apiInstance.usersIdTransactionsGet(id, startDate, endDate, updatedSince, uncategorised, type, needsReview, search, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#usersIdTransactionsGet");
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
| **id** | **Integer**| The unique identifier of the account. | |
| **startDate** | **String**| Limit to transactions on or after this date. Required if end_date is provided. If not provided, defaults to the furtherest date allowed by the user&#39;s subscription. | [optional] |
| **endDate** | **String**| Limit to transactions on or before this date. Required if start_date is provided. If not provided, defaults to today&#39;s date. | [optional] |
| **updatedSince** | **String**| Limit to transactions updated since an ISO 8601 timestamp. | [optional] |
| **uncategorised** | **Integer**| Limit to uncategorised transactions. | [optional] |
| **type** | **String**| Limit to transactions of this type. | [optional] [enum: debit, credit] |
| **needsReview** | **Integer**| Limit to transactions that need to be reviewed. | [optional] |
| **search** | **String**| Limit to transactions matching a keyword search string. The provided string is matched against the transaction amount, account name, payee, category title, note, labels, and the date in ISO 8601 format. | [optional] |
| **page** | **Integer**| Choose a particular page of the results. | [optional] |

### Return type

[**List&lt;Transaction&gt;**](Transaction.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **403** | Not Allowed |  -  |
| **404** | Not Found |  -  |

