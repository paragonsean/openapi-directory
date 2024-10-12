# RandommerApi.FinanceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiFinanceCountriesGet**](FinanceApi.md#apiFinanceCountriesGet) | **GET** /api/Finance/Countries | Get available countries
[**apiFinanceCryptoAddressGet**](FinanceApi.md#apiFinanceCryptoAddressGet) | **GET** /api/Finance/CryptoAddress | Get crypto address
[**apiFinanceCryptoAddressTypesGet**](FinanceApi.md#apiFinanceCryptoAddressTypesGet) | **GET** /api/Finance/CryptoAddress/Types | Get available crypto types
[**apiFinanceIbanCountryCodeGet**](FinanceApi.md#apiFinanceIbanCountryCodeGet) | **GET** /api/Finance/Iban/{countryCode} | Get IBAN by countryCode
[**apiFinanceVatValidatorPost**](FinanceApi.md#apiFinanceVatValidatorPost) | **POST** /api/Finance/Vat/Validator | 



## apiFinanceCountriesGet

> apiFinanceCountriesGet(opts)

Get available countries

### Example

```javascript
import RandommerApi from 'randommer_api';

let apiInstance = new RandommerApi.FinanceApi();
let opts = {
  'xApiKey': "xApiKey_example" // String | Enter your key
};
apiInstance.apiFinanceCountriesGet(opts, (error, data, response) => {
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


## apiFinanceCryptoAddressGet

> apiFinanceCryptoAddressGet(opts)

Get crypto address

### Example

```javascript
import RandommerApi from 'randommer_api';

let apiInstance = new RandommerApi.FinanceApi();
let opts = {
  'cryptoType': "cryptoType_example", // String | 
  'xApiKey': "xApiKey_example" // String | Enter your key
};
apiInstance.apiFinanceCryptoAddressGet(opts, (error, data, response) => {
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
 **cryptoType** | **String**|  | [optional] 
 **xApiKey** | **String**| Enter your key | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiFinanceCryptoAddressTypesGet

> apiFinanceCryptoAddressTypesGet(opts)

Get available crypto types

### Example

```javascript
import RandommerApi from 'randommer_api';

let apiInstance = new RandommerApi.FinanceApi();
let opts = {
  'xApiKey': "xApiKey_example" // String | Enter your key
};
apiInstance.apiFinanceCryptoAddressTypesGet(opts, (error, data, response) => {
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


## apiFinanceIbanCountryCodeGet

> apiFinanceIbanCountryCodeGet(countryCode, opts)

Get IBAN by countryCode

### Example

```javascript
import RandommerApi from 'randommer_api';

let apiInstance = new RandommerApi.FinanceApi();
let countryCode = "countryCode_example"; // String | 
let opts = {
  'xApiKey': "xApiKey_example" // String | Enter your key
};
apiInstance.apiFinanceIbanCountryCodeGet(countryCode, opts, (error, data, response) => {
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
 **xApiKey** | **String**| Enter your key | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiFinanceVatValidatorPost

> apiFinanceVatValidatorPost(country, vat, opts)



### Example

```javascript
import RandommerApi from 'randommer_api';

let apiInstance = new RandommerApi.FinanceApi();
let country = "country_example"; // String | 
let vat = "vat_example"; // String | 
let opts = {
  'xApiKey': "xApiKey_example" // String | Enter your key
};
apiInstance.apiFinanceVatValidatorPost(country, vat, opts, (error, data, response) => {
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
 **country** | **String**|  | 
 **vat** | **String**|  | 
 **xApiKey** | **String**| Enter your key | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

