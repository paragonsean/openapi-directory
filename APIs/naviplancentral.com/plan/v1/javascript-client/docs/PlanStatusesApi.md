# NaviPlanApi.PlanStatusesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/plan*

Method | HTTP request | Description
------------- | ------------- | -------------
[**planStatusesGetByPlanid**](PlanStatusesApi.md#planStatusesGetByPlanid) | **GET** /api/PlanStatuses | Retrieve plan data statuses



## planStatusesGetByPlanid

> PlanStatusesModel planStatusesGetByPlanid(planId)

Retrieve plan data statuses

This operation retrieves the data statuses of the published plan if on demand updates              are enabled

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.PlanStatusesApi();
let planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3)
apiInstance.planStatusesGetByPlanid(planId, (error, data, response) => {
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
 **planId** | **String**| Id of the plan to retrieve data from (e.g. 1001-11-3) | 

### Return type

[**PlanStatusesModel**](PlanStatusesModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

