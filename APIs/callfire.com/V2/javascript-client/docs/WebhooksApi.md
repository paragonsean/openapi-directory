# CallFireApiDocumentation.WebhooksApi

All URIs are relative to *https://api.callfire.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createWebhook**](WebhooksApi.md#createWebhook) | **POST** /webhooks | Create a webhook
[**deleteWebhook**](WebhooksApi.md#deleteWebhook) | **DELETE** /webhooks/{id} | Delete a webhook
[**findWebhookResources**](WebhooksApi.md#findWebhookResources) | **GET** /webhooks/resources | Find webhook resources
[**findWebhooks**](WebhooksApi.md#findWebhooks) | **GET** /webhooks | Find webhooks
[**getWebhook**](WebhooksApi.md#getWebhook) | **GET** /webhooks/{id} | Find a specific webhook
[**getWebhookResource**](WebhooksApi.md#getWebhookResource) | **GET** /webhooks/resources/{resource} | Find specific webhook resource
[**updateWebhook**](WebhooksApi.md#updateWebhook) | **PUT** /webhooks/{id} | Update a webhook



## createWebhook

> ResourceId createWebhook(opts)

Create a webhook

Create a Webhook for notification in the CallFire system. Use the webhooks API to receive notifications of important CallFire events. Select the resource to listen to, and then choose the resource events to receive notifications on. When an event triggers, a POST will be made to the callback URL with a payload of notification information. Available resources and their events include &#39;CccCampaign&#39;: [&#39;started&#39;, &#39;stopped&#39;, &#39;finished&#39;], &#39;CallBroadcast&#39;: [&#39;started&#39;, &#39;stopped&#39;, &#39;finished&#39;], &#39;TextBroadcast&#39;: [&#39;started&#39;, &#39;stopped&#39;, &#39;finished&#39;], &#39;OutboundCall&#39;: [&#39;finished&#39;], &#39;InboundCall&#39;: [&#39;finished&#39;], &#39;OutboundText&#39;: [&#39;finished&#39;], &#39;InboundText&#39;: [&#39;finished&#39;], &#39;ContactList&#39;: [&#39;validationFinished&#39;, &#39;validationFailed&#39;], &#39;MonthlyRenewal&#39;: [&#39;failed&#39;, &#39;finished&#39;], &#39;LowBalance&#39;: [&#39;failed&#39;, &#39;finished&#39;]. Webhooks support secret token which is used as signing key to HmacSHA1 hash of json payload which is returned in &#39;X-CallFire-Signature&#39; header. This header can be used to verify callback POST is coming from CallFire. See [security guide](https://developers.callfire.com/security-guide.html)

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.WebhooksApi();
let opts = {
  'webhook': new CallFireApiDocumentation.Webhook() // Webhook | A webhook object
};
apiInstance.createWebhook(opts, (error, data, response) => {
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
 **webhook** | [**Webhook**](Webhook.md)| A webhook object | [optional] 

### Return type

[**ResourceId**](ResourceId.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteWebhook

> deleteWebhook(id)

Delete a webhook

Deletes a webhook instance. Will be removed permanently

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.WebhooksApi();
let id = 789; // Number | An Id of a webhook
apiInstance.deleteWebhook(id, (error, data, response) => {
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
 **id** | **Number**| An Id of a webhook | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## findWebhookResources

> ItemListWebhookResource findWebhookResources(opts)

Find webhook resources

Searches for webhook resources. Available resources include &#39;CccCampaign&#39;: [&#39;started&#39;, &#39;stopped&#39;, &#39;finished&#39;], &#39;CallBroadcast&#39;: [&#39;started&#39;, &#39;stopped&#39;, &#39;finished&#39;], &#39;TextBroadcast&#39;: [&#39;started&#39;, &#39;stopped&#39;, &#39;finished&#39;], &#39;OutboundCall&#39;: [&#39;finished&#39;], &#39;InboundCall&#39;: [&#39;finished&#39;], &#39;OutboundText&#39;: [&#39;finished&#39;], &#39;InboundText&#39;: [&#39;finished&#39;], &#39;ContactList&#39;: [&#39;validationFinished&#39;, &#39;validationFailed&#39;], &#39;MonthlyRenewal&#39;: [&#39;failed&#39;, &#39;finished&#39;], &#39;LowBalance&#39;: [&#39;failed&#39;, &#39;finished&#39;]

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.WebhooksApi();
let opts = {
  'fields': "fields_example" // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
};
apiInstance.findWebhookResources(opts, (error, data, response) => {
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
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 

### Return type

[**ItemListWebhookResource**](ItemListWebhookResource.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## findWebhooks

> WebhookPage findWebhooks(opts)

Find webhooks

Searches all webhooks available for a current user. Searches by name, resource, event, callback URL, or whether they are enabled. Returns a paged list of Webhooks

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.WebhooksApi();
let opts = {
  'fields': "fields_example", // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
  'limit': 100, // Number | To set the maximum number of records to return in a paged list response. The default is 100
  'offset': 0, // Number | Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
  'name': "name_example", // String | A name of a webhook
  'resource': "resource_example", // String | A name of a resource, available values: 'CccCampaign', 'CallBroadcast', 'TextBroadcast',  'OutboundCall', 'OutboundText', 'InboundCall', 'InboundText', 'ContactList'
  'event': "event_example", // String | A name of event, available values: 'started', 'stopped', 'finished'
  'callback': "callback_example", // String | A callback URL
  'enabled': true // Boolean | Specifies whether webhook is enabled
};
apiInstance.findWebhooks(opts, (error, data, response) => {
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
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 
 **limit** | **Number**| To set the maximum number of records to return in a paged list response. The default is 100 | [optional] [default to 100]
 **offset** | **Number**| Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API. | [optional] [default to 0]
 **name** | **String**| A name of a webhook | [optional] 
 **resource** | **String**| A name of a resource, available values: &#39;CccCampaign&#39;, &#39;CallBroadcast&#39;, &#39;TextBroadcast&#39;,  &#39;OutboundCall&#39;, &#39;OutboundText&#39;, &#39;InboundCall&#39;, &#39;InboundText&#39;, &#39;ContactList&#39; | [optional] 
 **event** | **String**| A name of event, available values: &#39;started&#39;, &#39;stopped&#39;, &#39;finished&#39; | [optional] 
 **callback** | **String**| A callback URL | [optional] 
 **enabled** | **Boolean**| Specifies whether webhook is enabled | [optional] 

### Return type

[**WebhookPage**](WebhookPage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getWebhook

> Webhook getWebhook(id, opts)

Find a specific webhook

Returns a single Webhook instance for a given webhook id

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.WebhooksApi();
let id = 789; // Number | An id of a webhook
let opts = {
  'fields': "fields_example" // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
};
apiInstance.getWebhook(id, opts, (error, data, response) => {
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
 **id** | **Number**| An id of a webhook | 
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getWebhookResource

> WebhookResource getWebhookResource(resource, opts)

Find specific webhook resource

Returns information about supported events for a given webhook resource

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.WebhooksApi();
let resource = "resource_example"; // String | A name of a webhook resource. Available resources include 'CccCampaign': ['started', 'stopped', 'finished'], 'CallBroadcast': ['started', 'stopped', 'finished'], 'TextBroadcast': ['started', 'stopped', 'finished'], 'OutboundCall': ['finished'], 'InboundCall': ['finished'], 'OutboundText': ['finished'], 'InboundText': ['finished'], 'ContactList': ['validationFinished', 'validationFailed'], 'MonthlyRenewal': ['failed', 'finished'], 'LowBalance': ['failed', 'finished']
let opts = {
  'fields': "fields_example" // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
};
apiInstance.getWebhookResource(resource, opts, (error, data, response) => {
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
 **resource** | **String**| A name of a webhook resource. Available resources include &#39;CccCampaign&#39;: [&#39;started&#39;, &#39;stopped&#39;, &#39;finished&#39;], &#39;CallBroadcast&#39;: [&#39;started&#39;, &#39;stopped&#39;, &#39;finished&#39;], &#39;TextBroadcast&#39;: [&#39;started&#39;, &#39;stopped&#39;, &#39;finished&#39;], &#39;OutboundCall&#39;: [&#39;finished&#39;], &#39;InboundCall&#39;: [&#39;finished&#39;], &#39;OutboundText&#39;: [&#39;finished&#39;], &#39;InboundText&#39;: [&#39;finished&#39;], &#39;ContactList&#39;: [&#39;validationFinished&#39;, &#39;validationFailed&#39;], &#39;MonthlyRenewal&#39;: [&#39;failed&#39;, &#39;finished&#39;], &#39;LowBalance&#39;: [&#39;failed&#39;, &#39;finished&#39;] | 
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 

### Return type

[**WebhookResource**](WebhookResource.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateWebhook

> updateWebhook(id, opts)

Update a webhook

Updates the information in existing webhook

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.WebhooksApi();
let id = 789; // Number | An id of a webhook
let opts = {
  'webhook': new CallFireApiDocumentation.Webhook() // Webhook | A webhook object
};
apiInstance.updateWebhook(id, opts, (error, data, response) => {
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
 **id** | **Number**| An id of a webhook | 
 **webhook** | [**Webhook**](Webhook.md)| A webhook object | [optional] 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

