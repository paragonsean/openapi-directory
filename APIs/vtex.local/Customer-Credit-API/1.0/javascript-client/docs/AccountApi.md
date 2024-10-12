# CustomerCreditApi.AccountApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountstatements**](AccountApi.md#accountstatements) | **GET** /api/creditcontrol/accounts/{creditAccountId}/statements | Account statements
[**addanaccountHolder**](AccountApi.md#addanaccountHolder) | **POST** /api/creditcontrol/accounts/{creditAccountId}/holders | Add an account Holder
[**cancelaPreAuthorization**](AccountApi.md#cancelaPreAuthorization) | **DELETE** /api/creditcontrol/accounts/{creditAccountId}/transactions/{transactionId} | Cancel a Pre Authorization
[**changecreditlimitofanAccount**](AccountApi.md#changecreditlimitofanAccount) | **PUT** /api/creditcontrol/accounts/{creditAccountId}/creditlimit | Change credit limit of an Account
[**changetoleranceofanaccount**](AccountApi.md#changetoleranceofanaccount) | **PUT** /api/creditcontrol/accounts/{creditAccountId}/tolerance | Change tolerance of an account
[**closeanAccount**](AccountApi.md#closeanAccount) | **DELETE** /api/creditcontrol/accounts/{creditAccountId} | Close an Account
[**createaPreAuthorization**](AccountApi.md#createaPreAuthorization) | **POST** /api/creditcontrol/accounts/{creditAccountId}/transaction | Create a Pre Authorization
[**createaPreAuthorizationUsingid**](AccountApi.md#createaPreAuthorizationUsingid) | **PUT** /api/creditcontrol/accounts/{creditAccountId}/transactions/{transactionId} | Create a Pre Authorization (using id)
[**createorUpdateSettlement**](AccountApi.md#createorUpdateSettlement) | **PUT** /api/creditcontrol/accounts/{creditAccountId}/transactions/{transactionId}/settlement | Create or Update Settlement
[**decreasebalanceofanaccount**](AccountApi.md#decreasebalanceofanaccount) | **PUT** /api/creditcontrol/accounts/{creditAccountId}/statements/{statementId} | Decrease balance of an account
[**deleteanaccountholder**](AccountApi.md#deleteanaccountholder) | **DELETE** /api/creditcontrol/accounts/{creditAccountId}/holders/{holderId} | Delete an account holder
[**openanAccount**](AccountApi.md#openanAccount) | **POST** /api/creditcontrol/accounts | Open an Account
[**openorChangeAccount**](AccountApi.md#openorChangeAccount) | **PUT** /api/creditcontrol/accounts/{accountId} | Open or Change Account
[**partialorTotalRefundaSettlement**](AccountApi.md#partialorTotalRefundaSettlement) | **POST** /api/creditcontrol/accounts/{creditAccountId}/transactions/{transactionId}/refunds | Partial or Total Refund a Settlement
[**retrieveaAccountbyId**](AccountApi.md#retrieveaAccountbyId) | **GET** /api/creditcontrol/accounts/{creditAccountId} | Retrieve an Account by Id
[**searchallaccounts**](AccountApi.md#searchallaccounts) | **GET** /api/creditcontrol/accounts | Search all accounts
[**updateemailanddescriptionofaaccount**](AccountApi.md#updateemailanddescriptionofaaccount) | **PUT** /api/creditcontrol/accounts/{creditAccountId} | Update email and description of a account



## accountstatements

> Statements1 accountstatements(contentType, accept, creditAccountId)

Account statements

Get the account statements.

### Example

```javascript
import CustomerCreditApi from 'customer_credit_api';
let defaultClient = CustomerCreditApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new CustomerCreditApi.AccountApi();
let contentType = "'application/json'"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
let accept = "'application/json'"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let creditAccountId = "'insert identifier here'"; // String | 
apiInstance.accountstatements(contentType, accept, creditAccountId, (error, data, response) => {
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
 **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **creditAccountId** | **String**|  | [default to &#39;insert identifier here&#39;]

### Return type

[**Statements1**](Statements1.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## addanaccountHolder

> Searchcheckingaccounts1 addanaccountHolder(creditAccountId, accept, contentType, addanaccountHolderRequest1)

Add an account Holder



### Example

```javascript
import CustomerCreditApi from 'customer_credit_api';
let defaultClient = CustomerCreditApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new CustomerCreditApi.AccountApi();
let creditAccountId = "'insert identifier here'"; // String | Credit account's identification
let accept = "'application/json'"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let contentType = "'application/json'"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
let addanaccountHolderRequest1 = {"claims":{"email":"USER-EMAIL"}}; // AddanaccountHolderRequest1 | 
apiInstance.addanaccountHolder(creditAccountId, accept, contentType, addanaccountHolderRequest1, (error, data, response) => {
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
 **creditAccountId** | **String**| Credit account&#39;s identification | [default to &#39;insert identifier here&#39;]
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **addanaccountHolderRequest1** | [**AddanaccountHolderRequest1**](AddanaccountHolderRequest1.md)|  | 

### Return type

[**Searchcheckingaccounts1**](Searchcheckingaccounts1.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8


## cancelaPreAuthorization

> cancelaPreAuthorization(contentType, accept, creditAccountId, transactionId)

Cancel a Pre Authorization



### Example

```javascript
import CustomerCreditApi from 'customer_credit_api';
let defaultClient = CustomerCreditApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new CustomerCreditApi.AccountApi();
let contentType = "'application/json'"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
let accept = "'application/json'"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let creditAccountId = "'insert identifier here'"; // String | Credit account's identification
let transactionId = "'insert identifier here'"; // String | 
apiInstance.cancelaPreAuthorization(contentType, accept, creditAccountId, transactionId, (error, data, response) => {
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
 **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **creditAccountId** | **String**| Credit account&#39;s identification | [default to &#39;insert identifier here&#39;]
 **transactionId** | **String**|  | [default to &#39;insert identifier here&#39;]

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## changecreditlimitofanAccount

> Object changecreditlimitofanAccount(creditAccountId, accept, contentType, changecreditlimitofanAccountRequest1)

Change credit limit of an Account

Increase the credit limit of an account.

### Example

```javascript
import CustomerCreditApi from 'customer_credit_api';
let defaultClient = CustomerCreditApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new CustomerCreditApi.AccountApi();
let creditAccountId = "'insert identifier here'"; // String | Credit account's identifier
let accept = "'application/json'"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let contentType = "'application/json'"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
let changecreditlimitofanAccountRequest1 = {"value":10000}; // ChangecreditlimitofanAccountRequest1 | 
apiInstance.changecreditlimitofanAccount(creditAccountId, accept, contentType, changecreditlimitofanAccountRequest1, (error, data, response) => {
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
 **creditAccountId** | **String**| Credit account&#39;s identifier | [default to &#39;insert identifier here&#39;]
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **changecreditlimitofanAccountRequest1** | [**ChangecreditlimitofanAccountRequest1**](ChangecreditlimitofanAccountRequest1.md)|  | 

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: text/plain


## changetoleranceofanaccount

> Object changetoleranceofanaccount(creditAccountId, accept, contentType, changetoleranceofanaccountRequest1)

Change tolerance of an account

Increase the credit limit of a checking account.

### Example

```javascript
import CustomerCreditApi from 'customer_credit_api';
let defaultClient = CustomerCreditApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new CustomerCreditApi.AccountApi();
let creditAccountId = "'insert identifier here'"; // String | Credit account's identification
let accept = "'application/json'"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let contentType = "'application/json'"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
let changetoleranceofanaccountRequest1 = {"value":0.2}; // ChangetoleranceofanaccountRequest1 | 
apiInstance.changetoleranceofanaccount(creditAccountId, accept, contentType, changetoleranceofanaccountRequest1, (error, data, response) => {
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
 **creditAccountId** | **String**| Credit account&#39;s identification | [default to &#39;insert identifier here&#39;]
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **changetoleranceofanaccountRequest1** | [**ChangetoleranceofanaccountRequest1**](ChangetoleranceofanaccountRequest1.md)|  | 

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: text/plain


## closeanAccount

> closeanAccount(creditAccountId, accept, contentType, closeanAccountRequest1)

Close an Account

Closes an account.

### Example

```javascript
import CustomerCreditApi from 'customer_credit_api';
let defaultClient = CustomerCreditApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new CustomerCreditApi.AccountApi();
let creditAccountId = "'insert identifier here'"; // String | Credit account's identifier
let accept = "'application/json'"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let contentType = "'application/json'"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
let closeanAccountRequest1 = {"document":"number","documentType":"CPF ou CNPJ ou Other","email":"email"}; // CloseanAccountRequest1 | 
apiInstance.closeanAccount(creditAccountId, accept, contentType, closeanAccountRequest1, (error, data, response) => {
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
 **creditAccountId** | **String**| Credit account&#39;s identifier | [default to &#39;insert identifier here&#39;]
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **closeanAccountRequest1** | [**CloseanAccountRequest1**](CloseanAccountRequest1.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## createaPreAuthorization

> createaPreAuthorization(creditAccountId, accept, contentType, createaPreAuthorizationRequest1)

Create a Pre Authorization



### Example

```javascript
import CustomerCreditApi from 'customer_credit_api';
let defaultClient = CustomerCreditApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new CustomerCreditApi.AccountApi();
let creditAccountId = "'insert identifier here'"; // String | Credit account's identification
let accept = "'application/json'"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let contentType = "'application/json'"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
let createaPreAuthorizationRequest1 = {"expirationDate":"date in ISO8601 (UTC) dateformat (optional default is 1(one) day)","installments":"integer (optional default is 1)","settle":false,"value":"decimal (required)"}; // CreateaPreAuthorizationRequest1 | 
apiInstance.createaPreAuthorization(creditAccountId, accept, contentType, createaPreAuthorizationRequest1, (error, data, response) => {
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
 **creditAccountId** | **String**| Credit account&#39;s identification | [default to &#39;insert identifier here&#39;]
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **createaPreAuthorizationRequest1** | [**CreateaPreAuthorizationRequest1**](CreateaPreAuthorizationRequest1.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## createaPreAuthorizationUsingid

> createaPreAuthorizationUsingid(creditAccountId, transactionId, accept, contentType, createaPreAuthorizationUsingidRequest)

Create a Pre Authorization (using id)



### Example

```javascript
import CustomerCreditApi from 'customer_credit_api';
let defaultClient = CustomerCreditApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new CustomerCreditApi.AccountApi();
let creditAccountId = "'insert identifier here'"; // String | Credit account's identification
let transactionId = "'insert identifier here'"; // String | 
let accept = "'application/json'"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let contentType = "'application/json'"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
let createaPreAuthorizationUsingidRequest = {"expirationDate":"date in ISO8601 (UTC) dateformat (optional default is 1(one) day)","installments":"integer (optional default is 1)","settle":false,"value":"decimal (required)"}; // CreateaPreAuthorizationUsingidRequest | 
apiInstance.createaPreAuthorizationUsingid(creditAccountId, transactionId, accept, contentType, createaPreAuthorizationUsingidRequest, (error, data, response) => {
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
 **creditAccountId** | **String**| Credit account&#39;s identification | [default to &#39;insert identifier here&#39;]
 **transactionId** | **String**|  | [default to &#39;insert identifier here&#39;]
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **createaPreAuthorizationUsingidRequest** | [**CreateaPreAuthorizationUsingidRequest**](CreateaPreAuthorizationUsingidRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## createorUpdateSettlement

> ThisoperationcausesthecreationofNinvoicesWhereNisthenumberofinstallmentsThefirstinvoicewillhaveaduedatewith30daysandthenextinvoiceswillhaveaduedate30daysawayfrompreviousinvoice createorUpdateSettlement(creditAccountId, transactionId, accept, contentType, createorUpdateSettlementRequest1)

Create or Update Settlement

Debit a value from checking account.

### Example

```javascript
import CustomerCreditApi from 'customer_credit_api';
let defaultClient = CustomerCreditApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new CustomerCreditApi.AccountApi();
let creditAccountId = "'insert identifier here'"; // String | Credit account's identification
let transactionId = "'insert identifier here'"; // String | 
let accept = "'application/json'"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let contentType = "'application/json'"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
let createorUpdateSettlementRequest1 = {"value":"decimal (required)"}; // CreateorUpdateSettlementRequest1 | 
apiInstance.createorUpdateSettlement(creditAccountId, transactionId, accept, contentType, createorUpdateSettlementRequest1, (error, data, response) => {
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
 **creditAccountId** | **String**| Credit account&#39;s identification | [default to &#39;insert identifier here&#39;]
 **transactionId** | **String**|  | [default to &#39;insert identifier here&#39;]
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **createorUpdateSettlementRequest1** | [**CreateorUpdateSettlementRequest1**](CreateorUpdateSettlementRequest1.md)|  | 

### Return type

[**ThisoperationcausesthecreationofNinvoicesWhereNisthenumberofinstallmentsThefirstinvoicewillhaveaduedatewith30daysandthenextinvoiceswillhaveaduedate30daysawayfrompreviousinvoice**](ThisoperationcausesthecreationofNinvoicesWhereNisthenumberofinstallmentsThefirstinvoicewillhaveaduedatewith30daysandthenextinvoiceswillhaveaduedate30daysawayfrompreviousinvoice.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## decreasebalanceofanaccount

> decreasebalanceofanaccount(creditAccountId, statementId, accept, contentType, decreasebalanceofanaccountRequest1)

Decrease balance of an account

Create a debit value updating the account BALANCE.

### Example

```javascript
import CustomerCreditApi from 'customer_credit_api';
let defaultClient = CustomerCreditApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new CustomerCreditApi.AccountApi();
let creditAccountId = "'insert example here'"; // String | Credit account's identification
let statementId = "'insert example here'"; // String | 
let accept = "'application/json'"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let contentType = "'application/json'"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
let decreasebalanceofanaccountRequest1 = {"value":"-number"}; // DecreasebalanceofanaccountRequest1 | 
apiInstance.decreasebalanceofanaccount(creditAccountId, statementId, accept, contentType, decreasebalanceofanaccountRequest1, (error, data, response) => {
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
 **creditAccountId** | **String**| Credit account&#39;s identification | [default to &#39;insert example here&#39;]
 **statementId** | **String**|  | [default to &#39;insert example here&#39;]
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **decreasebalanceofanaccountRequest1** | [**DecreasebalanceofanaccountRequest1**](DecreasebalanceofanaccountRequest1.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## deleteanaccountholder

> Searchcheckingaccounts1 deleteanaccountholder(contentType, accept, creditAccountId, holderId)

Delete an account holder



### Example

```javascript
import CustomerCreditApi from 'customer_credit_api';
let defaultClient = CustomerCreditApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new CustomerCreditApi.AccountApi();
let contentType = "'application/json'"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
let accept = "'application/json'"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let creditAccountId = "'insert identifier here'"; // String | Credit account's identification
let holderId = "'insert identifier here'"; // String | 
apiInstance.deleteanaccountholder(contentType, accept, creditAccountId, holderId, (error, data, response) => {
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
 **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **creditAccountId** | **String**| Credit account&#39;s identification | [default to &#39;insert identifier here&#39;]
 **holderId** | **String**|  | [default to &#39;insert identifier here&#39;]

### Return type

[**Searchcheckingaccounts1**](Searchcheckingaccounts1.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## openanAccount

> String openanAccount(accept, contentType, openanAccountRequest1)

Open an Account

Open an account.

### Example

```javascript
import CustomerCreditApi from 'customer_credit_api';
let defaultClient = CustomerCreditApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new CustomerCreditApi.AccountApi();
let accept = "'application/json'"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let contentType = "'application/json'"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
let openanAccountRequest1 = {"creditLimit":"number","description":"description","document":"number","documentType":"CPF ou CNPJ ou Other","email":"email","tolerance":"1 is 100%"}; // OpenanAccountRequest1 | 
apiInstance.openanAccount(accept, contentType, openanAccountRequest1, (error, data, response) => {
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
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **openanAccountRequest1** | [**OpenanAccountRequest1**](OpenanAccountRequest1.md)|  | 

### Return type

**String**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8


## openorChangeAccount

> String openorChangeAccount(accountId, accept, contentType, opts)

Open or Change Account

Open or Change an account.

### Example

```javascript
import CustomerCreditApi from 'customer_credit_api';
let defaultClient = CustomerCreditApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new CustomerCreditApi.AccountApi();
let accountId = "'insert identifier here'"; // String | It must be an alphanumeric value
let accept = "'application/json'"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let contentType = "'application/json'"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
let opts = {
  'openorChangeAccountRequest1': {"creditLimit":"number","email":"email"} // OpenorChangeAccountRequest1 | 
};
apiInstance.openorChangeAccount(accountId, accept, contentType, opts, (error, data, response) => {
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
 **accountId** | **String**| It must be an alphanumeric value | [default to &#39;insert identifier here&#39;]
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **openorChangeAccountRequest1** | [**OpenorChangeAccountRequest1**](OpenorChangeAccountRequest1.md)|  | [optional] 

### Return type

**String**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8


## partialorTotalRefundaSettlement

> ThisoperationcausesthecreationofNinvoicesWhereNisthenumberofinstallmentsThefirstinvoicewillhaveaduedatewith30daysandthenextinvoiceswillhaveaduedate30daysawayfrompreviousinvoice partialorTotalRefundaSettlement(creditAccountId, transactionId, accept, contentType, partialorTotalRefundaSettlementRequest1)

Partial or Total Refund a Settlement

Refund a value from a already settled transaction.

### Example

```javascript
import CustomerCreditApi from 'customer_credit_api';
let defaultClient = CustomerCreditApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new CustomerCreditApi.AccountApi();
let creditAccountId = "'insert identifier here'"; // String | Credit account's identification
let transactionId = "'insert identifier here'"; // String | 
let accept = "'application/json'"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let contentType = "'application/json'"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
let partialorTotalRefundaSettlementRequest1 = {"value":"decimal (required)"}; // PartialorTotalRefundaSettlementRequest1 | 
apiInstance.partialorTotalRefundaSettlement(creditAccountId, transactionId, accept, contentType, partialorTotalRefundaSettlementRequest1, (error, data, response) => {
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
 **creditAccountId** | **String**| Credit account&#39;s identification | [default to &#39;insert identifier here&#39;]
 **transactionId** | **String**|  | [default to &#39;insert identifier here&#39;]
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **partialorTotalRefundaSettlementRequest1** | [**PartialorTotalRefundaSettlementRequest1**](PartialorTotalRefundaSettlementRequest1.md)|  | 

### Return type

[**ThisoperationcausesthecreationofNinvoicesWhereNisthenumberofinstallmentsThefirstinvoicewillhaveaduedatewith30daysandthenextinvoiceswillhaveaduedate30daysawayfrompreviousinvoice**](ThisoperationcausesthecreationofNinvoicesWhereNisthenumberofinstallmentsThefirstinvoicewillhaveaduedatewith30daysandthenextinvoiceswillhaveaduedate30daysawayfrompreviousinvoice.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## retrieveaAccountbyId

> Getaccount1 retrieveaAccountbyId(contentType, accept, creditAccountId)

Retrieve an Account by Id

Retrieve an account by id.

### Example

```javascript
import CustomerCreditApi from 'customer_credit_api';
let defaultClient = CustomerCreditApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new CustomerCreditApi.AccountApi();
let contentType = "'application/json'"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
let accept = "'application/json'"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let creditAccountId = "'insert identifier here'"; // String | 
apiInstance.retrieveaAccountbyId(contentType, accept, creditAccountId, (error, data, response) => {
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
 **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **creditAccountId** | **String**|  | [default to &#39;insert identifier here&#39;]

### Return type

[**Getaccount1**](Getaccount1.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## searchallaccounts

> Searchaccounts1 searchallaccounts(contentType, accept)

Search all accounts



### Example

```javascript
import CustomerCreditApi from 'customer_credit_api';
let defaultClient = CustomerCreditApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new CustomerCreditApi.AccountApi();
let contentType = "'application/json'"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
let accept = "'application/json'"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
apiInstance.searchallaccounts(contentType, accept, (error, data, response) => {
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
 **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]

### Return type

[**Searchaccounts1**](Searchaccounts1.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## updateemailanddescriptionofaaccount

> String updateemailanddescriptionofaaccount(creditAccountId, accept, contentType, updateemailanddescriptionofaaccountRequest1)

Update email and description of a account

Update a checking account.

### Example

```javascript
import CustomerCreditApi from 'customer_credit_api';
let defaultClient = CustomerCreditApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new CustomerCreditApi.AccountApi();
let creditAccountId = "'insert identifier here'"; // String | Credit account's identification
let accept = "'application/json'"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let contentType = "'application/json'"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
let updateemailanddescriptionofaaccountRequest1 = {"description":"string","email":"email"}; // UpdateemailanddescriptionofaaccountRequest1 | 
apiInstance.updateemailanddescriptionofaaccount(creditAccountId, accept, contentType, updateemailanddescriptionofaaccountRequest1, (error, data, response) => {
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
 **creditAccountId** | **String**| Credit account&#39;s identification | [default to &#39;insert identifier here&#39;]
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **updateemailanddescriptionofaaccountRequest1** | [**UpdateemailanddescriptionofaaccountRequest1**](UpdateemailanddescriptionofaaccountRequest1.md)|  | 

### Return type

**String**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8

