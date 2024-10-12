# HealthRepositoryProviderSpecificationsForHip.ConsentFlowApi

All URIs are relative to *https://dev.ndhm.gov.in/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05ConsentsHipNotifyPost**](ConsentFlowApi.md#v05ConsentsHipNotifyPost) | **POST** /v0.5/consents/hip/notify | Consent notification



## v05ConsentsHipNotifyPost

> v05ConsentsHipNotifyPost(authorization, X_HIP_ID, hIPConsentNotification)

Consent notification

Notification of consents to health information providers consent request granted, consent revoked, consent expired. Only the GRANTED and REVOKED status notifications will be sent to HIP.   1. If consent is granted, status&#x3D;GRANTED, then consentDetail contains the consent artefact details and signature is available.    2. If consent is revoked, then status&#x3D;REVOKED, and consentId specifes which consent artefact is revoked.  

### Example

```javascript
import HealthRepositoryProviderSpecificationsForHip from 'health_repository_provider_specifications_for_hip';

let apiInstance = new HealthRepositoryProviderSpecificationsForHip.ConsentFlowApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
let X_HIP_ID = "X_HIP_ID_example"; // String | Identifier of the health information provider to which the request was intended.
let hIPConsentNotification = new HealthRepositoryProviderSpecificationsForHip.HIPConsentNotification(); // HIPConsentNotification | 
apiInstance.v05ConsentsHipNotifyPost(authorization, X_HIP_ID, hIPConsentNotification, (error, data, response) => {
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
 **hIPConsentNotification** | [**HIPConsentNotification**](HIPConsentNotification.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

