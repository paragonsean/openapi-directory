# EnodeApi.VehiclesApi

All URIs are relative to *https://api.test.enode.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getVehicleChargestate**](VehiclesApi.md#getVehicleChargestate) | **GET** /vehicles/{vehicleId}/charge-state | Get Vehicle Charge State
[**getVehicles**](VehiclesApi.md#getVehicles) | **GET** /vehicles | List Vehicles
[**getVehiclesVehicleid**](VehiclesApi.md#getVehiclesVehicleid) | **GET** /vehicles/{vehicleId} | Get Vehicle
[**getVehiclesVehicleidInformation**](VehiclesApi.md#getVehiclesVehicleidInformation) | **GET** /vehicles/{vehicleId}/information | Get Vehicle Information
[**getVehiclesVehicleidLocation**](VehiclesApi.md#getVehiclesVehicleidLocation) | **GET** /vehicles/{vehicleId}/location | Get Vehicle Location
[**getVehiclesVehicleidOdometer**](VehiclesApi.md#getVehiclesVehicleidOdometer) | **GET** /vehicles/{vehicleId}/odometer | Get Vehicle Odometer
[**getVehiclesVehicleidSmartchargingpolicy**](VehiclesApi.md#getVehiclesVehicleidSmartchargingpolicy) | **GET** /vehicles/{vehicleId}/smart-charging-policy | Get Vehicle Smart Charging Policy
[**postVehiclesVehicleidCharging**](VehiclesApi.md#postVehiclesVehicleidCharging) | **POST** /vehicles/{vehicleId}/charging | Start / Stop Charging
[**postVehiclesVehicleidWatch**](VehiclesApi.md#postVehiclesVehicleidWatch) | **POST** /vehicles/{vehicleId}/watch | Start Watching Vehicle
[**putVehiclesVehicleidSmartchargingpolicy**](VehiclesApi.md#putVehiclesVehicleidSmartchargingpolicy) | **PUT** /vehicles/{vehicleId}/smart-charging-policy | Update Vehicle Smart Charging Policy



## getVehicleChargestate

> GetVehicleChargestate200Response getVehicleChargestate()

Get Vehicle Charge State

### Example

```javascript
import EnodeApi from 'enode_api';
let defaultClient = EnodeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: UserAccessToken
let UserAccessToken = defaultClient.authentications['UserAccessToken'];
UserAccessToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EnodeApi.VehiclesApi();
apiInstance.getVehicleChargestate((error, data, response) => {
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

[**GetVehicleChargestate200Response**](GetVehicleChargestate200Response.md)

### Authorization

[UserAccessToken](../README.md#UserAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVehicles

> [Object] getVehicles(opts)

List Vehicles

### Example

```javascript
import EnodeApi from 'enode_api';
let defaultClient = EnodeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: UserAccessToken
let UserAccessToken = defaultClient.authentications['UserAccessToken'];
UserAccessToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EnodeApi.VehiclesApi();
let opts = {
  'field': [null] // [Object] | An optional array of Vehicle fields that should be included in the response, for example: `?field[]=information&field[]=location`   By default, no fields are included and only the Vehicle ID will be returned. Response time may be impacted by which fields you request.
};
apiInstance.getVehicles(opts, (error, data, response) => {
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
 **field** | [**[Object]**](Object.md)| An optional array of Vehicle fields that should be included in the response, for example: &#x60;?field[]&#x3D;information&amp;field[]&#x3D;location&#x60;   By default, no fields are included and only the Vehicle ID will be returned. Response time may be impacted by which fields you request. | [optional] 

### Return type

**[Object]**

### Authorization

[UserAccessToken](../README.md#UserAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVehiclesVehicleid

> GetVehiclesVehicleid200Response getVehiclesVehicleid(vehicleId, opts)

Get Vehicle

### Example

```javascript
import EnodeApi from 'enode_api';
let defaultClient = EnodeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: UserAccessToken
let UserAccessToken = defaultClient.authentications['UserAccessToken'];
UserAccessToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EnodeApi.VehiclesApi();
let vehicleId = "vehicleId_example"; // String | ID of the Vehicle
let opts = {
  'field': ["null"] // [String] | An optional array of Vehicle fields that should be included in the response, for example: `?field[]=information&field[]=location`   By default, no fields are included and only the Vehicle ID will be returned. Response time may be impacted by which fields you request.
};
apiInstance.getVehiclesVehicleid(vehicleId, opts, (error, data, response) => {
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
 **vehicleId** | **String**| ID of the Vehicle | 
 **field** | [**[String]**](String.md)| An optional array of Vehicle fields that should be included in the response, for example: &#x60;?field[]&#x3D;information&amp;field[]&#x3D;location&#x60;   By default, no fields are included and only the Vehicle ID will be returned. Response time may be impacted by which fields you request. | [optional] 

### Return type

[**GetVehiclesVehicleid200Response**](GetVehiclesVehicleid200Response.md)

### Authorization

[UserAccessToken](../README.md#UserAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVehiclesVehicleidInformation

> GetVehiclesVehicleidInformation200Response getVehiclesVehicleidInformation()

Get Vehicle Information

### Example

```javascript
import EnodeApi from 'enode_api';
let defaultClient = EnodeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: UserAccessToken
let UserAccessToken = defaultClient.authentications['UserAccessToken'];
UserAccessToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EnodeApi.VehiclesApi();
apiInstance.getVehiclesVehicleidInformation((error, data, response) => {
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

[**GetVehiclesVehicleidInformation200Response**](GetVehiclesVehicleidInformation200Response.md)

### Authorization

[UserAccessToken](../README.md#UserAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVehiclesVehicleidLocation

> GetVehiclesVehicleidLocation200Response getVehiclesVehicleidLocation()

Get Vehicle Location

### Example

```javascript
import EnodeApi from 'enode_api';
let defaultClient = EnodeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: UserAccessToken
let UserAccessToken = defaultClient.authentications['UserAccessToken'];
UserAccessToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EnodeApi.VehiclesApi();
apiInstance.getVehiclesVehicleidLocation((error, data, response) => {
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

[**GetVehiclesVehicleidLocation200Response**](GetVehiclesVehicleidLocation200Response.md)

### Authorization

[UserAccessToken](../README.md#UserAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVehiclesVehicleidOdometer

> GetVehiclesVehicleidOdometer200Response getVehiclesVehicleidOdometer()

Get Vehicle Odometer

### Example

```javascript
import EnodeApi from 'enode_api';
let defaultClient = EnodeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: UserAccessToken
let UserAccessToken = defaultClient.authentications['UserAccessToken'];
UserAccessToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EnodeApi.VehiclesApi();
apiInstance.getVehiclesVehicleidOdometer((error, data, response) => {
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

[**GetVehiclesVehicleidOdometer200Response**](GetVehiclesVehicleidOdometer200Response.md)

### Authorization

[UserAccessToken](../README.md#UserAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVehiclesVehicleidSmartchargingpolicy

> Object getVehiclesVehicleidSmartchargingpolicy()

Get Vehicle Smart Charging Policy

### Example

```javascript
import EnodeApi from 'enode_api';
let defaultClient = EnodeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: UserAccessToken
let UserAccessToken = defaultClient.authentications['UserAccessToken'];
UserAccessToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EnodeApi.VehiclesApi();
apiInstance.getVehiclesVehicleidSmartchargingpolicy((error, data, response) => {
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

**Object**

### Authorization

[UserAccessToken](../README.md#UserAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postVehiclesVehicleidCharging

> postVehiclesVehicleidCharging()

Start / Stop Charging

Instruct the vehicle to start or stop charging.   #### Precedence over smart charging If the vehicle is at a charging location where smart charging is activated: - a request to &#x60;start&#x60; charging will override smart charging and charging will stay on until fully charged.  - a request to &#x60;stop&#x60; charging will override smart charging and charging will be kept off for the duration of the current smart charging cycle.  The smart charging settings are not altered by these actions.

### Example

```javascript
import EnodeApi from 'enode_api';
let defaultClient = EnodeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: UserAccessToken
let UserAccessToken = defaultClient.authentications['UserAccessToken'];
UserAccessToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EnodeApi.VehiclesApi();
apiInstance.postVehiclesVehicleidCharging((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[UserAccessToken](../README.md#UserAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postVehiclesVehicleidWatch

> Object postVehiclesVehicleidWatch(vehicleId, opts)

Start Watching Vehicle

Temporarily triggers high-rate updates of the vehicle&#39;s properties, and this state expires automatically. This gives you a way to tell us that user may be interacting with your application and are expecting as-fast-as-possible updates on the status of their vehicle in your UI.  Any data changes resulting from this high-rate updating are reflected everywhere, whether you pull data from the &#x60;Vehicles&#x60; endpoint, or recieve it via the [Firehose Webhook](#tag/Webhooks)  The specifics of the expiration times, watch behaviors, and change thresholds are tuned by us to make sure that they work as expected, without causing undue interruption to the vehicle. For many vendors, it is not appropriate to let the high-rate monitoring last indefinitely, as it will keep systems within the car awake that should be allowed to fall into low-power/standby modes. 

### Example

```javascript
import EnodeApi from 'enode_api';
let defaultClient = EnodeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: UserAccessToken
let UserAccessToken = defaultClient.authentications['UserAccessToken'];
UserAccessToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EnodeApi.VehiclesApi();
let vehicleId = "vehicleId_example"; // String | ID of the Vehicle
let opts = {
  'postVehiclesVehicleidWatchRequest': new EnodeApi.PostVehiclesVehicleidWatchRequest() // PostVehiclesVehicleidWatchRequest | 
};
apiInstance.postVehiclesVehicleidWatch(vehicleId, opts, (error, data, response) => {
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
 **vehicleId** | **String**| ID of the Vehicle | 
 **postVehiclesVehicleidWatchRequest** | [**PostVehiclesVehicleidWatchRequest**](PostVehiclesVehicleidWatchRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[UserAccessToken](../README.md#UserAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putVehiclesVehicleidSmartchargingpolicy

> Object putVehiclesVehicleidSmartchargingpolicy(vehicleId, opts)

Update Vehicle Smart Charging Policy

Updates the Smart Charging settings for a vehicle

### Example

```javascript
import EnodeApi from 'enode_api';
let defaultClient = EnodeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: UserAccessToken
let UserAccessToken = defaultClient.authentications['UserAccessToken'];
UserAccessToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EnodeApi.VehiclesApi();
let vehicleId = "vehicleId_example"; // String | ID of the Vehicle
let opts = {
  'putVehiclesVehicleidSmartchargingpolicyRequest': new EnodeApi.PutVehiclesVehicleidSmartchargingpolicyRequest() // PutVehiclesVehicleidSmartchargingpolicyRequest | 
};
apiInstance.putVehiclesVehicleidSmartchargingpolicy(vehicleId, opts, (error, data, response) => {
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
 **vehicleId** | **String**| ID of the Vehicle | 
 **putVehiclesVehicleidSmartchargingpolicyRequest** | [**PutVehiclesVehicleidSmartchargingpolicyRequest**](PutVehiclesVehicleidSmartchargingpolicyRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[UserAccessToken](../README.md#UserAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

