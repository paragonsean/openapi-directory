# MerakiDashboardApi.ContentFilteringApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworkApplianceContentFilteringCategories_1**](ContentFilteringApi.md#getNetworkApplianceContentFilteringCategories_1) | **GET** /networks/{networkId}/appliance/contentFiltering/categories | List all available content filtering categories for an MX network
[**getNetworkApplianceContentFiltering_1**](ContentFilteringApi.md#getNetworkApplianceContentFiltering_1) | **GET** /networks/{networkId}/appliance/contentFiltering | Return the content filtering settings for an MX network
[**updateNetworkApplianceContentFiltering_1**](ContentFilteringApi.md#updateNetworkApplianceContentFiltering_1) | **PUT** /networks/{networkId}/appliance/contentFiltering | Update the content filtering settings for an MX network



## getNetworkApplianceContentFilteringCategories_1

> Object getNetworkApplianceContentFilteringCategories_1(networkId)

List all available content filtering categories for an MX network

List all available content filtering categories for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ContentFilteringApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceContentFilteringCategories_1(networkId, (error, data, response) => {
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


## getNetworkApplianceContentFiltering_1

> Object getNetworkApplianceContentFiltering_1(networkId)

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

let apiInstance = new MerakiDashboardApi.ContentFilteringApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceContentFiltering_1(networkId, (error, data, response) => {
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


## updateNetworkApplianceContentFiltering_1

> Object updateNetworkApplianceContentFiltering_1(networkId, opts)

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

let apiInstance = new MerakiDashboardApi.ContentFilteringApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkApplianceContentFilteringRequest': new MerakiDashboardApi.UpdateNetworkApplianceContentFilteringRequest() // UpdateNetworkApplianceContentFilteringRequest | 
};
apiInstance.updateNetworkApplianceContentFiltering_1(networkId, opts, (error, data, response) => {
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
 **updateNetworkApplianceContentFilteringRequest** | [**UpdateNetworkApplianceContentFilteringRequest**](UpdateNetworkApplianceContentFilteringRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

