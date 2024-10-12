# GooglePlayDeveloper.InapppurchasesApi

All URIs are relative to *https://www.googleapis.com/androidpublisher/v1.1/applications*

Method | HTTP request | Description
------------- | ------------- | -------------
[**androidpublisherInapppurchasesGet**](InapppurchasesApi.md#androidpublisherInapppurchasesGet) | **GET** /{packageName}/inapp/{productId}/purchases/{token} | 



## androidpublisherInapppurchasesGet

> InappPurchase androidpublisherInapppurchasesGet(packageName, productId, token, opts)



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

let apiInstance = new GooglePlayDeveloper.InapppurchasesApi();
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
apiInstance.androidpublisherInapppurchasesGet(packageName, productId, token, opts, (error, data, response) => {
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

[**InappPurchase**](InappPurchase.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

