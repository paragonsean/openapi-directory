# Gateway.DataFlowApi

All URIs are relative to *https://dev.ndhm.gov.in/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05HealthInformationCmOnRequestPost**](DataFlowApi.md#v05HealthInformationCmOnRequestPost) | **POST** /v0.5/health-information/cm/on-request | Health information data request
[**v05HealthInformationCmRequestPost**](DataFlowApi.md#v05HealthInformationCmRequestPost) | **POST** /v0.5/health-information/cm/request | Health information data request
[**v05HealthInformationHipOnRequestPost**](DataFlowApi.md#v05HealthInformationHipOnRequestPost) | **POST** /v0.5/health-information/hip/on-request | Health information data request
[**v05HealthInformationHipRequestPost**](DataFlowApi.md#v05HealthInformationHipRequestPost) | **POST** /v0.5/health-information/hip/request | Health information data request
[**v05HealthInformationNotifyPost**](DataFlowApi.md#v05HealthInformationNotifyPost) | **POST** /v0.5/health-information/notify | Notifications corresponding to events during data flow



## v05HealthInformationCmOnRequestPost

> v05HealthInformationCmOnRequestPost(authorization, X_HIU_ID, hIUHealthInformationRequestResponse)

Health information data request

Callback API for acknowledgement of Health information request of HIU. CM calls this API when it has validated the Health Information request given the consent id. Either the **hiRequest** or **error** would need to be specified. If the health info request was valid, then the ***hiRequest.transactionId*** specifies the transaction context against which HIP would send over the data.  Possible cases of errors are   1. **Invalid consent artefact id**   2. **Consent has expired**   3. **Date ranges are invalid** 

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.DataFlowApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_HIU_ID = "X_HIU_ID_example"; // String | Identifier of the health information user to which the request was intended.
let hIUHealthInformationRequestResponse = new Gateway.HIUHealthInformationRequestResponse(); // HIUHealthInformationRequestResponse | 
apiInstance.v05HealthInformationCmOnRequestPost(authorization, X_HIU_ID, hIUHealthInformationRequestResponse, (error, data, response) => {
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
 **X_HIU_ID** | **String**| Identifier of the health information user to which the request was intended. | 
 **hIUHealthInformationRequestResponse** | [**HIUHealthInformationRequestResponse**](HIUHealthInformationRequestResponse.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05HealthInformationCmRequestPost

> v05HealthInformationCmRequestPost(authorization, X_CM_ID, hIRequest)

Health information data request

Request for Health information against a consent id. CM would generate a transactionId against each consent and pass it as trnasaction context / correlation id to the HIP and also return the same to HIU via /on-request.  

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.DataFlowApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
let hIRequest = new Gateway.HIRequest(); // HIRequest | 
apiInstance.v05HealthInformationCmRequestPost(authorization, X_CM_ID, hIRequest, (error, data, response) => {
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
 **hIRequest** | [**HIRequest**](HIRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05HealthInformationHipOnRequestPost

> v05HealthInformationHipOnRequestPost(authorization, X_CM_ID, hIPHealthInformationRequestAcknowledgement)

Health information data request

API called by HIP to acknowledge Health information request receipt. Either the **hiRequest** or **error** must be specified. **hiRequest** element returns the same transactionId as before with a status indicating that the request is acknowledged.   

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.DataFlowApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
let hIPHealthInformationRequestAcknowledgement = new Gateway.HIPHealthInformationRequestAcknowledgement(); // HIPHealthInformationRequestAcknowledgement | 
apiInstance.v05HealthInformationHipOnRequestPost(authorization, X_CM_ID, hIPHealthInformationRequestAcknowledgement, (error, data, response) => {
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
 **hIPHealthInformationRequestAcknowledgement** | [**HIPHealthInformationRequestAcknowledgement**](HIPHealthInformationRequestAcknowledgement.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05HealthInformationHipRequestPost

> v05HealthInformationHipRequestPost(authorization, X_HIP_ID, hIPHIRequest)

Health information data request

API called by CM to request Health information from HIP against a validated consent artefact. The transactionId is the correlation id that HIP should use use when pushing data to the **dataPushUrl**.  

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.DataFlowApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_HIP_ID = "X_HIP_ID_example"; // String | Identifier of the health information provider to which the request was intended.
let hIPHIRequest = new Gateway.HIPHIRequest(); // HIPHIRequest | 
apiInstance.v05HealthInformationHipRequestPost(authorization, X_HIP_ID, hIPHIRequest, (error, data, response) => {
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
 **hIPHIRequest** | [**HIPHIRequest**](HIPHIRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05HealthInformationNotifyPost

> v05HealthInformationNotifyPost(authorization, X_CM_ID, healthInformationNotification)

Notifications corresponding to events during data flow

API called by HIU and HIP during data-transfer.  1. HIP on transfer of data would send **sessionStatus** - one of [TRANSFERRED, FAILED] 2. HIP would also send **hiStatus** for each *careContextReference* - on of [DELIVERED, ERRORED] 3. HIU on receipt of data would send **sessionStatus** - one of [TRANSFERRED, FAILED]. For example, FAILED when if data was not sent or if invalid data was sent 4. HIU would also send **hiStatus** for each *careContextReference* - one of [OK, ERRORED]  

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.DataFlowApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
let healthInformationNotification = new Gateway.HealthInformationNotification(); // HealthInformationNotification | 
apiInstance.v05HealthInformationNotifyPost(authorization, X_CM_ID, healthInformationNotification, (error, data, response) => {
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
 **healthInformationNotification** | [**HealthInformationNotification**](HealthInformationNotification.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

