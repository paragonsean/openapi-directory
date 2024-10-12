# WeGaApi.ApplicationApi

All URIs are relative to *http://localhost:8080/exist/apps/WeGA-WebApp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applicationNewIDGet**](ApplicationApi.md#applicationNewIDGet) | **GET** /application/newID | Create a new WeGA ID
[**applicationStatusGet**](ApplicationApi.md#applicationStatusGet) | **GET** /application/status | Get status information about the running WeGA-WebApp



## applicationNewIDGet

> ApplicationNewIDGet200Response applicationNewIDGet(docType)

Create a new WeGA ID

### Example

```javascript
import WeGaApi from 'we_ga_api';

let apiInstance = new WeGaApi.ApplicationApi();
let docType = ["null"]; // [String] | The WeGA document type
apiInstance.applicationNewIDGet(docType, (error, data, response) => {
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
 **docType** | [**[String]**](String.md)| The WeGA document type | 

### Return type

[**ApplicationNewIDGet200Response**](ApplicationNewIDGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationStatusGet

> ApplicationStatusGet200Response applicationStatusGet()

Get status information about the running WeGA-WebApp

### Example

```javascript
import WeGaApi from 'we_ga_api';

let apiInstance = new WeGaApi.ApplicationApi();
apiInstance.applicationStatusGet((error, data, response) => {
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

[**ApplicationStatusGet200Response**](ApplicationStatusGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

