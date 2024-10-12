# NaviPlanApi.StockOptionsApi

All URIs are relative to *https://demo.uat.naviplancentral.com/plan*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stockOptionsGetByIdPlanid**](StockOptionsApi.md#stockOptionsGetByIdPlanid) | **GET** /api/StockOptions/{id} | Retrieve a stock option
[**stockOptionsGetByPlanid**](StockOptionsApi.md#stockOptionsGetByPlanid) | **GET** /api/StockOptions | Retrieve stock options



## stockOptionsGetByIdPlanid

> StockOptionModel stockOptionsGetByIdPlanid(id, planId)

Retrieve a stock option

This operation retrieves a stock option from the plan.

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.StockOptionsApi();
let id = 56; // Number | ID of stock option to retrieve
let planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
apiInstance.stockOptionsGetByIdPlanid(id, planId, (error, data, response) => {
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
 **id** | **Number**| ID of stock option to retrieve | 
 **planId** | **String**| Id of the plan to retrieve data from (e.g. 1001-11-3). | 

### Return type

[**StockOptionModel**](StockOptionModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## stockOptionsGetByPlanid

> StockOptionsModel stockOptionsGetByPlanid(planId)

Retrieve stock options

This operation retrieves a list of all of the stock options in the plan.

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.StockOptionsApi();
let planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
apiInstance.stockOptionsGetByPlanid(planId, (error, data, response) => {
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

[**StockOptionsModel**](StockOptionsModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

