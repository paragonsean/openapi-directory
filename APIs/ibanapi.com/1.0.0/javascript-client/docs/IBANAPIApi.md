# IbanapiOpenApiDocumentation.IBANAPIApi

All URIs are relative to *https://api.ibanapi.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getBalance**](IBANAPIApi.md#getBalance) | **GET** /balance | Get Account Balance
[**validateIBAN**](IBANAPIApi.md#validateIBAN) | **GET** /validate | Validate IBAN
[**validateIBANBasic**](IBANAPIApi.md#validateIBANBasic) | **GET** /validate-basic | Validate IBAN Basic



## getBalance

> BalanceResponse getBalance()

Get Account Balance

Returns the account balance and expiry

### Example

```javascript
import IbanapiOpenApiDocumentation from 'ibanapi_open_api_documentation';
let defaultClient = IbanapiOpenApiDocumentation.ApiClient.instance;
// Configure API key authorization: api_key_security
let api_key_security = defaultClient.authentications['api_key_security'];
api_key_security.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key_security.apiKeyPrefix = 'Token';

let apiInstance = new IbanapiOpenApiDocumentation.IBANAPIApi();
apiInstance.getBalance((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**BalanceResponse**](BalanceResponse.md)

### Authorization

[api_key_security](../README.md#api_key_security)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## validateIBAN

> IBANResult validateIBAN(iban)

Validate IBAN

Returns the validation results

### Example

```javascript
import IbanapiOpenApiDocumentation from 'ibanapi_open_api_documentation';
let defaultClient = IbanapiOpenApiDocumentation.ApiClient.instance;
// Configure API key authorization: api_key_security
let api_key_security = defaultClient.authentications['api_key_security'];
api_key_security.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key_security.apiKeyPrefix = 'Token';

let apiInstance = new IbanapiOpenApiDocumentation.IBANAPIApi();
let iban = "iban_example"; // String | The IBAN
apiInstance.validateIBAN(iban, (error, data, response) => {
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
 **iban** | **String**| The IBAN | 

### Return type

[**IBANResult**](IBANResult.md)

### Authorization

[api_key_security](../README.md#api_key_security)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## validateIBANBasic

> IBANResultBasic validateIBANBasic(iban)

Validate IBAN Basic

Returns the basic validation results

### Example

```javascript
import IbanapiOpenApiDocumentation from 'ibanapi_open_api_documentation';
let defaultClient = IbanapiOpenApiDocumentation.ApiClient.instance;
// Configure API key authorization: api_key_security
let api_key_security = defaultClient.authentications['api_key_security'];
api_key_security.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key_security.apiKeyPrefix = 'Token';

let apiInstance = new IbanapiOpenApiDocumentation.IBANAPIApi();
let iban = "iban_example"; // String | The IBAN
apiInstance.validateIBANBasic(iban, (error, data, response) => {
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
 **iban** | **String**| The IBAN | 

### Return type

[**IBANResultBasic**](IBANResultBasic.md)

### Authorization

[api_key_security](../README.md#api_key_security)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

