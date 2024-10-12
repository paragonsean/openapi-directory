# HealthRepositoryProviderSpecificationsForHiu.ConsentFlowApi

All URIs are relative to *https://dev.ndhm.gov.in/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05ConsentRequestsOnInitPost**](ConsentFlowApi.md#v05ConsentRequestsOnInitPost) | **POST** /v0.5/consent-requests/on-init | Response to consent request
[**v05ConsentRequestsOnStatusPost**](ConsentFlowApi.md#v05ConsentRequestsOnStatusPost) | **POST** /v0.5/consent-requests/on-status | Result of consent request status
[**v05ConsentsHiuNotifyPost**](ConsentFlowApi.md#v05ConsentsHiuNotifyPost) | **POST** /v0.5/consents/hiu/notify | Consent notification
[**v05ConsentsOnFetchPost**](ConsentFlowApi.md#v05ConsentsOnFetchPost) | **POST** /v0.5/consents/on-fetch | Result of fetch request for a consent artefact



## v05ConsentRequestsOnInitPost

> v05ConsentRequestsOnInitPost(authorization, X_HIU_ID, consentRequestInitResponse)

Response to consent request

Result of consent request creation for a patient. **id** represents the consentrequest id created by CM. The result must contain either **id** or the **error** caused. &lt;br/&gt;   Reasons for error may be   * Invalid references (e.g patient id, hiu id), purpose, hiTypes, ranges, persmission 

### Example

```javascript
import HealthRepositoryProviderSpecificationsForHiu from 'health_repository_provider_specifications_for_hiu';

let apiInstance = new HealthRepositoryProviderSpecificationsForHiu.ConsentFlowApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
let X_HIU_ID = "X_HIU_ID_example"; // String | Identifier of the health information user to which the request was intended.
let consentRequestInitResponse = new HealthRepositoryProviderSpecificationsForHiu.ConsentRequestInitResponse(); // ConsentRequestInitResponse | 
apiInstance.v05ConsentRequestsOnInitPost(authorization, X_HIU_ID, consentRequestInitResponse, (error, data, response) => {
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
 **X_HIU_ID** | **String**| Identifier of the health information user to which the request was intended. | 
 **consentRequestInitResponse** | [**ConsentRequestInitResponse**](ConsentRequestInitResponse.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05ConsentRequestsOnStatusPost

> v05ConsentRequestsOnStatusPost(authorization, X_HIU_ID, hIUConsentRequestStatus)

Result of consent request status

Result of consent request done previously. Status of request can be GRANTED,  DENIED, EXPIRED. If the request was GRANTED, then  

### Example

```javascript
import HealthRepositoryProviderSpecificationsForHiu from 'health_repository_provider_specifications_for_hiu';

let apiInstance = new HealthRepositoryProviderSpecificationsForHiu.ConsentFlowApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
let X_HIU_ID = "X_HIU_ID_example"; // String | Identifier of the health information user to which the request was intended.
let hIUConsentRequestStatus = new HealthRepositoryProviderSpecificationsForHiu.HIUConsentRequestStatus(); // HIUConsentRequestStatus | 
apiInstance.v05ConsentRequestsOnStatusPost(authorization, X_HIU_ID, hIUConsentRequestStatus, (error, data, response) => {
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
 **X_HIU_ID** | **String**| Identifier of the health information user to which the request was intended. | 
 **hIUConsentRequestStatus** | [**HIUConsentRequestStatus**](HIUConsentRequestStatus.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05ConsentsHiuNotifyPost

> v05ConsentsHiuNotifyPost(authorization, X_HIU_ID, hIUConsentNotificationEvent)

Consent notification

Health information user will get notified about the consent request granted or denied, consent revoked, consent expired.  1. For consent request grant, status&#x3D;GRANTED, consentRequestId&#x3D;&lt;consent-request-id&gt;, and consentArtefacts is an array of generated consent artefact Ids. 2. For consent request expiry, status&#x3D;EXPIRED, consentRequestId&#x3D;&lt;consent-request-id&gt; 3. For consent request denied, status&#x3D;DENIED, consentRequestId&#x3D;&lt;consent-request-id&gt; 4. For consent revocation, status&#x3D;REVOKED, consentArtefacts is an array of revoked consent artefact ids 

### Example

```javascript
import HealthRepositoryProviderSpecificationsForHiu from 'health_repository_provider_specifications_for_hiu';

let apiInstance = new HealthRepositoryProviderSpecificationsForHiu.ConsentFlowApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
let X_HIU_ID = "X_HIU_ID_example"; // String | Identifier of the health information user to which the request was intended.
let hIUConsentNotificationEvent = new HealthRepositoryProviderSpecificationsForHiu.HIUConsentNotificationEvent(); // HIUConsentNotificationEvent | 
apiInstance.v05ConsentsHiuNotifyPost(authorization, X_HIU_ID, hIUConsentNotificationEvent, (error, data, response) => {
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
 **X_HIU_ID** | **String**| Identifier of the health information user to which the request was intended. | 
 **hIUConsentNotificationEvent** | [**HIUConsentNotificationEvent**](HIUConsentNotificationEvent.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/xml


## v05ConsentsOnFetchPost

> v05ConsentsOnFetchPost(authorization, X_HIU_ID, consentArtefactResponse)

Result of fetch request for a consent artefact

Must contain either consent or error. Possible reason of errors are  1. consentId passed through /fetch is invalid 

### Example

```javascript
import HealthRepositoryProviderSpecificationsForHiu from 'health_repository_provider_specifications_for_hiu';

let apiInstance = new HealthRepositoryProviderSpecificationsForHiu.ConsentFlowApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
let X_HIU_ID = "X_HIU_ID_example"; // String | Identifier of the health information user to which the request was intended.
let consentArtefactResponse = new HealthRepositoryProviderSpecificationsForHiu.ConsentArtefactResponse(); // ConsentArtefactResponse | 
apiInstance.v05ConsentsOnFetchPost(authorization, X_HIU_ID, consentArtefactResponse, (error, data, response) => {
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
 **X_HIU_ID** | **String**| Identifier of the health information user to which the request was intended. | 
 **consentArtefactResponse** | [**ConsentArtefactResponse**](ConsentArtefactResponse.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

