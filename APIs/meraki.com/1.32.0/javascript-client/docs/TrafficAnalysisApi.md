# MerakiDashboardApi.TrafficAnalysisApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworkTrafficAnalysis_1**](TrafficAnalysisApi.md#getNetworkTrafficAnalysis_1) | **GET** /networks/{networkId}/trafficAnalysis | Return the traffic analysis settings for a network
[**updateNetworkTrafficAnalysis_1**](TrafficAnalysisApi.md#updateNetworkTrafficAnalysis_1) | **PUT** /networks/{networkId}/trafficAnalysis | Update the traffic analysis settings for a network



## getNetworkTrafficAnalysis_1

> Object getNetworkTrafficAnalysis_1(networkId)

Return the traffic analysis settings for a network

Return the traffic analysis settings for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.TrafficAnalysisApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkTrafficAnalysis_1(networkId, (error, data, response) => {
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


## updateNetworkTrafficAnalysis_1

> Object updateNetworkTrafficAnalysis_1(networkId, opts)

Update the traffic analysis settings for a network

Update the traffic analysis settings for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.TrafficAnalysisApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkTrafficAnalysisRequest': new MerakiDashboardApi.UpdateNetworkTrafficAnalysisRequest() // UpdateNetworkTrafficAnalysisRequest | 
};
apiInstance.updateNetworkTrafficAnalysis_1(networkId, opts, (error, data, response) => {
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
 **updateNetworkTrafficAnalysisRequest** | [**UpdateNetworkTrafficAnalysisRequest**](UpdateNetworkTrafficAnalysisRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

