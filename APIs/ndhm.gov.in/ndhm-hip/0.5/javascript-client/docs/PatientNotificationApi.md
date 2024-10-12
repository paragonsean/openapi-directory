# HealthRepositoryProviderSpecificationsForHip.PatientNotificationApi

All URIs are relative to *https://dev.ndhm.gov.in/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05PatientsSmsOnNotifyPost**](PatientNotificationApi.md#v05PatientsSmsOnNotifyPost) | **POST** /v0.5/patients/sms/on-notify | Acknowledgment response for SMS notification sent to patient by HIP



## v05PatientsSmsOnNotifyPost

> v05PatientsSmsOnNotifyPost(authorization, X_HIP_ID, patientSMSNotifcationResponse)

Acknowledgment response for SMS notification sent to patient by HIP

If the SMS notification is successfully sent to patient then \&quot;status\&quot; will be \&quot;ACKNOWLEDGED\&quot; with no error. If the SMS notification is failed then \&quot;status\&quot; will be \&quot;ERRORED\&quot; with error. 

### Example

```javascript
import HealthRepositoryProviderSpecificationsForHip from 'health_repository_provider_specifications_for_hip';

let apiInstance = new HealthRepositoryProviderSpecificationsForHip.PatientNotificationApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
let X_HIP_ID = "X_HIP_ID_example"; // String | Identifier of the health information provider to which the request was intended.
let patientSMSNotifcationResponse = new HealthRepositoryProviderSpecificationsForHip.PatientSMSNotifcationResponse(); // PatientSMSNotifcationResponse | 
apiInstance.v05PatientsSmsOnNotifyPost(authorization, X_HIP_ID, patientSMSNotifcationResponse, (error, data, response) => {
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
 **patientSMSNotifcationResponse** | [**PatientSMSNotifcationResponse**](PatientSMSNotifcationResponse.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

