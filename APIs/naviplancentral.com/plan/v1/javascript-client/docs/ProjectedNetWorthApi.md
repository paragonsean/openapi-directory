# NaviPlanApi.ProjectedNetWorthApi

All URIs are relative to *https://demo.uat.naviplancentral.com/plan*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projectedNetWorthGetByIdPlanid**](ProjectedNetWorthApi.md#projectedNetWorthGetByIdPlanid) | **GET** /api/ProjectedNetWorth/{id} | Retrieve projected net worth by id
[**projectedNetWorthGetByPlanid**](ProjectedNetWorthApi.md#projectedNetWorthGetByPlanid) | **GET** /api/ProjectedNetWorth | Retrieve projected net worth



## projectedNetWorthGetByIdPlanid

> NetWorthProjectionModel projectedNetWorthGetByIdPlanid(id, planId)

Retrieve projected net worth by id

This operation retrieves an object containing net worth information                 for a single specified year of the projected plan. These are EOY numbers.

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.ProjectedNetWorthApi();
let id = 56; // Number | Index into the list of annual projections
let planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
apiInstance.projectedNetWorthGetByIdPlanid(id, planId, (error, data, response) => {
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
 **id** | **Number**| Index into the list of annual projections | 
 **planId** | **String**| Id of the plan to retrieve data from (e.g. 1001-11-3). | 

### Return type

[**NetWorthProjectionModel**](NetWorthProjectionModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## projectedNetWorthGetByPlanid

> NetWorthProjectionsModel projectedNetWorthGetByPlanid(planId)

Retrieve projected net worth

This operation retrieves an object containing net worth information                 for each year of the projected plan. These are EOY numbers.

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.ProjectedNetWorthApi();
let planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
apiInstance.projectedNetWorthGetByPlanid(planId, (error, data, response) => {
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
 **planId** | **String**| Id of the plan to retrieve data from (e.g. 1001-11-3). | 

### Return type

[**NetWorthProjectionsModel**](NetWorthProjectionsModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

