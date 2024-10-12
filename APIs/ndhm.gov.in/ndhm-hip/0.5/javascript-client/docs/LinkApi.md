# HealthRepositoryProviderSpecificationsForHip.LinkApi

All URIs are relative to *https://dev.ndhm.gov.in/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05LinksLinkConfirmPost**](LinkApi.md#v05LinksLinkConfirmPost) | **POST** /v0.5/links/link/confirm | Token submission by Consent Manager for link confirmation
[**v05LinksLinkInitPost**](LinkApi.md#v05LinksLinkInitPost) | **POST** /v0.5/links/link/init | Link patient&#39;s care contexts
[**v05LinksLinkOnAddContextsPost**](LinkApi.md#v05LinksLinkOnAddContextsPost) | **POST** /v0.5/links/link/on-add-contexts | callback API for HIP initiated patient linking /link/add-context



## v05LinksLinkConfirmPost

> v05LinksLinkConfirmPost(authorization, X_HIP_ID, linkConfirmationRequest)

Token submission by Consent Manager for link confirmation

API to submit the token that was sent by HIP during the link request.  

### Example

```javascript
import HealthRepositoryProviderSpecificationsForHip from 'health_repository_provider_specifications_for_hip';

let apiInstance = new HealthRepositoryProviderSpecificationsForHip.LinkApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
let X_HIP_ID = "X_HIP_ID_example"; // String | Identifier of the health information provider to which the request was intended.
let linkConfirmationRequest = new HealthRepositoryProviderSpecificationsForHip.LinkConfirmationRequest(); // LinkConfirmationRequest | 
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
 **authorization** | **String**| Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge. | 
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

Request from Gateway to links care contexts associated with only one patient   1. **Validate account reference number and care context reference number**   2. **Validate transactionId in the request with discovery request entry to check whether there was a discovery       and were these care contexts discovered or not for a given patient**   3. **Before eventual link confirmation, HIP needs to authenticate the request with the patient(eg: OTP verification)**   4. **HIP should communicate the mode of authentication of a successful request to Consent Manager** 

### Example

```javascript
import HealthRepositoryProviderSpecificationsForHip from 'health_repository_provider_specifications_for_hip';

let apiInstance = new HealthRepositoryProviderSpecificationsForHip.LinkApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
let X_HIP_ID = "X_HIP_ID_example"; // String | Identifier of the health information provider to which the request was intended.
let patientLinkReferenceRequest = new HealthRepositoryProviderSpecificationsForHip.PatientLinkReferenceRequest(); // PatientLinkReferenceRequest | 
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
 **authorization** | **String**| Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge. | 
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
import HealthRepositoryProviderSpecificationsForHip from 'health_repository_provider_specifications_for_hip';

let apiInstance = new HealthRepositoryProviderSpecificationsForHip.LinkApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
let X_HIP_ID = "X_HIP_ID_example"; // String | Identifier of the health information provider to which the request was intended.
let patientCareContextLinkResponse = new HealthRepositoryProviderSpecificationsForHip.PatientCareContextLinkResponse(); // PatientCareContextLinkResponse | 
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
 **authorization** | **String**| Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge. | 
 **X_HIP_ID** | **String**| Identifier of the health information provider to which the request was intended. | 
 **patientCareContextLinkResponse** | [**PatientCareContextLinkResponse**](PatientCareContextLinkResponse.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

