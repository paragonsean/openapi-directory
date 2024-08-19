# OrbitApi.WebhooksApi

All URIs are relative to *https://app.orbit.love/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workspaceSlugWebhooksGet**](WebhooksApi.md#workspaceSlugWebhooksGet) | **GET** /{workspace_slug}/webhooks | List webhooks in a workspace
[**workspaceSlugWebhooksIdDelete**](WebhooksApi.md#workspaceSlugWebhooksIdDelete) | **DELETE** /{workspace_slug}/webhooks/{id} | Delete a webhook
[**workspaceSlugWebhooksIdGet**](WebhooksApi.md#workspaceSlugWebhooksIdGet) | **GET** /{workspace_slug}/webhooks/{id} | Get a webhook
[**workspaceSlugWebhooksIdPut**](WebhooksApi.md#workspaceSlugWebhooksIdPut) | **PUT** /{workspace_slug}/webhooks/{id} | Update a webhook
[**workspaceSlugWebhooksPost**](WebhooksApi.md#workspaceSlugWebhooksPost) | **POST** /{workspace_slug}/webhooks | Create a webhook



## workspaceSlugWebhooksGet

> workspaceSlugWebhooksGet(workspaceSlug)

List webhooks in a workspace

### Example

```javascript
import OrbitApi from 'orbit_api';
let defaultClient = OrbitApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new OrbitApi.WebhooksApi();
let workspaceSlug = "workspaceSlug_example"; // String | 
apiInstance.workspaceSlugWebhooksGet(workspaceSlug, (error, data, response) => {
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
 **workspaceSlug** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspaceSlugWebhooksIdDelete

> workspaceSlugWebhooksIdDelete(workspaceSlug, id)

Delete a webhook

### Example

```javascript
import OrbitApi from 'orbit_api';
let defaultClient = OrbitApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new OrbitApi.WebhooksApi();
let workspaceSlug = "workspaceSlug_example"; // String | 
let id = "id_example"; // String | 
apiInstance.workspaceSlugWebhooksIdDelete(workspaceSlug, id, (error, data, response) => {
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
 **workspaceSlug** | **String**|  | 
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## workspaceSlugWebhooksIdGet

> workspaceSlugWebhooksIdGet(workspaceSlug, id)

Get a webhook

### Example

```javascript
import OrbitApi from 'orbit_api';
let defaultClient = OrbitApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new OrbitApi.WebhooksApi();
let workspaceSlug = "workspaceSlug_example"; // String | 
let id = "id_example"; // String | 
apiInstance.workspaceSlugWebhooksIdGet(workspaceSlug, id, (error, data, response) => {
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
 **workspaceSlug** | **String**|  | 
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspaceSlugWebhooksIdPut

> workspaceSlugWebhooksIdPut(workspaceSlug, id, opts)

Update a webhook

### Example

```javascript
import OrbitApi from 'orbit_api';
let defaultClient = OrbitApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new OrbitApi.WebhooksApi();
let workspaceSlug = "workspaceSlug_example"; // String | 
let id = "id_example"; // String | 
let opts = {
  'webhookSubscription': new OrbitApi.WebhookSubscription() // WebhookSubscription | 
};
apiInstance.workspaceSlugWebhooksIdPut(workspaceSlug, id, opts, (error, data, response) => {
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
 **workspaceSlug** | **String**|  | 
 **id** | **String**|  | 
 **webhookSubscription** | [**WebhookSubscription**](WebhookSubscription.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## workspaceSlugWebhooksPost

> workspaceSlugWebhooksPost(workspaceSlug, opts)

Create a webhook

### Example

```javascript
import OrbitApi from 'orbit_api';
let defaultClient = OrbitApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new OrbitApi.WebhooksApi();
let workspaceSlug = "workspaceSlug_example"; // String | 
let opts = {
  'webhookSubscription': new OrbitApi.WebhookSubscription() // WebhookSubscription | 
};
apiInstance.workspaceSlugWebhooksPost(workspaceSlug, opts, (error, data, response) => {
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
 **workspaceSlug** | **String**|  | 
 **webhookSubscription** | [**WebhookSubscription**](WebhookSubscription.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

