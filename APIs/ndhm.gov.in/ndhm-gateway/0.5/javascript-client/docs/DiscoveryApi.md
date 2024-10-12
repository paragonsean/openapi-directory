# Gateway.DiscoveryApi

All URIs are relative to *https://dev.ndhm.gov.in/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05CareContextsDiscoverPost**](DiscoveryApi.md#v05CareContextsDiscoverPost) | **POST** /v0.5/care-contexts/discover | Discover patient&#39;s accounts
[**v05CareContextsOnDiscoverPost**](DiscoveryApi.md#v05CareContextsOnDiscoverPost) | **POST** /v0.5/care-contexts/on-discover | Response to patient&#39;s account discovery request



## v05CareContextsDiscoverPost

> v05CareContextsDiscoverPost(authorization, X_HIP_ID, patientDiscoveryRequest)

Discover patient&#39;s accounts

Request for patient care context discover, made by CM for a specific HIP. It is expected that HIP will subsequently return either zero or one patient record with (potentially masked) associated care contexts   1. **At least one of the verified identifier matches**   2. **Name (fuzzy), gender matches**   3. **If YoB was given, age band(+-2) matches**   4. **If unverified identifiers were given, one of them matches**   5. **If more than one patient records would be found after aforementioned steps, then patient who matches most verified and unverified identifiers would be returned.**   6. **If there would be still more than one patients (after ranking) error would be returned**   7. **Intended HIP should be able to resolve and identify results returned in the subsequent link confirmation request via the specified transactionId**   8. **Intended HIP should store the discovery results with transactionId and care contexts discovered for subsequent link initiation** 

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.DiscoveryApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_HIP_ID = "X_HIP_ID_example"; // String | Identifier of the health information provider to which the request was intended.
let patientDiscoveryRequest = new Gateway.PatientDiscoveryRequest(); // PatientDiscoveryRequest | 
apiInstance.v05CareContextsDiscoverPost(authorization, X_HIP_ID, patientDiscoveryRequest, (error, data, response) => {
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
 **patientDiscoveryRequest** | [**PatientDiscoveryRequest**](PatientDiscoveryRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05CareContextsOnDiscoverPost

> v05CareContextsOnDiscoverPost(authorization, X_CM_ID, patientDiscoveryResult)

Response to patient&#39;s account discovery request

Result of patient care-context discovery request at HIP end. If a matching patient found with zero or more care contexts associated, it is specified as result attribute. If the prior discovery request, resulted in errors then it is specified in the error attribute. Reasons of errors can be    1. **more than one definitive match for the given request**    2. **no verified identifer was specified** 

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.DiscoveryApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
let patientDiscoveryResult = new Gateway.PatientDiscoveryResult(); // PatientDiscoveryResult | 
apiInstance.v05CareContextsOnDiscoverPost(authorization, X_CM_ID, patientDiscoveryResult, (error, data, response) => {
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
 **patientDiscoveryResult** | [**PatientDiscoveryResult**](PatientDiscoveryResult.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

