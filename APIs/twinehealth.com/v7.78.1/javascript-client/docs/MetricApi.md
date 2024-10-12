# FitbitPlusApi.MetricApi

All URIs are relative to *https://api.twinehealth.com/pub*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createPatientHealthMetric**](MetricApi.md#createPatientHealthMetric) | **POST** /patient_health_metric | Create patient health metrics
[**fetchPatientHealthMetric**](MetricApi.md#fetchPatientHealthMetric) | **GET** /patient_health_metric/{id} | Get a patient health metric
[**fetchPatientHealthMetrics**](MetricApi.md#fetchPatientHealthMetrics) | **GET** /patient_health_metric | List patient health metrics



## createPatientHealthMetric

> CreatePatientHealthMetricResponse createPatientHealthMetric(createPatientHealthMetricRequest)

Create patient health metrics

Create one or more patient health metrics.  Example for creating a patient health result with a patient specified using &#x60;meta.query&#x60; instead of &#x60;id&#x60;:  &#x60;&#x60;&#x60;JSON   {     \&quot;data\&quot;: {       \&quot;type\&quot;: \&quot;patient_health_metric\&quot;,        \&quot;attributes\&quot;: {          \&quot;code\&quot;: {            \&quot;system\&quot;: \&quot;LOINC\&quot;,            \&quot;value\&quot;: \&quot;13457-7\&quot;          },          \&quot;type\&quot;: \&quot;ldl_cholesterol\&quot;,          \&quot;occurred_at\&quot;: \&quot;2017-03-14T11:00:57.000Z\&quot;,          \&quot;value\&quot;: 121,          \&quot;unit\&quot;: \&quot;mg/dl\&quot;       },       \&quot;relationships\&quot;: {         \&quot;patient\&quot;: {           \&quot;data\&quot;: {             \&quot;type\&quot;: \&quot;patient\&quot;,             \&quot;meta\&quot;: {               \&quot;query\&quot;: {                 \&quot;identifier\&quot;: {                   \&quot;system\&quot;: \&quot;medical-record-number\&quot;,                   \&quot;value\&quot;: \&quot;121212\&quot;                 },                 \&quot;organization\&quot;: \&quot;58c4554710123c5c40dbab81\&quot;               }             }           }         }       }     }   } &#x60;&#x60;&#x60; 

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.MetricApi();
let createPatientHealthMetricRequest = new FitbitPlusApi.CreatePatientHealthMetricRequest(); // CreatePatientHealthMetricRequest | 
apiInstance.createPatientHealthMetric(createPatientHealthMetricRequest, (error, data, response) => {
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
 **createPatientHealthMetricRequest** | [**CreatePatientHealthMetricRequest**](CreatePatientHealthMetricRequest.md)|  | 

### Return type

[**CreatePatientHealthMetricResponse**](CreatePatientHealthMetricResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/vnd.api+json
- **Accept**: application/vnd.api+json


## fetchPatientHealthMetric

> FetchPatientHealthMetricResponse fetchPatientHealthMetric(id)

Get a patient health metric

Get the plan summary for a patient.

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.MetricApi();
let id = "id_example"; // String | Patient health metric identifier
apiInstance.fetchPatientHealthMetric(id, (error, data, response) => {
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
 **id** | **String**| Patient health metric identifier | 

### Return type

[**FetchPatientHealthMetricResponse**](FetchPatientHealthMetricResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json


## fetchPatientHealthMetrics

> FetchPatientHealthMetricResponse fetchPatientHealthMetrics(opts)

List patient health metrics

Get a list of patient health metrics.

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.MetricApi();
let opts = {
  'filterPatient': "filterPatient_example", // String | Filter the patient health metrics for a specified patient. Note that one of the following filters must be specified: `filter[patient]`, `filter[groups]`, `filter[organization]`. 
  'filterGroups': "filterGroups_example", // String | Comma-separated list of group ids. Note that one of the following filters must be specified: `filter[patient]`, `filter[groups]`, `filter[organization]`. 
  'filterOrganization': "filterOrganization_example", // String | Fitbit Plus organization id. Note that one of the following filters must be specified: `filter[patient]`, `filter[groups]`, `filter[organization]`. 
  'pageNumber': 1, // Number | Page number
  'pageSize': 10, // Number | Page size
  'pageLimit': 50, // Number | Page limit
  'pageCursor': "pageCursor_example" // String | Page cursor
};
apiInstance.fetchPatientHealthMetrics(opts, (error, data, response) => {
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
 **filterPatient** | **String**| Filter the patient health metrics for a specified patient. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;.  | [optional] 
 **filterGroups** | **String**| Comma-separated list of group ids. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;.  | [optional] 
 **filterOrganization** | **String**| Fitbit Plus organization id. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;.  | [optional] 
 **pageNumber** | **Number**| Page number | [optional] [default to 1]
 **pageSize** | **Number**| Page size | [optional] [default to 10]
 **pageLimit** | **Number**| Page limit | [optional] [default to 50]
 **pageCursor** | **String**| Page cursor | [optional] 

### Return type

[**FetchPatientHealthMetricResponse**](FetchPatientHealthMetricResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json

