# TransactionApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelGiftCardTransaction**](TransactionApi.md#cancelGiftCardTransaction) | **POST** /giftcards/{giftCardID}/transactions/{transactionID}/cancellations | Cancel GiftCard Transaction |
| [**createGiftCardTransaction**](TransactionApi.md#createGiftCardTransaction) | **POST** /giftcards/{giftCardID}/transactions | Create GiftCard Transaction |
| [**getGiftCardTransactionbyID**](TransactionApi.md#getGiftCardTransactionbyID) | **GET** /giftcards/{giftCardID}/transactions/{transactionID} | Get GiftCard Transaction by ID |
| [**getGiftCardTransactions**](TransactionApi.md#getGiftCardTransactions) | **GET** /giftcards/{giftCardID}/transactions | Get GiftCard Transactions |
| [**getTransactionAuthorizations**](TransactionApi.md#getTransactionAuthorizations) | **GET** /giftcards/{giftCardID}/transactions/{transactionID}/authorization | Get Transaction Authorizations |
| [**getTransactionCancellations**](TransactionApi.md#getTransactionCancellations) | **GET** /giftcards/{giftCardID}/transactions/{transactionID}/cancellations | Get Transaction Cancellations |
| [**getTransactionSettlements**](TransactionApi.md#getTransactionSettlements) | **GET** /giftcards/{giftCardID}/transactions/{transactionID}/settlements | Get Transaction Settlements |
| [**settleGiftCardTransaction**](TransactionApi.md#settleGiftCardTransaction) | **POST** /giftcards/{giftCardID}/transactions/{transactionID}/settlements | Settle GiftCard Transaction |


<a id="cancelGiftCardTransaction"></a>
# **cancelGiftCardTransaction**
> Response6 cancelGiftCardTransaction(accept, contentType, giftCardID, transactionID, cancelGiftCardTransactionRequest)

Cancel GiftCard Transaction

Creates a cancellation in the transaction. Cancel a item reservation or create a refund.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    TransactionApi apiInstance = new TransactionApi(defaultClient);
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String contentType = "application/json"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
    String giftCardID = "6"; // String | 
    String transactionID = "b476900c"; // String | 
    CancelGiftCardTransactionRequest cancelGiftCardTransactionRequest = new CancelGiftCardTransactionRequest(); // CancelGiftCardTransactionRequest | 
    try {
      Response6 result = apiInstance.cancelGiftCardTransaction(accept, contentType, giftCardID, transactionID, cancelGiftCardTransactionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionApi#cancelGiftCardTransaction");
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
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to application/json] |
| **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to application/json] |
| **giftCardID** | **String**|  | [default to 6] |
| **transactionID** | **String**|  | [default to b476900c] |
| **cancelGiftCardTransactionRequest** | [**CancelGiftCardTransactionRequest**](CancelGiftCardTransactionRequest.md)|  | |

### Return type

[**Response6**](Response6.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="createGiftCardTransaction"></a>
# **createGiftCardTransaction**
> Response3 createGiftCardTransaction(accept, contentType, giftCardID, createGiftCardTransactionRequest)

Create GiftCard Transaction

Register a new giftcard transaction and authorize the item reservation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    TransactionApi apiInstance = new TransactionApi(defaultClient);
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String contentType = "application/json"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
    String giftCardID = "7"; // String | 
    CreateGiftCardTransactionRequest createGiftCardTransactionRequest = new CreateGiftCardTransactionRequest(); // CreateGiftCardTransactionRequest | 
    try {
      Response3 result = apiInstance.createGiftCardTransaction(accept, contentType, giftCardID, createGiftCardTransactionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionApi#createGiftCardTransaction");
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
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to application/json] |
| **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to application/json] |
| **giftCardID** | **String**|  | [default to 7] |
| **createGiftCardTransactionRequest** | [**CreateGiftCardTransactionRequest**](CreateGiftCardTransactionRequest.md)|  | [optional] |

### Return type

[**Response3**](Response3.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getGiftCardTransactionbyID"></a>
# **getGiftCardTransactionbyID**
> Response5 getGiftCardTransactionbyID(accept, contentType, giftCardID, transactionID)

Get GiftCard Transaction by ID



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    TransactionApi apiInstance = new TransactionApi(defaultClient);
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String contentType = "application/json"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
    String giftCardID = "6"; // String | 
    String transactionID = "b47690"; // String | 
    try {
      Response5 result = apiInstance.getGiftCardTransactionbyID(accept, contentType, giftCardID, transactionID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionApi#getGiftCardTransactionbyID");
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
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to application/json] |
| **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to application/json] |
| **giftCardID** | **String**|  | [default to 6] |
| **transactionID** | **String**|  | [default to b47690] |

### Return type

[**Response5**](Response5.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getGiftCardTransactions"></a>
# **getGiftCardTransactions**
> List&lt;Response3&gt; getGiftCardTransactions(accept, contentType, giftCardID)

Get GiftCard Transactions

Returns all transaction of a giftcard.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    TransactionApi apiInstance = new TransactionApi(defaultClient);
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String contentType = "application/json"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
    String giftCardID = "2"; // String | 
    try {
      List<Response3> result = apiInstance.getGiftCardTransactions(accept, contentType, giftCardID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionApi#getGiftCardTransactions");
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
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to application/json] |
| **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to application/json] |
| **giftCardID** | **String**|  | [default to 2] |

### Return type

[**List&lt;Response3&gt;**](Response3.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getTransactionAuthorizations"></a>
# **getTransactionAuthorizations**
> Response6 getTransactionAuthorizations(accept, contentType, giftCardID, transactionID)

Get Transaction Authorizations

Returns the giftcard transaction authorizations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    TransactionApi apiInstance = new TransactionApi(defaultClient);
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String contentType = "application/json"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
    String giftCardID = "6"; // String | 
    String transactionID = "b47690"; // String | 
    try {
      Response6 result = apiInstance.getTransactionAuthorizations(accept, contentType, giftCardID, transactionID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionApi#getTransactionAuthorizations");
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
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to application/json] |
| **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to application/json] |
| **giftCardID** | **String**|  | [default to 6] |
| **transactionID** | **String**|  | [default to b47690] |

### Return type

[**Response6**](Response6.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getTransactionCancellations"></a>
# **getTransactionCancellations**
> List&lt;Response7&gt; getTransactionCancellations(accept, contentType, giftCardID, transactionID)

Get Transaction Cancellations

Returns the giftcard transaction cancellations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    TransactionApi apiInstance = new TransactionApi(defaultClient);
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String contentType = "application/json"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
    String giftCardID = "6"; // String | 
    String transactionID = "b47690"; // String | 
    try {
      List<Response7> result = apiInstance.getTransactionCancellations(accept, contentType, giftCardID, transactionID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionApi#getTransactionCancellations");
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
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to application/json] |
| **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to application/json] |
| **giftCardID** | **String**|  | [default to 6] |
| **transactionID** | **String**|  | [default to b47690] |

### Return type

[**List&lt;Response7&gt;**](Response7.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getTransactionSettlements"></a>
# **getTransactionSettlements**
> List&lt;Response6&gt; getTransactionSettlements(accept, contentType, giftCardID, transactionID)

Get Transaction Settlements

Returns the giftcard transaction settlements.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    TransactionApi apiInstance = new TransactionApi(defaultClient);
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String contentType = "application/json"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
    String giftCardID = "7"; // String | 
    String transactionID = "b47690"; // String | 
    try {
      List<Response6> result = apiInstance.getTransactionSettlements(accept, contentType, giftCardID, transactionID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionApi#getTransactionSettlements");
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
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to application/json] |
| **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to application/json] |
| **giftCardID** | **String**|  | [default to 7] |
| **transactionID** | **String**|  | [default to b47690] |

### Return type

[**List&lt;Response6&gt;**](Response6.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="settleGiftCardTransaction"></a>
# **settleGiftCardTransaction**
> Response6 settleGiftCardTransaction(accept, contentType, giftCardID, transactionID, settleGiftCardTransactionRequest)

Settle GiftCard Transaction

Creates a giftcard transaction settlement.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    TransactionApi apiInstance = new TransactionApi(defaultClient);
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String contentType = "application/json"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
    String giftCardID = "6"; // String | 
    String transactionID = "b47690"; // String | 
    SettleGiftCardTransactionRequest settleGiftCardTransactionRequest = new SettleGiftCardTransactionRequest(); // SettleGiftCardTransactionRequest | 
    try {
      Response6 result = apiInstance.settleGiftCardTransaction(accept, contentType, giftCardID, transactionID, settleGiftCardTransactionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionApi#settleGiftCardTransaction");
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
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to application/json] |
| **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to application/json] |
| **giftCardID** | **String**|  | [default to 6] |
| **transactionID** | **String**|  | [default to b47690] |
| **settleGiftCardTransactionRequest** | [**SettleGiftCardTransactionRequest**](SettleGiftCardTransactionRequest.md)|  | |

### Return type

[**Response6**](Response6.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

