# Gateway.LinkApi

All URIs are relative to *https://dev.ndhm.gov.in/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05LinksLinkAddContextsPost**](LinkApi.md#v05LinksLinkAddContextsPost) | **POST** /v0.5/links/link/add-contexts | API for HIP initiated care-context linking for patient
[**v05LinksLinkConfirmPost**](LinkApi.md#v05LinksLinkConfirmPost) | **POST** /v0.5/links/link/confirm | Token submission by Consent Manager for link confirmation
[**v05LinksLinkInitPost**](LinkApi.md#v05LinksLinkInitPost) | **POST** /v0.5/links/link/init | Link patient&#39;s care contexts
[**v05LinksLinkOnAddContextsPost**](LinkApi.md#v05LinksLinkOnAddContextsPost) | **POST** /v0.5/links/link/on-add-contexts | callback API for HIP initiated patient linking /link/add-context
[**v05LinksLinkOnConfirmPost**](LinkApi.md#v05LinksLinkOnConfirmPost) | **POST** /v0.5/links/link/on-confirm | Token authenticated by HIP, indicating completion of linkage of care-contexts
[**v05LinksLinkOnInitPost**](LinkApi.md#v05LinksLinkOnInitPost) | **POST** /v0.5/links/link/on-init | Response to patient&#39;s care context link request



## v05LinksLinkAddContextsPost

> v05LinksLinkAddContextsPost(authorization, X_CM_ID, patientCareContextLinkRequest)

API for HIP initiated care-context linking for patient

API to submit care-context to CM for HIP initiated linking. The API must accompany the \&quot;accessToken\&quot; fetched in the users/auth process.     1. subsequent usage for accessToken may be invalid if it was meant for one-time usage or if it expired 

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.LinkApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
let patientCareContextLinkRequest = new Gateway.PatientCareContextLinkRequest(); // PatientCareContextLinkRequest | 
apiInstance.v05LinksLinkAddContextsPost(authorization, X_CM_ID, patientCareContextLinkRequest, (error, data, response) => {
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
 **patientCareContextLinkRequest** | [**PatientCareContextLinkRequest**](PatientCareContextLinkRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05LinksLinkConfirmPost

> v05LinksLinkConfirmPost(authorization, X_HIP_ID, linkConfirmationRequest)

Token submission by Consent Manager for link confirmation

API to submit the token that was sent by HIP during the link request.  

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.LinkApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_HIP_ID = "X_HIP_ID_example"; // String | Identifier of the health information provider to which the request was intended.
let linkConfirmationRequest = new Gateway.LinkConfirmationRequest(); // LinkConfirmationRequest | 
apiInstance.v05LinksLinkConfirmPost(authorization, X_HIP_ID, linkConfirmationRequest, (error, data, response) => {
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
 **linkConfirmationRequest** | [**LinkConfirmationRequest**](LinkConfirmationRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05LinksLinkInitPost

> v05LinksLinkInitPost(authorization, X_HIP_ID, patientLinkReferenceRequest)

Link patient&#39;s care contexts

Request from CM to links care contexts associated with only one patient   1. **Validate account reference number and care context reference number**   2. **Validate transactionId in the request with discovery request entry to check whether there was a discovery       and were these care contexts discovered or not for a given patient**   3. **Before eventual link confirmation, HIP needs to authenticate the request with the patient(eg: OTP verification)**   4. **HIP should communicate the mode of authentication of a successful request to Consent Manager** 

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.LinkApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_HIP_ID = "X_HIP_ID_example"; // String | Identifier of the health information provider to which the request was intended.
let patientLinkReferenceRequest = new Gateway.PatientLinkReferenceRequest(); // PatientLinkReferenceRequest | 
apiInstance.v05LinksLinkInitPost(authorization, X_HIP_ID, patientLinkReferenceRequest, (error, data, response) => {
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
 **patientLinkReferenceRequest** | [**PatientLinkReferenceRequest**](PatientLinkReferenceRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05LinksLinkOnAddContextsPost

> v05LinksLinkOnAddContextsPost(authorization, X_HIP_ID, patientCareContextLinkResponse)

callback API for HIP initiated patient linking /link/add-context

If the accessToken is valid for purpose of linking, and specified details provided, CM will send \&quot;acknoweldgement.status\&quot; as SUCCESS. If any error occcurred, for example invalid token, or other required patient or care-context information not provided, then \&quot;error\&quot; attribute conveys so.    1. **accessToken must be valid and must be for the purpose of linking** 

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.LinkApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_HIP_ID = "X_HIP_ID_example"; // String | Identifier of the health information provider to which the request was intended.
let patientCareContextLinkResponse = new Gateway.PatientCareContextLinkResponse(); // PatientCareContextLinkResponse | 
apiInstance.v05LinksLinkOnAddContextsPost(authorization, X_HIP_ID, patientCareContextLinkResponse, (error, data, response) => {
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
 **patientCareContextLinkResponse** | [**PatientCareContextLinkResponse**](PatientCareContextLinkResponse.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05LinksLinkOnConfirmPost

> v05LinksLinkOnConfirmPost(authorization, X_CM_ID, patientLinkResult)

Token authenticated by HIP, indicating completion of linkage of care-contexts

Returns a list of linked care contexts with patient reference number.   1. **Validated and linked account reference number**   2. **Validated that the token sent from Consent Manager is same as the one generated by HIP**   3. **Verified that same Consent Manager which made the link request is sending the token**   4. **Results of unmasked linked care contexts with patient reference number** 

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.LinkApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
let patientLinkResult = new Gateway.PatientLinkResult(); // PatientLinkResult | 
apiInstance.v05LinksLinkOnConfirmPost(authorization, X_CM_ID, patientLinkResult, (error, data, response) => {
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
 **patientLinkResult** | [**PatientLinkResult**](PatientLinkResult.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05LinksLinkOnInitPost

> v05LinksLinkOnInitPost(authorization, X_CM_ID, patientLinkReferenceResult)

Response to patient&#39;s care context link request

Result of patient care-context link request from HIP end. This happens in context of previous discovery of patient found at HIP end, therefore the link requests ought to be in reference to the patient reference and care-context references previously returned by the HIP. The correlation of discovery and link request is maintained through the transactionId. HIP should have   1. **Validated transactionId in the request to check whether there was a discovery done previously, and the link request corresponds to returned patient care care context references**   2. **Before returning the response, HIP should have sent an authentication request to the patient(eg: OTP verification)**   3. **HIP should communicate the mode of authentication of a successful request**   4. **HIP subsequently should expect the token passed via /link/confirm against the link.referenceNumber passed in this call**                        The error section in the body, represents the potential errors that may have occurred. Possible reasons:   1. **Patient reference number is invalid**   2. **Care context reference numbers are invalid** 

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.LinkApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
let patientLinkReferenceResult = new Gateway.PatientLinkReferenceResult(); // PatientLinkReferenceResult | 
apiInstance.v05LinksLinkOnInitPost(authorization, X_CM_ID, patientLinkReferenceResult, (error, data, response) => {
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
 **patientLinkReferenceResult** | [**PatientLinkReferenceResult**](PatientLinkReferenceResult.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

