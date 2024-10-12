# HealthRepositoryProviderSpecificationsForHip.DataFlowApi

All URIs are relative to *https://dev.ndhm.gov.in/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05HealthInformationHipRequestPost**](DataFlowApi.md#v05HealthInformationHipRequestPost) | **POST** /v0.5/health-information/hip/request | Health information data request



## v05HealthInformationHipRequestPost

> v05HealthInformationHipRequestPost(authorization, X_HIP_ID, hIPHealthInformationRequest)

Health information data request

API called by CM to request Health information from HIP against a validated consent artefact. The transactionId is the correlation id that HIP should use use when pushing data to the **dataPushUrl**.  

### Example

```javascript
import HealthRepositoryProviderSpecificationsForHip from 'health_repository_provider_specifications_for_hip';

let apiInstance = new HealthRepositoryProviderSpecificationsForHip.DataFlowApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
let X_HIP_ID = "X_HIP_ID_example"; // String | Identifier of the health information provider to which the request was intended.
let hIPHealthInformationRequest = new HealthRepositoryProviderSpecificationsForHip.HIPHealthInformationRequest(); // HIPHealthInformationRequest | 
apiInstance.v05HealthInformationHipRequestPost(authorization, X_HIP_ID, hIPHealthInformationRequest, (error, data, response) => {
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
 **hIPHealthInformationRequest** | [**HIPHealthInformationRequest**](HIPHealthInformationRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

