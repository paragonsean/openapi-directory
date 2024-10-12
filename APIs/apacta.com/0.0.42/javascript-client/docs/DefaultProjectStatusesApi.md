# Apacta.DefaultProjectStatusesApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projectStatusesAddDefaultPost**](DefaultProjectStatusesApi.md#projectStatusesAddDefaultPost) | **POST** /project_statuses/add_default | Add default project statuses to company



## projectStatusesAddDefaultPost

> AddDefaultProjectStatusesError projectStatusesAddDefaultPost()

Add default project statuses to company

### Example

```javascript
import Apacta from 'apacta';

let apiInstance = new Apacta.DefaultProjectStatusesApi();
apiInstance.projectStatusesAddDefaultPost((error, data, response) => {
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

[**AddDefaultProjectStatusesError**](AddDefaultProjectStatusesError.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

