# JumpsellerApi.RegionsApi

All URIs are relative to *https://api.jumpseller.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**countriesCountryCodeRegionsJsonGet_0**](RegionsApi.md#countriesCountryCodeRegionsJsonGet_0) | **GET** /countries/{country_code}/regions.json | Retrieve all Regions from a single Country.
[**countriesCountryCodeRegionsRegionCodeJsonGet_0**](RegionsApi.md#countriesCountryCodeRegionsRegionCodeJsonGet_0) | **GET** /countries/{country_code}/regions/{region_code}.json | Retrieve a single Region information object.



## countriesCountryCodeRegionsJsonGet_0

> [Region] countriesCountryCodeRegionsJsonGet_0(login, authtoken, countryCode)

Retrieve all Regions from a single Country.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.RegionsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let countryCode = "countryCode_example"; // String | ISO3166 Country Code
apiInstance.countriesCountryCodeRegionsJsonGet_0(login, authtoken, countryCode, (error, data, response) => {
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


## countriesCountryCodeRegionsRegionCodeJsonGet_0

> Region countriesCountryCodeRegionsRegionCodeJsonGet_0(login, authtoken, countryCode, regionCode)

Retrieve a single Region information object.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.RegionsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let countryCode = "countryCode_example"; // String | ISO3166 Country Code
let regionCode = "regionCode_example"; // String | Region Code
apiInstance.countriesCountryCodeRegionsRegionCodeJsonGet_0(login, authtoken, countryCode, regionCode, (error, data, response) => {
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

