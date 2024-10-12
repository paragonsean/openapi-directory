# TwilioPreview.PreviewDeployedDevicesKeyApi

All URIs are relative to *https://preview.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createDeployedDevicesKey**](PreviewDeployedDevicesKeyApi.md#createDeployedDevicesKey) | **POST** /DeployedDevices/Fleets/{FleetSid}/Keys | 
[**deleteDeployedDevicesKey**](PreviewDeployedDevicesKeyApi.md#deleteDeployedDevicesKey) | **DELETE** /DeployedDevices/Fleets/{FleetSid}/Keys/{Sid} | 
[**fetchDeployedDevicesKey**](PreviewDeployedDevicesKeyApi.md#fetchDeployedDevicesKey) | **GET** /DeployedDevices/Fleets/{FleetSid}/Keys/{Sid} | 
[**listDeployedDevicesKey**](PreviewDeployedDevicesKeyApi.md#listDeployedDevicesKey) | **GET** /DeployedDevices/Fleets/{FleetSid}/Keys | 
[**updateDeployedDevicesKey**](PreviewDeployedDevicesKeyApi.md#updateDeployedDevicesKey) | **POST** /DeployedDevices/Fleets/{FleetSid}/Keys/{Sid} | 



## createDeployedDevicesKey

> PreviewDeployedDevicesFleetKey createDeployedDevicesKey(fleetSid, opts)



Create a new Key credential in the Fleet, optionally giving it a friendly name and assigning to a Device.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewDeployedDevicesKeyApi();
let fleetSid = "fleetSid_example"; // String | 
let opts = {
  'deviceSid': "deviceSid_example", // String | Provides the unique string identifier of an existing Device to become authenticated with this Key credential.
  'friendlyName': "friendlyName_example" // String | Provides a human readable descriptive text for this Key credential, up to 256 characters long.
};
apiInstance.createDeployedDevicesKey(fleetSid, opts, (error, data, response) => {
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
 **deviceSid** | **String**| Provides the unique string identifier of an existing Device to become authenticated with this Key credential. | [optional] 
 **friendlyName** | **String**| Provides a human readable descriptive text for this Key credential, up to 256 characters long. | [optional] 

### Return type

[**PreviewDeployedDevicesFleetKey**](PreviewDeployedDevicesFleetKey.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteDeployedDevicesKey

> deleteDeployedDevicesKey(fleetSid, sid)



Delete a specific Key credential from the Fleet, effectively disallowing any inbound client connections that are presenting it.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewDeployedDevicesKeyApi();
let fleetSid = "fleetSid_example"; // String | 
let sid = "sid_example"; // String | Provides a 34 character string that uniquely identifies the requested Key credential resource.
apiInstance.deleteDeployedDevicesKey(fleetSid, sid, (error, data, response) => {
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
 **sid** | **String**| Provides a 34 character string that uniquely identifies the requested Key credential resource. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchDeployedDevicesKey

> PreviewDeployedDevicesFleetKey fetchDeployedDevicesKey(fleetSid, sid)



Fetch information about a specific Key credential in the Fleet.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewDeployedDevicesKeyApi();
let fleetSid = "fleetSid_example"; // String | 
let sid = "sid_example"; // String | Provides a 34 character string that uniquely identifies the requested Key credential resource.
apiInstance.fetchDeployedDevicesKey(fleetSid, sid, (error, data, response) => {
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
 **sid** | **String**| Provides a 34 character string that uniquely identifies the requested Key credential resource. | 

### Return type

[**PreviewDeployedDevicesFleetKey**](PreviewDeployedDevicesFleetKey.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDeployedDevicesKey

> ListDeployedDevicesKeyResponse listDeployedDevicesKey(fleetSid, opts)



Retrieve a list of all Keys credentials belonging to the Fleet.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewDeployedDevicesKeyApi();
let fleetSid = "fleetSid_example"; // String | 
let opts = {
  'deviceSid': "deviceSid_example", // String | Filters the resulting list of Keys by a unique string identifier of an authenticated Device.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listDeployedDevicesKey(fleetSid, opts, (error, data, response) => {
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
 **deviceSid** | **String**| Filters the resulting list of Keys by a unique string identifier of an authenticated Device. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListDeployedDevicesKeyResponse**](ListDeployedDevicesKeyResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateDeployedDevicesKey

> PreviewDeployedDevicesFleetKey updateDeployedDevicesKey(fleetSid, sid, opts)



Update the given properties of a specific Key credential in the Fleet, giving it a friendly name or assigning to a Device.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewDeployedDevicesKeyApi();
let fleetSid = "fleetSid_example"; // String | 
let sid = "sid_example"; // String | Provides a 34 character string that uniquely identifies the requested Key credential resource.
let opts = {
  'deviceSid': "deviceSid_example", // String | Provides the unique string identifier of an existing Device to become authenticated with this Key credential.
  'friendlyName': "friendlyName_example" // String | Provides a human readable descriptive text for this Key credential, up to 256 characters long.
};
apiInstance.updateDeployedDevicesKey(fleetSid, sid, opts, (error, data, response) => {
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
 **sid** | **String**| Provides a 34 character string that uniquely identifies the requested Key credential resource. | 
 **deviceSid** | **String**| Provides the unique string identifier of an existing Device to become authenticated with this Key credential. | [optional] 
 **friendlyName** | **String**| Provides a human readable descriptive text for this Key credential, up to 256 characters long. | [optional] 

### Return type

[**PreviewDeployedDevicesFleetKey**](PreviewDeployedDevicesFleetKey.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

