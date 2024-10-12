# AdSenseHostApi.AssociationsessionsApi

All URIs are relative to *https://www.googleapis.com/adsensehost/v4.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adsensehostAssociationsessionsStart**](AssociationsessionsApi.md#adsensehostAssociationsessionsStart) | **GET** /associationsessions/start | 
[**adsensehostAssociationsessionsVerify**](AssociationsessionsApi.md#adsensehostAssociationsessionsVerify) | **GET** /associationsessions/verify | 



## adsensehostAssociationsessionsStart

> AssociationSession adsensehostAssociationsessionsStart(productCode, websiteUrl, opts)



Create an association session for initiating an association with an AdSense user.

### Example

```javascript
import AdSenseHostApi from 'ad_sense_host_api';
let defaultClient = AdSenseHostApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdSenseHostApi.AssociationsessionsApi();
let productCode = ["null"]; // [String] | Products to associate with the user.
let websiteUrl = "websiteUrl_example"; // String | The URL of the user's hosted website.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'callbackUrl': "callbackUrl_example", // String | The URL to redirect the user to once association is completed. It receives a token parameter that can then be used to retrieve the associated account.
  'userLocale': "userLocale_example", // String | The preferred locale of the user.
  'websiteLocale': "websiteLocale_example" // String | The locale of the user's hosted website.
};
apiInstance.adsensehostAssociationsessionsStart(productCode, websiteUrl, opts, (error, data, response) => {
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
 **productCode** | [**[String]**](String.md)| Products to associate with the user. | 
 **websiteUrl** | **String**| The URL of the user&#39;s hosted website. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **callbackUrl** | **String**| The URL to redirect the user to once association is completed. It receives a token parameter that can then be used to retrieve the associated account. | [optional] 
 **userLocale** | **String**| The preferred locale of the user. | [optional] 
 **websiteLocale** | **String**| The locale of the user&#39;s hosted website. | [optional] 

### Return type

[**AssociationSession**](AssociationSession.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## adsensehostAssociationsessionsVerify

> AssociationSession adsensehostAssociationsessionsVerify(token, opts)



Verify an association session after the association callback returns from AdSense signup.

### Example

```javascript
import AdSenseHostApi from 'ad_sense_host_api';
let defaultClient = AdSenseHostApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdSenseHostApi.AssociationsessionsApi();
let token = "token_example"; // String | The token returned to the association callback URL.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.adsensehostAssociationsessionsVerify(token, opts, (error, data, response) => {
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
 **token** | **String**| The token returned to the association callback URL. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

[**AssociationSession**](AssociationSession.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

