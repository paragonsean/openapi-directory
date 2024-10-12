# NaviPlanApi.HouseholdsApi

All URIs are relative to *https://demo.uat.naviplancentral.com/plan*

Method | HTTP request | Description
------------- | ------------- | -------------
[**householdsGetByHouseholdid**](HouseholdsApi.md#householdsGetByHouseholdid) | **GET** /api/Households | Retrieve all Households associated with the user



## householdsGetByHouseholdid

> HouseholdsModel householdsGetByHouseholdid(opts)

Retrieve all Households associated with the user

This operation retrieves a list of households the current user has access to or one household specified by a householdId parameter

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.HouseholdsApi();
let opts = {
  'householdId': 56 // Number | The Id of the specific household to retrieve
};
apiInstance.householdsGetByHouseholdid(opts, (error, data, response) => {
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
 **householdId** | **Number**| The Id of the specific household to retrieve | [optional] 

### Return type

[**HouseholdsModel**](HouseholdsModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

