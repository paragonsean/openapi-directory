# AvazaApiDocumentation.WebhookApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhookDelete**](WebhookApi.md#webhookDelete) | **DELETE** /api/Webhook/{id} | Delete Webhook Subscription by ID
[**webhookDeleteByUrl**](WebhookApi.md#webhookDeleteByUrl) | **DELETE** /api/Webhook | Delete webhook subscription by URL
[**webhookGet**](WebhookApi.md#webhookGet) | **GET** /api/Webhook | Get list of Webhook Subscriptions
[**webhookGetByID**](WebhookApi.md#webhookGetByID) | **GET** /api/Webhook/{id} | Get Webhook Subscription by SubscriptionID
[**webhookPost**](WebhookApi.md#webhookPost) | **POST** /api/Webhook | Subscribe to Webhook. On success, returns ID of webhook subscription.



## webhookDelete

> Object webhookDelete(id)

Delete Webhook Subscription by ID

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.WebhookApi();
let id = 56; // Number | Subscription id to be deleted
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
 **id** | **Number**| Subscription id to be deleted | 

### Return type

**Object**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## webhookDeleteByUrl

> Object webhookDeleteByUrl(targetUrl)

Delete webhook subscription by URL

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.WebhookApi();
let targetUrl = "targetUrl_example"; // String | Target URL that should be used to delete subscriptions
apiInstance.webhookDeleteByUrl(targetUrl, (error, data, response) => {
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
 **targetUrl** | **String**| Target URL that should be used to delete subscriptions | 

### Return type

**Object**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## webhookGet

> WebhookList webhookGet()

Get list of Webhook Subscriptions

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.WebhookApi();
apiInstance.webhookGet((error, data, response) => {
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

[**WebhookList**](WebhookList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## webhookGetByID

> WebhookList webhookGetByID(id)

Get Webhook Subscription by SubscriptionID

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.WebhookApi();
let id = 56; // Number | 
apiInstance.webhookGetByID(id, (error, data, response) => {
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
 **id** | **Number**|  | 

### Return type

[**WebhookList**](WebhookList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## webhookPost

> SubscribeResult webhookPost(model)

Subscribe to Webhook. On success, returns ID of webhook subscription.

When you receive a webhook, you should respond with Http 200 OK Status Code, otherwise we will retry. To create a webhook, you need both the webhook_notifications scope, as well as the scope for the required entity being monitored.  Event values are: \&quot;company_created\&quot;, \&quot;company_deleted\&quot;, \&quot;company_updated\&quot;, \&quot;contact_created\&quot;, \&quot;contact_deleted\&quot;, \&quot;contact_updated\&quot;, \&quot;invoice_created\&quot;, \&quot;invoice_sent\&quot;,\&quot;invoice_updated\&quot;,\&quot;invoice_deleted\&quot;, \&quot;project_created\&quot;, \&quot;project_deleted\&quot;, \&quot;project_updated\&quot;, \&quot;task_created\&quot;, \&quot;task_updated\&quot;,\&quot;task_deleted\&quot;, \&quot;timesheet_created\&quot;, \&quot;timesheet_deleted\&quot;, \&quot;timesheet_updated, \&quot;bill_created\&quot;, \&quot;bill_updated\&quot;.  You can subscribe to any webhook, but you will only receive notifications for data appropriate to the roles of your user account. There is an optional  Secret parameter (string 255 char max). This allows for webhook authentication. If provided, the Secret will be BASE 64 encoded and passed with notications as a basic authentication http header. i.e. Authorization Basic [BASE64 of Secret]\&quot;

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.WebhookApi();
let model = new AvazaApiDocumentation.CreateSubscription(); // CreateSubscription | 
apiInstance.webhookPost(model, (error, data, response) => {
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
 **model** | [**CreateSubscription**](CreateSubscription.md)|  | 

### Return type

[**SubscribeResult**](SubscribeResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml

