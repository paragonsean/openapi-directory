# SwaggerApi2Cart.WebhookApi

All URIs are relative to *https://api.api2cart.com/v1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhookCount**](WebhookApi.md#webhookCount) | **GET** /webhook.count.json | 
[**webhookCreate**](WebhookApi.md#webhookCreate) | **POST** /webhook.create.json | 
[**webhookDelete**](WebhookApi.md#webhookDelete) | **DELETE** /webhook.delete.json | 
[**webhookEvents**](WebhookApi.md#webhookEvents) | **GET** /webhook.events.json | 
[**webhookList**](WebhookApi.md#webhookList) | **GET** /webhook.list.json | 
[**webhookUpdate**](WebhookApi.md#webhookUpdate) | **PUT** /webhook.update.json | 



## webhookCount

> WebhookCount200Response webhookCount(opts)



Count registered webhooks on the store.

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.WebhookApi();
let opts = {
  'entity': "entity_example", // String | The entity you want to filter webhooks by (e.g. order or product)
  'action': "action_example", // String | The action you want to filter webhooks by (e.g. order or product)
  'active': true // Boolean | The webhook status you want to filter webhooks by
};
apiInstance.webhookCount(opts, (error, data, response) => {
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
 **entity** | **String**| The entity you want to filter webhooks by (e.g. order or product) | [optional] 
 **action** | **String**| The action you want to filter webhooks by (e.g. order or product) | [optional] 
 **active** | **Boolean**| The webhook status you want to filter webhooks by | [optional] 

### Return type

[**WebhookCount200Response**](WebhookCount200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webhookCreate

> AttributeAdd200Response webhookCreate(entity, action, opts)



Create webhook on the store and subscribe to it.

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.WebhookApi();
let entity = "entity_example"; // String | Specify the entity that you want to enable webhooks for (e.g product, order, customer, category)
let action = "action_example"; // String | Specify what action (event) will trigger the webhook (e.g add, delete, or update)
let opts = {
  'callback': "callback_example", // String | Callback url that returns shipping rates. It should be able to accept POST requests with json data.
  'label': "label_example", // String | The name you give to the webhook
  'fields': "'force_all'", // String | Fields the webhook should send
  'active': true, // Boolean | Webhook status
  'storeId': "storeId_example" // String | Defines store id where the webhook should be assigned
};
apiInstance.webhookCreate(entity, action, opts, (error, data, response) => {
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
 **entity** | **String**| Specify the entity that you want to enable webhooks for (e.g product, order, customer, category) | 
 **action** | **String**| Specify what action (event) will trigger the webhook (e.g add, delete, or update) | 
 **callback** | **String**| Callback url that returns shipping rates. It should be able to accept POST requests with json data. | [optional] 
 **label** | **String**| The name you give to the webhook | [optional] 
 **fields** | **String**| Fields the webhook should send | [optional] [default to &#39;force_all&#39;]
 **active** | **Boolean**| Webhook status | [optional] [default to true]
 **storeId** | **String**| Defines store id where the webhook should be assigned | [optional] 

### Return type

[**AttributeAdd200Response**](AttributeAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webhookDelete

> AttributeDelete200Response webhookDelete(id)



Delete registered webhook on the store.

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.WebhookApi();
let id = "id_example"; // String | Webhook id
apiInstance.webhookDelete(id, (error, data, response) => {
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
 **id** | **String**| Webhook id | 

### Return type

[**AttributeDelete200Response**](AttributeDelete200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webhookEvents

> WebhookEvents200Response webhookEvents()



List all Webhooks that are available on this store.

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.WebhookApi();
apiInstance.webhookEvents((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**WebhookEvents200Response**](WebhookEvents200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webhookList

> WebhookList200Response webhookList(opts)



List registered webhook on the store.

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.WebhookApi();
let opts = {
  'params': "'id,entity,action,callback'", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'start': 0, // Number | This parameter sets the number from which you want to get entities
  'count': 10, // Number | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
  'entity': "entity_example", // String | The entity you want to filter webhooks by (e.g. order or product)
  'action': "action_example", // String | The action you want to filter webhooks by (e.g. add, update, or delete)
  'active': true, // Boolean | The webhook status you want to filter webhooks by
  'ids': "ids_example" // String | List of сomma-separated webhook ids
};
apiInstance.webhookList(opts, (error, data, response) => {
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
 **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to &#39;id,entity,action,callback&#39;]
 **start** | **Number**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **count** | **Number**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **entity** | **String**| The entity you want to filter webhooks by (e.g. order or product) | [optional] 
 **action** | **String**| The action you want to filter webhooks by (e.g. add, update, or delete) | [optional] 
 **active** | **Boolean**| The webhook status you want to filter webhooks by | [optional] 
 **ids** | **String**| List of сomma-separated webhook ids | [optional] 

### Return type

[**WebhookList200Response**](WebhookList200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webhookUpdate

> ProductImageUpdate200Response webhookUpdate(id, opts)



Update Webhooks parameters.

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.WebhookApi();
let id = "id_example"; // String | Webhook id
let opts = {
  'callback': "callback_example", // String | Callback url that returns shipping rates. It should be able to accept POST requests with json data.
  'label': "label_example", // String | The name you give to the webhook
  'fields': "fields_example", // String | Fields the webhook should send
  'active': true // Boolean | Webhook status
};
apiInstance.webhookUpdate(id, opts, (error, data, response) => {
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
 **id** | **String**| Webhook id | 
 **callback** | **String**| Callback url that returns shipping rates. It should be able to accept POST requests with json data. | [optional] 
 **label** | **String**| The name you give to the webhook | [optional] 
 **fields** | **String**| Fields the webhook should send | [optional] 
 **active** | **Boolean**| Webhook status | [optional] 

### Return type

[**ProductImageUpdate200Response**](ProductImageUpdate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

