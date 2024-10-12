# LinQr.SingleQRCodeApi

All URIs are relative to *https://run.byvalue.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dispatcherQrcodeContactPost**](SingleQRCodeApi.md#dispatcherQrcodeContactPost) | **POST** /qrcode/contact | Contact QR Code
[**dispatcherQrcodeCryptoPost**](SingleQRCodeApi.md#dispatcherQrcodeCryptoPost) | **POST** /qrcode/crypto | Cryptocurrency payment QR Code
[**dispatcherQrcodeEmailPost**](SingleQRCodeApi.md#dispatcherQrcodeEmailPost) | **POST** /qrcode/email | Email QR Code
[**dispatcherQrcodeGeoPost**](SingleQRCodeApi.md#dispatcherQrcodeGeoPost) | **POST** /qrcode/geo | Geolocation QR Code
[**dispatcherQrcodePhonePost**](SingleQRCodeApi.md#dispatcherQrcodePhonePost) | **POST** /qrcode/phone | Telephone QR Code
[**dispatcherQrcodePost**](SingleQRCodeApi.md#dispatcherQrcodePost) | **POST** /qrcode | Arbitrary data type QR Code
[**dispatcherQrcodeSmsPost**](SingleQRCodeApi.md#dispatcherQrcodeSmsPost) | **POST** /qrcode/sms | SMS QR Code
[**dispatcherQrcodeTextPost**](SingleQRCodeApi.md#dispatcherQrcodeTextPost) | **POST** /qrcode/text | Text QR Code
[**dispatcherQrcodeWifiPost**](SingleQRCodeApi.md#dispatcherQrcodeWifiPost) | **POST** /qrcode/wifi | WiFi QR Code



## dispatcherQrcodeContactPost

> File dispatcherQrcodeContactPost(opts)

Contact QR Code

This endpoint allows you to create a QR Code that allows user to quickly add contact information to the phone book. The code contains an appropriately encoded electronic business card. After scanning, the device prompts to save the contact in the phone book.

### Example

```javascript
import LinQr from 'lin_qr';
let defaultClient = LinQr.ApiClient.instance;
// Configure API key authorization: Byvalue
let Byvalue = defaultClient.authentications['Byvalue'];
Byvalue.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Byvalue.apiKeyPrefix = 'Token';
// Configure API key authorization: RapidAPI
let RapidAPI = defaultClient.authentications['RapidAPI'];
RapidAPI.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//RapidAPI.apiKeyPrefix = 'Token';

let apiInstance = new LinQr.SingleQRCodeApi();
let opts = {
  'contactQRCode': new LinQr.ContactQRCode() // ContactQRCode | 
};
apiInstance.dispatcherQrcodeContactPost(opts, (error, data, response) => {
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
 **contactQRCode** | [**ContactQRCode**](ContactQRCode.md)|  | [optional] 

### Return type

**File**

### Authorization

[Byvalue](../README.md#Byvalue), [RapidAPI](../README.md#RapidAPI)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/pdf, application/postscript, image/jpeg, image/png, image/svg+xml, image/webp, application/json, text/plain


## dispatcherQrcodeCryptoPost

> File dispatcherQrcodeCryptoPost(opts)

Cryptocurrency payment QR Code

This endpoint allows you to create a QR Code that allows user to make a quick cryptocurrency transfer. The code contains appropriately encoded data for the payment. After scanning the code, the cryptocurrency wallet application asks user to perform the transfer without rewriting all necessary data.

### Example

```javascript
import LinQr from 'lin_qr';
let defaultClient = LinQr.ApiClient.instance;
// Configure API key authorization: Byvalue
let Byvalue = defaultClient.authentications['Byvalue'];
Byvalue.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Byvalue.apiKeyPrefix = 'Token';
// Configure API key authorization: RapidAPI
let RapidAPI = defaultClient.authentications['RapidAPI'];
RapidAPI.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//RapidAPI.apiKeyPrefix = 'Token';

let apiInstance = new LinQr.SingleQRCodeApi();
let opts = {
  'cryptoPaymentQRCode': new LinQr.CryptoPaymentQRCode() // CryptoPaymentQRCode | 
};
apiInstance.dispatcherQrcodeCryptoPost(opts, (error, data, response) => {
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
 **cryptoPaymentQRCode** | [**CryptoPaymentQRCode**](CryptoPaymentQRCode.md)|  | [optional] 

### Return type

**File**

### Authorization

[Byvalue](../README.md#Byvalue), [RapidAPI](../README.md#RapidAPI)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/pdf, application/postscript, image/jpeg, image/png, image/svg+xml, image/webp, application/json, text/plain


## dispatcherQrcodeEmailPost

> File dispatcherQrcodeEmailPost(opts)

Email QR Code

This endpoint allows the creation of a QR Code allowing the user to quickly send an email. The code contains an appropriately encoded message template. After scanning, the device starts the e-mail client with pre-filled specified fields.

### Example

```javascript
import LinQr from 'lin_qr';
let defaultClient = LinQr.ApiClient.instance;
// Configure API key authorization: Byvalue
let Byvalue = defaultClient.authentications['Byvalue'];
Byvalue.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Byvalue.apiKeyPrefix = 'Token';
// Configure API key authorization: RapidAPI
let RapidAPI = defaultClient.authentications['RapidAPI'];
RapidAPI.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//RapidAPI.apiKeyPrefix = 'Token';

let apiInstance = new LinQr.SingleQRCodeApi();
let opts = {
  'emailQRCode': new LinQr.EmailQRCode() // EmailQRCode | 
};
apiInstance.dispatcherQrcodeEmailPost(opts, (error, data, response) => {
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
 **emailQRCode** | [**EmailQRCode**](EmailQRCode.md)|  | [optional] 

### Return type

**File**

### Authorization

[Byvalue](../README.md#Byvalue), [RapidAPI](../README.md#RapidAPI)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/pdf, application/postscript, image/jpeg, image/png, image/svg+xml, image/webp, application/json, text/plain


## dispatcherQrcodeGeoPost

> File dispatcherQrcodeGeoPost(opts)

Geolocation QR Code

This endpoint allows you to create a QR Code that allows to share location with the user. The code contains appropriately encoded geographic coordinates. After scanning the code, device maps application is invoked, pointing to the selected location (address).

### Example

```javascript
import LinQr from 'lin_qr';
let defaultClient = LinQr.ApiClient.instance;
// Configure API key authorization: Byvalue
let Byvalue = defaultClient.authentications['Byvalue'];
Byvalue.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Byvalue.apiKeyPrefix = 'Token';
// Configure API key authorization: RapidAPI
let RapidAPI = defaultClient.authentications['RapidAPI'];
RapidAPI.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//RapidAPI.apiKeyPrefix = 'Token';

let apiInstance = new LinQr.SingleQRCodeApi();
let opts = {
  'geolocationQRCode': new LinQr.GeolocationQRCode() // GeolocationQRCode | 
};
apiInstance.dispatcherQrcodeGeoPost(opts, (error, data, response) => {
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
 **geolocationQRCode** | [**GeolocationQRCode**](GeolocationQRCode.md)|  | [optional] 

### Return type

**File**

### Authorization

[Byvalue](../README.md#Byvalue), [RapidAPI](../README.md#RapidAPI)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/pdf, application/postscript, image/jpeg, image/png, image/svg+xml, image/webp, application/json, text/plain


## dispatcherQrcodePhonePost

> File dispatcherQrcodePhonePost(opts)

Telephone QR Code

This endpoint allows you to create a QR Code that allows user to make quick telephone call. The code contains appropriately encoded telephone number. After scanning the code, device dialer is invoked with prefilled phone number. To make a call, the user only needs to press the green phone key.

### Example

```javascript
import LinQr from 'lin_qr';
let defaultClient = LinQr.ApiClient.instance;
// Configure API key authorization: Byvalue
let Byvalue = defaultClient.authentications['Byvalue'];
Byvalue.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Byvalue.apiKeyPrefix = 'Token';
// Configure API key authorization: RapidAPI
let RapidAPI = defaultClient.authentications['RapidAPI'];
RapidAPI.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//RapidAPI.apiKeyPrefix = 'Token';

let apiInstance = new LinQr.SingleQRCodeApi();
let opts = {
  'phoneQRCode': new LinQr.PhoneQRCode() // PhoneQRCode | 
};
apiInstance.dispatcherQrcodePhonePost(opts, (error, data, response) => {
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
 **phoneQRCode** | [**PhoneQRCode**](PhoneQRCode.md)|  | [optional] 

### Return type

**File**

### Authorization

[Byvalue](../README.md#Byvalue), [RapidAPI](../README.md#RapidAPI)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/pdf, application/postscript, image/jpeg, image/png, image/svg+xml, image/webp, application/json, text/plain


## dispatcherQrcodePost

> File dispatcherQrcodePost(opts)

Arbitrary data type QR Code

This endpoint aggregates the functionality of all other endpoints in the group. The data type in the &#x60;data&#x60; field is recognized automatically and the data is encoded in an appropriate way.

### Example

```javascript
import LinQr from 'lin_qr';
let defaultClient = LinQr.ApiClient.instance;
// Configure API key authorization: Byvalue
let Byvalue = defaultClient.authentications['Byvalue'];
Byvalue.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Byvalue.apiKeyPrefix = 'Token';
// Configure API key authorization: RapidAPI
let RapidAPI = defaultClient.authentications['RapidAPI'];
RapidAPI.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//RapidAPI.apiKeyPrefix = 'Token';

let apiInstance = new LinQr.SingleQRCodeApi();
let opts = {
  'autoQRCode': new LinQr.AutoQRCode() // AutoQRCode | 
};
apiInstance.dispatcherQrcodePost(opts, (error, data, response) => {
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
 **autoQRCode** | [**AutoQRCode**](AutoQRCode.md)|  | [optional] 

### Return type

**File**

### Authorization

[Byvalue](../README.md#Byvalue), [RapidAPI](../README.md#RapidAPI)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/pdf, application/postscript, image/jpeg, image/png, image/svg+xml, image/webp, application/json, text/plain


## dispatcherQrcodeSmsPost

> File dispatcherQrcodeSmsPost(opts)

SMS QR Code

This endpoint allows you to create a QR Code that allows user to quickly send SMS. The code contains appropriately encoded recipient number and message template. After scanning the code, device message application is invoked with prefilled phone number and text, ready to be sent. To send a SMS, the user only needs to press *Send* button.

### Example

```javascript
import LinQr from 'lin_qr';
let defaultClient = LinQr.ApiClient.instance;
// Configure API key authorization: Byvalue
let Byvalue = defaultClient.authentications['Byvalue'];
Byvalue.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Byvalue.apiKeyPrefix = 'Token';
// Configure API key authorization: RapidAPI
let RapidAPI = defaultClient.authentications['RapidAPI'];
RapidAPI.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//RapidAPI.apiKeyPrefix = 'Token';

let apiInstance = new LinQr.SingleQRCodeApi();
let opts = {
  'sMSQRCode': new LinQr.SMSQRCode() // SMSQRCode | 
};
apiInstance.dispatcherQrcodeSmsPost(opts, (error, data, response) => {
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
 **sMSQRCode** | [**SMSQRCode**](SMSQRCode.md)|  | [optional] 

### Return type

**File**

### Authorization

[Byvalue](../README.md#Byvalue), [RapidAPI](../README.md#RapidAPI)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/pdf, application/postscript, image/jpeg, image/png, image/svg+xml, image/webp, application/json, text/plain


## dispatcherQrcodeTextPost

> File dispatcherQrcodeTextPost(opts)

Text QR Code

This endpoint allows you to create a QR Code containing any text, in particular, an URL that may redirect the user to the website. After QR code is scanned, website will be displayed to the user.

### Example

```javascript
import LinQr from 'lin_qr';
let defaultClient = LinQr.ApiClient.instance;
// Configure API key authorization: Byvalue
let Byvalue = defaultClient.authentications['Byvalue'];
Byvalue.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Byvalue.apiKeyPrefix = 'Token';
// Configure API key authorization: RapidAPI
let RapidAPI = defaultClient.authentications['RapidAPI'];
RapidAPI.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//RapidAPI.apiKeyPrefix = 'Token';

let apiInstance = new LinQr.SingleQRCodeApi();
let opts = {
  'textQRCode': new LinQr.TextQRCode() // TextQRCode | 
};
apiInstance.dispatcherQrcodeTextPost(opts, (error, data, response) => {
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
 **textQRCode** | [**TextQRCode**](TextQRCode.md)|  | [optional] 

### Return type

**File**

### Authorization

[Byvalue](../README.md#Byvalue), [RapidAPI](../README.md#RapidAPI)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/pdf, application/postscript, image/jpeg, image/png, image/svg+xml, image/webp, application/json, text/plain


## dispatcherQrcodeWifiPost

> File dispatcherQrcodeWifiPost(opts)

WiFi QR Code

This endpoint allows you to create a QR Code that allows user to quickly connect to a WiFi network. The code contains properly encoded network credentials. After scanning, the device can automatically connect to the network without having to enter the password manually.

### Example

```javascript
import LinQr from 'lin_qr';
let defaultClient = LinQr.ApiClient.instance;
// Configure API key authorization: Byvalue
let Byvalue = defaultClient.authentications['Byvalue'];
Byvalue.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Byvalue.apiKeyPrefix = 'Token';
// Configure API key authorization: RapidAPI
let RapidAPI = defaultClient.authentications['RapidAPI'];
RapidAPI.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//RapidAPI.apiKeyPrefix = 'Token';

let apiInstance = new LinQr.SingleQRCodeApi();
let opts = {
  'wiFiQRCode': new LinQr.WiFiQRCode() // WiFiQRCode | 
};
apiInstance.dispatcherQrcodeWifiPost(opts, (error, data, response) => {
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
 **wiFiQRCode** | [**WiFiQRCode**](WiFiQRCode.md)|  | [optional] 

### Return type

**File**

### Authorization

[Byvalue](../README.md#Byvalue), [RapidAPI](../README.md#RapidAPI)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/pdf, application/postscript, image/jpeg, image/png, image/svg+xml, image/webp, application/json, text/plain

