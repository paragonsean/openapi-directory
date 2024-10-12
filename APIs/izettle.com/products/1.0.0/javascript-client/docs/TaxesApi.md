# ProductLibraryApi.TaxesApi

All URIs are relative to *https://products.izettle.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createTaxRates**](TaxesApi.md#createTaxRates) | **POST** /v1/taxes | Create new tax rates
[**deleteTaxRate**](TaxesApi.md#deleteTaxRate) | **DELETE** /v1/taxes/{taxRateUuid} | Delete a single tax rate
[**getProductCountForAllTaxes**](TaxesApi.md#getProductCountForAllTaxes) | **GET** /v1/taxes/count | Get all tax rates and a count of products associated with each
[**getTaxRate**](TaxesApi.md#getTaxRate) | **GET** /v1/taxes/{taxRateUuid} | Get a single tax rate
[**getTaxRates**](TaxesApi.md#getTaxRates) | **GET** /v1/taxes | Get all available tax rates
[**getTaxSettings**](TaxesApi.md#getTaxSettings) | **GET** /v1/taxes/settings | Get the organization tax settings 
[**setTaxationMode**](TaxesApi.md#setTaxationMode) | **PUT** /v1/taxes/settings | Update the organization tax settings
[**updateTaxRate**](TaxesApi.md#updateTaxRate) | **PUT** /v1/taxes/{taxRateUuid} | Update a single tax rate



## createTaxRates

> TaxRatesResponse createTaxRates(taxRatesCreateRequest)

Create new tax rates

### Example

```javascript
import ProductLibraryApi from 'product_library_api';
let defaultClient = ProductLibraryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: ZettleOauth
let ZettleOauth = defaultClient.authentications['ZettleOauth'];
ZettleOauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ProductLibraryApi.TaxesApi();
let taxRatesCreateRequest = new ProductLibraryApi.TaxRatesCreateRequest(); // TaxRatesCreateRequest | 
apiInstance.createTaxRates(taxRatesCreateRequest, (error, data, response) => {
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
 **taxRatesCreateRequest** | [**TaxRatesCreateRequest**](TaxRatesCreateRequest.md)|  | 

### Return type

[**TaxRatesResponse**](TaxRatesResponse.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteTaxRate

> deleteTaxRate(taxRateUuid)

Delete a single tax rate

### Example

```javascript
import ProductLibraryApi from 'product_library_api';
let defaultClient = ProductLibraryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: ZettleOauth
let ZettleOauth = defaultClient.authentications['ZettleOauth'];
ZettleOauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ProductLibraryApi.TaxesApi();
let taxRateUuid = "taxRateUuid_example"; // String | 
apiInstance.deleteTaxRate(taxRateUuid, (error, data, response) => {
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
 **taxRateUuid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getProductCountForAllTaxes

> TaxRateProductCountResponse getProductCountForAllTaxes()

Get all tax rates and a count of products associated with each

### Example

```javascript
import ProductLibraryApi from 'product_library_api';
let defaultClient = ProductLibraryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: ZettleOauth
let ZettleOauth = defaultClient.authentications['ZettleOauth'];
ZettleOauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ProductLibraryApi.TaxesApi();
apiInstance.getProductCountForAllTaxes((error, data, response) => {
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

[**TaxRateProductCountResponse**](TaxRateProductCountResponse.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTaxRate

> TaxRate getTaxRate(taxRateUuid)

Get a single tax rate

### Example

```javascript
import ProductLibraryApi from 'product_library_api';
let defaultClient = ProductLibraryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: ZettleOauth
let ZettleOauth = defaultClient.authentications['ZettleOauth'];
ZettleOauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ProductLibraryApi.TaxesApi();
let taxRateUuid = "taxRateUuid_example"; // String | 
apiInstance.getTaxRate(taxRateUuid, (error, data, response) => {
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
 **taxRateUuid** | **String**|  | 

### Return type

[**TaxRate**](TaxRate.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTaxRates

> [TaxRatesResponse] getTaxRates()

Get all available tax rates

### Example

```javascript
import ProductLibraryApi from 'product_library_api';
let defaultClient = ProductLibraryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: ZettleOauth
let ZettleOauth = defaultClient.authentications['ZettleOauth'];
ZettleOauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ProductLibraryApi.TaxesApi();
apiInstance.getTaxRates((error, data, response) => {
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

[**[TaxRatesResponse]**](TaxRatesResponse.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTaxSettings

> TaxSettingsResponse getTaxSettings()

Get the organization tax settings 

### Example

```javascript
import ProductLibraryApi from 'product_library_api';
let defaultClient = ProductLibraryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: ZettleOauth
let ZettleOauth = defaultClient.authentications['ZettleOauth'];
ZettleOauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ProductLibraryApi.TaxesApi();
apiInstance.getTaxSettings((error, data, response) => {
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

[**TaxSettingsResponse**](TaxSettingsResponse.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setTaxationMode

> TaxSettingsResponse setTaxationMode(taxSettingsUpdateRequest)

Update the organization tax settings

### Example

```javascript
import ProductLibraryApi from 'product_library_api';
let defaultClient = ProductLibraryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: ZettleOauth
let ZettleOauth = defaultClient.authentications['ZettleOauth'];
ZettleOauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ProductLibraryApi.TaxesApi();
let taxSettingsUpdateRequest = new ProductLibraryApi.TaxSettingsUpdateRequest(); // TaxSettingsUpdateRequest | 
apiInstance.setTaxationMode(taxSettingsUpdateRequest, (error, data, response) => {
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
 **taxSettingsUpdateRequest** | [**TaxSettingsUpdateRequest**](TaxSettingsUpdateRequest.md)|  | 

### Return type

[**TaxSettingsResponse**](TaxSettingsResponse.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateTaxRate

> TaxRate updateTaxRate(taxRateUuid, taxRateUpdateRequest)

Update a single tax rate

### Example

```javascript
import ProductLibraryApi from 'product_library_api';
let defaultClient = ProductLibraryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: ZettleOauth
let ZettleOauth = defaultClient.authentications['ZettleOauth'];
ZettleOauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ProductLibraryApi.TaxesApi();
let taxRateUuid = "taxRateUuid_example"; // String | 
let taxRateUpdateRequest = new ProductLibraryApi.TaxRateUpdateRequest(); // TaxRateUpdateRequest | 
apiInstance.updateTaxRate(taxRateUuid, taxRateUpdateRequest, (error, data, response) => {
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
 **taxRateUuid** | **String**|  | 
 **taxRateUpdateRequest** | [**TaxRateUpdateRequest**](TaxRateUpdateRequest.md)|  | 

### Return type

[**TaxRate**](TaxRate.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

