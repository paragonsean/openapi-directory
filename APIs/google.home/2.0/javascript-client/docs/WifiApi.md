# GoogleHome.WifiApi

All URIs are relative to *http://example.com/setup*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connecttoWiFiNetwork**](WifiApi.md#connecttoWiFiNetwork) | **POST** /connect_wifi | Connect to Wi-Fi Network
[**forgetWiFiNetwork**](WifiApi.md#forgetWiFiNetwork) | **POST** /forget_wifi | Forget Wi-Fi Network
[**getSavedNetworks**](WifiApi.md#getSavedNetworks) | **GET** /configured_networks | Get Saved Networks
[**getWiFiScanResults**](WifiApi.md#getWiFiScanResults) | **GET** /scan_results | Get Wi-Fi Scan Results
[**scanforNetworks**](WifiApi.md#scanforNetworks) | **POST** /scan_wifi | Scan for Networks



## connecttoWiFiNetwork

> connecttoWiFiNetwork(connecttoWiFiNetworkRequest)

Connect to Wi-Fi Network

**Note:** Not sure how the password is encrypted. Might be using the public certificate from /setup/eureka_info. So this cannot be used as of now. If someone figures it out, please [create a new issue here](https://github.com/rithvikvibhu/GHLocalApi/issues/new).

### Example

```javascript
import GoogleHome from 'google_home';
let defaultClient = GoogleHome.ApiClient.instance;
// Configure API key authorization: cast-local-authorization-token
let cast-local-authorization-token = defaultClient.authentications['cast-local-authorization-token'];
cast-local-authorization-token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cast-local-authorization-token.apiKeyPrefix = 'Token';

let apiInstance = new GoogleHome.WifiApi();
let connecttoWiFiNetworkRequest = {"bssid":"5c:0a:xx:xx:xx:xx","enc_passwd":"xxxxxfPY=","signal_level":-42,"ssid":"myotherssid","wpa_auth":7,"wpa_cipher":4}; // ConnecttoWiFiNetworkRequest | 
apiInstance.connecttoWiFiNetwork(connecttoWiFiNetworkRequest, (error, data, response) => {
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
 **connecttoWiFiNetworkRequest** | [**ConnecttoWiFiNetworkRequest**](ConnecttoWiFiNetworkRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## forgetWiFiNetwork

> Object forgetWiFiNetwork(forgetWiFiNetworkRequest)

Forget Wi-Fi Network

This is to forget a saved network by &#x60;wpa_id&#x60;. Get the &#x60;wpa_id&#x60; from /setup/configured_networks

### Example

```javascript
import GoogleHome from 'google_home';
let defaultClient = GoogleHome.ApiClient.instance;
// Configure API key authorization: cast-local-authorization-token
let cast-local-authorization-token = defaultClient.authentications['cast-local-authorization-token'];
cast-local-authorization-token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cast-local-authorization-token.apiKeyPrefix = 'Token';

let apiInstance = new GoogleHome.WifiApi();
let forgetWiFiNetworkRequest = {"wpa_id":0}; // ForgetWiFiNetworkRequest | 
apiInstance.forgetWiFiNetwork(forgetWiFiNetworkRequest, (error, data, response) => {
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
 **forgetWiFiNetworkRequest** | [**ForgetWiFiNetworkRequest**](ForgetWiFiNetworkRequest.md)|  | 

### Return type

**Object**

### Authorization

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: text/plain


## getSavedNetworks

> [Example113] getSavedNetworks()

Get Saved Networks

This gets a list of all saved Wi-Fi networks.  Each network has &#x60;ssid&#x60;, &#x60;wpa_auth&#x60;, &#x60;wpa_cipher&#x60; and &#x60;wpa_id&#x60;.   &#x60;wpa_id&#x60; is an incrementing number used to identify a saved network.   #TODO: Add values for &#x60;wpa_auth&#x60; and &#x60;wpa_cipher&#x60;.

### Example

```javascript
import GoogleHome from 'google_home';
let defaultClient = GoogleHome.ApiClient.instance;
// Configure API key authorization: cast-local-authorization-token
let cast-local-authorization-token = defaultClient.authentications['cast-local-authorization-token'];
cast-local-authorization-token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cast-local-authorization-token.apiKeyPrefix = 'Token';

let apiInstance = new GoogleHome.WifiApi();
apiInstance.getSavedNetworks((error, data, response) => {
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

[**[Example113]**](Example113.md)

### Authorization

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getWiFiScanResults

> [Example114] getWiFiScanResults()

Get Wi-Fi Scan Results

This gets a list of all nearby Wi-Fi access points.  The list only has the connected AP by default. Once a scan is triggered by &#x60;/setup/scan_wifi&#x60;, the whole list is cached for ~3 minutes. Then it will revert to returning only the connected AP again.

### Example

```javascript
import GoogleHome from 'google_home';
let defaultClient = GoogleHome.ApiClient.instance;
// Configure API key authorization: cast-local-authorization-token
let cast-local-authorization-token = defaultClient.authentications['cast-local-authorization-token'];
cast-local-authorization-token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cast-local-authorization-token.apiKeyPrefix = 'Token';

let apiInstance = new GoogleHome.WifiApi();
apiInstance.getWiFiScanResults((error, data, response) => {
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

[**[Example114]**](Example114.md)

### Authorization

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## scanforNetworks

> Object scanforNetworks()

Scan for Networks

This initiates scanning for Wi-Fi networks.  The results can be obtained with &#x60;/setup/scan_results&#x60; after triggering the scan with this request.

### Example

```javascript
import GoogleHome from 'google_home';
let defaultClient = GoogleHome.ApiClient.instance;
// Configure API key authorization: cast-local-authorization-token
let cast-local-authorization-token = defaultClient.authentications['cast-local-authorization-token'];
cast-local-authorization-token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cast-local-authorization-token.apiKeyPrefix = 'Token';

let apiInstance = new GoogleHome.WifiApi();
apiInstance.scanforNetworks((error, data, response) => {
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

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain

