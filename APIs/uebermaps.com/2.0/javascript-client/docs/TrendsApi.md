# UebermapsApiEndpoints.TrendsApi

All URIs are relative to *http://uebermaps.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**trendsLatestGet**](TrendsApi.md#trendsLatestGet) | **GET** /trends/latest | List latest maps
[**trendsRecommendedGet**](TrendsApi.md#trendsRecommendedGet) | **GET** /trends/recommended | List recommended maps



## trendsLatestGet

> [Map] trendsLatestGet()

List latest maps

List latest maps.

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.TrendsApi();
apiInstance.trendsLatestGet((error, data, response) => {
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

[**[Map]**](Map.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## trendsRecommendedGet

> [Map] trendsRecommendedGet()

List recommended maps

List recommended maps.

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.TrendsApi();
apiInstance.trendsRecommendedGet((error, data, response) => {
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

[**[Map]**](Map.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

