# RebillyRestApi.BankAccountsApi

All URIs are relative to *https://api-sandbox.rebilly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getBankAccount**](BankAccountsApi.md#getBankAccount) | **GET** /bank-accounts/{id} | Retrieve a Bank Account
[**getBankAccountCollection**](BankAccountsApi.md#getBankAccountCollection) | **GET** /bank-accounts | Retrieve a list of bank accounts
[**patchBankAccount**](BankAccountsApi.md#patchBankAccount) | **PATCH** /bank-accounts/{id} | Update a bank account&#39;s values
[**postBankAccount**](BankAccountsApi.md#postBankAccount) | **POST** /bank-accounts | Create a Bank Account
[**postBankAccountDeactivation**](BankAccountsApi.md#postBankAccountDeactivation) | **POST** /bank-accounts/{id}/deactivation | Deactivate a Bank Account
[**putBankAccount**](BankAccountsApi.md#putBankAccount) | **PUT** /bank-accounts/{id} | Create a Bank Account with predefined ID



## getBankAccount

> BankAccount getBankAccount(id, opts)

Retrieve a Bank Account

Retrieve a Bank Account with specified identifier string. 

### Example

```javascript
import RebillyRestApi from 'rebilly_rest_api';
let defaultClient = RebillyRestApi.ApiClient.instance;
// Configure API key authorization: SecretApiKey
let SecretApiKey = defaultClient.authentications['SecretApiKey'];
SecretApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//SecretApiKey.apiKeyPrefix = 'Token';
// Configure Bearer (JWT) access token for authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new RebillyRestApi.BankAccountsApi();
let id = "id_example"; // String | The resource identifier string.
let opts = {
  'organizationId': "organizationId_example" // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
};
apiInstance.getBankAccount(id, opts, (error, data, response) => {
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
 **id** | **String**| The resource identifier string. | 
 **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] 

### Return type

[**BankAccount**](BankAccount.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBankAccountCollection

> [BankAccount] getBankAccountCollection(opts)

Retrieve a list of bank accounts

Retrieve a list of Bank Accounts. 

### Example

```javascript
import RebillyRestApi from 'rebilly_rest_api';
let defaultClient = RebillyRestApi.ApiClient.instance;
// Configure API key authorization: SecretApiKey
let SecretApiKey = defaultClient.authentications['SecretApiKey'];
SecretApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//SecretApiKey.apiKeyPrefix = 'Token';
// Configure Bearer (JWT) access token for authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new RebillyRestApi.BankAccountsApi();
let opts = {
  'organizationId': "organizationId_example", // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
  'limit': 56, // Number | The collection items limit.
  'offset': 56, // Number | The collection items offset.
  'q': "q_example", // String | The partial search of the text fields.
  'sort': ["null"], // [String] | The collection items sort field and order (prefix with \"-\" for descending sort).
  'filter': "filter_example", // String | The collection items filter requires a special format. Use \",\" for multiple allowed values.  Use \";\" for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format. 
  'expand': "expand_example" // String | Expand a response to get a full related object included inside of the `_embedded` path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info. 
};
apiInstance.getBankAccountCollection(opts, (error, data, response) => {
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
 **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] 
 **limit** | **Number**| The collection items limit. | [optional] 
 **offset** | **Number**| The collection items offset. | [optional] 
 **q** | **String**| The partial search of the text fields. | [optional] 
 **sort** | [**[String]**](String.md)| The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). | [optional] 
 **filter** | **String**| The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  | [optional] 
 **expand** | **String**| Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  | [optional] 

### Return type

[**[BankAccount]**](BankAccount.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchBankAccount

> BankAccount patchBankAccount(id, opts)

Update a bank account&#39;s values

Update bank account&#39;s values except for the account number and routing. number. 

### Example

```javascript
import RebillyRestApi from 'rebilly_rest_api';
let defaultClient = RebillyRestApi.ApiClient.instance;
// Configure API key authorization: SecretApiKey
let SecretApiKey = defaultClient.authentications['SecretApiKey'];
SecretApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//SecretApiKey.apiKeyPrefix = 'Token';
// Configure Bearer (JWT) access token for authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new RebillyRestApi.BankAccountsApi();
let id = "id_example"; // String | The resource identifier string.
let opts = {
  'organizationId': "organizationId_example", // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
  'bankAccountUpdatePlain': new RebillyRestApi.BankAccountUpdatePlain() // BankAccountUpdatePlain | Bank Account.
};
apiInstance.patchBankAccount(id, opts, (error, data, response) => {
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
 **id** | **String**| The resource identifier string. | 
 **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] 
 **bankAccountUpdatePlain** | [**BankAccountUpdatePlain**](BankAccountUpdatePlain.md)| Bank Account. | [optional] 

### Return type

[**BankAccount**](BankAccount.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postBankAccount

> BankAccount postBankAccount(postBankAccountRequest, opts)

Create a Bank Account

Create a Bank Account. 

### Example

```javascript
import RebillyRestApi from 'rebilly_rest_api';
let defaultClient = RebillyRestApi.ApiClient.instance;
// Configure API key authorization: SecretApiKey
let SecretApiKey = defaultClient.authentications['SecretApiKey'];
SecretApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//SecretApiKey.apiKeyPrefix = 'Token';
// Configure Bearer (JWT) access token for authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new RebillyRestApi.BankAccountsApi();
let postBankAccountRequest = new RebillyRestApi.PostBankAccountRequest(); // PostBankAccountRequest | BankAccount resource.
let opts = {
  'organizationId': "organizationId_example" // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
};
apiInstance.postBankAccount(postBankAccountRequest, opts, (error, data, response) => {
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
 **postBankAccountRequest** | [**PostBankAccountRequest**](PostBankAccountRequest.md)| BankAccount resource. | 
 **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] 

### Return type

[**BankAccount**](BankAccount.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postBankAccountDeactivation

> BankAccount postBankAccountDeactivation(id, opts)

Deactivate a Bank Account

Deactivate a Bank Account. 

### Example

```javascript
import RebillyRestApi from 'rebilly_rest_api';
let defaultClient = RebillyRestApi.ApiClient.instance;
// Configure API key authorization: SecretApiKey
let SecretApiKey = defaultClient.authentications['SecretApiKey'];
SecretApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//SecretApiKey.apiKeyPrefix = 'Token';
// Configure Bearer (JWT) access token for authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new RebillyRestApi.BankAccountsApi();
let id = "id_example"; // String | The resource identifier string.
let opts = {
  'organizationId': "organizationId_example" // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
};
apiInstance.postBankAccountDeactivation(id, opts, (error, data, response) => {
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
 **id** | **String**| The resource identifier string. | 
 **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] 

### Return type

[**BankAccount**](BankAccount.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putBankAccount

> BankAccount putBankAccount(id, postBankAccountRequest, opts)

Create a Bank Account with predefined ID

Create or update a BankAccount with predefined identifier string. 

### Example

```javascript
import RebillyRestApi from 'rebilly_rest_api';
let defaultClient = RebillyRestApi.ApiClient.instance;
// Configure API key authorization: SecretApiKey
let SecretApiKey = defaultClient.authentications['SecretApiKey'];
SecretApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//SecretApiKey.apiKeyPrefix = 'Token';
// Configure Bearer (JWT) access token for authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new RebillyRestApi.BankAccountsApi();
let id = "id_example"; // String | The resource identifier string.
let postBankAccountRequest = new RebillyRestApi.PostBankAccountRequest(); // PostBankAccountRequest | BankAccount resource.
let opts = {
  'organizationId': "organizationId_example" // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
};
apiInstance.putBankAccount(id, postBankAccountRequest, opts, (error, data, response) => {
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
 **id** | **String**| The resource identifier string. | 
 **postBankAccountRequest** | [**PostBankAccountRequest**](PostBankAccountRequest.md)| BankAccount resource. | 
 **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] 

### Return type

[**BankAccount**](BankAccount.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

