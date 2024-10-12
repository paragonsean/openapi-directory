# TwilioPreview.PreviewDeployedDevicesCertificateApi

All URIs are relative to *https://preview.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createDeployedDevicesCertificate**](PreviewDeployedDevicesCertificateApi.md#createDeployedDevicesCertificate) | **POST** /DeployedDevices/Fleets/{FleetSid}/Certificates | 
[**deleteDeployedDevicesCertificate**](PreviewDeployedDevicesCertificateApi.md#deleteDeployedDevicesCertificate) | **DELETE** /DeployedDevices/Fleets/{FleetSid}/Certificates/{Sid} | 
[**fetchDeployedDevicesCertificate**](PreviewDeployedDevicesCertificateApi.md#fetchDeployedDevicesCertificate) | **GET** /DeployedDevices/Fleets/{FleetSid}/Certificates/{Sid} | 
[**listDeployedDevicesCertificate**](PreviewDeployedDevicesCertificateApi.md#listDeployedDevicesCertificate) | **GET** /DeployedDevices/Fleets/{FleetSid}/Certificates | 
[**updateDeployedDevicesCertificate**](PreviewDeployedDevicesCertificateApi.md#updateDeployedDevicesCertificate) | **POST** /DeployedDevices/Fleets/{FleetSid}/Certificates/{Sid} | 



## createDeployedDevicesCertificate

> PreviewDeployedDevicesFleetCertificate createDeployedDevicesCertificate(fleetSid, certificateData, opts)



Enroll a new Certificate credential to the Fleet, optionally giving it a friendly name and assigning to a Device.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewDeployedDevicesCertificateApi();
let fleetSid = "fleetSid_example"; // String | 
let certificateData = "certificateData_example"; // String | Provides a URL encoded representation of the public certificate in PEM format.
let opts = {
  'deviceSid': "deviceSid_example", // String | Provides the unique string identifier of an existing Device to become authenticated with this Certificate credential.
  'friendlyName': "friendlyName_example" // String | Provides a human readable descriptive text for this Certificate credential, up to 256 characters long.
};
apiInstance.createDeployedDevicesCertificate(fleetSid, certificateData, opts, (error, data, response) => {
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
 **certificateData** | **String**| Provides a URL encoded representation of the public certificate in PEM format. | 
 **deviceSid** | **String**| Provides the unique string identifier of an existing Device to become authenticated with this Certificate credential. | [optional] 
 **friendlyName** | **String**| Provides a human readable descriptive text for this Certificate credential, up to 256 characters long. | [optional] 

### Return type

[**PreviewDeployedDevicesFleetCertificate**](PreviewDeployedDevicesFleetCertificate.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteDeployedDevicesCertificate

> deleteDeployedDevicesCertificate(fleetSid, sid)



Unregister a specific Certificate credential from the Fleet, effectively disallowing any inbound client connections that are presenting it.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewDeployedDevicesCertificateApi();
let fleetSid = "fleetSid_example"; // String | 
let sid = "sid_example"; // String | Provides a 34 character string that uniquely identifies the requested Certificate credential resource.
apiInstance.deleteDeployedDevicesCertificate(fleetSid, sid, (error, data, response) => {
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
 **sid** | **String**| Provides a 34 character string that uniquely identifies the requested Certificate credential resource. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchDeployedDevicesCertificate

> PreviewDeployedDevicesFleetCertificate fetchDeployedDevicesCertificate(fleetSid, sid)



Fetch information about a specific Certificate credential in the Fleet.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewDeployedDevicesCertificateApi();
let fleetSid = "fleetSid_example"; // String | 
let sid = "sid_example"; // String | Provides a 34 character string that uniquely identifies the requested Certificate credential resource.
apiInstance.fetchDeployedDevicesCertificate(fleetSid, sid, (error, data, response) => {
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
 **sid** | **String**| Provides a 34 character string that uniquely identifies the requested Certificate credential resource. | 

### Return type

[**PreviewDeployedDevicesFleetCertificate**](PreviewDeployedDevicesFleetCertificate.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDeployedDevicesCertificate

> ListDeployedDevicesCertificateResponse listDeployedDevicesCertificate(fleetSid, opts)



Retrieve a list of all Certificate credentials belonging to the Fleet.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewDeployedDevicesCertificateApi();
let fleetSid = "fleetSid_example"; // String | 
let opts = {
  'deviceSid': "deviceSid_example", // String | Filters the resulting list of Certificates by a unique string identifier of an authenticated Device.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listDeployedDevicesCertificate(fleetSid, opts, (error, data, response) => {
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
 **deviceSid** | **String**| Filters the resulting list of Certificates by a unique string identifier of an authenticated Device. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListDeployedDevicesCertificateResponse**](ListDeployedDevicesCertificateResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateDeployedDevicesCertificate

> PreviewDeployedDevicesFleetCertificate updateDeployedDevicesCertificate(fleetSid, sid, opts)



Update the given properties of a specific Certificate credential in the Fleet, giving it a friendly name or assigning to a Device.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewDeployedDevicesCertificateApi();
let fleetSid = "fleetSid_example"; // String | 
let sid = "sid_example"; // String | Provides a 34 character string that uniquely identifies the requested Certificate credential resource.
let opts = {
  'deviceSid': "deviceSid_example", // String | Provides the unique string identifier of an existing Device to become authenticated with this Certificate credential.
  'friendlyName': "friendlyName_example" // String | Provides a human readable descriptive text for this Certificate credential, up to 256 characters long.
};
apiInstance.updateDeployedDevicesCertificate(fleetSid, sid, opts, (error, data, response) => {
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
 **sid** | **String**| Provides a 34 character string that uniquely identifies the requested Certificate credential resource. | 
 **deviceSid** | **String**| Provides the unique string identifier of an existing Device to become authenticated with this Certificate credential. | [optional] 
 **friendlyName** | **String**| Provides a human readable descriptive text for this Certificate credential, up to 256 characters long. | [optional] 

### Return type

[**PreviewDeployedDevicesFleetCertificate**](PreviewDeployedDevicesFleetCertificate.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

