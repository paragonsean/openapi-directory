# OpenChannelMarketApi.UserAccountsFindAndModifyUserAccountsApi

All URIs are relative to *https://market.openchannel.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**userAccountsGet**](UserAccountsFindAndModifyUserAccountsApi.md#userAccountsGet) | **GET** /userAccounts | Returns a paginated list of userAccounts
[**userAccountsUserAccountIdDelete**](UserAccountsFindAndModifyUserAccountsApi.md#userAccountsUserAccountIdDelete) | **DELETE** /userAccounts/{userAccountId} | Removes the user account
[**userAccountsUserAccountIdGet**](UserAccountsFindAndModifyUserAccountsApi.md#userAccountsUserAccountIdGet) | **GET** /userAccounts/{userAccountId} | Returns a single user account
[**userAccountsUserAccountIdPatch**](UserAccountsFindAndModifyUserAccountsApi.md#userAccountsUserAccountIdPatch) | **PATCH** /userAccounts/{userAccountId} | Updates the user account fields
[**userAccountsUserAccountIdPost**](UserAccountsFindAndModifyUserAccountsApi.md#userAccountsUserAccountIdPost) | **POST** /userAccounts/{userAccountId} | Updates the user account or adds the user account if it doesn&#39;t exist



## userAccountsGet

> UserAccountPages userAccountsGet(opts)

Returns a paginated list of userAccounts

- Results are paginated and the default is value is 1000 if no limit is provided 

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.UserAccountsFindAndModifyUserAccountsApi();
let opts = {
  'query': "query_example", // String | A query document. Example: {'name':'NASA'} matches all the userAccounts that have the name 'NASA'
  'sort': "sort_example", // String | A sort document. Example: {'name':1} sorts the results by name in ascending order
  'pageNumber': 56, // Number | The result set page number to be returned
  'limit': 56 // Number | The maximum number of results to return per page
};
apiInstance.userAccountsGet(opts, (error, data, response) => {
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
 **query** | **String**| A query document. Example: {&#39;name&#39;:&#39;NASA&#39;} matches all the userAccounts that have the name &#39;NASA&#39; | [optional] 
 **sort** | **String**| A sort document. Example: {&#39;name&#39;:1} sorts the results by name in ascending order | [optional] 
 **pageNumber** | **Number**| The result set page number to be returned | [optional] 
 **limit** | **Number**| The maximum number of results to return per page | [optional] 

### Return type

[**UserAccountPages**](UserAccountPages.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## userAccountsUserAccountIdDelete

> userAccountsUserAccountIdDelete(userAccountId)

Removes the user account

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.UserAccountsFindAndModifyUserAccountsApi();
let userAccountId = "userAccountId_example"; // String | The id of the user account to be removed
apiInstance.userAccountsUserAccountIdDelete(userAccountId, (error, data, response) => {
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
 **userAccountId** | **String**| The id of the user account to be removed | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## userAccountsUserAccountIdGet

> UserAccount userAccountsUserAccountIdGet(userAccountId)

Returns a single user account

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.UserAccountsFindAndModifyUserAccountsApi();
let userAccountId = "userAccountId_example"; // String | The id of the user account to be located
apiInstance.userAccountsUserAccountIdGet(userAccountId, (error, data, response) => {
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
 **userAccountId** | **String**| The id of the user account to be located | 

### Return type

[**UserAccount**](UserAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## userAccountsUserAccountIdPatch

> UserAccount userAccountsUserAccountIdPatch(userAccountId, userId, opts)

Updates the user account fields

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.UserAccountsFindAndModifyUserAccountsApi();
let userAccountId = "userAccountId_example"; // String | The id of the user account to be updated
let userId = "userId_example"; // String | The Id of the user that this account belongs to
let opts = {
  'email': "email_example", // String | The contact email address
  'name': "name_example", // String | The user account name
  'customData': "customData_example" // String | A custom JSON object that you can create and attach to this record
};
apiInstance.userAccountsUserAccountIdPatch(userAccountId, userId, opts, (error, data, response) => {
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
 **userAccountId** | **String**| The id of the user account to be updated | 
 **userId** | **String**| The Id of the user that this account belongs to | 
 **email** | **String**| The contact email address | [optional] 
 **name** | **String**| The user account name | [optional] 
 **customData** | **String**| A custom JSON object that you can create and attach to this record | [optional] 

### Return type

[**UserAccount**](UserAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## userAccountsUserAccountIdPost

> UserAccount userAccountsUserAccountIdPost(userAccountId, userId, opts)

Updates the user account or adds the user account if it doesn&#39;t exist

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.UserAccountsFindAndModifyUserAccountsApi();
let userAccountId = "userAccountId_example"; // String | The id of the user account to be updated
let userId = "userId_example"; // String | The Id of the user that this account belongs to
let opts = {
  'email': "email_example", // String | The contact email address
  'name': "name_example", // String | The user account name
  'customData': "customData_example" // String | A custom JSON object that you can create and attach to this record
};
apiInstance.userAccountsUserAccountIdPost(userAccountId, userId, opts, (error, data, response) => {
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
 **userAccountId** | **String**| The id of the user account to be updated | 
 **userId** | **String**| The Id of the user that this account belongs to | 
 **email** | **String**| The contact email address | [optional] 
 **name** | **String**| The user account name | [optional] 
 **customData** | **String**| A custom JSON object that you can create and attach to this record | [optional] 

### Return type

[**UserAccount**](UserAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

