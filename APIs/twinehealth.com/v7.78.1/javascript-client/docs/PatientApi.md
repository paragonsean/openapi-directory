# FitbitPlusApi.PatientApi

All URIs are relative to *https://api.twinehealth.com/pub*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createPatient**](PatientApi.md#createPatient) | **POST** /patient | Create a patient
[**fetchPatient**](PatientApi.md#fetchPatient) | **GET** /patient/{id} | Get a patient
[**fetchPatientCoaches**](PatientApi.md#fetchPatientCoaches) | **GET** /patient/{id}/coaches | List coaches for a patient
[**fetchPatientGroups**](PatientApi.md#fetchPatientGroups) | **GET** /patient/{id}/groups | List groups for a patient
[**fetchPatients**](PatientApi.md#fetchPatients) | **GET** /patient | List patients
[**updatePatient**](PatientApi.md#updatePatient) | **PATCH** /patient/{id} | Update a patient
[**upsertPatient**](PatientApi.md#upsertPatient) | **PUT** /patient | Upsert patient



## createPatient

> CreatePatientResponse createPatient(createPatientRequest)

Create a patient

Create a patient record.  Example for creating a patient with a group specified using &#x60;meta.query&#x60; instead of &#x60;id&#x60;:  &#x60;&#x60;&#x60;JSON {   \&quot;data\&quot;: {     \&quot;type\&quot;: \&quot;patient\&quot;,     \&quot;attributes\&quot;: {       \&quot;first_name\&quot;: \&quot;Andrew\&quot;,       \&quot;last_name\&quot;: \&quot;Smith\&quot;     },     \&quot;relationships\&quot;: {       \&quot;groups\&quot;: {         \&quot;data\&quot;: [           {             \&quot;type\&quot;: \&quot;group\&quot;,             \&quot;meta\&quot;: {               \&quot;query\&quot;: {                 \&quot;organization\&quot;: \&quot;58c88de7c93eb96357a87033\&quot;,                 \&quot;name\&quot;: \&quot;Patients Lead\&quot;               }             }           }         ]       }     }   } } &#x60;&#x60;&#x60; 

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.PatientApi();
let createPatientRequest = new FitbitPlusApi.CreatePatientRequest(); // CreatePatientRequest | 
apiInstance.createPatient(createPatientRequest, (error, data, response) => {
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
 **createPatientRequest** | [**CreatePatientRequest**](CreatePatientRequest.md)|  | 

### Return type

[**CreatePatientResponse**](CreatePatientResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/vnd.api+json
- **Accept**: application/vnd.api+json


## fetchPatient

> FetchPatientResponse fetchPatient(id)

Get a patient

Gets a patient record by id.

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.PatientApi();
let id = "id_example"; // String | Patient identifier
apiInstance.fetchPatient(id, (error, data, response) => {
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
 **id** | **String**| Patient identifier | 

### Return type

[**FetchPatientResponse**](FetchPatientResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json


## fetchPatientCoaches

> FetchCoachesResponse fetchPatientCoaches(id)

List coaches for a patient

Get the list of coaches for a patient.

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.PatientApi();
let id = "id_example"; // String | Patient identifier
apiInstance.fetchPatientCoaches(id, (error, data, response) => {
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
 **id** | **String**| Patient identifier | 

### Return type

[**FetchCoachesResponse**](FetchCoachesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json


## fetchPatientGroups

> FetchGroupsResponse fetchPatientGroups(id)

List groups for a patient

Get the list of groups for a patient.

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.PatientApi();
let id = "id_example"; // String | Patient identifier
apiInstance.fetchPatientGroups(id, (error, data, response) => {
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
 **id** | **String**| Patient identifier | 

### Return type

[**FetchGroupsResponse**](FetchGroupsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json


## fetchPatients

> FetchPatientsResponse fetchPatients(opts)

List patients

Get a list of patients.

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.PatientApi();
let opts = {
  'filterGroups': "filterGroups_example", // String | Comma-separated list of group ids. Note that either `filter[group]` or `filter[organization]` must be specified.
  'filterOrganization': "filterOrganization_example", // String | Fitbit Plus organization id. Note that either `filter[group]` or `filter[organization]` must be specified.
  'filterIdentifierSystem': "filterIdentifierSystem_example", // String | Identifier system (example: \"MyEHR\") - requires a \"filter[identifier][value]\" parameter
  'filterIdentifierValue': "filterIdentifierValue_example", // String | Identifier value (example: \"12345\") - requires a \"filter[identifier][system]\" parameter
  'filterArchived': true, // Boolean | If not specified, return all patients. If set to 'true' return only archived patients, if set to 'false', return only patients who are not archived.
  'filterCreatedAt': "filterCreatedAt_example", // String | The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by `..`. Example for patients created in November 2017 (America/New_York): `filter[created_at]=2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00` 
  'filterUpdatedAt': "filterUpdatedAt_example", // String | The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by `..`. Example for patients updated in November 2017 (America/New_York): `filter[updated_at]=2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00` 
  'pageNumber': 1, // Number | Page number
  'pageSize': 10, // Number | Page size
  'pageLimit': 50, // Number | Page limit
  'pageCursor': "pageCursor_example" // String | Page cursor
};
apiInstance.fetchPatients(opts, (error, data, response) => {
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
 **filterGroups** | **String**| Comma-separated list of group ids. Note that either &#x60;filter[group]&#x60; or &#x60;filter[organization]&#x60; must be specified. | [optional] 
 **filterOrganization** | **String**| Fitbit Plus organization id. Note that either &#x60;filter[group]&#x60; or &#x60;filter[organization]&#x60; must be specified. | [optional] 
 **filterIdentifierSystem** | **String**| Identifier system (example: \&quot;MyEHR\&quot;) - requires a \&quot;filter[identifier][value]\&quot; parameter | [optional] 
 **filterIdentifierValue** | **String**| Identifier value (example: \&quot;12345\&quot;) - requires a \&quot;filter[identifier][system]\&quot; parameter | [optional] 
 **filterArchived** | **Boolean**| If not specified, return all patients. If set to &#39;true&#39; return only archived patients, if set to &#39;false&#39;, return only patients who are not archived. | [optional] 
 **filterCreatedAt** | **String**| The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by &#x60;..&#x60;. Example for patients created in November 2017 (America/New_York): &#x60;filter[created_at]&#x3D;2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00&#x60;  | [optional] 
 **filterUpdatedAt** | **String**| The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by &#x60;..&#x60;. Example for patients updated in November 2017 (America/New_York): &#x60;filter[updated_at]&#x3D;2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00&#x60;  | [optional] 
 **pageNumber** | **Number**| Page number | [optional] [default to 1]
 **pageSize** | **Number**| Page size | [optional] [default to 10]
 **pageLimit** | **Number**| Page limit | [optional] [default to 50]
 **pageCursor** | **String**| Page cursor | [optional] 

### Return type

[**FetchPatientsResponse**](FetchPatientsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json


## updatePatient

> UpdatePatientResponse updatePatient(id, updatePatientRequest)

Update a patient

Update a patient record.

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.PatientApi();
let id = "id_example"; // String | Patient identifier
let updatePatientRequest = new FitbitPlusApi.UpdatePatientRequest(); // UpdatePatientRequest | 
apiInstance.updatePatient(id, updatePatientRequest, (error, data, response) => {
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
 **id** | **String**| Patient identifier | 
 **updatePatientRequest** | [**UpdatePatientRequest**](UpdatePatientRequest.md)|  | 

### Return type

[**UpdatePatientResponse**](UpdatePatientResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/vnd.api+json
- **Accept**: application/vnd.api+json


## upsertPatient

> CreatePatientResponse upsertPatient(upsertPatientRequest)

Upsert patient

Create a new patient or update an existing patient

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.PatientApi();
let upsertPatientRequest = new FitbitPlusApi.UpsertPatientRequest(); // UpsertPatientRequest | 
apiInstance.upsertPatient(upsertPatientRequest, (error, data, response) => {
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
 **upsertPatientRequest** | [**UpsertPatientRequest**](UpsertPatientRequest.md)|  | 

### Return type

[**CreatePatientResponse**](CreatePatientResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/vnd.api+json
- **Accept**: application/vnd.api+json

