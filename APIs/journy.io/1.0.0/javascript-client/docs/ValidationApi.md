# DeveloperDocumentation.ValidationApi

All URIs are relative to *https://api.journy.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getValidity**](ValidationApi.md#getValidity) | **GET** /validate | Validate API key



## getValidity

> GetValidity200Response getValidity()

Validate API key

Endpoint used to test the validity and some basic information about a specific API Key.

### Example

```javascript
import DeveloperDocumentation from 'developer_documentation';

let apiInstance = new DeveloperDocumentation.ValidationApi();
apiInstance.getValidity((error, data, response) => {
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

[**GetValidity200Response**](GetValidity200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

