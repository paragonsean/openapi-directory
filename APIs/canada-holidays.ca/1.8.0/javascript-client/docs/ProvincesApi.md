# CanadaHolidaysApi.ProvincesApi

All URIs are relative to *https://canada-holidays.ca*

Method | HTTP request | Description
------------- | ------------- | -------------
[**province**](ProvincesApi.md#province) | **GET** /api/v1/provinces/{provinceId} | Get a province or territory by abbreviation
[**provinces**](ProvincesApi.md#provinces) | **GET** /api/v1/provinces | Get all provinces



## province

> Province200Response province(provinceId, opts)

Get a province or territory by abbreviation

Returns a Canadian province or territory with its associated holidays. Returns a 404 response for invalid abbreviations.

### Example

```javascript
import CanadaHolidaysApi from 'canada_holidays_api';

let apiInstance = new CanadaHolidaysApi.ProvincesApi();
let provinceId = "MB"; // String | A Canadian province abbreviation
let opts = {
  'year': 2023, // Number | A calendar year
  'optional': "'false'" // String | A boolean parameter (AB and BC only). If false or 0 (default), will return only legislated holidays. If true or 1, will return optional holidays from Alberta and BC.
};
apiInstance.province(provinceId, opts, (error, data, response) => {
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
 **provinceId** | **String**| A Canadian province abbreviation | 
 **year** | **Number**| A calendar year | [optional] [default to 2023]
 **optional** | **String**| A boolean parameter (AB and BC only). If false or 0 (default), will return only legislated holidays. If true or 1, will return optional holidays from Alberta and BC. | [optional] [default to &#39;false&#39;]

### Return type

[**Province200Response**](Province200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## provinces

> Provinces200Response provinces(opts)

Get all provinces

Returns provinces and territories in Canada. Each province or territory lists its associated holidays.

### Example

```javascript
import CanadaHolidaysApi from 'canada_holidays_api';

let apiInstance = new CanadaHolidaysApi.ProvincesApi();
let opts = {
  'year': 2023, // Number | A calendar year
  'optional': "'false'" // String | A boolean parameter. If false or 0 (default), will return only legislated holidays. If true or 1, will return optional holidays from Alberta and BC.
};
apiInstance.provinces(opts, (error, data, response) => {
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
 **year** | **Number**| A calendar year | [optional] [default to 2023]
 **optional** | **String**| A boolean parameter. If false or 0 (default), will return only legislated holidays. If true or 1, will return optional holidays from Alberta and BC. | [optional] [default to &#39;false&#39;]

### Return type

[**Provinces200Response**](Provinces200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

