# ShipEngineApi.AddressesApi

All URIs are relative to *https://api.shipengine.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**parseAddress**](AddressesApi.md#parseAddress) | **PUT** /v1/addresses/recognize | Parse an address
[**validateAddress**](AddressesApi.md#validateAddress) | **POST** /v1/addresses/validate | Validate An Address



## parseAddress

> ParseAddressResponseBody parseAddress(parseAddressRequestBody)

Parse an address

The address-recognition API makes it easy for you to extract address data from unstructured text, including the recipient name, line 1, line 2, city, postal code, and more.  Data often enters your system as unstructured text (for example: emails, SMS messages, support tickets, or other documents). ShipEngine&#39;s address-recognition API helps you extract meaningful, structured data from this unstructured text. The parsed address data is returned in the same structure that&#39;s used for other ShipEngine APIs, such as address validation, rate quotes, and shipping labels.  &gt; **Note:** Address recognition is currently supported for the United States, Canada, Australia, New Zealand, the United Kingdom, and Ireland. 

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.AddressesApi();
let parseAddressRequestBody = {"address":{"address_residential_indicator":true,"country_code":"US"},"text":"Margie McMiller at 3800 North Lamar suite 200 in austin, tx.  The zip code there is 78652."}; // ParseAddressRequestBody | The only required field is `text`, which is the text to be parsed. You can optionally also provide an `address` containing already-known values. For example, you may already know the recipient's name, city, and country, and only want to parse the street address into separate lines. 
apiInstance.parseAddress(parseAddressRequestBody, (error, data, response) => {
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
 **parseAddressRequestBody** | [**ParseAddressRequestBody**](ParseAddressRequestBody.md)| The only required field is &#x60;text&#x60;, which is the text to be parsed. You can optionally also provide an &#x60;address&#x60; containing already-known values. For example, you may already know the recipient&#39;s name, city, and country, and only want to parse the street address into separate lines.  | 

### Return type

[**ParseAddressResponseBody**](ParseAddressResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## validateAddress

> [AddressValidationResult] validateAddress(addressToValidate)

Validate An Address

Address validation ensures accurate addresses and can lead to reduced shipping costs by preventing address correction surcharges. ShipEngine cross references multiple databases to validate addresses and identify potential deliverability issues. 

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.AddressesApi();
let addressToValidate = [{"address_line1":"500 South Buena Vista Street","city_locality":"Burbank","company_name":"The Walt Disney Company","country_code":"US","name":"Mickey and Minnie Mouse","phone":"714-781-4565","postal_code":91521,"state_province":"CA"}]; // [AddressToValidate] | 
apiInstance.validateAddress(addressToValidate, (error, data, response) => {
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
 **addressToValidate** | [**[AddressToValidate]**](AddressToValidate.md)|  | 

### Return type

[**[AddressValidationResult]**](AddressValidationResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

