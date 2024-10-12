# InfluxOssApiService.CellsApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteDashboardsIDCellsID**](CellsApi.md#deleteDashboardsIDCellsID) | **DELETE** /dashboards/{dashboardID}/cells/{cellID} | Delete a dashboard cell
[**getDashboardsIDCellsIDView**](CellsApi.md#getDashboardsIDCellsIDView) | **GET** /dashboards/{dashboardID}/cells/{cellID}/view | Retrieve the view for a cell
[**patchDashboardsIDCellsID**](CellsApi.md#patchDashboardsIDCellsID) | **PATCH** /dashboards/{dashboardID}/cells/{cellID} | Update the non-positional information related to a cell
[**patchDashboardsIDCellsIDView**](CellsApi.md#patchDashboardsIDCellsIDView) | **PATCH** /dashboards/{dashboardID}/cells/{cellID}/view | Update the view for a cell
[**postDashboardsIDCells**](CellsApi.md#postDashboardsIDCells) | **POST** /dashboards/{dashboardID}/cells | Create a dashboard cell
[**putDashboardsIDCells**](CellsApi.md#putDashboardsIDCells) | **PUT** /dashboards/{dashboardID}/cells | Replace cells in a dashboard



## deleteDashboardsIDCellsID

> deleteDashboardsIDCellsID(dashboardID, cellID, opts)

Delete a dashboard cell

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.CellsApi();
let dashboardID = "dashboardID_example"; // String | The ID of the dashboard to delete.
let cellID = "cellID_example"; // String | The ID of the cell to delete.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.deleteDashboardsIDCellsID(dashboardID, cellID, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboardID** | **String**| The ID of the dashboard to delete. | 
 **cellID** | **String**| The ID of the cell to delete. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDashboardsIDCellsIDView

> View getDashboardsIDCellsIDView(dashboardID, cellID, opts)

Retrieve the view for a cell

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.CellsApi();
let dashboardID = "dashboardID_example"; // String | The dashboard ID.
let cellID = "cellID_example"; // String | The cell ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getDashboardsIDCellsIDView(dashboardID, cellID, opts, (error, data, response) => {
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


## patchDashboardsIDCellsID

> Cell patchDashboardsIDCellsID(dashboardID, cellID, cellUpdate, opts)

Update the non-positional information related to a cell

Updates the non positional information related to a cell. Updates to a single cell&#39;s positional data could cause grid conflicts.

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.CellsApi();
let dashboardID = "dashboardID_example"; // String | The ID of the dashboard to update.
let cellID = "cellID_example"; // String | The ID of the cell to update.
let cellUpdate = new InfluxOssApiService.CellUpdate(); // CellUpdate | 
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.patchDashboardsIDCellsID(dashboardID, cellID, cellUpdate, opts, (error, data, response) => {
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
 **cellUpdate** | [**CellUpdate**](CellUpdate.md)|  | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**Cell**](Cell.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## patchDashboardsIDCellsIDView

> View patchDashboardsIDCellsIDView(dashboardID, cellID, view, opts)

Update the view for a cell

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.CellsApi();
let dashboardID = "dashboardID_example"; // String | The ID of the dashboard to update.
let cellID = "cellID_example"; // String | The ID of the cell to update.
let view = new InfluxOssApiService.View(); // View | 
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.patchDashboardsIDCellsIDView(dashboardID, cellID, view, opts, (error, data, response) => {
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


## postDashboardsIDCells

> Cell postDashboardsIDCells(dashboardID, createCell, opts)

Create a dashboard cell

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.CellsApi();
let dashboardID = "dashboardID_example"; // String | The ID of the dashboard to update.
let createCell = new InfluxOssApiService.CreateCell(); // CreateCell | Cell that will be added
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.postDashboardsIDCells(dashboardID, createCell, opts, (error, data, response) => {
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
 **createCell** | [**CreateCell**](CreateCell.md)| Cell that will be added | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**Cell**](Cell.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putDashboardsIDCells

> Dashboard putDashboardsIDCells(dashboardID, cell, opts)

Replace cells in a dashboard

Replaces all cells in a dashboard. This is used primarily to update the positional information of all cells.

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.CellsApi();
let dashboardID = "dashboardID_example"; // String | The ID of the dashboard to update.
let cell = [new InfluxOssApiService.Cell()]; // [Cell] | 
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.putDashboardsIDCells(dashboardID, cell, opts, (error, data, response) => {
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
 **cell** | [**[Cell]**](Cell.md)|  | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

