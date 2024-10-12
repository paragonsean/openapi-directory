# ShipEngineApi.CarrierAccountsApi

All URIs are relative to *https://api.shipengine.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connectCarrier**](CarrierAccountsApi.md#connectCarrier) | **POST** /v1/connections/carriers/{carrier_name} | Connect a carrier account
[**disconnectCarrier**](CarrierAccountsApi.md#disconnectCarrier) | **DELETE** /v1/connections/carriers/{carrier_name}/{carrier_id} | Disconnect a carrier
[**getCarrierSettings**](CarrierAccountsApi.md#getCarrierSettings) | **GET** /v1/connections/carriers/{carrier_name}/{carrier_id}/settings | Get carrier settings
[**updateCarrierSettings**](CarrierAccountsApi.md#updateCarrierSettings) | **PUT** /v1/connections/carriers/{carrier_name}/{carrier_id}/settings | Update carrier settings



## connectCarrier

> ConnectCarrierResponseBody connectCarrier(carrierName, connectCarrierRequestBody)

Connect a carrier account

Connect a carrier account

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.CarrierAccountsApi();
let carrierName = new ShipEngineApi.CarrierName(); // CarrierName | The carrier name, such as `stamps_com`, `ups`, `fedex`, or `dhl_express`.
let connectCarrierRequestBody = new ShipEngineApi.ConnectCarrierRequestBody(); // ConnectCarrierRequestBody | 
apiInstance.connectCarrier(carrierName, connectCarrierRequestBody, (error, data, response) => {
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
 **carrierName** | [**CarrierName**](.md)| The carrier name, such as &#x60;stamps_com&#x60;, &#x60;ups&#x60;, &#x60;fedex&#x60;, or &#x60;dhl_express&#x60;. | 
 **connectCarrierRequestBody** | [**ConnectCarrierRequestBody**](ConnectCarrierRequestBody.md)|  | 

### Return type

[**ConnectCarrierResponseBody**](ConnectCarrierResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## disconnectCarrier

> String disconnectCarrier(carrierName, carrierId)

Disconnect a carrier

Disconnect a carrier

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.CarrierAccountsApi();
let carrierName = new ShipEngineApi.CarrierName(); // CarrierName | The carrier name, such as `stamps_com`, `ups`, `fedex`, or `dhl_express`.
let carrierId = "se-28529731"; // String | Carrier ID
apiInstance.disconnectCarrier(carrierName, carrierId, (error, data, response) => {
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
 **carrierName** | [**CarrierName**](.md)| The carrier name, such as &#x60;stamps_com&#x60;, &#x60;ups&#x60;, &#x60;fedex&#x60;, or &#x60;dhl_express&#x60;. | 
 **carrierId** | **String**| Carrier ID | 

### Return type

**String**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/plain


## getCarrierSettings

> GetCarrierSettingsResponseBody getCarrierSettings(carrierName, carrierId)

Get carrier settings

Get carrier settings

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.CarrierAccountsApi();
let carrierName = new ShipEngineApi.CarrierNameWithSettings(); // CarrierNameWithSettings | The carrier name, such as `ups`, `fedex`, or `dhl_express`.
let carrierId = "se-28529731"; // String | Carrier ID
apiInstance.getCarrierSettings(carrierName, carrierId, (error, data, response) => {
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
 **carrierName** | [**CarrierNameWithSettings**](.md)| The carrier name, such as &#x60;ups&#x60;, &#x60;fedex&#x60;, or &#x60;dhl_express&#x60;. | 
 **carrierId** | **String**| Carrier ID | 

### Return type

[**GetCarrierSettingsResponseBody**](GetCarrierSettingsResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateCarrierSettings

> String updateCarrierSettings(carrierName, carrierId, updateCarrierSettingsRequestBody)

Update carrier settings

Update carrier settings

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.CarrierAccountsApi();
let carrierName = new ShipEngineApi.CarrierNameWithSettings(); // CarrierNameWithSettings | The carrier name, such as `ups`, `fedex`, or `dhl_express`.
let carrierId = "se-28529731"; // String | Carrier ID
let updateCarrierSettingsRequestBody = new ShipEngineApi.UpdateCarrierSettingsRequestBody(); // UpdateCarrierSettingsRequestBody | 
apiInstance.updateCarrierSettings(carrierName, carrierId, updateCarrierSettingsRequestBody, (error, data, response) => {
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
 **carrierName** | [**CarrierNameWithSettings**](.md)| The carrier name, such as &#x60;ups&#x60;, &#x60;fedex&#x60;, or &#x60;dhl_express&#x60;. | 
 **carrierId** | **String**| Carrier ID | 
 **updateCarrierSettingsRequestBody** | [**UpdateCarrierSettingsRequestBody**](UpdateCarrierSettingsRequestBody.md)|  | 

### Return type

**String**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/plain

