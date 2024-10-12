# WireMock.ScenariosApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adminScenariosGet**](ScenariosApi.md#adminScenariosGet) | **GET** /__admin/scenarios | Get all scenarios
[**adminScenariosResetPost**](ScenariosApi.md#adminScenariosResetPost) | **POST** /__admin/scenarios/reset | Reset the state of all scenarios



## adminScenariosGet

> AdminScenariosGet200Response adminScenariosGet()

Get all scenarios

### Example

```javascript
import WireMock from 'wire_mock';

let apiInstance = new WireMock.ScenariosApi();
apiInstance.adminScenariosGet((error, data, response) => {
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

[**AdminScenariosGet200Response**](AdminScenariosGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## adminScenariosResetPost

> adminScenariosResetPost()

Reset the state of all scenarios

### Example

```javascript
import WireMock from 'wire_mock';

let apiInstance = new WireMock.ScenariosApi();
apiInstance.adminScenariosResetPost((error, data, response) => {
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

