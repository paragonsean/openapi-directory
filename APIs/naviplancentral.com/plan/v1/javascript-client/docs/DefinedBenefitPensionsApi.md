# NaviPlanApi.DefinedBenefitPensionsApi

All URIs are relative to *https://demo.uat.naviplancentral.com/plan*

Method | HTTP request | Description
------------- | ------------- | -------------
[**definedBenefitPensionsGetByIdPlanid**](DefinedBenefitPensionsApi.md#definedBenefitPensionsGetByIdPlanid) | **GET** /api/DefinedBenefitPensions/{id} | Retrieve a definedBenefitPension
[**definedBenefitPensionsGetByPlanid**](DefinedBenefitPensionsApi.md#definedBenefitPensionsGetByPlanid) | **GET** /api/DefinedBenefitPensions | Retrieve defined benefit pensions



## definedBenefitPensionsGetByIdPlanid

> DefinedBenefitPensionModel definedBenefitPensionsGetByIdPlanid(id, planId)

Retrieve a definedBenefitPension

This operation retrieves a defined benefit pension from the plan.

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.DefinedBenefitPensionsApi();
let id = 56; // Number | ID of defined benefit pension to retrieve
let planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
apiInstance.definedBenefitPensionsGetByIdPlanid(id, planId, (error, data, response) => {
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
 **id** | **Number**| ID of defined benefit pension to retrieve | 
 **planId** | **String**| Id of the plan to retrieve data from (e.g. 1001-11-3). | 

### Return type

[**DefinedBenefitPensionModel**](DefinedBenefitPensionModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## definedBenefitPensionsGetByPlanid

> DefinedBenefitPensionsModel definedBenefitPensionsGetByPlanid(planId)

Retrieve defined benefit pensions

This operation retrieves a list of all of the defined benefit pensions in the plan.

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.DefinedBenefitPensionsApi();
let planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
apiInstance.definedBenefitPensionsGetByPlanid(planId, (error, data, response) => {
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

[**DefinedBenefitPensionsModel**](DefinedBenefitPensionsModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

