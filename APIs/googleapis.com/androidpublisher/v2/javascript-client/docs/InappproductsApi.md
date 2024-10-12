# GooglePlayDeveloper.InappproductsApi

All URIs are relative to *https://www.googleapis.com/androidpublisher/v2/applications*

Method | HTTP request | Description
------------- | ------------- | -------------
[**androidpublisherInappproductsDelete**](InappproductsApi.md#androidpublisherInappproductsDelete) | **DELETE** /{packageName}/inappproducts/{sku} | 
[**androidpublisherInappproductsGet**](InappproductsApi.md#androidpublisherInappproductsGet) | **GET** /{packageName}/inappproducts/{sku} | 
[**androidpublisherInappproductsInsert**](InappproductsApi.md#androidpublisherInappproductsInsert) | **POST** /{packageName}/inappproducts | 
[**androidpublisherInappproductsList**](InappproductsApi.md#androidpublisherInappproductsList) | **GET** /{packageName}/inappproducts | 
[**androidpublisherInappproductsPatch**](InappproductsApi.md#androidpublisherInappproductsPatch) | **PATCH** /{packageName}/inappproducts/{sku} | 
[**androidpublisherInappproductsUpdate**](InappproductsApi.md#androidpublisherInappproductsUpdate) | **PUT** /{packageName}/inappproducts/{sku} | 



## androidpublisherInappproductsDelete

> androidpublisherInappproductsDelete(packageName, sku, opts)



Delete an in-app product for an app.

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

let apiInstance = new GooglePlayDeveloper.InappproductsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app with the in-app product; for example, \"com.spiffygame\".
let sku = "sku_example"; // String | Unique identifier for the in-app product.
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.androidpublisherInappproductsDelete(packageName, sku, opts, (error, data, response) => {
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
 **packageName** | **String**| Unique identifier for the Android app with the in-app product; for example, \&quot;com.spiffygame\&quot;. | 
 **sku** | **String**| Unique identifier for the in-app product. | 
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


## androidpublisherInappproductsGet

> InAppProduct androidpublisherInappproductsGet(packageName, sku, opts)



Returns information about the in-app product specified.

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

let apiInstance = new GooglePlayDeveloper.InappproductsApi();
let packageName = "packageName_example"; // String | 
let sku = "sku_example"; // String | Unique identifier for the in-app product.
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.androidpublisherInappproductsGet(packageName, sku, opts, (error, data, response) => {
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
 **packageName** | **String**|  | 
 **sku** | **String**| Unique identifier for the in-app product. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

[**InAppProduct**](InAppProduct.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## androidpublisherInappproductsInsert

> InAppProduct androidpublisherInappproductsInsert(packageName, opts)



Creates a new in-app product for an app.

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

let apiInstance = new GooglePlayDeveloper.InappproductsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app; for example, \"com.spiffygame\".
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'autoConvertMissingPrices': true, // Boolean | If true the prices for all regions targeted by the parent app that don't have a price specified for this in-app product will be auto converted to the target currency based on the default price. Defaults to false.
  'inAppProduct': new GooglePlayDeveloper.InAppProduct() // InAppProduct | 
};
apiInstance.androidpublisherInappproductsInsert(packageName, opts, (error, data, response) => {
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
 **packageName** | **String**| Unique identifier for the Android app; for example, \&quot;com.spiffygame\&quot;. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **autoConvertMissingPrices** | **Boolean**| If true the prices for all regions targeted by the parent app that don&#39;t have a price specified for this in-app product will be auto converted to the target currency based on the default price. Defaults to false. | [optional] 
 **inAppProduct** | [**InAppProduct**](InAppProduct.md)|  | [optional] 

### Return type

[**InAppProduct**](InAppProduct.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## androidpublisherInappproductsList

> InappproductsListResponse androidpublisherInappproductsList(packageName, opts)



List all the in-app products for an Android app, both subscriptions and managed in-app products..

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

let apiInstance = new GooglePlayDeveloper.InappproductsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app with in-app products; for example, \"com.spiffygame\".
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'maxResults': 56, // Number | 
  'startIndex': 56, // Number | 
  'token': "token_example" // String | 
};
apiInstance.androidpublisherInappproductsList(packageName, opts, (error, data, response) => {
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
 **packageName** | **String**| Unique identifier for the Android app with in-app products; for example, \&quot;com.spiffygame\&quot;. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **maxResults** | **Number**|  | [optional] 
 **startIndex** | **Number**|  | [optional] 
 **token** | **String**|  | [optional] 

### Return type

[**InappproductsListResponse**](InappproductsListResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## androidpublisherInappproductsPatch

> InAppProduct androidpublisherInappproductsPatch(packageName, sku, opts)



Updates the details of an in-app product. This method supports patch semantics.

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

let apiInstance = new GooglePlayDeveloper.InappproductsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app with the in-app product; for example, \"com.spiffygame\".
let sku = "sku_example"; // String | Unique identifier for the in-app product.
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'autoConvertMissingPrices': true, // Boolean | If true the prices for all regions targeted by the parent app that don't have a price specified for this in-app product will be auto converted to the target currency based on the default price. Defaults to false.
  'inAppProduct': new GooglePlayDeveloper.InAppProduct() // InAppProduct | 
};
apiInstance.androidpublisherInappproductsPatch(packageName, sku, opts, (error, data, response) => {
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
 **packageName** | **String**| Unique identifier for the Android app with the in-app product; for example, \&quot;com.spiffygame\&quot;. | 
 **sku** | **String**| Unique identifier for the in-app product. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **autoConvertMissingPrices** | **Boolean**| If true the prices for all regions targeted by the parent app that don&#39;t have a price specified for this in-app product will be auto converted to the target currency based on the default price. Defaults to false. | [optional] 
 **inAppProduct** | [**InAppProduct**](InAppProduct.md)|  | [optional] 

### Return type

[**InAppProduct**](InAppProduct.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## androidpublisherInappproductsUpdate

> InAppProduct androidpublisherInappproductsUpdate(packageName, sku, opts)



Updates the details of an in-app product.

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

let apiInstance = new GooglePlayDeveloper.InappproductsApi();
let packageName = "packageName_example"; // String | Unique identifier for the Android app with the in-app product; for example, \"com.spiffygame\".
let sku = "sku_example"; // String | Unique identifier for the in-app product.
let opts = {
  'alt': "'json'", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'autoConvertMissingPrices': true, // Boolean | If true the prices for all regions targeted by the parent app that don't have a price specified for this in-app product will be auto converted to the target currency based on the default price. Defaults to false.
  'inAppProduct': new GooglePlayDeveloper.InAppProduct() // InAppProduct | 
};
apiInstance.androidpublisherInappproductsUpdate(packageName, sku, opts, (error, data, response) => {
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
 **packageName** | **String**| Unique identifier for the Android app with the in-app product; for example, \&quot;com.spiffygame\&quot;. | 
 **sku** | **String**| Unique identifier for the in-app product. | 
 **alt** | **String**| Data format for the response. | [optional] [default to &#39;json&#39;]
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **autoConvertMissingPrices** | **Boolean**| If true the prices for all regions targeted by the parent app that don&#39;t have a price specified for this in-app product will be auto converted to the target currency based on the default price. Defaults to false. | [optional] 
 **inAppProduct** | [**InAppProduct**](InAppProduct.md)|  | [optional] 

### Return type

[**InAppProduct**](InAppProduct.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*

