# MerakiDashboardApi.MqttBrokersApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createNetworkMqttBroker_1**](MqttBrokersApi.md#createNetworkMqttBroker_1) | **POST** /networks/{networkId}/mqttBrokers | Add an MQTT broker
[**deleteNetworkMqttBroker_1**](MqttBrokersApi.md#deleteNetworkMqttBroker_1) | **DELETE** /networks/{networkId}/mqttBrokers/{mqttBrokerId} | Delete an MQTT broker
[**getNetworkMqttBroker_1**](MqttBrokersApi.md#getNetworkMqttBroker_1) | **GET** /networks/{networkId}/mqttBrokers/{mqttBrokerId} | Return an MQTT broker
[**getNetworkMqttBrokers_1**](MqttBrokersApi.md#getNetworkMqttBrokers_1) | **GET** /networks/{networkId}/mqttBrokers | List the MQTT brokers for this network
[**updateNetworkMqttBroker_1**](MqttBrokersApi.md#updateNetworkMqttBroker_1) | **PUT** /networks/{networkId}/mqttBrokers/{mqttBrokerId} | Update an MQTT broker



## createNetworkMqttBroker_1

> Object createNetworkMqttBroker_1(networkId, createNetworkMqttBrokerRequest)

Add an MQTT broker

Add an MQTT broker

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MqttBrokersApi();
let networkId = "networkId_example"; // String | 
let createNetworkMqttBrokerRequest = new MerakiDashboardApi.CreateNetworkMqttBrokerRequest(); // CreateNetworkMqttBrokerRequest | 
apiInstance.createNetworkMqttBroker_1(networkId, createNetworkMqttBrokerRequest, (error, data, response) => {
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
 **createNetworkMqttBrokerRequest** | [**CreateNetworkMqttBrokerRequest**](CreateNetworkMqttBrokerRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteNetworkMqttBroker_1

> deleteNetworkMqttBroker_1(networkId, mqttBrokerId)

Delete an MQTT broker

Delete an MQTT broker

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MqttBrokersApi();
let networkId = "networkId_example"; // String | 
let mqttBrokerId = "mqttBrokerId_example"; // String | 
apiInstance.deleteNetworkMqttBroker_1(networkId, mqttBrokerId, (error, data, response) => {
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
 **mqttBrokerId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNetworkMqttBroker_1

> Object getNetworkMqttBroker_1(networkId, mqttBrokerId)

Return an MQTT broker

Return an MQTT broker

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MqttBrokersApi();
let networkId = "networkId_example"; // String | 
let mqttBrokerId = "mqttBrokerId_example"; // String | 
apiInstance.getNetworkMqttBroker_1(networkId, mqttBrokerId, (error, data, response) => {
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
 **mqttBrokerId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkMqttBrokers_1

> [Object] getNetworkMqttBrokers_1(networkId)

List the MQTT brokers for this network

List the MQTT brokers for this network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MqttBrokersApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkMqttBrokers_1(networkId, (error, data, response) => {
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


## updateNetworkMqttBroker_1

> Object updateNetworkMqttBroker_1(networkId, mqttBrokerId, opts)

Update an MQTT broker

Update an MQTT broker

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MqttBrokersApi();
let networkId = "networkId_example"; // String | 
let mqttBrokerId = "mqttBrokerId_example"; // String | 
let opts = {
  'updateNetworkMqttBrokerRequest': new MerakiDashboardApi.UpdateNetworkMqttBrokerRequest() // UpdateNetworkMqttBrokerRequest | 
};
apiInstance.updateNetworkMqttBroker_1(networkId, mqttBrokerId, opts, (error, data, response) => {
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
 **mqttBrokerId** | **String**|  | 
 **updateNetworkMqttBrokerRequest** | [**UpdateNetworkMqttBrokerRequest**](UpdateNetworkMqttBrokerRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

