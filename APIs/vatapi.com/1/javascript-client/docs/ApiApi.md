# VatApi.ApiApi

All URIs are relative to *https://vatapi.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiUsage**](ApiApi.md#apiUsage) | **GET** /usage-check | Check api requests remaining on current subscription plan
[**convertPrice**](ApiApi.md#convertPrice) | **GET** /vat-price | Convert a price to or from VAT price.
[**countryCodeCheck**](ApiApi.md#countryCodeCheck) | **GET** /country-code-check | Retrieve a countries VAT rates by its 2 digit country code
[**createInvoice**](ApiApi.md#createInvoice) | **POST** /invoice | Create a VAT invoice
[**currencyConversion**](ApiApi.md#currencyConversion) | **GET** /currency-conversion | Convert a currency
[**getInvoice**](ApiApi.md#getInvoice) | **GET** /invoice/{id} | Retrieve an invoice
[**invoiceDelete**](ApiApi.md#invoiceDelete) | **DELETE** /invoice/{id} | Delete an invoice
[**invoiceUpdate**](ApiApi.md#invoiceUpdate) | **PUT** /invoice/{id} | Update an existing invoice
[**ipCheck**](ApiApi.md#ipCheck) | **GET** /ip-check | Retrieve a countries VAT rates from an IP address
[**vatNumberValidate**](ApiApi.md#vatNumberValidate) | **GET** /vat-number-check | Validate a VAT number
[**vatRates**](ApiApi.md#vatRates) | **GET** /vat-rates | Retrieve all current EU VAT rates



## apiUsage

> ApiUsage apiUsage(opts)

Check api requests remaining on current subscription plan

### Example

```javascript
import VatApi from 'vat_api';
let defaultClient = VatApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new VatApi.ApiApi();
let opts = {
  'responseType': "responseType_example" // String | The default response type is application/json if you would like to receive an XML response then set this to XML
};
apiInstance.apiUsage(opts, (error, data, response) => {
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
 **responseType** | **String**| The default response type is application/json if you would like to receive an XML response then set this to XML | [optional] 

### Return type

[**ApiUsage**](ApiUsage.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## convertPrice

> ConvertPrice convertPrice(code, price, opts)

Convert a price to or from VAT price.

### Example

```javascript
import VatApi from 'vat_api';
let defaultClient = VatApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new VatApi.ApiApi();
let code = "code_example"; // String | The 2 digit country code
let price = 56; // Number | The price you want converting
let opts = {
  'responseType': "responseType_example", // String | The default response type is application/json if you would like to receive an XML response then set this to XML
  'countryRate': "countryRate_example", // String | The VAT rate to get the price for. Default: standard
  'type': "type_example" // String | Optional, if the price is including VAT set the type to 'incl'. Otherwise the default is assumed as excluding VAT already, 'excl'
};
apiInstance.convertPrice(code, price, opts, (error, data, response) => {
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
 **code** | **String**| The 2 digit country code | 
 **price** | **Number**| The price you want converting | 
 **responseType** | **String**| The default response type is application/json if you would like to receive an XML response then set this to XML | [optional] 
 **countryRate** | **String**| The VAT rate to get the price for. Default: standard | [optional] 
 **type** | **String**| Optional, if the price is including VAT set the type to &#39;incl&#39;. Otherwise the default is assumed as excluding VAT already, &#39;excl&#39; | [optional] 

### Return type

[**ConvertPrice**](ConvertPrice.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## countryCodeCheck

> CountryCodeCheck countryCodeCheck(code, opts)

Retrieve a countries VAT rates by its 2 digit country code

### Example

```javascript
import VatApi from 'vat_api';
let defaultClient = VatApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new VatApi.ApiApi();
let code = "code_example"; // String | The 2 digit country code
let opts = {
  'responseType': "responseType_example" // String | The default response type is application/json if you would like to receive an XML response then set this to XML
};
apiInstance.countryCodeCheck(code, opts, (error, data, response) => {
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
 **code** | **String**| The 2 digit country code | 
 **responseType** | **String**| The default response type is application/json if you would like to receive an XML response then set this to XML | [optional] 

### Return type

[**CountryCodeCheck**](CountryCodeCheck.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## createInvoice

> CreateInvoice createInvoice(body, opts)

Create a VAT invoice

### Example

```javascript
import VatApi from 'vat_api';
let defaultClient = VatApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new VatApi.ApiApi();
let body = new VatApi.InvoiceData(); // InvoiceData | Enter invoice data as JSON
let opts = {
  'responseType': "responseType_example" // String | The default response type is application/json if you would like to receive an XML response then set this to XML
};
apiInstance.createInvoice(body, opts, (error, data, response) => {
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
 **body** | [**InvoiceData**](InvoiceData.md)| Enter invoice data as JSON | 
 **responseType** | **String**| The default response type is application/json if you would like to receive an XML response then set this to XML | [optional] 

### Return type

[**CreateInvoice**](CreateInvoice.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## currencyConversion

> CurrencyConversion currencyConversion(currencyFrom, currencyTo, opts)

Convert a currency

### Example

```javascript
import VatApi from 'vat_api';
let defaultClient = VatApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new VatApi.ApiApi();
let currencyFrom = "currencyFrom_example"; // String | The currency code you are converting from
let currencyTo = "currencyTo_example"; // String | The currency code you are converting to
let opts = {
  'responseType': "responseType_example", // String | The default response type is application/json if you would like to receive an XML response then set this to XML
  'amount': 56 // Number | Optional, an amount you are wanting to convert. Leave blank to just get the current rate
};
apiInstance.currencyConversion(currencyFrom, currencyTo, opts, (error, data, response) => {
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
 **currencyFrom** | **String**| The currency code you are converting from | 
 **currencyTo** | **String**| The currency code you are converting to | 
 **responseType** | **String**| The default response type is application/json if you would like to receive an XML response then set this to XML | [optional] 
 **amount** | **Number**| Optional, an amount you are wanting to convert. Leave blank to just get the current rate | [optional] 

### Return type

[**CurrencyConversion**](CurrencyConversion.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getInvoice

> RetrieveInvoice getInvoice(id, opts)

Retrieve an invoice

### Example

```javascript
import VatApi from 'vat_api';
let defaultClient = VatApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new VatApi.ApiApi();
let id = 56; // Number | Enter the invoice id
let opts = {
  'responseType': "responseType_example" // String | The default response type is application/json if you would like to receive an XML response then set this to XML
};
apiInstance.getInvoice(id, opts, (error, data, response) => {
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
 **id** | **Number**| Enter the invoice id | 
 **responseType** | **String**| The default response type is application/json if you would like to receive an XML response then set this to XML | [optional] 

### Return type

[**RetrieveInvoice**](RetrieveInvoice.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## invoiceDelete

> invoiceDelete(id, opts)

Delete an invoice

### Example

```javascript
import VatApi from 'vat_api';
let defaultClient = VatApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new VatApi.ApiApi();
let id = 56; // Number | Enter an invoice id
let opts = {
  'responseType': "responseType_example" // String | The default response type is application/json if you would like to receive an XML response then set this to XML
};
apiInstance.invoiceDelete(id, opts, (error, data, response) => {
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
 **id** | **Number**| Enter an invoice id | 
 **responseType** | **String**| The default response type is application/json if you would like to receive an XML response then set this to XML | [optional] 

### Return type

null (empty response body)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## invoiceUpdate

> UpdateInvoice invoiceUpdate(id, body, opts)

Update an existing invoice

### Example

```javascript
import VatApi from 'vat_api';
let defaultClient = VatApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new VatApi.ApiApi();
let id = 56; // Number | Enter an invoice id
let body = new VatApi.UpdateInvoiceArray(); // UpdateInvoiceArray | Enter invoice data as JSON
let opts = {
  'responseType': "responseType_example" // String | The default response type is application/json if you would like to receive an XML response then set this to XML
};
apiInstance.invoiceUpdate(id, body, opts, (error, data, response) => {
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
 **id** | **Number**| Enter an invoice id | 
 **body** | [**UpdateInvoiceArray**](UpdateInvoiceArray.md)| Enter invoice data as JSON | 
 **responseType** | **String**| The default response type is application/json if you would like to receive an XML response then set this to XML | [optional] 

### Return type

[**UpdateInvoice**](UpdateInvoice.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## ipCheck

> IPCheck ipCheck(address, opts)

Retrieve a countries VAT rates from an IP address

### Example

```javascript
import VatApi from 'vat_api';
let defaultClient = VatApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new VatApi.ApiApi();
let address = "address_example"; // String | The IP address to search against
let opts = {
  'responseType': "responseType_example" // String | The default response type is application/json if you would like to receive an XML response then set this to XML
};
apiInstance.ipCheck(address, opts, (error, data, response) => {
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
 **address** | **String**| The IP address to search against | 
 **responseType** | **String**| The default response type is application/json if you would like to receive an XML response then set this to XML | [optional] 

### Return type

[**IPCheck**](IPCheck.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## vatNumberValidate

> vatNumberValidate(vatid, opts)

Validate a VAT number

&lt;p&gt;We highly recommend if you are able, to check a VAT number on your end first to save wasted API lookups. It maybe that your customer has simply entered the wrong format. &lt;a href&#x3D;&#39;http://www.braemoor.co.uk/software/vat.shtml&#39; target&#x3D;&#39;_blank&#39;&gt;Heres a client side way to check the format using Javascript&lt;/a&gt;&lt;/p&gt;

### Example

```javascript
import VatApi from 'vat_api';
let defaultClient = VatApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new VatApi.ApiApi();
let vatid = "vatid_example"; // String | The VAT number to validate
let opts = {
  'responseType': "responseType_example" // String | The default response type is application/json if you would like to receive an XML response then set this to XML
};
apiInstance.vatNumberValidate(vatid, opts, (error, data, response) => {
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
 **vatid** | **String**| The VAT number to validate | 
 **responseType** | **String**| The default response type is application/json if you would like to receive an XML response then set this to XML | [optional] 

### Return type

null (empty response body)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## vatRates

> VatRates vatRates(opts)

Retrieve all current EU VAT rates

### Example

```javascript
import VatApi from 'vat_api';
let defaultClient = VatApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new VatApi.ApiApi();
let opts = {
  'responseType': "responseType_example" // String | The default response type is application/json if you would like to receive an XML response then set this to XML
};
apiInstance.vatRates(opts, (error, data, response) => {
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
 **responseType** | **String**| The default response type is application/json if you would like to receive an XML response then set this to XML | [optional] 

### Return type

[**VatRates**](VatRates.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

