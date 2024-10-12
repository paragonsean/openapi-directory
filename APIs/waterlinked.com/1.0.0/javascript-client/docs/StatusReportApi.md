# TheWaterLinkedUnderwaterGpsApi.StatusReportApi

All URIs are relative to *http://demo.waterlinked.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**statusReportGet**](StatusReportApi.md#statusReportGet) | **GET** /api/v1/status_report/ | Get status_report



## statusReportGet

> [WlStatusGroup] statusReportGet()

Get status_report

Get list of status reports from all status groups

### Example

```javascript
import TheWaterLinkedUnderwaterGpsApi from 'the_water_linked_underwater_gps_api';

let apiInstance = new TheWaterLinkedUnderwaterGpsApi.StatusReportApi();
apiInstance.statusReportGet((error, data, response) => {
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

[**[WlStatusGroup]**](WlStatusGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.wl.status.group+json; type=collection

