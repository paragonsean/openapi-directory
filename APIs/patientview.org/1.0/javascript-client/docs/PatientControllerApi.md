# PatientView.PatientControllerApi

All URIs are relative to *https://www.patientview.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getBasicPatientDetails**](PatientControllerApi.md#getBasicPatientDetails) | **GET** /patient/{userId}/basic | Get Basic Patient Information



## getBasicPatientDetails

> [Patient] getBasicPatientDetails(userId)

Get Basic Patient Information

Given a User ID, get basic patient information for a user from clinical data stored in FHIR

### Example

```javascript
import PatientView from 'patient_view';

let apiInstance = new PatientView.PatientControllerApi();
let userId = 789; // Number | userId
apiInstance.getBasicPatientDetails(userId, (error, data, response) => {
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

### Return type

[**[Patient]**](Patient.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

