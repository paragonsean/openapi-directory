# RudderApi.BrandingApi

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getBrandingConf**](BrandingApi.md#getBrandingConf) | **GET** /branding | Get branding configuration
[**reloadBrandingConf**](BrandingApi.md#reloadBrandingConf) | **POST** /branding/reload | Reload branding file
[**updateBRandingConf**](BrandingApi.md#updateBRandingConf) | **POST** /branding | Update web interface customization



## getBrandingConf

> GetBrandingConf200Response getBrandingConf()

Get branding configuration

Get all web interface customization parameters

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.BrandingApi();
apiInstance.getBrandingConf((error, data, response) => {
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

[**GetBrandingConf200Response**](GetBrandingConf200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reloadBrandingConf

> GetBrandingConf200Response reloadBrandingConf()

Reload branding file

Reload the configuration from file

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.BrandingApi();
apiInstance.reloadBrandingConf((error, data, response) => {
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

[**GetBrandingConf200Response**](GetBrandingConf200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateBRandingConf

> UpdateBRandingConf200Response updateBRandingConf(brandingConf)

Update web interface customization

change color, logo, label etc.

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.BrandingApi();
let brandingConf = new RudderApi.BrandingConf(); // BrandingConf | 
apiInstance.updateBRandingConf(brandingConf, (error, data, response) => {
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
 **brandingConf** | [**BrandingConf**](BrandingConf.md)|  | 

### Return type

[**UpdateBRandingConf200Response**](UpdateBRandingConf200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

