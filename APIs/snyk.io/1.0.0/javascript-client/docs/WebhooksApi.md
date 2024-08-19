# SnykApi.WebhooksApi

All URIs are relative to *https://api.snyk.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createAWebhook**](WebhooksApi.md#createAWebhook) | **POST** /org/{orgId}/webhooks | Create a webhook
[**deleteAWebhook**](WebhooksApi.md#deleteAWebhook) | **DELETE** /org/{orgId}/webhooks/{webhookId} | Delete a webhook
[**listWebhooks**](WebhooksApi.md#listWebhooks) | **GET** /org/{orgId}/webhooks | List webhooks
[**pingAWebhook**](WebhooksApi.md#pingAWebhook) | **POST** /org/{orgId}/webhooks/{webhookId}/ping | Ping a webhook
[**retrieveAWebhook**](WebhooksApi.md#retrieveAWebhook) | **GET** /org/{orgId}/webhooks/{webhookId} | Retrieve a webhook



## createAWebhook

> createAWebhook(orgId, opts)

Create a webhook



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.WebhooksApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID to list projects for. The `API_KEY` must have access to this organization.
let opts = {
  'createAWebhookRequest': new SnykApi.CreateAWebhookRequest() // CreateAWebhookRequest | 
};
apiInstance.createAWebhook(orgId, opts, (error, data, response) => {
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
 **orgId** | **String**| The organization ID to list projects for. The &#x60;API_KEY&#x60; must have access to this organization. | 
 **createAWebhookRequest** | [**CreateAWebhookRequest**](CreateAWebhookRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## deleteAWebhook

> deleteAWebhook(orgId, webhookId)

Delete a webhook



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.WebhooksApi();
let orgId = "orgId_example"; // String | Automatically added
let webhookId = "webhookId_example"; // String | Automatically added
apiInstance.deleteAWebhook(orgId, webhookId, (error, data, response) => {
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
 **orgId** | **String**| Automatically added | 
 **webhookId** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listWebhooks

> listWebhooks(orgId)

List webhooks



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.WebhooksApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID to list projects for. The `API_KEY` must have access to this organization.
apiInstance.listWebhooks(orgId, (error, data, response) => {
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
 **orgId** | **String**| The organization ID to list projects for. The &#x60;API_KEY&#x60; must have access to this organization. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## pingAWebhook

> pingAWebhook(orgId, webhookId)

Ping a webhook



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.WebhooksApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID the project belongs to. The `API_KEY` must have access to this organization.
let webhookId = "463c1ee5-31bc-428c-b451-b79a3270db08"; // String | The webhook ID.
apiInstance.pingAWebhook(orgId, webhookId, (error, data, response) => {
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
 **orgId** | **String**| The organization ID the project belongs to. The &#x60;API_KEY&#x60; must have access to this organization. | 
 **webhookId** | **String**| The webhook ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## retrieveAWebhook

> retrieveAWebhook(orgId, webhookId)

Retrieve a webhook



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.WebhooksApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID the project belongs to. The `API_KEY` must have access to this organization.
let webhookId = "463c1ee5-31bc-428c-b451-b79a3270db08"; // String | The webhook ID.
apiInstance.retrieveAWebhook(orgId, webhookId, (error, data, response) => {
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
 **orgId** | **String**| The organization ID the project belongs to. The &#x60;API_KEY&#x60; must have access to this organization. | 
 **webhookId** | **String**| The webhook ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

