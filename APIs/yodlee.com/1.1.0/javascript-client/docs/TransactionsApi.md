# YodleeCoreApis.TransactionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createOrRunTransactionCategorizationRules**](TransactionsApi.md#createOrRunTransactionCategorizationRules) | **POST** /transactions/categories/rules | Create or Run Transaction Categorization Rule
[**createTransactionCategory**](TransactionsApi.md#createTransactionCategory) | **POST** /transactions/categories | Create Category
[**deleteTransactionCategorizationRule**](TransactionsApi.md#deleteTransactionCategorizationRule) | **DELETE** /transactions/categories/rules/{ruleId} | Delete Transaction Categorization Rule
[**deleteTransactionCategory**](TransactionsApi.md#deleteTransactionCategory) | **DELETE** /transactions/categories/{categoryId} | Delete Category
[**getTransactionCategories**](TransactionsApi.md#getTransactionCategories) | **GET** /transactions/categories | Get Transaction Category List
[**getTransactionCategorizationRules**](TransactionsApi.md#getTransactionCategorizationRules) | **GET** /transactions/categories/txnRules | Get Transaction Categorization Rules
[**getTransactionCategorizationRulesDeprecated**](TransactionsApi.md#getTransactionCategorizationRulesDeprecated) | **GET** /transactions/categories/rules | Get Transaction Categorization Rules
[**getTransactions**](TransactionsApi.md#getTransactions) | **GET** /transactions | Get Transactions
[**getTransactionsCount**](TransactionsApi.md#getTransactionsCount) | **GET** /transactions/count | Get Transactions Count
[**runTransactionCategorizationRule**](TransactionsApi.md#runTransactionCategorizationRule) | **POST** /transactions/categories/rules/{ruleId} | Run Transaction Categorization Rule
[**updateTransaction**](TransactionsApi.md#updateTransaction) | **PUT** /transactions/{transactionId} | Update Transaction
[**updateTransactionCategorizationRule**](TransactionsApi.md#updateTransactionCategorizationRule) | **PUT** /transactions/categories/rules/{ruleId} | Update Transaction Categorization Rule
[**updateTransactionCategory**](TransactionsApi.md#updateTransactionCategory) | **PUT** /transactions/categories | Update Category



## createOrRunTransactionCategorizationRules

> createOrRunTransactionCategorizationRules(opts)

Create or Run Transaction Categorization Rule

The Create or Run Transaction Categorization Rule endpoint is used to: &lt;br&gt;Create transaction categorization rules for both system and user-defined categories.&lt;br&gt;Run all the transaction categorization rules to categorize transactions by calling the endpoint with action&#x3D;run as the query parameter. &lt;br&gt;&lt;br&gt;The input body parameters to create transaction categorization rules follow:&lt;br&gt;     categoryId - This field is mandatory and numeric&lt;br&gt;     priority - This field is optional and numeric. Priority decides the order in which the rule gets applied on transactions.&lt;br&gt;     ruleClause - This field is mandatory and should contain at least one rule&lt;br&gt;     field - The value can be description or amount&lt;br&gt;&lt;br&gt;       If the field value is description then,&lt;br&gt;         1. operation - value can be stringEquals or stringContains&lt;br&gt;         2. value - value should be min of 3 and max of 50 characters&lt;br&gt;&lt;br&gt;       If the field value is amount then, &lt;br&gt;         1. operation - value can be numberEquals, numberLessThan, numberLessThanEquals, numberGreaterThan or numberGreaterThanEquals&lt;br&gt;         2. value - min value 0 and a max value of 99999999999.99 is allowed&lt;br&gt;The HTTP response code is 201 (Created Successfully).

### Example

```javascript
import YodleeCoreApis from 'yodlee_core_apis';

let apiInstance = new YodleeCoreApis.TransactionsApi();
let opts = {
  'action': "action_example", // String | To run rules, pass action=run. Only value run is supported
  'ruleParam': "ruleParam_example" // String | rules(JSON format) to categorize the transactions
};
apiInstance.createOrRunTransactionCategorizationRules(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **String**| To run rules, pass action&#x3D;run. Only value run is supported | [optional] 
 **ruleParam** | **String**| rules(JSON format) to categorize the transactions | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## createTransactionCategory

> createTransactionCategory(transactionCategoryRequest)

Create Category

The create transaction categories service is used to create user-defined categories for a system-defined category.&lt;br&gt;The parentCategoryId is the system-defined category id.This can be retrieved using get transaction categories service.&lt;br&gt;The categoryName can accept minimum of 1, maximum of 50 alphanumeric or special characters.&lt;br&gt;The HTTP response code is 201 (Created successfully).&lt;br&gt;

### Example

```javascript
import YodleeCoreApis from 'yodlee_core_apis';

let apiInstance = new YodleeCoreApis.TransactionsApi();
let transactionCategoryRequest = new YodleeCoreApis.TransactionCategoryRequest(); // TransactionCategoryRequest | User Transaction Category in JSON format
apiInstance.createTransactionCategory(transactionCategoryRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transactionCategoryRequest** | [**TransactionCategoryRequest**](TransactionCategoryRequest.md)| User Transaction Category in JSON format | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json;charset=UTF-8


## deleteTransactionCategorizationRule

> deleteTransactionCategorizationRule(ruleId)

Delete Transaction Categorization Rule

The delete transaction categorization rule service is used to delete the given user-defined transaction categorization rule for both system-defined category as well as user-defined category.&lt;br&gt;This will delete all the corresponding rule clauses associated with the rule.&lt;br&gt;The HTTP response code is 204 (Success without content).&lt;br&gt;

### Example

```javascript
import YodleeCoreApis from 'yodlee_core_apis';

let apiInstance = new YodleeCoreApis.TransactionsApi();
let ruleId = 789; // Number | ruleId
apiInstance.deleteTransactionCategorizationRule(ruleId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ruleId** | **Number**| ruleId | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## deleteTransactionCategory

> deleteTransactionCategory(categoryId)

Delete Category

The delete transaction categories service is used to delete the given user-defined category.&lt;br&gt;The HTTP response code is 204 (Success without content).&lt;br&gt;

### Example

```javascript
import YodleeCoreApis from 'yodlee_core_apis';

let apiInstance = new YodleeCoreApis.TransactionsApi();
let categoryId = 789; // Number | categoryId
apiInstance.deleteTransactionCategory(categoryId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **categoryId** | **Number**| categoryId | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getTransactionCategories

> TransactionCategoryResponse getTransactionCategories()

Get Transaction Category List

The categories service returns the list of available transaction categories.&lt;br&gt;High level category is returned in the response only if it is opted by the customer.&lt;br&gt;When invoked by passing the cobrand session or admin access token, this service returns the supported transaction categories at the cobrand level. &lt;br&gt;When invoked by passing the cobrand session and the user session or user access token, this service returns the transaction categories &lt;br&gt;along with user-defined categories.&lt;br&gt;Double quotes in the user-defined category name will be prefixed by backslashes (&amp;#92;) in the response, &lt;br&gt;e.g. Toys \&quot;R\&quot; Us.&lt;br/&gt;Source and id are the primary attributes of the category entity.&lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt;&lt;li&gt;This service supports the localization feature and accepts locale as a header parameter.&lt;/li&gt;

### Example

```javascript
import YodleeCoreApis from 'yodlee_core_apis';

let apiInstance = new YodleeCoreApis.TransactionsApi();
apiInstance.getTransactionCategories((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## getTransactionCategorizationRules

> TransactionCategorizationRuleResponse getTransactionCategorizationRules()

Get Transaction Categorization Rules

The get transaction categorization rule service is used to get all the categorization rules.&lt;br&gt;

### Example

```javascript
import YodleeCoreApis from 'yodlee_core_apis';

let apiInstance = new YodleeCoreApis.TransactionsApi();
apiInstance.getTransactionCategorizationRules((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## getTransactionCategorizationRulesDeprecated

> [TransactionCategorizationRule] getTransactionCategorizationRulesDeprecated()

Get Transaction Categorization Rules

The get transaction categorization rule service is used to get all the categorization rules.&lt;br&gt;

### Example

```javascript
import YodleeCoreApis from 'yodlee_core_apis';

let apiInstance = new YodleeCoreApis.TransactionsApi();
apiInstance.getTransactionCategorizationRulesDeprecated((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[TransactionCategorizationRule]**](TransactionCategorizationRule.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getTransactions

> TransactionResponse getTransactions(opts)

Get Transactions

The Transaction service is used to get a list of transactions for a user.&lt;br&gt;By default, this service returns the last 30 days of transactions from today&#39;s date.&lt;br&gt;The keyword parameter performs a contains search on the original, consumer, and simple description attributes, replace the special characters #, &amp;, and + with percent-encoding values %23, %26, and %2B respectively. Eg: for -Debit# , pass the input as -Debit%23.&lt;br&gt;Values for categoryId parameter can be fetched from get transaction category list service.&lt;br&gt; The categoryId is used to filter transactions based on system-defined category as well as user-defined category.&lt;br&gt;User-defined categoryIds should be provided in the filter with the prefix &#39;&#39;U&#39;&#39;. E.g. U10002&lt;br&gt;The skip and top parameters are used for pagination. In the skip and top parameters pass the number of records to be skipped and retrieved, respectively. The response header provides the links to retrieve the next and previous set of transactions.&lt;br&gt;Double quotes in the merchant name will be prefixed by backslashes (&amp;#92;) in the response, e.g. Toys \&quot;R\&quot; Us. &lt;br&gt;sourceId is a unique ID that the provider site has assigned to the transaction. The source ID is only available for the pre-populated accounts. Pre-populated accounts are the accounts that the FI customers shares with Yodlee, so that the user does not have to add or aggregate those accounts.&lt;br&gt;&lt;br&gt;&lt;b&gt;Note&lt;/b&gt;&lt;li&gt; &lt;a href&#x3D;\&quot;https://developer.yodlee.com/docs/api/1.1/Transaction_Data_Enrichment\&quot;&gt;TDE&lt;/a&gt; is made available for bank and card accounts and for the US market only.The address field in the response is available only when the TDE key is turned on.&lt;li&gt;The pagination feature is available by default. If no values are passed in the skip and top parameters, the API will only return the first 500 transactions.&lt;li&gt;This service supports the localization feature and accepts locale as a header parameter.&lt;br&gt;

### Example

```javascript
import YodleeCoreApis from 'yodlee_core_apis';

let apiInstance = new YodleeCoreApis.TransactionsApi();
let opts = {
  'accountId': "accountId_example", // String | Comma separated accountIds
  'baseType': "baseType_example", // String | DEBIT/CREDIT
  'categoryId': "categoryId_example", // String | Comma separated categoryIds
  'categoryType': "categoryType_example", // String | Transaction Category Type(UNCATEGORIZE, INCOME, TRANSFER, EXPENSE or DEFERRED_COMPENSATION)
  'container': "container_example", // String | bank/creditCard/investment/insurance/loan
  'detailCategoryId': "detailCategoryId_example", // String | Comma separated detailCategoryIds
  'fromDate': "fromDate_example", // String | Transaction from date(YYYY-MM-DD)
  'highLevelCategoryId': "highLevelCategoryId_example", // String | Comma separated highLevelCategoryIds
  'keyword': "keyword_example", // String | Transaction search text
  'skip': 56, // Number | skip (Min 0)
  'toDate': "toDate_example", // String | Transaction end date (YYYY-MM-DD)
  'top': 56, // Number | top (Max 500)
  'type': "type_example" // String | Transaction Type(SELL,SWEEP, etc.) for bank/creditCard/investment
};
apiInstance.getTransactions(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| Comma separated accountIds | [optional] 
 **baseType** | **String**| DEBIT/CREDIT | [optional] 
 **categoryId** | **String**| Comma separated categoryIds | [optional] 
 **categoryType** | **String**| Transaction Category Type(UNCATEGORIZE, INCOME, TRANSFER, EXPENSE or DEFERRED_COMPENSATION) | [optional] 
 **container** | **String**| bank/creditCard/investment/insurance/loan | [optional] 
 **detailCategoryId** | **String**| Comma separated detailCategoryIds | [optional] 
 **fromDate** | **String**| Transaction from date(YYYY-MM-DD) | [optional] 
 **highLevelCategoryId** | **String**| Comma separated highLevelCategoryIds | [optional] 
 **keyword** | **String**| Transaction search text | [optional] 
 **skip** | **Number**| skip (Min 0) | [optional] 
 **toDate** | **String**| Transaction end date (YYYY-MM-DD) | [optional] 
 **top** | **Number**| top (Max 500) | [optional] 
 **type** | **String**| Transaction Type(SELL,SWEEP, etc.) for bank/creditCard/investment | [optional] 

### Return type

[**TransactionResponse**](TransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getTransactionsCount

> TransactionCountResponse getTransactionsCount(opts)

Get Transactions Count

The count service provides the total number of transactions for a specific user depending on the input parameters passed.&lt;br&gt;If you are implementing pagination for transactions, call this endpoint before calling GET /transactions to know the number of transactions that are returned for the input parameters passed.&lt;br&gt;The functionality of the input parameters remains the same as that of the GET /transactions endpoint.&lt;br&gt;

### Example

```javascript
import YodleeCoreApis from 'yodlee_core_apis';

let apiInstance = new YodleeCoreApis.TransactionsApi();
let opts = {
  'accountId': "accountId_example", // String | Comma separated accountIds 
  'baseType': "baseType_example", // String | DEBIT/CREDIT
  'categoryId': "categoryId_example", // String | Comma separated categoryIds
  'categoryType': "categoryType_example", // String | Transaction Category Type(UNCATEGORIZE, INCOME, TRANSFER, EXPENSE or DEFERRED_COMPENSATION)
  'container': "container_example", // String | bank/creditCard/investment/insurance/loan
  'detailCategoryId': "detailCategoryId_example", // String | Comma separated detailCategoryIds
  'fromDate': "fromDate_example", // String | Transaction from date(YYYY-MM-DD)
  'highLevelCategoryId': "highLevelCategoryId_example", // String | Comma separated highLevelCategoryIds
  'keyword': "keyword_example", // String | Transaction search text 
  'toDate': "toDate_example", // String | Transaction end date (YYYY-MM-DD)
  'type': "type_example" // String | Transaction Type(SELL,SWEEP, etc.)
};
apiInstance.getTransactionsCount(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| Comma separated accountIds  | [optional] 
 **baseType** | **String**| DEBIT/CREDIT | [optional] 
 **categoryId** | **String**| Comma separated categoryIds | [optional] 
 **categoryType** | **String**| Transaction Category Type(UNCATEGORIZE, INCOME, TRANSFER, EXPENSE or DEFERRED_COMPENSATION) | [optional] 
 **container** | **String**| bank/creditCard/investment/insurance/loan | [optional] 
 **detailCategoryId** | **String**| Comma separated detailCategoryIds | [optional] 
 **fromDate** | **String**| Transaction from date(YYYY-MM-DD) | [optional] 
 **highLevelCategoryId** | **String**| Comma separated highLevelCategoryIds | [optional] 
 **keyword** | **String**| Transaction search text  | [optional] 
 **toDate** | **String**| Transaction end date (YYYY-MM-DD) | [optional] 
 **type** | **String**| Transaction Type(SELL,SWEEP, etc.) | [optional] 

### Return type

[**TransactionCountResponse**](TransactionCountResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## runTransactionCategorizationRule

> runTransactionCategorizationRule(action, ruleId)

Run Transaction Categorization Rule

The run transaction categorization rule service is used to run a rule on transactions, to categorize the transactions.&lt;br&gt;The HTTP response code is 204 (Success with no content).&lt;br&gt;

### Example

```javascript
import YodleeCoreApis from 'yodlee_core_apis';

let apiInstance = new YodleeCoreApis.TransactionsApi();
let action = "'run'"; // String | 
let ruleId = 789; // Number | Unique id of the categorization rule
apiInstance.runTransactionCategorizationRule(action, ruleId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **String**|  | [default to &#39;run&#39;]
 **ruleId** | **Number**| Unique id of the categorization rule | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## updateTransaction

> updateTransaction(transactionId, transactionRequest)

Update Transaction

The update transaction service is used to update the category,consumer description, memo for a transaction.&lt;br&gt;The HTTP response code is 204 (Success without content).&lt;br&gt;

### Example

```javascript
import YodleeCoreApis from 'yodlee_core_apis';

let apiInstance = new YodleeCoreApis.TransactionsApi();
let transactionId = 789; // Number | transactionId
let transactionRequest = new YodleeCoreApis.TransactionRequest(); // TransactionRequest | transactionRequest
apiInstance.updateTransaction(transactionId, transactionRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transactionId** | **Number**| transactionId | 
 **transactionRequest** | [**TransactionRequest**](TransactionRequest.md)| transactionRequest | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json;charset=UTF-8


## updateTransactionCategorizationRule

> updateTransactionCategorizationRule(ruleId, transactionCategorizationRuleRequest)

Update Transaction Categorization Rule

The update transaction categorization rule service is used to update a categorization rule for both system-defined category as well as user-defined category.&lt;br&gt;ruleParam JSON input should be as explained in the create transaction categorization rule service.&lt;br&gt;The HTTP response code is 204 (Success without content).&lt;br&gt;

### Example

```javascript
import YodleeCoreApis from 'yodlee_core_apis';

let apiInstance = new YodleeCoreApis.TransactionsApi();
let ruleId = 789; // Number | ruleId
let transactionCategorizationRuleRequest = new YodleeCoreApis.TransactionCategorizationRuleRequest(); // TransactionCategorizationRuleRequest | transactionCategoriesRuleRequest
apiInstance.updateTransactionCategorizationRule(ruleId, transactionCategorizationRuleRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ruleId** | **Number**| ruleId | 
 **transactionCategorizationRuleRequest** | [**TransactionCategorizationRuleRequest**](TransactionCategorizationRuleRequest.md)| transactionCategoriesRuleRequest | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json;charset=UTF-8


## updateTransactionCategory

> updateTransactionCategory(updateCategoryRequest)

Update Category

The update transaction categories service is used to update the transaction category name&lt;br&gt;for a high level category, a system-defined category and a user-defined category.&lt;br&gt;The renamed category can be set back to the original name by passing an empty string for categoryName.&lt;br&gt;The categoryName can accept minimum of 1, maximum of 50 alphanumeric or special characters.&lt;br&gt;The HTTP response code is 204 (Success without content).&lt;br&gt;

### Example

```javascript
import YodleeCoreApis from 'yodlee_core_apis';

let apiInstance = new YodleeCoreApis.TransactionsApi();
let updateCategoryRequest = new YodleeCoreApis.UpdateCategoryRequest(); // UpdateCategoryRequest | updateCategoryRequest
apiInstance.updateTransactionCategory(updateCategoryRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updateCategoryRequest** | [**UpdateCategoryRequest**](UpdateCategoryRequest.md)| updateCategoryRequest | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json;charset=UTF-8

