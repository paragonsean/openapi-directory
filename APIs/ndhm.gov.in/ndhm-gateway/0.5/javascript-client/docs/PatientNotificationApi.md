# Gateway.PatientNotificationApi

All URIs are relative to *https://dev.ndhm.gov.in/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05PatientsSmsNotifyPost_0**](PatientNotificationApi.md#v05PatientsSmsNotifyPost_0) | **POST** /v0.5/patients/sms/notify | API for HIP to send SMS notifications to patients
[**v05PatientsSmsOnNotifyPost_0**](PatientNotificationApi.md#v05PatientsSmsOnNotifyPost_0) | **POST** /v0.5/patients/sms/on-notify | Acknowledgment response for SMS notification sent to patient by HIP



## v05PatientsSmsNotifyPost_0

> v05PatientsSmsNotifyPost_0(authorization, X_CM_ID, patientSMSNotifcationRequest)

API for HIP to send SMS notifications to patients

API to send SMS notifications to patient with custom deeplink. 

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.PatientNotificationApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
let patientSMSNotifcationRequest = new Gateway.PatientSMSNotifcationRequest(); // PatientSMSNotifcationRequest | 
apiInstance.v05PatientsSmsNotifyPost_0(authorization, X_CM_ID, patientSMSNotifcationRequest, (error, data, response) => {
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
 **X_CM_ID** | **String**| Suffix of the consent manager to which the request was intended. | 
 **patientSMSNotifcationRequest** | [**PatientSMSNotifcationRequest**](PatientSMSNotifcationRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05PatientsSmsOnNotifyPost_0

> v05PatientsSmsOnNotifyPost_0(authorization, X_HIP_ID, patientSMSNotifcationResponse)

Acknowledgment response for SMS notification sent to patient by HIP

If the SMS notification is successfully sent to patient then \&quot;status\&quot; will be \&quot;ACKNOWLEDGED\&quot; with no error. If the SMS notification is failed then \&quot;status\&quot; will be \&quot;ERRORED\&quot; with error. 

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.PatientNotificationApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_HIP_ID = "X_HIP_ID_example"; // String | Identifier of the health information provider to which the request was intended.
let patientSMSNotifcationResponse = new Gateway.PatientSMSNotifcationResponse(); // PatientSMSNotifcationResponse | 
apiInstance.v05PatientsSmsOnNotifyPost_0(authorization, X_HIP_ID, patientSMSNotifcationResponse, (error, data, response) => {
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
 **X_HIP_ID** | **String**| Identifier of the health information provider to which the request was intended. | 
 **patientSMSNotifcationResponse** | [**PatientSMSNotifcationResponse**](PatientSMSNotifcationResponse.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

