# HealthRepositoryProviderSpecificationsForHip.UserAuthApi

All URIs are relative to *https://dev.ndhm.gov.in/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05UsersAuthNotifyPost**](UserAuthApi.md#v05UsersAuthNotifyPost) | **POST** /v0.5/users/auth/notify | notification API in case of DIRECT mode of authentication by the CM
[**v05UsersAuthOnConfirmPost**](UserAuthApi.md#v05UsersAuthOnConfirmPost) | **POST** /v0.5/users/auth/on-confirm | callback API for /auth/confirm (in case of MEDIATED auth) to confirm user authentication or not
[**v05UsersAuthOnFetchModesPost**](UserAuthApi.md#v05UsersAuthOnFetchModesPost) | **POST** /v0.5/users/auth/on-fetch-modes | Identification result for a consent-manager user-id
[**v05UsersAuthOnInitPost**](UserAuthApi.md#v05UsersAuthOnInitPost) | **POST** /v0.5/users/auth/on-init | Response to user authentication initialization from HIP



## v05UsersAuthNotifyPost

> v05UsersAuthNotifyPost(authorization, X_HIP_ID, X_HIU_ID, patientAuthNotification)

notification API in case of DIRECT mode of authentication by the CM

This API is called by CM to confirm authentication of users. The transactionId returned is same as that passed in /auth/on-init. The \&quot;auth.status\&quot; conveys whether the request was GRANTED or DENIED.    1. **auth.accessToken** - is specific to the purpose mentioned in the /auth/init. This token needs to be used for initiating the intended action. For example for HIP initiated linking of care-contexts   2. **NOTE**, only one of **X-HIP-ID** or **X-HIU-ID** will be sent as part of header, not both.   3. The payload is conditional to the purpose of auth. If purpose specified in /auth/init is KYC or KYC_AND_LINK, then patient details are passed. **auth.accessToken** is passed only if the purpose is LINK or KYC_AND_LINK. 

### Example

```javascript
import HealthRepositoryProviderSpecificationsForHip from 'health_repository_provider_specifications_for_hip';

let apiInstance = new HealthRepositoryProviderSpecificationsForHip.UserAuthApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
let X_HIP_ID = "X_HIP_ID_example"; // String | Identifier of the health information provider to which the request was intended.
let X_HIU_ID = "X_HIU_ID_example"; // String | Identifier of the health information user to which the request was intended.
let patientAuthNotification = new HealthRepositoryProviderSpecificationsForHip.PatientAuthNotification(); // PatientAuthNotification | 
apiInstance.v05UsersAuthNotifyPost(authorization, X_HIP_ID, X_HIU_ID, patientAuthNotification, (error, data, response) => {
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
 **X_HIP_ID** | **String**| Identifier of the health information provider to which the request was intended. | 
 **X_HIU_ID** | **String**| Identifier of the health information user to which the request was intended. | 
 **patientAuthNotification** | [**PatientAuthNotification**](PatientAuthNotification.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05UsersAuthOnConfirmPost

> v05UsersAuthOnConfirmPost(authorization, X_HIP_ID, X_HIU_ID, patientAuthConfirmResponse)

callback API for /auth/confirm (in case of MEDIATED auth) to confirm user authentication or not

This API is called by CM to confirm authentication of users.    1. **auth.accessToken** - is specific to the purpose mentioned in the /auth/init. This token needs to be used for initiating the intended action. For example for HIP initiated linking of care-contexts   2. **NOTE**, only one of **X-HIP-ID** or **X-HIU-ID** will be sent as part of header, not both.      

### Example

```javascript
import HealthRepositoryProviderSpecificationsForHip from 'health_repository_provider_specifications_for_hip';

let apiInstance = new HealthRepositoryProviderSpecificationsForHip.UserAuthApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
let X_HIP_ID = "X_HIP_ID_example"; // String | Identifier of the health information provider to which the request was intended.
let X_HIU_ID = "X_HIU_ID_example"; // String | Identifier of the health information user to which the request was intended.
let patientAuthConfirmResponse = new HealthRepositoryProviderSpecificationsForHip.PatientAuthConfirmResponse(); // PatientAuthConfirmResponse | 
apiInstance.v05UsersAuthOnConfirmPost(authorization, X_HIP_ID, X_HIU_ID, patientAuthConfirmResponse, (error, data, response) => {
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
 **X_HIP_ID** | **String**| Identifier of the health information provider to which the request was intended. | 
 **X_HIU_ID** | **String**| Identifier of the health information user to which the request was intended. | 
 **patientAuthConfirmResponse** | [**PatientAuthConfirmResponse**](PatientAuthConfirmResponse.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05UsersAuthOnFetchModesPost

> v05UsersAuthOnFetchModesPost(authorization, X_HIP_ID, X_HIU_ID, patientAuthModeQueryResponse)

Identification result for a consent-manager user-id

If a patient is found then **auth** attribute contains the supported modes for the specified purpose.  Otherwise, error is raised for invalid requests or for non-existent id. Note in addition to the \&quot;Authorization\&quot; header, one of the following headers must be specified 1. **X-HIU-ID** if the requester is HIU (identified from /auth/fetch-modes requester.id) 2. **X-HIP-ID** if the requester is HIP (identified from /auth/fetch-modes requester.id) 

### Example

```javascript
import HealthRepositoryProviderSpecificationsForHip from 'health_repository_provider_specifications_for_hip';

let apiInstance = new HealthRepositoryProviderSpecificationsForHip.UserAuthApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
let X_HIP_ID = "X_HIP_ID_example"; // String | Identifier of the health information provider to which the request was intended.
let X_HIU_ID = "X_HIU_ID_example"; // String | Identifier of the health information user to which the request was intended.
let patientAuthModeQueryResponse = new HealthRepositoryProviderSpecificationsForHip.PatientAuthModeQueryResponse(); // PatientAuthModeQueryResponse | 
apiInstance.v05UsersAuthOnFetchModesPost(authorization, X_HIP_ID, X_HIU_ID, patientAuthModeQueryResponse, (error, data, response) => {
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
 **X_HIP_ID** | **String**| Identifier of the health information provider to which the request was intended. | 
 **X_HIU_ID** | **String**| Identifier of the health information user to which the request was intended. | 
 **patientAuthModeQueryResponse** | [**PatientAuthModeQueryResponse**](PatientAuthModeQueryResponse.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05UsersAuthOnInitPost

> v05UsersAuthOnInitPost(authorization, X_HIP_ID, X_HIU_ID, patientAuthInitResponse)

Response to user authentication initialization from HIP

If the patient&#39;s id is valid, CM will return a transactionId as initialization of user auth. If the request is valid, then &#39;auth.mode&#39; will convey how the authentication should be done. The authentication can be *mediated* or *direct*. For mediated authentication modes, HIP or HIU is epected to send over relevant code (OTP/token) or demographic info via subsequent API call to /auth/confirm. for direct authentication case, CM will notify requester through/users/auth/notify API.     1. **auth.mode** conveys whats the mode of authentication is, and what is expected from HIP/HIU in the subsequent /auth/confirm API call. Possible values        1. MOBILE_OTP - auth via OTP to registered mobile. Mediated.        2. AADHAAR_OTP - auth initiated with Aadhaar with OTP. Mediated.        3. DEMOGRAPHICS - auth initiated with demographic verification       4. DIRECT - for authentication directly with the patient. e.g. Mobile App, SMS. In this case, the HIP/HIU is not expected to call subsequent /auth/confirm call. CM will do direct authentication with the User (e.g. Mobile App, SMS etc) and will notify requester   2. **meta.expiry** conveys the expiry time of the token and the authentication session   3. **NOTE**, only one of **X-HIP-ID** or **X-HIU-ID** will be sent as part of header, not both.                         The error section in the body, represents the potential errors that may have occurred. Possible reasons:   1. Patient id is invalid 

### Example

```javascript
import HealthRepositoryProviderSpecificationsForHip from 'health_repository_provider_specifications_for_hip';

let apiInstance = new HealthRepositoryProviderSpecificationsForHip.UserAuthApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
let X_HIP_ID = "X_HIP_ID_example"; // String | Identifier of the health information provider to which the request was intended.
let X_HIU_ID = "X_HIU_ID_example"; // String | Identifier of the health information user to which the request was intended.
let patientAuthInitResponse = new HealthRepositoryProviderSpecificationsForHip.PatientAuthInitResponse(); // PatientAuthInitResponse | 
apiInstance.v05UsersAuthOnInitPost(authorization, X_HIP_ID, X_HIU_ID, patientAuthInitResponse, (error, data, response) => {
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
 **X_HIP_ID** | **String**| Identifier of the health information provider to which the request was intended. | 
 **X_HIU_ID** | **String**| Identifier of the health information user to which the request was intended. | 
 **patientAuthInitResponse** | [**PatientAuthInitResponse**](PatientAuthInitResponse.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

