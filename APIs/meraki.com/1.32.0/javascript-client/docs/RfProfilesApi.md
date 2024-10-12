# MerakiDashboardApi.RfProfilesApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createNetworkWirelessRfProfile_1**](RfProfilesApi.md#createNetworkWirelessRfProfile_1) | **POST** /networks/{networkId}/wireless/rfProfiles | Creates new RF profile for this network
[**deleteNetworkWirelessRfProfile_1**](RfProfilesApi.md#deleteNetworkWirelessRfProfile_1) | **DELETE** /networks/{networkId}/wireless/rfProfiles/{rfProfileId} | Delete a RF Profile
[**getNetworkWirelessRfProfile_1**](RfProfilesApi.md#getNetworkWirelessRfProfile_1) | **GET** /networks/{networkId}/wireless/rfProfiles/{rfProfileId} | Return a RF profile
[**getNetworkWirelessRfProfiles_1**](RfProfilesApi.md#getNetworkWirelessRfProfiles_1) | **GET** /networks/{networkId}/wireless/rfProfiles | List the non-basic RF profiles for this network
[**updateNetworkWirelessRfProfile_1**](RfProfilesApi.md#updateNetworkWirelessRfProfile_1) | **PUT** /networks/{networkId}/wireless/rfProfiles/{rfProfileId} | Updates specified RF profile for this network



## createNetworkWirelessRfProfile_1

> CreateNetworkWirelessRfProfile201Response createNetworkWirelessRfProfile_1(networkId, createNetworkWirelessRfProfileRequest)

Creates new RF profile for this network

Creates new RF profile for this network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.RfProfilesApi();
let networkId = "networkId_example"; // String | 
let createNetworkWirelessRfProfileRequest = new MerakiDashboardApi.CreateNetworkWirelessRfProfileRequest(); // CreateNetworkWirelessRfProfileRequest | 
apiInstance.createNetworkWirelessRfProfile_1(networkId, createNetworkWirelessRfProfileRequest, (error, data, response) => {
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
 **createNetworkWirelessRfProfileRequest** | [**CreateNetworkWirelessRfProfileRequest**](CreateNetworkWirelessRfProfileRequest.md)|  | 

### Return type

[**CreateNetworkWirelessRfProfile201Response**](CreateNetworkWirelessRfProfile201Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteNetworkWirelessRfProfile_1

> deleteNetworkWirelessRfProfile_1(networkId, rfProfileId)

Delete a RF Profile

Delete a RF Profile

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.RfProfilesApi();
let networkId = "networkId_example"; // String | 
let rfProfileId = "rfProfileId_example"; // String | 
apiInstance.deleteNetworkWirelessRfProfile_1(networkId, rfProfileId, (error, data, response) => {
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
 **rfProfileId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNetworkWirelessRfProfile_1

> Object getNetworkWirelessRfProfile_1(networkId, rfProfileId)

Return a RF profile

Return a RF profile

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.RfProfilesApi();
let networkId = "networkId_example"; // String | 
let rfProfileId = "rfProfileId_example"; // String | 
apiInstance.getNetworkWirelessRfProfile_1(networkId, rfProfileId, (error, data, response) => {
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
 **rfProfileId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWirelessRfProfiles_1

> [Object] getNetworkWirelessRfProfiles_1(networkId, opts)

List the non-basic RF profiles for this network

List the non-basic RF profiles for this network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.RfProfilesApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'includeTemplateProfiles': true // Boolean | If the network is bound to a template, this parameter controls whether or not the non-basic RF profiles defined on the template should be included in the response alongside the non-basic profiles defined on the bound network. Defaults to false.
};
apiInstance.getNetworkWirelessRfProfiles_1(networkId, opts, (error, data, response) => {
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
 **includeTemplateProfiles** | **Boolean**| If the network is bound to a template, this parameter controls whether or not the non-basic RF profiles defined on the template should be included in the response alongside the non-basic profiles defined on the bound network. Defaults to false. | [optional] 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateNetworkWirelessRfProfile_1

> CreateNetworkWirelessRfProfile201Response updateNetworkWirelessRfProfile_1(networkId, rfProfileId, opts)

Updates specified RF profile for this network

Updates specified RF profile for this network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.RfProfilesApi();
let networkId = "networkId_example"; // String | 
let rfProfileId = "rfProfileId_example"; // String | 
let opts = {
  'updateNetworkWirelessRfProfileRequest': new MerakiDashboardApi.UpdateNetworkWirelessRfProfileRequest() // UpdateNetworkWirelessRfProfileRequest | 
};
apiInstance.updateNetworkWirelessRfProfile_1(networkId, rfProfileId, opts, (error, data, response) => {
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
 **rfProfileId** | **String**|  | 
 **updateNetworkWirelessRfProfileRequest** | [**UpdateNetworkWirelessRfProfileRequest**](UpdateNetworkWirelessRfProfileRequest.md)|  | [optional] 

### Return type

[**CreateNetworkWirelessRfProfile201Response**](CreateNetworkWirelessRfProfile201Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

