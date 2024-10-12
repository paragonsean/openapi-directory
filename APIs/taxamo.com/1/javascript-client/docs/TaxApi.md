# Taxamo.TaxApi

All URIs are relative to *https://api.taxamo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calculateSimpleTax**](TaxApi.md#calculateSimpleTax) | **GET** /api/v1/tax/calculate | Simple tax
[**calculateTax**](TaxApi.md#calculateTax) | **POST** /api/v1/tax/calculate | Calculate tax
[**calculateTaxLocation**](TaxApi.md#calculateTaxLocation) | **GET** /api/v1/tax/location/calculate | Calculate location
[**validateTaxNumber**](TaxApi.md#validateTaxNumber) | **GET** /api/v1/tax/vat_numbers/{tax_number}/validate | Validate VAT number



## calculateSimpleTax

> CalculateSimpleTaxOut calculateSimpleTax(currencyCode, opts)

Simple tax

### Example

```javascript
import Taxamo from 'taxamo';

let apiInstance = new Taxamo.TaxApi();
let currencyCode = "currencyCode_example"; // String | Currency code for transaction - e.g. EUR.
let opts = {
  'productType': "productType_example", // String | Product type, according to dictionary /dictionaries/product_types. 
  'invoiceAddressCity': "invoiceAddressCity_example", // String | Invoice address/postal_code
  'buyerCreditCardPrefix': "buyerCreditCardPrefix_example", // String | First 6 digits of buyer's credit card prefix.
  'invoiceAddressRegion': "invoiceAddressRegion_example", // String | Invoice address/region
  'unitPrice': 3.4, // Number | Unit price.
  'quantity': 3.4, // Number | Quantity Defaults to 1.
  'buyerTaxNumber': "buyerTaxNumber_example", // String |  Buyer's tax number - EU VAT number for example. If using EU VAT number, it is possible to provide country code in it (e.g. IE1234567X) or simply use billing_country_code field for that. In the first case, if billing_country_code value was provided, it will be overwritten with country code value extracted from VAT number - but only if the VAT has been verified properly.
  'forceCountryCode': "forceCountryCode_example", // String | Two-letter ISO country code, e.g. FR. Use it to force country code for tax calculation.
  'orderDate': "orderDate_example", // String | Order date in yyyy-MM-dd format, in merchant's timezone. If provided by the API caller, no timezone conversion is performed. Default value is current date and time. When using public token, the default value is used.
  'amount': 3.4, // Number | Amount. Required if total amount or both unit price and quantity are not provided.
  'billingCountryCode': "billingCountryCode_example", // String | Billing two letter ISO country code.
  'invoiceAddressPostalCode': "invoiceAddressPostalCode_example", // String | Invoice address/postal_code
  'totalAmount': 3.4, // Number | Total amount. Required if amount or both unit price and quantity are not provided.
  'taxDeducted': true // Boolean | If the transaction is in a country supported by Taxamo, but the tax is not calculated due to merchant settings or EU B2B transaction for example.
};
apiInstance.calculateSimpleTax(currencyCode, opts, (error, data, response) => {
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
 **currencyCode** | **String**| Currency code for transaction - e.g. EUR. | 
 **productType** | **String**| Product type, according to dictionary /dictionaries/product_types.  | [optional] 
 **invoiceAddressCity** | **String**| Invoice address/postal_code | [optional] 
 **buyerCreditCardPrefix** | **String**| First 6 digits of buyer&#39;s credit card prefix. | [optional] 
 **invoiceAddressRegion** | **String**| Invoice address/region | [optional] 
 **unitPrice** | **Number**| Unit price. | [optional] 
 **quantity** | **Number**| Quantity Defaults to 1. | [optional] 
 **buyerTaxNumber** | **String**|  Buyer&#39;s tax number - EU VAT number for example. If using EU VAT number, it is possible to provide country code in it (e.g. IE1234567X) or simply use billing_country_code field for that. In the first case, if billing_country_code value was provided, it will be overwritten with country code value extracted from VAT number - but only if the VAT has been verified properly. | [optional] 
 **forceCountryCode** | **String**| Two-letter ISO country code, e.g. FR. Use it to force country code for tax calculation. | [optional] 
 **orderDate** | **String**| Order date in yyyy-MM-dd format, in merchant&#39;s timezone. If provided by the API caller, no timezone conversion is performed. Default value is current date and time. When using public token, the default value is used. | [optional] 
 **amount** | **Number**| Amount. Required if total amount or both unit price and quantity are not provided. | [optional] 
 **billingCountryCode** | **String**| Billing two letter ISO country code. | [optional] 
 **invoiceAddressPostalCode** | **String**| Invoice address/postal_code | [optional] 
 **totalAmount** | **Number**| Total amount. Required if amount or both unit price and quantity are not provided. | [optional] 
 **taxDeducted** | **Boolean**| If the transaction is in a country supported by Taxamo, but the tax is not calculated due to merchant settings or EU B2B transaction for example. | [optional] 

### Return type

[**CalculateSimpleTaxOut**](CalculateSimpleTaxOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## calculateTax

> CalculateTaxOut calculateTax(input)

Calculate tax

### Example

```javascript
import Taxamo from 'taxamo';

let apiInstance = new Taxamo.TaxApi();
let input = new Taxamo.CalculateTaxIn(); // CalculateTaxIn | Input
apiInstance.calculateTax(input, (error, data, response) => {
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
 **input** | [**CalculateTaxIn**](CalculateTaxIn.md)| Input | 

### Return type

[**CalculateTaxOut**](CalculateTaxOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## calculateTaxLocation

> CalculateTaxLocationOut calculateTaxLocation(opts)

Calculate location

### Example

```javascript
import Taxamo from 'taxamo';

let apiInstance = new Taxamo.TaxApi();
let opts = {
  'billingCountryCode': "billingCountryCode_example", // String | Billing two letter ISO country code.
  'buyerCreditCardPrefix': "buyerCreditCardPrefix_example" // String | First 6 digits of buyer's credit card prefix.
};
apiInstance.calculateTaxLocation(opts, (error, data, response) => {
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
 **billingCountryCode** | **String**| Billing two letter ISO country code. | [optional] 
 **buyerCreditCardPrefix** | **String**| First 6 digits of buyer&#39;s credit card prefix. | [optional] 

### Return type

[**CalculateTaxLocationOut**](CalculateTaxLocationOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## validateTaxNumber

> ValidateTaxNumberOut validateTaxNumber(taxNumber, opts)

Validate VAT number

### Example

```javascript
import Taxamo from 'taxamo';

let apiInstance = new Taxamo.TaxApi();
let taxNumber = "taxNumber_example"; // String | Tax number
let opts = {
  'countryCode': "countryCode_example" // String | Two-letter ISO country code.
};
apiInstance.validateTaxNumber(taxNumber, opts, (error, data, response) => {
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
 **taxNumber** | **String**| Tax number | 
 **countryCode** | **String**| Two-letter ISO country code. | [optional] 

### Return type

[**ValidateTaxNumberOut**](ValidateTaxNumberOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

