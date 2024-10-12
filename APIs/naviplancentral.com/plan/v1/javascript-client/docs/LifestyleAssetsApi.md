# NaviPlanApi.LifestyleAssetsApi

All URIs are relative to *https://demo.uat.naviplancentral.com/plan*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lifestyleAssetsGetByIdPlanid**](LifestyleAssetsApi.md#lifestyleAssetsGetByIdPlanid) | **GET** /api/LifestyleAssets/{id} | Retrieve lifestyle assets
[**lifestyleAssetsGetByPlanid**](LifestyleAssetsApi.md#lifestyleAssetsGetByPlanid) | **GET** /api/LifestyleAssets | Retrieve lifestyle assets



## lifestyleAssetsGetByIdPlanid

> LifestyleAssetModel lifestyleAssetsGetByIdPlanid(id, planId)

Retrieve lifestyle assets

This operation retrieves a lifestyle asset from the plan.

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.LifestyleAssetsApi();
let id = 56; // Number | ID of lifestyle asset to retrieve
let planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
apiInstance.lifestyleAssetsGetByIdPlanid(id, planId, (error, data, response) => {
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
 **id** | **Number**| ID of lifestyle asset to retrieve | 
 **planId** | **String**| Id of the plan to retrieve data from (e.g. 1001-11-3). | 

### Return type

[**LifestyleAssetModel**](LifestyleAssetModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## lifestyleAssetsGetByPlanid

> LifestyleAssetsModel lifestyleAssetsGetByPlanid(planId)

Retrieve lifestyle assets

This operation retrieves a list of all of the lifestyle assets in the plan.

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.LifestyleAssetsApi();
let planId = "planId_example"; // String | Id of the plan to retrieve data from (e.g. 1001-11-3).
apiInstance.lifestyleAssetsGetByPlanid(planId, (error, data, response) => {
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

[**LifestyleAssetsModel**](LifestyleAssetsModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

