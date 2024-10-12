# EnodeApi.ChargersApi

All URIs are relative to *https://api.test.enode.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**controlChargerCharging**](ChargersApi.md#controlChargerCharging) | **POST** /chargers/{chargerId}/charging | Control Charging
[**getCharger**](ChargersApi.md#getCharger) | **GET** /chargers/{chargerId} | Get Charger
[**getChargers**](ChargersApi.md#getChargers) | **GET** /chargers | List Chargers



## controlChargerCharging

> controlChargerCharging(chargerId, opts)

Control Charging

Instruct the charger to start or stop charging

### Example

```javascript
import EnodeApi from 'enode_api';
let defaultClient = EnodeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: UserAccessToken
let UserAccessToken = defaultClient.authentications['UserAccessToken'];
UserAccessToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EnodeApi.ChargersApi();
let chargerId = "chargerId_example"; // String | ID of the Charger
let opts = {
  'controlChargerChargingRequest': new EnodeApi.ControlChargerChargingRequest() // ControlChargerChargingRequest | 
};
apiInstance.controlChargerCharging(chargerId, opts, (error, data, response) => {
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
 **chargerId** | **String**| ID of the Charger | 
 **controlChargerChargingRequest** | [**ControlChargerChargingRequest**](ControlChargerChargingRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[UserAccessToken](../README.md#UserAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## getCharger

> GetCharger200Response getCharger(chargerId)

Get Charger

### Example

```javascript
import EnodeApi from 'enode_api';
let defaultClient = EnodeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: UserAccessToken
let UserAccessToken = defaultClient.authentications['UserAccessToken'];
UserAccessToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EnodeApi.ChargersApi();
let chargerId = "chargerId_example"; // String | ID of the Charger
apiInstance.getCharger(chargerId, (error, data, response) => {
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
 **chargerId** | **String**| ID of the Charger | 

### Return type

[**GetCharger200Response**](GetCharger200Response.md)

### Authorization

[UserAccessToken](../README.md#UserAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getChargers

> [Object] getChargers(opts)

List Chargers

### Example

```javascript
import EnodeApi from 'enode_api';
let defaultClient = EnodeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: UserAccessToken
let UserAccessToken = defaultClient.authentications['UserAccessToken'];
UserAccessToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EnodeApi.ChargersApi();
let opts = {
  'field': ["null"] // [String] | An optional array of Charger fields that should be included in the response, for example: `?field[]=information&field[]=chargeState`   By default, no optional fields are included and only the Charger ID will be returned. Response time will generally be slower the more fields you request.
};
apiInstance.getChargers(opts, (error, data, response) => {
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
 **field** | [**[String]**](String.md)| An optional array of Charger fields that should be included in the response, for example: &#x60;?field[]&#x3D;information&amp;field[]&#x3D;chargeState&#x60;   By default, no optional fields are included and only the Charger ID will be returned. Response time will generally be slower the more fields you request. | [optional] 

### Return type

**[Object]**

### Authorization

[UserAccessToken](../README.md#UserAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

