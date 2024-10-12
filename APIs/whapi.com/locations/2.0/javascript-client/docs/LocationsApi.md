# Locations.LocationsApi

All URIs are relative to *https://sandbox.whapi.com/v2/locations*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addressLookup**](LocationsApi.md#addressLookup) | **GET** /address/lookup/ | 
[**getCountries**](LocationsApi.md#getCountries) | **GET** /countries/ | 
[**getCountry**](LocationsApi.md#getCountry) | **GET** /countries/{countryCode} | 
[**getCurrencies**](LocationsApi.md#getCurrencies) | **GET** /currencies/ | 
[**getCurrency**](LocationsApi.md#getCurrency) | **GET** /currencies/{currencyCode} | 



## addressLookup

> Addresses addressLookup(houseNum, postCode)



Retrieves a list of addresses when supplied with a house number or name and a postcode. It is generally used during customer registration to provide a list of possible addresses from where the customer can select their own address details. 

### Example

```javascript
import Locations from 'locations';
let defaultClient = Locations.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new Locations.LocationsApi();
let houseNum = "houseNum_example"; // String | House number or name of the address.
let postCode = "postCode_example"; // String | Postcode of the address, no spaces required.
apiInstance.addressLookup(houseNum, postCode, (error, data, response) => {
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
 **houseNum** | **String**| House number or name of the address. | 
 **postCode** | **String**| Postcode of the address, no spaces required. | 

### Return type

[**Addresses**](Addresses.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCountries

> Countries getCountries()



Retrieves a list of countries and its currencies.

### Example

```javascript
import Locations from 'locations';
let defaultClient = Locations.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new Locations.LocationsApi();
apiInstance.getCountries((error, data, response) => {
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

[**Countries**](Countries.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCountry

> Country getCountry(countryCode)



Retrieves the specified country and its currency.

### Example

```javascript
import Locations from 'locations';
let defaultClient = Locations.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new Locations.LocationsApi();
let countryCode = "countryCode_example"; // String | Code of the country
apiInstance.getCountry(countryCode, (error, data, response) => {
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
 **countryCode** | **String**| Code of the country | 

### Return type

[**Country**](Country.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCurrencies

> Currencies getCurrencies()



Retreives the list of currencies.

### Example

```javascript
import Locations from 'locations';
let defaultClient = Locations.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new Locations.LocationsApi();
apiInstance.getCurrencies((error, data, response) => {
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

[**Currencies**](Currencies.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCurrency

> Currency getCurrency(currencyCode)



Retreives the specified currency.

### Example

```javascript
import Locations from 'locations';
let defaultClient = Locations.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new Locations.LocationsApi();
let currencyCode = "currencyCode_example"; // String | Code of the currency
apiInstance.getCurrency(currencyCode, (error, data, response) => {
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
 **currencyCode** | **String**| Code of the currency | 

### Return type

[**Currency**](Currency.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

