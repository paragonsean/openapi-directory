# PendoFeedbackApi.AccountApi

All URIs are relative to *https://api.feedback.eu.pendo.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountsGet**](AccountApi.md#accountsGet) | **GET** /accounts | Query accounts
[**accountsIdDelete**](AccountApi.md#accountsIdDelete) | **DELETE** /accounts/{id} | Delete an Account
[**accountsIdGet**](AccountApi.md#accountsIdGet) | **GET** /accounts/{id} | Get an Account
[**accountsIdPut**](AccountApi.md#accountsIdPut) | **PUT** /accounts/{id} | Update an Account
[**accountsIdTagsDelete**](AccountApi.md#accountsIdTagsDelete) | **DELETE** /accounts/{id}/tags | Delete custom Account tags
[**accountsIdTagsGet**](AccountApi.md#accountsIdTagsGet) | **GET** /accounts/{id}/tags | Get custom Account tags
[**accountsIdTagsPost**](AccountApi.md#accountsIdTagsPost) | **POST** /accounts/{id}/tags | Overwrite current custom Account tags with the given tags



## accountsGet

> [Account] accountsGet(opts)

Query accounts

### Example

```javascript
import PendoFeedbackApi from 'pendo_feedback_api';
let defaultClient = PendoFeedbackApi.ApiClient.instance;
// Configure API key authorization: userApiKey (request header)
let userApiKey (request header) = defaultClient.authentications['userApiKey (request header)'];
userApiKey (request header).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (request header).apiKeyPrefix = 'Token';
// Configure API key authorization: userApiKey (query parameter)
let userApiKey (query parameter) = defaultClient.authentications['userApiKey (query parameter)'];
userApiKey (query parameter).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (query parameter).apiKeyPrefix = 'Token';

let apiInstance = new PendoFeedbackApi.AccountApi();
let opts = {
  'limit': 3.4, // Number | Limit the number of records returned
  'start': 3.4, // Number | Offset to start at
  'orderDir': "orderDir_example", // String | The sort direction
  'orderBy': "orderBy_example" // String | The field to use for sort
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
 **limit** | **Number**| Limit the number of records returned | [optional] 
 **start** | **Number**| Offset to start at | [optional] 
 **orderDir** | **String**| The sort direction | [optional] 
 **orderBy** | **String**| The field to use for sort | [optional] 

### Return type

[**[Account]**](Account.md)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsIdDelete

> Account accountsIdDelete(id)

Delete an Account

This removes most traces of an Accounts existence from the system.

### Example

```javascript
import PendoFeedbackApi from 'pendo_feedback_api';
let defaultClient = PendoFeedbackApi.ApiClient.instance;
// Configure API key authorization: userApiKey (request header)
let userApiKey (request header) = defaultClient.authentications['userApiKey (request header)'];
userApiKey (request header).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (request header).apiKeyPrefix = 'Token';
// Configure API key authorization: userApiKey (query parameter)
let userApiKey (query parameter) = defaultClient.authentications['userApiKey (query parameter)'];
userApiKey (query parameter).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (query parameter).apiKeyPrefix = 'Token';

let apiInstance = new PendoFeedbackApi.AccountApi();
let id = 3.4; // Number | 
apiInstance.accountsIdDelete(id, (error, data, response) => {
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
 **id** | **Number**|  | 

### Return type

[**Account**](Account.md)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsIdGet

> Account accountsIdGet(id)

Get an Account

### Example

```javascript
import PendoFeedbackApi from 'pendo_feedback_api';
let defaultClient = PendoFeedbackApi.ApiClient.instance;
// Configure API key authorization: userApiKey (request header)
let userApiKey (request header) = defaultClient.authentications['userApiKey (request header)'];
userApiKey (request header).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (request header).apiKeyPrefix = 'Token';
// Configure API key authorization: userApiKey (query parameter)
let userApiKey (query parameter) = defaultClient.authentications['userApiKey (query parameter)'];
userApiKey (query parameter).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (query parameter).apiKeyPrefix = 'Token';

let apiInstance = new PendoFeedbackApi.AccountApi();
let id = 3.4; // Number | Account ID (generated by Feedback)
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
 **id** | **Number**| Account ID (generated by Feedback) | 

### Return type

[**Account**](Account.md)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsIdPut

> accountsIdPut(id, opts)

Update an Account

### Example

```javascript
import PendoFeedbackApi from 'pendo_feedback_api';
let defaultClient = PendoFeedbackApi.ApiClient.instance;
// Configure API key authorization: userApiKey (request header)
let userApiKey (request header) = defaultClient.authentications['userApiKey (request header)'];
userApiKey (request header).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (request header).apiKeyPrefix = 'Token';
// Configure API key authorization: userApiKey (query parameter)
let userApiKey (query parameter) = defaultClient.authentications['userApiKey (query parameter)'];
userApiKey (query parameter).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (query parameter).apiKeyPrefix = 'Token';

let apiInstance = new PendoFeedbackApi.AccountApi();
let id = 3.4; // Number | Account ID (generated by Feedback)
let opts = {
  'account': new PendoFeedbackApi.AccountsIdPutRequest() // AccountsIdPutRequest | Updated Account values
};
apiInstance.accountsIdPut(id, opts, (error, data, response) => {
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
 **id** | **Number**| Account ID (generated by Feedback) | 
 **account** | [**AccountsIdPutRequest**](AccountsIdPutRequest.md)| Updated Account values | [optional] 

### Return type

null (empty response body)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## accountsIdTagsDelete

> accountsIdTagsDelete(id)

Delete custom Account tags

Removes all custom tags associated with the Account

### Example

```javascript
import PendoFeedbackApi from 'pendo_feedback_api';
let defaultClient = PendoFeedbackApi.ApiClient.instance;
// Configure API key authorization: userApiKey (request header)
let userApiKey (request header) = defaultClient.authentications['userApiKey (request header)'];
userApiKey (request header).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (request header).apiKeyPrefix = 'Token';
// Configure API key authorization: userApiKey (query parameter)
let userApiKey (query parameter) = defaultClient.authentications['userApiKey (query parameter)'];
userApiKey (query parameter).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (query parameter).apiKeyPrefix = 'Token';

let apiInstance = new PendoFeedbackApi.AccountApi();
let id = 3.4; // Number | Account ID (generated by Feedback)
apiInstance.accountsIdTagsDelete(id, (error, data, response) => {
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
 **id** | **Number**| Account ID (generated by Feedback) | 

### Return type

null (empty response body)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## accountsIdTagsGet

> accountsIdTagsGet(id)

Get custom Account tags

### Example

```javascript
import PendoFeedbackApi from 'pendo_feedback_api';
let defaultClient = PendoFeedbackApi.ApiClient.instance;
// Configure API key authorization: userApiKey (request header)
let userApiKey (request header) = defaultClient.authentications['userApiKey (request header)'];
userApiKey (request header).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (request header).apiKeyPrefix = 'Token';
// Configure API key authorization: userApiKey (query parameter)
let userApiKey (query parameter) = defaultClient.authentications['userApiKey (query parameter)'];
userApiKey (query parameter).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (query parameter).apiKeyPrefix = 'Token';

let apiInstance = new PendoFeedbackApi.AccountApi();
let id = 3.4; // Number | Account ID (generated by Feedback)
apiInstance.accountsIdTagsGet(id, (error, data, response) => {
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
 **id** | **Number**| Account ID (generated by Feedback) | 

### Return type

null (empty response body)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## accountsIdTagsPost

> accountsIdTagsPost(id, tags)

Overwrite current custom Account tags with the given tags

### Example

```javascript
import PendoFeedbackApi from 'pendo_feedback_api';
let defaultClient = PendoFeedbackApi.ApiClient.instance;
// Configure API key authorization: userApiKey (request header)
let userApiKey (request header) = defaultClient.authentications['userApiKey (request header)'];
userApiKey (request header).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (request header).apiKeyPrefix = 'Token';
// Configure API key authorization: userApiKey (query parameter)
let userApiKey (query parameter) = defaultClient.authentications['userApiKey (query parameter)'];
userApiKey (query parameter).apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//userApiKey (query parameter).apiKeyPrefix = 'Token';

let apiInstance = new PendoFeedbackApi.AccountApi();
let id = 3.4; // Number | Account ID (generated by Feedback)
let tags = {key: null}; // Object | An array of maps specifying tags under each tag group, for example:  [  {'impacts' => ['sales']},  {'resources' => ['dev', 'test', 'support']}  ]
apiInstance.accountsIdTagsPost(id, tags, (error, data, response) => {
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
 **id** | **Number**| Account ID (generated by Feedback) | 
 **tags** | **Object**| An array of maps specifying tags under each tag group, for example:  [  {&#39;impacts&#39; &#x3D;&gt; [&#39;sales&#39;]},  {&#39;resources&#39; &#x3D;&gt; [&#39;dev&#39;, &#39;test&#39;, &#39;support&#39;]}  ] | 

### Return type

null (empty response body)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

