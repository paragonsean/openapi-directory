# Gateway.CmFacingApi

All URIs are relative to *https://dev.ndhm.gov.in/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05CareContextsDiscoverPost_0**](CmFacingApi.md#v05CareContextsDiscoverPost_0) | **POST** /v0.5/care-contexts/discover | Discover patient&#39;s accounts
[**v05CareContextsOnDiscoverPost_0**](CmFacingApi.md#v05CareContextsOnDiscoverPost_0) | **POST** /v0.5/care-contexts/on-discover | Response to patient&#39;s account discovery request
[**v05ConsentRequestsOnInitPost_0**](CmFacingApi.md#v05ConsentRequestsOnInitPost_0) | **POST** /v0.5/consent-requests/on-init | Response to consent request
[**v05ConsentRequestsOnStatusPost_0**](CmFacingApi.md#v05ConsentRequestsOnStatusPost_0) | **POST** /v0.5/consent-requests/on-status | Result of consent request status
[**v05ConsentsHipNotifyPost_0**](CmFacingApi.md#v05ConsentsHipNotifyPost_0) | **POST** /v0.5/consents/hip/notify | Consent notification
[**v05ConsentsHiuNotifyPost_0**](CmFacingApi.md#v05ConsentsHiuNotifyPost_0) | **POST** /v0.5/consents/hiu/notify | Consent notification
[**v05ConsentsOnFetchPost_0**](CmFacingApi.md#v05ConsentsOnFetchPost_0) | **POST** /v0.5/consents/on-fetch | Result of fetch request for a consent artefact
[**v05HealthInformationCmOnRequestPost_0**](CmFacingApi.md#v05HealthInformationCmOnRequestPost_0) | **POST** /v0.5/health-information/cm/on-request | Health information data request
[**v05HealthInformationHipRequestPost_0**](CmFacingApi.md#v05HealthInformationHipRequestPost_0) | **POST** /v0.5/health-information/hip/request | Health information data request
[**v05LinksLinkConfirmPost_0**](CmFacingApi.md#v05LinksLinkConfirmPost_0) | **POST** /v0.5/links/link/confirm | Token submission by Consent Manager for link confirmation
[**v05LinksLinkInitPost_0**](CmFacingApi.md#v05LinksLinkInitPost_0) | **POST** /v0.5/links/link/init | Link patient&#39;s care contexts
[**v05LinksLinkOnAddContextsPost_0**](CmFacingApi.md#v05LinksLinkOnAddContextsPost_0) | **POST** /v0.5/links/link/on-add-contexts | callback API for HIP initiated patient linking /link/add-context
[**v05PatientsOnFindPost_0**](CmFacingApi.md#v05PatientsOnFindPost_0) | **POST** /v0.5/patients/on-find | Identification result for a consent-manager user-id
[**v05PatientsProfileSharePost_0**](CmFacingApi.md#v05PatientsProfileSharePost_0) | **POST** /v0.5/patients/profile/share | Share patient profile details
[**v05PatientsSmsOnNotifyPost**](CmFacingApi.md#v05PatientsSmsOnNotifyPost) | **POST** /v0.5/patients/sms/on-notify | Acknowledgment response for SMS notification sent to patient by HIP
[**v05SubscriptionRequestsCmOnInitPost_0**](CmFacingApi.md#v05SubscriptionRequestsCmOnInitPost_0) | **POST** /v0.5/subscription-requests/cm/on-init | callback API for the /subscription-requests/cm/init to notify a HIU on acceptance/acknowledgement of the request for subscription.
[**v05SubscriptionRequestsHiuNotifyPost_0**](CmFacingApi.md#v05SubscriptionRequestsHiuNotifyPost_0) | **POST** /v0.5/subscription-requests/hiu/notify | Notification for subscription grant/deny/revoke
[**v05SubscriptionsHiuNotifyPost_0**](CmFacingApi.md#v05SubscriptionsHiuNotifyPost_0) | **POST** /v0.5/subscriptions/hiu/notify | Notification to HIU on basis of a granted subscription
[**v05UsersAuthNotifyPost_0**](CmFacingApi.md#v05UsersAuthNotifyPost_0) | **POST** /v0.5/users/auth/notify | notification API in case of DIRECT mode of authentication by the CM
[**v05UsersAuthOnConfirmPost_0**](CmFacingApi.md#v05UsersAuthOnConfirmPost_0) | **POST** /v0.5/users/auth/on-confirm | callback API for /auth/confirm (in case of MEDIATED auth) to confirm user authentication or not
[**v05UsersAuthOnFetchModesPost_0**](CmFacingApi.md#v05UsersAuthOnFetchModesPost_0) | **POST** /v0.5/users/auth/on-fetch-modes | Identification result for a consent-manager user-id
[**v05UsersAuthOnInitPost_0**](CmFacingApi.md#v05UsersAuthOnInitPost_0) | **POST** /v0.5/users/auth/on-init | Response to user authentication initialization from HIP



## v05CareContextsDiscoverPost_0

> v05CareContextsDiscoverPost_0(authorization, X_HIP_ID, patientDiscoveryRequest)

Discover patient&#39;s accounts

Request for patient care context discover, made by CM for a specific HIP. It is expected that HIP will subsequently return either zero or one patient record with (potentially masked) associated care contexts   1. **At least one of the verified identifier matches**   2. **Name (fuzzy), gender matches**   3. **If YoB was given, age band(+-2) matches**   4. **If unverified identifiers were given, one of them matches**   5. **If more than one patient records would be found after aforementioned steps, then patient who matches most verified and unverified identifiers would be returned.**   6. **If there would be still more than one patients (after ranking) error would be returned**   7. **Intended HIP should be able to resolve and identify results returned in the subsequent link confirmation request via the specified transactionId**   8. **Intended HIP should store the discovery results with transactionId and care contexts discovered for subsequent link initiation** 

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.CmFacingApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_HIP_ID = "X_HIP_ID_example"; // String | Identifier of the health information provider to which the request was intended.
let patientDiscoveryRequest = new Gateway.PatientDiscoveryRequest(); // PatientDiscoveryRequest | 
apiInstance.v05CareContextsDiscoverPost_0(authorization, X_HIP_ID, patientDiscoveryRequest, (error, data, response) => {
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


## v05CareContextsOnDiscoverPost_0

> v05CareContextsOnDiscoverPost_0(authorization, X_CM_ID, patientDiscoveryResult)

Response to patient&#39;s account discovery request

Result of patient care-context discovery request at HIP end. If a matching patient found with zero or more care contexts associated, it is specified as result attribute. If the prior discovery request, resulted in errors then it is specified in the error attribute. Reasons of errors can be    1. **more than one definitive match for the given request**    2. **no verified identifer was specified** 

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.CmFacingApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
let patientDiscoveryResult = new Gateway.PatientDiscoveryResult(); // PatientDiscoveryResult | 
apiInstance.v05CareContextsOnDiscoverPost_0(authorization, X_CM_ID, patientDiscoveryResult, (error, data, response) => {
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


## v05ConsentRequestsOnInitPost_0

> v05ConsentRequestsOnInitPost_0(authorization, X_HIU_ID, consentRequestInitResponse)

Response to consent request

Result of consent request creation for a patient. **consentRequest.id** represents the consentrequest id created by CM. The result must contain either **consentRequest** or the **error** caused. &lt;br/&gt;   Reasons for error may be   * Invalid references (e.g patient id, hiu id), purpose, hiTypes, ranges, persmission 

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.CmFacingApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_HIU_ID = "X_HIU_ID_example"; // String | Identifier of the health information user to which the request was intended.
let consentRequestInitResponse = new Gateway.ConsentRequestInitResponse(); // ConsentRequestInitResponse | 
apiInstance.v05ConsentRequestsOnInitPost_0(authorization, X_HIU_ID, consentRequestInitResponse, (error, data, response) => {
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
 **consentRequestInitResponse** | [**ConsentRequestInitResponse**](ConsentRequestInitResponse.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05ConsentRequestsOnStatusPost_0

> v05ConsentRequestsOnStatusPost_0(authorization, X_HIU_ID, hIUConsentRequestStatus)

Result of consent request status

Result of consent request done previously. Status of request can be GRANTED,  DENIED, EXPIRED. If the request was GRANTED, then  

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.CmFacingApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_HIU_ID = "X_HIU_ID_example"; // String | Identifier of the health information user to which the request was intended.
let hIUConsentRequestStatus = new Gateway.HIUConsentRequestStatus(); // HIUConsentRequestStatus | 
apiInstance.v05ConsentRequestsOnStatusPost_0(authorization, X_HIU_ID, hIUConsentRequestStatus, (error, data, response) => {
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
 **hIUConsentRequestStatus** | [**HIUConsentRequestStatus**](HIUConsentRequestStatus.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05ConsentsHipNotifyPost_0

> v05ConsentsHipNotifyPost_0(authorization, X_HIP_ID, hIPConsentNotification)

Consent notification

Notification of consents to health information providers consent request granted, consent revoked, consent expired. Only the GRANTED, REVOKED and EXPIRED status notifications will be sent to HIP.   1. If consent is granted, status&#x3D;GRANTED, then consentDetail contains the consent artefact details and signature is available.    2. If consent is revoked, then status&#x3D;REVOKED, and consentId specifes which consent artefact is revoked.    3. If the consent has expired, then status&#x3D;EXPIRED, and consentId specifies which consent artefact has expired. Note, this is also responsibility of the HIP to keep track of consent expiry. Any data request on expired consent artefact must not be done.  

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.CmFacingApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_HIP_ID = "X_HIP_ID_example"; // String | Identifier of the health information provider to which the request was intended.
let hIPConsentNotification = new Gateway.HIPConsentNotification(); // HIPConsentNotification | 
apiInstance.v05ConsentsHipNotifyPost_0(authorization, X_HIP_ID, hIPConsentNotification, (error, data, response) => {
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
 **hIPConsentNotification** | [**HIPConsentNotification**](HIPConsentNotification.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05ConsentsHiuNotifyPost_0

> v05ConsentsHiuNotifyPost_0(authorization, X_HIU_ID, hIUConsentNotificationEvent)

Consent notification

Health information user will get notified about the consent request granted or denied, consent revoked, consent expired.  1. For consent request grant, status&#x3D;GRANTED, consentRequestId&#x3D;&lt;consent-request-id&gt;, and consentArtefacts is an array of generated consent artefact Ids. 2. For consent request expiry, status&#x3D;EXPIRED, consentRequestId&#x3D;&lt;consent-request-id&gt; 3. For consent request denied, status&#x3D;DENIED, consentRequestId&#x3D;&lt;consent-request-id&gt; 4. For consent revocation, status&#x3D;REVOKED, consentArtefacts is an array of revoked consent artefact ids 

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.CmFacingApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_HIU_ID = "X_HIU_ID_example"; // String | Identifier of the health information user to which the request was intended.
let hIUConsentNotificationEvent = new Gateway.HIUConsentNotificationEvent(); // HIUConsentNotificationEvent | 
apiInstance.v05ConsentsHiuNotifyPost_0(authorization, X_HIU_ID, hIUConsentNotificationEvent, (error, data, response) => {
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
 **hIUConsentNotificationEvent** | [**HIUConsentNotificationEvent**](HIUConsentNotificationEvent.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/xml


## v05ConsentsOnFetchPost_0

> v05ConsentsOnFetchPost_0(authorization, X_HIU_ID, consentArtefactResponse)

Result of fetch request for a consent artefact

Must contain either consentDetail or error. Possible reason of errors are  1. consentId passed through /fetch is invalid 

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.CmFacingApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_HIU_ID = "X_HIU_ID_example"; // String | Identifier of the health information user to which the request was intended.
let consentArtefactResponse = new Gateway.ConsentArtefactResponse(); // ConsentArtefactResponse | 
apiInstance.v05ConsentsOnFetchPost_0(authorization, X_HIU_ID, consentArtefactResponse, (error, data, response) => {
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
 **consentArtefactResponse** | [**ConsentArtefactResponse**](ConsentArtefactResponse.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05HealthInformationCmOnRequestPost_0

> v05HealthInformationCmOnRequestPost_0(authorization, X_HIU_ID, hIUHealthInformationRequestResponse)

Health information data request

Callback API for acknowledgement of Health information request of HIU. CM calls this API when it has validated the Health Information request given the consent id. Either the **hiRequest** or **error** would need to be specified. If the health info request was valid, then the ***hiRequest.transactionId*** specifies the transaction context against which HIP would send over the data.  Possible cases of errors are   1. **Invalid consent artefact id**   2. **Consent has expired**   3. **Date ranges are invalid** 

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.CmFacingApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_HIU_ID = "X_HIU_ID_example"; // String | Identifier of the health information user to which the request was intended.
let hIUHealthInformationRequestResponse = new Gateway.HIUHealthInformationRequestResponse(); // HIUHealthInformationRequestResponse | 
apiInstance.v05HealthInformationCmOnRequestPost_0(authorization, X_HIU_ID, hIUHealthInformationRequestResponse, (error, data, response) => {
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


## v05HealthInformationHipRequestPost_0

> v05HealthInformationHipRequestPost_0(authorization, X_HIP_ID, hIPHIRequest)

Health information data request

API called by CM to request Health information from HIP against a validated consent artefact. The transactionId is the correlation id that HIP should use use when pushing data to the **dataPushUrl**.  

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.CmFacingApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_HIP_ID = "X_HIP_ID_example"; // String | Identifier of the health information provider to which the request was intended.
let hIPHIRequest = new Gateway.HIPHIRequest(); // HIPHIRequest | 
apiInstance.v05HealthInformationHipRequestPost_0(authorization, X_HIP_ID, hIPHIRequest, (error, data, response) => {
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


## v05LinksLinkConfirmPost_0

> v05LinksLinkConfirmPost_0(authorization, X_HIP_ID, linkConfirmationRequest)

Token submission by Consent Manager for link confirmation

API to submit the token that was sent by HIP during the link request.  

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.CmFacingApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_HIP_ID = "X_HIP_ID_example"; // String | Identifier of the health information provider to which the request was intended.
let linkConfirmationRequest = new Gateway.LinkConfirmationRequest(); // LinkConfirmationRequest | 
apiInstance.v05LinksLinkConfirmPost_0(authorization, X_HIP_ID, linkConfirmationRequest, (error, data, response) => {
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


## v05LinksLinkInitPost_0

> v05LinksLinkInitPost_0(authorization, X_HIP_ID, patientLinkReferenceRequest)

Link patient&#39;s care contexts

Request from CM to links care contexts associated with only one patient   1. **Validate account reference number and care context reference number**   2. **Validate transactionId in the request with discovery request entry to check whether there was a discovery       and were these care contexts discovered or not for a given patient**   3. **Before eventual link confirmation, HIP needs to authenticate the request with the patient(eg: OTP verification)**   4. **HIP should communicate the mode of authentication of a successful request to Consent Manager** 

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.CmFacingApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_HIP_ID = "X_HIP_ID_example"; // String | Identifier of the health information provider to which the request was intended.
let patientLinkReferenceRequest = new Gateway.PatientLinkReferenceRequest(); // PatientLinkReferenceRequest | 
apiInstance.v05LinksLinkInitPost_0(authorization, X_HIP_ID, patientLinkReferenceRequest, (error, data, response) => {
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


## v05LinksLinkOnAddContextsPost_0

> v05LinksLinkOnAddContextsPost_0(authorization, X_HIP_ID, patientCareContextLinkResponse)

callback API for HIP initiated patient linking /link/add-context

If the accessToken is valid for purpose of linking, and specified details provided, CM will send \&quot;acknoweldgement.status\&quot; as SUCCESS. If any error occcurred, for example invalid token, or other required patient or care-context information not provided, then \&quot;error\&quot; attribute conveys so.    1. **accessToken must be valid and must be for the purpose of linking** 

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.CmFacingApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_HIP_ID = "X_HIP_ID_example"; // String | Identifier of the health information provider to which the request was intended.
let patientCareContextLinkResponse = new Gateway.PatientCareContextLinkResponse(); // PatientCareContextLinkResponse | 
apiInstance.v05LinksLinkOnAddContextsPost_0(authorization, X_HIP_ID, patientCareContextLinkResponse, (error, data, response) => {
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


## v05PatientsOnFindPost_0

> v05PatientsOnFindPost_0(authorization, patientIdentificationResponse)

Identification result for a consent-manager user-id

If a patient is found then patient.name contains the patients name.  Otherwise, patient is not provided, and possibly error is raised for invalid requests Note in addition to the \&quot;Authorization\&quot; header, one of the following headers must be specified 1. specify **X-HIU-ID** if the requester is HIU (identified from /find requester.id) 2. specify **X-HIP-ID** if the requester is HIP (identified from /find requester.id) 

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.CmFacingApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let patientIdentificationResponse = new Gateway.PatientIdentificationResponse(); // PatientIdentificationResponse | 
apiInstance.v05PatientsOnFindPost_0(authorization, patientIdentificationResponse, (error, data, response) => {
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
 **patientIdentificationResponse** | [**PatientIdentificationResponse**](PatientIdentificationResponse.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05PatientsProfileSharePost_0

> v05PatientsProfileSharePost_0(authorization, X_HIP_ID, shareProfileRequest)

Share patient profile details

Request for sharing patient&#39;s profile details to HIP 

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.CmFacingApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_HIP_ID = "X_HIP_ID_example"; // String | Identifier of the health information provider to which the request was intended.
let shareProfileRequest = new Gateway.ShareProfileRequest(); // ShareProfileRequest | 
apiInstance.v05PatientsProfileSharePost_0(authorization, X_HIP_ID, shareProfileRequest, (error, data, response) => {
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
 **shareProfileRequest** | [**ShareProfileRequest**](ShareProfileRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05PatientsSmsOnNotifyPost

> v05PatientsSmsOnNotifyPost(authorization, X_HIP_ID, patientSMSNotifcationResponse)

Acknowledgment response for SMS notification sent to patient by HIP

If the SMS notification is successfully sent to patient then \&quot;status\&quot; will be \&quot;ACKNOWLEDGED\&quot; with no error. If the SMS notification is failed then \&quot;status\&quot; will be \&quot;ERRORED\&quot; with error. 

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.CmFacingApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_HIP_ID = "X_HIP_ID_example"; // String | Identifier of the health information provider to which the request was intended.
let patientSMSNotifcationResponse = new Gateway.PatientSMSNotifcationResponse(); // PatientSMSNotifcationResponse | 
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


## v05SubscriptionRequestsCmOnInitPost_0

> v05SubscriptionRequestsCmOnInitPost_0(authorization, X_HIU_ID, hIUSubscriptionRequestReceipt)

callback API for the /subscription-requests/cm/init to notify a HIU on acceptance/acknowledgement of the request for subscription.

This callback API acknowledges the request for subscription from a HIU, and sends back a \&quot;id\&quot; that will be used when the patient/user approves or denies the subscription.  

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.CmFacingApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_HIU_ID = "X_HIU_ID_example"; // String | Identifier of the health information user to which the request was intended.
let hIUSubscriptionRequestReceipt = new Gateway.HIUSubscriptionRequestReceipt(); // HIUSubscriptionRequestReceipt | 
apiInstance.v05SubscriptionRequestsCmOnInitPost_0(authorization, X_HIU_ID, hIUSubscriptionRequestReceipt, (error, data, response) => {
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
 **hIUSubscriptionRequestReceipt** | [**HIUSubscriptionRequestReceipt**](HIUSubscriptionRequestReceipt.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/xml


## v05SubscriptionRequestsHiuNotifyPost_0

> v05SubscriptionRequestsHiuNotifyPost_0(authorization, X_HIU_ID, subscriptionApprovalNotification)

Notification for subscription grant/deny/revoke

This API is used by CM to notify a HIU to grant or deny a request for subscription, and also to notify that in case an existing subscription is revoked or expired. For notifying that a particular subscription request was GRANTED or DENIED, the **subscriptionRequestId** is passed.  

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.CmFacingApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_HIU_ID = "X_HIU_ID_example"; // String | Identifier of the health information user to which the request was intended.
let subscriptionApprovalNotification = new Gateway.SubscriptionApprovalNotification(); // SubscriptionApprovalNotification | 
apiInstance.v05SubscriptionRequestsHiuNotifyPost_0(authorization, X_HIU_ID, subscriptionApprovalNotification, (error, data, response) => {
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
 **subscriptionApprovalNotification** | [**SubscriptionApprovalNotification**](SubscriptionApprovalNotification.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05SubscriptionsHiuNotifyPost_0

> v05SubscriptionsHiuNotifyPost_0(authorization, X_HIU_ID, hIUSubscriptionNotification)

Notification to HIU on basis of a granted subscription

This API is used by CM to notify a HIU for notification relevant to subscription. Notifications are sent to subscribed HIUs whenever a new care-context is linked or new data is available on an existing linked care-context.  1. if event.category &#x3D; LINK, then only care-contexts are passed when new care-contexts are linked for patient.  2. If event.category &#x3D; DATA, then hiTypes are passed. Care-context is passed only if the subscribed HIU has any valid consent for that care-context 

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.CmFacingApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_HIU_ID = "X_HIU_ID_example"; // String | Identifier of the health information user to which the request was intended.
let hIUSubscriptionNotification = new Gateway.HIUSubscriptionNotification(); // HIUSubscriptionNotification | 
apiInstance.v05SubscriptionsHiuNotifyPost_0(authorization, X_HIU_ID, hIUSubscriptionNotification, (error, data, response) => {
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
 **hIUSubscriptionNotification** | [**HIUSubscriptionNotification**](HIUSubscriptionNotification.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05UsersAuthNotifyPost_0

> v05UsersAuthNotifyPost_0(authorization, X_HIP_ID, X_HIU_ID, patientAuthNotification)

notification API in case of DIRECT mode of authentication by the CM

This API is called by CM to confirm authentication of users. The transactionId returned is same as that passed in /auth/on-init. The \&quot;auth.status\&quot; conveys whether the request was GRANTED or DENIED.    1. **auth.accessToken** - is specific to the purpose mentioned in the /auth/init. This token needs to be used for initiating the intended action. For example for HIP initiated linking of care-contexts   2. **NOTE**, only one of **X-HIP-ID** or **X-HIU-ID** will be sent as part of header, not both.   3. The payload is conditional to the purpose of auth. If purpose specified in /auth/init is KYC or KYC_AND_LINK, then patient details are passed. **auth.accessToken** is passed only if the purpose is LINK or KYC_AND_LINK. 

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.CmFacingApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_HIP_ID = "X_HIP_ID_example"; // String | Identifier of the health information provider to which the request was intended.
let X_HIU_ID = "X_HIU_ID_example"; // String | Identifier of the health information user to which the request was intended.
let patientAuthNotification = new Gateway.PatientAuthNotification(); // PatientAuthNotification | 
apiInstance.v05UsersAuthNotifyPost_0(authorization, X_HIP_ID, X_HIU_ID, patientAuthNotification, (error, data, response) => {
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
 **X_HIU_ID** | **String**| Identifier of the health information user to which the request was intended. | 
 **patientAuthNotification** | [**PatientAuthNotification**](PatientAuthNotification.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05UsersAuthOnConfirmPost_0

> v05UsersAuthOnConfirmPost_0(authorization, X_HIP_ID, X_HIU_ID, patientAuthConfirmResponse)

callback API for /auth/confirm (in case of MEDIATED auth) to confirm user authentication or not

This API is called by CM to confirm authentication of users.    1. **auth.accessToken** - is specific to the purpose mentioned in the /auth/init. This token needs to be used for initiating the intended action. For example for HIP initiated linking of care-contexts   2. **NOTE**, only one of **X-HIP-ID** or **X-HIU-ID** will be sent as part of header, not both.      

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.CmFacingApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_HIP_ID = "X_HIP_ID_example"; // String | Identifier of the health information provider to which the request was intended.
let X_HIU_ID = "X_HIU_ID_example"; // String | Identifier of the health information user to which the request was intended.
let patientAuthConfirmResponse = new Gateway.PatientAuthConfirmResponse(); // PatientAuthConfirmResponse | 
apiInstance.v05UsersAuthOnConfirmPost_0(authorization, X_HIP_ID, X_HIU_ID, patientAuthConfirmResponse, (error, data, response) => {
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
 **X_HIU_ID** | **String**| Identifier of the health information user to which the request was intended. | 
 **patientAuthConfirmResponse** | [**PatientAuthConfirmResponse**](PatientAuthConfirmResponse.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05UsersAuthOnFetchModesPost_0

> v05UsersAuthOnFetchModesPost_0(authorization, X_HIP_ID, X_HIU_ID, patientAuthModeQueryResponse)

Identification result for a consent-manager user-id

If a patient is found then **auth** attribute contains the supported modes for the specified purpose.  Otherwise, error is raised for invalid requests or for non-existent id. Note in addition to the \&quot;Authorization\&quot; header, one of the following headers must be specified 1. **X-HIU-ID** if the requester is HIU (identified from /auth/fetch-modes requester.id) 2. **X-HIP-ID** if the requester is HIP (identified from /auth/fetch-modes requester.id) 

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.CmFacingApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_HIP_ID = "X_HIP_ID_example"; // String | Identifier of the health information provider to which the request was intended.
let X_HIU_ID = "X_HIU_ID_example"; // String | Identifier of the health information user to which the request was intended.
let patientAuthModeQueryResponse = new Gateway.PatientAuthModeQueryResponse(); // PatientAuthModeQueryResponse | 
apiInstance.v05UsersAuthOnFetchModesPost_0(authorization, X_HIP_ID, X_HIU_ID, patientAuthModeQueryResponse, (error, data, response) => {
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
 **X_HIU_ID** | **String**| Identifier of the health information user to which the request was intended. | 
 **patientAuthModeQueryResponse** | [**PatientAuthModeQueryResponse**](PatientAuthModeQueryResponse.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05UsersAuthOnInitPost_0

> v05UsersAuthOnInitPost_0(authorization, X_HIP_ID, X_HIU_ID, patientAuthInitResponse)

Response to user authentication initialization from HIP

If the patient&#39;s id is valid, CM will return a transactionId as initialization of user auth. If the request is valid, then &#39;auth.mode&#39; will convey how the authentication should be done. The authentication can be *mediated* or *direct*. For mediated authentication modes, HIP or HIU is epected to send over relevant code (OTP/token) or demographic info via subsequent API call to /auth/confirm. for direct authentication case, CM will notify requester through/users/auth/notify API.     1. **auth.mode** conveys whats the mode of authentication is, and what is expected from HIP/HIU in the subsequent /auth/confirm API call. Possible values        1. MOBILE_OTP - auth via OTP to registered mobile. Mediated.        2. AADHAAR_OTP - auth initiated with Aadhaar with OTP. Mediated.        3. DEMOGRAPHICS - auth initiated with demographic verification       4. DIRECT - for authentication directly with the patient. e.g. Mobile App, SMS. In this case, the HIP/HIU is not expected to call subsequent /auth/confirm call. CM will do direct authentication with the User (e.g. Mobile App, SMS etc) and will notify requester   2. **meta.expiry** conveys the expiry time of the token and the authentication session   3. **NOTE**, only one of **X-HIP-ID** or **X-HIU-ID** will be sent as part of header, not both.                         The error section in the body, represents the potential errors that may have occurred. Possible reasons:   1. Patient id is invalid 

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.CmFacingApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_HIP_ID = "X_HIP_ID_example"; // String | Identifier of the health information provider to which the request was intended.
let X_HIU_ID = "X_HIU_ID_example"; // String | Identifier of the health information user to which the request was intended.
let patientAuthInitResponse = new Gateway.PatientAuthInitResponse(); // PatientAuthInitResponse | 
apiInstance.v05UsersAuthOnInitPost_0(authorization, X_HIP_ID, X_HIU_ID, patientAuthInitResponse, (error, data, response) => {
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
 **X_HIU_ID** | **String**| Identifier of the health information user to which the request was intended. | 
 **patientAuthInitResponse** | [**PatientAuthInitResponse**](PatientAuthInitResponse.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

