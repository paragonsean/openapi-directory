# Signl4Api.SubscriptionsApi

All URIs are relative to *https://connect.signl4.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscriptionsGet**](SubscriptionsApi.md#subscriptionsGet) | **GET** /subscriptions | Get infos of all available/managed subscriptions.
[**subscriptionsSubscriptionIdChannelPricesGet**](SubscriptionsApi.md#subscriptionsSubscriptionIdChannelPricesGet) | **GET** /subscriptions/{subscriptionId}/channelPrices | Returns the subscription&#39;s channel price information.
[**subscriptionsSubscriptionIdFeaturesGet**](SubscriptionsApi.md#subscriptionsSubscriptionIdFeaturesGet) | **GET** /subscriptions/{subscriptionId}/features | Returns the features of a specified subscription.
[**subscriptionsSubscriptionIdGet**](SubscriptionsApi.md#subscriptionsSubscriptionIdGet) | **GET** /subscriptions/{subscriptionId} | Get infos of a specific subscription.
[**subscriptionsSubscriptionIdProfilePut**](SubscriptionsApi.md#subscriptionsSubscriptionIdProfilePut) | **PUT** /subscriptions/{subscriptionId}/profile | Updates a subscriptions profile.
[**subscriptionsSubscriptionIdUserLicensesGet**](SubscriptionsApi.md#subscriptionsSubscriptionIdUserLicensesGet) | **GET** /subscriptions/{subscriptionId}/userLicenses | Gets a subscription&#39;s user licenses.



## subscriptionsGet

> [SubscriptionInfo] subscriptionsGet()

Get infos of all available/managed subscriptions.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.SubscriptionsApi();
apiInstance.subscriptionsGet((error, data, response) => {
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

[**[SubscriptionInfo]**](SubscriptionInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## subscriptionsSubscriptionIdChannelPricesGet

> ChannelPriceInfo subscriptionsSubscriptionIdChannelPricesGet(subscriptionId)

Returns the subscription&#39;s channel price information.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.SubscriptionsApi();
let subscriptionId = "subscriptionId_example"; // String | Id of the subscription that needs to be retrieved.
apiInstance.subscriptionsSubscriptionIdChannelPricesGet(subscriptionId, (error, data, response) => {
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
 **subscriptionId** | **String**| Id of the subscription that needs to be retrieved. | 

### Return type

[**ChannelPriceInfo**](ChannelPriceInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## subscriptionsSubscriptionIdFeaturesGet

> [SubscriptionFeature] subscriptionsSubscriptionIdFeaturesGet(subscriptionId)

Returns the features of a specified subscription.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.SubscriptionsApi();
let subscriptionId = "subscriptionId_example"; // String | Id of the subscription from which the features need to be retrieved.
apiInstance.subscriptionsSubscriptionIdFeaturesGet(subscriptionId, (error, data, response) => {
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
 **subscriptionId** | **String**| Id of the subscription from which the features need to be retrieved. | 

### Return type

[**[SubscriptionFeature]**](SubscriptionFeature.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## subscriptionsSubscriptionIdGet

> SubscriptionInfo subscriptionsSubscriptionIdGet(subscriptionId)

Get infos of a specific subscription.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.SubscriptionsApi();
let subscriptionId = "subscriptionId_example"; // String | Id of the subscription that's to be retrieved.
apiInstance.subscriptionsSubscriptionIdGet(subscriptionId, (error, data, response) => {
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
 **subscriptionId** | **String**| Id of the subscription that&#39;s to be retrieved. | 

### Return type

[**SubscriptionInfo**](SubscriptionInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## subscriptionsSubscriptionIdProfilePut

> SubscriptionInfo subscriptionsSubscriptionIdProfilePut(subscriptionId, opts)

Updates a subscriptions profile.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.SubscriptionsApi();
let subscriptionId = "subscriptionId_example"; // String | ID of the subscription to be updated
let opts = {
  'subscriptionProfile': new Signl4Api.SubscriptionProfile() // SubscriptionProfile | Profile data to update subscription with
};
apiInstance.subscriptionsSubscriptionIdProfilePut(subscriptionId, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| ID of the subscription to be updated | 
 **subscriptionProfile** | [**SubscriptionProfile**](SubscriptionProfile.md)| Profile data to update subscription with | [optional] 

### Return type

[**SubscriptionInfo**](SubscriptionInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## subscriptionsSubscriptionIdUserLicensesGet

> UserLicenseInfo subscriptionsSubscriptionIdUserLicensesGet(subscriptionId)

Gets a subscription&#39;s user licenses.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.SubscriptionsApi();
let subscriptionId = "subscriptionId_example"; // String | ID of the subscription
apiInstance.subscriptionsSubscriptionIdUserLicensesGet(subscriptionId, (error, data, response) => {
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
 **subscriptionId** | **String**| ID of the subscription | 

### Return type

[**UserLicenseInfo**](UserLicenseInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

