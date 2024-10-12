# HealthRepositoryProviderSpecificationsForHiu.IdentificationApi

All URIs are relative to *https://dev.ndhm.gov.in/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05PatientsOnFindPost**](IdentificationApi.md#v05PatientsOnFindPost) | **POST** /v0.5/patients/on-find | Identification result for a consent-manager user-id



## v05PatientsOnFindPost

> v05PatientsOnFindPost(authorization, patientIdentificationResponse)

Identification result for a consent-manager user-id

If a patient is found then patient.name contains the patients name.  Otherwise, patient is not provided, and possibly error is raised for invalid requests Note in addition to the \&quot;Authorization\&quot; header, one of the following headers must be specified 1. specify **X-HIU-ID** if the requester is HIU (identified from /find requester.id) 2. specify **X-HIP-ID** if the requester is HIP (identified from /find requester.id) 

### Example

```javascript
import HealthRepositoryProviderSpecificationsForHiu from 'health_repository_provider_specifications_for_hiu';

let apiInstance = new HealthRepositoryProviderSpecificationsForHiu.IdentificationApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
let patientIdentificationResponse = new HealthRepositoryProviderSpecificationsForHiu.PatientIdentificationResponse(); // PatientIdentificationResponse | 
apiInstance.v05PatientsOnFindPost(authorization, patientIdentificationResponse, (error, data, response) => {
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
 **authorization** | **String**| Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge. | 
 **patientIdentificationResponse** | [**PatientIdentificationResponse**](PatientIdentificationResponse.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

