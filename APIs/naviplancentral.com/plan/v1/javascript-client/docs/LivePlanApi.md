# NaviPlanApi.LivePlanApi

All URIs are relative to *https://demo.uat.naviplancentral.com/plan*

Method | HTTP request | Description
------------- | ------------- | -------------
[**livePlanGetAccountsByClientidPlanid**](LivePlanApi.md#livePlanGetAccountsByClientidPlanid) | **GET** /api/LivePlan/NetWorth/Accounts | Retrieves accounts for a given plan
[**livePlanGetGoalFundingListByClientidPlanid**](LivePlanApi.md#livePlanGetGoalFundingListByClientidPlanid) | **GET** /api/LivePlan/Goals/Funding | Retrieve a list of funding accounts
[**livePlanGetGoalsByClientidPlanid**](LivePlanApi.md#livePlanGetGoalsByClientidPlanid) | **GET** /api/LivePlan/Goals | Retrieves all goals from the live plan
[**livePlanGetLiabilitiesByClientidPlanid**](LivePlanApi.md#livePlanGetLiabilitiesByClientidPlanid) | **GET** /api/LivePlan/NetWorth/Liabilities | Retrieves liabilities for a given plan
[**livePlanGetLifestyleAssetsByClientidPlanid**](LivePlanApi.md#livePlanGetLifestyleAssetsByClientidPlanid) | **GET** /api/LivePlan/NetWorth/LifestyleAssets | Retrieves lifestyle assets for a given plan
[**livePlanGetProjectedNeedsVsAbilitiesByIdClientidPlanid**](LivePlanApi.md#livePlanGetProjectedNeedsVsAbilitiesByIdClientidPlanid) | **GET** /api/LivePlan/Projections/{id}/NeedsVsAbilities | Retrieves needs vs abilities projections
[**livePlanGetProjectedNetWorthByClientidPlanid**](LivePlanApi.md#livePlanGetProjectedNetWorthByClientidPlanid) | **GET** /api/LivePlan/Projections/NetWorth | Retrieves net worth projections
[**livePlanGetRealEstateAssetsByClientidPlanid**](LivePlanApi.md#livePlanGetRealEstateAssetsByClientidPlanid) | **GET** /api/LivePlan/NetWorth/RealEstate | Retrieves real estate accounts for a given plan
[**livePlanGetWhatAreMyOptionsByIdClientidPlanid**](LivePlanApi.md#livePlanGetWhatAreMyOptionsByIdClientidPlanid) | **GET** /api/LivePlan/Goals/{id}/WhatAreMyOptions | Retrieve WAMO values for a given goal



## livePlanGetAccountsByClientidPlanid

> AdvicentNaviPlanRestApiNetWorthModelsAccountBaseModel livePlanGetAccountsByClientidPlanid(planId, opts)

Retrieves accounts for a given plan

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.LivePlanApi();
let planId = "planId_example"; // String | Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
let opts = {
  'clientId': "clientId_example" // String | Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
};
apiInstance.livePlanGetAccountsByClientidPlanid(planId, opts, (error, data, response) => {
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

[**AdvicentNaviPlanRestApiNetWorthModelsAccountBaseModel**](AdvicentNaviPlanRestApiNetWorthModelsAccountBaseModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## livePlanGetGoalFundingListByClientidPlanid

> AdvicentNaviPlanRestApiGoalsModelsGoalFundingListModel livePlanGetGoalFundingListByClientidPlanid(planId, opts)

Retrieve a list of funding accounts

This function retrieves a list of funding accounts for the goals in the plan

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.LivePlanApi();
let planId = "planId_example"; // String | Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
let opts = {
  'clientId': "clientId_example" // String | Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
};
apiInstance.livePlanGetGoalFundingListByClientidPlanid(planId, opts, (error, data, response) => {
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

[**AdvicentNaviPlanRestApiGoalsModelsGoalFundingListModel**](AdvicentNaviPlanRestApiGoalsModelsGoalFundingListModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## livePlanGetGoalsByClientidPlanid

> AdvicentNaviPlanRestApiGoalsModelsLiveGoalBaseModel livePlanGetGoalsByClientidPlanid(planId, opts)

Retrieves all goals from the live plan

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.LivePlanApi();
let planId = "planId_example"; // String | Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
let opts = {
  'clientId': "clientId_example" // String | Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
};
apiInstance.livePlanGetGoalsByClientidPlanid(planId, opts, (error, data, response) => {
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

[**AdvicentNaviPlanRestApiGoalsModelsLiveGoalBaseModel**](AdvicentNaviPlanRestApiGoalsModelsLiveGoalBaseModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## livePlanGetLiabilitiesByClientidPlanid

> AdvicentNaviPlanRestApiNetWorthModelsLiabilityBaseModel livePlanGetLiabilitiesByClientidPlanid(planId, opts)

Retrieves liabilities for a given plan

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.LivePlanApi();
let planId = "planId_example"; // String | Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
let opts = {
  'clientId': "clientId_example" // String | Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
};
apiInstance.livePlanGetLiabilitiesByClientidPlanid(planId, opts, (error, data, response) => {
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

[**AdvicentNaviPlanRestApiNetWorthModelsLiabilityBaseModel**](AdvicentNaviPlanRestApiNetWorthModelsLiabilityBaseModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## livePlanGetLifestyleAssetsByClientidPlanid

> AdvicentNaviPlanRestApiNetWorthModelsLifestyleAssetBaseModel livePlanGetLifestyleAssetsByClientidPlanid(planId, opts)

Retrieves lifestyle assets for a given plan

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.LivePlanApi();
let planId = "planId_example"; // String | Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
let opts = {
  'clientId': "clientId_example" // String | Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
};
apiInstance.livePlanGetLifestyleAssetsByClientidPlanid(planId, opts, (error, data, response) => {
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

[**AdvicentNaviPlanRestApiNetWorthModelsLifestyleAssetBaseModel**](AdvicentNaviPlanRestApiNetWorthModelsLifestyleAssetBaseModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## livePlanGetProjectedNeedsVsAbilitiesByIdClientidPlanid

> AdvicentNaviPlanRestApiProjectionsModelsNeedsVsAbilitiesProjectionsModel livePlanGetProjectedNeedsVsAbilitiesByIdClientidPlanid(id, planId, opts)

Retrieves needs vs abilities projections

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.LivePlanApi();
let id = 56; // Number | 
let planId = "planId_example"; // String | Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
let opts = {
  'clientId': "clientId_example" // String | Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
};
apiInstance.livePlanGetProjectedNeedsVsAbilitiesByIdClientidPlanid(id, planId, opts, (error, data, response) => {
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
 **id** | **Number**|  | 
 **planId** | **String**| Id of the Plan to retrieve or update data for (e.g. 1001-11-3). | 
 **clientId** | **String**| Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions. | [optional] 

### Return type

[**AdvicentNaviPlanRestApiProjectionsModelsNeedsVsAbilitiesProjectionsModel**](AdvicentNaviPlanRestApiProjectionsModelsNeedsVsAbilitiesProjectionsModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## livePlanGetProjectedNetWorthByClientidPlanid

> AdvicentNaviPlanRestApiProjectionsModelsNetWorthProjectionsModel livePlanGetProjectedNetWorthByClientidPlanid(planId, opts)

Retrieves net worth projections

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.LivePlanApi();
let planId = "planId_example"; // String | Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
let opts = {
  'clientId': "clientId_example" // String | Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
};
apiInstance.livePlanGetProjectedNetWorthByClientidPlanid(planId, opts, (error, data, response) => {
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

[**AdvicentNaviPlanRestApiProjectionsModelsNetWorthProjectionsModel**](AdvicentNaviPlanRestApiProjectionsModelsNetWorthProjectionsModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## livePlanGetRealEstateAssetsByClientidPlanid

> AdvicentNaviPlanRestApiNetWorthModelsRealEstateBaseModel livePlanGetRealEstateAssetsByClientidPlanid(planId, opts)

Retrieves real estate accounts for a given plan

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.LivePlanApi();
let planId = "planId_example"; // String | Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
let opts = {
  'clientId': "clientId_example" // String | Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
};
apiInstance.livePlanGetRealEstateAssetsByClientidPlanid(planId, opts, (error, data, response) => {
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

[**AdvicentNaviPlanRestApiNetWorthModelsRealEstateBaseModel**](AdvicentNaviPlanRestApiNetWorthModelsRealEstateBaseModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## livePlanGetWhatAreMyOptionsByIdClientidPlanid

> AdvicentNaviPlanRestApiGoalAdjustmentsModelsWhatAreMyOptionsModel livePlanGetWhatAreMyOptionsByIdClientidPlanid(id, planId, opts)

Retrieve WAMO values for a given goal

This function retrieves the WAMO values for the specified goal

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.LivePlanApi();
let id = 56; // Number | The id of the goal
let planId = "planId_example"; // String | Id of the Plan to retrieve or update data for (e.g. 1001-11-3).
let opts = {
  'clientId': "clientId_example" // String | Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions.
};
apiInstance.livePlanGetWhatAreMyOptionsByIdClientidPlanid(id, planId, opts, (error, data, response) => {
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
 **id** | **Number**| The id of the goal | 
 **planId** | **String**| Id of the Plan to retrieve or update data for (e.g. 1001-11-3). | 
 **clientId** | **String**| Id of the client user for the plan. Required if current session user is an advisor. Ignored for client user sessions. | [optional] 

### Return type

[**AdvicentNaviPlanRestApiGoalAdjustmentsModelsWhatAreMyOptionsModel**](AdvicentNaviPlanRestApiGoalAdjustmentsModelsWhatAreMyOptionsModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

