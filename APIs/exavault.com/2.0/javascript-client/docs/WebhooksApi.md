# ExaVault.WebhooksApi

All URIs are relative to *https://accountname.exavault.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addWebhook**](WebhooksApi.md#addWebhook) | **POST** /webhooks | Add A New Webhook
[**deleteWebhook**](WebhooksApi.md#deleteWebhook) | **DELETE** /webhooks/{id} | Delete a webhook
[**getWebhookById**](WebhooksApi.md#getWebhookById) | **GET** /webhooks/{id} | Get info for a webhook
[**getWehooksList**](WebhooksApi.md#getWehooksList) | **GET** /webhooks | Get Webhooks List
[**regenerateWebhookToken**](WebhooksApi.md#regenerateWebhookToken) | **POST** /webhooks/regenerate-token/{id} | Regenerate security token
[**resendWebhookActivityEntry**](WebhooksApi.md#resendWebhookActivityEntry) | **POST** /webhooks/resend/{activityId} | Resend a webhook message
[**updateWebhook**](WebhooksApi.md#updateWebhook) | **PATCH** /webhooks/{id} | Update a webhook



## addWebhook

> WebhookResponse addWebhook(evApiKey, evAccessToken, opts)

Add A New Webhook

Create a new Webhook on your account. Creating a Webhook will require an endpoint URL, a path, what events should trigger a webhook, and what request version to use. 

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.WebhooksApi();
let evApiKey = "evApiKey_example"; // String | API key required to make the API call.
let evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
let opts = {
  'addWebhookRequestBody': new ExaVault.AddWebhookRequestBody() // AddWebhookRequestBody | 
};
apiInstance.addWebhook(evApiKey, evAccessToken, opts, (error, data, response) => {
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
 **evApiKey** | **String**| API key required to make the API call. | 
 **evAccessToken** | **String**| Access token required to make the API call. | 
 **addWebhookRequestBody** | [**AddWebhookRequestBody**](AddWebhookRequestBody.md)|  | [optional] 

### Return type

[**WebhookResponse**](WebhookResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteWebhook

> EmptyResponse deleteWebhook(id, evApiKey, evAccessToken)

Delete a webhook

Deleted the specified webhook. This will not affect logs or any resources the webhook is connected to. 

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.WebhooksApi();
let id = 56; // Number | Webhook endpoint ID
let evApiKey = "evApiKey_example"; // String | API key required to make the API call.
let evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
apiInstance.deleteWebhook(id, evApiKey, evAccessToken, (error, data, response) => {
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
 **id** | **Number**| Webhook endpoint ID | 
 **evApiKey** | **String**| API key required to make the API call. | 
 **evAccessToken** | **String**| Access token required to make the API call. | 

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getWebhookById

> WebhookResponse getWebhookById(id, evApiKey, evAccessToken, opts)

Get info for a webhook

Returns the metadata for a specific webhook. Webhook IDs can be retrieve from GET /webhooks

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.WebhooksApi();
let id = 56; // Number | Webhook endpoint ID
let evApiKey = "evApiKey_example"; // String | API key required to make the API call.
let evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
let opts = {
  'include': "include_example" // String |  Include metadata for related items; `ownerAccount` and/or `resource` 
};
apiInstance.getWebhookById(id, evApiKey, evAccessToken, opts, (error, data, response) => {
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
 **id** | **Number**| Webhook endpoint ID | 
 **evApiKey** | **String**| API key required to make the API call. | 
 **evAccessToken** | **String**| Access token required to make the API call. | 
 **include** | **String**|  Include metadata for related items; &#x60;ownerAccount&#x60; and/or &#x60;resource&#x60;  | [optional] 

### Return type

[**WebhookResponse**](WebhookResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getWehooksList

> WebhookCollectionResponse getWehooksList(evApiKey, evAccessToken, opts)

Get Webhooks List

Returns a list of Webhooks. By default, this will return metadata on all Webhooks within the account. 

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.WebhooksApi();
let evApiKey = "evApiKey_example"; // String | API key required to make the API call.
let evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
let opts = {
  'include': "include_example", // String | List of related record types to include. Valid options are `owningAccount` and `resource`
  'offset': 100, // Number | Records to skip before returning results.
  'limit': 10 // Number | Limit of the records list
};
apiInstance.getWehooksList(evApiKey, evAccessToken, opts, (error, data, response) => {
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
 **evApiKey** | **String**| API key required to make the API call. | 
 **evAccessToken** | **String**| Access token required to make the API call. | 
 **include** | **String**| List of related record types to include. Valid options are &#x60;owningAccount&#x60; and &#x60;resource&#x60; | [optional] 
 **offset** | **Number**| Records to skip before returning results. | [optional] 
 **limit** | **Number**| Limit of the records list | [optional] 

### Return type

[**WebhookCollectionResponse**](WebhookCollectionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## regenerateWebhookToken

> WebhookResponse regenerateWebhookToken(id, evApiKey, evAccessToken)

Regenerate security token

This endpoint will allow you to regenerate the security token for a webhook if you believe it’s been compromised in any way. 

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.WebhooksApi();
let id = "id_example"; // String | Webhook ID
let evApiKey = "evApiKey_example"; // String | API key required to make the API call.
let evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
apiInstance.regenerateWebhookToken(id, evApiKey, evAccessToken, (error, data, response) => {
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
 **id** | **String**| Webhook ID | 
 **evApiKey** | **String**| API key required to make the API call. | 
 **evAccessToken** | **String**| Access token required to make the API call. | 

### Return type

[**WebhookResponse**](WebhookResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resendWebhookActivityEntry

> EmptyResponse resendWebhookActivityEntry(activityId, evApiKey, evAccessToken)

Resend a webhook message

This endpoint will allow you to resend a webhook that was previously sent. Resent webhooks will send exactly the same as the original webhook with the exception of the “sent” timestamp. Activity IDs can be retrieve from the webhook logs in your account or via GET /activity/webhooks

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.WebhooksApi();
let activityId = "activityId_example"; // String | Webhooks activity entry ID
let evApiKey = "evApiKey_example"; // String | API key required to make the API call.
let evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
apiInstance.resendWebhookActivityEntry(activityId, evApiKey, evAccessToken, (error, data, response) => {
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
 **activityId** | **String**| Webhooks activity entry ID | 
 **evApiKey** | **String**| API key required to make the API call. | 
 **evAccessToken** | **String**| Access token required to make the API call. | 

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateWebhook

> WebhookResponse updateWebhook(id, evApiKey, evAccessToken, opts)

Update a webhook

Update the specified webhook. Updated webhooks will take effect immediately and could impact active workflows. Please be certain the webhook is not currently in use prior to updating.   You only need to send the portions of the webhook configuration you wish to change, rather than the entire webhook object.

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.WebhooksApi();
let id = 56; // Number | Webhook endpoint ID
let evApiKey = "evApiKey_example"; // String | API key required to make the API call.
let evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
let opts = {
  'updateWebhookRequestBody': new ExaVault.UpdateWebhookRequestBody() // UpdateWebhookRequestBody | 
};
apiInstance.updateWebhook(id, evApiKey, evAccessToken, opts, (error, data, response) => {
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
 **id** | **Number**| Webhook endpoint ID | 
 **evApiKey** | **String**| API key required to make the API call. | 
 **evAccessToken** | **String**| Access token required to make the API call. | 
 **updateWebhookRequestBody** | [**UpdateWebhookRequestBody**](UpdateWebhookRequestBody.md)|  | [optional] 

### Return type

[**WebhookResponse**](WebhookResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

