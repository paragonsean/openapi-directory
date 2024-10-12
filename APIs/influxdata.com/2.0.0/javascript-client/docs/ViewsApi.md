# InfluxOssApiService.ViewsApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDashboardsIDCellsIDView_1**](ViewsApi.md#getDashboardsIDCellsIDView_1) | **GET** /dashboards/{dashboardID}/cells/{cellID}/view | Retrieve the view for a cell
[**patchDashboardsIDCellsIDView_1**](ViewsApi.md#patchDashboardsIDCellsIDView_1) | **PATCH** /dashboards/{dashboardID}/cells/{cellID}/view | Update the view for a cell



## getDashboardsIDCellsIDView_1

> View getDashboardsIDCellsIDView_1(dashboardID, cellID, opts)

Retrieve the view for a cell

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.ViewsApi();
let dashboardID = "dashboardID_example"; // String | The dashboard ID.
let cellID = "cellID_example"; // String | The cell ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getDashboardsIDCellsIDView_1(dashboardID, cellID, opts, (error, data, response) => {
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
 **dashboardID** | **String**| The dashboard ID. | 
 **cellID** | **String**| The cell ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**View**](View.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchDashboardsIDCellsIDView_1

> View patchDashboardsIDCellsIDView_1(dashboardID, cellID, view, opts)

Update the view for a cell

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.ViewsApi();
let dashboardID = "dashboardID_example"; // String | The ID of the dashboard to update.
let cellID = "cellID_example"; // String | The ID of the cell to update.
let view = new InfluxOssApiService.View(); // View | 
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.patchDashboardsIDCellsIDView_1(dashboardID, cellID, view, opts, (error, data, response) => {
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
 **dashboardID** | **String**| The ID of the dashboard to update. | 
 **cellID** | **String**| The ID of the cell to update. | 
 **view** | [**View**](View.md)|  | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**View**](View.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

