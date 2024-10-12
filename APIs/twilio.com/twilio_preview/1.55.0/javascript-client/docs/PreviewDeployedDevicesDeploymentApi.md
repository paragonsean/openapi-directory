# TwilioPreview.PreviewDeployedDevicesDeploymentApi

All URIs are relative to *https://preview.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createDeployedDevicesDeployment**](PreviewDeployedDevicesDeploymentApi.md#createDeployedDevicesDeployment) | **POST** /DeployedDevices/Fleets/{FleetSid}/Deployments | 
[**deleteDeployedDevicesDeployment**](PreviewDeployedDevicesDeploymentApi.md#deleteDeployedDevicesDeployment) | **DELETE** /DeployedDevices/Fleets/{FleetSid}/Deployments/{Sid} | 
[**fetchDeployedDevicesDeployment**](PreviewDeployedDevicesDeploymentApi.md#fetchDeployedDevicesDeployment) | **GET** /DeployedDevices/Fleets/{FleetSid}/Deployments/{Sid} | 
[**listDeployedDevicesDeployment**](PreviewDeployedDevicesDeploymentApi.md#listDeployedDevicesDeployment) | **GET** /DeployedDevices/Fleets/{FleetSid}/Deployments | 
[**updateDeployedDevicesDeployment**](PreviewDeployedDevicesDeploymentApi.md#updateDeployedDevicesDeployment) | **POST** /DeployedDevices/Fleets/{FleetSid}/Deployments/{Sid} | 



## createDeployedDevicesDeployment

> PreviewDeployedDevicesFleetDeployment createDeployedDevicesDeployment(fleetSid, opts)



Create a new Deployment in the Fleet, optionally giving it a friendly name and linking to a specific Twilio Sync service instance.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewDeployedDevicesDeploymentApi();
let fleetSid = "fleetSid_example"; // String | 
let opts = {
  'friendlyName': "friendlyName_example", // String | Provides a human readable descriptive text for this Deployment, up to 256 characters long.
  'syncServiceSid': "syncServiceSid_example" // String | Provides the unique string identifier of the Twilio Sync service instance that will be linked to and accessible by this Deployment.
};
apiInstance.createDeployedDevicesDeployment(fleetSid, opts, (error, data, response) => {
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
 **friendlyName** | **String**| Provides a human readable descriptive text for this Deployment, up to 256 characters long. | [optional] 
 **syncServiceSid** | **String**| Provides the unique string identifier of the Twilio Sync service instance that will be linked to and accessible by this Deployment. | [optional] 

### Return type

[**PreviewDeployedDevicesFleetDeployment**](PreviewDeployedDevicesFleetDeployment.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteDeployedDevicesDeployment

> deleteDeployedDevicesDeployment(fleetSid, sid)



Delete a specific Deployment from the Fleet, leaving associated devices effectively undeployed.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewDeployedDevicesDeploymentApi();
let fleetSid = "fleetSid_example"; // String | 
let sid = "sid_example"; // String | Provides a 34 character string that uniquely identifies the requested Deployment resource.
apiInstance.deleteDeployedDevicesDeployment(fleetSid, sid, (error, data, response) => {
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
 **sid** | **String**| Provides a 34 character string that uniquely identifies the requested Deployment resource. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchDeployedDevicesDeployment

> PreviewDeployedDevicesFleetDeployment fetchDeployedDevicesDeployment(fleetSid, sid)



Fetch information about a specific Deployment in the Fleet.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewDeployedDevicesDeploymentApi();
let fleetSid = "fleetSid_example"; // String | 
let sid = "sid_example"; // String | Provides a 34 character string that uniquely identifies the requested Deployment resource.
apiInstance.fetchDeployedDevicesDeployment(fleetSid, sid, (error, data, response) => {
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
 **sid** | **String**| Provides a 34 character string that uniquely identifies the requested Deployment resource. | 

### Return type

[**PreviewDeployedDevicesFleetDeployment**](PreviewDeployedDevicesFleetDeployment.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDeployedDevicesDeployment

> ListDeployedDevicesDeploymentResponse listDeployedDevicesDeployment(fleetSid, opts)



Retrieve a list of all Deployments belonging to the Fleet.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewDeployedDevicesDeploymentApi();
let fleetSid = "fleetSid_example"; // String | 
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listDeployedDevicesDeployment(fleetSid, opts, (error, data, response) => {
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
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListDeployedDevicesDeploymentResponse**](ListDeployedDevicesDeploymentResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateDeployedDevicesDeployment

> PreviewDeployedDevicesFleetDeployment updateDeployedDevicesDeployment(fleetSid, sid, opts)



Update the given properties of a specific Deployment credential in the Fleet, giving it a friendly name or linking to a specific Twilio Sync service instance.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewDeployedDevicesDeploymentApi();
let fleetSid = "fleetSid_example"; // String | 
let sid = "sid_example"; // String | Provides a 34 character string that uniquely identifies the requested Deployment resource.
let opts = {
  'friendlyName': "friendlyName_example", // String | Provides a human readable descriptive text for this Deployment, up to 64 characters long
  'syncServiceSid': "syncServiceSid_example" // String | Provides the unique string identifier of the Twilio Sync service instance that will be linked to and accessible by this Deployment.
};
apiInstance.updateDeployedDevicesDeployment(fleetSid, sid, opts, (error, data, response) => {
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
 **sid** | **String**| Provides a 34 character string that uniquely identifies the requested Deployment resource. | 
 **friendlyName** | **String**| Provides a human readable descriptive text for this Deployment, up to 64 characters long | [optional] 
 **syncServiceSid** | **String**| Provides the unique string identifier of the Twilio Sync service instance that will be linked to and accessible by this Deployment. | [optional] 

### Return type

[**PreviewDeployedDevicesFleetDeployment**](PreviewDeployedDevicesFleetDeployment.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

