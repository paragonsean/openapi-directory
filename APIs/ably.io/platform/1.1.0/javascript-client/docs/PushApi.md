# PlatformApi.PushApi

All URIs are relative to *https://rest.ably.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deletePushDeviceDetails**](PushApi.md#deletePushDeviceDetails) | **DELETE** /push/channelSubscriptions | Delete a registered device&#39;s update token
[**getChannelsWithPushSubscribers**](PushApi.md#getChannelsWithPushSubscribers) | **GET** /push/channels | List all channels with at least one subscribed device
[**getPushDeviceDetails**](PushApi.md#getPushDeviceDetails) | **GET** /push/deviceRegistrations/{device_id} | Get a device registration
[**getPushSubscriptionsOnChannels**](PushApi.md#getPushSubscriptionsOnChannels) | **GET** /push/channelSubscriptions | List channel subscriptions
[**getRegisteredPushDevices**](PushApi.md#getRegisteredPushDevices) | **GET** /push/deviceRegistrations | List devices registered for receiving push notifications
[**patchPushDeviceDetails**](PushApi.md#patchPushDeviceDetails) | **PATCH** /push/deviceRegistrations/{device_id} | Update a device registration
[**publishPushNotificationToDevices**](PushApi.md#publishPushNotificationToDevices) | **POST** /push/publish | Publish a push notification to device(s)
[**putPushDeviceDetails**](PushApi.md#putPushDeviceDetails) | **PUT** /push/deviceRegistrations/{device_id} | Update a device registration
[**registerPushDevice**](PushApi.md#registerPushDevice) | **POST** /push/deviceRegistrations | Register a device for receiving push notifications
[**subscribePushDeviceToChannel**](PushApi.md#subscribePushDeviceToChannel) | **POST** /push/channelSubscriptions | Subscribe a device to a channel
[**unregisterAllPushDevices**](PushApi.md#unregisterAllPushDevices) | **DELETE** /push/deviceRegistrations | Unregister matching devices for push notifications
[**unregisterPushDevice**](PushApi.md#unregisterPushDevice) | **DELETE** /push/deviceRegistrations/{device_id} | Unregister a single device for push notifications
[**updatePushDeviceDetails**](PushApi.md#updatePushDeviceDetails) | **GET** /push/deviceRegistrations/{device_id}/resetUpdateToken | Reset a registered device&#39;s update token



## deletePushDeviceDetails

> deletePushDeviceDetails(opts)

Delete a registered device&#39;s update token

Delete a device details object.

### Example

```javascript
import PlatformApi from 'platform_api';
let defaultClient = PlatformApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new PlatformApi.PushApi();
let opts = {
  'xAblyVersion': "xAblyVersion_example", // String | The version of the API you wish to use.
  'format': "format_example", // String | The response format you would like
  'channel': "channel_example", // String | Filter to restrict to subscriptions associated with that channel.
  'deviceId': "deviceId_example", // String | Must be set when clientId is empty, cannot be used with clientId.
  'clientId': "clientId_example" // String | Must be set when deviceId is empty, cannot be used with deviceId.
};
apiInstance.deletePushDeviceDetails(opts, (error, data, response) => {
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
 **xAblyVersion** | **String**| The version of the API you wish to use. | [optional] 
 **format** | **String**| The response format you would like | [optional] 
 **channel** | **String**| Filter to restrict to subscriptions associated with that channel. | [optional] 
 **deviceId** | **String**| Must be set when clientId is empty, cannot be used with clientId. | [optional] 
 **clientId** | **String**| Must be set when deviceId is empty, cannot be used with deviceId. | [optional] 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/x-msgpack, text/html


## getChannelsWithPushSubscribers

> [String] getChannelsWithPushSubscribers(opts)

List all channels with at least one subscribed device

Returns a paginated response of channel names.

### Example

```javascript
import PlatformApi from 'platform_api';
let defaultClient = PlatformApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new PlatformApi.PushApi();
let opts = {
  'xAblyVersion': "xAblyVersion_example", // String | The version of the API you wish to use.
  'format': "format_example" // String | The response format you would like
};
apiInstance.getChannelsWithPushSubscribers(opts, (error, data, response) => {
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
 **xAblyVersion** | **String**| The version of the API you wish to use. | [optional] 
 **format** | **String**| The response format you would like | [optional] 

### Return type

**[String]**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/x-msgpack, text/html


## getPushDeviceDetails

> DeviceDetails getPushDeviceDetails(deviceId, opts)

Get a device registration

Get the full details of a device.

### Example

```javascript
import PlatformApi from 'platform_api';
let defaultClient = PlatformApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new PlatformApi.PushApi();
let deviceId = "deviceId_example"; // String | Device's ID.
let opts = {
  'xAblyVersion': "xAblyVersion_example", // String | The version of the API you wish to use.
  'format': "format_example" // String | The response format you would like
};
apiInstance.getPushDeviceDetails(deviceId, opts, (error, data, response) => {
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
 **deviceId** | **String**| Device&#39;s ID. | 
 **xAblyVersion** | **String**| The version of the API you wish to use. | [optional] 
 **format** | **String**| The response format you would like | [optional] 

### Return type

[**DeviceDetails**](DeviceDetails.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/x-msgpack, text/html


## getPushSubscriptionsOnChannels

> DeviceDetails getPushSubscriptionsOnChannels(opts)

List channel subscriptions

Get a list of push notification subscriptions to channels.

### Example

```javascript
import PlatformApi from 'platform_api';
let defaultClient = PlatformApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new PlatformApi.PushApi();
let opts = {
  'xAblyVersion': "xAblyVersion_example", // String | The version of the API you wish to use.
  'format': "format_example", // String | The response format you would like
  'channel': "channel_example", // String | Filter to restrict to subscriptions associated with that channel.
  'deviceId': "deviceId_example", // String | Optional filter to restrict to devices associated with that deviceId. Cannot be used with clientId.
  'clientId': "clientId_example", // String | Optional filter to restrict to devices associated with that clientId. Cannot be used with deviceId.
  'limit': 100 // Number | The maximum number of records to return.
};
apiInstance.getPushSubscriptionsOnChannels(opts, (error, data, response) => {
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
 **xAblyVersion** | **String**| The version of the API you wish to use. | [optional] 
 **format** | **String**| The response format you would like | [optional] 
 **channel** | **String**| Filter to restrict to subscriptions associated with that channel. | [optional] 
 **deviceId** | **String**| Optional filter to restrict to devices associated with that deviceId. Cannot be used with clientId. | [optional] 
 **clientId** | **String**| Optional filter to restrict to devices associated with that clientId. Cannot be used with deviceId. | [optional] 
 **limit** | **Number**| The maximum number of records to return. | [optional] [default to 100]

### Return type

[**DeviceDetails**](DeviceDetails.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/x-msgpack, text/html


## getRegisteredPushDevices

> DeviceDetails getRegisteredPushDevices(opts)

List devices registered for receiving push notifications

List of device details of devices registed for push notifications.

### Example

```javascript
import PlatformApi from 'platform_api';
let defaultClient = PlatformApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new PlatformApi.PushApi();
let opts = {
  'xAblyVersion': "xAblyVersion_example", // String | The version of the API you wish to use.
  'format': "format_example", // String | The response format you would like
  'deviceId': "deviceId_example", // String | Optional filter to restrict to devices associated with that deviceId.
  'clientId': "clientId_example", // String | Optional filter to restrict to devices associated with that clientId.
  'limit': 100 // Number | The maximum number of records to return.
};
apiInstance.getRegisteredPushDevices(opts, (error, data, response) => {
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
 **xAblyVersion** | **String**| The version of the API you wish to use. | [optional] 
 **format** | **String**| The response format you would like | [optional] 
 **deviceId** | **String**| Optional filter to restrict to devices associated with that deviceId. | [optional] 
 **clientId** | **String**| Optional filter to restrict to devices associated with that clientId. | [optional] 
 **limit** | **Number**| The maximum number of records to return. | [optional] [default to 100]

### Return type

[**DeviceDetails**](DeviceDetails.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/x-msgpack, text/html


## patchPushDeviceDetails

> DeviceDetails patchPushDeviceDetails(deviceId, opts)

Update a device registration

Specific attributes of an existing registration can be updated. Only clientId, metadata and push.recipient are mutable.

### Example

```javascript
import PlatformApi from 'platform_api';
let defaultClient = PlatformApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new PlatformApi.PushApi();
let deviceId = "deviceId_example"; // String | Device's ID.
let opts = {
  'xAblyVersion': "xAblyVersion_example", // String | The version of the API you wish to use.
  'format': "format_example", // String | The response format you would like
  'deviceDetails': new PlatformApi.DeviceDetails() // DeviceDetails | 
};
apiInstance.patchPushDeviceDetails(deviceId, opts, (error, data, response) => {
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
 **deviceId** | **String**| Device&#39;s ID. | 
 **xAblyVersion** | **String**| The version of the API you wish to use. | [optional] 
 **format** | **String**| The response format you would like | [optional] 
 **deviceDetails** | [**DeviceDetails**](DeviceDetails.md)|  | [optional] 

### Return type

[**DeviceDetails**](DeviceDetails.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-msgpack, application/x-www-form-urlencoded
- **Accept**: application/json, application/x-msgpack, text/html


## publishPushNotificationToDevices

> publishPushNotificationToDevices(opts)

Publish a push notification to device(s)

A convenience endpoint to deliver a push notification payload to a single device or set of devices identified by their client identifier.

### Example

```javascript
import PlatformApi from 'platform_api';
let defaultClient = PlatformApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new PlatformApi.PushApi();
let opts = {
  'xAblyVersion': "xAblyVersion_example", // String | The version of the API you wish to use.
  'format': "format_example", // String | The response format you would like
  'publishPushNotificationToDevicesRequest': new PlatformApi.PublishPushNotificationToDevicesRequest() // PublishPushNotificationToDevicesRequest | 
};
apiInstance.publishPushNotificationToDevices(opts, (error, data, response) => {
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
 **xAblyVersion** | **String**| The version of the API you wish to use. | [optional] 
 **format** | **String**| The response format you would like | [optional] 
 **publishPushNotificationToDevicesRequest** | [**PublishPushNotificationToDevicesRequest**](PublishPushNotificationToDevicesRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-msgpack, application/x-www-form-urlencoded
- **Accept**: application/json, application/x-msgpack, text/html


## putPushDeviceDetails

> DeviceDetails putPushDeviceDetails(deviceId, opts)

Update a device registration

Device registrations can be upserted (the existing registration is replaced entirely) with a PUT operation. Only clientId, metadata and push.recipient are mutable.

### Example

```javascript
import PlatformApi from 'platform_api';
let defaultClient = PlatformApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new PlatformApi.PushApi();
let deviceId = "deviceId_example"; // String | Device's ID.
let opts = {
  'xAblyVersion': "xAblyVersion_example", // String | The version of the API you wish to use.
  'format': "format_example", // String | The response format you would like
  'deviceDetails': new PlatformApi.DeviceDetails() // DeviceDetails | 
};
apiInstance.putPushDeviceDetails(deviceId, opts, (error, data, response) => {
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
 **deviceId** | **String**| Device&#39;s ID. | 
 **xAblyVersion** | **String**| The version of the API you wish to use. | [optional] 
 **format** | **String**| The response format you would like | [optional] 
 **deviceDetails** | [**DeviceDetails**](DeviceDetails.md)|  | [optional] 

### Return type

[**DeviceDetails**](DeviceDetails.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-msgpack, application/x-www-form-urlencoded
- **Accept**: application/json, application/x-msgpack, text/html


## registerPushDevice

> DeviceDetails registerPushDevice(opts)

Register a device for receiving push notifications

Register a device’s details, including the information necessary to deliver push notifications to it. Requires \&quot;push-admin\&quot; capability.

### Example

```javascript
import PlatformApi from 'platform_api';
let defaultClient = PlatformApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new PlatformApi.PushApi();
let opts = {
  'xAblyVersion': "xAblyVersion_example", // String | The version of the API you wish to use.
  'format': "format_example", // String | The response format you would like
  'deviceDetails': new PlatformApi.DeviceDetails() // DeviceDetails | 
};
apiInstance.registerPushDevice(opts, (error, data, response) => {
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
 **xAblyVersion** | **String**| The version of the API you wish to use. | [optional] 
 **format** | **String**| The response format you would like | [optional] 
 **deviceDetails** | [**DeviceDetails**](DeviceDetails.md)|  | [optional] 

### Return type

[**DeviceDetails**](DeviceDetails.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-msgpack
- **Accept**: application/json, application/x-msgpack, text/html


## subscribePushDeviceToChannel

> subscribePushDeviceToChannel(opts)

Subscribe a device to a channel

Subscribe either a single device or all devices associated with a client ID to receive push notifications from messages sent to a channel.

### Example

```javascript
import PlatformApi from 'platform_api';
let defaultClient = PlatformApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new PlatformApi.PushApi();
let opts = {
  'xAblyVersion': "xAblyVersion_example", // String | The version of the API you wish to use.
  'format': "format_example", // String | The response format you would like
  'subscribePushDeviceToChannelRequest': {"channel":"my:channel","clientId":"myClientId"} // SubscribePushDeviceToChannelRequest | 
};
apiInstance.subscribePushDeviceToChannel(opts, (error, data, response) => {
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
 **xAblyVersion** | **String**| The version of the API you wish to use. | [optional] 
 **format** | **String**| The response format you would like | [optional] 
 **subscribePushDeviceToChannelRequest** | [**SubscribePushDeviceToChannelRequest**](SubscribePushDeviceToChannelRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-msgpack, application/x-www-form-urlencoded
- **Accept**: application/json, application/x-msgpack, text/html


## unregisterAllPushDevices

> unregisterAllPushDevices(opts)

Unregister matching devices for push notifications

Unregisters devices. All their subscriptions for receiving push notifications through channels will also be deleted.

### Example

```javascript
import PlatformApi from 'platform_api';
let defaultClient = PlatformApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new PlatformApi.PushApi();
let opts = {
  'xAblyVersion': "xAblyVersion_example", // String | The version of the API you wish to use.
  'format': "format_example", // String | The response format you would like
  'deviceId': "deviceId_example", // String | Optional filter to restrict to devices associated with that deviceId. Cannot be used with clientId.
  'clientId': "clientId_example" // String | Optional filter to restrict to devices associated with that clientId. Cannot be used with deviceId.
};
apiInstance.unregisterAllPushDevices(opts, (error, data, response) => {
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
 **xAblyVersion** | **String**| The version of the API you wish to use. | [optional] 
 **format** | **String**| The response format you would like | [optional] 
 **deviceId** | **String**| Optional filter to restrict to devices associated with that deviceId. Cannot be used with clientId. | [optional] 
 **clientId** | **String**| Optional filter to restrict to devices associated with that clientId. Cannot be used with deviceId. | [optional] 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/x-msgpack, text/html


## unregisterPushDevice

> unregisterPushDevice(deviceId, opts)

Unregister a single device for push notifications

Unregisters a single device by its device ID. All its subscriptions for receiving push notifications through channels will also be deleted.

### Example

```javascript
import PlatformApi from 'platform_api';
let defaultClient = PlatformApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new PlatformApi.PushApi();
let deviceId = "deviceId_example"; // String | Device's ID.
let opts = {
  'xAblyVersion': "xAblyVersion_example", // String | The version of the API you wish to use.
  'format': "format_example" // String | The response format you would like
};
apiInstance.unregisterPushDevice(deviceId, opts, (error, data, response) => {
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
 **deviceId** | **String**| Device&#39;s ID. | 
 **xAblyVersion** | **String**| The version of the API you wish to use. | [optional] 
 **format** | **String**| The response format you would like | [optional] 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/x-msgpack, text/html


## updatePushDeviceDetails

> DeviceDetails updatePushDeviceDetails(deviceId, opts)

Reset a registered device&#39;s update token

Gets an updated device details object.

### Example

```javascript
import PlatformApi from 'platform_api';
let defaultClient = PlatformApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new PlatformApi.PushApi();
let deviceId = "deviceId_example"; // String | Device's ID.
let opts = {
  'xAblyVersion': "xAblyVersion_example", // String | The version of the API you wish to use.
  'format': "format_example" // String | The response format you would like
};
apiInstance.updatePushDeviceDetails(deviceId, opts, (error, data, response) => {
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
 **deviceId** | **String**| Device&#39;s ID. | 
 **xAblyVersion** | **String**| The version of the API you wish to use. | [optional] 
 **format** | **String**| The response format you would like | [optional] 

### Return type

[**DeviceDetails**](DeviceDetails.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/x-msgpack, text/html

