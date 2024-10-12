# PatientView.ObservationHeadingControllerApi

All URIs are relative to *https://www.patientview.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAvailableObservationHeadings**](ObservationHeadingControllerApi.md#getAvailableObservationHeadings) | **GET** /user/{userId}/availableobservationheadings | Get Available Observations Types For a User
[**getPatientEnteredObservationHeadings**](ObservationHeadingControllerApi.md#getPatientEnteredObservationHeadings) | **GET** /user/{userId}/patiententeredobservationheadings | Get Available Patient Entered Observations Types For a User



## getAvailableObservationHeadings

> [ObservationHeading] getAvailableObservationHeadings(userId)

Get Available Observations Types For a User

Given a User ID retrieve a list of available observation types for that user (where they have observation data).

### Example

```javascript
import PatientView from 'patient_view';

let apiInstance = new PatientView.ObservationHeadingControllerApi();
let userId = 789; // Number | userId
apiInstance.getAvailableObservationHeadings(userId, (error, data, response) => {
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

[**[ObservationHeading]**](ObservationHeading.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPatientEnteredObservationHeadings

> [ObservationHeading] getPatientEnteredObservationHeadings(userId)

Get Available Patient Entered Observations Types For a User

Given a User ID retrieve a list of available observation types for that user (where they have patient entered observation data).

### Example

```javascript
import PatientView from 'patient_view';

let apiInstance = new PatientView.ObservationHeadingControllerApi();
let userId = 789; // Number | userId
apiInstance.getPatientEnteredObservationHeadings(userId, (error, data, response) => {
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

[**[ObservationHeading]**](ObservationHeading.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

