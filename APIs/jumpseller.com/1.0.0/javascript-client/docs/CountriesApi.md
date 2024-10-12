# JumpsellerApi.CountriesApi

All URIs are relative to *https://api.jumpseller.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**countriesCountryCodeJsonGet**](CountriesApi.md#countriesCountryCodeJsonGet) | **GET** /countries/{country_code}.json | Retrieve a single Country information.
[**countriesCountryCodeRegionsJsonGet**](CountriesApi.md#countriesCountryCodeRegionsJsonGet) | **GET** /countries/{country_code}/regions.json | Retrieve all Regions from a single Country.
[**countriesCountryCodeRegionsRegionCodeJsonGet**](CountriesApi.md#countriesCountryCodeRegionsRegionCodeJsonGet) | **GET** /countries/{country_code}/regions/{region_code}.json | Retrieve a single Region information object.
[**countriesJsonGet**](CountriesApi.md#countriesJsonGet) | **GET** /countries.json | Retrieve all Countries.



## countriesCountryCodeJsonGet

> Country countriesCountryCodeJsonGet(login, authtoken, countryCode)

Retrieve a single Country information.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CountriesApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let countryCode = "countryCode_example"; // String | ISO3166 Country Code
apiInstance.countriesCountryCodeJsonGet(login, authtoken, countryCode, (error, data, response) => {
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
 **login** | **String**| API OAuth login. | 
 **authtoken** | **String**| API OAuth token. | 
 **countryCode** | **String**| ISO3166 Country Code | 

### Return type

[**Country**](Country.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## countriesCountryCodeRegionsJsonGet

> [Region] countriesCountryCodeRegionsJsonGet(login, authtoken, countryCode)

Retrieve all Regions from a single Country.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CountriesApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let countryCode = "countryCode_example"; // String | ISO3166 Country Code
apiInstance.countriesCountryCodeRegionsJsonGet(login, authtoken, countryCode, (error, data, response) => {
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
 **login** | **String**| API OAuth login. | 
 **authtoken** | **String**| API OAuth token. | 
 **countryCode** | **String**| ISO3166 Country Code | 

### Return type

[**[Region]**](Region.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## countriesCountryCodeRegionsRegionCodeJsonGet

> Region countriesCountryCodeRegionsRegionCodeJsonGet(login, authtoken, countryCode, regionCode)

Retrieve a single Region information object.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CountriesApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let countryCode = "countryCode_example"; // String | ISO3166 Country Code
let regionCode = "regionCode_example"; // String | Region Code
apiInstance.countriesCountryCodeRegionsRegionCodeJsonGet(login, authtoken, countryCode, regionCode, (error, data, response) => {
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
 **login** | **String**| API OAuth login. | 
 **authtoken** | **String**| API OAuth token. | 
 **countryCode** | **String**| ISO3166 Country Code | 
 **regionCode** | **String**| Region Code | 

### Return type

[**Region**](Region.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## countriesJsonGet

> [Country] countriesJsonGet(login, authtoken)

Retrieve all Countries.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CountriesApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
apiInstance.countriesJsonGet(login, authtoken, (error, data, response) => {
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
 **login** | **String**| API OAuth login. | 
 **authtoken** | **String**| API OAuth token. | 

### Return type

[**[Country]**](Country.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

