# GroundhogDayApi.InfoApi

All URIs are relative to *https://virtserver.swaggerhub.com/pcraig3/groundhog-day-api/1.2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**root**](InfoApi.md#root) | **GET** /api/v1 | Root
[**spec**](InfoApi.md#spec) | **GET** /api/v1/spec | Get JSON schema



## root

> Root200Response root()

Root

Returns a welcome message.

### Example

```javascript
import GroundhogDayApi from 'groundhog_day_api';

let apiInstance = new GroundhogDayApi.InfoApi();
apiInstance.root((error, data, response) => {
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

[**Root200Response**](Root200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## spec

> spec()

Get JSON schema

Gets the schema for the JSON API as a yaml file.

### Example

```javascript
import GroundhogDayApi from 'groundhog_day_api';

let apiInstance = new GroundhogDayApi.InfoApi();
apiInstance.spec((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

