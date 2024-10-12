# NaviPlanApi.AssumptionsApi

All URIs are relative to *https://demo.uat.naviplancentral.com/plan*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assumptionsGetByPlanid**](AssumptionsApi.md#assumptionsGetByPlanid) | **GET** /api/Assumptions | Retrieve plan assumptions



## assumptionsGetByPlanid

> AssumptionsModel assumptionsGetByPlanid(planId)

Retrieve plan assumptions

This operation retrieves an object containing all assumptions for the specified plan.

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.AssumptionsApi();
let planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
apiInstance.assumptionsGetByPlanid(planId, (error, data, response) => {
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

[**AssumptionsModel**](AssumptionsModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

