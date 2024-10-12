# NaviPlanApi.GoalAdjustmentsApi

All URIs are relative to *https://demo.uat.naviplancentral.com/plan*

Method | HTTP request | Description
------------- | ------------- | -------------
[**goalAdjustmentsGetEducationByIdClientidPlanid**](GoalAdjustmentsApi.md#goalAdjustmentsGetEducationByIdClientidPlanid) | **GET** /api/GoalAdjustments/Education/{id}/Adjustments | Retrieve the adjustments
[**goalAdjustmentsGetGoalAdjustmentRestrictionsByClientidPlanid**](GoalAdjustmentsApi.md#goalAdjustmentsGetGoalAdjustmentRestrictionsByClientidPlanid) | **GET** /api/GoalAdjustments/Restrictions | Returns a list of goal adjustment restrictions.
[**goalAdjustmentsGetGoalSuccessRatesByClientidPlanid**](GoalAdjustmentsApi.md#goalAdjustmentsGetGoalSuccessRatesByClientidPlanid) | **GET** /api/GoalAdjustments/GoalSuccessRates | Returns a list of goals with their relevant success rates.
[**goalAdjustmentsGetMajorPurchaseByIdClientidPlanid**](GoalAdjustmentsApi.md#goalAdjustmentsGetMajorPurchaseByIdClientidPlanid) | **GET** /api/GoalAdjustments/MajorPurchase/{id}/Adjustments | Retrieve the adjustments
[**goalAdjustmentsGetRetirementByClientidPlanid**](GoalAdjustmentsApi.md#goalAdjustmentsGetRetirementByClientidPlanid) | **GET** /api/GoalAdjustments/Retirement/Adjustments | Retrieve the adjustments
[**goalAdjustmentsGetWhatAreMyOptionsByIdClientidPlanid**](GoalAdjustmentsApi.md#goalAdjustmentsGetWhatAreMyOptionsByIdClientidPlanid) | **GET** /api/GoalAdjustments/{id}/WhatAreMyOptions | Returns WAMO values for current goal
[**goalAdjustmentsPostEducationByIdGoaladjustmentsPlanid**](GoalAdjustmentsApi.md#goalAdjustmentsPostEducationByIdGoaladjustmentsPlanid) | **POST** /api/GoalAdjustments/Education/{id}/Calculations | Perform calculations
[**goalAdjustmentsPostMajorPurchaseByIdGoaladjustmentsPlanid**](GoalAdjustmentsApi.md#goalAdjustmentsPostMajorPurchaseByIdGoaladjustmentsPlanid) | **POST** /api/GoalAdjustments/MajorPurchase/{id}/Calculations | Perform calculations
[**goalAdjustmentsPostRetirementByGoaladjustmentsPlanid**](GoalAdjustmentsApi.md#goalAdjustmentsPostRetirementByGoaladjustmentsPlanid) | **POST** /api/GoalAdjustments/Retirement/Calculations | Perform calculations



## goalAdjustmentsGetEducationByIdClientidPlanid

> AdvicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel goalAdjustmentsGetEducationByIdClientidPlanid(id, planId, opts)

Retrieve the adjustments

This function retrieves a goal and the adjustments made to it

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.GoalAdjustmentsApi();
let id = 56; // Number | The id of the goal to retrieve adjustments for.
let planId = "planId_example"; // String | Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
let opts = {
  'clientId': "clientId_example" // String | Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
};
apiInstance.goalAdjustmentsGetEducationByIdClientidPlanid(id, planId, opts, (error, data, response) => {
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
 **id** | **Number**| The id of the goal to retrieve adjustments for. | 
 **planId** | **String**| Id of the Plan to retrieve or update data for (e.g. 1001-11-3). | 
 **clientId** | **String**| Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions. | [optional] 

### Return type

[**AdvicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel**](AdvicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## goalAdjustmentsGetGoalAdjustmentRestrictionsByClientidPlanid

> AdvicentNaviPlanRestApiGoalAdjustmentsModelsRestrictionsResultModel goalAdjustmentsGetGoalAdjustmentRestrictionsByClientidPlanid(planId, opts)

Returns a list of goal adjustment restrictions.

This function returns a list of adjustment restrictions for all goals.

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.GoalAdjustmentsApi();
let planId = "planId_example"; // String | Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
let opts = {
  'clientId': "clientId_example" // String | Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
};
apiInstance.goalAdjustmentsGetGoalAdjustmentRestrictionsByClientidPlanid(planId, opts, (error, data, response) => {
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
 **planId** | **String**| Id of the Plan to retrieve or update data for (e.g. 1001-11-3). | 
 **clientId** | **String**| Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions. | [optional] 

### Return type

[**AdvicentNaviPlanRestApiGoalAdjustmentsModelsRestrictionsResultModel**](AdvicentNaviPlanRestApiGoalAdjustmentsModelsRestrictionsResultModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## goalAdjustmentsGetGoalSuccessRatesByClientidPlanid

> AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateResultsModel goalAdjustmentsGetGoalSuccessRatesByClientidPlanid(planId, opts)

Returns a list of goals with their relevant success rates.

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.GoalAdjustmentsApi();
let planId = "planId_example"; // String | Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
let opts = {
  'clientId': "clientId_example" // String | Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
};
apiInstance.goalAdjustmentsGetGoalSuccessRatesByClientidPlanid(planId, opts, (error, data, response) => {
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
 **planId** | **String**| Id of the Plan to retrieve or update data for (e.g. 1001-11-3). | 
 **clientId** | **String**| Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions. | [optional] 

### Return type

[**AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateResultsModel**](AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateResultsModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## goalAdjustmentsGetMajorPurchaseByIdClientidPlanid

> AdvicentNaviPlanRestApiGoalAdjustmentsModelsMajorPurchaseGoalAdjustmentsModel goalAdjustmentsGetMajorPurchaseByIdClientidPlanid(id, planId, opts)

Retrieve the adjustments

This function retrieves a goal and the adjustments made to it

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.GoalAdjustmentsApi();
let id = 56; // Number | The id of the goal to retrieve adjustments for.
let planId = "planId_example"; // String | Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
let opts = {
  'clientId': "clientId_example" // String | Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
};
apiInstance.goalAdjustmentsGetMajorPurchaseByIdClientidPlanid(id, planId, opts, (error, data, response) => {
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
 **id** | **Number**| The id of the goal to retrieve adjustments for. | 
 **planId** | **String**| Id of the Plan to retrieve or update data for (e.g. 1001-11-3). | 
 **clientId** | **String**| Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions. | [optional] 

### Return type

[**AdvicentNaviPlanRestApiGoalAdjustmentsModelsMajorPurchaseGoalAdjustmentsModel**](AdvicentNaviPlanRestApiGoalAdjustmentsModelsMajorPurchaseGoalAdjustmentsModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## goalAdjustmentsGetRetirementByClientidPlanid

> AdvicentNaviPlanRestApiGoalAdjustmentsModelsRetirementGoalAdjustmentsModel goalAdjustmentsGetRetirementByClientidPlanid(planId, opts)

Retrieve the adjustments

This function retrieves a goal and the adjustments made to it for a particular client

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.GoalAdjustmentsApi();
let planId = "planId_example"; // String | Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
let opts = {
  'clientId': "clientId_example" // String | Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
};
apiInstance.goalAdjustmentsGetRetirementByClientidPlanid(planId, opts, (error, data, response) => {
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
 **planId** | **String**| Id of the Plan to retrieve or update data for (e.g. 1001-11-3). | 
 **clientId** | **String**| Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions. | [optional] 

### Return type

[**AdvicentNaviPlanRestApiGoalAdjustmentsModelsRetirementGoalAdjustmentsModel**](AdvicentNaviPlanRestApiGoalAdjustmentsModelsRetirementGoalAdjustmentsModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## goalAdjustmentsGetWhatAreMyOptionsByIdClientidPlanid

> AdvicentNaviPlanRestApiGoalAdjustmentsModelsWhatAreMyOptionsModel goalAdjustmentsGetWhatAreMyOptionsByIdClientidPlanid(id, planId, opts)

Returns WAMO values for current goal

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.GoalAdjustmentsApi();
let id = 56; // Number | The id of the goal to retrieve WAMO values for.
let planId = "planId_example"; // String | Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
let opts = {
  'clientId': "clientId_example" // String | Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
};
apiInstance.goalAdjustmentsGetWhatAreMyOptionsByIdClientidPlanid(id, planId, opts, (error, data, response) => {
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
 **id** | **Number**| The id of the goal to retrieve WAMO values for. | 
 **planId** | **String**| Id of the Plan to retrieve or update data for (e.g. 1001-11-3). | 
 **clientId** | **String**| Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions. | [optional] 

### Return type

[**AdvicentNaviPlanRestApiGoalAdjustmentsModelsWhatAreMyOptionsModel**](AdvicentNaviPlanRestApiGoalAdjustmentsModelsWhatAreMyOptionsModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## goalAdjustmentsPostEducationByIdGoaladjustmentsPlanid

> AdvicentNaviPlanRestApiGoalAdjustmentsModelsCoverageProjectionsResultModelAdvicentDomainLogicGoalWhatIfEducationGoalAdjustments goalAdjustmentsPostEducationByIdGoaladjustmentsPlanid(id, planId, goalAdjustments)

Perform calculations

This function returns the posted object and the adjusted calculation values

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.GoalAdjustmentsApi();
let id = 56; // Number | The id of the goal to retrieve adjustments for.
let planId = "planId_example"; // String | Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
let goalAdjustments = new NaviPlanApi.AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalAdjustmentsModelAdvicentDomainLogicGoalWhatIfEducationGoalAdjustments(); // AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalAdjustmentsModelAdvicentDomainLogicGoalWhatIfEducationGoalAdjustments | The adjusted values for this goal
apiInstance.goalAdjustmentsPostEducationByIdGoaladjustmentsPlanid(id, planId, goalAdjustments, (error, data, response) => {
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
 **id** | **Number**| The id of the goal to retrieve adjustments for. | 
 **planId** | **String**| Id of the Plan to retrieve or update data for (e.g. 1001-11-3). | 
 **goalAdjustments** | [**AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalAdjustmentsModelAdvicentDomainLogicGoalWhatIfEducationGoalAdjustments**](AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalAdjustmentsModelAdvicentDomainLogicGoalWhatIfEducationGoalAdjustments.md)| The adjusted values for this goal | 

### Return type

[**AdvicentNaviPlanRestApiGoalAdjustmentsModelsCoverageProjectionsResultModelAdvicentDomainLogicGoalWhatIfEducationGoalAdjustments**](AdvicentNaviPlanRestApiGoalAdjustmentsModelsCoverageProjectionsResultModelAdvicentDomainLogicGoalWhatIfEducationGoalAdjustments.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## goalAdjustmentsPostMajorPurchaseByIdGoaladjustmentsPlanid

> AdvicentNaviPlanRestApiGoalAdjustmentsModelsCoverageProjectionsResultModelAdvicentDomainLogicGoalWhatIfMajorPurchaseGoalAdjustments goalAdjustmentsPostMajorPurchaseByIdGoaladjustmentsPlanid(id, planId, goalAdjustments)

Perform calculations

This function returns the posted object and the adjusted calculation values

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.GoalAdjustmentsApi();
let id = 56; // Number | The id of the goal to retrieve adjustments for.
let planId = "planId_example"; // String | Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
let goalAdjustments = new NaviPlanApi.AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalAdjustmentsModelAdvicentDomainLogicGoalWhatIfMajorPurchaseGoalAdjustments(); // AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalAdjustmentsModelAdvicentDomainLogicGoalWhatIfMajorPurchaseGoalAdjustments | The adjusted values for this goal
apiInstance.goalAdjustmentsPostMajorPurchaseByIdGoaladjustmentsPlanid(id, planId, goalAdjustments, (error, data, response) => {
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
 **id** | **Number**| The id of the goal to retrieve adjustments for. | 
 **planId** | **String**| Id of the Plan to retrieve or update data for (e.g. 1001-11-3). | 
 **goalAdjustments** | [**AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalAdjustmentsModelAdvicentDomainLogicGoalWhatIfMajorPurchaseGoalAdjustments**](AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalAdjustmentsModelAdvicentDomainLogicGoalWhatIfMajorPurchaseGoalAdjustments.md)| The adjusted values for this goal | 

### Return type

[**AdvicentNaviPlanRestApiGoalAdjustmentsModelsCoverageProjectionsResultModelAdvicentDomainLogicGoalWhatIfMajorPurchaseGoalAdjustments**](AdvicentNaviPlanRestApiGoalAdjustmentsModelsCoverageProjectionsResultModelAdvicentDomainLogicGoalWhatIfMajorPurchaseGoalAdjustments.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## goalAdjustmentsPostRetirementByGoaladjustmentsPlanid

> AdvicentNaviPlanRestApiGoalAdjustmentsModelsCoverageProjectionsResultModelAdvicentDomainLogicGoalWhatIfRetirementGoalAdjustments goalAdjustmentsPostRetirementByGoaladjustmentsPlanid(planId, goalAdjustments)

Perform calculations

This function returns the posted object and the adjusted calculation values

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.GoalAdjustmentsApi();
let planId = "planId_example"; // String | Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
let goalAdjustments = new NaviPlanApi.AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalAdjustmentsModelAdvicentDomainLogicGoalWhatIfRetirementGoalAdjustments(); // AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalAdjustmentsModelAdvicentDomainLogicGoalWhatIfRetirementGoalAdjustments | The adjusted values for this goal
apiInstance.goalAdjustmentsPostRetirementByGoaladjustmentsPlanid(planId, goalAdjustments, (error, data, response) => {
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
 **planId** | **String**| Id of the Plan to retrieve or update data for (e.g. 1001-11-3). | 
 **goalAdjustments** | [**AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalAdjustmentsModelAdvicentDomainLogicGoalWhatIfRetirementGoalAdjustments**](AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalAdjustmentsModelAdvicentDomainLogicGoalWhatIfRetirementGoalAdjustments.md)| The adjusted values for this goal | 

### Return type

[**AdvicentNaviPlanRestApiGoalAdjustmentsModelsCoverageProjectionsResultModelAdvicentDomainLogicGoalWhatIfRetirementGoalAdjustments**](AdvicentNaviPlanRestApiGoalAdjustmentsModelsCoverageProjectionsResultModelAdvicentDomainLogicGoalWhatIfRetirementGoalAdjustments.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

