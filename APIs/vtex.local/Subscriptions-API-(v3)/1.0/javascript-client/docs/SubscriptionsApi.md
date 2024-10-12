# SubscriptionsApiV3.SubscriptionsApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiRnsPubSubscriptionsGet**](SubscriptionsApi.md#apiRnsPubSubscriptionsGet) | **GET** /api/rns/pub/subscriptions | List subscriptions
[**apiRnsPubSubscriptionsIdGet**](SubscriptionsApi.md#apiRnsPubSubscriptionsIdGet) | **GET** /api/rns/pub/subscriptions/{id} | Get subscription details
[**apiRnsPubSubscriptionsIdItemsItemIdDelete**](SubscriptionsApi.md#apiRnsPubSubscriptionsIdItemsItemIdDelete) | **DELETE** /api/rns/pub/subscriptions/{id}/items/{itemId} | Remove items from a subscription.
[**apiRnsPubSubscriptionsIdItemsItemIdPatch**](SubscriptionsApi.md#apiRnsPubSubscriptionsIdItemsItemIdPatch) | **PATCH** /api/rns/pub/subscriptions/{id}/items/{itemId} | Edit items on a subscription.
[**apiRnsPubSubscriptionsIdItemsPost**](SubscriptionsApi.md#apiRnsPubSubscriptionsIdItemsPost) | **POST** /api/rns/pub/subscriptions/{id}/items | Add item to subscription
[**apiRnsPubSubscriptionsIdPatch**](SubscriptionsApi.md#apiRnsPubSubscriptionsIdPatch) | **PATCH** /api/rns/pub/subscriptions/{id} | Update subscription
[**apiRnsPubSubscriptionsIdSimulatePost**](SubscriptionsApi.md#apiRnsPubSubscriptionsIdSimulatePost) | **POST** /api/rns/pub/subscriptions/{id}/simulate | Calculate the current prices for a specific subscription
[**apiRnsPubSubscriptionsPost**](SubscriptionsApi.md#apiRnsPubSubscriptionsPost) | **POST** /api/rns/pub/subscriptions | Create subscription
[**apiRnsPubSubscriptionsSimulatePost**](SubscriptionsApi.md#apiRnsPubSubscriptionsSimulatePost) | **POST** /api/rns/pub/subscriptions/simulate | Calculate the current prices for the provided subscription template
[**apiRnsPubSubscriptionsSubscriptionIdConversationMessageGet**](SubscriptionsApi.md#apiRnsPubSubscriptionsSubscriptionIdConversationMessageGet) | **GET** /api/rns/pub/subscriptions/{subscriptionId}/conversation-message | Get conversation messages



## apiRnsPubSubscriptionsGet

> [SubscriptionGroupResponse] apiRnsPubSubscriptionsGet(contentType, accept, opts)

List subscriptions

List subscriptions filtering by some arguments.

### Example

```javascript
import SubscriptionsApiV3 from 'subscriptions_api__v3';
let defaultClient = SubscriptionsApiV3.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new SubscriptionsApiV3.SubscriptionsApi();
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let opts = {
  'customerEmail': "customerEmail_example", // String | Customer that owns the subscription. Defaults to the current logged user.
  'status': "status_example", // String | Current subscription status
  'addressId': "addressId_example", // String | Id from the address used as shipping address
  'paymentId': "paymentId_example", // String | Id from the payment used as payment method
  'planId': "planId_example", // String | Id from the plan that the subscription belongs to
  'nextPurchaseDate': "nextPurchaseDate_example", // String | Date for the next cycle
  'originalOrderId': "originalOrderId_example", // String | Id from the order that generated the subscription
  'page': 1, // Number | Page used for pagination
  'size': 15 // Number | Page size used for pagination
};
apiInstance.apiRnsPubSubscriptionsGet(contentType, accept, opts, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | 
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | 
 **customerEmail** | **String**| Customer that owns the subscription. Defaults to the current logged user. | [optional] 
 **status** | **String**| Current subscription status | [optional] 
 **addressId** | **String**| Id from the address used as shipping address | [optional] 
 **paymentId** | **String**| Id from the payment used as payment method | [optional] 
 **planId** | **String**| Id from the plan that the subscription belongs to | [optional] 
 **nextPurchaseDate** | **String**| Date for the next cycle | [optional] 
 **originalOrderId** | **String**| Id from the order that generated the subscription | [optional] 
 **page** | **Number**| Page used for pagination | [optional] [default to 1]
 **size** | **Number**| Page size used for pagination | [optional] [default to 15]

### Return type

[**[SubscriptionGroupResponse]**](SubscriptionGroupResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiRnsPubSubscriptionsIdGet

> SubscriptionGroupResponse apiRnsPubSubscriptionsIdGet(id, contentType, accept)

Get subscription details

Retrieve a specific subscription by its ID.

### Example

```javascript
import SubscriptionsApiV3 from 'subscriptions_api__v3';
let defaultClient = SubscriptionsApiV3.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new SubscriptionsApiV3.SubscriptionsApi();
let id = "id_example"; // String | ID from the target subscription.
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
apiInstance.apiRnsPubSubscriptionsIdGet(id, contentType, accept, (error, data, response) => {
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
 **id** | **String**| ID from the target subscription. | 
 **contentType** | **String**| Type of the content being sent. | 
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | 

### Return type

[**SubscriptionGroupResponse**](SubscriptionGroupResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiRnsPubSubscriptionsIdItemsItemIdDelete

> apiRnsPubSubscriptionsIdItemsItemIdDelete(id, itemId, contentType, accept)

Remove items from a subscription.

Removes a specific item from a given subscription

### Example

```javascript
import SubscriptionsApiV3 from 'subscriptions_api__v3';
let defaultClient = SubscriptionsApiV3.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new SubscriptionsApiV3.SubscriptionsApi();
let id = "id_example"; // String | Id from the target subscription
let itemId = "itemId_example"; // String | Id from the subscription item that will be removed
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
apiInstance.apiRnsPubSubscriptionsIdItemsItemIdDelete(id, itemId, contentType, accept, (error, data, response) => {
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
 **id** | **String**| Id from the target subscription | 
 **itemId** | **String**| Id from the subscription item that will be removed | 
 **contentType** | **String**| Type of the content being sent. | 
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiRnsPubSubscriptionsIdItemsItemIdPatch

> SubscriptionGroupResponse apiRnsPubSubscriptionsIdItemsItemIdPatch(id, itemId, contentType, accept, opts)

Edit items on a subscription.

Edit a given item on a specific subscription

### Example

```javascript
import SubscriptionsApiV3 from 'subscriptions_api__v3';
let defaultClient = SubscriptionsApiV3.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new SubscriptionsApiV3.SubscriptionsApi();
let id = "id_example"; // String | Id from the target subscription
let itemId = "itemId_example"; // String | Id from the target item
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let opts = {
  'updateItemInput': new SubscriptionsApiV3.UpdateItemInput() // UpdateItemInput | 
};
apiInstance.apiRnsPubSubscriptionsIdItemsItemIdPatch(id, itemId, contentType, accept, opts, (error, data, response) => {
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
 **id** | **String**| Id from the target subscription | 
 **itemId** | **String**| Id from the target item | 
 **contentType** | **String**| Type of the content being sent. | 
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | 
 **updateItemInput** | [**UpdateItemInput**](UpdateItemInput.md)|  | [optional] 

### Return type

[**SubscriptionGroupResponse**](SubscriptionGroupResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## apiRnsPubSubscriptionsIdItemsPost

> SubscriptionGroupResponse apiRnsPubSubscriptionsIdItemsPost(id, contentType, accept, opts)

Add item to subscription

Add a new item to a given subscription.

### Example

```javascript
import SubscriptionsApiV3 from 'subscriptions_api__v3';
let defaultClient = SubscriptionsApiV3.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new SubscriptionsApiV3.SubscriptionsApi();
let id = "id_example"; // String | ID from the target subscription
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let opts = {
  'subscriptionThinItemRequest': new SubscriptionsApiV3.SubscriptionThinItemRequest() // SubscriptionThinItemRequest | 
};
apiInstance.apiRnsPubSubscriptionsIdItemsPost(id, contentType, accept, opts, (error, data, response) => {
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
 **id** | **String**| ID from the target subscription | 
 **contentType** | **String**| Type of the content being sent. | 
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | 
 **subscriptionThinItemRequest** | [**SubscriptionThinItemRequest**](SubscriptionThinItemRequest.md)|  | [optional] 

### Return type

[**SubscriptionGroupResponse**](SubscriptionGroupResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## apiRnsPubSubscriptionsIdPatch

> SubscriptionGroupResponse apiRnsPubSubscriptionsIdPatch(id, contentType, accept, opts)

Update subscription

Update a specific subscription.

### Example

```javascript
import SubscriptionsApiV3 from 'subscriptions_api__v3';
let defaultClient = SubscriptionsApiV3.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new SubscriptionsApiV3.SubscriptionsApi();
let id = "4002961"; // String | ID from the given subscription.
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let opts = {
  'subscriptionUpdateRequestV3': new SubscriptionsApiV3.SubscriptionUpdateRequestV3() // SubscriptionUpdateRequestV3 | 
};
apiInstance.apiRnsPubSubscriptionsIdPatch(id, contentType, accept, opts, (error, data, response) => {
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
 **id** | **String**| ID from the given subscription. | 
 **contentType** | **String**| Type of the content being sent. | 
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | 
 **subscriptionUpdateRequestV3** | [**SubscriptionUpdateRequestV3**](SubscriptionUpdateRequestV3.md)|  | [optional] 

### Return type

[**SubscriptionGroupResponse**](SubscriptionGroupResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## apiRnsPubSubscriptionsIdSimulatePost

> SimulateResponseVO apiRnsPubSubscriptionsIdSimulatePost(id, contentType, accept)

Calculate the current prices for a specific subscription

Simulates an order made by the specific subscription on checkout and retrieves the current price for items and shipping.

### Example

```javascript
import SubscriptionsApiV3 from 'subscriptions_api__v3';
let defaultClient = SubscriptionsApiV3.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new SubscriptionsApiV3.SubscriptionsApi();
let id = "id_example"; // String | Id from the target subscription
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
apiInstance.apiRnsPubSubscriptionsIdSimulatePost(id, contentType, accept, (error, data, response) => {
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
 **id** | **String**| Id from the target subscription | 
 **contentType** | **String**| Type of the content being sent. | 
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | 

### Return type

[**SimulateResponseVO**](SimulateResponseVO.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiRnsPubSubscriptionsPost

> SubscriptionGroupResponse apiRnsPubSubscriptionsPost(contentType, accept, opts)

Create subscription

Create a new subscription.

### Example

```javascript
import SubscriptionsApiV3 from 'subscriptions_api__v3';
let defaultClient = SubscriptionsApiV3.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new SubscriptionsApiV3.SubscriptionsApi();
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let opts = {
  'subscriptionGroupRequest': new SubscriptionsApiV3.SubscriptionGroupRequest() // SubscriptionGroupRequest | 
};
apiInstance.apiRnsPubSubscriptionsPost(contentType, accept, opts, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | 
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | 
 **subscriptionGroupRequest** | [**SubscriptionGroupRequest**](SubscriptionGroupRequest.md)|  | [optional] 

### Return type

[**SubscriptionGroupResponse**](SubscriptionGroupResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## apiRnsPubSubscriptionsSimulatePost

> SimulateResponseVO apiRnsPubSubscriptionsSimulatePost(contentType, accept, opts)

Calculate the current prices for the provided subscription template

Simulates an order made by subscriptions on checkout and retrieves the current price for items and shipping.

### Example

```javascript
import SubscriptionsApiV3 from 'subscriptions_api__v3';
let defaultClient = SubscriptionsApiV3.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new SubscriptionsApiV3.SubscriptionsApi();
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let opts = {
  'subscriptionGroupRequest': new SubscriptionsApiV3.SubscriptionGroupRequest() // SubscriptionGroupRequest | 
};
apiInstance.apiRnsPubSubscriptionsSimulatePost(contentType, accept, opts, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | 
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | 
 **subscriptionGroupRequest** | [**SubscriptionGroupRequest**](SubscriptionGroupRequest.md)|  | [optional] 

### Return type

[**SimulateResponseVO**](SimulateResponseVO.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## apiRnsPubSubscriptionsSubscriptionIdConversationMessageGet

> [ApiRnsPubSubscriptionsSubscriptionIdConversationMessageGet200ResponseInner] apiRnsPubSubscriptionsSubscriptionIdConversationMessageGet(subscriptionId, contentType, accept)

Get conversation messages

Retrieve all conversation messages sent to a customer regarding a given subscription.

### Example

```javascript
import SubscriptionsApiV3 from 'subscriptions_api__v3';
let defaultClient = SubscriptionsApiV3.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new SubscriptionsApiV3.SubscriptionsApi();
let subscriptionId = "'123456789abc'"; // String | ID of the subscription.
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
apiInstance.apiRnsPubSubscriptionsSubscriptionIdConversationMessageGet(subscriptionId, contentType, accept, (error, data, response) => {
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
 **subscriptionId** | **String**| ID of the subscription. | [default to &#39;123456789abc&#39;]
 **contentType** | **String**| Type of the content being sent. | 
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | 

### Return type

[**[ApiRnsPubSubscriptionsSubscriptionIdConversationMessageGet200ResponseInner]**](ApiRnsPubSubscriptionsSubscriptionIdConversationMessageGet200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

