# NamSorApiV2.SocialApi

All URIs are relative to *https://v2.namsor.com/NamSorAPIv2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**phoneCode**](SocialApi.md#phoneCode) | **GET** /api2/json/phoneCode/{firstName}/{lastName}/{phoneNumber} | [USES 11 UNITS PER NAME] Infer the likely country and phone prefix, given a personal name and formatted / unformatted phone number.
[**phoneCodeBatch**](SocialApi.md#phoneCodeBatch) | **POST** /api2/json/phoneCodeBatch | [USES 11 UNITS PER NAME] Infer the likely country and phone prefix, of up to 100 personal names, detecting automatically the local context given a name and formatted / unformatted phone number.
[**phoneCodeGeo**](SocialApi.md#phoneCodeGeo) | **GET** /api2/json/phoneCodeGeo/{firstName}/{lastName}/{phoneNumber}/{countryIso2} | [USES 11 UNITS PER NAME] Infer the likely phone prefix, given a personal name and formatted / unformatted phone number, with a local context (ISO2 country of residence).
[**phoneCodeGeoBatch**](SocialApi.md#phoneCodeGeoBatch) | **POST** /api2/json/phoneCodeGeoBatch | [USES 11 UNITS PER NAME] Infer the likely country and phone prefix, of up to 100 personal names, with a local context (ISO2 country of residence).
[**phoneCodeGeoFeedbackLoop**](SocialApi.md#phoneCodeGeoFeedbackLoop) | **GET** /api2/json/phoneCodeGeoFeedbackLoop/{firstName}/{lastName}/{phoneNumber}/{phoneNumberE164}/{countryIso2} | [CREDITS 1 UNIT] Feedback loop to better infer the likely phone prefix, given a personal name and formatted / unformatted phone number, with a local context (ISO2 country of residence).



## phoneCode

> FirstLastNamePhoneCodedOut phoneCode(firstName, lastName, phoneNumber)

[USES 11 UNITS PER NAME] Infer the likely country and phone prefix, given a personal name and formatted / unformatted phone number.

### Example

```javascript
import NamSorApiV2 from 'nam_sor_api_v2';
let defaultClient = NamSorApiV2.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new NamSorApiV2.SocialApi();
let firstName = "firstName_example"; // String | 
let lastName = "lastName_example"; // String | 
let phoneNumber = "phoneNumber_example"; // String | 
apiInstance.phoneCode(firstName, lastName, phoneNumber, (error, data, response) => {
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
 **firstName** | **String**|  | 
 **lastName** | **String**|  | 
 **phoneNumber** | **String**|  | 

### Return type

[**FirstLastNamePhoneCodedOut**](FirstLastNamePhoneCodedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## phoneCodeBatch

> BatchFirstLastNamePhoneCodedOut phoneCodeBatch(opts)

[USES 11 UNITS PER NAME] Infer the likely country and phone prefix, of up to 100 personal names, detecting automatically the local context given a name and formatted / unformatted phone number.

### Example

```javascript
import NamSorApiV2 from 'nam_sor_api_v2';
let defaultClient = NamSorApiV2.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new NamSorApiV2.SocialApi();
let opts = {
  'batchFirstLastNamePhoneNumberIn': new NamSorApiV2.BatchFirstLastNamePhoneNumberIn() // BatchFirstLastNamePhoneNumberIn | A list of personal names
};
apiInstance.phoneCodeBatch(opts, (error, data, response) => {
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
 **batchFirstLastNamePhoneNumberIn** | [**BatchFirstLastNamePhoneNumberIn**](BatchFirstLastNamePhoneNumberIn.md)| A list of personal names | [optional] 

### Return type

[**BatchFirstLastNamePhoneCodedOut**](BatchFirstLastNamePhoneCodedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## phoneCodeGeo

> FirstLastNamePhoneCodedOut phoneCodeGeo(firstName, lastName, phoneNumber, countryIso2)

[USES 11 UNITS PER NAME] Infer the likely phone prefix, given a personal name and formatted / unformatted phone number, with a local context (ISO2 country of residence).

### Example

```javascript
import NamSorApiV2 from 'nam_sor_api_v2';
let defaultClient = NamSorApiV2.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new NamSorApiV2.SocialApi();
let firstName = "firstName_example"; // String | 
let lastName = "lastName_example"; // String | 
let phoneNumber = "phoneNumber_example"; // String | 
let countryIso2 = "countryIso2_example"; // String | 
apiInstance.phoneCodeGeo(firstName, lastName, phoneNumber, countryIso2, (error, data, response) => {
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
 **firstName** | **String**|  | 
 **lastName** | **String**|  | 
 **phoneNumber** | **String**|  | 
 **countryIso2** | **String**|  | 

### Return type

[**FirstLastNamePhoneCodedOut**](FirstLastNamePhoneCodedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## phoneCodeGeoBatch

> BatchFirstLastNamePhoneCodedOut phoneCodeGeoBatch(opts)

[USES 11 UNITS PER NAME] Infer the likely country and phone prefix, of up to 100 personal names, with a local context (ISO2 country of residence).

### Example

```javascript
import NamSorApiV2 from 'nam_sor_api_v2';
let defaultClient = NamSorApiV2.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new NamSorApiV2.SocialApi();
let opts = {
  'batchFirstLastNamePhoneNumberGeoIn': new NamSorApiV2.BatchFirstLastNamePhoneNumberGeoIn() // BatchFirstLastNamePhoneNumberGeoIn | A list of personal names
};
apiInstance.phoneCodeGeoBatch(opts, (error, data, response) => {
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
 **batchFirstLastNamePhoneNumberGeoIn** | [**BatchFirstLastNamePhoneNumberGeoIn**](BatchFirstLastNamePhoneNumberGeoIn.md)| A list of personal names | [optional] 

### Return type

[**BatchFirstLastNamePhoneCodedOut**](BatchFirstLastNamePhoneCodedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## phoneCodeGeoFeedbackLoop

> FirstLastNamePhoneCodedOut phoneCodeGeoFeedbackLoop(firstName, lastName, phoneNumber, phoneNumberE164, countryIso2)

[CREDITS 1 UNIT] Feedback loop to better infer the likely phone prefix, given a personal name and formatted / unformatted phone number, with a local context (ISO2 country of residence).

### Example

```javascript
import NamSorApiV2 from 'nam_sor_api_v2';
let defaultClient = NamSorApiV2.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new NamSorApiV2.SocialApi();
let firstName = "firstName_example"; // String | 
let lastName = "lastName_example"; // String | 
let phoneNumber = "phoneNumber_example"; // String | 
let phoneNumberE164 = "phoneNumberE164_example"; // String | 
let countryIso2 = "countryIso2_example"; // String | 
apiInstance.phoneCodeGeoFeedbackLoop(firstName, lastName, phoneNumber, phoneNumberE164, countryIso2, (error, data, response) => {
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
 **firstName** | **String**|  | 
 **lastName** | **String**|  | 
 **phoneNumber** | **String**|  | 
 **phoneNumberE164** | **String**|  | 
 **countryIso2** | **String**|  | 

### Return type

[**FirstLastNamePhoneCodedOut**](FirstLastNamePhoneCodedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

