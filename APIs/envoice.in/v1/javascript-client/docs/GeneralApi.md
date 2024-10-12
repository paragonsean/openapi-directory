# ApiV100.GeneralApi

All URIs are relative to *https://www.envoice.in*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generalApiCountries**](GeneralApi.md#generalApiCountries) | **GET** /api/general/countries | Return all of the platform supported countries
[**generalApiCurrencies**](GeneralApi.md#generalApiCurrencies) | **GET** /api/general/currencies | Return all of the platform supported currencies
[**generalApiDateFormats**](GeneralApi.md#generalApiDateFormats) | **GET** /api/general/dateformats | Return all of the platform supported Date Formats
[**generalApiUiLanguages**](GeneralApi.md#generalApiUiLanguages) | **GET** /api/general/uilanguages | Return all of the platform supported UI languages



## generalApiCountries

> [CountryDetailsApiModel] generalApiCountries(xAuthKey, xAuthSecret)

Return all of the platform supported countries

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.GeneralApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
apiInstance.generalApiCountries(xAuthKey, xAuthSecret, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]

### Return type

[**[CountryDetailsApiModel]**](CountryDetailsApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## generalApiCurrencies

> [CurrencyDetailsApiModel] generalApiCurrencies(xAuthKey, xAuthSecret)

Return all of the platform supported currencies

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.GeneralApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
apiInstance.generalApiCurrencies(xAuthKey, xAuthSecret, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]

### Return type

[**[CurrencyDetailsApiModel]**](CurrencyDetailsApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## generalApiDateFormats

> [String] generalApiDateFormats(xAuthKey, xAuthSecret)

Return all of the platform supported Date Formats

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.GeneralApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
apiInstance.generalApiDateFormats(xAuthKey, xAuthSecret, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## generalApiUiLanguages

> [UILanguageDetailsApiModel] generalApiUiLanguages(xAuthKey, xAuthSecret)

Return all of the platform supported UI languages

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.GeneralApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
apiInstance.generalApiUiLanguages(xAuthKey, xAuthSecret, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]

### Return type

[**[UILanguageDetailsApiModel]**](UILanguageDetailsApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/html, text/json, text/xml

