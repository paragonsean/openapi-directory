# PatientView.PatientManagementControllerApi

All URIs are relative to *https://www.patientview.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPatientManagement**](PatientManagementControllerApi.md#getPatientManagement) | **GET** /patientmanagement/{userId}/group/{groupId}/identifier/{identifierId} | getPatientManagement
[**getPatientManagementDiagnoses**](PatientManagementControllerApi.md#getPatientManagementDiagnoses) | **GET** /patientmanagement/diagnoses | getPatientManagementDiagnoses
[**getPatientManagementLookupTypes**](PatientManagementControllerApi.md#getPatientManagementLookupTypes) | **GET** /patientmanagement/lookuptypes | getPatientManagementLookupTypes
[**savePatientManagement**](PatientManagementControllerApi.md#savePatientManagement) | **POST** /patientmanagement/{userId}/group/{groupId}/identifier/{identifierId} | savePatientManagement
[**savePatientManagementSurgeries**](PatientManagementControllerApi.md#savePatientManagementSurgeries) | **POST** /patientmanagement/{userId}/group/{groupId}/identifier/{identifierId}/surgeries | savePatientManagementSurgeries
[**validatePatientManagement**](PatientManagementControllerApi.md#validatePatientManagement) | **POST** /patientmanagement/validate | validatePatientManagement



## getPatientManagement

> PatientManagement getPatientManagement(userId, groupId, identifierId)

getPatientManagement

getPatientManagement

### Example

```javascript
import PatientView from 'patient_view';

let apiInstance = new PatientView.PatientManagementControllerApi();
let userId = 789; // Number | userId
let groupId = 789; // Number | groupId
let identifierId = 789; // Number | identifierId
apiInstance.getPatientManagement(userId, groupId, identifierId, (error, data, response) => {
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
 **groupId** | **Number**| groupId | 
 **identifierId** | **Number**| identifierId | 

### Return type

[**PatientManagement**](PatientManagement.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPatientManagementDiagnoses

> [Code] getPatientManagementDiagnoses()

getPatientManagementDiagnoses

getPatientManagementDiagnoses

### Example

```javascript
import PatientView from 'patient_view';

let apiInstance = new PatientView.PatientManagementControllerApi();
apiInstance.getPatientManagementDiagnoses((error, data, response) => {
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

[**[Code]**](Code.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPatientManagementLookupTypes

> [LookupType] getPatientManagementLookupTypes()

getPatientManagementLookupTypes

getPatientManagementLookupTypes

### Example

```javascript
import PatientView from 'patient_view';

let apiInstance = new PatientView.PatientManagementControllerApi();
apiInstance.getPatientManagementLookupTypes((error, data, response) => {
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

[**[LookupType]**](LookupType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## savePatientManagement

> savePatientManagement(userId, groupId, identifierId, opts)

savePatientManagement

savePatientManagement

### Example

```javascript
import PatientView from 'patient_view';

let apiInstance = new PatientView.PatientManagementControllerApi();
let userId = 789; // Number | userId
let groupId = 789; // Number | groupId
let identifierId = 789; // Number | identifierId
let opts = {
  'patientManagement': new PatientView.PatientManagement() // PatientManagement | patientManagement
};
apiInstance.savePatientManagement(userId, groupId, identifierId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userId** | **Number**| userId | 
 **groupId** | **Number**| groupId | 
 **identifierId** | **Number**| identifierId | 
 **patientManagement** | [**PatientManagement**](PatientManagement.md)| patientManagement | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## savePatientManagementSurgeries

> savePatientManagementSurgeries(userId, groupId, identifierId, opts)

savePatientManagementSurgeries

savePatientManagementSurgeries

### Example

```javascript
import PatientView from 'patient_view';

let apiInstance = new PatientView.PatientManagementControllerApi();
let userId = 789; // Number | userId
let groupId = 789; // Number | groupId
let identifierId = 789; // Number | identifierId
let opts = {
  'patientManagement': new PatientView.PatientManagement() // PatientManagement | patientManagement
};
apiInstance.savePatientManagementSurgeries(userId, groupId, identifierId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userId** | **Number**| userId | 
 **groupId** | **Number**| groupId | 
 **identifierId** | **Number**| identifierId | 
 **patientManagement** | [**PatientManagement**](PatientManagement.md)| patientManagement | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## validatePatientManagement

> validatePatientManagement(opts)

validatePatientManagement

validatePatientManagement

### Example

```javascript
import PatientView from 'patient_view';

let apiInstance = new PatientView.PatientManagementControllerApi();
let opts = {
  'patientManagement': new PatientView.PatientManagement() // PatientManagement | patientManagement
};
apiInstance.validatePatientManagement(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patientManagement** | [**PatientManagement**](PatientManagement.md)| patientManagement | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

