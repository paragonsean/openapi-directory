# GooglePlayDeveloper.PurchasesApi

All URIs are relative to *https://www.googleapis.com/androidpublisher/v1/applications*

Method | HTTP request | Description
------------- | ------------- | -------------
[**androidpublisherPurchasesCancel**](PurchasesApi.md#androidpublisherPurchasesCancel) | **POST** /{packageName}/subscriptions/{subscriptionId}/purchases/{token}/cancel | 
[**androidpublisherPurchasesGet**](PurchasesApi.md#androidpublisherPurchasesGet) | **GET** /{packageName}/subscriptions/{subscriptionId}/purchases/{token} | 



## androidpublisherPurchasesCancel

> androidpublisherPurchasesCancel(packageName, subscriptionId, token, opts)



Cancels a user&#39;s subscription purchase. The subscription remains valid until its expiration time.

### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.PurchasesApi();
let packageName = "packageName_example"; // String | The package name of the application for which this subscription was purchased (for example, 'com.some.thing').
let subscriptionId = "subscriptionId_example"; // String | The purchased subscription ID (for example, 'monthly001').
let token = "token_example"; // String | The token provided to the user's device when the subscription was purchased.
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.androidpublisherPurchasesCancel(packageName, subscriptionId, token, opts, (error, data, response) => {
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
 **packageName** | **String**| The package name of the application for which this subscription was purchased (for example, &#39;com.some.thing&#39;). | 
 **subscriptionId** | **String**| The purchased subscription ID (for example, &#39;monthly001&#39;). | 
 **token** | **String**| The token provided to the user&#39;s device when the subscription was purchased. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

null (empty response body)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## androidpublisherPurchasesGet

> SubscriptionPurchase androidpublisherPurchasesGet(packageName, subscriptionId, token, opts)



Checks whether a user&#39;s subscription purchase is valid and returns its expiry time.

### Example

```javascript
import GooglePlayDeveloper from 'google_play_developer';
let defaultClient = GooglePlayDeveloper.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloper.PurchasesApi();
let packageName = "packageName_example"; // String | The package name of the application for which this subscription was purchased (for example, 'com.some.thing').
let subscriptionId = "subscriptionId_example"; // String | The purchased subscription ID (for example, 'monthly001').
let token = "token_example"; // String | The token provided to the user's device when the subscription was purchased.
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.androidpublisherPurchasesGet(packageName, subscriptionId, token, opts, (error, data, response) => {
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
 **packageName** | **String**| The package name of the application for which this subscription was purchased (for example, &#39;com.some.thing&#39;). | 
 **subscriptionId** | **String**| The purchased subscription ID (for example, &#39;monthly001&#39;). | 
 **token** | **String**| The token provided to the user&#39;s device when the subscription was purchased. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

[**SubscriptionPurchase**](SubscriptionPurchase.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

