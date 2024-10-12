# TwilioPreview.PreviewDeployedDevicesFleetApi

All URIs are relative to *https://preview.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createDeployedDevicesFleet**](PreviewDeployedDevicesFleetApi.md#createDeployedDevicesFleet) | **POST** /DeployedDevices/Fleets | 
[**deleteDeployedDevicesFleet**](PreviewDeployedDevicesFleetApi.md#deleteDeployedDevicesFleet) | **DELETE** /DeployedDevices/Fleets/{Sid} | 
[**fetchDeployedDevicesFleet**](PreviewDeployedDevicesFleetApi.md#fetchDeployedDevicesFleet) | **GET** /DeployedDevices/Fleets/{Sid} | 
[**listDeployedDevicesFleet**](PreviewDeployedDevicesFleetApi.md#listDeployedDevicesFleet) | **GET** /DeployedDevices/Fleets | 
[**updateDeployedDevicesFleet**](PreviewDeployedDevicesFleetApi.md#updateDeployedDevicesFleet) | **POST** /DeployedDevices/Fleets/{Sid} | 



## createDeployedDevicesFleet

> PreviewDeployedDevicesFleet createDeployedDevicesFleet(opts)



Create a new Fleet for scoping of deployed devices within your account.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewDeployedDevicesFleetApi();
let opts = {
  'friendlyName': "friendlyName_example" // String | Provides a human readable descriptive text for this Fleet, up to 256 characters long.
};
apiInstance.createDeployedDevicesFleet(opts, (error, data, response) => {
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
 **friendlyName** | **String**| Provides a human readable descriptive text for this Fleet, up to 256 characters long. | [optional] 

### Return type

[**PreviewDeployedDevicesFleet**](PreviewDeployedDevicesFleet.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteDeployedDevicesFleet

> deleteDeployedDevicesFleet(sid)



Delete a specific Fleet from your account, also destroys all nested resources: Devices, Deployments, Certificates, Keys.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewDeployedDevicesFleetApi();
let sid = "sid_example"; // String | Provides a 34 character string that uniquely identifies the requested Fleet resource.
apiInstance.deleteDeployedDevicesFleet(sid, (error, data, response) => {
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
 **sid** | **String**| Provides a 34 character string that uniquely identifies the requested Fleet resource. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchDeployedDevicesFleet

> PreviewDeployedDevicesFleet fetchDeployedDevicesFleet(sid)



Fetch information about a specific Fleet in your account.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewDeployedDevicesFleetApi();
let sid = "sid_example"; // String | Provides a 34 character string that uniquely identifies the requested Fleet resource.
apiInstance.fetchDeployedDevicesFleet(sid, (error, data, response) => {
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
 **sid** | **String**| Provides a 34 character string that uniquely identifies the requested Fleet resource. | 

### Return type

[**PreviewDeployedDevicesFleet**](PreviewDeployedDevicesFleet.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDeployedDevicesFleet

> ListDeployedDevicesFleetResponse listDeployedDevicesFleet(opts)



Retrieve a list of all Fleets belonging to your account.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewDeployedDevicesFleetApi();
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listDeployedDevicesFleet(opts, (error, data, response) => {
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
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListDeployedDevicesFleetResponse**](ListDeployedDevicesFleetResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateDeployedDevicesFleet

> PreviewDeployedDevicesFleet updateDeployedDevicesFleet(sid, opts)



Update the friendly name property of a specific Fleet in your account.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewDeployedDevicesFleetApi();
let sid = "sid_example"; // String | Provides a 34 character string that uniquely identifies the requested Fleet resource.
let opts = {
  'defaultDeploymentSid': "defaultDeploymentSid_example", // String | Provides a string identifier of a Deployment that is going to be used as a default one for this Fleet.
  'friendlyName': "friendlyName_example" // String | Provides a human readable descriptive text for this Fleet, up to 256 characters long.
};
apiInstance.updateDeployedDevicesFleet(sid, opts, (error, data, response) => {
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
 **sid** | **String**| Provides a 34 character string that uniquely identifies the requested Fleet resource. | 
 **defaultDeploymentSid** | **String**| Provides a string identifier of a Deployment that is going to be used as a default one for this Fleet. | [optional] 
 **friendlyName** | **String**| Provides a human readable descriptive text for this Fleet, up to 256 characters long. | [optional] 

### Return type

[**PreviewDeployedDevicesFleet**](PreviewDeployedDevicesFleet.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

