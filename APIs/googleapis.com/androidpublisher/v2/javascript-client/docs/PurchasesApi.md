# GooglePlayDeveloper.PurchasesApi

All URIs are relative to *https://www.googleapis.com/androidpublisher/v2/applications*

Method | HTTP request | Description
------------- | ------------- | -------------
[**androidpublisherPurchasesProductsGet**](PurchasesApi.md#androidpublisherPurchasesProductsGet) | **GET** /{packageName}/purchases/products/{productId}/tokens/{token} | 
[**androidpublisherPurchasesSubscriptionsCancel**](PurchasesApi.md#androidpublisherPurchasesSubscriptionsCancel) | **POST** /{packageName}/purchases/subscriptions/{subscriptionId}/tokens/{token}:cancel | 
[**androidpublisherPurchasesSubscriptionsDefer**](PurchasesApi.md#androidpublisherPurchasesSubscriptionsDefer) | **POST** /{packageName}/purchases/subscriptions/{subscriptionId}/tokens/{token}:defer | 
[**androidpublisherPurchasesSubscriptionsGet**](PurchasesApi.md#androidpublisherPurchasesSubscriptionsGet) | **GET** /{packageName}/purchases/subscriptions/{subscriptionId}/tokens/{token} | 
[**androidpublisherPurchasesSubscriptionsRefund**](PurchasesApi.md#androidpublisherPurchasesSubscriptionsRefund) | **POST** /{packageName}/purchases/subscriptions/{subscriptionId}/tokens/{token}:refund | 
[**androidpublisherPurchasesSubscriptionsRevoke**](PurchasesApi.md#androidpublisherPurchasesSubscriptionsRevoke) | **POST** /{packageName}/purchases/subscriptions/{subscriptionId}/tokens/{token}:revoke | 
[**androidpublisherPurchasesVoidedpurchasesList**](PurchasesApi.md#androidpublisherPurchasesVoidedpurchasesList) | **GET** /{packageName}/purchases/voidedpurchases | 



## androidpublisherPurchasesProductsGet

> ProductPurchase androidpublisherPurchasesProductsGet(packageName, productId, token, opts)



Checks the purchase and consumption status of an inapp item.

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
let packageName = "packageName_example"; // String | The package name of the application the inapp product was sold in (for example, 'com.some.thing').
let productId = "productId_example"; // String | The inapp product SKU (for example, 'com.some.thing.inapp1').
let token = "token_example"; // String | The token provided to the user's device when the inapp product was purchased.
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.androidpublisherPurchasesProductsGet(packageName, productId, token, opts, (error, data, response) => {
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
 **packageName** | **String**| The package name of the application the inapp product was sold in (for example, &#39;com.some.thing&#39;). | 
 **productId** | **String**| The inapp product SKU (for example, &#39;com.some.thing.inapp1&#39;). | 
 **token** | **String**| The token provided to the user&#39;s device when the inapp product was purchased. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

[**ProductPurchase**](ProductPurchase.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## androidpublisherPurchasesSubscriptionsCancel

> androidpublisherPurchasesSubscriptionsCancel(packageName, subscriptionId, token, opts)



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
apiInstance.androidpublisherPurchasesSubscriptionsCancel(packageName, subscriptionId, token, opts, (error, data, response) => {
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


## androidpublisherPurchasesSubscriptionsDefer

> SubscriptionPurchasesDeferResponse androidpublisherPurchasesSubscriptionsDefer(packageName, subscriptionId, token, opts)



Defers a user&#39;s subscription purchase until a specified future expiration time.

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
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'subscriptionPurchasesDeferRequest': new GooglePlayDeveloper.SubscriptionPurchasesDeferRequest() // SubscriptionPurchasesDeferRequest | 
};
apiInstance.androidpublisherPurchasesSubscriptionsDefer(packageName, subscriptionId, token, opts, (error, data, response) => {
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
 **subscriptionPurchasesDeferRequest** | [**SubscriptionPurchasesDeferRequest**](SubscriptionPurchasesDeferRequest.md)|  | [optional] 

### Return type

[**SubscriptionPurchasesDeferResponse**](SubscriptionPurchasesDeferResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## androidpublisherPurchasesSubscriptionsGet

> SubscriptionPurchase androidpublisherPurchasesSubscriptionsGet(packageName, subscriptionId, token, opts)



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
apiInstance.androidpublisherPurchasesSubscriptionsGet(packageName, subscriptionId, token, opts, (error, data, response) => {
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


## androidpublisherPurchasesSubscriptionsRefund

> androidpublisherPurchasesSubscriptionsRefund(packageName, subscriptionId, token, opts)



Refunds a user&#39;s subscription purchase, but the subscription remains valid until its expiration time and it will continue to recur.

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
apiInstance.androidpublisherPurchasesSubscriptionsRefund(packageName, subscriptionId, token, opts, (error, data, response) => {
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


## androidpublisherPurchasesSubscriptionsRevoke

> androidpublisherPurchasesSubscriptionsRevoke(packageName, subscriptionId, token, opts)



Refunds and immediately revokes a user&#39;s subscription purchase. Access to the subscription will be terminated immediately and it will stop recurring.

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
apiInstance.androidpublisherPurchasesSubscriptionsRevoke(packageName, subscriptionId, token, opts, (error, data, response) => {
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


## androidpublisherPurchasesVoidedpurchasesList

> VoidedPurchasesListResponse androidpublisherPurchasesVoidedpurchasesList(packageName, opts)



Lists the purchases that were canceled, refunded or charged-back.

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
let packageName = "packageName_example"; // String | The package name of the application for which voided purchases need to be returned (for example, 'com.some.thing').
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'endTime': "endTime_example", // String | The time, in milliseconds since the Epoch, of the newest voided purchase that you want to see in the response. The value of this parameter cannot be greater than the current time and is ignored if a pagination token is set. Default value is current time. Note: This filter is applied on the time at which the record is seen as voided by our systems and not the actual voided time returned in the response.
  'maxResults': 56, // Number | 
  'startIndex': 56, // Number | 
  'startTime': "startTime_example", // String | The time, in milliseconds since the Epoch, of the oldest voided purchase that you want to see in the response. The value of this parameter cannot be older than 30 days and is ignored if a pagination token is set. Default value is current time minus 30 days. Note: This filter is applied on the time at which the record is seen as voided by our systems and not the actual voided time returned in the response.
  'token': "token_example" // String | 
};
apiInstance.androidpublisherPurchasesVoidedpurchasesList(packageName, opts, (error, data, response) => {
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
 **packageName** | **String**| The package name of the application for which voided purchases need to be returned (for example, &#39;com.some.thing&#39;). | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **endTime** | **String**| The time, in milliseconds since the Epoch, of the newest voided purchase that you want to see in the response. The value of this parameter cannot be greater than the current time and is ignored if a pagination token is set. Default value is current time. Note: This filter is applied on the time at which the record is seen as voided by our systems and not the actual voided time returned in the response. | [optional] 
 **maxResults** | **Number**|  | [optional] 
 **startIndex** | **Number**|  | [optional] 
 **startTime** | **String**| The time, in milliseconds since the Epoch, of the oldest voided purchase that you want to see in the response. The value of this parameter cannot be older than 30 days and is ignored if a pagination token is set. Default value is current time minus 30 days. Note: This filter is applied on the time at which the record is seen as voided by our systems and not the actual voided time returned in the response. | [optional] 
 **token** | **String**|  | [optional] 

### Return type

[**VoidedPurchasesListResponse**](VoidedPurchasesListResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

