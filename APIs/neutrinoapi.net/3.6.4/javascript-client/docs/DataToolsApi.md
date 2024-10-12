# NeutrinoApi.DataToolsApi

All URIs are relative to *https://neutrinoapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**badWordFilter**](DataToolsApi.md#badWordFilter) | **POST** /bad-word-filter | Bad Word Filter
[**emailValidate**](DataToolsApi.md#emailValidate) | **GET** /email-validate | Email Validate
[**phoneValidate**](DataToolsApi.md#phoneValidate) | **GET** /phone-validate | Phone Validate
[**uALookup**](DataToolsApi.md#uALookup) | **GET** /ua-lookup | UA Lookup



## badWordFilter

> BadWordFilterResponse badWordFilter(content, opts)

Bad Word Filter

Detect bad words, swear words and profanity in a given text

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

let apiInstance = new NeutrinoApi.DataToolsApi();
let content = "content_example"; // String | The content to scan. This can be either a URL to load from, a file upload (multipart/form-data) or an HTML content string
let opts = {
  'catalog': "'strict'", // String | Which catalog of bad words to use, we currently maintain two bad word catalogs: <br> <ul> <li>strict - the largest database of bad words which includes profanity, obscenity, sexual, rude, cuss, dirty, swear and objectionable words and phrases. This catalog is suitable for environments of all ages including educational or children's content</li> <li>obscene - like the strict catalog but does not include any mild profanities, idiomatic phrases or words which are considered formal terminology. This catalog is suitable for adult environments where certain types of bad words are considered OK</li> </ul>
  'censorCharacter': "censorCharacter_example" // String | The character to use to censor out the bad words found
};
apiInstance.badWordFilter(content, opts, (error, data, response) => {
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
 **content** | **String**| The content to scan. This can be either a URL to load from, a file upload (multipart/form-data) or an HTML content string | 
 **catalog** | **String**| Which catalog of bad words to use, we currently maintain two bad word catalogs: &lt;br&gt; &lt;ul&gt; &lt;li&gt;strict - the largest database of bad words which includes profanity, obscenity, sexual, rude, cuss, dirty, swear and objectionable words and phrases. This catalog is suitable for environments of all ages including educational or children&#39;s content&lt;/li&gt; &lt;li&gt;obscene - like the strict catalog but does not include any mild profanities, idiomatic phrases or words which are considered formal terminology. This catalog is suitable for adult environments where certain types of bad words are considered OK&lt;/li&gt; &lt;/ul&gt; | [optional] [default to &#39;strict&#39;]
 **censorCharacter** | **String**| The character to use to censor out the bad words found | [optional] 

### Return type

[**BadWordFilterResponse**](BadWordFilterResponse.md)

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## emailValidate

> EmailValidateResponse emailValidate(email, opts)

Email Validate

Parse, validate and clean an email address

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

let apiInstance = new NeutrinoApi.DataToolsApi();
let email = "email_example"; // String | An email address
let opts = {
  'fixTypos': false // Boolean | Automatically attempt to fix typos in the address
};
apiInstance.emailValidate(email, opts, (error, data, response) => {
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
 **email** | **String**| An email address | 
 **fixTypos** | **Boolean**| Automatically attempt to fix typos in the address | [optional] [default to false]

### Return type

[**EmailValidateResponse**](EmailValidateResponse.md)

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## phoneValidate

> PhoneValidateResponse phoneValidate(number, opts)

Phone Validate

Parse, validate and get location information about a phone number

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

let apiInstance = new NeutrinoApi.DataToolsApi();
let number = "number_example"; // String | A phone number. This can be in international format (E.164) or local format. If passing local format you must also set either the 'country-code' OR 'ip' options as well
let opts = {
  'countryCode': "countryCode_example", // String | ISO 2-letter country code, assume numbers are based in this country. If not set numbers are assumed to be in international format (with or without the leading + sign)
  'ip': "ip_example" // String | Pass in a users IP address and we will assume numbers are based in the country of the IP address
};
apiInstance.phoneValidate(number, opts, (error, data, response) => {
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
 **number** | **String**| A phone number. This can be in international format (E.164) or local format. If passing local format you must also set either the &#39;country-code&#39; OR &#39;ip&#39; options as well | 
 **countryCode** | **String**| ISO 2-letter country code, assume numbers are based in this country. If not set numbers are assumed to be in international format (with or without the leading + sign) | [optional] 
 **ip** | **String**| Pass in a users IP address and we will assume numbers are based in the country of the IP address | [optional] 

### Return type

[**PhoneValidateResponse**](PhoneValidateResponse.md)

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## uALookup

> UALookupResponse uALookup(ua, opts)

UA Lookup

Parse, validate and get detailed user-agent information from a user agent string or from client hints

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

let apiInstance = new NeutrinoApi.DataToolsApi();
let ua = "ua_example"; // String | The user-agent string to lookup. For client hints use the 'UA' header or the JSON data directly from 'navigator.userAgentData.brands' or 'navigator.userAgentData.getHighEntropyValues()'
let opts = {
  'uaVersion': "uaVersion_example", // String | For client hints this corresponds to the 'UA-Full-Version' header or 'uaFullVersion' from NavigatorUAData
  'uaPlatform': "uaPlatform_example", // String | For client hints this corresponds to the 'UA-Platform' header or 'platform' from NavigatorUAData
  'uaPlatformVersion': "uaPlatformVersion_example", // String | For client hints this corresponds to the 'UA-Platform-Version' header or 'platformVersion' from NavigatorUAData
  'uaMobile': "uaMobile_example", // String | For client hints this corresponds to the 'UA-Mobile' header or 'mobile' from NavigatorUAData
  'deviceModel': "deviceModel_example", // String | For client hints this corresponds to the 'UA-Model' header or 'model' from NavigatorUAData. <br>You can also use this parameter to lookup a device directly by its model name, model code or hardware code, on android you can get the model name from: https://developer.android.com/reference/android/os/Build.html#MODEL
  'deviceBrand': "deviceBrand_example" // String | This parameter is only used in combination with 'device-model' when doing direct device lookups without any user-agent data. Set this to the brand or manufacturer name, this is required for accurate device detection with ambiguous model names. On android you can get the device brand from: https://developer.android.com/reference/android/os/Build#MANUFACTURER
};
apiInstance.uALookup(ua, opts, (error, data, response) => {
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
 **ua** | **String**| The user-agent string to lookup. For client hints use the &#39;UA&#39; header or the JSON data directly from &#39;navigator.userAgentData.brands&#39; or &#39;navigator.userAgentData.getHighEntropyValues()&#39; | 
 **uaVersion** | **String**| For client hints this corresponds to the &#39;UA-Full-Version&#39; header or &#39;uaFullVersion&#39; from NavigatorUAData | [optional] 
 **uaPlatform** | **String**| For client hints this corresponds to the &#39;UA-Platform&#39; header or &#39;platform&#39; from NavigatorUAData | [optional] 
 **uaPlatformVersion** | **String**| For client hints this corresponds to the &#39;UA-Platform-Version&#39; header or &#39;platformVersion&#39; from NavigatorUAData | [optional] 
 **uaMobile** | **String**| For client hints this corresponds to the &#39;UA-Mobile&#39; header or &#39;mobile&#39; from NavigatorUAData | [optional] 
 **deviceModel** | **String**| For client hints this corresponds to the &#39;UA-Model&#39; header or &#39;model&#39; from NavigatorUAData. &lt;br&gt;You can also use this parameter to lookup a device directly by its model name, model code or hardware code, on android you can get the model name from: https://developer.android.com/reference/android/os/Build.html#MODEL | [optional] 
 **deviceBrand** | **String**| This parameter is only used in combination with &#39;device-model&#39; when doing direct device lookups without any user-agent data. Set this to the brand or manufacturer name, this is required for accurate device detection with ambiguous model names. On android you can get the device brand from: https://developer.android.com/reference/android/os/Build#MANUFACTURER | [optional] 

### Return type

[**UALookupResponse**](UALookupResponse.md)

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

