# DeveloperDocumentation.SegmentsApi

All URIs are relative to *https://api.journy.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAccountSegments**](SegmentsApi.md#getAccountSegments) | **GET** /segments/accounts | Get account segments
[**getUserSegments**](SegmentsApi.md#getUserSegments) | **GET** /segments/users | Get user segments



## getAccountSegments

> GetAccountSegments200Response getAccountSegments()

Get account segments

Endpoint to list account segments.

### Example

```javascript
import DeveloperDocumentation from 'developer_documentation';

let apiInstance = new DeveloperDocumentation.SegmentsApi();
apiInstance.getAccountSegments((error, data, response) => {
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

[**GetAccountSegments200Response**](GetAccountSegments200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUserSegments

> GetAccountSegments200Response getUserSegments()

Get user segments

Endpoint to list user segments.

### Example

```javascript
import DeveloperDocumentation from 'developer_documentation';

let apiInstance = new DeveloperDocumentation.SegmentsApi();
apiInstance.getUserSegments((error, data, response) => {
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

[**GetAccountSegments200Response**](GetAccountSegments200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

