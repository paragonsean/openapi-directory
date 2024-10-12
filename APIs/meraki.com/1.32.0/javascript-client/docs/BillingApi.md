# MerakiDashboardApi.BillingApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworkWirelessBilling_1**](BillingApi.md#getNetworkWirelessBilling_1) | **GET** /networks/{networkId}/wireless/billing | Return the billing settings of this network
[**updateNetworkWirelessBilling_1**](BillingApi.md#updateNetworkWirelessBilling_1) | **PUT** /networks/{networkId}/wireless/billing | Update the billing settings



## getNetworkWirelessBilling_1

> Object getNetworkWirelessBilling_1(networkId)

Return the billing settings of this network

Return the billing settings of this network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.BillingApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkWirelessBilling_1(networkId, (error, data, response) => {
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


## updateNetworkWirelessBilling_1

> Object updateNetworkWirelessBilling_1(networkId, opts)

Update the billing settings

Update the billing settings

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.BillingApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkWirelessBillingRequest': new MerakiDashboardApi.UpdateNetworkWirelessBillingRequest() // UpdateNetworkWirelessBillingRequest | 
};
apiInstance.updateNetworkWirelessBilling_1(networkId, opts, (error, data, response) => {
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
 **updateNetworkWirelessBillingRequest** | [**UpdateNetworkWirelessBillingRequest**](UpdateNetworkWirelessBillingRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

