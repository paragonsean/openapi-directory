# DeveloperDocumentation.PropertiesApi

All URIs are relative to *https://api.journy.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAccountProperties**](PropertiesApi.md#getAccountProperties) | **GET** /properties/accounts | Get account properties
[**getUserProperties**](PropertiesApi.md#getUserProperties) | **GET** /properties/users | Get user properties



## getAccountProperties

> GetAccountProperties200Response getAccountProperties()

Get account properties

Endpoint to list account properties.

### Example

```javascript
import DeveloperDocumentation from 'developer_documentation';

let apiInstance = new DeveloperDocumentation.PropertiesApi();
apiInstance.getAccountProperties((error, data, response) => {
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

[**GetAccountProperties200Response**](GetAccountProperties200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUserProperties

> GetAccountProperties200Response getUserProperties()

Get user properties

Endpoint to list user properties.

### Example

```javascript
import DeveloperDocumentation from 'developer_documentation';

let apiInstance = new DeveloperDocumentation.PropertiesApi();
apiInstance.getUserProperties((error, data, response) => {
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

[**GetAccountProperties200Response**](GetAccountProperties200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

