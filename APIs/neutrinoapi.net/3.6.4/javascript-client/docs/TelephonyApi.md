# NeutrinoApi.TelephonyApi

All URIs are relative to *https://neutrinoapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hLRLookup**](TelephonyApi.md#hLRLookup) | **GET** /hlr-lookup | HLR Lookup
[**phonePlayback**](TelephonyApi.md#phonePlayback) | **POST** /phone-playback | Phone Playback
[**phoneVerify**](TelephonyApi.md#phoneVerify) | **POST** /phone-verify | Phone Verify
[**sMSVerify**](TelephonyApi.md#sMSVerify) | **POST** /sms-verify | SMS Verify
[**verifySecurityCode**](TelephonyApi.md#verifySecurityCode) | **GET** /verify-security-code | Verify Security Code



## hLRLookup

> HLRLookupResponse hLRLookup(number, opts)

HLR Lookup

Connect to the global mobile cellular network and retrieve the status of a mobile device

### Example

```javascript
import NeutrinoApi from 'neutrino_api';
let defaultClient = NeutrinoApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: user-id
let user-id = defaultClient.authentications['user-id'];
user-id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user-id.apiKeyPrefix = 'Token';

let apiInstance = new NeutrinoApi.TelephonyApi();
let number = "number_example"; // String | A phone number
let opts = {
  'countryCode': "countryCode_example" // String | ISO 2-letter country code, assume numbers are based in this country. <br>If not set numbers are assumed to be in international format (with or without the leading + sign)
};
apiInstance.hLRLookup(number, opts, (error, data, response) => {
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
 **number** | **String**| A phone number | 
 **countryCode** | **String**| ISO 2-letter country code, assume numbers are based in this country. &lt;br&gt;If not set numbers are assumed to be in international format (with or without the leading + sign) | [optional] 

### Return type

[**HLRLookupResponse**](HLRLookupResponse.md)

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## phonePlayback

> PhonePlaybackResponse phonePlayback(audioUrl, number, opts)

Phone Playback

Make an automated call to any valid phone number and playback an audio message

### Example

```javascript
import NeutrinoApi from 'neutrino_api';
let defaultClient = NeutrinoApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: user-id
let user-id = defaultClient.authentications['user-id'];
user-id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user-id.apiKeyPrefix = 'Token';

let apiInstance = new NeutrinoApi.TelephonyApi();
let audioUrl = "audioUrl_example"; // String | A URL to a valid audio file. Accepted audio formats are: <ul> <li>MP3</li> <li>WAV</li> <li>OGG</li> </ul>You can use the following MP3 URL for testing: <br>https://www.neutrinoapi.com/test-files/test1.mp3
let number = "number_example"; // String | The phone number to call. Must be in valid international format
let opts = {
  'limit': 3, // Number | Limit the total number of calls allowed to the supplied phone number, if the limit is reached within the TTL then error code 14 will be returned
  'limitTtl': 1 // Number | Set the TTL in number of days that the 'limit' option will remember a phone number (the default is 1 day and the maximum is 365 days)
};
apiInstance.phonePlayback(audioUrl, number, opts, (error, data, response) => {
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
 **audioUrl** | **String**| A URL to a valid audio file. Accepted audio formats are: &lt;ul&gt; &lt;li&gt;MP3&lt;/li&gt; &lt;li&gt;WAV&lt;/li&gt; &lt;li&gt;OGG&lt;/li&gt; &lt;/ul&gt;You can use the following MP3 URL for testing: &lt;br&gt;https://www.neutrinoapi.com/test-files/test1.mp3 | 
 **number** | **String**| The phone number to call. Must be in valid international format | 
 **limit** | **Number**| Limit the total number of calls allowed to the supplied phone number, if the limit is reached within the TTL then error code 14 will be returned | [optional] [default to 3]
 **limitTtl** | **Number**| Set the TTL in number of days that the &#39;limit&#39; option will remember a phone number (the default is 1 day and the maximum is 365 days) | [optional] [default to 1]

### Return type

[**PhonePlaybackResponse**](PhonePlaybackResponse.md)

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## phoneVerify

> PhoneVerifyResponse phoneVerify(number, opts)

Phone Verify

Make an automated call to any valid phone number and playback a unique security code

### Example

```javascript
import NeutrinoApi from 'neutrino_api';
let defaultClient = NeutrinoApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: user-id
let user-id = defaultClient.authentications['user-id'];
user-id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user-id.apiKeyPrefix = 'Token';

let apiInstance = new NeutrinoApi.TelephonyApi();
let number = "number_example"; // String | The phone number to send the verification code to
let opts = {
  'codeLength': 6, // Number | The number of digits to use in the security code (between 4 and 12)
  'countryCode': "countryCode_example", // String | ISO 2-letter country code, assume numbers are based in this country. <br>If not set numbers are assumed to be in international format (with or without the leading + sign)
  'languageCode': "'en'", // String | The language to playback the verification code in, available languages are: <ul> <li>de - German</li> <li>en - English</li> <li>es - Spanish</li> <li>fr - French</li> <li>it - Italian</li> <li>pt - Portuguese</li> <li>ru - Russian</li> </ul>
  'limit': 3, // Number | Limit the total number of calls allowed to the supplied phone number, if the limit is reached within the TTL then error code 14 will be returned
  'limitTtl': 1, // Number | Set the TTL in number of days that the 'limit' option will remember a phone number (the default is 1 day and the maximum is 365 days)
  'playbackDelay': 800, // Number | The delay in milliseconds between the playback of each security code
  'securityCode': 56 // Number | Pass in your own security code. This is useful if you have implemented TOTP or similar 2FA methods. If not set then we will generate a secure random code
};
apiInstance.phoneVerify(number, opts, (error, data, response) => {
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
 **number** | **String**| The phone number to send the verification code to | 
 **codeLength** | **Number**| The number of digits to use in the security code (between 4 and 12) | [optional] [default to 6]
 **countryCode** | **String**| ISO 2-letter country code, assume numbers are based in this country. &lt;br&gt;If not set numbers are assumed to be in international format (with or without the leading + sign) | [optional] 
 **languageCode** | **String**| The language to playback the verification code in, available languages are: &lt;ul&gt; &lt;li&gt;de - German&lt;/li&gt; &lt;li&gt;en - English&lt;/li&gt; &lt;li&gt;es - Spanish&lt;/li&gt; &lt;li&gt;fr - French&lt;/li&gt; &lt;li&gt;it - Italian&lt;/li&gt; &lt;li&gt;pt - Portuguese&lt;/li&gt; &lt;li&gt;ru - Russian&lt;/li&gt; &lt;/ul&gt; | [optional] [default to &#39;en&#39;]
 **limit** | **Number**| Limit the total number of calls allowed to the supplied phone number, if the limit is reached within the TTL then error code 14 will be returned | [optional] [default to 3]
 **limitTtl** | **Number**| Set the TTL in number of days that the &#39;limit&#39; option will remember a phone number (the default is 1 day and the maximum is 365 days) | [optional] [default to 1]
 **playbackDelay** | **Number**| The delay in milliseconds between the playback of each security code | [optional] [default to 800]
 **securityCode** | **Number**| Pass in your own security code. This is useful if you have implemented TOTP or similar 2FA methods. If not set then we will generate a secure random code | [optional] 

### Return type

[**PhoneVerifyResponse**](PhoneVerifyResponse.md)

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## sMSVerify

> SMSVerifyResponse sMSVerify(number, opts)

SMS Verify

Send a unique security code to any mobile device via SMS

### Example

```javascript
import NeutrinoApi from 'neutrino_api';
let defaultClient = NeutrinoApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: user-id
let user-id = defaultClient.authentications['user-id'];
user-id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user-id.apiKeyPrefix = 'Token';

let apiInstance = new NeutrinoApi.TelephonyApi();
let number = "number_example"; // String | The phone number to send a verification code to
let opts = {
  'codeLength': 5, // Number | The number of digits to use in the security code (must be between 4 and 12)
  'countryCode': "countryCode_example", // String | ISO 2-letter country code, assume numbers are based in this country. <br>If not set numbers are assumed to be in international format (with or without the leading + sign)
  'languageCode': "'en'", // String | The language to send the verification code in, available languages are: <ul> <li>de - German</li> <li>en - English</li> <li>es - Spanish</li> <li>fr - French</li> <li>it - Italian</li> <li>pt - Portuguese</li> <li>ru - Russian</li> </ul>
  'limit': 10, // Number | Limit the total number of SMS allowed to the supplied phone number, if the limit is reached within the TTL then error code 14 will be returned
  'limitTtl': 1, // Number | Set the TTL in number of days that the 'limit' option will remember a phone number (the default is 1 day and the maximum is 365 days)
  'securityCode': 56 // Number | Pass in your own security code. This is useful if you have implemented TOTP or similar 2FA methods. If not set then we will generate a secure random code
};
apiInstance.sMSVerify(number, opts, (error, data, response) => {
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
 **number** | **String**| The phone number to send a verification code to | 
 **codeLength** | **Number**| The number of digits to use in the security code (must be between 4 and 12) | [optional] [default to 5]
 **countryCode** | **String**| ISO 2-letter country code, assume numbers are based in this country. &lt;br&gt;If not set numbers are assumed to be in international format (with or without the leading + sign) | [optional] 
 **languageCode** | **String**| The language to send the verification code in, available languages are: &lt;ul&gt; &lt;li&gt;de - German&lt;/li&gt; &lt;li&gt;en - English&lt;/li&gt; &lt;li&gt;es - Spanish&lt;/li&gt; &lt;li&gt;fr - French&lt;/li&gt; &lt;li&gt;it - Italian&lt;/li&gt; &lt;li&gt;pt - Portuguese&lt;/li&gt; &lt;li&gt;ru - Russian&lt;/li&gt; &lt;/ul&gt; | [optional] [default to &#39;en&#39;]
 **limit** | **Number**| Limit the total number of SMS allowed to the supplied phone number, if the limit is reached within the TTL then error code 14 will be returned | [optional] [default to 10]
 **limitTtl** | **Number**| Set the TTL in number of days that the &#39;limit&#39; option will remember a phone number (the default is 1 day and the maximum is 365 days) | [optional] [default to 1]
 **securityCode** | **Number**| Pass in your own security code. This is useful if you have implemented TOTP or similar 2FA methods. If not set then we will generate a secure random code | [optional] 

### Return type

[**SMSVerifyResponse**](SMSVerifyResponse.md)

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## verifySecurityCode

> VerifySecurityCodeResponse verifySecurityCode(securityCode, opts)

Verify Security Code

Check if a security code sent via SMS Verify or Phone Verify is valid

### Example

```javascript
import NeutrinoApi from 'neutrino_api';
let defaultClient = NeutrinoApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: user-id
let user-id = defaultClient.authentications['user-id'];
user-id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user-id.apiKeyPrefix = 'Token';

let apiInstance = new NeutrinoApi.TelephonyApi();
let securityCode = "securityCode_example"; // String | The security code to verify
let opts = {
  'limitBy': "limitBy_example" // String | If set then enable additional brute-force protection by limiting the number of attempts by the supplied value. This can be set to any unique identifier you would like to limit by, for example a hash of the users email, phone number or IP address. Requests to this API will be ignored after approximately 10 failed verification attempts
};
apiInstance.verifySecurityCode(securityCode, opts, (error, data, response) => {
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
 **securityCode** | **String**| The security code to verify | 
 **limitBy** | **String**| If set then enable additional brute-force protection by limiting the number of attempts by the supplied value. This can be set to any unique identifier you would like to limit by, for example a hash of the users email, phone number or IP address. Requests to this API will be ignored after approximately 10 failed verification attempts | [optional] 

### Return type

[**VerifySecurityCodeResponse**](VerifySecurityCodeResponse.md)

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

