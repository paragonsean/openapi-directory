# Apacta.MassMessagesUsersApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**massMessagesUsersGet**](MassMessagesUsersApi.md#massMessagesUsersGet) | **GET** /mass_messages_users | View list of mass messages for specific user
[**massMessagesUsersMassMessagesUserIdGet**](MassMessagesUsersApi.md#massMessagesUsersMassMessagesUserIdGet) | **GET** /mass_messages_users/{mass_messages_user_id} | View mass message
[**massMessagesUsersMassMessagesUserIdPut**](MassMessagesUsersApi.md#massMessagesUsersMassMessagesUserIdPut) | **PUT** /mass_messages_users/{mass_messages_user_id} | Edit mass message



## massMessagesUsersGet

> MassMessagesUsersGet200Response massMessagesUsersGet(opts)

View list of mass messages for specific user

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.MassMessagesUsersApi();
let opts = {
  'isRead': true // Boolean | Used to filter on the `is_read` of the mass messages
};
apiInstance.massMessagesUsersGet(opts, (error, data, response) => {
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
 **isRead** | **Boolean**| Used to filter on the &#x60;is_read&#x60; of the mass messages | [optional] 

### Return type

[**MassMessagesUsersGet200Response**](MassMessagesUsersGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## massMessagesUsersMassMessagesUserIdGet

> MassMessagesUsersMassMessagesUserIdGet200Response massMessagesUsersMassMessagesUserIdGet(massMessagesUserId)

View mass message

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.MassMessagesUsersApi();
let massMessagesUserId = "massMessagesUserId_example"; // String | 
apiInstance.massMessagesUsersMassMessagesUserIdGet(massMessagesUserId, (error, data, response) => {
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
 **massMessagesUserId** | **String**|  | 

### Return type

[**MassMessagesUsersMassMessagesUserIdGet200Response**](MassMessagesUsersMassMessagesUserIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## massMessagesUsersMassMessagesUserIdPut

> ClockingRecordsClockingRecordIdPut200Response massMessagesUsersMassMessagesUserIdPut(massMessagesUserId)

Edit mass message

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.MassMessagesUsersApi();
let massMessagesUserId = "massMessagesUserId_example"; // String | 
apiInstance.massMessagesUsersMassMessagesUserIdPut(massMessagesUserId, (error, data, response) => {
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
 **massMessagesUserId** | **String**|  | 

### Return type

[**ClockingRecordsClockingRecordIdPut200Response**](ClockingRecordsClockingRecordIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

