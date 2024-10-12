# PatientView.ObservationControllerApi

All URIs are relative to *https://www.patientview.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getObservationsByCode**](ObservationControllerApi.md#getObservationsByCode) | **GET** /user/{userId}/observations/{code} | Get Observations of a Certain Type For a User
[**getObservationsByCodes**](ObservationControllerApi.md#getObservationsByCodes) | **GET** /user/{userId}/observations | Get Observations of Multiple Types For a User
[**getPatientEnteredObservationsByCode**](ObservationControllerApi.md#getPatientEnteredObservationsByCode) | **GET** /user/{userId}/observations/{code}/patiententered | Get patient entered Observations of a Certain Type For a User



## getObservationsByCode

> [FhirObservation] getObservationsByCode(userId, code)

Get Observations of a Certain Type For a User

Given a User ID and observation code, retrieve all observations.

### Example

```javascript
import PatientView from 'patient_view';

let apiInstance = new PatientView.ObservationControllerApi();
let userId = 789; // Number | userId
let code = "code_example"; // String | code
apiInstance.getObservationsByCode(userId, code, (error, data, response) => {
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
 **userId** | **Number**| userId | 
 **code** | **String**| code | 

### Return type

[**[FhirObservation]**](FhirObservation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getObservationsByCodes

> FhirObservationPage getObservationsByCodes(userId, code, limit, offset, orderDirection)

Get Observations of Multiple Types For a User

Given a User ID and search parameters, retrieve a page of observations.

### Example

```javascript
import PatientView from 'patient_view';

let apiInstance = new PatientView.ObservationControllerApi();
let userId = 789; // Number | userId
let code = ["null"]; // [String] | code
let limit = 789; // Number | limit
let offset = 789; // Number | offset
let orderDirection = "orderDirection_example"; // String | orderDirection
apiInstance.getObservationsByCodes(userId, code, limit, offset, orderDirection, (error, data, response) => {
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
 **userId** | **Number**| userId | 
 **code** | [**[String]**](String.md)| code | 
 **limit** | **Number**| limit | 
 **offset** | **Number**| offset | 
 **orderDirection** | **String**| orderDirection | 

### Return type

[**FhirObservationPage**](FhirObservationPage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getPatientEnteredObservationsByCode

> [FhirObservation] getPatientEnteredObservationsByCode(userId, code)

Get patient entered Observations of a Certain Type For a User

Given a User ID and observation code, retrieve patient entered observations.

### Example

```javascript
import PatientView from 'patient_view';

let apiInstance = new PatientView.ObservationControllerApi();
let userId = 789; // Number | userId
let code = "code_example"; // String | code
apiInstance.getPatientEnteredObservationsByCode(userId, code, (error, data, response) => {
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
 **userId** | **Number**| userId | 
 **code** | **String**| code | 

### Return type

[**[FhirObservation]**](FhirObservation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

