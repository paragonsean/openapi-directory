# Appwrite.AvatarsApi

All URIs are relative to *https://appwrite.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**avatarsGetBrowser**](AvatarsApi.md#avatarsGetBrowser) | **GET** /avatars/browsers/{code} | Get Browser Icon
[**avatarsGetCreditCard**](AvatarsApi.md#avatarsGetCreditCard) | **GET** /avatars/credit-cards/{code} | Get Credit Card Icon
[**avatarsGetFavicon**](AvatarsApi.md#avatarsGetFavicon) | **GET** /avatars/favicon | Get Favicon
[**avatarsGetFlag**](AvatarsApi.md#avatarsGetFlag) | **GET** /avatars/flags/{code} | Get Country Flag
[**avatarsGetImage**](AvatarsApi.md#avatarsGetImage) | **GET** /avatars/image | Get Image from URL
[**avatarsGetInitials**](AvatarsApi.md#avatarsGetInitials) | **GET** /avatars/initials | Get User Initials
[**avatarsGetQR**](AvatarsApi.md#avatarsGetQR) | **GET** /avatars/qr | Get QR Code



## avatarsGetBrowser

> avatarsGetBrowser(code, opts)

Get Browser Icon

You can use this endpoint to show different browser icons to your users. The code argument receives the browser code as it appears in your user /account/sessions endpoint. Use width, height and quality arguments to change the output settings.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.AvatarsApi();
let code = "code_example"; // String | Browser Code.
let opts = {
  'width': 100, // Number | Image width. Pass an integer between 0 to 2000. Defaults to 100.
  'height': 100, // Number | Image height. Pass an integer between 0 to 2000. Defaults to 100.
  'quality': 100 // Number | Image quality. Pass an integer between 0 to 100. Defaults to 100.
};
apiInstance.avatarsGetBrowser(code, opts, (error, data, response) => {
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
 **code** | **String**| Browser Code. | 
 **width** | **Number**| Image width. Pass an integer between 0 to 2000. Defaults to 100. | [optional] [default to 100]
 **height** | **Number**| Image height. Pass an integer between 0 to 2000. Defaults to 100. | [optional] [default to 100]
 **quality** | **Number**| Image quality. Pass an integer between 0 to 100. Defaults to 100. | [optional] [default to 100]

### Return type

null (empty response body)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## avatarsGetCreditCard

> avatarsGetCreditCard(code, opts)

Get Credit Card Icon

The credit card endpoint will return you the icon of the credit card provider you need. Use width, height and quality arguments to change the output settings.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.AvatarsApi();
let code = "code_example"; // String | Credit Card Code. Possible values: amex, argencard, cabal, censosud, diners, discover, elo, hipercard, jcb, mastercard, naranja, targeta-shopping, union-china-pay, visa, mir, maestro.
let opts = {
  'width': 100, // Number | Image width. Pass an integer between 0 to 2000. Defaults to 100.
  'height': 100, // Number | Image height. Pass an integer between 0 to 2000. Defaults to 100.
  'quality': 100 // Number | Image quality. Pass an integer between 0 to 100. Defaults to 100.
};
apiInstance.avatarsGetCreditCard(code, opts, (error, data, response) => {
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
 **code** | **String**| Credit Card Code. Possible values: amex, argencard, cabal, censosud, diners, discover, elo, hipercard, jcb, mastercard, naranja, targeta-shopping, union-china-pay, visa, mir, maestro. | 
 **width** | **Number**| Image width. Pass an integer between 0 to 2000. Defaults to 100. | [optional] [default to 100]
 **height** | **Number**| Image height. Pass an integer between 0 to 2000. Defaults to 100. | [optional] [default to 100]
 **quality** | **Number**| Image quality. Pass an integer between 0 to 100. Defaults to 100. | [optional] [default to 100]

### Return type

null (empty response body)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## avatarsGetFavicon

> avatarsGetFavicon(url)

Get Favicon

Use this endpoint to fetch the favorite icon (AKA favicon) of any remote website URL. 

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.AvatarsApi();
let url = "url_example"; // String | Website URL which you want to fetch the favicon from.
apiInstance.avatarsGetFavicon(url, (error, data, response) => {
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
 **url** | **String**| Website URL which you want to fetch the favicon from. | 

### Return type

null (empty response body)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## avatarsGetFlag

> avatarsGetFlag(code, opts)

Get Country Flag

You can use this endpoint to show different country flags icons to your users. The code argument receives the 2 letter country code. Use width, height and quality arguments to change the output settings.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.AvatarsApi();
let code = "code_example"; // String | Country Code. ISO Alpha-2 country code format.
let opts = {
  'width': 100, // Number | Image width. Pass an integer between 0 to 2000. Defaults to 100.
  'height': 100, // Number | Image height. Pass an integer between 0 to 2000. Defaults to 100.
  'quality': 100 // Number | Image quality. Pass an integer between 0 to 100. Defaults to 100.
};
apiInstance.avatarsGetFlag(code, opts, (error, data, response) => {
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
 **code** | **String**| Country Code. ISO Alpha-2 country code format. | 
 **width** | **Number**| Image width. Pass an integer between 0 to 2000. Defaults to 100. | [optional] [default to 100]
 **height** | **Number**| Image height. Pass an integer between 0 to 2000. Defaults to 100. | [optional] [default to 100]
 **quality** | **Number**| Image quality. Pass an integer between 0 to 100. Defaults to 100. | [optional] [default to 100]

### Return type

null (empty response body)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## avatarsGetImage

> avatarsGetImage(url, opts)

Get Image from URL

Use this endpoint to fetch a remote image URL and crop it to any image size you want. This endpoint is very useful if you need to crop and display remote images in your app or in case you want to make sure a 3rd party image is properly served using a TLS protocol.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.AvatarsApi();
let url = "url_example"; // String | Image URL which you want to crop.
let opts = {
  'width': 400, // Number | Resize preview image width, Pass an integer between 0 to 2000.
  'height': 400 // Number | Resize preview image height, Pass an integer between 0 to 2000.
};
apiInstance.avatarsGetImage(url, opts, (error, data, response) => {
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
 **url** | **String**| Image URL which you want to crop. | 
 **width** | **Number**| Resize preview image width, Pass an integer between 0 to 2000. | [optional] [default to 400]
 **height** | **Number**| Resize preview image height, Pass an integer between 0 to 2000. | [optional] [default to 400]

### Return type

null (empty response body)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## avatarsGetInitials

> avatarsGetInitials(opts)

Get User Initials

Use this endpoint to show your user initials avatar icon on your website or app. By default, this route will try to print your logged-in user name or email initials. You can also overwrite the user name if you pass the &#39;name&#39; parameter. If no name is given and no user is logged, an empty avatar will be returned.  You can use the color and background params to change the avatar colors. By default, a random theme will be selected. The random theme will persist for the user&#39;s initials when reloading the same theme will always return for the same initials.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.AvatarsApi();
let opts = {
  'name': "''", // String | Full Name. When empty, current user name or email will be used. Max length: 128 chars.
  'width': 500, // Number | Image width. Pass an integer between 0 to 2000. Defaults to 100.
  'height': 500, // Number | Image height. Pass an integer between 0 to 2000. Defaults to 100.
  'color': "''", // String | Changes text color. By default a random color will be picked and stay will persistent to the given name.
  'background': "''" // String | Changes background color. By default a random color will be picked and stay will persistent to the given name.
};
apiInstance.avatarsGetInitials(opts, (error, data, response) => {
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
 **name** | **String**| Full Name. When empty, current user name or email will be used. Max length: 128 chars. | [optional] [default to &#39;&#39;]
 **width** | **Number**| Image width. Pass an integer between 0 to 2000. Defaults to 100. | [optional] [default to 500]
 **height** | **Number**| Image height. Pass an integer between 0 to 2000. Defaults to 100. | [optional] [default to 500]
 **color** | **String**| Changes text color. By default a random color will be picked and stay will persistent to the given name. | [optional] [default to &#39;&#39;]
 **background** | **String**| Changes background color. By default a random color will be picked and stay will persistent to the given name. | [optional] [default to &#39;&#39;]

### Return type

null (empty response body)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## avatarsGetQR

> avatarsGetQR(text, opts)

Get QR Code

Converts a given plain text to a QR code image. You can use the query parameters to change the size and style of the resulting image.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.AvatarsApi();
let text = "text_example"; // String | Plain text to be converted to QR code image.
let opts = {
  'size': 400, // Number | QR code size. Pass an integer between 0 to 1000. Defaults to 400.
  'margin': 1, // Number | Margin from edge. Pass an integer between 0 to 10. Defaults to 1.
  'download': false // Boolean | Return resulting image with 'Content-Disposition: attachment ' headers for the browser to start downloading it. Pass 0 for no header, or 1 for otherwise. Default value is set to 0.
};
apiInstance.avatarsGetQR(text, opts, (error, data, response) => {
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
 **text** | **String**| Plain text to be converted to QR code image. | 
 **size** | **Number**| QR code size. Pass an integer between 0 to 1000. Defaults to 400. | [optional] [default to 400]
 **margin** | **Number**| Margin from edge. Pass an integer between 0 to 10. Defaults to 1. | [optional] [default to 1]
 **download** | **Boolean**| Return resulting image with &#39;Content-Disposition: attachment &#39; headers for the browser to start downloading it. Pass 0 for no header, or 1 for otherwise. Default value is set to 0. | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

