# ChecksApi.HooksApi

All URIs are relative to *https://api.truora.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createHook**](HooksApi.md#createHook) | **POST** /v1/hooks | Creates a hook subscription
[**deletHook**](HooksApi.md#deletHook) | **DELETE** /v1/hooks/{hook_id} | Deletes hook
[**listHook**](HooksApi.md#listHook) | **GET** /v1/hooks | Lists all hooks
[**updateHook**](HooksApi.md#updateHook) | **PUT** /v1/hooks/{hook_id} | Updates hook



## createHook

> Hook createHook(eventType, subscriberType, opts)

Creates a hook subscription

Creates a hook subscription to notify events in Truora plataform. Subscriptions broadcast data as events occur and additional subscription instances are not required in order to refresh the information. Events are received in an array as a JWT and are decoded using the signing key returned by this endpoint. Their structure is as follows:  &#x60;&#x60;&#x60; {     \&quot;events\&quot;: [         {             \&quot;event_action\&quot;: \&quot;created\&quot;,             \&quot;event_type\&quot;: \&quot;check\&quot;,             \&quot;id\&quot;: \&quot;HKEdd28c569cf5eb74e45f0f4c092096e62c1c95ba2\&quot;,             \&quot;object\&quot;: {                 \&quot;check_id\&quot;: \&quot;CHK9c39003424c521aec8566ce59e1ddc86\&quot;,                 \&quot;country\&quot;: \&quot;CO\&quot;,                 \&quot;creation_date\&quot;: \&quot;2020-04-01T23:00:30.581232281Z\&quot;,                 \&quot;homonym_score\&quot;: 0,                 \&quot;id_score\&quot;: 0,                 \&quot;national_id\&quot;: \&quot;1151959906\&quot;,                 \&quot;previous_check\&quot;: \&quot;CHK4ec814fecd147eaae41027081d7d5caf\&quot;,                 \&quot;score\&quot;: -1,                 \&quot;status\&quot;: \&quot;not_started\&quot;,                 \&quot;type\&quot;: \&quot;person\&quot;,                 \&quot;update_date\&quot;: \&quot;2020-04-01T23:00:30.680937413Z\&quot;             },             \&quot;timestamp\&quot;: \&quot;2020-04-01T23:00:30Z\&quot;,             \&quot;version\&quot;: \&quot;1.0\&quot;         }     ],     \&quot;iat\&quot;: 1585782031,     \&quot;iss\&quot;: \&quot;Truora\&quot; } &#x60;&#x60;&#x60;  Keep in mind that the object attribute varies depending on the event_type.

### Example

```javascript
import ChecksApi from 'checks_api';
let defaultClient = ChecksApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ChecksApi.HooksApi();
let eventType = "eventType_example"; // String | The entity events the client wants to subscribe
let subscriberType = "subscriberType_example"; // String | A platform with an endpoint ready to process the information
let opts = {
  'actions': ["null"], // [String] | Actions you want to be notified. Possible inputs are created, started, and finished or any combination of those three
  'status': "status_example", // String | indicates whether the hook is active or not. enabled by default
  'subscriberAddress': "subscriberAddress_example", // String | Email address where the notification is to be sent. Required if subscriber_type was set to email
  'subscriberLanguage': "subscriberLanguage_example", // String | Language for the notification to be sent
  'subscriberName': "subscriberName_example", // String | Name of the person to be notified
  'subscriberUrl': "subscriberUrl_example" // String | URL where the notification is to be sent. Required only if subscriber_type is set to web
};
apiInstance.createHook(eventType, subscriberType, opts, (error, data, response) => {
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
 **eventType** | **String**| The entity events the client wants to subscribe | 
 **subscriberType** | **String**| A platform with an endpoint ready to process the information | 
 **actions** | [**[String]**](String.md)| Actions you want to be notified. Possible inputs are created, started, and finished or any combination of those three | [optional] 
 **status** | **String**| indicates whether the hook is active or not. enabled by default | [optional] 
 **subscriberAddress** | **String**| Email address where the notification is to be sent. Required if subscriber_type was set to email | [optional] 
 **subscriberLanguage** | **String**| Language for the notification to be sent | [optional] 
 **subscriberName** | **String**| Name of the person to be notified | [optional] 
 **subscriberUrl** | **String**| URL where the notification is to be sent. Required only if subscriber_type is set to web | [optional] 

### Return type

[**Hook**](Hook.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deletHook

> String deletHook(hookId)

Deletes hook

Deletes hook configuration.

### Example

```javascript
import ChecksApi from 'checks_api';
let defaultClient = ChecksApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ChecksApi.HooksApi();
let hookId = "hookId_example"; // String | Hook ID
apiInstance.deletHook(hookId, (error, data, response) => {
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
 **hookId** | **String**| Hook ID | 

### Return type

**String**

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listHook

> HookOutput listHook()

Lists all hooks

Lists all the configured hooks in your account.

### Example

```javascript
import ChecksApi from 'checks_api';
let defaultClient = ChecksApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ChecksApi.HooksApi();
apiInstance.listHook((error, data, response) => {
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

[**HookOutput**](HookOutput.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateHook

> Hook updateHook(hookId, eventType, subscriberType, opts)

Updates hook

Updates a hook configuration.

### Example

```javascript
import ChecksApi from 'checks_api';
let defaultClient = ChecksApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ChecksApi.HooksApi();
let hookId = "hookId_example"; // String | Hook ID
let eventType = "eventType_example"; // String | The entity events the client wants to subscribe
let subscriberType = "subscriberType_example"; // String | A platform with an endpoint ready to process the information
let opts = {
  'actions': ["null"], // [String] | Actions you want to be notified. Possible inputs are created, started, and finished or any combination of those three
  'status': "status_example", // String | indicates whether the hook is active or not. enabled by default
  'subscriberAddress': "subscriberAddress_example", // String | Email address where the notification is to be sent. Required if subscriber_type was set to email
  'subscriberLanguage': "subscriberLanguage_example", // String | Language for the notification to be sent
  'subscriberName': "subscriberName_example", // String | Name of the person to be notified
  'subscriberUrl': "subscriberUrl_example" // String | URL where the notification is to be sent. Required only if subscriber_type is set to web
};
apiInstance.updateHook(hookId, eventType, subscriberType, opts, (error, data, response) => {
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
 **hookId** | **String**| Hook ID | 
 **eventType** | **String**| The entity events the client wants to subscribe | 
 **subscriberType** | **String**| A platform with an endpoint ready to process the information | 
 **actions** | [**[String]**](String.md)| Actions you want to be notified. Possible inputs are created, started, and finished or any combination of those three | [optional] 
 **status** | **String**| indicates whether the hook is active or not. enabled by default | [optional] 
 **subscriberAddress** | **String**| Email address where the notification is to be sent. Required if subscriber_type was set to email | [optional] 
 **subscriberLanguage** | **String**| Language for the notification to be sent | [optional] 
 **subscriberName** | **String**| Name of the person to be notified | [optional] 
 **subscriberUrl** | **String**| URL where the notification is to be sent. Required only if subscriber_type is set to web | [optional] 

### Return type

[**Hook**](Hook.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/x-www-form-urlencoded, application/json

