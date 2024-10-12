# OpenChannelMarketApi.DeveloperAccountsFindAndModifyDeveloperAccountsApi

All URIs are relative to *https://market.openchannel.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**developerAccountsDeveloperAccountIdDelete**](DeveloperAccountsFindAndModifyDeveloperAccountsApi.md#developerAccountsDeveloperAccountIdDelete) | **DELETE** /developerAccounts/{developerAccountId} | Removes the developer account
[**developerAccountsDeveloperAccountIdGet**](DeveloperAccountsFindAndModifyDeveloperAccountsApi.md#developerAccountsDeveloperAccountIdGet) | **GET** /developerAccounts/{developerAccountId} | Returns a single developer account
[**developerAccountsDeveloperAccountIdPatch**](DeveloperAccountsFindAndModifyDeveloperAccountsApi.md#developerAccountsDeveloperAccountIdPatch) | **PATCH** /developerAccounts/{developerAccountId} | Updates the developer account fields
[**developerAccountsDeveloperAccountIdPost**](DeveloperAccountsFindAndModifyDeveloperAccountsApi.md#developerAccountsDeveloperAccountIdPost) | **POST** /developerAccounts/{developerAccountId} | Updates the developer account or adds the developer account if it doesn&#39;t exist
[**developerAccountsGet**](DeveloperAccountsFindAndModifyDeveloperAccountsApi.md#developerAccountsGet) | **GET** /developerAccounts | Returns a paginated list of developerAccounts



## developerAccountsDeveloperAccountIdDelete

> developerAccountsDeveloperAccountIdDelete(developerAccountId)

Removes the developer account

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.DeveloperAccountsFindAndModifyDeveloperAccountsApi();
let developerAccountId = "developerAccountId_example"; // String | The id of the developer account to be updated
apiInstance.developerAccountsDeveloperAccountIdDelete(developerAccountId, (error, data, response) => {
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
 **developerAccountId** | **String**| The id of the developer account to be updated | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## developerAccountsDeveloperAccountIdGet

> DeveloperAccount developerAccountsDeveloperAccountIdGet(developerAccountId)

Returns a single developer account

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.DeveloperAccountsFindAndModifyDeveloperAccountsApi();
let developerAccountId = "developerAccountId_example"; // String | The id of the developer account to be located
apiInstance.developerAccountsDeveloperAccountIdGet(developerAccountId, (error, data, response) => {
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
 **developerAccountId** | **String**| The id of the developer account to be located | 

### Return type

[**DeveloperAccount**](DeveloperAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## developerAccountsDeveloperAccountIdPatch

> DeveloperAccount developerAccountsDeveloperAccountIdPatch(developerAccountId, developerId, opts)

Updates the developer account fields

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.DeveloperAccountsFindAndModifyDeveloperAccountsApi();
let developerAccountId = "developerAccountId_example"; // String | The id of the developer account to be updated
let developerId = "developerId_example"; // String | The id of the developer that this account belongs to
let opts = {
  'email': "email_example", // String | The contact email address
  'name': "name_example", // String | The name for the account
  'customData': "customData_example" // String | A custom JSON object that you can create and attach to this record
};
apiInstance.developerAccountsDeveloperAccountIdPatch(developerAccountId, developerId, opts, (error, data, response) => {
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
 **developerAccountId** | **String**| The id of the developer account to be updated | 
 **developerId** | **String**| The id of the developer that this account belongs to | 
 **email** | **String**| The contact email address | [optional] 
 **name** | **String**| The name for the account | [optional] 
 **customData** | **String**| A custom JSON object that you can create and attach to this record | [optional] 

### Return type

[**DeveloperAccount**](DeveloperAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## developerAccountsDeveloperAccountIdPost

> DeveloperAccount developerAccountsDeveloperAccountIdPost(developerAccountId, developerId, opts)

Updates the developer account or adds the developer account if it doesn&#39;t exist

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.DeveloperAccountsFindAndModifyDeveloperAccountsApi();
let developerAccountId = "developerAccountId_example"; // String | The id of the developer account to be updated
let developerId = "developerId_example"; // String | The id of the developer that this account belongs to
let opts = {
  'email': "email_example", // String | The contact email address
  'name': "name_example", // String | The name for the account
  'customData': "customData_example" // String | A custom JSON object that you can create and attach to this record
};
apiInstance.developerAccountsDeveloperAccountIdPost(developerAccountId, developerId, opts, (error, data, response) => {
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
 **developerAccountId** | **String**| The id of the developer account to be updated | 
 **developerId** | **String**| The id of the developer that this account belongs to | 
 **email** | **String**| The contact email address | [optional] 
 **name** | **String**| The name for the account | [optional] 
 **customData** | **String**| A custom JSON object that you can create and attach to this record | [optional] 

### Return type

[**DeveloperAccount**](DeveloperAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## developerAccountsGet

> DeveloperAccountPages developerAccountsGet(opts)

Returns a paginated list of developerAccounts

- Results are paginated and the default is value is 1000 if no limit is provided 

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.DeveloperAccountsFindAndModifyDeveloperAccountsApi();
let opts = {
  'query': "query_example", // String | A query document. Example: {'name':'NASA'} matches all the developerAccounts that have the name 'NASA'
  'sort': "sort_example", // String | A sort document. Example: {'name':1} sorts the results by name in ascending order
  'pageNumber': 56, // Number | The result set page number to be returned
  'limit': 56 // Number | The maximum number of results to return per page
};
apiInstance.developerAccountsGet(opts, (error, data, response) => {
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
 **query** | **String**| A query document. Example: {&#39;name&#39;:&#39;NASA&#39;} matches all the developerAccounts that have the name &#39;NASA&#39; | [optional] 
 **sort** | **String**| A sort document. Example: {&#39;name&#39;:1} sorts the results by name in ascending order | [optional] 
 **pageNumber** | **Number**| The result set page number to be returned | [optional] 
 **limit** | **Number**| The maximum number of results to return per page | [optional] 

### Return type

[**DeveloperAccountPages**](DeveloperAccountPages.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

