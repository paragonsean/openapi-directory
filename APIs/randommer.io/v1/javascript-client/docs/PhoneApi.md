# RandommerApi.PhoneApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiPhoneCountriesGet**](PhoneApi.md#apiPhoneCountriesGet) | **GET** /api/Phone/Countries | Get available countries
[**apiPhoneGenerateGet**](PhoneApi.md#apiPhoneGenerateGet) | **GET** /api/Phone/Generate | Get bulk telephone numbers for a country
[**apiPhoneIMEIGet**](PhoneApi.md#apiPhoneIMEIGet) | **GET** /api/Phone/IMEI | Get bulk imeis
[**apiPhoneValidateGet**](PhoneApi.md#apiPhoneValidateGet) | **GET** /api/Phone/Validate | Validate a phone number



## apiPhoneCountriesGet

> apiPhoneCountriesGet(opts)

Get available countries

### Example

```javascript
import RandommerApi from 'randommer_api';

let apiInstance = new RandommerApi.PhoneApi();
let opts = {
  'xApiKey': "xApiKey_example" // String | Enter your key
};
apiInstance.apiPhoneCountriesGet(opts, (error, data, response) => {
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
 **xApiKey** | **String**| Enter your key | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiPhoneGenerateGet

> apiPhoneGenerateGet(countryCode, quantity, opts)

Get bulk telephone numbers for a country

### Example

```javascript
import RandommerApi from 'randommer_api';

let apiInstance = new RandommerApi.PhoneApi();
let countryCode = "countryCode_example"; // String | 
let quantity = 56; // Number | 
let opts = {
  'xApiKey': "xApiKey_example" // String | Enter your key
};
apiInstance.apiPhoneGenerateGet(countryCode, quantity, opts, (error, data, response) => {
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
 **countryCode** | **String**|  | 
 **quantity** | **Number**|  | 
 **xApiKey** | **String**| Enter your key | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiPhoneIMEIGet

> apiPhoneIMEIGet(quantity, opts)

Get bulk imeis

### Example

```javascript
import RandommerApi from 'randommer_api';

let apiInstance = new RandommerApi.PhoneApi();
let quantity = 56; // Number | 
let opts = {
  'xApiKey': "xApiKey_example" // String | Enter your key
};
apiInstance.apiPhoneIMEIGet(quantity, opts, (error, data, response) => {
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
 **quantity** | **Number**|  | 
 **xApiKey** | **String**| Enter your key | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiPhoneValidateGet

> apiPhoneValidateGet(telephone, opts)

Validate a phone number

### Example

```javascript
import RandommerApi from 'randommer_api';

let apiInstance = new RandommerApi.PhoneApi();
let telephone = "telephone_example"; // String | 
let opts = {
  'countryCode': "countryCode_example", // String | 
  'xApiKey': "xApiKey_example" // String | Enter your key
};
apiInstance.apiPhoneValidateGet(telephone, opts, (error, data, response) => {
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
 **telephone** | **String**|  | 
 **countryCode** | **String**|  | [optional] 
 **xApiKey** | **String**| Enter your key | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

