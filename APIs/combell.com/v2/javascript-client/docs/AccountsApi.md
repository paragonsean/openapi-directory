# PublicApi.AccountsApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createAccount**](AccountsApi.md#createAccount) | **POST** /accounts | Create a new account
[**getAccount**](AccountsApi.md#getAccount) | **GET** /accounts/{accountId} | Get a specific account
[**getAccounts**](AccountsApi.md#getAccounts) | **GET** /accounts | Overview of accounts



## createAccount

> createAccount(opts)

Create a new account

The creation of an account requires some background processing. There is no instant feedback of the creation status.

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.AccountsApi();
let opts = {
  'createAccount': new PublicApi.CreateAccount() // CreateAccount | 
};
apiInstance.createAccount(opts, (error, data, response) => {
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
 **createAccount** | [**CreateAccount**](CreateAccount.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getAccount

> AccountDetail getAccount(accountId, accountId2)

Get a specific account



### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.AccountsApi();
let accountId = 56; // Number | The id of the account.
let accountId2 = "accountId_example"; // String | Automatically added
apiInstance.getAccount(accountId, accountId2, (error, data, response) => {
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
 **accountId** | **Number**| The id of the account. | 
 **accountId2** | **String**| Automatically added | 

### Return type

[**AccountDetail**](AccountDetail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAccounts

> [Account] getAccounts(opts)

Overview of accounts

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.AccountsApi();
let opts = {
  'skip': 56, // Number | The number of items to skip in the resultset.
  'take': 56, // Number | The number of items to return in the resultset. The returned count can be equal or less than this number.
  'assetType': new PublicApi.AssetType(), // AssetType | Filters the list, returning only accounts containing the specified asset type.
  'identifier': "identifier_example" // String | Return only accounts, matching the specified identifier.
};
apiInstance.getAccounts(opts, (error, data, response) => {
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
 **skip** | **Number**| The number of items to skip in the resultset. | [optional] 
 **take** | **Number**| The number of items to return in the resultset. The returned count can be equal or less than this number. | [optional] 
 **assetType** | [**AssetType**](.md)| Filters the list, returning only accounts containing the specified asset type. | [optional] 
 **identifier** | **String**| Return only accounts, matching the specified identifier. | [optional] 

### Return type

[**[Account]**](Account.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

