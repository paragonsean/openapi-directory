# SubscriptionV1Deprecated.MiscellaneousApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addrecurrenceitem**](MiscellaneousApi.md#addrecurrenceitem) | **POST** /subscriptions/{recurrenceId}/items | Add Subscription item
[**getRecurrencebyemail**](MiscellaneousApi.md#getRecurrencebyemail) | **GET** /subscriptions | Get Subscriptions
[**getRecurrencebyrecurrenceId**](MiscellaneousApi.md#getRecurrencebyrecurrenceId) | **GET** /subscriptions/{recurrenceId} | Get Subscription by recurrenceId
[**getpaymentaccounts**](MiscellaneousApi.md#getpaymentaccounts) | **GET** /subscriptions/{recurrenceid}/accounts | Get payment accounts
[**getrecurrenceaddresses**](MiscellaneousApi.md#getrecurrenceaddresses) | **GET** /subscriptions/{recurrenceId}/addresses | Get Subscription addresses
[**getrecurrencesettings**](MiscellaneousApi.md#getrecurrencesettings) | **GET** /subscriptions/settings | Get Subscription settings
[**getselfrecurrence**](MiscellaneousApi.md#getselfrecurrence) | **GET** /subscriptions/me | Get self Subscription
[**reindexrecurrence**](MiscellaneousApi.md#reindexrecurrence) | **PATCH** /subscriptions/{recurrenceId}/reindex | Reindex Subscription
[**updatepartialrecurrence**](MiscellaneousApi.md#updatepartialrecurrence) | **PATCH** /subscriptions/{recurrenceId} | Update partial Subscription
[**updaterecurrence**](MiscellaneousApi.md#updaterecurrence) | **PUT** /subscriptions | Update Subscription
[**updaterecurrencesettings**](MiscellaneousApi.md#updaterecurrencesettings) | **PUT** /subscriptions/settings | Update Subscription settings



## addrecurrenceitem

> addrecurrenceitem(contentType, accept, recurrenceId, addrecurrenceitemRequest)

Add Subscription item

Adds an item to a Subscription (formerly Recurrence).

### Example

```javascript
import SubscriptionV1Deprecated from 'subscription__v1_deprecated';
let defaultClient = SubscriptionV1Deprecated.ApiClient.instance;
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

let apiInstance = new SubscriptionV1Deprecated.MiscellaneousApi();
let contentType = "application/json"; // String | Type of the content being sent
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let recurrenceId = "recurrenceId_example"; // String | 
let addrecurrenceitemRequest = [{"frequency":{"interval":1,"periodicity":"monthly"},"quantity":2,"seller":"1","shippingAddressId":"-1461618656161","sku":"20"}]; // [AddrecurrenceitemRequest] | 
apiInstance.addrecurrenceitem(contentType, accept, recurrenceId, addrecurrenceitemRequest, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent | 
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | 
 **recurrenceId** | **String**|  | 
 **addrecurrenceitemRequest** | [**[AddrecurrenceitemRequest]**](AddrecurrenceitemRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## getRecurrencebyemail

> getRecurrencebyemail(contentType, accept, opts)

Get Subscriptions

Retrieves a given Subscription (formerly recurrence). There are three options of filtering your Subscruptions v1. It&#39;s possible to get a list of all Subscriptions v1, by not adding any query params to your request, and simply executing a call to the url. It is also possible to list the Subscriptions by email, filtering by the email query param. And finnally, it is possible to list recurrences with failures on the last execution cycle, filtering by the cycleStatus query param.

### Example

```javascript
import SubscriptionV1Deprecated from 'subscription__v1_deprecated';
let defaultClient = SubscriptionV1Deprecated.ApiClient.instance;
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

let apiInstance = new SubscriptionV1Deprecated.MiscellaneousApi();
let contentType = "application/json"; // String | Type of the content being sent
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let opts = {
  'email': "{{email}}", // String | If you wish to list tasks by email, insert the desired user's email.
  'cycleStatus': "{{cycleStatus}}" // String | If you wish to list tasks by Subscriptions with failures on the last execution cycle, insert the desired cycleStatus.
};
apiInstance.getRecurrencebyemail(contentType, accept, opts, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent | 
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | 
 **email** | **String**| If you wish to list tasks by email, insert the desired user&#39;s email. | [optional] 
 **cycleStatus** | **String**| If you wish to list tasks by Subscriptions with failures on the last execution cycle, insert the desired cycleStatus. | [optional] 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getRecurrencebyrecurrenceId

> getRecurrencebyrecurrenceId(contentType, accept, recurrenceId)

Get Subscription by recurrenceId

Retrieves a given Subscription (formerly recurrence) by recurrenceId.

### Example

```javascript
import SubscriptionV1Deprecated from 'subscription__v1_deprecated';
let defaultClient = SubscriptionV1Deprecated.ApiClient.instance;
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

let apiInstance = new SubscriptionV1Deprecated.MiscellaneousApi();
let contentType = "application/json"; // String | Type of the content being sent
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let recurrenceId = "recurrenceId_example"; // String | 
apiInstance.getRecurrencebyrecurrenceId(contentType, accept, recurrenceId, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent | 
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | 
 **recurrenceId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getpaymentaccounts

> getpaymentaccounts(recurrenceid, contentType, accept)

Get payment accounts

Lists payment accounts of a given Subscription (formerly Recurrence) by recurrenceId.

### Example

```javascript
import SubscriptionV1Deprecated from 'subscription__v1_deprecated';
let defaultClient = SubscriptionV1Deprecated.ApiClient.instance;
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

let apiInstance = new SubscriptionV1Deprecated.MiscellaneousApi();
let recurrenceid = "recurrenceid_example"; // String | 
let contentType = "application/json"; // String | Type of the content being sent
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
apiInstance.getpaymentaccounts(recurrenceid, contentType, accept, (error, data, response) => {
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
 **recurrenceid** | **String**|  | 
 **contentType** | **String**| Type of the content being sent | 
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getrecurrenceaddresses

> getrecurrenceaddresses(contentType, accept, recurrenceId)

Get Subscription addresses

Retrieves the addresses attached to a given subscription (formerly recurrence) by recurrenceId.

### Example

```javascript
import SubscriptionV1Deprecated from 'subscription__v1_deprecated';
let defaultClient = SubscriptionV1Deprecated.ApiClient.instance;
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

let apiInstance = new SubscriptionV1Deprecated.MiscellaneousApi();
let contentType = "application/json"; // String | Type of the content being sent
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let recurrenceId = "recurrenceId_example"; // String | 
apiInstance.getrecurrenceaddresses(contentType, accept, recurrenceId, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent | 
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | 
 **recurrenceId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getrecurrencesettings

> getrecurrencesettings(contentType, accept)

Get Subscription settings

Retrieves your store&#39;s Subscriptions&#39; (formerly recurrence) settings.

### Example

```javascript
import SubscriptionV1Deprecated from 'subscription__v1_deprecated';
let defaultClient = SubscriptionV1Deprecated.ApiClient.instance;
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

let apiInstance = new SubscriptionV1Deprecated.MiscellaneousApi();
let contentType = "application/json"; // String | Type of the content being sent
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
apiInstance.getrecurrencesettings(contentType, accept, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent | 
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getselfrecurrence

> getselfrecurrence(contentType, accept)

Get self Subscription

Lists details of your self Subscription (formerly Recurrence).

### Example

```javascript
import SubscriptionV1Deprecated from 'subscription__v1_deprecated';
let defaultClient = SubscriptionV1Deprecated.ApiClient.instance;
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

let apiInstance = new SubscriptionV1Deprecated.MiscellaneousApi();
let contentType = "application/json"; // String | Type of the content being sent
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
apiInstance.getselfrecurrence(contentType, accept, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent | 
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## reindexrecurrence

> reindexrecurrence(recurrenceId, contentType, accept, reindexrecurrenceRequest)

Reindex Subscription

Alters the frequency of a given Subscription (formerly Recurrence) by changing period and interval.

### Example

```javascript
import SubscriptionV1Deprecated from 'subscription__v1_deprecated';
let defaultClient = SubscriptionV1Deprecated.ApiClient.instance;
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

let apiInstance = new SubscriptionV1Deprecated.MiscellaneousApi();
let recurrenceId = "recurrenceId_example"; // String | 
let contentType = "application/json"; // String | Type of the content being sent
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let reindexrecurrenceRequest = [{"frequency":{"interval":1,"periodicity":"yearly"}}]; // [ReindexrecurrenceRequest] | 
apiInstance.reindexrecurrence(recurrenceId, contentType, accept, reindexrecurrenceRequest, (error, data, response) => {
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
 **recurrenceId** | **String**|  | 
 **contentType** | **String**| Type of the content being sent | 
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | 
 **reindexrecurrenceRequest** | [**[ReindexrecurrenceRequest]**](ReindexrecurrenceRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updatepartialrecurrence

> updatepartialrecurrence(recurrenceId, contentType, accept, updatepartialrecurrenceRequest)

Update partial Subscription

Updates partial information of a given subscription (formerly Recurrence).

### Example

```javascript
import SubscriptionV1Deprecated from 'subscription__v1_deprecated';
let defaultClient = SubscriptionV1Deprecated.ApiClient.instance;
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

let apiInstance = new SubscriptionV1Deprecated.MiscellaneousApi();
let recurrenceId = "recurrenceId_example"; // String | 
let contentType = "application/json"; // String | Type of the content being sent
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let updatepartialrecurrenceRequest = {"deliveryDay":18,"deliveryWeekday":"Monday","status":"inactive"}; // UpdatepartialrecurrenceRequest | 
apiInstance.updatepartialrecurrence(recurrenceId, contentType, accept, updatepartialrecurrenceRequest, (error, data, response) => {
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
 **recurrenceId** | **String**|  | 
 **contentType** | **String**| Type of the content being sent | 
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | 
 **updatepartialrecurrenceRequest** | [**UpdatepartialrecurrenceRequest**](UpdatepartialrecurrenceRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updaterecurrence

> updaterecurrence(contentType, accept, updaterecurrenceRequest)

Update Subscription

Updates details of a given Subscription (formerly recurrence).

### Example

```javascript
import SubscriptionV1Deprecated from 'subscription__v1_deprecated';
let defaultClient = SubscriptionV1Deprecated.ApiClient.instance;
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

let apiInstance = new SubscriptionV1Deprecated.MiscellaneousApi();
let contentType = "application/json"; // String | Type of the content being sent
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let updaterecurrenceRequest = {"deliveryDay":26,"deliveryWeekday":"Friday","email":"user@vtex.com.br","items":[{"frequency":{"interval":1,"periodicity":"weekly"},"quantity":2,"seller":"1","shippingAddressId":"-1461618656161","sku":"18"}],"paymentAccountId":"87FE21B06C0D42908D31A5B11E6FC043"}; // UpdaterecurrenceRequest | 
apiInstance.updaterecurrence(contentType, accept, updaterecurrenceRequest, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent | 
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | 
 **updaterecurrenceRequest** | [**UpdaterecurrenceRequest**](UpdaterecurrenceRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updaterecurrencesettings

> updaterecurrencesettings(contentType, accept, updaterecurrencesettingsRequest)

Update Subscription settings

Updates the Subscriptions&#39; (formerly Recurrence) settings of your store by salesChannel and defaultSLA.

### Example

```javascript
import SubscriptionV1Deprecated from 'subscription__v1_deprecated';
let defaultClient = SubscriptionV1Deprecated.ApiClient.instance;
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

let apiInstance = new SubscriptionV1Deprecated.MiscellaneousApi();
let contentType = "application/json"; // String | Type of the content being sent
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let updaterecurrencesettingsRequest = {"defaultSLA":"Normal","salesChannel":"1"}; // UpdaterecurrencesettingsRequest | 
apiInstance.updaterecurrencesettings(contentType, accept, updaterecurrencesettingsRequest, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent | 
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | 
 **updaterecurrencesettingsRequest** | [**UpdaterecurrencesettingsRequest**](UpdaterecurrencesettingsRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

