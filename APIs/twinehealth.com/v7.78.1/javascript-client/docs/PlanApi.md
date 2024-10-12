# FitbitPlusApi.PlanApi

All URIs are relative to *https://api.twinehealth.com/pub*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchPatientPlanSummaries**](PlanApi.md#fetchPatientPlanSummaries) | **GET** /patient_plan_summary | List patient plan summaries
[**fetchPatientPlanSummary**](PlanApi.md#fetchPatientPlanSummary) | **GET** /patient_plan_summary/{id} | Get the plan summary for a patient
[**updatePatientPlanSummary**](PlanApi.md#updatePatientPlanSummary) | **PATCH** /patient_plan_summary/{id} | Update a plan summary



## fetchPatientPlanSummaries

> FetchPatientPlanSummariesResponse fetchPatientPlanSummaries(opts)

List patient plan summaries

Get a list of patient plan summaries

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.PlanApi();
let opts = {
  'filterPatient': "filterPatient_example", // String | Patient id to fetch plan summary for. Note that one of the following filters must be specified: `filter[patient]`, `filter[groups]`, `filter[organization]`. 
  'filterGroups': "filterGroups_example", // String | Comma-separated list of group ids. Note that one of the following filters must be specified: `filter[patient]`, `filter[groups]`, `filter[organization]`. 
  'filterOrganization': "filterOrganization_example", // String | Fitbit Plus organization id. Note that one of the following filters must be specified: `filter[patient]`, `filter[groups]`, `filter[organization]`. 
  'include': "include_example" // String | List of related resources to include in the response
};
apiInstance.fetchPatientPlanSummaries(opts, (error, data, response) => {
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
 **filterPatient** | **String**| Patient id to fetch plan summary for. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;.  | [optional] 
 **filterGroups** | **String**| Comma-separated list of group ids. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;.  | [optional] 
 **filterOrganization** | **String**| Fitbit Plus organization id. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;.  | [optional] 
 **include** | **String**| List of related resources to include in the response | [optional] 

### Return type

[**FetchPatientPlanSummariesResponse**](FetchPatientPlanSummariesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json


## fetchPatientPlanSummary

> FetchPatientPlanSummaryResponse fetchPatientPlanSummary(id, opts)

Get the plan summary for a patient

Get the plan summary for a patient.

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.PlanApi();
let id = "id_example"; // String | Plan summary identifier
let opts = {
  'include': "include_example" // String | List of related resources to include in the response
};
apiInstance.fetchPatientPlanSummary(id, opts, (error, data, response) => {
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
 **id** | **String**| Plan summary identifier | 
 **include** | **String**| List of related resources to include in the response | [optional] 

### Return type

[**FetchPatientPlanSummaryResponse**](FetchPatientPlanSummaryResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json


## updatePatientPlanSummary

> UpdatePatientPlanSummaryResponse updatePatientPlanSummary(id, updatePatientPlanSummaryRequest)

Update a plan summary

Update a plan summary record for a patient.

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.PlanApi();
let id = "id_example"; // String | Plan summary identifier
let updatePatientPlanSummaryRequest = new FitbitPlusApi.UpdatePatientPlanSummaryRequest(); // UpdatePatientPlanSummaryRequest | 
apiInstance.updatePatientPlanSummary(id, updatePatientPlanSummaryRequest, (error, data, response) => {
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
 **id** | **String**| Plan summary identifier | 
 **updatePatientPlanSummaryRequest** | [**UpdatePatientPlanSummaryRequest**](UpdatePatientPlanSummaryRequest.md)|  | 

### Return type

[**UpdatePatientPlanSummaryResponse**](UpdatePatientPlanSummaryResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/vnd.api+json
- **Accept**: application/vnd.api+json

