# SubscriptionsApiV2Deprecated.SubscriptionsApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelSubscriptionsbySubscriptionId**](SubscriptionsApi.md#cancelSubscriptionsbySubscriptionId) | **PATCH** /subscriptions/{subscriptionId}/cancel | Cancel Subscriptions by SubscriptionId
[**getSubscriptionList**](SubscriptionsApi.md#getSubscriptionList) | **GET** /subscriptions/list | Get Subscription List
[**getfrequencyoptionsbysubscriptionId**](SubscriptionsApi.md#getfrequencyoptionsbysubscriptionId) | **GET** /subscriptions/{subscriptionId}/frequency-options | Get frequency options by subscriptionId
[**getsubscriptionbyId**](SubscriptionsApi.md#getsubscriptionbyId) | **GET** /subscriptions/{subscriptionId} | Retrieve subscription by ID
[**getsubscriptionstocustomer**](SubscriptionsApi.md#getsubscriptionstocustomer) | **GET** /subscriptions | Retrieve customer&#39;s subscriptions
[**insertAddressesforSubscription**](SubscriptionsApi.md#insertAddressesforSubscription) | **POST** /subscriptions/{subscriptionId}/addresses | Insert Addresses for Subscription
[**updateSubscriptionsbySubscriptionId**](SubscriptionsApi.md#updateSubscriptionsbySubscriptionId) | **PATCH** /subscriptions/{subscriptionId} | Update Subscriptions by SubscriptionId



## cancelSubscriptionsbySubscriptionId

> cancelSubscriptionsbySubscriptionId(accept, contentType, subscriptionId)

Cancel Subscriptions by SubscriptionId

Cancels all Subscriptions of a subscription group. This operation does not have a rollback. Once cancelled, it cannot be re-activated

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

let apiInstance = new SubscriptionsApiV2Deprecated.SubscriptionsApi();
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "'application/json'"; // String | Type of the content being sent.
let subscriptionId = "1"; // String | Subscription ID.
apiInstance.cancelSubscriptionsbySubscriptionId(accept, contentType, subscriptionId, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription ID. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getSubscriptionList

> getSubscriptionList(contentType, accept)

Get Subscription List

Retrieves a list of Subscriptions linked to your store.

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

let apiInstance = new SubscriptionsApiV2Deprecated.SubscriptionsApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
apiInstance.getSubscriptionList(contentType, accept, (error, data, response) => {
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


## getfrequencyoptionsbysubscriptionId

> getfrequencyoptionsbysubscriptionId(contentType, accept, subscriptionId)

Get frequency options by subscriptionId

Lists frequency options for the Subscription, filtering by &#x60;subscriptionId&#x60;.

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

let apiInstance = new SubscriptionsApiV2Deprecated.SubscriptionsApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let subscriptionId = "1"; // String | Subscription ID.
apiInstance.getfrequencyoptionsbysubscriptionId(contentType, accept, subscriptionId, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription ID. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getsubscriptionbyId

> getsubscriptionbyId(contentType, accept, subscriptionId)

Retrieve subscription by ID

Lists Subscription&#39;s details, searching by &#x60;subscriptionId&#x60;.

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

let apiInstance = new SubscriptionsApiV2Deprecated.SubscriptionsApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let subscriptionId = "1"; // String | Subscription ID.
apiInstance.getsubscriptionbyId(contentType, accept, subscriptionId, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription ID. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getsubscriptionstocustomer

> getsubscriptionstocustomer(customerId, contentType, accept)

Retrieve customer&#39;s subscriptions

Retrieves details of a given customer&#39;s subscriptions, searching by that customer&#39;s &#x60;customerId&#x60;.

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

let apiInstance = new SubscriptionsApiV2Deprecated.SubscriptionsApi();
let customerId = "user@vtex.com.br"; // String | Customer ID.
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
apiInstance.getsubscriptionstocustomer(customerId, contentType, accept, (error, data, response) => {
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
 **customerId** | **String**| Customer ID. | 
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## insertAddressesforSubscription

> insertAddressesforSubscription(subscriptionId, contentType, accept, insertAddressesforSubscriptionRequest)

Insert Addresses for Subscription

Inserts address&#39;s information to complement the Subscription details.

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

let apiInstance = new SubscriptionsApiV2Deprecated.SubscriptionsApi();
let subscriptionId = "1"; // String | Subscription ID.
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let insertAddressesforSubscriptionRequest = [{"additionalComponents":null,"addressId":"1234567890","addressName":"xt5353818181nhshs","addressType":"residential","city":"Rio de Janeiro","complement":null,"country":"BRA","formattedAddress":null,"geoCoordinate":null,"neighborhood":"Barra da Tijuca","number":"1","postalCode":"22204-004","receiverName":"Fulano","reference":null,"state":"RJ","street":"Avenida do Estado"}]; // [InsertAddressesforSubscriptionRequest] | 
apiInstance.insertAddressesforSubscription(subscriptionId, contentType, accept, insertAddressesforSubscriptionRequest, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription ID. | 
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **insertAddressesforSubscriptionRequest** | [**[InsertAddressesforSubscriptionRequest]**](InsertAddressesforSubscriptionRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateSubscriptionsbySubscriptionId

> updateSubscriptionsbySubscriptionId(subscriptionId, contentType, accept, updateSubscriptionsbySubscriptionIdRequest)

Update Subscriptions by SubscriptionId

Update, add or alter information of a given Subscription, filtering by &#x60;subscriptionId&#x60;.

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

let apiInstance = new SubscriptionsApiV2Deprecated.SubscriptionsApi();
let subscriptionId = "1"; // String | Subscription ID.
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let updateSubscriptionsbySubscriptionIdRequest = {"isSkipped":true,"item":{"endpoint":"string","priceAtSubscriptionDate":0,"quantity":0,"sellingPrice":0,"sku":{"detailUrl":"string","id":"string","imageUrl":"string","name":"string","nameComplete":"string","productName":"string"}},"metadata":[{"name":"string","properties":{"additionalProp1":"string","additionalProp2":"string","additionalProp3":"string"}}],"plan":{"frequency":{"interval":0,"periodicity":"string"},"type":"string","validity":{"begin":"2019-07-04T14:40:30.819Z","end":"2019-07-04T14:40:30.819Z"}},"purchaseSettings":{"currencyCode":"string","paymentMethod":{"paymentAccountId":"string","paymentSystem":"string"},"purchaseDay":"string","salesChannel":"string","selectedSla":"string","seller":"string"},"shippingAddress":{"additionalComponents":[{"longName":"string","shortName":"string","types":["string"]}],"addressId":"string","addressName":"string","addressType":"string","city":"string","complement":"string","country":"string","formattedAddress":"string","geoCoordinate":[0],"neighborhood":"string","number":"string","postalCode":"string","receiverName":"string","reference":"string","state":"string","street":"string"},"status":"string"}; // UpdateSubscriptionsbySubscriptionIdRequest | 
apiInstance.updateSubscriptionsbySubscriptionId(subscriptionId, contentType, accept, updateSubscriptionsbySubscriptionIdRequest, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription ID. | 
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **updateSubscriptionsbySubscriptionIdRequest** | [**UpdateSubscriptionsbySubscriptionIdRequest**](UpdateSubscriptionsbySubscriptionIdRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

