# SalesLoftPlatform.WebhookSubscriptionsApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2WebhookSubscriptionsGet**](WebhookSubscriptionsApi.md#v2WebhookSubscriptionsGet) | **GET** /v2/webhook_subscriptions | List webhook subscriptions
[**v2WebhookSubscriptionsIdDelete**](WebhookSubscriptionsApi.md#v2WebhookSubscriptionsIdDelete) | **DELETE** /v2/webhook_subscriptions/{id} | Delete a webhook subscription
[**v2WebhookSubscriptionsIdGet**](WebhookSubscriptionsApi.md#v2WebhookSubscriptionsIdGet) | **GET** /v2/webhook_subscriptions/{id} | Fetch a webhook subscription
[**v2WebhookSubscriptionsIdPut**](WebhookSubscriptionsApi.md#v2WebhookSubscriptionsIdPut) | **PUT** /v2/webhook_subscriptions/{id} | Update a webhook subscription
[**v2WebhookSubscriptionsPost**](WebhookSubscriptionsApi.md#v2WebhookSubscriptionsPost) | **POST** /v2/webhook_subscriptions | Create a webhook subscription



## v2WebhookSubscriptionsGet

> [Subscription] v2WebhookSubscriptionsGet(opts)

List webhook subscriptions

Fetches all of the customer&#39;s webhook subscriptions for your application.

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.WebhookSubscriptionsApi();
let opts = {
  'enabled': true // Boolean | Filters webhook subscriptions by whether is enabled or not.
};
apiInstance.v2WebhookSubscriptionsGet(opts, (error, data, response) => {
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
 **enabled** | **Boolean**| Filters webhook subscriptions by whether is enabled or not. | [optional] 

### Return type

[**[Subscription]**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## v2WebhookSubscriptionsIdDelete

> v2WebhookSubscriptionsIdDelete(id)

Delete a webhook subscription

Deletes a webhook subscription. This operation is not reversible without contacting support. This operation can be called multiple times successfully.

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.WebhookSubscriptionsApi();
let id = 56; // Number | The id of the Webhook Subscription to delete
apiInstance.v2WebhookSubscriptionsIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| The id of the Webhook Subscription to delete | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## v2WebhookSubscriptionsIdGet

> Subscription v2WebhookSubscriptionsIdGet(id)

Fetch a webhook subscription

Fetches a webhook subscription, by ID only.

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.WebhookSubscriptionsApi();
let id = 56; // Number | The id for the Webhook Subscription
apiInstance.v2WebhookSubscriptionsIdGet(id, (error, data, response) => {
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
 **id** | **Number**| The id for the Webhook Subscription | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## v2WebhookSubscriptionsIdPut

> Subscription v2WebhookSubscriptionsIdPut(id, opts)

Update a webhook subscription

Updates a webhook subscription. Request must be made with a valid Oauth token or API key.

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.WebhookSubscriptionsApi();
let id = 56; // Number | The Webhook Suscription id to update
let opts = {
  'enabled': true // Boolean | Enable or disable the webhook subscription
};
apiInstance.v2WebhookSubscriptionsIdPut(id, opts, (error, data, response) => {
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
 **id** | **Number**| The Webhook Suscription id to update | 
 **enabled** | **Boolean**| Enable or disable the webhook subscription | [optional] 

### Return type

[**Subscription**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: */*


## v2WebhookSubscriptionsPost

> Subscription v2WebhookSubscriptionsPost(callbackToken, callbackUrl, eventType)

Create a webhook subscription

Creates a webhook subscription. Visit the &lt;a href&#x3D;\&quot;/webhooks.html\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;webhooks page&lt;/a&gt; for additional details and a list of available webhooks. Request must be made with a valid Oauth token or API key.

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.WebhookSubscriptionsApi();
let callbackToken = "callbackToken_example"; // String | Any string to be used as a shared secret when subscription events are published. SalesLoft will send the value of this callback_token in the payload of each event so the receiver may verify it matches the original value. This ensures webhook events are being delivered by SalesLoft.
let callbackUrl = "callbackUrl_example"; // String | URL for your callback handler
let eventType = "eventType_example"; // String | Type of event the subscription is for. Visit the \\\"Event Types\\\" section of the webhooks page to find a list of supported event types.
apiInstance.v2WebhookSubscriptionsPost(callbackToken, callbackUrl, eventType, (error, data, response) => {
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
 **callbackToken** | **String**| Any string to be used as a shared secret when subscription events are published. SalesLoft will send the value of this callback_token in the payload of each event so the receiver may verify it matches the original value. This ensures webhook events are being delivered by SalesLoft. | 
 **callbackUrl** | **String**| URL for your callback handler | 
 **eventType** | **String**| Type of event the subscription is for. Visit the \\\&quot;Event Types\\\&quot; section of the webhooks page to find a list of supported event types. | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: */*

