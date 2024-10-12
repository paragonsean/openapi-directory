# JellyfinApi.BrandingApi

All URIs are relative to *http://jellyfin.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getBrandingCss**](BrandingApi.md#getBrandingCss) | **GET** /Branding/Css | Gets branding css.
[**getBrandingCss2**](BrandingApi.md#getBrandingCss2) | **GET** /Branding/Css.css | Gets branding css.
[**getBrandingOptions**](BrandingApi.md#getBrandingOptions) | **GET** /Branding/Configuration | Gets branding configuration.



## getBrandingCss

> String getBrandingCss()

Gets branding css.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.BrandingApi();
apiInstance.getBrandingCss((error, data, response) => {
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

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase, text/css


## getBrandingCss2

> String getBrandingCss2()

Gets branding css.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.BrandingApi();
apiInstance.getBrandingCss2((error, data, response) => {
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

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase, text/css


## getBrandingOptions

> BrandingOptions getBrandingOptions()

Gets branding configuration.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.BrandingApi();
apiInstance.getBrandingOptions((error, data, response) => {
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

[**BrandingOptions**](BrandingOptions.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase

