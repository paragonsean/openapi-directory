# MerakiDashboardApi.SwitchSettingsApi

All URIs are relative to *https://api.meraki.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createNetworkSwitchSettingsQosRule**](SwitchSettingsApi.md#createNetworkSwitchSettingsQosRule) | **POST** /networks/{networkId}/switch/settings/qosRules | Add a quality of service rule
[**deleteNetworkSwitchSettingsQosRule**](SwitchSettingsApi.md#deleteNetworkSwitchSettingsQosRule) | **DELETE** /networks/{networkId}/switch/settings/qosRules/{qosRuleId} | Delete a quality of service rule
[**getNetworkSwitchSettings**](SwitchSettingsApi.md#getNetworkSwitchSettings) | **GET** /networks/{networkId}/switch/settings | Returns the switch network settings
[**getNetworkSwitchSettingsMtu**](SwitchSettingsApi.md#getNetworkSwitchSettingsMtu) | **GET** /networks/{networkId}/switch/settings/mtu | Return the MTU configuration
[**getNetworkSwitchSettingsMulticast**](SwitchSettingsApi.md#getNetworkSwitchSettingsMulticast) | **GET** /networks/{networkId}/switch/settings/multicast | Return multicast settings for a network
[**getNetworkSwitchSettingsQosRule**](SwitchSettingsApi.md#getNetworkSwitchSettingsQosRule) | **GET** /networks/{networkId}/switch/settings/qosRules/{qosRuleId} | Return a quality of service rule
[**getNetworkSwitchSettingsQosRules**](SwitchSettingsApi.md#getNetworkSwitchSettingsQosRules) | **GET** /networks/{networkId}/switch/settings/qosRules | List quality of service rules
[**getNetworkSwitchSettingsQosRulesOrder**](SwitchSettingsApi.md#getNetworkSwitchSettingsQosRulesOrder) | **GET** /networks/{networkId}/switch/settings/qosRules/order | Return the quality of service rule IDs by order in which they will be processed by the switch
[**getNetworkSwitchSettingsStormControl**](SwitchSettingsApi.md#getNetworkSwitchSettingsStormControl) | **GET** /networks/{networkId}/switch/settings/stormControl | Return the storm control configuration for a switch network
[**updateNetworkSwitchSettings**](SwitchSettingsApi.md#updateNetworkSwitchSettings) | **PUT** /networks/{networkId}/switch/settings | Update switch network settings
[**updateNetworkSwitchSettingsMulticast**](SwitchSettingsApi.md#updateNetworkSwitchSettingsMulticast) | **PUT** /networks/{networkId}/switch/settings/multicast | Update multicast settings for a network
[**updateNetworkSwitchSettingsQosRule**](SwitchSettingsApi.md#updateNetworkSwitchSettingsQosRule) | **PUT** /networks/{networkId}/switch/settings/qosRules/{qosRuleId} | Update a quality of service rule
[**updateNetworkSwitchSettingsQosRulesOrder**](SwitchSettingsApi.md#updateNetworkSwitchSettingsQosRulesOrder) | **PUT** /networks/{networkId}/switch/settings/qosRules/order | Update the order in which the rules should be processed by the switch
[**updateNetworkSwitchSettingsStormControl**](SwitchSettingsApi.md#updateNetworkSwitchSettingsStormControl) | **PUT** /networks/{networkId}/switch/settings/stormControl | Update the storm control configuration for a switch network



## createNetworkSwitchSettingsQosRule

> Object createNetworkSwitchSettingsQosRule(networkId, createNetworkSwitchSettingsQosRuleRequest)

Add a quality of service rule

Add a quality of service rule

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SwitchSettingsApi();
let networkId = "networkId_example"; // String | 
let createNetworkSwitchSettingsQosRuleRequest = new MerakiDashboardApi.CreateNetworkSwitchSettingsQosRuleRequest(); // CreateNetworkSwitchSettingsQosRuleRequest | 
apiInstance.createNetworkSwitchSettingsQosRule(networkId, createNetworkSwitchSettingsQosRuleRequest, (error, data, response) => {
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
 **createNetworkSwitchSettingsQosRuleRequest** | [**CreateNetworkSwitchSettingsQosRuleRequest**](CreateNetworkSwitchSettingsQosRuleRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteNetworkSwitchSettingsQosRule

> deleteNetworkSwitchSettingsQosRule(networkId, qosRuleId)

Delete a quality of service rule

Delete a quality of service rule

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SwitchSettingsApi();
let networkId = "networkId_example"; // String | 
let qosRuleId = "qosRuleId_example"; // String | 
apiInstance.deleteNetworkSwitchSettingsQosRule(networkId, qosRuleId, (error, data, response) => {
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
 **qosRuleId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNetworkSwitchSettings

> Object getNetworkSwitchSettings(networkId)

Returns the switch network settings

Returns the switch network settings

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SwitchSettingsApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSwitchSettings(networkId, (error, data, response) => {
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


## getNetworkSwitchSettingsMtu

> Object getNetworkSwitchSettingsMtu(networkId)

Return the MTU configuration

Return the MTU configuration

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SwitchSettingsApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSwitchSettingsMtu(networkId, (error, data, response) => {
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


## getNetworkSwitchSettingsMulticast

> Object getNetworkSwitchSettingsMulticast(networkId)

Return multicast settings for a network

Return multicast settings for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SwitchSettingsApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSwitchSettingsMulticast(networkId, (error, data, response) => {
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


## getNetworkSwitchSettingsQosRule

> Object getNetworkSwitchSettingsQosRule(networkId, qosRuleId)

Return a quality of service rule

Return a quality of service rule

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SwitchSettingsApi();
let networkId = "networkId_example"; // String | 
let qosRuleId = "qosRuleId_example"; // String | 
apiInstance.getNetworkSwitchSettingsQosRule(networkId, qosRuleId, (error, data, response) => {
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
 **qosRuleId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSwitchSettingsQosRules

> [Object] getNetworkSwitchSettingsQosRules(networkId)

List quality of service rules

List quality of service rules

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SwitchSettingsApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSwitchSettingsQosRules(networkId, (error, data, response) => {
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

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSwitchSettingsQosRulesOrder

> Object getNetworkSwitchSettingsQosRulesOrder(networkId)

Return the quality of service rule IDs by order in which they will be processed by the switch

Return the quality of service rule IDs by order in which they will be processed by the switch

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SwitchSettingsApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSwitchSettingsQosRulesOrder(networkId, (error, data, response) => {
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


## getNetworkSwitchSettingsStormControl

> Object getNetworkSwitchSettingsStormControl(networkId)

Return the storm control configuration for a switch network

Return the storm control configuration for a switch network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SwitchSettingsApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSwitchSettingsStormControl(networkId, (error, data, response) => {
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


## updateNetworkSwitchSettings

> Object updateNetworkSwitchSettings(networkId, opts)

Update switch network settings

Update switch network settings

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SwitchSettingsApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkSwitchSettingsRequest': new MerakiDashboardApi.UpdateNetworkSwitchSettingsRequest() // UpdateNetworkSwitchSettingsRequest | 
};
apiInstance.updateNetworkSwitchSettings(networkId, opts, (error, data, response) => {
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
 **updateNetworkSwitchSettingsRequest** | [**UpdateNetworkSwitchSettingsRequest**](UpdateNetworkSwitchSettingsRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkSwitchSettingsMulticast

> Object updateNetworkSwitchSettingsMulticast(networkId, opts)

Update multicast settings for a network

Update multicast settings for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SwitchSettingsApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkSwitchSettingsMulticastRequest': new MerakiDashboardApi.UpdateNetworkSwitchSettingsMulticastRequest() // UpdateNetworkSwitchSettingsMulticastRequest | 
};
apiInstance.updateNetworkSwitchSettingsMulticast(networkId, opts, (error, data, response) => {
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
 **updateNetworkSwitchSettingsMulticastRequest** | [**UpdateNetworkSwitchSettingsMulticastRequest**](UpdateNetworkSwitchSettingsMulticastRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkSwitchSettingsQosRule

> Object updateNetworkSwitchSettingsQosRule(networkId, qosRuleId, opts)

Update a quality of service rule

Update a quality of service rule

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SwitchSettingsApi();
let networkId = "networkId_example"; // String | 
let qosRuleId = "qosRuleId_example"; // String | 
let opts = {
  'updateNetworkSwitchSettingsQosRuleRequest': new MerakiDashboardApi.UpdateNetworkSwitchSettingsQosRuleRequest() // UpdateNetworkSwitchSettingsQosRuleRequest | 
};
apiInstance.updateNetworkSwitchSettingsQosRule(networkId, qosRuleId, opts, (error, data, response) => {
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
 **qosRuleId** | **String**|  | 
 **updateNetworkSwitchSettingsQosRuleRequest** | [**UpdateNetworkSwitchSettingsQosRuleRequest**](UpdateNetworkSwitchSettingsQosRuleRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkSwitchSettingsQosRulesOrder

> Object updateNetworkSwitchSettingsQosRulesOrder(networkId, updateNetworkSwitchSettingsQosRulesOrderRequest)

Update the order in which the rules should be processed by the switch

Update the order in which the rules should be processed by the switch

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SwitchSettingsApi();
let networkId = "networkId_example"; // String | 
let updateNetworkSwitchSettingsQosRulesOrderRequest = new MerakiDashboardApi.UpdateNetworkSwitchSettingsQosRulesOrderRequest(); // UpdateNetworkSwitchSettingsQosRulesOrderRequest | 
apiInstance.updateNetworkSwitchSettingsQosRulesOrder(networkId, updateNetworkSwitchSettingsQosRulesOrderRequest, (error, data, response) => {
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
 **updateNetworkSwitchSettingsQosRulesOrderRequest** | [**UpdateNetworkSwitchSettingsQosRulesOrderRequest**](UpdateNetworkSwitchSettingsQosRulesOrderRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkSwitchSettingsStormControl

> Object updateNetworkSwitchSettingsStormControl(networkId, opts)

Update the storm control configuration for a switch network

Update the storm control configuration for a switch network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SwitchSettingsApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkSwitchSettingsStormControlRequest': new MerakiDashboardApi.UpdateNetworkSwitchSettingsStormControlRequest() // UpdateNetworkSwitchSettingsStormControlRequest | 
};
apiInstance.updateNetworkSwitchSettingsStormControl(networkId, opts, (error, data, response) => {
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
 **updateNetworkSwitchSettingsStormControlRequest** | [**UpdateNetworkSwitchSettingsStormControlRequest**](UpdateNetworkSwitchSettingsStormControlRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

