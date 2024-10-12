# NaviPlanApi.PlanInformationApi

All URIs are relative to *https://demo.uat.naviplancentral.com/plan*

Method | HTTP request | Description
------------- | ------------- | -------------
[**planInformationGetByPlanid**](PlanInformationApi.md#planInformationGetByPlanid) | **GET** /api/PlanInformation | Retrieve plan information



## planInformationGetByPlanid

> PlanInformationModel planInformationGetByPlanid(planId)

Retrieve plan information

This operation retrieves the high level plan information for a given plan

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.PlanInformationApi();
let planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
apiInstance.planInformationGetByPlanid(planId, (error, data, response) => {
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

[**PlanInformationModel**](PlanInformationModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

