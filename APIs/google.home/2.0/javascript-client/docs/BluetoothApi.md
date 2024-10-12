# GoogleHome.BluetoothApi

All URIs are relative to *http://example.com/setup*

Method | HTTP request | Description
------------- | ------------- | -------------
[**changeDiscoverability**](BluetoothApi.md#changeDiscoverability) | **POST** /bluetooth/discovery | Change Discoverability
[**forgetpaireddevice**](BluetoothApi.md#forgetpaireddevice) | **POST** /bluetooth/bond | Forget paired device
[**getPairedDevices**](BluetoothApi.md#getPairedDevices) | **GET** /bluetooth/get_bonded | Get Paired Devices
[**getScanResults**](BluetoothApi.md#getScanResults) | **GET** /bluetooth/scan_results | Get Scan Results
[**pairwithSpeaker**](BluetoothApi.md#pairwithSpeaker) | **POST** /bluetooth/connect | Pair with Speaker
[**scanfordevices**](BluetoothApi.md#scanfordevices) | **POST** /bluetooth/scan | Scan for devices
[**status**](BluetoothApi.md#status) | **GET** /bluetooth/status | Status



## changeDiscoverability

> Object changeDiscoverability(changeDiscoverabilityRequest)

Change Discoverability

*See note for Bluetooth under &#x60;/setup/bluetooth/status&#x60;*  **For Part 1 only**  This enables/disables Home&#39;s bluetooth discovery and other devices can pair with Home (where Home acts as a speaker).

### Example

```javascript
import GoogleHome from 'google_home';
let defaultClient = GoogleHome.ApiClient.instance;
// Configure API key authorization: cast-local-authorization-token
let cast-local-authorization-token = defaultClient.authentications['cast-local-authorization-token'];
cast-local-authorization-token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cast-local-authorization-token.apiKeyPrefix = 'Token';

let apiInstance = new GoogleHome.BluetoothApi();
let changeDiscoverabilityRequest = {"enable_discovery":true}; // ChangeDiscoverabilityRequest | 
apiInstance.changeDiscoverability(changeDiscoverabilityRequest, (error, data, response) => {
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
 **changeDiscoverabilityRequest** | [**ChangeDiscoverabilityRequest**](ChangeDiscoverabilityRequest.md)|  | 

### Return type

**Object**

### Authorization

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: text/plain


## forgetpaireddevice

> Object forgetpaireddevice(forgetpaireddeviceRequest)

Forget paired device

*See note for Bluetooth under &#x60;/setup/bluetooth/status&#x60;*  **For both parts**  This is to forget paired devices by mac address. Works for both kinds of devices (Part 1 and Part 2).

### Example

```javascript
import GoogleHome from 'google_home';
let defaultClient = GoogleHome.ApiClient.instance;
// Configure API key authorization: cast-local-authorization-token
let cast-local-authorization-token = defaultClient.authentications['cast-local-authorization-token'];
cast-local-authorization-token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cast-local-authorization-token.apiKeyPrefix = 'Token';

let apiInstance = new GoogleHome.BluetoothApi();
let forgetpaireddeviceRequest = {"bond":false,"mac_address":"xx:xx:xx:xx:xx:xx"}; // ForgetpaireddeviceRequest | 
apiInstance.forgetpaireddevice(forgetpaireddeviceRequest, (error, data, response) => {
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
 **forgetpaireddeviceRequest** | [**ForgetpaireddeviceRequest**](ForgetpaireddeviceRequest.md)|  | 

### Return type

**Object**

### Authorization

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: text/plain


## getPairedDevices

> [Example111] getPairedDevices()

Get Paired Devices

*See note for Bluetooth under &#x60;/setup/bluetooth/status&#x60;*  **For both parts**  This gives a list of all paired or &#39;bonded&#39; devices. The response field names are self-descriptive.

### Example

```javascript
import GoogleHome from 'google_home';
let defaultClient = GoogleHome.ApiClient.instance;
// Configure API key authorization: cast-local-authorization-token
let cast-local-authorization-token = defaultClient.authentications['cast-local-authorization-token'];
cast-local-authorization-token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cast-local-authorization-token.apiKeyPrefix = 'Token';

let apiInstance = new GoogleHome.BluetoothApi();
apiInstance.getPairedDevices((error, data, response) => {
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

[**[Example111]**](Example111.md)

### Authorization

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getScanResults

> [Example112] getScanResults()

Get Scan Results

*See note for Bluetooth under &#x60;/setup/bluetooth/status&#x60;*  **For Part 2 only**  This returns a list of all nearby bluetooth devices. While the Home app only shows speakers, this list contains all devices including TVs, mobiles, etc.  &#x60;rssi&#x60; is signal strength, &#x60;name&#x60; is name, &#x60;mac_address&#x60; is mac address.   &#x60;device_class&#x60; and &#x60;device_type&#x60; are bluetooth codes.    The Home app only lists those devices with &#x60;expected_profiles&#x60; &gt; 0. Basically, the device should function as a speaker.

### Example

```javascript
import GoogleHome from 'google_home';
let defaultClient = GoogleHome.ApiClient.instance;
// Configure API key authorization: cast-local-authorization-token
let cast-local-authorization-token = defaultClient.authentications['cast-local-authorization-token'];
cast-local-authorization-token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cast-local-authorization-token.apiKeyPrefix = 'Token';

let apiInstance = new GoogleHome.BluetoothApi();
apiInstance.getScanResults((error, data, response) => {
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

[**[Example112]**](Example112.md)

### Authorization

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pairwithSpeaker

> Object pairwithSpeaker(pairwithSpeakerRequest)

Pair with Speaker

*See note for Bluetooth under &#x60;/setup/bluetooth/status&#x60;*  **For Part 2 only**  This pairs with other bluetooth speakers by mac address.

### Example

```javascript
import GoogleHome from 'google_home';
let defaultClient = GoogleHome.ApiClient.instance;
// Configure API key authorization: cast-local-authorization-token
let cast-local-authorization-token = defaultClient.authentications['cast-local-authorization-token'];
cast-local-authorization-token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cast-local-authorization-token.apiKeyPrefix = 'Token';

let apiInstance = new GoogleHome.BluetoothApi();
let pairwithSpeakerRequest = {"connect":true,"mac_address":"54:13:79:49:19:22","profile":2}; // PairwithSpeakerRequest | 
apiInstance.pairwithSpeaker(pairwithSpeakerRequest, (error, data, response) => {
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
 **pairwithSpeakerRequest** | [**PairwithSpeakerRequest**](PairwithSpeakerRequest.md)|  | 

### Return type

**Object**

### Authorization

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: text/plain


## scanfordevices

> Object scanfordevices(scanfordevicesRequest)

Scan for devices

*See note for Bluetooth under &#x60;/setup/bluetooth/status&#x60;*  **For Part 2 only**  This initiates scan for other bluetooth speakers/devices. Scan results will be updated continuously for &#x60;timeout&#x60; seconds.   To get the scan results, see /setup/bluetooth/scan_results.

### Example

```javascript
import GoogleHome from 'google_home';
let defaultClient = GoogleHome.ApiClient.instance;
// Configure API key authorization: cast-local-authorization-token
let cast-local-authorization-token = defaultClient.authentications['cast-local-authorization-token'];
cast-local-authorization-token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cast-local-authorization-token.apiKeyPrefix = 'Token';

let apiInstance = new GoogleHome.BluetoothApi();
let scanfordevicesRequest = {"clear_results":true,"enable":true,"timeout":60}; // ScanfordevicesRequest | 
apiInstance.scanfordevices(scanfordevicesRequest, (error, data, response) => {
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
 **scanfordevicesRequest** | [**ScanfordevicesRequest**](ScanfordevicesRequest.md)|  | 

### Return type

**Object**

### Authorization

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: text/plain


## status

> Example110 status()

Status

&gt; **There are 2 parts of Bluetooth.** &gt; &gt; *Part 1*: Devices like phones connect to Home and play audio through Home.   &gt; For this, /setup/bluetooth/discovery is used to make Home discoverable. Then devices can connect to it as if Home is just another bluetooth speaker. &gt; &gt; *Part 2*: Bluetooth speakers connect to Home and Home plays audio through the speakers. &gt; For this, /setup/bluetooth/scan and /setup/bluetooth/scan_results are used to connect to other speakers. &gt; &gt; The other endpoints are common for both parts.   **For both parts**  This gives the status of all bluetooth things. - Not sure what &#x60;audio_mode&#x60; is. - &#x60;discovery_enabled&#x60; states whether Home is discoverable. (**Part 1**) - &#x60;connecting_devices&#x60; is a list of all media sources (like phones) connected to Home. (**Part 1**) - &#x60;scanning_enabled&#x60; states whether Home scanning for other bluetooth speakers/devices. (**Part 2**) - &#x60;connected_devices&#x60; is a list of all speakers connected to Home. (**Part 2**)

### Example

```javascript
import GoogleHome from 'google_home';
let defaultClient = GoogleHome.ApiClient.instance;
// Configure API key authorization: cast-local-authorization-token
let cast-local-authorization-token = defaultClient.authentications['cast-local-authorization-token'];
cast-local-authorization-token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cast-local-authorization-token.apiKeyPrefix = 'Token';

let apiInstance = new GoogleHome.BluetoothApi();
apiInstance.status((error, data, response) => {
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

[**Example110**](Example110.md)

### Authorization

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

