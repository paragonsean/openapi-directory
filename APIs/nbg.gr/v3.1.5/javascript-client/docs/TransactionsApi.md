# AccountAndTransactionApiSpecificationUk.TransactionsApi

All URIs are relative to *https://apis.nbg.gr/sandbox/uk.openbanking.accountinfo/oauth2/v3.1.5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountsAccountIdStatementsStatementIdTransactionsGet**](TransactionsApi.md#accountsAccountIdStatementsStatementIdTransactionsGet) | **GET** /accounts/{accountId}/statements/{statementId}/transactions | Get Transactions
[**accountsAccountIdTransactionsGet**](TransactionsApi.md#accountsAccountIdTransactionsGet) | **GET** /accounts/{accountId}/transactions | Get Transactions



## accountsAccountIdStatementsStatementIdTransactionsGet

> OBReadTransaction6 accountsAccountIdStatementsStatementIdTransactionsGet(accountId, statementId, sandboxId, opts)

Get Transactions

Get Transactions by Account ID and Statement ID

### Example

```javascript
import AccountAndTransactionApiSpecificationUk from 'account_and_transaction_api_specification_uk';
let defaultClient = AccountAndTransactionApiSpecificationUk.ApiClient.instance;
// Configure OAuth2 access token for authorization: Authorization-Code-Token
let Authorization-Code-Token = defaultClient.authentications['Authorization-Code-Token'];
Authorization-Code-Token.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: Client-Id
let Client-Id = defaultClient.authentications['Client-Id'];
Client-Id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Client-Id.apiKeyPrefix = 'Token';

let apiInstance = new AccountAndTransactionApiSpecificationUk.TransactionsApi();
let accountId = "accountId_example"; // String | AccountId
let statementId = "statementId_example"; // String | StatementId
let sandboxId = "sandboxId_example"; // String | The unique id of the sandbox to be used
let opts = {
  'xFapiAuthDate': "xFapiAuthDate_example", // String | The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC
  'xFapiCustomerIpAddress': "xFapiCustomerIpAddress_example", // String | The PSU's IP address if the PSU is currently logged in with the TPP.
  'xFapiInteractionId': "xFapiInteractionId_example", // String | An RFC4122 UID used as a correlation id.
  'xCustomerUserAgent': "xCustomerUserAgent_example" // String | Indicates the user-agent that the PSU is using.
};
apiInstance.accountsAccountIdStatementsStatementIdTransactionsGet(accountId, statementId, sandboxId, opts, (error, data, response) => {
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
 **accountId** | **String**| AccountId | 
 **statementId** | **String**| StatementId | 
 **sandboxId** | **String**| The unique id of the sandbox to be used | 
 **xFapiAuthDate** | **String**| The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **xFapiCustomerIpAddress** | **String**| The PSU&#39;s IP address if the PSU is currently logged in with the TPP. | [optional] 
 **xFapiInteractionId** | **String**| An RFC4122 UID used as a correlation id. | [optional] 
 **xCustomerUserAgent** | **String**| Indicates the user-agent that the PSU is using. | [optional] 

### Return type

[**OBReadTransaction6**](OBReadTransaction6.md)

### Authorization

[Authorization-Code-Token](../README.md#Authorization-Code-Token), [Client-Id](../README.md#Client-Id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; charset=utf-8


## accountsAccountIdTransactionsGet

> OBReadTransaction6 accountsAccountIdTransactionsGet(accountId, sandboxId, opts)

Get Transactions

Get Transactions by Account ID

### Example

```javascript
import AccountAndTransactionApiSpecificationUk from 'account_and_transaction_api_specification_uk';
let defaultClient = AccountAndTransactionApiSpecificationUk.ApiClient.instance;
// Configure OAuth2 access token for authorization: Authorization-Code-Token
let Authorization-Code-Token = defaultClient.authentications['Authorization-Code-Token'];
Authorization-Code-Token.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: Client-Id
let Client-Id = defaultClient.authentications['Client-Id'];
Client-Id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Client-Id.apiKeyPrefix = 'Token';

let apiInstance = new AccountAndTransactionApiSpecificationUk.TransactionsApi();
let accountId = "accountId_example"; // String | AccountId
let sandboxId = "sandboxId_example"; // String | The unique id of the sandbox to be used
let opts = {
  'fromBookingDateTime': new Date("2013-10-20T19:20:30+01:00"), // Date | The UTC ISO 8601 Date Time to filter transactions FROM NB Time component is optional - set to 00:00:00 for just Date. If the Date Time contains a timezone, the ASPSP must ignore the timezone component.
  'toBookingDateTime': new Date("2013-10-20T19:20:30+01:00"), // Date | The UTC ISO 8601 Date Time to filter transactions TO NB Time component is optional - set to 00:00:00 for just Date. If the Date Time contains a timezone, the ASPSP must ignore the timezone component.
  'xFapiAuthDate': "xFapiAuthDate_example", // String | The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC
  'xFapiCustomerIpAddress': "xFapiCustomerIpAddress_example", // String | The PSU's IP address if the PSU is currently logged in with the TPP.
  'xFapiInteractionId': "xFapiInteractionId_example", // String | An RFC4122 UID used as a correlation id.
  'xCustomerUserAgent': "xCustomerUserAgent_example" // String | Indicates the user-agent that the PSU is using.
};
apiInstance.accountsAccountIdTransactionsGet(accountId, sandboxId, opts, (error, data, response) => {
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
 **accountId** | **String**| AccountId | 
 **sandboxId** | **String**| The unique id of the sandbox to be used | 
 **fromBookingDateTime** | **Date**| The UTC ISO 8601 Date Time to filter transactions FROM NB Time component is optional - set to 00:00:00 for just Date. If the Date Time contains a timezone, the ASPSP must ignore the timezone component. | [optional] 
 **toBookingDateTime** | **Date**| The UTC ISO 8601 Date Time to filter transactions TO NB Time component is optional - set to 00:00:00 for just Date. If the Date Time contains a timezone, the ASPSP must ignore the timezone component. | [optional] 
 **xFapiAuthDate** | **String**| The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **xFapiCustomerIpAddress** | **String**| The PSU&#39;s IP address if the PSU is currently logged in with the TPP. | [optional] 
 **xFapiInteractionId** | **String**| An RFC4122 UID used as a correlation id. | [optional] 
 **xCustomerUserAgent** | **String**| Indicates the user-agent that the PSU is using. | [optional] 

### Return type

[**OBReadTransaction6**](OBReadTransaction6.md)

### Authorization

[Authorization-Code-Token](../README.md#Authorization-Code-Token), [Client-Id](../README.md#Client-Id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; charset=utf-8

