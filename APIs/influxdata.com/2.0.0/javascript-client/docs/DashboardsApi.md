# InfluxOssApiService.DashboardsApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteDashboardsID**](DashboardsApi.md#deleteDashboardsID) | **DELETE** /dashboards/{dashboardID} | Delete a dashboard
[**deleteDashboardsIDCellsID_0**](DashboardsApi.md#deleteDashboardsIDCellsID_0) | **DELETE** /dashboards/{dashboardID}/cells/{cellID} | Delete a dashboard cell
[**deleteDashboardsIDLabelsID**](DashboardsApi.md#deleteDashboardsIDLabelsID) | **DELETE** /dashboards/{dashboardID}/labels/{labelID} | Delete a label from a dashboard
[**deleteDashboardsIDMembersID**](DashboardsApi.md#deleteDashboardsIDMembersID) | **DELETE** /dashboards/{dashboardID}/members/{userID} | Remove a member from a dashboard
[**deleteDashboardsIDOwnersID**](DashboardsApi.md#deleteDashboardsIDOwnersID) | **DELETE** /dashboards/{dashboardID}/owners/{userID} | Remove an owner from a dashboard
[**getDashboards**](DashboardsApi.md#getDashboards) | **GET** /dashboards | List all dashboards
[**getDashboardsID**](DashboardsApi.md#getDashboardsID) | **GET** /dashboards/{dashboardID} | Retrieve a Dashboard
[**getDashboardsIDCellsIDView_0**](DashboardsApi.md#getDashboardsIDCellsIDView_0) | **GET** /dashboards/{dashboardID}/cells/{cellID}/view | Retrieve the view for a cell
[**getDashboardsIDLabels**](DashboardsApi.md#getDashboardsIDLabels) | **GET** /dashboards/{dashboardID}/labels | List all labels for a dashboard
[**getDashboardsIDMembers**](DashboardsApi.md#getDashboardsIDMembers) | **GET** /dashboards/{dashboardID}/members | List all dashboard members
[**getDashboardsIDOwners**](DashboardsApi.md#getDashboardsIDOwners) | **GET** /dashboards/{dashboardID}/owners | List all dashboard owners
[**patchDashboardsID**](DashboardsApi.md#patchDashboardsID) | **PATCH** /dashboards/{dashboardID} | Update a dashboard
[**patchDashboardsIDCellsIDView_0**](DashboardsApi.md#patchDashboardsIDCellsIDView_0) | **PATCH** /dashboards/{dashboardID}/cells/{cellID}/view | Update the view for a cell
[**patchDashboardsIDCellsID_0**](DashboardsApi.md#patchDashboardsIDCellsID_0) | **PATCH** /dashboards/{dashboardID}/cells/{cellID} | Update the non-positional information related to a cell
[**postDashboards**](DashboardsApi.md#postDashboards) | **POST** /dashboards | Create a dashboard
[**postDashboardsIDCells_0**](DashboardsApi.md#postDashboardsIDCells_0) | **POST** /dashboards/{dashboardID}/cells | Create a dashboard cell
[**postDashboardsIDLabels**](DashboardsApi.md#postDashboardsIDLabels) | **POST** /dashboards/{dashboardID}/labels | Add a label to a dashboard
[**postDashboardsIDMembers**](DashboardsApi.md#postDashboardsIDMembers) | **POST** /dashboards/{dashboardID}/members | Add a member to a dashboard
[**postDashboardsIDOwners**](DashboardsApi.md#postDashboardsIDOwners) | **POST** /dashboards/{dashboardID}/owners | Add an owner to a dashboard
[**putDashboardsIDCells_0**](DashboardsApi.md#putDashboardsIDCells_0) | **PUT** /dashboards/{dashboardID}/cells | Replace cells in a dashboard



## deleteDashboardsID

> deleteDashboardsID(dashboardID, opts)

Delete a dashboard

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.DashboardsApi();
let dashboardID = "dashboardID_example"; // String | The ID of the dashboard to update.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.deleteDashboardsID(dashboardID, opts, (error, data, response) => {
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
 **dashboardID** | **String**| The ID of the dashboard to update. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteDashboardsIDCellsID_0

> deleteDashboardsIDCellsID_0(dashboardID, cellID, opts)

Delete a dashboard cell

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.DashboardsApi();
let dashboardID = "dashboardID_example"; // String | The ID of the dashboard to delete.
let cellID = "cellID_example"; // String | The ID of the cell to delete.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.deleteDashboardsIDCellsID_0(dashboardID, cellID, opts, (error, data, response) => {
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


## deleteDashboardsIDLabelsID

> deleteDashboardsIDLabelsID(dashboardID, labelID, opts)

Delete a label from a dashboard

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.DashboardsApi();
let dashboardID = "dashboardID_example"; // String | The dashboard ID.
let labelID = "labelID_example"; // String | The ID of the label to delete.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.deleteDashboardsIDLabelsID(dashboardID, labelID, opts, (error, data, response) => {
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
 **dashboardID** | **String**| The dashboard ID. | 
 **labelID** | **String**| The ID of the label to delete. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteDashboardsIDMembersID

> deleteDashboardsIDMembersID(userID, dashboardID, opts)

Remove a member from a dashboard

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.DashboardsApi();
let userID = "userID_example"; // String | The ID of the member to remove.
let dashboardID = "dashboardID_example"; // String | The dashboard ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.deleteDashboardsIDMembersID(userID, dashboardID, opts, (error, data, response) => {
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
 **userID** | **String**| The ID of the member to remove. | 
 **dashboardID** | **String**| The dashboard ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteDashboardsIDOwnersID

> deleteDashboardsIDOwnersID(userID, dashboardID, opts)

Remove an owner from a dashboard

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.DashboardsApi();
let userID = "userID_example"; // String | The ID of the owner to remove.
let dashboardID = "dashboardID_example"; // String | The dashboard ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.deleteDashboardsIDOwnersID(userID, dashboardID, opts, (error, data, response) => {
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
 **userID** | **String**| The ID of the owner to remove. | 
 **dashboardID** | **String**| The dashboard ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDashboards

> Dashboards getDashboards(opts)

List all dashboards

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.DashboardsApi();
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}", // String | OpenTracing span context
  'offset': 56, // Number | 
  'limit': 20, // Number | 
  'descending': false, // Boolean | 
  'owner': "owner_example", // String | A user identifier. Returns only dashboards where this user has the `owner` role.
  'sortBy': "sortBy_example", // String | The column to sort by.
  'id': ["null"], // [String] | A list of dashboard identifiers. Returns only the listed dashboards. If both `id` and `owner` are specified, only `id` is used.
  'orgID': "orgID_example", // String | The identifier of the organization.
  'org': "org_example" // String | The name of the organization.
};
apiInstance.getDashboards(opts, (error, data, response) => {
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
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 
 **offset** | **Number**|  | [optional] 
 **limit** | **Number**|  | [optional] [default to 20]
 **descending** | **Boolean**|  | [optional] [default to false]
 **owner** | **String**| A user identifier. Returns only dashboards where this user has the &#x60;owner&#x60; role. | [optional] 
 **sortBy** | **String**| The column to sort by. | [optional] 
 **id** | [**[String]**](String.md)| A list of dashboard identifiers. Returns only the listed dashboards. If both &#x60;id&#x60; and &#x60;owner&#x60; are specified, only &#x60;id&#x60; is used. | [optional] 
 **orgID** | **String**| The identifier of the organization. | [optional] 
 **org** | **String**| The name of the organization. | [optional] 

### Return type

[**Dashboards**](Dashboards.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDashboardsID

> PostDashboards201Response getDashboardsID(dashboardID, opts)

Retrieve a Dashboard

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.DashboardsApi();
let dashboardID = "dashboardID_example"; // String | The ID of the dashboard to update.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}", // String | OpenTracing span context
  'include': "include_example" // String | Includes the cell view properties in the response if set to `properties`
};
apiInstance.getDashboardsID(dashboardID, opts, (error, data, response) => {
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
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 
 **include** | **String**| Includes the cell view properties in the response if set to &#x60;properties&#x60; | [optional] 

### Return type

[**PostDashboards201Response**](PostDashboards201Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDashboardsIDCellsIDView_0

> View getDashboardsIDCellsIDView_0(dashboardID, cellID, opts)

Retrieve the view for a cell

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.DashboardsApi();
let dashboardID = "dashboardID_example"; // String | The dashboard ID.
let cellID = "cellID_example"; // String | The cell ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getDashboardsIDCellsIDView_0(dashboardID, cellID, opts, (error, data, response) => {
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


## getDashboardsIDLabels

> LabelsResponse getDashboardsIDLabels(dashboardID, opts)

List all labels for a dashboard

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.DashboardsApi();
let dashboardID = "dashboardID_example"; // String | The dashboard ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getDashboardsIDLabels(dashboardID, opts, (error, data, response) => {
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
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**LabelsResponse**](LabelsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDashboardsIDMembers

> ResourceMembers getDashboardsIDMembers(dashboardID, opts)

List all dashboard members

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.DashboardsApi();
let dashboardID = "dashboardID_example"; // String | The dashboard ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getDashboardsIDMembers(dashboardID, opts, (error, data, response) => {
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
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**ResourceMembers**](ResourceMembers.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDashboardsIDOwners

> ResourceOwners getDashboardsIDOwners(dashboardID, opts)

List all dashboard owners

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.DashboardsApi();
let dashboardID = "dashboardID_example"; // String | The dashboard ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getDashboardsIDOwners(dashboardID, opts, (error, data, response) => {
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
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**ResourceOwners**](ResourceOwners.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchDashboardsID

> Dashboard patchDashboardsID(dashboardID, patchDashboardRequest, opts)

Update a dashboard

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.DashboardsApi();
let dashboardID = "dashboardID_example"; // String | The ID of the dashboard to update.
let patchDashboardRequest = new InfluxOssApiService.PatchDashboardRequest(); // PatchDashboardRequest | Patching of a dashboard
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.patchDashboardsID(dashboardID, patchDashboardRequest, opts, (error, data, response) => {
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
 **patchDashboardRequest** | [**PatchDashboardRequest**](PatchDashboardRequest.md)| Patching of a dashboard | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## patchDashboardsIDCellsIDView_0

> View patchDashboardsIDCellsIDView_0(dashboardID, cellID, view, opts)

Update the view for a cell

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.DashboardsApi();
let dashboardID = "dashboardID_example"; // String | The ID of the dashboard to update.
let cellID = "cellID_example"; // String | The ID of the cell to update.
let view = new InfluxOssApiService.View(); // View | 
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.patchDashboardsIDCellsIDView_0(dashboardID, cellID, view, opts, (error, data, response) => {
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


## patchDashboardsIDCellsID_0

> Cell patchDashboardsIDCellsID_0(dashboardID, cellID, cellUpdate, opts)

Update the non-positional information related to a cell

Updates the non positional information related to a cell. Updates to a single cell&#39;s positional data could cause grid conflicts.

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.DashboardsApi();
let dashboardID = "dashboardID_example"; // String | The ID of the dashboard to update.
let cellID = "cellID_example"; // String | The ID of the cell to update.
let cellUpdate = new InfluxOssApiService.CellUpdate(); // CellUpdate | 
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.patchDashboardsIDCellsID_0(dashboardID, cellID, cellUpdate, opts, (error, data, response) => {
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


## postDashboards

> PostDashboards201Response postDashboards(createDashboardRequest, opts)

Create a dashboard

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.DashboardsApi();
let createDashboardRequest = new InfluxOssApiService.CreateDashboardRequest(); // CreateDashboardRequest | Dashboard to create
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.postDashboards(createDashboardRequest, opts, (error, data, response) => {
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
 **createDashboardRequest** | [**CreateDashboardRequest**](CreateDashboardRequest.md)| Dashboard to create | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**PostDashboards201Response**](PostDashboards201Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postDashboardsIDCells_0

> Cell postDashboardsIDCells_0(dashboardID, createCell, opts)

Create a dashboard cell

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.DashboardsApi();
let dashboardID = "dashboardID_example"; // String | The ID of the dashboard to update.
let createCell = new InfluxOssApiService.CreateCell(); // CreateCell | Cell that will be added
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.postDashboardsIDCells_0(dashboardID, createCell, opts, (error, data, response) => {
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


## postDashboardsIDLabels

> LabelResponse postDashboardsIDLabels(dashboardID, labelMapping, opts)

Add a label to a dashboard

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.DashboardsApi();
let dashboardID = "dashboardID_example"; // String | The dashboard ID.
let labelMapping = new InfluxOssApiService.LabelMapping(); // LabelMapping | Label to add
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.postDashboardsIDLabels(dashboardID, labelMapping, opts, (error, data, response) => {
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
 **labelMapping** | [**LabelMapping**](LabelMapping.md)| Label to add | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**LabelResponse**](LabelResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postDashboardsIDMembers

> ResourceMember postDashboardsIDMembers(dashboardID, addResourceMemberRequestBody, opts)

Add a member to a dashboard

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.DashboardsApi();
let dashboardID = "dashboardID_example"; // String | The dashboard ID.
let addResourceMemberRequestBody = new InfluxOssApiService.AddResourceMemberRequestBody(); // AddResourceMemberRequestBody | User to add as member
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.postDashboardsIDMembers(dashboardID, addResourceMemberRequestBody, opts, (error, data, response) => {
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
 **addResourceMemberRequestBody** | [**AddResourceMemberRequestBody**](AddResourceMemberRequestBody.md)| User to add as member | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**ResourceMember**](ResourceMember.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postDashboardsIDOwners

> ResourceOwner postDashboardsIDOwners(dashboardID, addResourceMemberRequestBody, opts)

Add an owner to a dashboard

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.DashboardsApi();
let dashboardID = "dashboardID_example"; // String | The dashboard ID.
let addResourceMemberRequestBody = new InfluxOssApiService.AddResourceMemberRequestBody(); // AddResourceMemberRequestBody | User to add as owner
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.postDashboardsIDOwners(dashboardID, addResourceMemberRequestBody, opts, (error, data, response) => {
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
 **addResourceMemberRequestBody** | [**AddResourceMemberRequestBody**](AddResourceMemberRequestBody.md)| User to add as owner | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**ResourceOwner**](ResourceOwner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putDashboardsIDCells_0

> Dashboard putDashboardsIDCells_0(dashboardID, cell, opts)

Replace cells in a dashboard

Replaces all cells in a dashboard. This is used primarily to update the positional information of all cells.

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.DashboardsApi();
let dashboardID = "dashboardID_example"; // String | The ID of the dashboard to update.
let cell = [new InfluxOssApiService.Cell()]; // [Cell] | 
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.putDashboardsIDCells_0(dashboardID, cell, opts, (error, data, response) => {
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

