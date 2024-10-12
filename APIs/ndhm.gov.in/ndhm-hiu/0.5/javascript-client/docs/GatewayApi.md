# HealthRepositoryProviderSpecificationsForHiu.GatewayApi

All URIs are relative to *https://dev.ndhm.gov.in/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05CertsGet**](GatewayApi.md#v05CertsGet) | **GET** /v0.5/certs | Get certs for JWT verification
[**v05ConsentRequestsInitPost**](GatewayApi.md#v05ConsentRequestsInitPost) | **POST** /v0.5/consent-requests/init | Create consent request
[**v05ConsentRequestsStatusPost**](GatewayApi.md#v05ConsentRequestsStatusPost) | **POST** /v0.5/consent-requests/status | Get consent request status
[**v05ConsentsFetchPost**](GatewayApi.md#v05ConsentsFetchPost) | **POST** /v0.5/consents/fetch | Get consent artefact
[**v05ConsentsHiuOnNotifyPost**](GatewayApi.md#v05ConsentsHiuOnNotifyPost) | **POST** /v0.5/consents/hiu/on-notify | Consent notification
[**v05HealthInformationCmRequestPost**](GatewayApi.md#v05HealthInformationCmRequestPost) | **POST** /v0.5/health-information/cm/request | Health information data request
[**v05HealthInformationNotifyPost**](GatewayApi.md#v05HealthInformationNotifyPost) | **POST** /v0.5/health-information/notify | Notifications corresponding to events during data flow
[**v05PatientsFindPost**](GatewayApi.md#v05PatientsFindPost) | **POST** /v0.5/patients/find | Identify a patient by her consent-manager user-id
[**v05SessionsPost**](GatewayApi.md#v05SessionsPost) | **POST** /v0.5/sessions | Get access token
[**v05SubscriptionRequestsCmInitPost**](GatewayApi.md#v05SubscriptionRequestsCmInitPost) | **POST** /v0.5/subscription-requests/cm/init | Request for subscription
[**v05SubscriptionRequestsHiuOnNotifyPost**](GatewayApi.md#v05SubscriptionRequestsHiuOnNotifyPost) | **POST** /v0.5/subscription-requests/hiu/on-notify | Callback API for /subscription-requests/hiu/notify to acknowledge receipt of notification.
[**v05SubscriptionsHiuOnNotifyPost**](GatewayApi.md#v05SubscriptionsHiuOnNotifyPost) | **POST** /v0.5/subscriptions/hiu/on-notify | Callback API for /subscriptions/hiu/notify to acknowledge receipt of notification.
[**v05UsersAuthConfirmPost**](GatewayApi.md#v05UsersAuthConfirmPost) | **POST** /v0.5/users/auth/confirm | Confirmation request sending token, otp or other authentication details from HIP/HIU for confirmation
[**v05UsersAuthFetchModesPost**](GatewayApi.md#v05UsersAuthFetchModesPost) | **POST** /v0.5/users/auth/fetch-modes | Get a patient&#39;s authentication modes relevant to specified purpose
[**v05UsersAuthInitPost**](GatewayApi.md#v05UsersAuthInitPost) | **POST** /v0.5/users/auth/init | Initialize authentication from HIP
[**v05UsersAuthOnNotifyPost**](GatewayApi.md#v05UsersAuthOnNotifyPost) | **POST** /v0.5/users/auth/on-notify | callback API by HIU/HIPs as acknowledgement of auth notification
[**v05WellKnownOpenidConfigurationGet**](GatewayApi.md#v05WellKnownOpenidConfigurationGet) | **GET** /v0.5/.well-known/openid-configuration | Get openid configuration



## v05CertsGet

> Certs v05CertsGet()

Get certs for JWT verification

### Example

```javascript
import HealthRepositoryProviderSpecificationsForHiu from 'health_repository_provider_specifications_for_hiu';

let apiInstance = new HealthRepositoryProviderSpecificationsForHiu.GatewayApi();
apiInstance.v05CertsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**Certs**](Certs.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## v05ConsentRequestsInitPost

> v05ConsentRequestsInitPost(authorization, X_CM_ID, consentRequest)

Create consent request

Creates a consent request to get data about a patient by HIU user.

### Example

```javascript
import HealthRepositoryProviderSpecificationsForHiu from 'health_repository_provider_specifications_for_hiu';

let apiInstance = new HealthRepositoryProviderSpecificationsForHiu.GatewayApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
let X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
let consentRequest = new HealthRepositoryProviderSpecificationsForHiu.ConsentRequest(); // ConsentRequest | 
apiInstance.v05ConsentRequestsInitPost(authorization, X_CM_ID, consentRequest, (error, data, response) => {
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
 **X_CM_ID** | **String**| Suffix of the consent manager to which the request was intended. | 
 **consentRequest** | [**ConsentRequest**](ConsentRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05ConsentRequestsStatusPost

> v05ConsentRequestsStatusPost(authorization, X_CM_ID, consentRequestStatusRequest)

Get consent request status

Get status of consent request done previously

### Example

```javascript
import HealthRepositoryProviderSpecificationsForHiu from 'health_repository_provider_specifications_for_hiu';

let apiInstance = new HealthRepositoryProviderSpecificationsForHiu.GatewayApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
let X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
let consentRequestStatusRequest = new HealthRepositoryProviderSpecificationsForHiu.ConsentRequestStatusRequest(); // ConsentRequestStatusRequest | 
apiInstance.v05ConsentRequestsStatusPost(authorization, X_CM_ID, consentRequestStatusRequest, (error, data, response) => {
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
 **X_CM_ID** | **String**| Suffix of the consent manager to which the request was intended. | 
 **consentRequestStatusRequest** | [**ConsentRequestStatusRequest**](ConsentRequestStatusRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05ConsentsFetchPost

> v05ConsentsFetchPost(authorization, X_CM_ID, consentFetchRequest)

Get consent artefact

### Example

```javascript
import HealthRepositoryProviderSpecificationsForHiu from 'health_repository_provider_specifications_for_hiu';

let apiInstance = new HealthRepositoryProviderSpecificationsForHiu.GatewayApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
let X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
let consentFetchRequest = new HealthRepositoryProviderSpecificationsForHiu.ConsentFetchRequest(); // ConsentFetchRequest | 
apiInstance.v05ConsentsFetchPost(authorization, X_CM_ID, consentFetchRequest, (error, data, response) => {
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
 **X_CM_ID** | **String**| Suffix of the consent manager to which the request was intended. | 
 **consentFetchRequest** | [**ConsentFetchRequest**](ConsentFetchRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/xml


## v05ConsentsHiuOnNotifyPost

> v05ConsentsHiuOnNotifyPost(authorization, X_CM_ID, hIUConsentNotificationResponse)

Consent notification

This API is called by HIU as acknowledgement to consent notifications, specifically for cases when consent is REVOKED or EXPIRED. 

### Example

```javascript
import HealthRepositoryProviderSpecificationsForHiu from 'health_repository_provider_specifications_for_hiu';

let apiInstance = new HealthRepositoryProviderSpecificationsForHiu.GatewayApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
let X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
let hIUConsentNotificationResponse = new HealthRepositoryProviderSpecificationsForHiu.HIUConsentNotificationResponse(); // HIUConsentNotificationResponse | 
apiInstance.v05ConsentsHiuOnNotifyPost(authorization, X_CM_ID, hIUConsentNotificationResponse, (error, data, response) => {
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
 **X_CM_ID** | **String**| Suffix of the consent manager to which the request was intended. | 
 **hIUConsentNotificationResponse** | [**HIUConsentNotificationResponse**](HIUConsentNotificationResponse.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/xml


## v05HealthInformationCmRequestPost

> v05HealthInformationCmRequestPost(authorization, X_CM_ID, hIRequest)

Health information data request

Request for Health information against a consent id. CM would generate a transactionId against each consent and pass it as trnasaction context / correlation id to the HIP and also return the same to HIU via /on-request.  

### Example

```javascript
import HealthRepositoryProviderSpecificationsForHiu from 'health_repository_provider_specifications_for_hiu';

let apiInstance = new HealthRepositoryProviderSpecificationsForHiu.GatewayApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
let X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
let hIRequest = new HealthRepositoryProviderSpecificationsForHiu.HIRequest(); // HIRequest | 
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
 **authorization** | **String**| Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge. | 
 **X_CM_ID** | **String**| Suffix of the consent manager to which the request was intended. | 
 **hIRequest** | [**HIRequest**](HIRequest.md)|  | 

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

API called by HIU and HIP during data-transfer. 1. HIP on transfer of data would send **sessionStatus** - one of [TRANSFERRED, FAILED] 2. HIP would also send **hiStatus** for each *careContextReference* - on of [DELIVERED, ERRORED] 3. HIU on receipt of data would send **sessionStatus** - one of [TRANSFERRED, FAILED]. For example, FAILED when if data was not sent or if invalid data was sent 4. HIU would also send **hiStatus** for each *careContextReference* - one of [OK, ERRORED] 

### Example

```javascript
import HealthRepositoryProviderSpecificationsForHiu from 'health_repository_provider_specifications_for_hiu';

let apiInstance = new HealthRepositoryProviderSpecificationsForHiu.GatewayApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
let X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
let healthInformationNotification = new HealthRepositoryProviderSpecificationsForHiu.HealthInformationNotification(); // HealthInformationNotification | 
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
 **authorization** | **String**| Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge. | 
 **X_CM_ID** | **String**| Suffix of the consent manager to which the request was intended. | 
 **healthInformationNotification** | [**HealthInformationNotification**](HealthInformationNotification.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05PatientsFindPost

> v05PatientsFindPost(authorization, X_CM_ID, patientIdentificationRequest)

Identify a patient by her consent-manager user-id

This API is meant for identify to patient given her consent-manager-user-id 

### Example

```javascript
import HealthRepositoryProviderSpecificationsForHiu from 'health_repository_provider_specifications_for_hiu';

let apiInstance = new HealthRepositoryProviderSpecificationsForHiu.GatewayApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
let X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
let patientIdentificationRequest = new HealthRepositoryProviderSpecificationsForHiu.PatientIdentificationRequest(); // PatientIdentificationRequest | 
apiInstance.v05PatientsFindPost(authorization, X_CM_ID, patientIdentificationRequest, (error, data, response) => {
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
 **X_CM_ID** | **String**| Suffix of the consent manager to which the request was intended. | 
 **patientIdentificationRequest** | [**PatientIdentificationRequest**](PatientIdentificationRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05SessionsPost

> SessionResponse v05SessionsPost(sessionRequest)

Get access token

### Example

```javascript
import HealthRepositoryProviderSpecificationsForHiu from 'health_repository_provider_specifications_for_hiu';

let apiInstance = new HealthRepositoryProviderSpecificationsForHiu.GatewayApi();
let sessionRequest = new HealthRepositoryProviderSpecificationsForHiu.SessionRequest(); // SessionRequest | 
apiInstance.v05SessionsPost(sessionRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sessionRequest** | [**SessionRequest**](SessionRequest.md)|  | 

### Return type

[**SessionResponse**](SessionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05SubscriptionRequestsCmInitPost

> v05SubscriptionRequestsCmInitPost(authorization, X_CM_ID, subscriptionRequest)

Request for subscription

creates a request for subscription. The subscription categories can be for care-contexts linkages or availability of data against existing care-contexts. Note that the requester must have HIU role

### Example

```javascript
import HealthRepositoryProviderSpecificationsForHiu from 'health_repository_provider_specifications_for_hiu';

let apiInstance = new HealthRepositoryProviderSpecificationsForHiu.GatewayApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
let X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
let subscriptionRequest = new HealthRepositoryProviderSpecificationsForHiu.SubscriptionRequest(); // SubscriptionRequest | 
apiInstance.v05SubscriptionRequestsCmInitPost(authorization, X_CM_ID, subscriptionRequest, (error, data, response) => {
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
 **X_CM_ID** | **String**| Suffix of the consent manager to which the request was intended. | 
 **subscriptionRequest** | [**SubscriptionRequest**](SubscriptionRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05SubscriptionRequestsHiuOnNotifyPost

> v05SubscriptionRequestsHiuOnNotifyPost(authorization, X_CM_ID, hIUSubscriptionRequestNotificationAcknowledgement)

Callback API for /subscription-requests/hiu/notify to acknowledge receipt of notification.

This API is called by HIU as acknowledgement to subscription request relevant notifications.  

### Example

```javascript
import HealthRepositoryProviderSpecificationsForHiu from 'health_repository_provider_specifications_for_hiu';

let apiInstance = new HealthRepositoryProviderSpecificationsForHiu.GatewayApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
let X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
let hIUSubscriptionRequestNotificationAcknowledgement = new HealthRepositoryProviderSpecificationsForHiu.HIUSubscriptionRequestNotificationAcknowledgement(); // HIUSubscriptionRequestNotificationAcknowledgement | 
apiInstance.v05SubscriptionRequestsHiuOnNotifyPost(authorization, X_CM_ID, hIUSubscriptionRequestNotificationAcknowledgement, (error, data, response) => {
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
 **X_CM_ID** | **String**| Suffix of the consent manager to which the request was intended. | 
 **hIUSubscriptionRequestNotificationAcknowledgement** | [**HIUSubscriptionRequestNotificationAcknowledgement**](HIUSubscriptionRequestNotificationAcknowledgement.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/xml


## v05SubscriptionsHiuOnNotifyPost

> v05SubscriptionsHiuOnNotifyPost(authorization, X_CM_ID, hIUSubscriptionNotificationAcknowledgment)

Callback API for /subscriptions/hiu/notify to acknowledge receipt of notification.

This API is called by HIU as acknowledgement to consent notifications, specifically for cases when consent is REVOKED or EXPIRED. 

### Example

```javascript
import HealthRepositoryProviderSpecificationsForHiu from 'health_repository_provider_specifications_for_hiu';

let apiInstance = new HealthRepositoryProviderSpecificationsForHiu.GatewayApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
let X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
let hIUSubscriptionNotificationAcknowledgment = new HealthRepositoryProviderSpecificationsForHiu.HIUSubscriptionNotificationAcknowledgment(); // HIUSubscriptionNotificationAcknowledgment | 
apiInstance.v05SubscriptionsHiuOnNotifyPost(authorization, X_CM_ID, hIUSubscriptionNotificationAcknowledgment, (error, data, response) => {
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
 **X_CM_ID** | **String**| Suffix of the consent manager to which the request was intended. | 
 **hIUSubscriptionNotificationAcknowledgment** | [**HIUSubscriptionNotificationAcknowledgment**](HIUSubscriptionNotificationAcknowledgment.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/xml


## v05UsersAuthConfirmPost

> v05UsersAuthConfirmPost(authorization, X_CM_ID, patientAuthConfirmRequest)

Confirmation request sending token, otp or other authentication details from HIP/HIU for confirmation

This API is called by HIP/HIUs to confirm authentication of users. The transactionId returned by the previous callback API /users/auth/on-init must be sent. If Authentication is successful the callback API will send an \&quot;access token\&quot; for subsequent purpose specific API calls. Note only **credential.authCode** or **credential.demographic** should be sent   1. demographic details are only required for  demographic auth as of now.    2. demographic details are required only in MEDIATED cases and if the **auth.mode** so demands. e.g. if **auth.mode** is DEMOGRAPHICS. Usually for demographic authentication, the name, gender and DOB must be exactly as specified in User Account.   3. demographic.identifier is optional, however maybe required if authentication so mandates.    4. credential.authCode is required for other MEDIATED authentication like MOBILE_OTP, AADHAAR_OTP.  

### Example

```javascript
import HealthRepositoryProviderSpecificationsForHiu from 'health_repository_provider_specifications_for_hiu';

let apiInstance = new HealthRepositoryProviderSpecificationsForHiu.GatewayApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
let X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
let patientAuthConfirmRequest = new HealthRepositoryProviderSpecificationsForHiu.PatientAuthConfirmRequest(); // PatientAuthConfirmRequest | 
apiInstance.v05UsersAuthConfirmPost(authorization, X_CM_ID, patientAuthConfirmRequest, (error, data, response) => {
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
 **X_CM_ID** | **String**| Suffix of the consent manager to which the request was intended. | 
 **patientAuthConfirmRequest** | [**PatientAuthConfirmRequest**](PatientAuthConfirmRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05UsersAuthFetchModesPost

> v05UsersAuthFetchModesPost(authorization, X_CM_ID, patientAuthModeQueryRequest)

Get a patient&#39;s authentication modes relevant to specified purpose

This API is meant for identify supported authentication modes for a patient given a specific purpose 

### Example

```javascript
import HealthRepositoryProviderSpecificationsForHiu from 'health_repository_provider_specifications_for_hiu';

let apiInstance = new HealthRepositoryProviderSpecificationsForHiu.GatewayApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
let X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
let patientAuthModeQueryRequest = new HealthRepositoryProviderSpecificationsForHiu.PatientAuthModeQueryRequest(); // PatientAuthModeQueryRequest | 
apiInstance.v05UsersAuthFetchModesPost(authorization, X_CM_ID, patientAuthModeQueryRequest, (error, data, response) => {
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
 **X_CM_ID** | **String**| Suffix of the consent manager to which the request was intended. | 
 **patientAuthModeQueryRequest** | [**PatientAuthModeQueryRequest**](PatientAuthModeQueryRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05UsersAuthInitPost

> v05UsersAuthInitPost(authorization, X_CM_ID, patientAuthInitRequest)

Initialize authentication from HIP

This API is called by HIPs to initiate authentication of users. A transactionId is retuned by the corresponding callback API for confirmation of user auth.   1. **NOTE**, only **KYC** purpose is applicable for HIU. Hence HIU should only sent KYC in **query.authMode** in the request 

### Example

```javascript
import HealthRepositoryProviderSpecificationsForHiu from 'health_repository_provider_specifications_for_hiu';

let apiInstance = new HealthRepositoryProviderSpecificationsForHiu.GatewayApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
let X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
let patientAuthInitRequest = new HealthRepositoryProviderSpecificationsForHiu.PatientAuthInitRequest(); // PatientAuthInitRequest | 
apiInstance.v05UsersAuthInitPost(authorization, X_CM_ID, patientAuthInitRequest, (error, data, response) => {
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
 **X_CM_ID** | **String**| Suffix of the consent manager to which the request was intended. | 
 **patientAuthInitRequest** | [**PatientAuthInitRequest**](PatientAuthInitRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05UsersAuthOnNotifyPost

> v05UsersAuthOnNotifyPost(authorization, X_CM_ID, patientAuthNotificationAcknowledgement)

callback API by HIU/HIPs as acknowledgement of auth notification

This API is called by HIU/HIPs to confirm acknowledgement for receipt of auth notification is case of DIRECT authentication.  

### Example

```javascript
import HealthRepositoryProviderSpecificationsForHiu from 'health_repository_provider_specifications_for_hiu';

let apiInstance = new HealthRepositoryProviderSpecificationsForHiu.GatewayApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
let X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
let patientAuthNotificationAcknowledgement = new HealthRepositoryProviderSpecificationsForHiu.PatientAuthNotificationAcknowledgement(); // PatientAuthNotificationAcknowledgement | 
apiInstance.v05UsersAuthOnNotifyPost(authorization, X_CM_ID, patientAuthNotificationAcknowledgement, (error, data, response) => {
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
 **X_CM_ID** | **String**| Suffix of the consent manager to which the request was intended. | 
 **patientAuthNotificationAcknowledgement** | [**PatientAuthNotificationAcknowledgement**](PatientAuthNotificationAcknowledgement.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05WellKnownOpenidConfigurationGet

> OpenIdConfiguration v05WellKnownOpenidConfigurationGet()

Get openid configuration

### Example

```javascript
import HealthRepositoryProviderSpecificationsForHiu from 'health_repository_provider_specifications_for_hiu';

let apiInstance = new HealthRepositoryProviderSpecificationsForHiu.GatewayApi();
apiInstance.v05WellKnownOpenidConfigurationGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**OpenIdConfiguration**](OpenIdConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

