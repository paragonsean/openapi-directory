# NaviPlanApi.ProjectedAnnualSummaryApi

All URIs are relative to *https://demo.uat.naviplancentral.com/plan*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projectedAnnualSummaryGetByIdPlanid**](ProjectedAnnualSummaryApi.md#projectedAnnualSummaryGetByIdPlanid) | **GET** /api/ProjectedAnnualSummary/{id} | Retrieve projected annual summary by id
[**projectedAnnualSummaryGetByPlanid**](ProjectedAnnualSummaryApi.md#projectedAnnualSummaryGetByPlanid) | **GET** /api/ProjectedAnnualSummary | Retrieve projected annual summaries



## projectedAnnualSummaryGetByIdPlanid

> ProjectedAnnualSummaryModel projectedAnnualSummaryGetByIdPlanid(id, planId)

Retrieve projected annual summary by id

This operation retrieves an object containing annual summary information                 for a single specified year of the projected plan.

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.ProjectedAnnualSummaryApi();
let id = 56; // Number | Index into the list of annual projections
let planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
apiInstance.projectedAnnualSummaryGetByIdPlanid(id, planId, (error, data, response) => {
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

[**ProjectedAnnualSummaryModel**](ProjectedAnnualSummaryModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## projectedAnnualSummaryGetByPlanid

> ProjectedAnnualSummariesModel projectedAnnualSummaryGetByPlanid(planId)

Retrieve projected annual summaries

This operation retrieves an object containing annual summary information                 for each year of the projected plan.

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.ProjectedAnnualSummaryApi();
let planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
apiInstance.projectedAnnualSummaryGetByPlanid(planId, (error, data, response) => {
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

[**ProjectedAnnualSummariesModel**](ProjectedAnnualSummariesModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

