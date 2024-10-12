# UpApi.AccountsApi

All URIs are relative to *https://api.up.com.au/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountsGet**](AccountsApi.md#accountsGet) | **GET** /accounts | List accounts
[**accountsIdGet**](AccountsApi.md#accountsIdGet) | **GET** /accounts/{id} | Retrieve account



## accountsGet

> ListAccountsResponse accountsGet(opts)

List accounts

Retrieve a paginated list of all accounts for the currently authenticated user. The returned list is paginated and can be scrolled by following the &#x60;prev&#x60; and &#x60;next&#x60; links where present. 

### Example

```javascript
import UpApi from 'up_api';
let defaultClient = UpApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new UpApi.AccountsApi();
let opts = {
  'pageSize': 30, // Number | The number of records to return in each page. 
  'filterAccountType': new UpApi.AccountTypeEnum(), // AccountTypeEnum | The type of account for which to return records. This can be used to filter Savers from spending accounts. 
  'filterOwnershipType': new UpApi.OwnershipTypeEnum() // OwnershipTypeEnum | The account ownership structure for which to return records. This can be used to filter 2Up accounts from Up accounts. 
};
apiInstance.accountsGet(opts, (error, data, response) => {
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
 **pageSize** | **Number**| The number of records to return in each page.  | [optional] 
 **filterAccountType** | [**AccountTypeEnum**](.md)| The type of account for which to return records. This can be used to filter Savers from spending accounts.  | [optional] 
 **filterOwnershipType** | [**OwnershipTypeEnum**](.md)| The account ownership structure for which to return records. This can be used to filter 2Up accounts from Up accounts.  | [optional] 

### Return type

[**ListAccountsResponse**](ListAccountsResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsIdGet

> GetAccountResponse accountsIdGet(id)

Retrieve account

Retrieve a specific account by providing its unique identifier. 

### Example

```javascript
import UpApi from 'up_api';
let defaultClient = UpApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new UpApi.AccountsApi();
let id = "92b41408-6b7b-4fca-982b-3fb1fdd77220"; // String | The unique identifier for the account. 
apiInstance.accountsIdGet(id, (error, data, response) => {
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
 **id** | **String**| The unique identifier for the account.  | 

### Return type

[**GetAccountResponse**](GetAccountResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

