# HealthDataConsentManager.UserAuthApi

All URIs are relative to *https://dev.ndhm.gov.in/cm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05UsersAuthConfirmPost**](UserAuthApi.md#v05UsersAuthConfirmPost) | **POST** /v0.5/users/auth/confirm | Confirmation request sending token, otp or other authentication details from HIP/HIU for confirmation
[**v05UsersAuthFetchModesPost**](UserAuthApi.md#v05UsersAuthFetchModesPost) | **POST** /v0.5/users/auth/fetch-modes | Get a patient&#39;s authentication modes relevant to specified purpose
[**v05UsersAuthInitPost**](UserAuthApi.md#v05UsersAuthInitPost) | **POST** /v0.5/users/auth/init | Initialize authentication from HIP
[**v05UsersAuthOnNotifyPost**](UserAuthApi.md#v05UsersAuthOnNotifyPost) | **POST** /v0.5/users/auth/on-notify | callback API from HIU/HIPs as acknowledgement of auth notification (in case of DIRECT auth)



## v05UsersAuthConfirmPost

> v05UsersAuthConfirmPost(authorization, patientAuthConfirmRequest)

Confirmation request sending token, otp or other authentication details from HIP/HIU for confirmation

This API is called by HIP/HIUs to confirm authentication of users. The transactionId returned by the previous callback API /users/auth/on-init must be sent. If Authentication is successful the callback API will send an \&quot;access token\&quot; for subsequent purpose specific API calls. Note only **credential.authCode** or **credential.demographic** should be sent   1. demographic details are only required for  demographic auth as of now.    2. demographic details are required only in MEDIATED cases and if the **auth.mode** so demands. e.g. if **auth.mode** is DEMOGRAPHICS. Usually for demographic authentication, the name, gender and DOB must be exactly as specified in User Account.   3. demographic.identifier is optional, however maybe required if authentication so mandates.    4. credential.authCode is required for other MEDIATED authentication like MOBILE_OTP, AADHAAR_OTP.  

### Example

```javascript
import HealthDataConsentManager from 'health_data_consent_manager';

let apiInstance = new HealthDataConsentManager.UserAuthApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let patientAuthConfirmRequest = new HealthDataConsentManager.PatientAuthConfirmRequest(); // PatientAuthConfirmRequest | 
apiInstance.v05UsersAuthConfirmPost(authorization, patientAuthConfirmRequest, (error, data, response) => {
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
 **patientAuthConfirmRequest** | [**PatientAuthConfirmRequest**](PatientAuthConfirmRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05UsersAuthFetchModesPost

> v05UsersAuthFetchModesPost(authorization, patientAuthModeQueryRequest)

Get a patient&#39;s authentication modes relevant to specified purpose

This API is meant for identify supported authentication modes for a patient given a specific purpose 

### Example

```javascript
import HealthDataConsentManager from 'health_data_consent_manager';

let apiInstance = new HealthDataConsentManager.UserAuthApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let patientAuthModeQueryRequest = new HealthDataConsentManager.PatientAuthModeQueryRequest(); // PatientAuthModeQueryRequest | 
apiInstance.v05UsersAuthFetchModesPost(authorization, patientAuthModeQueryRequest, (error, data, response) => {
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


## v05UsersAuthInitPost

> v05UsersAuthInitPost(authorization, patientAuthInitRequest)

Initialize authentication from HIP

This API is called by HIPs to initiate authentication of users. A transactionId is retuned by the corresponding callback API for confirmation of user auth. 

### Example

```javascript
import HealthDataConsentManager from 'health_data_consent_manager';

let apiInstance = new HealthDataConsentManager.UserAuthApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let patientAuthInitRequest = new HealthDataConsentManager.PatientAuthInitRequest(); // PatientAuthInitRequest | 
apiInstance.v05UsersAuthInitPost(authorization, patientAuthInitRequest, (error, data, response) => {
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
 **patientAuthInitRequest** | [**PatientAuthInitRequest**](PatientAuthInitRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05UsersAuthOnNotifyPost

> v05UsersAuthOnNotifyPost(authorization, patientAuthNotificationAcknowledgement)

callback API from HIU/HIPs as acknowledgement of auth notification (in case of DIRECT auth)

This API is called by HIU/HIPs to confirm acknowledgement for receipt of auth notification is case of DIRECT authentication.  

### Example

```javascript
import HealthDataConsentManager from 'health_data_consent_manager';

let apiInstance = new HealthDataConsentManager.UserAuthApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let patientAuthNotificationAcknowledgement = new HealthDataConsentManager.PatientAuthNotificationAcknowledgement(); // PatientAuthNotificationAcknowledgement | 
apiInstance.v05UsersAuthOnNotifyPost(authorization, patientAuthNotificationAcknowledgement, (error, data, response) => {
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

