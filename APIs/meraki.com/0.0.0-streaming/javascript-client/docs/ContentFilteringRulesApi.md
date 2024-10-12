# MerakiDashboardApi.ContentFilteringRulesApi

All URIs are relative to *https://api.meraki.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworkContentFiltering**](ContentFilteringRulesApi.md#getNetworkContentFiltering) | **GET** /networks/{networkId}/contentFiltering | Return the content filtering settings for an MX network
[**updateNetworkContentFiltering**](ContentFilteringRulesApi.md#updateNetworkContentFiltering) | **PUT** /networks/{networkId}/contentFiltering | Update the content filtering settings for an MX network



## getNetworkContentFiltering

> Object getNetworkContentFiltering(networkId)

Return the content filtering settings for an MX network

Return the content filtering settings for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ContentFilteringRulesApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkContentFiltering(networkId, (error, data, response) => {
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


## updateNetworkContentFiltering

> Object updateNetworkContentFiltering(networkId, opts)

Update the content filtering settings for an MX network

Update the content filtering settings for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ContentFilteringRulesApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkContentFilteringRequest': new MerakiDashboardApi.UpdateNetworkContentFilteringRequest() // UpdateNetworkContentFilteringRequest | 
};
apiInstance.updateNetworkContentFiltering(networkId, opts, (error, data, response) => {
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
 **updateNetworkContentFilteringRequest** | [**UpdateNetworkContentFilteringRequest**](UpdateNetworkContentFilteringRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

