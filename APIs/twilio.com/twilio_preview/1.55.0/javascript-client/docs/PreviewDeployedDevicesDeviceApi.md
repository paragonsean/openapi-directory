# TwilioPreview.PreviewDeployedDevicesDeviceApi

All URIs are relative to *https://preview.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createDeployedDevicesDevice**](PreviewDeployedDevicesDeviceApi.md#createDeployedDevicesDevice) | **POST** /DeployedDevices/Fleets/{FleetSid}/Devices | 
[**deleteDeployedDevicesDevice**](PreviewDeployedDevicesDeviceApi.md#deleteDeployedDevicesDevice) | **DELETE** /DeployedDevices/Fleets/{FleetSid}/Devices/{Sid} | 
[**fetchDeployedDevicesDevice**](PreviewDeployedDevicesDeviceApi.md#fetchDeployedDevicesDevice) | **GET** /DeployedDevices/Fleets/{FleetSid}/Devices/{Sid} | 
[**listDeployedDevicesDevice**](PreviewDeployedDevicesDeviceApi.md#listDeployedDevicesDevice) | **GET** /DeployedDevices/Fleets/{FleetSid}/Devices | 
[**updateDeployedDevicesDevice**](PreviewDeployedDevicesDeviceApi.md#updateDeployedDevicesDevice) | **POST** /DeployedDevices/Fleets/{FleetSid}/Devices/{Sid} | 



## createDeployedDevicesDevice

> PreviewDeployedDevicesFleetDevice createDeployedDevicesDevice(fleetSid, opts)



Create a new Device in the Fleet, optionally giving it a unique name, friendly name, and assigning to a Deployment and/or human identity.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewDeployedDevicesDeviceApi();
let fleetSid = "fleetSid_example"; // String | 
let opts = {
  'deploymentSid': "deploymentSid_example", // String | Specifies the unique string identifier of the Deployment group that this Device is going to be associated with.
  'enabled': true, // Boolean | 
  'friendlyName': "friendlyName_example", // String | Provides a human readable descriptive text to be assigned to this Device, up to 256 characters long.
  'identity': "identity_example", // String | Provides an arbitrary string identifier representing a human user to be associated with this Device, up to 256 characters long.
  'uniqueName': "uniqueName_example" // String | Provides a unique and addressable name to be assigned to this Device, to be used in addition to SID, up to 128 characters long.
};
apiInstance.createDeployedDevicesDevice(fleetSid, opts, (error, data, response) => {
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
 **fleetSid** | **String**|  | 
 **deploymentSid** | **String**| Specifies the unique string identifier of the Deployment group that this Device is going to be associated with. | [optional] 
 **enabled** | **Boolean**|  | [optional] 
 **friendlyName** | **String**| Provides a human readable descriptive text to be assigned to this Device, up to 256 characters long. | [optional] 
 **identity** | **String**| Provides an arbitrary string identifier representing a human user to be associated with this Device, up to 256 characters long. | [optional] 
 **uniqueName** | **String**| Provides a unique and addressable name to be assigned to this Device, to be used in addition to SID, up to 128 characters long. | [optional] 

### Return type

[**PreviewDeployedDevicesFleetDevice**](PreviewDeployedDevicesFleetDevice.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteDeployedDevicesDevice

> deleteDeployedDevicesDevice(fleetSid, sid)



Delete a specific Device from the Fleet, also removing it from associated Deployments.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewDeployedDevicesDeviceApi();
let fleetSid = "fleetSid_example"; // String | 
let sid = "sid_example"; // String | Provides a 34 character string that uniquely identifies the requested Device resource.
apiInstance.deleteDeployedDevicesDevice(fleetSid, sid, (error, data, response) => {
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
 **fleetSid** | **String**|  | 
 **sid** | **String**| Provides a 34 character string that uniquely identifies the requested Device resource. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchDeployedDevicesDevice

> PreviewDeployedDevicesFleetDevice fetchDeployedDevicesDevice(fleetSid, sid)



Fetch information about a specific Device in the Fleet.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewDeployedDevicesDeviceApi();
let fleetSid = "fleetSid_example"; // String | 
let sid = "sid_example"; // String | Provides a 34 character string that uniquely identifies the requested Device resource.
apiInstance.fetchDeployedDevicesDevice(fleetSid, sid, (error, data, response) => {
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
 **fleetSid** | **String**|  | 
 **sid** | **String**| Provides a 34 character string that uniquely identifies the requested Device resource. | 

### Return type

[**PreviewDeployedDevicesFleetDevice**](PreviewDeployedDevicesFleetDevice.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDeployedDevicesDevice

> ListDeployedDevicesDeviceResponse listDeployedDevicesDevice(fleetSid, opts)



Retrieve a list of all Devices belonging to the Fleet.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewDeployedDevicesDeviceApi();
let fleetSid = "fleetSid_example"; // String | 
let opts = {
  'deploymentSid': "deploymentSid_example", // String | Filters the resulting list of Devices by a unique string identifier of the Deployment they are associated with.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listDeployedDevicesDevice(fleetSid, opts, (error, data, response) => {
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
 **fleetSid** | **String**|  | 
 **deploymentSid** | **String**| Filters the resulting list of Devices by a unique string identifier of the Deployment they are associated with. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListDeployedDevicesDeviceResponse**](ListDeployedDevicesDeviceResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateDeployedDevicesDevice

> PreviewDeployedDevicesFleetDevice updateDeployedDevicesDevice(fleetSid, sid, opts)



Update the given properties of a specific Device in the Fleet, giving it a friendly name, assigning to a Deployment, or a human identity.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewDeployedDevicesDeviceApi();
let fleetSid = "fleetSid_example"; // String | 
let sid = "sid_example"; // String | Provides a 34 character string that uniquely identifies the requested Device resource.
let opts = {
  'deploymentSid': "deploymentSid_example", // String | Specifies the unique string identifier of the Deployment group that this Device is going to be associated with.
  'enabled': true, // Boolean | 
  'friendlyName': "friendlyName_example", // String | Provides a human readable descriptive text to be assigned to this Device, up to 256 characters long.
  'identity': "identity_example" // String | Provides an arbitrary string identifier representing a human user to be associated with this Device, up to 256 characters long.
};
apiInstance.updateDeployedDevicesDevice(fleetSid, sid, opts, (error, data, response) => {
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
 **fleetSid** | **String**|  | 
 **sid** | **String**| Provides a 34 character string that uniquely identifies the requested Device resource. | 
 **deploymentSid** | **String**| Specifies the unique string identifier of the Deployment group that this Device is going to be associated with. | [optional] 
 **enabled** | **Boolean**|  | [optional] 
 **friendlyName** | **String**| Provides a human readable descriptive text to be assigned to this Device, up to 256 characters long. | [optional] 
 **identity** | **String**| Provides an arbitrary string identifier representing a human user to be associated with this Device, up to 256 characters long. | [optional] 

### Return type

[**PreviewDeployedDevicesFleetDevice**](PreviewDeployedDevicesFleetDevice.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

