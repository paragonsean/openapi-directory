# TheWaterLinkedUnderwaterGpsApi.WarningsApi

All URIs are relative to *http://demo.waterlinked.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**warningsGet**](WarningsApi.md#warningsGet) | **GET** /api/v1/warnings/ | Get warnings



## warningsGet

> [WlWarning] warningsGet()

Get warnings

[DEPRECATED] Get current list of messages

### Example

```javascript
import TheWaterLinkedUnderwaterGpsApi from 'the_water_linked_underwater_gps_api';

let apiInstance = new TheWaterLinkedUnderwaterGpsApi.WarningsApi();
apiInstance.warningsGet((error, data, response) => {
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

[**[WlWarning]**](WlWarning.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.waterlinked.operation_response+json, application/vnd.wl.warning+json; type=collection

