# GroundhogDayApi.GroundhogsApi

All URIs are relative to *https://virtserver.swaggerhub.com/pcraig3/groundhog-day-api/1.2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**groundhog**](GroundhogsApi.md#groundhog) | **GET** /api/v1/groundhogs/{slug} | Get a groundhog by slug
[**groundhogs**](GroundhogsApi.md#groundhogs) | **GET** /api/v1/groundhogs | Get all groundhogs



## groundhog

> Groundhog200Response groundhog(slug)

Get a groundhog by slug

Returns a prognosticating animal and its known predictions.

### Example

```javascript
import GroundhogDayApi from 'groundhog_day_api';

let apiInstance = new GroundhogDayApi.GroundhogsApi();
let slug = "slug_example"; // String | Groundhog name in kebab-case: (eg, lucy-the-lobster)
apiInstance.groundhog(slug, (error, data, response) => {
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
 **slug** | **String**| Groundhog name in kebab-case: (eg, lucy-the-lobster) | 

### Return type

[**Groundhog200Response**](Groundhog200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## groundhogs

> Groundhogs200Response groundhogs(opts)

Get all groundhogs

Returns all prognosticating animals with their known predictions.

### Example

```javascript
import GroundhogDayApi from 'groundhog_day_api';

let apiInstance = new GroundhogDayApi.GroundhogsApi();
let opts = {
  'country': "Canada or USA", // String | Filter groundhogs by country of origin (USA or Canada).
  'isGroundhog': "isGroundhog_example" // String | Filter groundhogs by type (actual, alive groundhogs, or other prognosticators)
};
apiInstance.groundhogs(opts, (error, data, response) => {
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
 **country** | **String**| Filter groundhogs by country of origin (USA or Canada). | [optional] 
 **isGroundhog** | **String**| Filter groundhogs by type (actual, alive groundhogs, or other prognosticators) | [optional] 

### Return type

[**Groundhogs200Response**](Groundhogs200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

