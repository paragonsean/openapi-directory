# IxApi.AccountsApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountsCreate**](AccountsApi.md#accountsCreate) | **POST** /accounts | 
[**accountsDestroy**](AccountsApi.md#accountsDestroy) | **DELETE** /accounts/{id} | 
[**accountsList**](AccountsApi.md#accountsList) | **GET** /accounts | 
[**accountsPartialUpdate**](AccountsApi.md#accountsPartialUpdate) | **PATCH** /accounts/{id} | 
[**accountsRead**](AccountsApi.md#accountsRead) | **GET** /accounts/{id} | 
[**accountsUpdate**](AccountsApi.md#accountsUpdate) | **PUT** /accounts/{id} | 



## accountsCreate

> Account accountsCreate(opts)



Create a new account.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.AccountsApi();
let opts = {
  'accountRequest': new IxApi.AccountRequest() // AccountRequest | Account Request
};
apiInstance.accountsCreate(opts, (error, data, response) => {
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
 **accountRequest** | [**AccountRequest**](AccountRequest.md)| Account Request | [optional] 

### Return type

[**Account**](Account.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## accountsDestroy

> Account accountsDestroy(id)



Accounts can be deleted, when all services and configs are decommissioned or the account is not longer referenced e.g. as a &#x60;managing_account&#x60; or &#x60;billing_account&#x60;.  Deleting an account will cascade to &#x60;contacts&#x60; and &#x60;role-assignments&#x60;.  The request will immediately fail, if the above preconditions are not met.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.AccountsApi();
let id = "id_example"; // String | Get by id
apiInstance.accountsDestroy(id, (error, data, response) => {
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
 **id** | **String**| Get by id | 

### Return type

[**Account**](Account.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsList

> [Account] accountsList(opts)



Retrieve a list of &#x60;Account&#x60;s.  This includes all accounts the currently authorized account is managing and the current account itself.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.AccountsApi();
let opts = {
  'id': ["null"], // [String] | Filter by id
  'state': "state_example", // String | Filter by state
  'stateIsNot': "stateIsNot_example", // String | Filter by state__is_not
  'managingAccount': "managingAccount_example", // String | Filter by managing_account
  'billable': 56, // Number | Filter by billable
  'externalRef': "externalRef_example", // String | Filter by external_ref
  'name': "name_example" // String | Filter by name
};
apiInstance.accountsList(opts, (error, data, response) => {
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
 **id** | [**[String]**](String.md)| Filter by id | [optional] 
 **state** | **String**| Filter by state | [optional] 
 **stateIsNot** | **String**| Filter by state__is_not | [optional] 
 **managingAccount** | **String**| Filter by managing_account | [optional] 
 **billable** | **Number**| Filter by billable | [optional] 
 **externalRef** | **String**| Filter by external_ref | [optional] 
 **name** | **String**| Filter by name | [optional] 

### Return type

[**[Account]**](Account.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsPartialUpdate

> Account accountsPartialUpdate(id, opts)



Update parts of an account.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.AccountsApi();
let id = "id_example"; // String | Get by id
let opts = {
  'accountUpdatePartial': new IxApi.AccountUpdatePartial() // AccountUpdatePartial | Account Update Request
};
apiInstance.accountsPartialUpdate(id, opts, (error, data, response) => {
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
 **id** | **String**| Get by id | 
 **accountUpdatePartial** | [**AccountUpdatePartial**](AccountUpdatePartial.md)| Account Update Request | [optional] 

### Return type

[**Account**](Account.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json


## accountsRead

> Account accountsRead(id)



Get a single account.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.AccountsApi();
let id = "id_example"; // String | Get by id
apiInstance.accountsRead(id, (error, data, response) => {
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
 **id** | **String**| Get by id | 

### Return type

[**Account**](Account.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsUpdate

> Account accountsUpdate(id, opts)



Update the entire account.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.AccountsApi();
let id = "id_example"; // String | Get by id
let opts = {
  'accountUpdate': new IxApi.AccountUpdate() // AccountUpdate | Account Update Request
};
apiInstance.accountsUpdate(id, opts, (error, data, response) => {
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
 **id** | **String**| Get by id | 
 **accountUpdate** | [**AccountUpdate**](AccountUpdate.md)| Account Update Request | [optional] 

### Return type

[**Account**](Account.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

