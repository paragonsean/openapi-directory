# MerakiDashboardApi.ConnectivityMonitoringDestinationsApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworkApplianceConnectivityMonitoringDestinations_1**](ConnectivityMonitoringDestinationsApi.md#getNetworkApplianceConnectivityMonitoringDestinations_1) | **GET** /networks/{networkId}/appliance/connectivityMonitoringDestinations | Return the connectivity testing destinations for an MX network
[**getNetworkCellularGatewayConnectivityMonitoringDestinations_1**](ConnectivityMonitoringDestinationsApi.md#getNetworkCellularGatewayConnectivityMonitoringDestinations_1) | **GET** /networks/{networkId}/cellularGateway/connectivityMonitoringDestinations | Return the connectivity testing destinations for an MG network
[**updateNetworkApplianceConnectivityMonitoringDestinations_1**](ConnectivityMonitoringDestinationsApi.md#updateNetworkApplianceConnectivityMonitoringDestinations_1) | **PUT** /networks/{networkId}/appliance/connectivityMonitoringDestinations | Update the connectivity testing destinations for an MX network
[**updateNetworkCellularGatewayConnectivityMonitoringDestinations_1**](ConnectivityMonitoringDestinationsApi.md#updateNetworkCellularGatewayConnectivityMonitoringDestinations_1) | **PUT** /networks/{networkId}/cellularGateway/connectivityMonitoringDestinations | Update the connectivity testing destinations for an MG network



## getNetworkApplianceConnectivityMonitoringDestinations_1

> Object getNetworkApplianceConnectivityMonitoringDestinations_1(networkId)

Return the connectivity testing destinations for an MX network

Return the connectivity testing destinations for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConnectivityMonitoringDestinationsApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkApplianceConnectivityMonitoringDestinations_1(networkId, (error, data, response) => {
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


## getNetworkCellularGatewayConnectivityMonitoringDestinations_1

> Object getNetworkCellularGatewayConnectivityMonitoringDestinations_1(networkId)

Return the connectivity testing destinations for an MG network

Return the connectivity testing destinations for an MG network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConnectivityMonitoringDestinationsApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkCellularGatewayConnectivityMonitoringDestinations_1(networkId, (error, data, response) => {
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


## updateNetworkApplianceConnectivityMonitoringDestinations_1

> Object updateNetworkApplianceConnectivityMonitoringDestinations_1(networkId, opts)

Update the connectivity testing destinations for an MX network

Update the connectivity testing destinations for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConnectivityMonitoringDestinationsApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkApplianceConnectivityMonitoringDestinationsRequest': new MerakiDashboardApi.UpdateNetworkApplianceConnectivityMonitoringDestinationsRequest() // UpdateNetworkApplianceConnectivityMonitoringDestinationsRequest | 
};
apiInstance.updateNetworkApplianceConnectivityMonitoringDestinations_1(networkId, opts, (error, data, response) => {
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
 **updateNetworkApplianceConnectivityMonitoringDestinationsRequest** | [**UpdateNetworkApplianceConnectivityMonitoringDestinationsRequest**](UpdateNetworkApplianceConnectivityMonitoringDestinationsRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkCellularGatewayConnectivityMonitoringDestinations_1

> Object updateNetworkCellularGatewayConnectivityMonitoringDestinations_1(networkId, opts)

Update the connectivity testing destinations for an MG network

Update the connectivity testing destinations for an MG network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConnectivityMonitoringDestinationsApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest': new MerakiDashboardApi.UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest() // UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest | 
};
apiInstance.updateNetworkCellularGatewayConnectivityMonitoringDestinations_1(networkId, opts, (error, data, response) => {
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
 **updateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest** | [**UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest**](UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

