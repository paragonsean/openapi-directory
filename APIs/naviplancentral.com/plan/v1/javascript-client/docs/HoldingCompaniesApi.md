# NaviPlanApi.HoldingCompaniesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/plan*

Method | HTTP request | Description
------------- | ------------- | -------------
[**holdingCompaniesGetByIdPlanid**](HoldingCompaniesApi.md#holdingCompaniesGetByIdPlanid) | **GET** /api/HoldingCompanies/{id} | Retrieve a holding company
[**holdingCompaniesGetByPlanid**](HoldingCompaniesApi.md#holdingCompaniesGetByPlanid) | **GET** /api/HoldingCompanies | Retrieve holding companies



## holdingCompaniesGetByIdPlanid

> HoldingCompanyModel holdingCompaniesGetByIdPlanid(id, planId)

Retrieve a holding company

This operation retrieves a holding company from the plan.

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.HoldingCompaniesApi();
let id = 56; // Number | ID of holding company to retrieve
let planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
apiInstance.holdingCompaniesGetByIdPlanid(id, planId, (error, data, response) => {
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
 **id** | **Number**| ID of holding company to retrieve | 
 **planId** | **String**| Id of the plan to retrieve data from (e.g. 1001-11-3). | 

### Return type

[**HoldingCompanyModel**](HoldingCompanyModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## holdingCompaniesGetByPlanid

> HoldingCompaniesModel holdingCompaniesGetByPlanid(planId)

Retrieve holding companies

This operation retrieves a list of all of the holding companies in the plan.

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.HoldingCompaniesApi();
let planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
apiInstance.holdingCompaniesGetByPlanid(planId, (error, data, response) => {
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

[**HoldingCompaniesModel**](HoldingCompaniesModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

