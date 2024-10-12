# HealthDataConsentManager.HipFacingApi

All URIs are relative to *https://dev.ndhm.gov.in/cm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05UsersAuthFetchModesPost_0**](HipFacingApi.md#v05UsersAuthFetchModesPost_0) | **POST** /v0.5/users/auth/fetch-modes | Get a patient&#39;s authentication modes relevant to specified purpose
[**v05UsersAuthOnNotifyPost_0**](HipFacingApi.md#v05UsersAuthOnNotifyPost_0) | **POST** /v0.5/users/auth/on-notify | callback API from HIU/HIPs as acknowledgement of auth notification (in case of DIRECT auth)



## v05UsersAuthFetchModesPost_0

> v05UsersAuthFetchModesPost_0(authorization, patientAuthModeQueryRequest)

Get a patient&#39;s authentication modes relevant to specified purpose

This API is meant for identify supported authentication modes for a patient given a specific purpose 

### Example

```javascript
import HealthDataConsentManager from 'health_data_consent_manager';

let apiInstance = new HealthDataConsentManager.HipFacingApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let patientAuthModeQueryRequest = new HealthDataConsentManager.PatientAuthModeQueryRequest(); // PatientAuthModeQueryRequest | 
apiInstance.v05UsersAuthFetchModesPost_0(authorization, patientAuthModeQueryRequest, (error, data, response) => {
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
 **patientAuthModeQueryRequest** | [**PatientAuthModeQueryRequest**](PatientAuthModeQueryRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05UsersAuthOnNotifyPost_0

> v05UsersAuthOnNotifyPost_0(authorization, patientAuthNotificationAcknowledgement)

callback API from HIU/HIPs as acknowledgement of auth notification (in case of DIRECT auth)

This API is called by HIU/HIPs to confirm acknowledgement for receipt of auth notification is case of DIRECT authentication.  

### Example

```javascript
import HealthDataConsentManager from 'health_data_consent_manager';

let apiInstance = new HealthDataConsentManager.HipFacingApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let patientAuthNotificationAcknowledgement = new HealthDataConsentManager.PatientAuthNotificationAcknowledgement(); // PatientAuthNotificationAcknowledgement | 
apiInstance.v05UsersAuthOnNotifyPost_0(authorization, patientAuthNotificationAcknowledgement, (error, data, response) => {
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
 **patientAuthNotificationAcknowledgement** | [**PatientAuthNotificationAcknowledgement**](PatientAuthNotificationAcknowledgement.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

