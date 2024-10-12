# MerakiDashboardApi.RollbacksApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createNetworkFirmwareUpgradesRollback_2**](RollbacksApi.md#createNetworkFirmwareUpgradesRollback_2) | **POST** /networks/{networkId}/firmwareUpgrades/rollbacks | Rollback a Firmware Upgrade For A Network



## createNetworkFirmwareUpgradesRollback_2

> CreateNetworkFirmwareUpgradesRollback200Response createNetworkFirmwareUpgradesRollback_2(networkId, createNetworkFirmwareUpgradesRollbackRequest)

Rollback a Firmware Upgrade For A Network

Rollback a Firmware Upgrade For A Network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.RollbacksApi();
let networkId = "networkId_example"; // String | 
let createNetworkFirmwareUpgradesRollbackRequest = new MerakiDashboardApi.CreateNetworkFirmwareUpgradesRollbackRequest(); // CreateNetworkFirmwareUpgradesRollbackRequest | 
apiInstance.createNetworkFirmwareUpgradesRollback_2(networkId, createNetworkFirmwareUpgradesRollbackRequest, (error, data, response) => {
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
 **createNetworkFirmwareUpgradesRollbackRequest** | [**CreateNetworkFirmwareUpgradesRollbackRequest**](CreateNetworkFirmwareUpgradesRollbackRequest.md)|  | 

### Return type

[**CreateNetworkFirmwareUpgradesRollback200Response**](CreateNetworkFirmwareUpgradesRollback200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

