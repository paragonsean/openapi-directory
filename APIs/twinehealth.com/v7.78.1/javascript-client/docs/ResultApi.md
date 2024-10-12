# FitbitPlusApi.ResultApi

All URIs are relative to *https://api.twinehealth.com/pub*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchPatientHealthResult**](ResultApi.md#fetchPatientHealthResult) | **GET** /result/{id} | Get a patient health result
[**fetchPatientHealthResults**](ResultApi.md#fetchPatientHealthResults) | **GET** /result | List patient health results



## fetchPatientHealthResult

> FetchPatientHealthResultResponse fetchPatientHealthResult(id)

Get a patient health result

Get patient health result by id.

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.ResultApi();
let id = "id_example"; // String | Patient health result identifier
apiInstance.fetchPatientHealthResult(id, (error, data, response) => {
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
 **id** | **String**| Patient health result identifier | 

### Return type

[**FetchPatientHealthResultResponse**](FetchPatientHealthResultResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json


## fetchPatientHealthResults

> FetchPatientHealthResultResponse fetchPatientHealthResults(filterPatient, opts)

List patient health results

Get a list of patient health results.

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.ResultApi();
let filterPatient = "filterPatient_example"; // String | Filter the patient health results for a specified patient
let opts = {
  'filterActions': "filterActions_example", // String | A comma-separated list of action identifiers
  'filterStartAt': "filterStartAt_example", // String | Filter results that occurred after the passed ISO date and time string
  'filterEndAt': "filterEndAt_example", // String | Filter results that occurred before the passed ISO date and time string
  'filterThreads': "filterThreads_example", // String | A comma-separated list of thread identifiers
  'filterCreatedAt': "filterCreatedAt_example", // String | The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by `..`. Example for results created in November 2017 (America/New_York): `filter[created_at]=2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00` 
  'filterUpdatedAt': "filterUpdatedAt_example", // String | The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by `..`. Example for results updated in November 2017 (America/New_York): `filter[updated_at]=2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00` 
  'pageNumber': 1, // Number | Page number
  'pageSize': 10, // Number | Page size
  'pageLimit': 50, // Number | Page limit
  'pageAfter': "pageAfter_example" // String | Page cursor
};
apiInstance.fetchPatientHealthResults(filterPatient, opts, (error, data, response) => {
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
 **filterPatient** | **String**| Filter the patient health results for a specified patient | 
 **filterActions** | **String**| A comma-separated list of action identifiers | [optional] 
 **filterStartAt** | **String**| Filter results that occurred after the passed ISO date and time string | [optional] 
 **filterEndAt** | **String**| Filter results that occurred before the passed ISO date and time string | [optional] 
 **filterThreads** | **String**| A comma-separated list of thread identifiers | [optional] 
 **filterCreatedAt** | **String**| The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by &#x60;..&#x60;. Example for results created in November 2017 (America/New_York): &#x60;filter[created_at]&#x3D;2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00&#x60;  | [optional] 
 **filterUpdatedAt** | **String**| The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by &#x60;..&#x60;. Example for results updated in November 2017 (America/New_York): &#x60;filter[updated_at]&#x3D;2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00&#x60;  | [optional] 
 **pageNumber** | **Number**| Page number | [optional] [default to 1]
 **pageSize** | **Number**| Page size | [optional] [default to 10]
 **pageLimit** | **Number**| Page limit | [optional] [default to 50]
 **pageAfter** | **String**| Page cursor | [optional] 

### Return type

[**FetchPatientHealthResultResponse**](FetchPatientHealthResultResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json

