# Ritc.AppsApi

All URIs are relative to *https://api.ritc.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addApp**](AppsApi.md#addApp) | **POST** /apps | 
[**addAppChannelUser**](AppsApi.md#addAppChannelUser) | **POST** /apps/channels/{channel_id}/users/{user_id} | 
[**addChannelExternalCredentials**](AppsApi.md#addChannelExternalCredentials) | **POST** /apps/ext/api/credentials | 
[**getApp**](AppsApi.md#getApp) | **GET** /apps/{app_id} | 
[**getAppChannelUser**](AppsApi.md#getAppChannelUser) | **GET** /apps/channels/{channel_id}/users/{user_id} | 
[**getChannelExternalCredentials**](AppsApi.md#getChannelExternalCredentials) | **GET** /apps/ext/api/credentials/{channel_id} | 
[**listAppChannelUsers**](AppsApi.md#listAppChannelUsers) | **GET** /apps/channels/{channel_id}/users | 
[**listAppChannels**](AppsApi.md#listAppChannels) | **GET** /apps/channels/users | 
[**listApps**](AppsApi.md#listApps) | **GET** /apps | 
[**listChannelExternalCredentials**](AppsApi.md#listChannelExternalCredentials) | **GET** /apps/ext/api/credentials | 
[**removeApp**](AppsApi.md#removeApp) | **DELETE** /apps/{app_id} | 
[**removeChannelExternalCredentials**](AppsApi.md#removeChannelExternalCredentials) | **DELETE** /apps/ext/api/credentials/{channel_id} | 
[**runApp**](AppsApi.md#runApp) | **POST** /apps/rules/run | 
[**runRuleGroup**](AppsApi.md#runRuleGroup) | **POST** /apps/rulegroup/run/{rule_id_list} | 
[**updateApp**](AppsApi.md#updateApp) | **PATCH** /apps/{app_id} | 
[**updateChannelExternalCredentials**](AppsApi.md#updateChannelExternalCredentials) | **PATCH** /apps/ext/api/credentials/{channel_id} | 



## addApp

> AppResponse addApp(appObject)



Create a new app

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.AppsApi();
let appObject = new Ritc.App(); // App | App information
apiInstance.addApp(appObject, (error, data, response) => {
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
 **appObject** | [**App**](App.md)| App information | 

### Return type

[**AppResponse**](AppResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## addAppChannelUser

> AppChannelResponse addAppChannelUser(channelId, userId)



Create user channel

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.AppsApi();
let channelId = "channelId_example"; // String | Id of Channel
let userId = "userId_example"; // String | Id of User
apiInstance.addAppChannelUser(channelId, userId, (error, data, response) => {
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
 **channelId** | **String**| Id of Channel | 
 **userId** | **String**| Id of User | 

### Return type

[**AppChannelResponse**](AppChannelResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## addChannelExternalCredentials

> AppExternalCredentialsResponse addChannelExternalCredentials(appExternalCredentialsObject)



Create new external credentials

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.AppsApi();
let appExternalCredentialsObject = new Ritc.AppExternalCredentials(); // AppExternalCredentials | App_External_Credentials information
apiInstance.addChannelExternalCredentials(appExternalCredentialsObject, (error, data, response) => {
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
 **appExternalCredentialsObject** | [**AppExternalCredentials**](AppExternalCredentials.md)| App_External_Credentials information | 

### Return type

[**AppExternalCredentialsResponse**](AppExternalCredentialsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getApp

> [AppResponse] getApp(appId)



Get app information

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.AppsApi();
let appId = "appId_example"; // String | Id of App
apiInstance.getApp(appId, (error, data, response) => {
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
 **appId** | **String**| Id of App | 

### Return type

[**[AppResponse]**](AppResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAppChannelUser

> [AppChannelResponse] getAppChannelUser(channelId, userId)



Get user of a specified channel

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.AppsApi();
let channelId = "channelId_example"; // String | Id of Channel
let userId = "userId_example"; // String | Id of User
apiInstance.getAppChannelUser(channelId, userId, (error, data, response) => {
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
 **channelId** | **String**| Id of Channel | 
 **userId** | **String**| Id of User | 

### Return type

[**[AppChannelResponse]**](AppChannelResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getChannelExternalCredentials

> [AppExternalCredentialsResponse] getChannelExternalCredentials(channelId)



Get credentials for a channel in an app

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.AppsApi();
let channelId = "channelId_example"; // String | Id of Channel
apiInstance.getChannelExternalCredentials(channelId, (error, data, response) => {
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
 **channelId** | **String**| Id of Channel | 

### Return type

[**[AppExternalCredentialsResponse]**](AppExternalCredentialsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAppChannelUsers

> [AppChannelResponse] listAppChannelUsers(channelId)



Get users of a specified channel

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.AppsApi();
let channelId = "channelId_example"; // String | Id of Channel
apiInstance.listAppChannelUsers(channelId, (error, data, response) => {
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
 **channelId** | **String**| Id of Channel | 

### Return type

[**[AppChannelResponse]**](AppChannelResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAppChannels

> [AppChannelResponse] listAppChannels()



Get app channels

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.AppsApi();
apiInstance.listAppChannels((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[AppChannelResponse]**](AppChannelResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listApps

> [AppResponse] listApps()



Get apps information

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.AppsApi();
apiInstance.listApps((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[AppResponse]**](AppResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listChannelExternalCredentials

> [AppExternalCredentialsResponse] listChannelExternalCredentials()



Get external credentials

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.AppsApi();
apiInstance.listChannelExternalCredentials((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[AppExternalCredentialsResponse]**](AppExternalCredentialsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeApp

> removeApp(appId)



Delete an app

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.AppsApi();
let appId = "appId_example"; // String | Id of App
apiInstance.removeApp(appId, (error, data, response) => {
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
 **appId** | **String**| Id of App | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeChannelExternalCredentials

> removeChannelExternalCredentials(channelId)



Delete credentials for a channel

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.AppsApi();
let channelId = "channelId_example"; // String | Id of Channel
apiInstance.removeChannelExternalCredentials(channelId, (error, data, response) => {
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
 **channelId** | **String**| Id of Channel | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## runApp

> [RuleResults] runApp(opts)



Run active app rules

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.AppsApi();
let opts = {
  'breakWhenRuleFires': true, // Boolean | Do not continue with remaining rules after a rule fires
  'initialData': {key: null} // Object | Initial data
};
apiInstance.runApp(opts, (error, data, response) => {
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
 **breakWhenRuleFires** | **Boolean**| Do not continue with remaining rules after a rule fires | [optional] 
 **initialData** | **Object**| Initial data | [optional] 

### Return type

[**[RuleResults]**](RuleResults.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## runRuleGroup

> [RuleResults] runRuleGroup(ruleIdList, opts)



Run specified rule group in the app

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.AppsApi();
let ruleIdList = "ruleIdList_example"; // String | Ids of rules in the group, separated by commas, no spaces
let opts = {
  'breakWhenRuleFires': true, // Boolean | Do not continue with remaining rules after a rule fires
  'initialData': {key: null} // Object | Initial data
};
apiInstance.runRuleGroup(ruleIdList, opts, (error, data, response) => {
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
 **ruleIdList** | **String**| Ids of rules in the group, separated by commas, no spaces | 
 **breakWhenRuleFires** | **Boolean**| Do not continue with remaining rules after a rule fires | [optional] 
 **initialData** | **Object**| Initial data | [optional] 

### Return type

[**[RuleResults]**](RuleResults.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateApp

> AppResponse updateApp(appId, appObject)



Update an app

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.AppsApi();
let appId = "appId_example"; // String | Id of app
let appObject = new Ritc.App(); // App | App information
apiInstance.updateApp(appId, appObject, (error, data, response) => {
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
 **appId** | **String**| Id of app | 
 **appObject** | [**App**](App.md)| App information | 

### Return type

[**AppResponse**](AppResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateChannelExternalCredentials

> AppExternalCredentialsResponse updateChannelExternalCredentials(channelId, appExternalCredentialsObject)



Update credentials for a channel

### Example

```javascript
import Ritc from 'ritc';
let defaultClient = Ritc.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Ritc.AppsApi();
let channelId = "channelId_example"; // String | Id of Channel
let appExternalCredentialsObject = new Ritc.AppExternalCredentials(); // AppExternalCredentials | App_External_Credentials information
apiInstance.updateChannelExternalCredentials(channelId, appExternalCredentialsObject, (error, data, response) => {
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
 **channelId** | **String**| Id of Channel | 
 **appExternalCredentialsObject** | [**AppExternalCredentials**](AppExternalCredentials.md)| App_External_Credentials information | 

### Return type

[**AppExternalCredentialsResponse**](AppExternalCredentialsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

