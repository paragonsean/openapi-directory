# NaviPlanApi.ProjectedCashFlowApi

All URIs are relative to *https://demo.uat.naviplancentral.com/plan*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projectedCashFlowGetByIdPlanid**](ProjectedCashFlowApi.md#projectedCashFlowGetByIdPlanid) | **GET** /api/ProjectedCashFlow/{id} | Retrieve projected cash flow by id
[**projectedCashFlowGetByPlanid**](ProjectedCashFlowApi.md#projectedCashFlowGetByPlanid) | **GET** /api/ProjectedCashFlow | Retrieve projected cash flow



## projectedCashFlowGetByIdPlanid

> CashFlowProjectionModel projectedCashFlowGetByIdPlanid(id, planId)

Retrieve projected cash flow by id

This operation retrieves an object containing cash flow information                 for a single specified year of the projected plan.

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.ProjectedCashFlowApi();
let id = 56; // Number | Index into the list of annual projections
let planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
apiInstance.projectedCashFlowGetByIdPlanid(id, planId, (error, data, response) => {
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

[**CashFlowProjectionModel**](CashFlowProjectionModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## projectedCashFlowGetByPlanid

> CashFlowProjectionsModel projectedCashFlowGetByPlanid(planId)

Retrieve projected cash flow

This operation retrieves an object containing cash flow information                 for each year of the projected plan.

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.ProjectedCashFlowApi();
let planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
apiInstance.projectedCashFlowGetByPlanid(planId, (error, data, response) => {
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

[**CashFlowProjectionsModel**](CashFlowProjectionsModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

