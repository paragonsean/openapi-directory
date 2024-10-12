# MerakiDashboardApi.DscpToCosMappingsApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworkSwitchDscpToCosMappings_1**](DscpToCosMappingsApi.md#getNetworkSwitchDscpToCosMappings_1) | **GET** /networks/{networkId}/switch/dscpToCosMappings | Return the DSCP to CoS mappings
[**updateNetworkSwitchDscpToCosMappings_1**](DscpToCosMappingsApi.md#updateNetworkSwitchDscpToCosMappings_1) | **PUT** /networks/{networkId}/switch/dscpToCosMappings | Update the DSCP to CoS mappings



## getNetworkSwitchDscpToCosMappings_1

> Object getNetworkSwitchDscpToCosMappings_1(networkId)

Return the DSCP to CoS mappings

Return the DSCP to CoS mappings

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.DscpToCosMappingsApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSwitchDscpToCosMappings_1(networkId, (error, data, response) => {
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


## updateNetworkSwitchDscpToCosMappings_1

> Object updateNetworkSwitchDscpToCosMappings_1(networkId, updateNetworkSwitchDscpToCosMappingsRequest)

Update the DSCP to CoS mappings

Update the DSCP to CoS mappings

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.DscpToCosMappingsApi();
let networkId = "networkId_example"; // String | 
let updateNetworkSwitchDscpToCosMappingsRequest = new MerakiDashboardApi.UpdateNetworkSwitchDscpToCosMappingsRequest(); // UpdateNetworkSwitchDscpToCosMappingsRequest | 
apiInstance.updateNetworkSwitchDscpToCosMappings_1(networkId, updateNetworkSwitchDscpToCosMappingsRequest, (error, data, response) => {
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
 **updateNetworkSwitchDscpToCosMappingsRequest** | [**UpdateNetworkSwitchDscpToCosMappingsRequest**](UpdateNetworkSwitchDscpToCosMappingsRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

