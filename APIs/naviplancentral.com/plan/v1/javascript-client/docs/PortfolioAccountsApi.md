# NaviPlanApi.PortfolioAccountsApi

All URIs are relative to *https://demo.uat.naviplancentral.com/plan*

Method | HTTP request | Description
------------- | ------------- | -------------
[**portfolioAccountsGetByIdPlanid**](PortfolioAccountsApi.md#portfolioAccountsGetByIdPlanid) | **GET** /api/PortfolioAccounts/{id} | Retrieve a portfolio account
[**portfolioAccountsGetByPlanid**](PortfolioAccountsApi.md#portfolioAccountsGetByPlanid) | **GET** /api/PortfolioAccounts | Retrieve portfolio accounts



## portfolioAccountsGetByIdPlanid

> PortfolioAccountModel portfolioAccountsGetByIdPlanid(id, planId)

Retrieve a portfolio account

This operation retrieves a portfolio account from the plan.

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.PortfolioAccountsApi();
let id = 56; // Number | ID of portfolio account to retrieve
let planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
apiInstance.portfolioAccountsGetByIdPlanid(id, planId, (error, data, response) => {
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
 **id** | **Number**| ID of portfolio account to retrieve | 
 **planId** | **String**| Id of the plan to retrieve data from (e.g. 1001-11-3). | 

### Return type

[**PortfolioAccountModel**](PortfolioAccountModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## portfolioAccountsGetByPlanid

> PortfolioAccountsModel portfolioAccountsGetByPlanid(planId)

Retrieve portfolio accounts

This operation retrieves a list of all of the portfolio accounts in the plan.

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.PortfolioAccountsApi();
let planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
apiInstance.portfolioAccountsGetByPlanid(planId, (error, data, response) => {
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

[**PortfolioAccountsModel**](PortfolioAccountsModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

