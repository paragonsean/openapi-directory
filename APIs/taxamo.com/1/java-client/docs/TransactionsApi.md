# TransactionsApi

All URIs are relative to *https://api.taxamo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelTransaction**](TransactionsApi.md#cancelTransaction) | **DELETE** /api/v1/transactions/{key} | Delete transaction |
| [**confirmTransaction**](TransactionsApi.md#confirmTransaction) | **POST** /api/v1/transactions/{key}/confirm | Confirm transaction |
| [**createTransaction**](TransactionsApi.md#createTransaction) | **POST** /api/v1/transactions | Store transaction |
| [**getTransaction**](TransactionsApi.md#getTransaction) | **GET** /api/v1/transactions/{key} | Retrieve transaction data. |
| [**listTransactions**](TransactionsApi.md#listTransactions) | **GET** /api/v1/transactions | Browse transactions |
| [**unconfirmTransaction**](TransactionsApi.md#unconfirmTransaction) | **POST** /api/v1/transactions/{key}/unconfirm | Un-confirm the transaction |
| [**updateTransaction**](TransactionsApi.md#updateTransaction) | **PUT** /api/v1/transactions/{key} | Update transaction |


<a id="cancelTransaction"></a>
# **cancelTransaction**
> CancelTransactionOut cancelTransaction(key)

Delete transaction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taxamo.com");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    String key = "key_example"; // String | Transaction key
    try {
      CancelTransactionOut result = apiInstance.cancelTransaction(key);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#cancelTransaction");
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
| **key** | **String**| Transaction key | |

### Return type

[**CancelTransactionOut**](CancelTransactionOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Validation failed, see JSON body response for details. |  -  |
| **401** | Incorrect token |  -  |

<a id="confirmTransaction"></a>
# **confirmTransaction**
> ConfirmTransactionOut confirmTransaction(key, input)

Confirm transaction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taxamo.com");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    String key = "key_example"; // String | Transaction key.
    ConfirmTransactionIn input = new ConfirmTransactionIn(); // ConfirmTransactionIn | Input
    try {
      ConfirmTransactionOut result = apiInstance.confirmTransaction(key, input);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#confirmTransaction");
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
| **key** | **String**| Transaction key. | |
| **input** | [**ConfirmTransactionIn**](ConfirmTransactionIn.md)| Input | |

### Return type

[**ConfirmTransactionOut**](ConfirmTransactionOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Validation failed, see JSON body response for details. |  -  |
| **401** | Incorrect token |  -  |

<a id="createTransaction"></a>
# **createTransaction**
> CreateTransactionOut createTransaction(input)

Store transaction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taxamo.com");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    CreateTransactionIn input = new CreateTransactionIn(); // CreateTransactionIn | Input
    try {
      CreateTransactionOut result = apiInstance.createTransaction(input);
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
| **input** | [**CreateTransactionIn**](CreateTransactionIn.md)| Input | |

### Return type

[**CreateTransactionOut**](CreateTransactionOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Validation failed, see JSON body response for details. |  -  |
| **401** | Incorrect token |  -  |

<a id="getTransaction"></a>
# **getTransaction**
> GetTransactionOut getTransaction(key)

Retrieve transaction data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taxamo.com");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    String key = "key_example"; // String | Transaction key
    try {
      GetTransactionOut result = apiInstance.getTransaction(key);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#getTransaction");
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
| **key** | **String**| Transaction key | |

### Return type

[**GetTransactionOut**](GetTransactionOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Validation failed, see JSON body response for details. |  -  |
| **401** | Incorrect token |  -  |

<a id="listTransactions"></a>
# **listTransactions**
> ListTransactionsOut listTransactions(filterText, offset, hasNote, keyOrCustomId, currencyCode, orderDateTo, sortReverse, limit, invoiceNumber, taxCountryCodes, statuses, originalTransactionKey, orderDateFrom, totalAmountGreaterThan, format, totalAmountLessThan, taxCountryCode)

Browse transactions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taxamo.com");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    String filterText = "filterText_example"; // String | Filtering expression
    Integer offset = 56; // Integer | Offset
    Boolean hasNote = true; // Boolean | Return only transactions with a note field set.
    String keyOrCustomId = "keyOrCustomId_example"; // String | Taxamo provided transaction key or custom id
    String currencyCode = "currencyCode_example"; // String | Three letter ISO currency code.
    String orderDateTo = "orderDateTo_example"; // String | Order date to in yyyy-MM-dd format.
    Boolean sortReverse = true; // Boolean | If true, results are sorted in descending order.
    Integer limit = 56; // Integer | Limit (no more than 1000, defaults to 100).
    String invoiceNumber = "invoiceNumber_example"; // String | Transaction invoice number.
    String taxCountryCodes = "taxCountryCodes_example"; // String | Comma separated list of two letter ISO tax country codes.
    String statuses = "statuses_example"; // String | Comma separated list of of transaction statuses. 'N' - unconfirmed transaction, 'C' - confirmed transaction.
    String originalTransactionKey = "originalTransactionKey_example"; // String | Taxamo provided original transaction key
    String orderDateFrom = "orderDateFrom_example"; // String | Order date from in yyyy-MM-dd format.
    String totalAmountGreaterThan = "totalAmountGreaterThan_example"; // String | Return only transactions with total amount greater than given number. Transactions with total amount equal to a given number (e.g. 0) are not returned.
    String format = "format_example"; // String | Output format - supports 'csv' value for this operation.
    String totalAmountLessThan = "totalAmountLessThan_example"; // String | Return only transactions with total amount less than a given number. Transactions with total amount equal to a given number (e.g. 1) are not returned.
    String taxCountryCode = "taxCountryCode_example"; // String | Two letter ISO tax country code.
    try {
      ListTransactionsOut result = apiInstance.listTransactions(filterText, offset, hasNote, keyOrCustomId, currencyCode, orderDateTo, sortReverse, limit, invoiceNumber, taxCountryCodes, statuses, originalTransactionKey, orderDateFrom, totalAmountGreaterThan, format, totalAmountLessThan, taxCountryCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#listTransactions");
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
| **filterText** | **String**| Filtering expression | [optional] |
| **offset** | **Integer**| Offset | [optional] |
| **hasNote** | **Boolean**| Return only transactions with a note field set. | [optional] |
| **keyOrCustomId** | **String**| Taxamo provided transaction key or custom id | [optional] |
| **currencyCode** | **String**| Three letter ISO currency code. | [optional] |
| **orderDateTo** | **String**| Order date to in yyyy-MM-dd format. | [optional] |
| **sortReverse** | **Boolean**| If true, results are sorted in descending order. | [optional] |
| **limit** | **Integer**| Limit (no more than 1000, defaults to 100). | [optional] |
| **invoiceNumber** | **String**| Transaction invoice number. | [optional] |
| **taxCountryCodes** | **String**| Comma separated list of two letter ISO tax country codes. | [optional] |
| **statuses** | **String**| Comma separated list of of transaction statuses. &#39;N&#39; - unconfirmed transaction, &#39;C&#39; - confirmed transaction. | [optional] |
| **originalTransactionKey** | **String**| Taxamo provided original transaction key | [optional] |
| **orderDateFrom** | **String**| Order date from in yyyy-MM-dd format. | [optional] |
| **totalAmountGreaterThan** | **String**| Return only transactions with total amount greater than given number. Transactions with total amount equal to a given number (e.g. 0) are not returned. | [optional] |
| **format** | **String**| Output format - supports &#39;csv&#39; value for this operation. | [optional] |
| **totalAmountLessThan** | **String**| Return only transactions with total amount less than a given number. Transactions with total amount equal to a given number (e.g. 1) are not returned. | [optional] |
| **taxCountryCode** | **String**| Two letter ISO tax country code. | [optional] |

### Return type

[**ListTransactionsOut**](ListTransactionsOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Validation failed, see JSON body response for details. |  -  |
| **401** | Incorrect token |  -  |

<a id="unconfirmTransaction"></a>
# **unconfirmTransaction**
> UnconfirmTransactionOut unconfirmTransaction(key, input)

Un-confirm the transaction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taxamo.com");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    String key = "key_example"; // String | Transaction key.
    UnconfirmTransactionIn input = new UnconfirmTransactionIn(); // UnconfirmTransactionIn | Input
    try {
      UnconfirmTransactionOut result = apiInstance.unconfirmTransaction(key, input);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#unconfirmTransaction");
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
| **key** | **String**| Transaction key. | |
| **input** | [**UnconfirmTransactionIn**](UnconfirmTransactionIn.md)| Input | |

### Return type

[**UnconfirmTransactionOut**](UnconfirmTransactionOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Validation failed, see JSON body response for details. |  -  |
| **401** | Incorrect token |  -  |

<a id="updateTransaction"></a>
# **updateTransaction**
> UpdateTransactionOut updateTransaction(key, input)

Update transaction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taxamo.com");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    String key = "key_example"; // String | Transaction key.
    UpdateTransactionIn input = new UpdateTransactionIn(); // UpdateTransactionIn | Input
    try {
      UpdateTransactionOut result = apiInstance.updateTransaction(key, input);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#updateTransaction");
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
| **key** | **String**| Transaction key. | |
| **input** | [**UpdateTransactionIn**](UpdateTransactionIn.md)| Input | |

### Return type

[**UpdateTransactionOut**](UpdateTransactionOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Validation failed, see JSON body response for details. |  -  |
| **401** | Incorrect token |  -  |

