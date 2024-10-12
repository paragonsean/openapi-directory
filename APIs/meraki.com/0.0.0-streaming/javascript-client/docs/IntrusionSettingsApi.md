# MerakiDashboardApi.IntrusionSettingsApi

All URIs are relative to *https://api.meraki.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworkSecurityIntrusionSettings**](IntrusionSettingsApi.md#getNetworkSecurityIntrusionSettings) | **GET** /networks/{networkId}/security/intrusionSettings | Returns all supported intrusion settings for an MX network
[**getOrganizationSecurityIntrusionSettings**](IntrusionSettingsApi.md#getOrganizationSecurityIntrusionSettings) | **GET** /organizations/{organizationId}/security/intrusionSettings | Returns all supported intrusion settings for an organization
[**updateNetworkSecurityIntrusionSettings**](IntrusionSettingsApi.md#updateNetworkSecurityIntrusionSettings) | **PUT** /networks/{networkId}/security/intrusionSettings | Set the supported intrusion settings for an MX network
[**updateOrganizationSecurityIntrusionSettings**](IntrusionSettingsApi.md#updateOrganizationSecurityIntrusionSettings) | **PUT** /organizations/{organizationId}/security/intrusionSettings | Sets supported intrusion settings for an organization



## getNetworkSecurityIntrusionSettings

> Object getNetworkSecurityIntrusionSettings(networkId)

Returns all supported intrusion settings for an MX network

Returns all supported intrusion settings for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.IntrusionSettingsApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSecurityIntrusionSettings(networkId, (error, data, response) => {
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

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationSecurityIntrusionSettings

> Object getOrganizationSecurityIntrusionSettings(organizationId)

Returns all supported intrusion settings for an organization

Returns all supported intrusion settings for an organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.IntrusionSettingsApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationSecurityIntrusionSettings(organizationId, (error, data, response) => {
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
 **organizationId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateNetworkSecurityIntrusionSettings

> Object updateNetworkSecurityIntrusionSettings(networkId, opts)

Set the supported intrusion settings for an MX network

Set the supported intrusion settings for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.IntrusionSettingsApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkSecurityIntrusionSettingsRequest': new MerakiDashboardApi.UpdateNetworkSecurityIntrusionSettingsRequest() // UpdateNetworkSecurityIntrusionSettingsRequest | 
};
apiInstance.updateNetworkSecurityIntrusionSettings(networkId, opts, (error, data, response) => {
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
 **updateNetworkSecurityIntrusionSettingsRequest** | [**UpdateNetworkSecurityIntrusionSettingsRequest**](UpdateNetworkSecurityIntrusionSettingsRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOrganizationSecurityIntrusionSettings

> Object updateOrganizationSecurityIntrusionSettings(organizationId, updateOrganizationSecurityIntrusionSettingsRequest)

Sets supported intrusion settings for an organization

Sets supported intrusion settings for an organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.IntrusionSettingsApi();
let organizationId = "organizationId_example"; // String | 
let updateOrganizationSecurityIntrusionSettingsRequest = new MerakiDashboardApi.UpdateOrganizationSecurityIntrusionSettingsRequest(); // UpdateOrganizationSecurityIntrusionSettingsRequest | 
apiInstance.updateOrganizationSecurityIntrusionSettings(organizationId, updateOrganizationSecurityIntrusionSettingsRequest, (error, data, response) => {
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
 **organizationId** | **String**|  | 
 **updateOrganizationSecurityIntrusionSettingsRequest** | [**UpdateOrganizationSecurityIntrusionSettingsRequest**](UpdateOrganizationSecurityIntrusionSettingsRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

