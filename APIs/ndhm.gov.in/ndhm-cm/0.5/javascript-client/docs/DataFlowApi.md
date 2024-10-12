# HealthDataConsentManager.DataFlowApi

All URIs are relative to *https://dev.ndhm.gov.in/cm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05HealthInformationNotifyPost**](DataFlowApi.md#v05HealthInformationNotifyPost) | **POST** /v0.5/health-information/notify | Notifications corresponding to events during data flow
[**v05HealthInformationOnRequestPost**](DataFlowApi.md#v05HealthInformationOnRequestPost) | **POST** /v0.5/health-information/on-request | Health information data request acknowledgement from HIP
[**v05HealthInformationRequestPost**](DataFlowApi.md#v05HealthInformationRequestPost) | **POST** /v0.5/health-information/request | Health information data request from HIU



## v05HealthInformationNotifyPost

> v05HealthInformationNotifyPost(authorization, healthInformationNotification)

Notifications corresponding to events during data flow

API called by HIU and HIP during data-transfer.  1. HIP on transfer of data would send **sessionStatus** - one of [TRANSFERRED, FAILED] 2. HIP would also send **hiStatus** for each *careContextReference* - on of [DELIVERED, ERRORED] 3. HIU on receipt of data would send **sessionStatus** - one of [TRANSFERRED, FAILED]. For example, FAILED when if data was not sent or if invalid data was sent 4. HIU would also send **hiStatus** for each *careContextReference* - one of [OK, ERRORED]  

### Example

```javascript
import HealthDataConsentManager from 'health_data_consent_manager';

let apiInstance = new HealthDataConsentManager.DataFlowApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let healthInformationNotification = new HealthDataConsentManager.HealthInformationNotification(); // HealthInformationNotification | 
apiInstance.v05HealthInformationNotifyPost(authorization, healthInformationNotification, (error, data, response) => {
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
 **healthInformationNotification** | [**HealthInformationNotification**](HealthInformationNotification.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05HealthInformationOnRequestPost

> v05HealthInformationOnRequestPost(authorization, hIPHealthInformationRequestAcknowledgement)

Health information data request acknowledgement from HIP

This API is called by HIP to acknowledge Health information request receipt. When HIU requests health information, CM generates a transactionId and makes a health information request to the HIP(s). HIPs acknowledgement to the health-information request is coveyed by this API. Either the **hiRequest** or **error** must be specified. **hiRequest** element returns the same transactionId as before with a status indicating that the request is acknowledged.   

### Example

```javascript
import HealthDataConsentManager from 'health_data_consent_manager';

let apiInstance = new HealthDataConsentManager.DataFlowApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let hIPHealthInformationRequestAcknowledgement = new HealthDataConsentManager.HIPHealthInformationRequestAcknowledgement(); // HIPHealthInformationRequestAcknowledgement | 
apiInstance.v05HealthInformationOnRequestPost(authorization, hIPHealthInformationRequestAcknowledgement, (error, data, response) => {
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
 **hIPHealthInformationRequestAcknowledgement** | [**HIPHealthInformationRequestAcknowledgement**](HIPHealthInformationRequestAcknowledgement.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05HealthInformationRequestPost

> v05HealthInformationRequestPost(authorization, hIRequest)

Health information data request from HIU

HIU request for Health information against a consent id. CM would generate a transactionId against each consent and pass it as trnasaction context / correlation id to the HIP and also return the same to HIU via Gateway API - ***_/v0.5/health-information/cm/on-request***.  

### Example

```javascript
import HealthDataConsentManager from 'health_data_consent_manager';

let apiInstance = new HealthDataConsentManager.DataFlowApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let hIRequest = new HealthDataConsentManager.HIRequest(); // HIRequest | 
apiInstance.v05HealthInformationRequestPost(authorization, hIRequest, (error, data, response) => {
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
 **hIRequest** | [**HIRequest**](HIRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

