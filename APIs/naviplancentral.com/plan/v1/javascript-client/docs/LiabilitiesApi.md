# NaviPlanApi.LiabilitiesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/plan*

Method | HTTP request | Description
------------- | ------------- | -------------
[**liabilitiesGetByIdPlanid**](LiabilitiesApi.md#liabilitiesGetByIdPlanid) | **GET** /api/Liabilities/{id} | Retrieve a liability
[**liabilitiesGetByPlanid**](LiabilitiesApi.md#liabilitiesGetByPlanid) | **GET** /api/Liabilities | Retrieve liabilities



## liabilitiesGetByIdPlanid

> LiabilityModel liabilitiesGetByIdPlanid(id, planId)

Retrieve a liability

This operation retrieves a liability from the plan.

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.LiabilitiesApi();
let id = 56; // Number | ID of liability to retrieve
let planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
apiInstance.liabilitiesGetByIdPlanid(id, planId, (error, data, response) => {
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
 **id** | **Number**| ID of liability to retrieve | 
 **planId** | **String**| Id of the plan to retrieve data from (e.g. 1001-11-3). | 

### Return type

[**LiabilityModel**](LiabilityModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## liabilitiesGetByPlanid

> LiabilitiesModel liabilitiesGetByPlanid(planId)

Retrieve liabilities

This operation retrieves a list of all of the liabilities in the plan.

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.LiabilitiesApi();
let planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
apiInstance.liabilitiesGetByPlanid(planId, (error, data, response) => {
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

[**LiabilitiesModel**](LiabilitiesModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

