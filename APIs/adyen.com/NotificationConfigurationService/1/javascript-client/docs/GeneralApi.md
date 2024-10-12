# NotificationConfigurationApi.GeneralApi

All URIs are relative to *https://cal-test.adyen.com/cal/services/Notification/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postCreateNotificationConfiguration**](GeneralApi.md#postCreateNotificationConfiguration) | **POST** /createNotificationConfiguration | Subscribe to notifications
[**postDeleteNotificationConfigurations**](GeneralApi.md#postDeleteNotificationConfigurations) | **POST** /deleteNotificationConfigurations | Delete a notification subscription configuration
[**postGetNotificationConfiguration**](GeneralApi.md#postGetNotificationConfiguration) | **POST** /getNotificationConfiguration | Get a notification subscription configuration
[**postGetNotificationConfigurationList**](GeneralApi.md#postGetNotificationConfigurationList) | **POST** /getNotificationConfigurationList | Get a list of notification subscription configurations
[**postTestNotificationConfiguration**](GeneralApi.md#postTestNotificationConfiguration) | **POST** /testNotificationConfiguration | Test a notification configuration
[**postUpdateNotificationConfiguration**](GeneralApi.md#postUpdateNotificationConfiguration) | **POST** /updateNotificationConfiguration | Update a notification subscription configuration



## postCreateNotificationConfiguration

> GetNotificationConfigurationResponse postCreateNotificationConfiguration(opts)

Subscribe to notifications

Creates a subscription to notifications informing you of events on your platform. After the subscription is created, the events specified in the configuration will be sent to the URL specified in the configuration. Subscriptions must be configured on a per-event basis (as opposed to, for example, a per-account holder basis), so all event notifications of a marketplace and of a given type will be sent to the same endpoint(s). A marketplace may have multiple endpoints if desired; an event notification may be sent to as many or as few different endpoints as configured.

### Example

```javascript
import NotificationConfigurationApi from 'notification_configuration_api';
let defaultClient = NotificationConfigurationApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new NotificationConfigurationApi.GeneralApi();
let opts = {
  'createNotificationConfigurationRequest': new NotificationConfigurationApi.CreateNotificationConfigurationRequest() // CreateNotificationConfigurationRequest | 
};
apiInstance.postCreateNotificationConfiguration(opts, (error, data, response) => {
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
 **createNotificationConfigurationRequest** | [**CreateNotificationConfigurationRequest**](CreateNotificationConfigurationRequest.md)|  | [optional] 

### Return type

[**GetNotificationConfigurationResponse**](GetNotificationConfigurationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postDeleteNotificationConfigurations

> GenericResponse postDeleteNotificationConfigurations(opts)

Delete a notification subscription configuration

Deletes an existing notification subscription configuration. After the subscription is deleted, no further event notifications will be sent to the URL defined in the subscription.

### Example

```javascript
import NotificationConfigurationApi from 'notification_configuration_api';
let defaultClient = NotificationConfigurationApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new NotificationConfigurationApi.GeneralApi();
let opts = {
  'deleteNotificationConfigurationRequest': new NotificationConfigurationApi.DeleteNotificationConfigurationRequest() // DeleteNotificationConfigurationRequest | 
};
apiInstance.postDeleteNotificationConfigurations(opts, (error, data, response) => {
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
 **deleteNotificationConfigurationRequest** | [**DeleteNotificationConfigurationRequest**](DeleteNotificationConfigurationRequest.md)|  | [optional] 

### Return type

[**GenericResponse**](GenericResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postGetNotificationConfiguration

> GetNotificationConfigurationResponse postGetNotificationConfiguration(opts)

Get a notification subscription configuration

Returns the details of the configuration of a notification subscription.

### Example

```javascript
import NotificationConfigurationApi from 'notification_configuration_api';
let defaultClient = NotificationConfigurationApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new NotificationConfigurationApi.GeneralApi();
let opts = {
  'getNotificationConfigurationRequest': new NotificationConfigurationApi.GetNotificationConfigurationRequest() // GetNotificationConfigurationRequest | 
};
apiInstance.postGetNotificationConfiguration(opts, (error, data, response) => {
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
 **getNotificationConfigurationRequest** | [**GetNotificationConfigurationRequest**](GetNotificationConfigurationRequest.md)|  | [optional] 

### Return type

[**GetNotificationConfigurationResponse**](GetNotificationConfigurationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postGetNotificationConfigurationList

> GetNotificationConfigurationListResponse postGetNotificationConfigurationList(opts)

Get a list of notification subscription configurations

Returns the details of the configurations of all of the notification subscriptions in the platform of the executing user.

### Example

```javascript
import NotificationConfigurationApi from 'notification_configuration_api';
let defaultClient = NotificationConfigurationApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new NotificationConfigurationApi.GeneralApi();
let opts = {
  'body': {key: null} // Object | 
};
apiInstance.postGetNotificationConfigurationList(opts, (error, data, response) => {
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
 **body** | **Object**|  | [optional] 

### Return type

[**GetNotificationConfigurationListResponse**](GetNotificationConfigurationListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postTestNotificationConfiguration

> TestNotificationConfigurationResponse postTestNotificationConfiguration(opts)

Test a notification configuration

Tests an existing notification subscription configuration. For each event type specified, a test notification will be generated and sent to the URL configured in the subscription specified.

### Example

```javascript
import NotificationConfigurationApi from 'notification_configuration_api';
let defaultClient = NotificationConfigurationApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new NotificationConfigurationApi.GeneralApi();
let opts = {
  'testNotificationConfigurationRequest': new NotificationConfigurationApi.TestNotificationConfigurationRequest() // TestNotificationConfigurationRequest | 
};
apiInstance.postTestNotificationConfiguration(opts, (error, data, response) => {
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
 **testNotificationConfigurationRequest** | [**TestNotificationConfigurationRequest**](TestNotificationConfigurationRequest.md)|  | [optional] 

### Return type

[**TestNotificationConfigurationResponse**](TestNotificationConfigurationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postUpdateNotificationConfiguration

> GetNotificationConfigurationResponse postUpdateNotificationConfiguration(opts)

Update a notification subscription configuration

Updates an existing notification subscription configuration. If you are updating the event types, you must provide all event types, otherwise the previous event type configuration will be overwritten.

### Example

```javascript
import NotificationConfigurationApi from 'notification_configuration_api';
let defaultClient = NotificationConfigurationApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new NotificationConfigurationApi.GeneralApi();
let opts = {
  'updateNotificationConfigurationRequest': new NotificationConfigurationApi.UpdateNotificationConfigurationRequest() // UpdateNotificationConfigurationRequest | 
};
apiInstance.postUpdateNotificationConfiguration(opts, (error, data, response) => {
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
 **updateNotificationConfigurationRequest** | [**UpdateNotificationConfigurationRequest**](UpdateNotificationConfigurationRequest.md)|  | [optional] 

### Return type

[**GetNotificationConfigurationResponse**](GetNotificationConfigurationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

