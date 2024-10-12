# FunGeneratorsApi.QRCodeApi

All URIs are relative to *https://api.fungenerators.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**qrcodeBusinessCardGet**](QRCodeApi.md#qrcodeBusinessCardGet) | **GET** /qrcode/business_card | 
[**qrcodeDecodePost**](QRCodeApi.md#qrcodeDecodePost) | **POST** /qrcode/decode | 
[**qrcodeEmailGet**](QRCodeApi.md#qrcodeEmailGet) | **GET** /qrcode/email | 
[**qrcodePhoneGet**](QRCodeApi.md#qrcodePhoneGet) | **GET** /qrcode/phone | 
[**qrcodeRawGet**](QRCodeApi.md#qrcodeRawGet) | **GET** /qrcode/raw | 
[**qrcodeSkypeGet**](QRCodeApi.md#qrcodeSkypeGet) | **GET** /qrcode/skype | 
[**qrcodeSmsGet**](QRCodeApi.md#qrcodeSmsGet) | **GET** /qrcode/sms | 
[**qrcodeTextGet**](QRCodeApi.md#qrcodeTextGet) | **GET** /qrcode/text | 
[**qrcodeUrlGet**](QRCodeApi.md#qrcodeUrlGet) | **GET** /qrcode/url | 



## qrcodeBusinessCardGet

> qrcodeBusinessCardGet(firstname, lastname, email, opts)



Get a QR Code image for a business card aka VCARD

### Example

```javascript
import FunGeneratorsApi from 'fun_generators_api';
let defaultClient = FunGeneratorsApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FunGeneratorsApi.QRCodeApi();
let firstname = "firstname_example"; // String | First Name
let lastname = "lastname_example"; // String | Last Name
let email = "email_example"; // String | Email id
let opts = {
  'middlename': "middlename_example", // String | Middle Name
  'company': "company_example", // String | Company Name
  'phoneWork': "phoneWork_example", // String | Work Phone Number
  'phoneHome': "phoneHome_example", // String | Home Phone Number
  'phoneCell': "phoneCell_example", // String | Cell Phone Number
  'street1': "street1_example", // String | Street Address
  'street2': "street2_example", // String | Street Address 2
  'city': "city_example", // String | City
  'zip': "zip_example", // String | Zip Code
  'state': "state_example", // String | State
  'country': "country_example", // String | Country
  'format': "format_example" // String | Output image format. Must be one of png/eps/raw/svg
};
apiInstance.qrcodeBusinessCardGet(firstname, lastname, email, opts, (error, data, response) => {
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
 **firstname** | **String**| First Name | 
 **lastname** | **String**| Last Name | 
 **email** | **String**| Email id | 
 **middlename** | **String**| Middle Name | [optional] 
 **company** | **String**| Company Name | [optional] 
 **phoneWork** | **String**| Work Phone Number | [optional] 
 **phoneHome** | **String**| Home Phone Number | [optional] 
 **phoneCell** | **String**| Cell Phone Number | [optional] 
 **street1** | **String**| Street Address | [optional] 
 **street2** | **String**| Street Address 2 | [optional] 
 **city** | **String**| City | [optional] 
 **zip** | **String**| Zip Code | [optional] 
 **state** | **String**| State | [optional] 
 **country** | **String**| Country | [optional] 
 **format** | **String**| Output image format. Must be one of png/eps/raw/svg | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## qrcodeDecodePost

> qrcodeDecodePost(qrcodeDecodePostRequest)



Decode a QR Code image and return the cotents if successful

### Example

```javascript
import FunGeneratorsApi from 'fun_generators_api';
let defaultClient = FunGeneratorsApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FunGeneratorsApi.QRCodeApi();
let qrcodeDecodePostRequest = new FunGeneratorsApi.QrcodeDecodePostRequest(); // QrcodeDecodePostRequest | 
apiInstance.qrcodeDecodePost(qrcodeDecodePostRequest, (error, data, response) => {
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
 **qrcodeDecodePostRequest** | [**QrcodeDecodePostRequest**](QrcodeDecodePostRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: mulitpart/form-data, mulitpart/form-data-endcoded, application/x-www-form-urlencoded
- **Accept**: application/json


## qrcodeEmailGet

> qrcodeEmailGet(email, opts)



Get a QR Code image for an email

### Example

```javascript
import FunGeneratorsApi from 'fun_generators_api';
let defaultClient = FunGeneratorsApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FunGeneratorsApi.QRCodeApi();
let email = "email_example"; // String | Email id to send the email to
let opts = {
  'subject': "subject_example", // String | Subject of the email(optional)
  'body': "body_example", // String | Body of the email(optional)
  'format': "format_example" // String | Output image format. Must be one of png/png/eps/raw/svg
};
apiInstance.qrcodeEmailGet(email, opts, (error, data, response) => {
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
 **email** | **String**| Email id to send the email to | 
 **subject** | **String**| Subject of the email(optional) | [optional] 
 **body** | **String**| Body of the email(optional) | [optional] 
 **format** | **String**| Output image format. Must be one of png/png/eps/raw/svg | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## qrcodePhoneGet

> qrcodePhoneGet(number, opts)



Get a QR Code image for a phone number

### Example

```javascript
import FunGeneratorsApi from 'fun_generators_api';
let defaultClient = FunGeneratorsApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FunGeneratorsApi.QRCodeApi();
let number = "number_example"; // String | Phone Number
let opts = {
  'format': "format_example" // String | Output image format. Must be one of png/eps/raw/svg
};
apiInstance.qrcodePhoneGet(number, opts, (error, data, response) => {
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
 **number** | **String**| Phone Number | 
 **format** | **String**| Output image format. Must be one of png/eps/raw/svg | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## qrcodeRawGet

> qrcodeRawGet(rawtext, opts)



Get a QR Code image for a block of raw data

### Example

```javascript
import FunGeneratorsApi from 'fun_generators_api';
let defaultClient = FunGeneratorsApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FunGeneratorsApi.QRCodeApi();
let rawtext = "rawtext_example"; // String | Raw Text value
let opts = {
  'format': "format_example" // String | Output image format. Must be one of png/eps/raw/svg
};
apiInstance.qrcodeRawGet(rawtext, opts, (error, data, response) => {
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
 **rawtext** | **String**| Raw Text value | 
 **format** | **String**| Output image format. Must be one of png/eps/raw/svg | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## qrcodeSkypeGet

> qrcodeSkypeGet(username, opts)



Get a QR Code image for a skype user

### Example

```javascript
import FunGeneratorsApi from 'fun_generators_api';
let defaultClient = FunGeneratorsApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FunGeneratorsApi.QRCodeApi();
let username = "username_example"; // String | Skype User name
let opts = {
  'format': "format_example" // String | Output image format. Must be one of png/eps/raw/svg
};
apiInstance.qrcodeSkypeGet(username, opts, (error, data, response) => {
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
 **username** | **String**| Skype User name | 
 **format** | **String**| Output image format. Must be one of png/eps/raw/svg | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## qrcodeSmsGet

> qrcodeSmsGet(number, opts)



Get a QR Code image for a Phone number for SMS messaging

### Example

```javascript
import FunGeneratorsApi from 'fun_generators_api';
let defaultClient = FunGeneratorsApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FunGeneratorsApi.QRCodeApi();
let number = "number_example"; // String | Phone Number to SMS
let opts = {
  'format': "format_example" // String | Output image format. Must be one of png/eps/raw/svg
};
apiInstance.qrcodeSmsGet(number, opts, (error, data, response) => {
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
 **number** | **String**| Phone Number to SMS | 
 **format** | **String**| Output image format. Must be one of png/eps/raw/svg | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## qrcodeTextGet

> qrcodeTextGet(text, opts)



Get a QR Code image for a block of text

### Example

```javascript
import FunGeneratorsApi from 'fun_generators_api';
let defaultClient = FunGeneratorsApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FunGeneratorsApi.QRCodeApi();
let text = "text_example"; // String | Text value
let opts = {
  'format': "format_example" // String | Output image format. Must be one of png/eps/raw/svg
};
apiInstance.qrcodeTextGet(text, opts, (error, data, response) => {
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
 **text** | **String**| Text value | 
 **format** | **String**| Output image format. Must be one of png/eps/raw/svg | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## qrcodeUrlGet

> qrcodeUrlGet(url, opts)



Get a QR Code image for a url

### Example

```javascript
import FunGeneratorsApi from 'fun_generators_api';
let defaultClient = FunGeneratorsApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FunGeneratorsApi.QRCodeApi();
let url = "url_example"; // String | URL value
let opts = {
  'format': "format_example" // String | Output image format. Must be one of png/raw/eps/svg
};
apiInstance.qrcodeUrlGet(url, opts, (error, data, response) => {
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
 **url** | **String**| URL value | 
 **format** | **String**| Output image format. Must be one of png/raw/eps/svg | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

