# NaviPlanApi.AdvisorsApi

All URIs are relative to *https://demo.uat.naviplancentral.com/plan*

Method | HTTP request | Description
------------- | ------------- | -------------
[**advisorsGet**](AdvisorsApi.md#advisorsGet) | **GET** /api/Advisors | Retrieve Advisors
[**advisorsGetByHouseholdidClientid**](AdvisorsApi.md#advisorsGetByHouseholdidClientid) | **GET** /api/Advisors/{householdId}/{clientId} | Retrieve Advisors for a Client
[**advisorsGetById**](AdvisorsApi.md#advisorsGetById) | **GET** /api/Advisors/{id} | Retrieve an Advisor



## advisorsGet

> AdvisorsModel advisorsGet()

Retrieve Advisors

This operation retrieves a list of all of the Advisors in the plan.

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.AdvisorsApi();
apiInstance.advisorsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**AdvisorsModel**](AdvisorsModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## advisorsGetByHouseholdidClientid

> AdvisorsModel advisorsGetByHouseholdidClientid(householdId, clientId)

Retrieve Advisors for a Client

This operation retrieves a list of all of the Advisors for the client.

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.AdvisorsApi();
let householdId = 56; // Number | Integer id of the household
let clientId = "clientId_example"; // String | Guid id of the client.
apiInstance.advisorsGetByHouseholdidClientid(householdId, clientId, (error, data, response) => {
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
 **householdId** | **Number**| Integer id of the household | 
 **clientId** | **String**| Guid id of the client. | 

### Return type

[**AdvisorsModel**](AdvisorsModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## advisorsGetById

> AdvisorModel advisorsGetById(id)

Retrieve an Advisor

This operation retrieves an Advisor from the plan.

### Example

```javascript
import NaviPlanApi from 'navi_plan_api';

let apiInstance = new NaviPlanApi.AdvisorsApi();
let id = "id_example"; // String | Guid id of the advisor
apiInstance.advisorsGetById(id, (error, data, response) => {
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
 **id** | **String**| Guid id of the advisor | 

### Return type

[**AdvisorModel**](AdvisorModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

