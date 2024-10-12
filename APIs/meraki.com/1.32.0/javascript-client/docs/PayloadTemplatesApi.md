# MerakiDashboardApi.PayloadTemplatesApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createNetworkWebhooksPayloadTemplate_2**](PayloadTemplatesApi.md#createNetworkWebhooksPayloadTemplate_2) | **POST** /networks/{networkId}/webhooks/payloadTemplates | Create a webhook payload template for a network
[**deleteNetworkWebhooksPayloadTemplate_2**](PayloadTemplatesApi.md#deleteNetworkWebhooksPayloadTemplate_2) | **DELETE** /networks/{networkId}/webhooks/payloadTemplates/{payloadTemplateId} | Destroy a webhook payload template for a network
[**getNetworkWebhooksPayloadTemplate_2**](PayloadTemplatesApi.md#getNetworkWebhooksPayloadTemplate_2) | **GET** /networks/{networkId}/webhooks/payloadTemplates/{payloadTemplateId} | Get the webhook payload template for a network
[**getNetworkWebhooksPayloadTemplates_2**](PayloadTemplatesApi.md#getNetworkWebhooksPayloadTemplates_2) | **GET** /networks/{networkId}/webhooks/payloadTemplates | List the webhook payload templates for a network
[**updateNetworkWebhooksPayloadTemplate_2**](PayloadTemplatesApi.md#updateNetworkWebhooksPayloadTemplate_2) | **PUT** /networks/{networkId}/webhooks/payloadTemplates/{payloadTemplateId} | Update a webhook payload template for a network



## createNetworkWebhooksPayloadTemplate_2

> GetNetworkWebhooksPayloadTemplates200ResponseInner createNetworkWebhooksPayloadTemplate_2(networkId, createNetworkWebhooksPayloadTemplateRequest)

Create a webhook payload template for a network

Create a webhook payload template for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.PayloadTemplatesApi();
let networkId = "networkId_example"; // String | 
let createNetworkWebhooksPayloadTemplateRequest = new MerakiDashboardApi.CreateNetworkWebhooksPayloadTemplateRequest(); // CreateNetworkWebhooksPayloadTemplateRequest | 
apiInstance.createNetworkWebhooksPayloadTemplate_2(networkId, createNetworkWebhooksPayloadTemplateRequest, (error, data, response) => {
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
 **createNetworkWebhooksPayloadTemplateRequest** | [**CreateNetworkWebhooksPayloadTemplateRequest**](CreateNetworkWebhooksPayloadTemplateRequest.md)|  | 

### Return type

[**GetNetworkWebhooksPayloadTemplates200ResponseInner**](GetNetworkWebhooksPayloadTemplates200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteNetworkWebhooksPayloadTemplate_2

> deleteNetworkWebhooksPayloadTemplate_2(networkId, payloadTemplateId)

Destroy a webhook payload template for a network

Destroy a webhook payload template for a network. Does not work for included templates (&#39;wpt_00001&#39;, &#39;wpt_00002&#39;, &#39;wpt_00003&#39;, &#39;wpt_00004&#39;, &#39;wpt_00005&#39; or &#39;wpt_00006&#39;)

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.PayloadTemplatesApi();
let networkId = "networkId_example"; // String | 
let payloadTemplateId = "payloadTemplateId_example"; // String | 
apiInstance.deleteNetworkWebhooksPayloadTemplate_2(networkId, payloadTemplateId, (error, data, response) => {
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
 **payloadTemplateId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNetworkWebhooksPayloadTemplate_2

> GetNetworkWebhooksPayloadTemplates200ResponseInner getNetworkWebhooksPayloadTemplate_2(networkId, payloadTemplateId)

Get the webhook payload template for a network

Get the webhook payload template for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.PayloadTemplatesApi();
let networkId = "networkId_example"; // String | 
let payloadTemplateId = "payloadTemplateId_example"; // String | 
apiInstance.getNetworkWebhooksPayloadTemplate_2(networkId, payloadTemplateId, (error, data, response) => {
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
 **payloadTemplateId** | **String**|  | 

### Return type

[**GetNetworkWebhooksPayloadTemplates200ResponseInner**](GetNetworkWebhooksPayloadTemplates200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkWebhooksPayloadTemplates_2

> [GetNetworkWebhooksPayloadTemplates200ResponseInner] getNetworkWebhooksPayloadTemplates_2(networkId)

List the webhook payload templates for a network

List the webhook payload templates for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.PayloadTemplatesApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkWebhooksPayloadTemplates_2(networkId, (error, data, response) => {
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

[**[GetNetworkWebhooksPayloadTemplates200ResponseInner]**](GetNetworkWebhooksPayloadTemplates200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateNetworkWebhooksPayloadTemplate_2

> GetNetworkWebhooksPayloadTemplates200ResponseInner updateNetworkWebhooksPayloadTemplate_2(networkId, payloadTemplateId, opts)

Update a webhook payload template for a network

Update a webhook payload template for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.PayloadTemplatesApi();
let networkId = "networkId_example"; // String | 
let payloadTemplateId = "payloadTemplateId_example"; // String | 
let opts = {
  'updateNetworkWebhooksPayloadTemplateRequest': new MerakiDashboardApi.UpdateNetworkWebhooksPayloadTemplateRequest() // UpdateNetworkWebhooksPayloadTemplateRequest | 
};
apiInstance.updateNetworkWebhooksPayloadTemplate_2(networkId, payloadTemplateId, opts, (error, data, response) => {
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
 **payloadTemplateId** | **String**|  | 
 **updateNetworkWebhooksPayloadTemplateRequest** | [**UpdateNetworkWebhooksPayloadTemplateRequest**](UpdateNetworkWebhooksPayloadTemplateRequest.md)|  | [optional] 

### Return type

[**GetNetworkWebhooksPayloadTemplates200ResponseInner**](GetNetworkWebhooksPayloadTemplates200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

