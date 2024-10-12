# HealthDataConsentManager.IdentificationApi

All URIs are relative to *https://dev.ndhm.gov.in/cm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05PatientsFindPost**](IdentificationApi.md#v05PatientsFindPost) | **POST** /v0.5/patients/find | Identify a patient by her consent-manager user-id



## v05PatientsFindPost

> v05PatientsFindPost(authorization, patientIdentificationRequest)

Identify a patient by her consent-manager user-id

This API is meant for identify to patient given her consent-manager-user-id. CM subsequently makes the /on-find Gateway API call with results.  

### Example

```javascript
import HealthDataConsentManager from 'health_data_consent_manager';

let apiInstance = new HealthDataConsentManager.IdentificationApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let patientIdentificationRequest = new HealthDataConsentManager.PatientIdentificationRequest(); // PatientIdentificationRequest | 
apiInstance.v05PatientsFindPost(authorization, patientIdentificationRequest, (error, data, response) => {
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
 **authorization** | **String**| Access token which was issued after successful login with gateway auth server. | 
 **patientIdentificationRequest** | [**PatientIdentificationRequest**](PatientIdentificationRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

