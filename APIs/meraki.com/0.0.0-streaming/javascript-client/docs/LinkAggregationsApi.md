# MerakiDashboardApi.LinkAggregationsApi

All URIs are relative to *https://api.meraki.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createNetworkSwitchLinkAggregation**](LinkAggregationsApi.md#createNetworkSwitchLinkAggregation) | **POST** /networks/{networkId}/switch/linkAggregations | Create a link aggregation group
[**deleteNetworkSwitchLinkAggregation**](LinkAggregationsApi.md#deleteNetworkSwitchLinkAggregation) | **DELETE** /networks/{networkId}/switch/linkAggregations/{linkAggregationId} | Split a link aggregation group into separate ports
[**getNetworkSwitchLinkAggregations**](LinkAggregationsApi.md#getNetworkSwitchLinkAggregations) | **GET** /networks/{networkId}/switch/linkAggregations | List link aggregation groups
[**updateNetworkSwitchLinkAggregation**](LinkAggregationsApi.md#updateNetworkSwitchLinkAggregation) | **PUT** /networks/{networkId}/switch/linkAggregations/{linkAggregationId} | Update a link aggregation group



## createNetworkSwitchLinkAggregation

> Object createNetworkSwitchLinkAggregation(networkId, opts)

Create a link aggregation group

Create a link aggregation group

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.LinkAggregationsApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'createNetworkSwitchLinkAggregationRequest': new MerakiDashboardApi.CreateNetworkSwitchLinkAggregationRequest() // CreateNetworkSwitchLinkAggregationRequest | 
};
apiInstance.createNetworkSwitchLinkAggregation(networkId, opts, (error, data, response) => {
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
 **createNetworkSwitchLinkAggregationRequest** | [**CreateNetworkSwitchLinkAggregationRequest**](CreateNetworkSwitchLinkAggregationRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteNetworkSwitchLinkAggregation

> deleteNetworkSwitchLinkAggregation(networkId, linkAggregationId)

Split a link aggregation group into separate ports

Split a link aggregation group into separate ports

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.LinkAggregationsApi();
let networkId = "networkId_example"; // String | 
let linkAggregationId = "linkAggregationId_example"; // String | 
apiInstance.deleteNetworkSwitchLinkAggregation(networkId, linkAggregationId, (error, data, response) => {
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
 **linkAggregationId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNetworkSwitchLinkAggregations

> [Object] getNetworkSwitchLinkAggregations(networkId)

List link aggregation groups

List link aggregation groups

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.LinkAggregationsApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSwitchLinkAggregations(networkId, (error, data, response) => {
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


## updateNetworkSwitchLinkAggregation

> Object updateNetworkSwitchLinkAggregation(networkId, linkAggregationId, opts)

Update a link aggregation group

Update a link aggregation group

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.LinkAggregationsApi();
let networkId = "networkId_example"; // String | 
let linkAggregationId = "linkAggregationId_example"; // String | 
let opts = {
  'updateNetworkSwitchLinkAggregationRequest': new MerakiDashboardApi.UpdateNetworkSwitchLinkAggregationRequest() // UpdateNetworkSwitchLinkAggregationRequest | 
};
apiInstance.updateNetworkSwitchLinkAggregation(networkId, linkAggregationId, opts, (error, data, response) => {
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
 **linkAggregationId** | **String**|  | 
 **updateNetworkSwitchLinkAggregationRequest** | [**UpdateNetworkSwitchLinkAggregationRequest**](UpdateNetworkSwitchLinkAggregationRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

