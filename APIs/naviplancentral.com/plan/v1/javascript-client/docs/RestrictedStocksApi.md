# NaviPlanApi.RestrictedStocksApi

All URIs are relative to *https://demo.uat.naviplancentral.com/plan*

Method | HTTP request | Description
------------- | ------------- | -------------
[**restrictedStocksGetByIdPlanid**](RestrictedStocksApi.md#restrictedStocksGetByIdPlanid) | **GET** /api/RestrictedStocks/{id} | Retrieve a restricted stock
[**restrictedStocksGetByPlanid**](RestrictedStocksApi.md#restrictedStocksGetByPlanid) | **GET** /api/RestrictedStocks | Retrieve restricted stocks



## restrictedStocksGetByIdPlanid

> RestrictedStockModel restrictedStocksGetByIdPlanid(id, planId)

Retrieve a restricted stock

This operation retrieves a restricted stock from the plan.

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.RestrictedStocksApi();
let id = 56; // Number | ID of restricted stock to retrieve
let planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
apiInstance.restrictedStocksGetByIdPlanid(id, planId, (error, data, response) => {
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
 **id** | **Number**| ID of restricted stock to retrieve | 
 **planId** | **String**| Id of the plan to retrieve data from (e.g. 1001-11-3). | 

### Return type

[**RestrictedStockModel**](RestrictedStockModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## restrictedStocksGetByPlanid

> RestrictedStocksModel restrictedStocksGetByPlanid(planId)

Retrieve restricted stocks

This operation retrieves a list of all of the restricted stocks in the plan.

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.RestrictedStocksApi();
let planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
apiInstance.restrictedStocksGetByPlanid(planId, (error, data, response) => {
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

[**RestrictedStocksModel**](RestrictedStocksModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

