# KycApiDocumentation.V1VatVerificationApi

All URIs are relative to *https://api.kompany.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vatBasic**](V1VatVerificationApi.md#vatBasic) | **POST** /api/v1/vat-verification/basic-check/{country} | Returns a verification result
[**vatComprehensive**](V1VatVerificationApi.md#vatComprehensive) | **POST** /api/v1/vat-verification/comprehensive-check/{country} | Returns a verification result and company data
[**vatLevelTwo**](V1VatVerificationApi.md#vatLevelTwo) | **POST** /api/v1/vat-verification/leveltwo-check/{country} | Returns a level two verification result
[**vatLookup**](V1VatVerificationApi.md#vatLookup) | **POST** /api/v1/vat-verification/lookup/{country} | Returns a list of vat numbers with additional data



## vatBasic

> VatBasic200Response vatBasic(country, vatNumber, opts)

Returns a verification result

Basic verification of given VAT number against VIES. Optional parameters may help to build a better confidence score.

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1VatVerificationApi();
let country = "country_example"; // String | ISO_3166-1_alpha-2 representation of a country name - 2 chars
let vatNumber = "vatNumber_example"; // String | VAT number to validate
let opts = {
  'companyAddress': "companyAddress_example", // String | company address lines
  'companyName': "companyName_example", // String | Company name
  'companyNumber': "companyNumber_example" // String | official company number
};
apiInstance.vatBasic(country, vatNumber, opts, (error, data, response) => {
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
 **country** | **String**| ISO_3166-1_alpha-2 representation of a country name - 2 chars | 
 **vatNumber** | **String**| VAT number to validate | 
 **companyAddress** | **String**| company address lines | [optional] 
 **companyName** | **String**| Company name | [optional] 
 **companyNumber** | **String**| official company number | [optional] 

### Return type

[**VatBasic200Response**](VatBasic200Response.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## vatComprehensive

> vatComprehensive(country, vatNumber, opts)

Returns a verification result and company data

Extended verification of given VAT number against VIES. Optional parameters may help to build a better confidence score.

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1VatVerificationApi();
let country = "country_example"; // String | ISO_3166-1_alpha-2 representation of a country name - 2 chars
let vatNumber = "vatNumber_example"; // String | VAT number to validate
let opts = {
  'companyAddress': "companyAddress_example", // String | company address lines
  'companyName': "companyName_example", // String | Company name
  'companyNumber': "companyNumber_example" // String | official company number
};
apiInstance.vatComprehensive(country, vatNumber, opts, (error, data, response) => {
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
 **country** | **String**| ISO_3166-1_alpha-2 representation of a country name - 2 chars | 
 **vatNumber** | **String**| VAT number to validate | 
 **companyAddress** | **String**| company address lines | [optional] 
 **companyName** | **String**| Company name | [optional] 
 **companyNumber** | **String**| official company number | [optional] 

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## vatLevelTwo

> VatLevelTwo200Response vatLevelTwo(country, vatNumber, opts)

Returns a level two verification result

Second Level Verification of VAT number against BMF Austria. Optional confirmation parameter can be provided to order a Confirmation Report.

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1VatVerificationApi();
let country = "country_example"; // String | ISO_3166-1_alpha-2 representation of a country name - 2 chars
let vatNumber = "vatNumber_example"; // String | VAT number to validate
let opts = {
  'confirmation': true // Boolean | If a confirmation document should be ordered
};
apiInstance.vatLevelTwo(country, vatNumber, opts, (error, data, response) => {
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
 **country** | **String**| ISO_3166-1_alpha-2 representation of a country name - 2 chars | 
 **vatNumber** | **String**| VAT number to validate | 
 **confirmation** | **Boolean**| If a confirmation document should be ordered | [optional] 

### Return type

[**VatLevelTwo200Response**](VatLevelTwo200Response.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## vatLookup

> VatLookup200Response vatLookup(country, name, opts)

Returns a list of vat numbers with additional data

Reverse VAT Lookup: Search for companies and their VAT numbers by company name. Search is forwarded to a provider.

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1VatVerificationApi();
let country = "country_example"; // String | ISO_3166-1_alpha-2 representation of a country name - 2 chars
let name = "name_example"; // String | Company name
let opts = {
  'address': "address_example" // String | Company address
};
apiInstance.vatLookup(country, name, opts, (error, data, response) => {
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
 **country** | **String**| ISO_3166-1_alpha-2 representation of a country name - 2 chars | 
 **name** | **String**| Company name | 
 **address** | **String**| Company address | [optional] 

### Return type

[**VatLookup200Response**](VatLookup200Response.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

