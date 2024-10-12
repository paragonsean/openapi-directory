# TransactionsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createOrRunTransactionCategorizationRules**](TransactionsApi.md#createOrRunTransactionCategorizationRules) | **POST** /transactions/categories/rules | Create or Run Transaction Categorization Rule |
| [**createTransactionCategory**](TransactionsApi.md#createTransactionCategory) | **POST** /transactions/categories | Create Category |
| [**deleteTransactionCategorizationRule**](TransactionsApi.md#deleteTransactionCategorizationRule) | **DELETE** /transactions/categories/rules/{ruleId} | Delete Transaction Categorization Rule |
| [**deleteTransactionCategory**](TransactionsApi.md#deleteTransactionCategory) | **DELETE** /transactions/categories/{categoryId} | Delete Category |
| [**getTransactionCategories**](TransactionsApi.md#getTransactionCategories) | **GET** /transactions/categories | Get Transaction Category List |
| [**getTransactionCategorizationRules**](TransactionsApi.md#getTransactionCategorizationRules) | **GET** /transactions/categories/txnRules | Get Transaction Categorization Rules |
| [**getTransactionCategorizationRulesDeprecated**](TransactionsApi.md#getTransactionCategorizationRulesDeprecated) | **GET** /transactions/categories/rules | Get Transaction Categorization Rules |
| [**getTransactions**](TransactionsApi.md#getTransactions) | **GET** /transactions | Get Transactions |
| [**getTransactionsCount**](TransactionsApi.md#getTransactionsCount) | **GET** /transactions/count | Get Transactions Count |
| [**runTransactionCategorizationRule**](TransactionsApi.md#runTransactionCategorizationRule) | **POST** /transactions/categories/rules/{ruleId} | Run Transaction Categorization Rule |
| [**updateTransaction**](TransactionsApi.md#updateTransaction) | **PUT** /transactions/{transactionId} | Update Transaction |
| [**updateTransactionCategorizationRule**](TransactionsApi.md#updateTransactionCategorizationRule) | **PUT** /transactions/categories/rules/{ruleId} | Update Transaction Categorization Rule |
| [**updateTransactionCategory**](TransactionsApi.md#updateTransactionCategory) | **PUT** /transactions/categories | Update Category |


<a id="createOrRunTransactionCategorizationRules"></a>
# **createOrRunTransactionCategorizationRules**
> createOrRunTransactionCategorizationRules(action, ruleParam)

Create or Run Transaction Categorization Rule

The Create or Run Transaction Categorization Rule endpoint is used to: &lt;br&gt;Create transaction categorization rules for both system and user-defined categories.&lt;br&gt;Run all the transaction categorization rules to categorize transactions by calling the endpoint with action&#x3D;run as the query parameter. &lt;br&gt;&lt;br&gt;The input body parameters to create transaction categorization rules follow:&lt;br&gt;     categoryId - This field is mandatory and numeric&lt;br&gt;     priority - This field is optional and numeric. Priority decides the order in which the rule gets applied on transactions.&lt;br&gt;     ruleClause - This field is mandatory and should contain at least one rule&lt;br&gt;     field - The value can be description or amount&lt;br&gt;&lt;br&gt;       If the field value is description then,&lt;br&gt;         1. operation - value can be stringEquals or stringContains&lt;br&gt;         2. value - value should be min of 3 and max of 50 characters&lt;br&gt;&lt;br&gt;       If the field value is amount then, &lt;br&gt;         1. operation - value can be numberEquals, numberLessThan, numberLessThanEquals, numberGreaterThan or numberGreaterThanEquals&lt;br&gt;         2. value - min value 0 and a max value of 99999999999.99 is allowed&lt;br&gt;The HTTP response code is 201 (Created Successfully).

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
    defaultClient.setBasePath("http://localhost");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    String action = "action_example"; // String | To run rules, pass action=run. Only value run is supported
    String ruleParam = "ruleParam_example"; // String | rules(JSON format) to categorize the transactions
    try {
      apiInstance.createOrRunTransactionCategorizationRules(action, ruleParam);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#createOrRunTransactionCategorizationRules");
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
| **action** | **String**| To run rules, pass action&#x3D;run. Only value run is supported | [optional] |
| **ruleParam** | **String**| rules(JSON format) to categorize the transactions | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created Successfully |  -  |
| **204** | No Content |  -  |
| **400** | Y806 : Invalid input&lt;br&gt;Y400 : Rule already exists. Rule should be unique in terms of combination of description and amount |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="createTransactionCategory"></a>
# **createTransactionCategory**
> createTransactionCategory(transactionCategoryRequest)

Create Category

The create transaction categories service is used to create user-defined categories for a system-defined category.&lt;br&gt;The parentCategoryId is the system-defined category id.This can be retrieved using get transaction categories service.&lt;br&gt;The categoryName can accept minimum of 1, maximum of 50 alphanumeric or special characters.&lt;br&gt;The HTTP response code is 201 (Created successfully).&lt;br&gt;

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
    defaultClient.setBasePath("http://localhost");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    TransactionCategoryRequest transactionCategoryRequest = new TransactionCategoryRequest(); // TransactionCategoryRequest | User Transaction Category in JSON format
    try {
      apiInstance.createTransactionCategory(transactionCategoryRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#createTransactionCategory");
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
| **transactionCategoryRequest** | [**TransactionCategoryRequest**](TransactionCategoryRequest.md)| User Transaction Category in JSON format | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created Successfully |  -  |
| **400** | Y800 : Invalid value for categoryParam&lt;br&gt;Y800 : Invalid value for source&lt;br&gt;Y801 : Invalid length for categoryName. Min 1 and max 50 is required&lt;br&gt;Y803 : parentCategoryId required&lt;br&gt;Y811 : categoryName value already exists |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="deleteTransactionCategorizationRule"></a>
# **deleteTransactionCategorizationRule**
> deleteTransactionCategorizationRule(ruleId)

Delete Transaction Categorization Rule

The delete transaction categorization rule service is used to delete the given user-defined transaction categorization rule for both system-defined category as well as user-defined category.&lt;br&gt;This will delete all the corresponding rule clauses associated with the rule.&lt;br&gt;The HTTP response code is 204 (Success without content).&lt;br&gt;

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
    defaultClient.setBasePath("http://localhost");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    Long ruleId = 56L; // Long | ruleId
    try {
      apiInstance.deleteTransactionCategorizationRule(ruleId);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#deleteTransactionCategorizationRule");
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
| **ruleId** | **Long**| ruleId | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Deleted Successfully |  -  |
| **400** | Y800 : Invalid value for ruleId |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="deleteTransactionCategory"></a>
# **deleteTransactionCategory**
> deleteTransactionCategory(categoryId)

Delete Category

The delete transaction categories service is used to delete the given user-defined category.&lt;br&gt;The HTTP response code is 204 (Success without content).&lt;br&gt;

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
    defaultClient.setBasePath("http://localhost");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    Long categoryId = 56L; // Long | categoryId
    try {
      apiInstance.deleteTransactionCategory(categoryId);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#deleteTransactionCategory");
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
| **categoryId** | **Long**| categoryId | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Deleted Successfully |  -  |
| **400** | Y800 : Invalid value for categoryId |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="getTransactionCategories"></a>
# **getTransactionCategories**
> TransactionCategoryResponse getTransactionCategories()

Get Transaction Category List

The categories service returns the list of available transaction categories.&lt;br&gt;High level category is returned in the response only if it is opted by the customer.&lt;br&gt;When invoked by passing the cobrand session or admin access token, this service returns the supported transaction categories at the cobrand level. &lt;br&gt;When invoked by passing the cobrand session and the user session or user access token, this service returns the transaction categories &lt;br&gt;along with user-defined categories.&lt;br&gt;Double quotes in the user-defined category name will be prefixed by backslashes (&amp;#92;) in the response, &lt;br&gt;e.g. Toys \&quot;R\&quot; Us.&lt;br/&gt;Source and id are the primary attributes of the category entity.&lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt;&lt;li&gt;This service supports the localization feature and accepts locale as a header parameter.&lt;/li&gt;

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
    defaultClient.setBasePath("http://localhost");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    try {
      TransactionCategoryResponse result = apiInstance.getTransactionCategories();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#getTransactionCategories");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TransactionCategoryResponse**](TransactionCategoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="getTransactionCategorizationRules"></a>
# **getTransactionCategorizationRules**
> TransactionCategorizationRuleResponse getTransactionCategorizationRules()

Get Transaction Categorization Rules

The get transaction categorization rule service is used to get all the categorization rules.&lt;br&gt;

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
    defaultClient.setBasePath("http://localhost");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    try {
      TransactionCategorizationRuleResponse result = apiInstance.getTransactionCategorizationRules();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#getTransactionCategorizationRules");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TransactionCategorizationRuleResponse**](TransactionCategorizationRuleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="getTransactionCategorizationRulesDeprecated"></a>
# **getTransactionCategorizationRulesDeprecated**
> List&lt;TransactionCategorizationRule&gt; getTransactionCategorizationRulesDeprecated()

Get Transaction Categorization Rules

The get transaction categorization rule service is used to get all the categorization rules.&lt;br&gt;

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
    defaultClient.setBasePath("http://localhost");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    try {
      List<TransactionCategorizationRule> result = apiInstance.getTransactionCategorizationRulesDeprecated();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#getTransactionCategorizationRulesDeprecated");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;TransactionCategorizationRule&gt;**](TransactionCategorizationRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="getTransactions"></a>
# **getTransactions**
> TransactionResponse getTransactions(accountId, baseType, categoryId, categoryType, container, detailCategoryId, fromDate, highLevelCategoryId, keyword, skip, toDate, top, type)

Get Transactions

The Transaction service is used to get a list of transactions for a user.&lt;br&gt;By default, this service returns the last 30 days of transactions from today&#39;s date.&lt;br&gt;The keyword parameter performs a contains search on the original, consumer, and simple description attributes, replace the special characters #, &amp;, and + with percent-encoding values %23, %26, and %2B respectively. Eg: for -Debit# , pass the input as -Debit%23.&lt;br&gt;Values for categoryId parameter can be fetched from get transaction category list service.&lt;br&gt; The categoryId is used to filter transactions based on system-defined category as well as user-defined category.&lt;br&gt;User-defined categoryIds should be provided in the filter with the prefix &#39;&#39;U&#39;&#39;. E.g. U10002&lt;br&gt;The skip and top parameters are used for pagination. In the skip and top parameters pass the number of records to be skipped and retrieved, respectively. The response header provides the links to retrieve the next and previous set of transactions.&lt;br&gt;Double quotes in the merchant name will be prefixed by backslashes (&amp;#92;) in the response, e.g. Toys \&quot;R\&quot; Us. &lt;br&gt;sourceId is a unique ID that the provider site has assigned to the transaction. The source ID is only available for the pre-populated accounts. Pre-populated accounts are the accounts that the FI customers shares with Yodlee, so that the user does not have to add or aggregate those accounts.&lt;br&gt;&lt;br&gt;&lt;b&gt;Note&lt;/b&gt;&lt;li&gt; &lt;a href&#x3D;\&quot;https://developer.yodlee.com/docs/api/1.1/Transaction_Data_Enrichment\&quot;&gt;TDE&lt;/a&gt; is made available for bank and card accounts and for the US market only.The address field in the response is available only when the TDE key is turned on.&lt;li&gt;The pagination feature is available by default. If no values are passed in the skip and top parameters, the API will only return the first 500 transactions.&lt;li&gt;This service supports the localization feature and accepts locale as a header parameter.&lt;br&gt;

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
    defaultClient.setBasePath("http://localhost");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    String accountId = "accountId_example"; // String | Comma separated accountIds
    String baseType = "baseType_example"; // String | DEBIT/CREDIT
    String categoryId = "categoryId_example"; // String | Comma separated categoryIds
    String categoryType = "categoryType_example"; // String | Transaction Category Type(UNCATEGORIZE, INCOME, TRANSFER, EXPENSE or DEFERRED_COMPENSATION)
    String container = "container_example"; // String | bank/creditCard/investment/insurance/loan
    String detailCategoryId = "detailCategoryId_example"; // String | Comma separated detailCategoryIds
    String fromDate = "fromDate_example"; // String | Transaction from date(YYYY-MM-DD)
    String highLevelCategoryId = "highLevelCategoryId_example"; // String | Comma separated highLevelCategoryIds
    String keyword = "keyword_example"; // String | Transaction search text
    Integer skip = 56; // Integer | skip (Min 0)
    String toDate = "toDate_example"; // String | Transaction end date (YYYY-MM-DD)
    Integer top = 56; // Integer | top (Max 500)
    String type = "type_example"; // String | Transaction Type(SELL,SWEEP, etc.) for bank/creditCard/investment
    try {
      TransactionResponse result = apiInstance.getTransactions(accountId, baseType, categoryId, categoryType, container, detailCategoryId, fromDate, highLevelCategoryId, keyword, skip, toDate, top, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#getTransactions");
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
| **accountId** | **String**| Comma separated accountIds | [optional] |
| **baseType** | **String**| DEBIT/CREDIT | [optional] |
| **categoryId** | **String**| Comma separated categoryIds | [optional] |
| **categoryType** | **String**| Transaction Category Type(UNCATEGORIZE, INCOME, TRANSFER, EXPENSE or DEFERRED_COMPENSATION) | [optional] |
| **container** | **String**| bank/creditCard/investment/insurance/loan | [optional] |
| **detailCategoryId** | **String**| Comma separated detailCategoryIds | [optional] |
| **fromDate** | **String**| Transaction from date(YYYY-MM-DD) | [optional] |
| **highLevelCategoryId** | **String**| Comma separated highLevelCategoryIds | [optional] |
| **keyword** | **String**| Transaction search text | [optional] |
| **skip** | **Integer**| skip (Min 0) | [optional] |
| **toDate** | **String**| Transaction end date (YYYY-MM-DD) | [optional] |
| **top** | **Integer**| top (Max 500) | [optional] |
| **type** | **String**| Transaction Type(SELL,SWEEP, etc.) for bank/creditCard/investment | [optional] |

### Return type

[**TransactionResponse**](TransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Y800 : Invalid value for baseType&lt;br&gt;Y800 : Invalid value for fromDate&lt;br&gt;Y800 : Invalid value for category&lt;br&gt;Y800 : Invalid value for toDate&lt;br&gt;Y800 : Invalid value for container&lt;br&gt;Y809 : Invalid date range&lt;br&gt;Y804 : Permitted values of top between 1 - 500&lt;br&gt;Y805 : Multiple containers not supported&lt;br&gt;Y800 : Invalid value for transaction type&lt;br&gt;Y824 : The maximum number of accountIds permitted is 100&lt;br&gt;Y824 : The maximum number of categoryIds permitted is 100&lt;br&gt;Y824 : The maximum number of highLevelCategoryIds permitted is 100&lt;br&gt;Y848 : detailCategoryId cannot be provided as input, as the detailedCategory feature is not enabled&lt;br&gt;Y823 : detailCategoryId is not for applicable containers other than bank and card&lt;br&gt;Y824 : The maximum number of detailCategoryIds permitted is 100&lt;br&gt;Y800 : Invalid value for detailCategoryId |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="getTransactionsCount"></a>
# **getTransactionsCount**
> TransactionCountResponse getTransactionsCount(accountId, baseType, categoryId, categoryType, container, detailCategoryId, fromDate, highLevelCategoryId, keyword, toDate, type)

Get Transactions Count

The count service provides the total number of transactions for a specific user depending on the input parameters passed.&lt;br&gt;If you are implementing pagination for transactions, call this endpoint before calling GET /transactions to know the number of transactions that are returned for the input parameters passed.&lt;br&gt;The functionality of the input parameters remains the same as that of the GET /transactions endpoint.&lt;br&gt;

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
    defaultClient.setBasePath("http://localhost");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    String accountId = "accountId_example"; // String | Comma separated accountIds 
    String baseType = "baseType_example"; // String | DEBIT/CREDIT
    String categoryId = "categoryId_example"; // String | Comma separated categoryIds
    String categoryType = "categoryType_example"; // String | Transaction Category Type(UNCATEGORIZE, INCOME, TRANSFER, EXPENSE or DEFERRED_COMPENSATION)
    String container = "container_example"; // String | bank/creditCard/investment/insurance/loan
    String detailCategoryId = "detailCategoryId_example"; // String | Comma separated detailCategoryIds
    String fromDate = "fromDate_example"; // String | Transaction from date(YYYY-MM-DD)
    String highLevelCategoryId = "highLevelCategoryId_example"; // String | Comma separated highLevelCategoryIds
    String keyword = "keyword_example"; // String | Transaction search text 
    String toDate = "toDate_example"; // String | Transaction end date (YYYY-MM-DD)
    String type = "type_example"; // String | Transaction Type(SELL,SWEEP, etc.)
    try {
      TransactionCountResponse result = apiInstance.getTransactionsCount(accountId, baseType, categoryId, categoryType, container, detailCategoryId, fromDate, highLevelCategoryId, keyword, toDate, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#getTransactionsCount");
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
| **accountId** | **String**| Comma separated accountIds  | [optional] |
| **baseType** | **String**| DEBIT/CREDIT | [optional] |
| **categoryId** | **String**| Comma separated categoryIds | [optional] |
| **categoryType** | **String**| Transaction Category Type(UNCATEGORIZE, INCOME, TRANSFER, EXPENSE or DEFERRED_COMPENSATION) | [optional] |
| **container** | **String**| bank/creditCard/investment/insurance/loan | [optional] |
| **detailCategoryId** | **String**| Comma separated detailCategoryIds | [optional] |
| **fromDate** | **String**| Transaction from date(YYYY-MM-DD) | [optional] |
| **highLevelCategoryId** | **String**| Comma separated highLevelCategoryIds | [optional] |
| **keyword** | **String**| Transaction search text  | [optional] |
| **toDate** | **String**| Transaction end date (YYYY-MM-DD) | [optional] |
| **type** | **String**| Transaction Type(SELL,SWEEP, etc.) | [optional] |

### Return type

[**TransactionCountResponse**](TransactionCountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Y800 : Invalid value for detailCategoryId&lt;br&gt;Y848 : detailCategoryId cannot be provided as input, as the detailedCategory feature is not enabled&lt;br&gt;Y823 : detailCategoryId is not applicable for containers other than bank and card&lt;br&gt;Y824 : The maximum number of detailCategoryIds permitted is 100&lt;br&gt; |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="runTransactionCategorizationRule"></a>
# **runTransactionCategorizationRule**
> runTransactionCategorizationRule(action, ruleId)

Run Transaction Categorization Rule

The run transaction categorization rule service is used to run a rule on transactions, to categorize the transactions.&lt;br&gt;The HTTP response code is 204 (Success with no content).&lt;br&gt;

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
    defaultClient.setBasePath("http://localhost");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    String action = "run"; // String | 
    Long ruleId = 56L; // Long | Unique id of the categorization rule
    try {
      apiInstance.runTransactionCategorizationRule(action, ruleId);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#runTransactionCategorizationRule");
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
| **action** | **String**|  | [default to run] [enum: run] |
| **ruleId** | **Long**| Unique id of the categorization rule | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Run Successfully |  -  |
| **400** | Y800 : Invalid value for ruleId&lt;br&gt;Y400 : Categorization already in progress |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="updateTransaction"></a>
# **updateTransaction**
> updateTransaction(transactionId, transactionRequest)

Update Transaction

The update transaction service is used to update the category,consumer description, memo for a transaction.&lt;br&gt;The HTTP response code is 204 (Success without content).&lt;br&gt;

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
    defaultClient.setBasePath("http://localhost");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    Long transactionId = 56L; // Long | transactionId
    TransactionRequest transactionRequest = new TransactionRequest(); // TransactionRequest | transactionRequest
    try {
      apiInstance.updateTransaction(transactionId, transactionRequest);
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
| **transactionId** | **Long**| transactionId | |
| **transactionRequest** | [**TransactionRequest**](TransactionRequest.md)| transactionRequest | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Updated Successfully |  -  |
| **400** | Y812 : Required field -container missing in the transactionParam parameter input&lt;br&gt;Y800 : Invalid value for transactionId&lt;br&gt;Y800 : Invalid value for categoryId&lt;br&gt;Y868 : No action is allowed, as the data is being migrated to the Open Banking provider&lt;br&gt; |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="updateTransactionCategorizationRule"></a>
# **updateTransactionCategorizationRule**
> updateTransactionCategorizationRule(ruleId, transactionCategorizationRuleRequest)

Update Transaction Categorization Rule

The update transaction categorization rule service is used to update a categorization rule for both system-defined category as well as user-defined category.&lt;br&gt;ruleParam JSON input should be as explained in the create transaction categorization rule service.&lt;br&gt;The HTTP response code is 204 (Success without content).&lt;br&gt;

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
    defaultClient.setBasePath("http://localhost");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    Long ruleId = 56L; // Long | ruleId
    TransactionCategorizationRuleRequest transactionCategorizationRuleRequest = new TransactionCategorizationRuleRequest(); // TransactionCategorizationRuleRequest | transactionCategoriesRuleRequest
    try {
      apiInstance.updateTransactionCategorizationRule(ruleId, transactionCategorizationRuleRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#updateTransactionCategorizationRule");
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
| **ruleId** | **Long**| ruleId | |
| **transactionCategorizationRuleRequest** | [**TransactionCategorizationRuleRequest**](TransactionCategorizationRuleRequest.md)| transactionCategoriesRuleRequest | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Updated Successfully |  -  |
| **400** | Y800 : Invalid value for ruleId&lt;br&gt;Y806 : Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="updateTransactionCategory"></a>
# **updateTransactionCategory**
> updateTransactionCategory(updateCategoryRequest)

Update Category

The update transaction categories service is used to update the transaction category name&lt;br&gt;for a high level category, a system-defined category and a user-defined category.&lt;br&gt;The renamed category can be set back to the original name by passing an empty string for categoryName.&lt;br&gt;The categoryName can accept minimum of 1, maximum of 50 alphanumeric or special characters.&lt;br&gt;The HTTP response code is 204 (Success without content).&lt;br&gt;

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
    defaultClient.setBasePath("http://localhost");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    UpdateCategoryRequest updateCategoryRequest = new UpdateCategoryRequest(); // UpdateCategoryRequest | updateCategoryRequest
    try {
      apiInstance.updateTransactionCategory(updateCategoryRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#updateTransactionCategory");
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
| **updateCategoryRequest** | [**UpdateCategoryRequest**](UpdateCategoryRequest.md)| updateCategoryRequest | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Updated Successfully |  -  |
| **400** | Y800 : Invalid value for categoryParam&lt;br&gt;Y800 : Invalid value for source&lt;br&gt;Y801 : Invalid length for categoryName. Min 1 and max 50 is required&lt;br&gt;Y803 : id required&lt;br&gt;Y811 : categoryName value already exists |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

