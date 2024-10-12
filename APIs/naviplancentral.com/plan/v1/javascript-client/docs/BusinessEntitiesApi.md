# NaviPlanApi.BusinessEntitiesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/plan*

Method | HTTP request | Description
------------- | ------------- | -------------
[**businessEntitiesGetByIdPlanid**](BusinessEntitiesApi.md#businessEntitiesGetByIdPlanid) | **GET** /api/BusinessEntities/{id} | Retrieve a business entity
[**businessEntitiesGetByPlanid**](BusinessEntitiesApi.md#businessEntitiesGetByPlanid) | **GET** /api/BusinessEntities | Retrieve business entities



## businessEntitiesGetByIdPlanid

> BusinessEntityModel businessEntitiesGetByIdPlanid(id, planId)

Retrieve a business entity

This operation retrieves a business entity from the plan.

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.BusinessEntitiesApi();
let id = 56; // Number | ID of business entity to retrieve
let planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
apiInstance.businessEntitiesGetByIdPlanid(id, planId, (error, data, response) => {
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
 **id** | **Number**| ID of business entity to retrieve | 
 **planId** | **String**| Id of the plan to retrieve data from (e.g. 1001-11-3). | 

### Return type

[**BusinessEntityModel**](BusinessEntityModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## businessEntitiesGetByPlanid

> BusinessEntitiesModel businessEntitiesGetByPlanid(planId)

Retrieve business entities

This operation retrieves a list of all of the business entities in the plan.

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.BusinessEntitiesApi();
let planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
apiInstance.businessEntitiesGetByPlanid(planId, (error, data, response) => {
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

[**BusinessEntitiesModel**](BusinessEntitiesModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

