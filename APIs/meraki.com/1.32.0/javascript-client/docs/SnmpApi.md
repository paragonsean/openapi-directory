# MerakiDashboardApi.SnmpApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworkSnmp_1**](SnmpApi.md#getNetworkSnmp_1) | **GET** /networks/{networkId}/snmp | Return the SNMP settings for a network
[**getOrganizationSnmp_1**](SnmpApi.md#getOrganizationSnmp_1) | **GET** /organizations/{organizationId}/snmp | Return the SNMP settings for an organization
[**updateNetworkSnmp_1**](SnmpApi.md#updateNetworkSnmp_1) | **PUT** /networks/{networkId}/snmp | Update the SNMP settings for a network
[**updateOrganizationSnmp_1**](SnmpApi.md#updateOrganizationSnmp_1) | **PUT** /organizations/{organizationId}/snmp | Update the SNMP settings for an organization



## getNetworkSnmp_1

> Object getNetworkSnmp_1(networkId)

Return the SNMP settings for a network

Return the SNMP settings for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SnmpApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSnmp_1(networkId, (error, data, response) => {
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


## getOrganizationSnmp_1

> Object getOrganizationSnmp_1(organizationId)

Return the SNMP settings for an organization

Return the SNMP settings for an organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SnmpApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationSnmp_1(organizationId, (error, data, response) => {
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


## updateNetworkSnmp_1

> Object updateNetworkSnmp_1(networkId, opts)

Update the SNMP settings for a network

Update the SNMP settings for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SnmpApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkSnmpRequest': new MerakiDashboardApi.UpdateNetworkSnmpRequest() // UpdateNetworkSnmpRequest | 
};
apiInstance.updateNetworkSnmp_1(networkId, opts, (error, data, response) => {
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
 **updateNetworkSnmpRequest** | [**UpdateNetworkSnmpRequest**](UpdateNetworkSnmpRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOrganizationSnmp_1

> Object updateOrganizationSnmp_1(organizationId, opts)

Update the SNMP settings for an organization

Update the SNMP settings for an organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SnmpApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'updateOrganizationSnmpRequest': new MerakiDashboardApi.UpdateOrganizationSnmpRequest() // UpdateOrganizationSnmpRequest | 
};
apiInstance.updateOrganizationSnmp_1(organizationId, opts, (error, data, response) => {
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
 **updateOrganizationSnmpRequest** | [**UpdateOrganizationSnmpRequest**](UpdateOrganizationSnmpRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

