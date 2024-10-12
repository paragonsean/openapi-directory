# AccountApi.AccountHoldersApi

All URIs are relative to *https://cal-test.adyen.com/cal/services/Account/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postCloseAccountHolder**](AccountHoldersApi.md#postCloseAccountHolder) | **POST** /closeAccountHolder | Close an account holder
[**postCreateAccountHolder**](AccountHoldersApi.md#postCreateAccountHolder) | **POST** /createAccountHolder | Create an account holder
[**postGetAccountHolder**](AccountHoldersApi.md#postGetAccountHolder) | **POST** /getAccountHolder | Get an account holder
[**postGetTaxForm**](AccountHoldersApi.md#postGetTaxForm) | **POST** /getTaxForm | Get a tax form
[**postSuspendAccountHolder**](AccountHoldersApi.md#postSuspendAccountHolder) | **POST** /suspendAccountHolder | Suspend an account holder
[**postUnSuspendAccountHolder**](AccountHoldersApi.md#postUnSuspendAccountHolder) | **POST** /unSuspendAccountHolder | Unsuspend an account holder
[**postUpdateAccountHolder**](AccountHoldersApi.md#postUpdateAccountHolder) | **POST** /updateAccountHolder | Update an account holder
[**postUpdateAccountHolderState**](AccountHoldersApi.md#postUpdateAccountHolderState) | **POST** /updateAccountHolderState | Update payout or processing state



## postCloseAccountHolder

> CloseAccountHolderResponse postCloseAccountHolder(opts)

Close an account holder

Changes the [status of an account holder](https://docs.adyen.com/marketplaces-and-platforms/classic/account-holders-and-accounts#account-holder-statuses) to **Closed**. This state is final. If an account holder is closed, you can&#39;t process transactions, pay out funds, or reopen it. If payments are made to an account of an account holder with a **Closed** [&#x60;status&#x60;](https://docs.adyen.com/api-explorer/#/Account/latest/post/getAccountHolder__resParam_verification-accountHolder-checks-status), the payments are sent to your liable account.

### Example

```javascript
import AccountApi from 'account_api';
let defaultClient = AccountApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AccountApi.AccountHoldersApi();
let opts = {
  'closeAccountHolderRequest': new AccountApi.CloseAccountHolderRequest() // CloseAccountHolderRequest | 
};
apiInstance.postCloseAccountHolder(opts, (error, data, response) => {
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
 **closeAccountHolderRequest** | [**CloseAccountHolderRequest**](CloseAccountHolderRequest.md)|  | [optional] 

### Return type

[**CloseAccountHolderResponse**](CloseAccountHolderResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postCreateAccountHolder

> CreateAccountHolderResponse postCreateAccountHolder(opts)

Create an account holder

Creates an account holder that [represents the sub-merchant&#39;s entity](https://docs.adyen.com/marketplaces-and-platforms/classic/account-structure#your-platform) in your platform. The details that you need to provide in the request depend on the sub-merchant&#39;s legal entity type. For more information, refer to [Account holder and accounts](https://docs.adyen.com/marketplaces-and-platforms/classic/account-holders-and-accounts#legal-entity-types).

### Example

```javascript
import AccountApi from 'account_api';
let defaultClient = AccountApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AccountApi.AccountHoldersApi();
let opts = {
  'createAccountHolderRequest': new AccountApi.CreateAccountHolderRequest() // CreateAccountHolderRequest | 
};
apiInstance.postCreateAccountHolder(opts, (error, data, response) => {
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
 **createAccountHolderRequest** | [**CreateAccountHolderRequest**](CreateAccountHolderRequest.md)|  | [optional] 

### Return type

[**CreateAccountHolderResponse**](CreateAccountHolderResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postGetAccountHolder

> GetAccountHolderResponse postGetAccountHolder(opts)

Get an account holder

Returns the details of an account holder.

### Example

```javascript
import AccountApi from 'account_api';
let defaultClient = AccountApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AccountApi.AccountHoldersApi();
let opts = {
  'getAccountHolderRequest': new AccountApi.GetAccountHolderRequest() // GetAccountHolderRequest | 
};
apiInstance.postGetAccountHolder(opts, (error, data, response) => {
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
 **getAccountHolderRequest** | [**GetAccountHolderRequest**](GetAccountHolderRequest.md)|  | [optional] 

### Return type

[**GetAccountHolderResponse**](GetAccountHolderResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postGetTaxForm

> GetTaxFormResponse postGetTaxForm(opts)

Get a tax form

Generates a tax form for account holders operating in the US. For more information, refer to [Providing tax forms](https://docs.adyen.com/marketplaces-and-platforms/classic/tax-forms).

### Example

```javascript
import AccountApi from 'account_api';
let defaultClient = AccountApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AccountApi.AccountHoldersApi();
let opts = {
  'getTaxFormRequest': new AccountApi.GetTaxFormRequest() // GetTaxFormRequest | 
};
apiInstance.postGetTaxForm(opts, (error, data, response) => {
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
 **getTaxFormRequest** | [**GetTaxFormRequest**](GetTaxFormRequest.md)|  | [optional] 

### Return type

[**GetTaxFormResponse**](GetTaxFormResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postSuspendAccountHolder

> SuspendAccountHolderResponse postSuspendAccountHolder(opts)

Suspend an account holder

Changes the [status of an account holder](https://docs.adyen.com/marketplaces-and-platforms/classic/account-holders-and-accounts#account-holder-statuses) to **Suspended**.

### Example

```javascript
import AccountApi from 'account_api';
let defaultClient = AccountApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AccountApi.AccountHoldersApi();
let opts = {
  'suspendAccountHolderRequest': new AccountApi.SuspendAccountHolderRequest() // SuspendAccountHolderRequest | 
};
apiInstance.postSuspendAccountHolder(opts, (error, data, response) => {
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
 **suspendAccountHolderRequest** | [**SuspendAccountHolderRequest**](SuspendAccountHolderRequest.md)|  | [optional] 

### Return type

[**SuspendAccountHolderResponse**](SuspendAccountHolderResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postUnSuspendAccountHolder

> UnSuspendAccountHolderResponse postUnSuspendAccountHolder(opts)

Unsuspend an account holder

Changes the [status of an account holder](https://docs.adyen.com/marketplaces-and-platforms/classic/account-holders-and-accounts#account-holder-statuses) from **Suspended** to **Inactive**.  Account holders can have a **Suspended** [&#x60;status&#x60;](https://docs.adyen.com/api-explorer/#/Account/latest/post/getAccountHolder__resParam_verification-accountHolder-checks-status) if you suspend them through the [&#x60;/suspendAccountHolder&#x60;](https://docs.adyen.com/api-explorer/#/Account/v5/post/suspendAccountHolder) endpoint or if a verification deadline expires.  You can only unsuspend account holders if they do not have verification checks with a **FAILED** [&#x60;status&#x60;](https://docs.adyen.com/api-explorer/#/Account/latest/post/getAccountHolder__resParam_verification-accountHolder-checks-status).

### Example

```javascript
import AccountApi from 'account_api';
let defaultClient = AccountApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AccountApi.AccountHoldersApi();
let opts = {
  'unSuspendAccountHolderRequest': new AccountApi.UnSuspendAccountHolderRequest() // UnSuspendAccountHolderRequest | 
};
apiInstance.postUnSuspendAccountHolder(opts, (error, data, response) => {
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
 **unSuspendAccountHolderRequest** | [**UnSuspendAccountHolderRequest**](UnSuspendAccountHolderRequest.md)|  | [optional] 

### Return type

[**UnSuspendAccountHolderResponse**](UnSuspendAccountHolderResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postUpdateAccountHolder

> UpdateAccountHolderResponse postUpdateAccountHolder(opts)

Update an account holder

Updates the &#x60;accountHolderDetails&#x60; and &#x60;processingTier&#x60; of an account holder, and adds bank accounts and shareholders.  When updating &#x60;accountHolderDetails&#x60;, parameters that are not included in the request are left unchanged except for the following object:  * &#x60;metadata&#x60;: Updating the metadata replaces the entire object. This means that to update an existing key-value pair, you must provide the changes, as well as other existing key-value pairs.  When updating any field in the following objects, you must submit all the fields required for validation:   * &#x60;address&#x60;  * &#x60;fullPhoneNumber&#x60;  * &#x60;bankAccountDetails.BankAccountDetail&#x60;  * &#x60;businessDetails.shareholders.ShareholderContact&#x60;   For example, to update the &#x60;address.postalCode&#x60;, you must also submit the &#x60;address.country&#x60;, &#x60;.city&#x60;, &#x60;.street&#x60;, &#x60;.postalCode&#x60;, and possibly &#x60;.stateOrProvince&#x60; so that the address can be validated.  To add a bank account or shareholder, provide the bank account or shareholder details without a &#x60;bankAccountUUID&#x60; or a &#x60;shareholderCode&#x60;.  

### Example

```javascript
import AccountApi from 'account_api';
let defaultClient = AccountApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AccountApi.AccountHoldersApi();
let opts = {
  'updateAccountHolderRequest': new AccountApi.UpdateAccountHolderRequest() // UpdateAccountHolderRequest | 
};
apiInstance.postUpdateAccountHolder(opts, (error, data, response) => {
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
 **updateAccountHolderRequest** | [**UpdateAccountHolderRequest**](UpdateAccountHolderRequest.md)|  | [optional] 

### Return type

[**UpdateAccountHolderResponse**](UpdateAccountHolderResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postUpdateAccountHolderState

> GetAccountHolderStatusResponse postUpdateAccountHolderState(opts)

Update payout or processing state

Disables or enables the processing or payout state of an account holder.

### Example

```javascript
import AccountApi from 'account_api';
let defaultClient = AccountApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AccountApi.AccountHoldersApi();
let opts = {
  'updateAccountHolderStateRequest': new AccountApi.UpdateAccountHolderStateRequest() // UpdateAccountHolderStateRequest | 
};
apiInstance.postUpdateAccountHolderState(opts, (error, data, response) => {
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
 **updateAccountHolderStateRequest** | [**UpdateAccountHolderStateRequest**](UpdateAccountHolderStateRequest.md)|  | [optional] 

### Return type

[**GetAccountHolderStatusResponse**](GetAccountHolderStatusResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

