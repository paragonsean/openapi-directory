# SubscriptionsApiV2Deprecated.SubscriptionGroupApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**additemsubscriptionGroupId**](SubscriptionGroupApi.md#additemsubscriptionGroupId) | **POST** /subscriptions-group/{groupId}/additem | Add Subscription item by groupId
[**cancelSubscriptionbygroupId**](SubscriptionGroupApi.md#cancelSubscriptionbygroupId) | **PATCH** /subscriptions-group/{groupId}/cancel | Cancel Subscription by groupId
[**getAllsubscriptiongroup**](SubscriptionGroupApi.md#getAllsubscriptiongroup) | **GET** /subscriptions-group | List All subscription groups
[**getConfigsubscriptionsgroup**](SubscriptionGroupApi.md#getConfigsubscriptionsgroup) | **GET** /subscriptions-group/{groupId}/config | List Subscription group&#39;s Configuration
[**getConversationMessagebygroupId**](SubscriptionGroupApi.md#getConversationMessagebygroupId) | **GET** /subscriptions-group/{groupId}/conversation-message | Get Conversation Message by groupId
[**getNextpurchase**](SubscriptionGroupApi.md#getNextpurchase) | **GET** /subscriptions-group/nextPurchase/{dateStr} | Get Next purchase
[**getSimulatebysubscriptionGroup**](SubscriptionGroupApi.md#getSimulatebysubscriptionGroup) | **GET** /subscriptions-group/simulate/{groupId} | Get Simulation by subscription-group
[**getSubscriptionbygroupId**](SubscriptionGroupApi.md#getSubscriptionbygroupId) | **GET** /subscriptions-group/{groupId} | Get Subscription by groupId
[**getaddressesbygroupId**](SubscriptionGroupApi.md#getaddressesbygroupId) | **GET** /subscriptions-group/{groupId}/addresses | Get addresses by groupId
[**getfrequencyoptionsbygroupId**](SubscriptionGroupApi.md#getfrequencyoptionsbygroupId) | **GET** /subscriptions-group/{groupId}/frequency-options | Get frequency options by groupId
[**getpaymentSystembygroupId**](SubscriptionGroupApi.md#getpaymentSystembygroupId) | **GET** /subscriptions-group/{groupId}/payment-systems | Get payment System by groupId
[**getsubscriptiongrouplist**](SubscriptionGroupApi.md#getsubscriptiongrouplist) | **GET** /subscriptions-group/list | Get subscription group list
[**getwillcreatebygroupId**](SubscriptionGroupApi.md#getwillcreatebygroupId) | **GET** /subscriptions-group/{groupId}/will-create | List &#39;Will create&#39; by groupId
[**insertAddressesbygroupId**](SubscriptionGroupApi.md#insertAddressesbygroupId) | **POST** /subscriptions-group/{groupId}/addresses | Insert Addresses by groupId
[**retrysubscriptionbygroupId**](SubscriptionGroupApi.md#retrysubscriptionbygroupId) | **POST** /subscriptions-group/{groupid}/instances/{instanceId}/retry | Retry subscription by groupId
[**updateSubscriptionbygroupId**](SubscriptionGroupApi.md#updateSubscriptionbygroupId) | **PATCH** /subscriptions-group/{groupId} | Update Subscription by groupId



## additemsubscriptionGroupId

> additemsubscriptionGroupId(groupId, accept, contentType, additemsubscriptionGroupIdRequest)

Add Subscription item by groupId

Adds an SKU to a given Subscription, filtering by groupId.

### Example

```javascript
import SubscriptionsApiV2Deprecated from 'subscriptions_api__v2_deprecated';
let defaultClient = SubscriptionsApiV2Deprecated.ApiClient.instance;
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

let apiInstance = new SubscriptionsApiV2Deprecated.SubscriptionGroupApi();
let groupId = "1"; // String | Group ID.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "'application/json'"; // String | Type of the content being sent.
let additemsubscriptionGroupIdRequest = {"endpoint":"string","priceAtSubscriptionDate":0,"quantity":0,"sellingPrice":0,"sku":{"detailUrl":"string","id":"string","imageUrl":"string","name":"string","nameComplete":"string","productName":"string"}}; // AdditemsubscriptionGroupIdRequest | 
apiInstance.additemsubscriptionGroupId(groupId, accept, contentType, additemsubscriptionGroupIdRequest, (error, data, response) => {
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
 **groupId** | **String**| Group ID. | 
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **additemsubscriptionGroupIdRequest** | [**AdditemsubscriptionGroupIdRequest**](AdditemsubscriptionGroupIdRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## cancelSubscriptionbygroupId

> cancelSubscriptionbygroupId(accept, contentType, groupId)

Cancel Subscription by groupId

Cancels Subscription by &#x60;groupId&#x60;

### Example

```javascript
import SubscriptionsApiV2Deprecated from 'subscriptions_api__v2_deprecated';
let defaultClient = SubscriptionsApiV2Deprecated.ApiClient.instance;
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

let apiInstance = new SubscriptionsApiV2Deprecated.SubscriptionGroupApi();
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "'application/json'"; // String | Type of the content being sent.
let groupId = "1"; // String | Group ID.
apiInstance.cancelSubscriptionbygroupId(accept, contentType, groupId, (error, data, response) => {
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
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **groupId** | **String**| Group ID. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAllsubscriptiongroup

> getAllsubscriptiongroup(contentType, accept)

List All subscription groups

Retrieves all subscription groups in your store.

### Example

```javascript
import SubscriptionsApiV2Deprecated from 'subscriptions_api__v2_deprecated';
let defaultClient = SubscriptionsApiV2Deprecated.ApiClient.instance;
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

let apiInstance = new SubscriptionsApiV2Deprecated.SubscriptionGroupApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
apiInstance.getAllsubscriptiongroup(contentType, accept, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getConfigsubscriptionsgroup

> getConfigsubscriptionsgroup(contentType, accept, groupId)

List Subscription group&#39;s Configuration

Retrieves details about a given subscription group&#39;s configuration, filtering by groupId.

### Example

```javascript
import SubscriptionsApiV2Deprecated from 'subscriptions_api__v2_deprecated';
let defaultClient = SubscriptionsApiV2Deprecated.ApiClient.instance;
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

let apiInstance = new SubscriptionsApiV2Deprecated.SubscriptionGroupApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let groupId = "1"; // String | Group ID.
apiInstance.getConfigsubscriptionsgroup(contentType, accept, groupId, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **groupId** | **String**| Group ID. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getConversationMessagebygroupId

> getConversationMessagebygroupId(contentType, accept, groupId)

Get Conversation Message by groupId

Retrieves the conversation of a given Subscription group, filtering by groupId.

### Example

```javascript
import SubscriptionsApiV2Deprecated from 'subscriptions_api__v2_deprecated';
let defaultClient = SubscriptionsApiV2Deprecated.ApiClient.instance;
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

let apiInstance = new SubscriptionsApiV2Deprecated.SubscriptionGroupApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let groupId = "1"; // String | Group ID.
apiInstance.getConversationMessagebygroupId(contentType, accept, groupId, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **groupId** | **String**| Group ID. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNextpurchase

> getNextpurchase(contentType, accept, dateStr)

Get Next purchase

Lists details of a given subscription group&#39;s next purchase, filtering by dateStr.

### Example

```javascript
import SubscriptionsApiV2Deprecated from 'subscriptions_api__v2_deprecated';
let defaultClient = SubscriptionsApiV2Deprecated.ApiClient.instance;
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

let apiInstance = new SubscriptionsApiV2Deprecated.SubscriptionGroupApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let dateStr = "dateStr_example"; // String | Reference date that retrieves all next purchases, starting from the dateStr inserted. Must be in the format of {{yyyyMMdd}}
apiInstance.getNextpurchase(contentType, accept, dateStr, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **dateStr** | **String**| Reference date that retrieves all next purchases, starting from the dateStr inserted. Must be in the format of {{yyyyMMdd}} | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getSimulatebysubscriptionGroup

> getSimulatebysubscriptionGroup(contentType, accept, groupId)

Get Simulation by subscription-group

Retrieves Subscription simulations, filtering by groupId.

### Example

```javascript
import SubscriptionsApiV2Deprecated from 'subscriptions_api__v2_deprecated';
let defaultClient = SubscriptionsApiV2Deprecated.ApiClient.instance;
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

let apiInstance = new SubscriptionsApiV2Deprecated.SubscriptionGroupApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let groupId = "1"; // String | Group ID.
apiInstance.getSimulatebysubscriptionGroup(contentType, accept, groupId, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **groupId** | **String**| Group ID. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getSubscriptionbygroupId

> getSubscriptionbygroupId(contentType, accept, groupId)

Get Subscription by groupId

Lists Subscription details, filtering by &#x60;groupId&#x60;.

### Example

```javascript
import SubscriptionsApiV2Deprecated from 'subscriptions_api__v2_deprecated';
let defaultClient = SubscriptionsApiV2Deprecated.ApiClient.instance;
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

let apiInstance = new SubscriptionsApiV2Deprecated.SubscriptionGroupApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let groupId = "1"; // String | Group ID.
apiInstance.getSubscriptionbygroupId(contentType, accept, groupId, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **groupId** | **String**| Group ID. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getaddressesbygroupId

> getaddressesbygroupId(contentType, accept, groupId)

Get addresses by groupId

Lists addresses linked to a given Subscription group, filtering by groupId.

### Example

```javascript
import SubscriptionsApiV2Deprecated from 'subscriptions_api__v2_deprecated';
let defaultClient = SubscriptionsApiV2Deprecated.ApiClient.instance;
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

let apiInstance = new SubscriptionsApiV2Deprecated.SubscriptionGroupApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let groupId = ""; // String | 
apiInstance.getaddressesbygroupId(contentType, accept, groupId, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **groupId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getfrequencyoptionsbygroupId

> getfrequencyoptionsbygroupId(contentType, accept, groupId)

Get frequency options by groupId

Lists frequency options of a given Subscription group, filtering by groupId.

### Example

```javascript
import SubscriptionsApiV2Deprecated from 'subscriptions_api__v2_deprecated';
let defaultClient = SubscriptionsApiV2Deprecated.ApiClient.instance;
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

let apiInstance = new SubscriptionsApiV2Deprecated.SubscriptionGroupApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let groupId = "1"; // String | Group ID.
apiInstance.getfrequencyoptionsbygroupId(contentType, accept, groupId, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **groupId** | **String**| Group ID. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getpaymentSystembygroupId

> getpaymentSystembygroupId(contentType, accept, groupId)

Get payment System by groupId

Retrieves payment system&#39;s information of a given Subscription group, filtering by groupId.

### Example

```javascript
import SubscriptionsApiV2Deprecated from 'subscriptions_api__v2_deprecated';
let defaultClient = SubscriptionsApiV2Deprecated.ApiClient.instance;
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

let apiInstance = new SubscriptionsApiV2Deprecated.SubscriptionGroupApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let groupId = "1"; // String | Group ID.
apiInstance.getpaymentSystembygroupId(contentType, accept, groupId, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **groupId** | **String**| Group ID. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getsubscriptiongrouplist

> getsubscriptiongrouplist(contentType, accept)

Get subscription group list

Retrieves a list of Subscription groups in your store.

### Example

```javascript
import SubscriptionsApiV2Deprecated from 'subscriptions_api__v2_deprecated';
let defaultClient = SubscriptionsApiV2Deprecated.ApiClient.instance;
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

let apiInstance = new SubscriptionsApiV2Deprecated.SubscriptionGroupApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
apiInstance.getsubscriptiongrouplist(contentType, accept, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getwillcreatebygroupId

> getwillcreatebygroupId(contentType, accept, groupId)

List &#39;Will create&#39; by groupId

Retrieves Subscription groups listed as &#39;will create&#39;, filtering by groupId.

### Example

```javascript
import SubscriptionsApiV2Deprecated from 'subscriptions_api__v2_deprecated';
let defaultClient = SubscriptionsApiV2Deprecated.ApiClient.instance;
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

let apiInstance = new SubscriptionsApiV2Deprecated.SubscriptionGroupApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let groupId = "1"; // String | Group ID.
apiInstance.getwillcreatebygroupId(contentType, accept, groupId, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **groupId** | **String**| Group ID. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## insertAddressesbygroupId

> insertAddressesbygroupId(groupId, accept, contentType, insertAddressesbygroupIdRequest)

Insert Addresses by groupId

Insert address information of a given Subscription group, filtering by groupId.

### Example

```javascript
import SubscriptionsApiV2Deprecated from 'subscriptions_api__v2_deprecated';
let defaultClient = SubscriptionsApiV2Deprecated.ApiClient.instance;
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

let apiInstance = new SubscriptionsApiV2Deprecated.SubscriptionGroupApi();
let groupId = "1"; // String | Group ID.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "'application/json'"; // String | Type of the content being sent.
let insertAddressesbygroupIdRequest = {"additionalComponents":[{"longName":"string","shortName":"string","types":["string"]}],"addressId":"string","addressName":"string","addressType":"string","city":"string","complement":"string","country":"string","formattedAddress":"string","geoCoordinate":[0],"neighborhood":"string","number":"string","postalCode":"string","receiverName":"string","reference":"string","state":"string","street":"string"}; // InsertAddressesbygroupIdRequest | 
apiInstance.insertAddressesbygroupId(groupId, accept, contentType, insertAddressesbygroupIdRequest, (error, data, response) => {
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
 **groupId** | **String**| Group ID. | 
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **insertAddressesbygroupIdRequest** | [**InsertAddressesbygroupIdRequest**](InsertAddressesbygroupIdRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## retrysubscriptionbygroupId

> retrysubscriptionbygroupId(groupid, instanceId, accept, contentType)

Retry subscription by groupId

Permits the retry of a Subscription group, via API, filtering by groupId and instanceId.

### Example

```javascript
import SubscriptionsApiV2Deprecated from 'subscriptions_api__v2_deprecated';
let defaultClient = SubscriptionsApiV2Deprecated.ApiClient.instance;
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

let apiInstance = new SubscriptionsApiV2Deprecated.SubscriptionGroupApi();
let groupid = "1"; // String | Group ID.
let instanceId = "instanceId_example"; // String | Instance ID.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "'application/json'"; // String | Type of the content being sent.
apiInstance.retrysubscriptionbygroupId(groupid, instanceId, accept, contentType, (error, data, response) => {
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
 **groupid** | **String**| Group ID. | 
 **instanceId** | **String**| Instance ID. | 
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateSubscriptionbygroupId

> updateSubscriptionbygroupId(groupId, updateSubscriptionbygroupIdRequest)

Update Subscription by groupId

Updates a Subscription by &#x60;groupId&#x60;.

### Example

```javascript
import SubscriptionsApiV2Deprecated from 'subscriptions_api__v2_deprecated';
let defaultClient = SubscriptionsApiV2Deprecated.ApiClient.instance;
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

let apiInstance = new SubscriptionsApiV2Deprecated.SubscriptionGroupApi();
let groupId = "1"; // String | Group ID.
let updateSubscriptionbygroupIdRequest = {"isSkipped":true,"item":[{"SubscriptionId":"string","createdAt":"2019-06-20T18:27:41.23Z","cycleCount":0,"endpoint":"string","isSkipped":true,"lastUpdate":"2019-06-20T18:27:41.23Z","metadata":[{"name":"string","properties":{"additionalProp1":"string","additionalProp2":"string","additionalProp3":"string"}}],"originalItemIndex":0,"originalOrderId":"string","priceAtSubscriptionDate":0,"quantity":0,"sellingPrice":0,"sku":{"detailUrl":"string","id":"string","imageUrl":"string","name":"string","nameComplete":"string","productName":"string"},"status":"ACTIVE"}],"metadata":[{"name":"string","properties":{"additionalProp1":"string","additionalProp2":"string","additionalProp3":"string"}}],"plan":{"frequency":{"interval":0,"periodicity":"string"},"type":"string","validity":{"begin":"2019-06-20T18:27:41.23Z","end":"2019-06-20T18:27:41.23Z"}},"purchaseSettings":{"currencyCode":"string","paymentMethod":{"paymentAccountId":"string","paymentSystem":"string"},"purchaseDay":"string","salesChannel":"string","selectedSla":"string","seller":"string"},"shippingAddress":{"additionalComponents":[{"longName":"string","shortName":"string","types":["string"]}],"addressId":"string","addressName":"string","addressType":"string","city":"string","complement":"string","country":"string","formattedAddress":"string","geoCoordinate":[0],"neighborhood":"string","number":"string","postalCode":"string","receiverName":"string","reference":"string","state":"string","street":"string"},"status":"string"}; // UpdateSubscriptionbygroupIdRequest | 
apiInstance.updateSubscriptionbygroupId(groupId, updateSubscriptionbygroupIdRequest, (error, data, response) => {
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
 **groupId** | **String**| Group ID. | 
 **updateSubscriptionbygroupIdRequest** | [**UpdateSubscriptionbygroupIdRequest**](UpdateSubscriptionbygroupIdRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

