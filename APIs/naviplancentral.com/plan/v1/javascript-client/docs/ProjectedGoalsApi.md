# NaviPlanApi.ProjectedGoalsApi

All URIs are relative to *https://demo.uat.naviplancentral.com/plan*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projectedGoalsGetAssetsFundingGoalsByPlanid**](ProjectedGoalsApi.md#projectedGoalsGetAssetsFundingGoalsByPlanid) | **GET** /api/ProjectedGoals/AssetsFundingGoals | Retrieve assets funding goals over time
[**projectedGoalsGetNeedsVsAbilitiesByPlanid**](ProjectedGoalsApi.md#projectedGoalsGetNeedsVsAbilitiesByPlanid) | **GET** /api/ProjectedGoals/NeedsVsAbilities | Retrieve needs vs abilities data



## projectedGoalsGetAssetsFundingGoalsByPlanid

> AssetsFundingGoalModel projectedGoalsGetAssetsFundingGoalsByPlanid(planId)

Retrieve assets funding goals over time

This operation retrieves the assets funding each goal throughout the plan years

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.ProjectedGoalsApi();
let planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
apiInstance.projectedGoalsGetAssetsFundingGoalsByPlanid(planId, (error, data, response) => {
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

[**AssetsFundingGoalModel**](AssetsFundingGoalModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## projectedGoalsGetNeedsVsAbilitiesByPlanid

> NeedsVsAbilitiesModel projectedGoalsGetNeedsVsAbilitiesByPlanid(planId)

Retrieve needs vs abilities data

This operation retrieves a needs and abilities data for all goals throughout                the plan years.

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.ProjectedGoalsApi();
let planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
apiInstance.projectedGoalsGetNeedsVsAbilitiesByPlanid(planId, (error, data, response) => {
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

[**NeedsVsAbilitiesModel**](NeedsVsAbilitiesModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

