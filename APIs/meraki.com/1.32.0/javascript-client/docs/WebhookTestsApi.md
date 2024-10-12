# MerakiDashboardApi.WebhookTestsApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createNetworkWebhooksWebhookTest_2**](WebhookTestsApi.md#createNetworkWebhooksWebhookTest_2) | **POST** /networks/{networkId}/webhooks/webhookTests | Send a test webhook for a network
[**getNetworkWebhooksWebhookTest_2**](WebhookTestsApi.md#getNetworkWebhooksWebhookTest_2) | **GET** /networks/{networkId}/webhooks/webhookTests/{webhookTestId} | Return the status of a webhook test for a network



## createNetworkWebhooksWebhookTest_2

> CreateNetworkWebhooksWebhookTest201Response createNetworkWebhooksWebhookTest_2(networkId, createNetworkWebhooksWebhookTestRequest)

Send a test webhook for a network

Send a test webhook for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WebhookTestsApi();
let networkId = "networkId_example"; // String | 
let createNetworkWebhooksWebhookTestRequest = new MerakiDashboardApi.CreateNetworkWebhooksWebhookTestRequest(); // CreateNetworkWebhooksWebhookTestRequest | 
apiInstance.createNetworkWebhooksWebhookTest_2(networkId, createNetworkWebhooksWebhookTestRequest, (error, data, response) => {
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
 **createNetworkWebhooksWebhookTestRequest** | [**CreateNetworkWebhooksWebhookTestRequest**](CreateNetworkWebhooksWebhookTestRequest.md)|  | 

### Return type

[**CreateNetworkWebhooksWebhookTest201Response**](CreateNetworkWebhooksWebhookTest201Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getNetworkWebhooksWebhookTest_2

> CreateNetworkWebhooksWebhookTest201Response getNetworkWebhooksWebhookTest_2(networkId, webhookTestId)

Return the status of a webhook test for a network

Return the status of a webhook test for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WebhookTestsApi();
let networkId = "networkId_example"; // String | 
let webhookTestId = "webhookTestId_example"; // String | 
apiInstance.getNetworkWebhooksWebhookTest_2(networkId, webhookTestId, (error, data, response) => {
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
 **webhookTestId** | **String**|  | 

### Return type

[**CreateNetworkWebhooksWebhookTest201Response**](CreateNetworkWebhooksWebhookTest201Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

