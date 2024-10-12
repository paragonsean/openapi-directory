# MerakiDashboardApi.PrefixesApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createNetworkAppliancePrefixesDelegatedStatic_1**](PrefixesApi.md#createNetworkAppliancePrefixesDelegatedStatic_1) | **POST** /networks/{networkId}/appliance/prefixes/delegated/statics | Add a static delegated prefix from a network
[**deleteNetworkAppliancePrefixesDelegatedStatic_1**](PrefixesApi.md#deleteNetworkAppliancePrefixesDelegatedStatic_1) | **DELETE** /networks/{networkId}/appliance/prefixes/delegated/statics/{staticDelegatedPrefixId} | Delete a static delegated prefix from a network
[**getDeviceAppliancePrefixesDelegatedVlanAssignments_1**](PrefixesApi.md#getDeviceAppliancePrefixesDelegatedVlanAssignments_1) | **GET** /devices/{serial}/appliance/prefixes/delegated/vlanAssignments | Return prefixes assigned to all IPv6 enabled VLANs on an appliance.
[**getDeviceAppliancePrefixesDelegated_1**](PrefixesApi.md#getDeviceAppliancePrefixesDelegated_1) | **GET** /devices/{serial}/appliance/prefixes/delegated | Return current delegated IPv6 prefixes on an appliance.
[**getNetworkAppliancePrefixesDelegatedStatic_1**](PrefixesApi.md#getNetworkAppliancePrefixesDelegatedStatic_1) | **GET** /networks/{networkId}/appliance/prefixes/delegated/statics/{staticDelegatedPrefixId} | Return a static delegated prefix from a network
[**getNetworkAppliancePrefixesDelegatedStatics_1**](PrefixesApi.md#getNetworkAppliancePrefixesDelegatedStatics_1) | **GET** /networks/{networkId}/appliance/prefixes/delegated/statics | List static delegated prefixes for a network
[**updateNetworkAppliancePrefixesDelegatedStatic_1**](PrefixesApi.md#updateNetworkAppliancePrefixesDelegatedStatic_1) | **PUT** /networks/{networkId}/appliance/prefixes/delegated/statics/{staticDelegatedPrefixId} | Update a static delegated prefix from a network



## createNetworkAppliancePrefixesDelegatedStatic_1

> Object createNetworkAppliancePrefixesDelegatedStatic_1(networkId, createNetworkAppliancePrefixesDelegatedStaticRequest)

Add a static delegated prefix from a network

Add a static delegated prefix from a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.PrefixesApi();
let networkId = "networkId_example"; // String | 
let createNetworkAppliancePrefixesDelegatedStaticRequest = new MerakiDashboardApi.CreateNetworkAppliancePrefixesDelegatedStaticRequest(); // CreateNetworkAppliancePrefixesDelegatedStaticRequest | 
apiInstance.createNetworkAppliancePrefixesDelegatedStatic_1(networkId, createNetworkAppliancePrefixesDelegatedStaticRequest, (error, data, response) => {
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
 **networkId** | **String**|  | 
 **createNetworkAppliancePrefixesDelegatedStaticRequest** | [**CreateNetworkAppliancePrefixesDelegatedStaticRequest**](CreateNetworkAppliancePrefixesDelegatedStaticRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteNetworkAppliancePrefixesDelegatedStatic_1

> deleteNetworkAppliancePrefixesDelegatedStatic_1(networkId, staticDelegatedPrefixId)

Delete a static delegated prefix from a network

Delete a static delegated prefix from a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.PrefixesApi();
let networkId = "networkId_example"; // String | 
let staticDelegatedPrefixId = "staticDelegatedPrefixId_example"; // String | 
apiInstance.deleteNetworkAppliancePrefixesDelegatedStatic_1(networkId, staticDelegatedPrefixId, (error, data, response) => {
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
 **networkId** | **String**|  | 
 **staticDelegatedPrefixId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getDeviceAppliancePrefixesDelegatedVlanAssignments_1

> [Object] getDeviceAppliancePrefixesDelegatedVlanAssignments_1(serial)

Return prefixes assigned to all IPv6 enabled VLANs on an appliance.

Return prefixes assigned to all IPv6 enabled VLANs on an appliance.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.PrefixesApi();
let serial = "serial_example"; // String | 
apiInstance.getDeviceAppliancePrefixesDelegatedVlanAssignments_1(serial, (error, data, response) => {
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
 **serial** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeviceAppliancePrefixesDelegated_1

> [Object] getDeviceAppliancePrefixesDelegated_1(serial)

Return current delegated IPv6 prefixes on an appliance.

Return current delegated IPv6 prefixes on an appliance.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.PrefixesApi();
let serial = "serial_example"; // String | 
apiInstance.getDeviceAppliancePrefixesDelegated_1(serial, (error, data, response) => {
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
 **serial** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkAppliancePrefixesDelegatedStatic_1

> GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner getNetworkAppliancePrefixesDelegatedStatic_1(networkId, staticDelegatedPrefixId)

Return a static delegated prefix from a network

Return a static delegated prefix from a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.PrefixesApi();
let networkId = "networkId_example"; // String | 
let staticDelegatedPrefixId = "staticDelegatedPrefixId_example"; // String | 
apiInstance.getNetworkAppliancePrefixesDelegatedStatic_1(networkId, staticDelegatedPrefixId, (error, data, response) => {
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
 **networkId** | **String**|  | 
 **staticDelegatedPrefixId** | **String**|  | 

### Return type

[**GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner**](GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkAppliancePrefixesDelegatedStatics_1

> [GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner] getNetworkAppliancePrefixesDelegatedStatics_1(networkId)

List static delegated prefixes for a network

List static delegated prefixes for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.PrefixesApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkAppliancePrefixesDelegatedStatics_1(networkId, (error, data, response) => {
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
 **networkId** | **String**|  | 

### Return type

[**[GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner]**](GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateNetworkAppliancePrefixesDelegatedStatic_1

> Object updateNetworkAppliancePrefixesDelegatedStatic_1(networkId, staticDelegatedPrefixId, opts)

Update a static delegated prefix from a network

Update a static delegated prefix from a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.PrefixesApi();
let networkId = "networkId_example"; // String | 
let staticDelegatedPrefixId = "staticDelegatedPrefixId_example"; // String | 
let opts = {
  'updateNetworkAppliancePrefixesDelegatedStaticRequest': new MerakiDashboardApi.UpdateNetworkAppliancePrefixesDelegatedStaticRequest() // UpdateNetworkAppliancePrefixesDelegatedStaticRequest | 
};
apiInstance.updateNetworkAppliancePrefixesDelegatedStatic_1(networkId, staticDelegatedPrefixId, opts, (error, data, response) => {
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
 **networkId** | **String**|  | 
 **staticDelegatedPrefixId** | **String**|  | 
 **updateNetworkAppliancePrefixesDelegatedStaticRequest** | [**UpdateNetworkAppliancePrefixesDelegatedStaticRequest**](UpdateNetworkAppliancePrefixesDelegatedStaticRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

