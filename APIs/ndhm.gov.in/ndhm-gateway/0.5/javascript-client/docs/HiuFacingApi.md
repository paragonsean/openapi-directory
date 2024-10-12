# Gateway.HiuFacingApi

All URIs are relative to *https://dev.ndhm.gov.in/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05ConsentRequestsInitPost_0**](HiuFacingApi.md#v05ConsentRequestsInitPost_0) | **POST** /v0.5/consent-requests/init | Create consent request
[**v05ConsentRequestsStatusPost_0**](HiuFacingApi.md#v05ConsentRequestsStatusPost_0) | **POST** /v0.5/consent-requests/status | Get consent request status
[**v05ConsentsFetchPost_0**](HiuFacingApi.md#v05ConsentsFetchPost_0) | **POST** /v0.5/consents/fetch | Get consent artefact
[**v05ConsentsHiuOnNotifyPost_0**](HiuFacingApi.md#v05ConsentsHiuOnNotifyPost_0) | **POST** /v0.5/consents/hiu/on-notify | Consent notification
[**v05HealthInformationCmRequestPost_0**](HiuFacingApi.md#v05HealthInformationCmRequestPost_0) | **POST** /v0.5/health-information/cm/request | Health information data request
[**v05HealthInformationNotifyPost_1**](HiuFacingApi.md#v05HealthInformationNotifyPost_1) | **POST** /v0.5/health-information/notify | Notifications corresponding to events during data flow
[**v05PatientsFindPost_0**](HiuFacingApi.md#v05PatientsFindPost_0) | **POST** /v0.5/patients/find | Identify a patient by her consent-manager user-id
[**v05SubscriptionRequestsCmInitPost_0**](HiuFacingApi.md#v05SubscriptionRequestsCmInitPost_0) | **POST** /v0.5/subscription-requests/cm/init | Request for subscription
[**v05SubscriptionRequestsHiuOnNotifyPost_0**](HiuFacingApi.md#v05SubscriptionRequestsHiuOnNotifyPost_0) | **POST** /v0.5/subscription-requests/hiu/on-notify | Callback API for /subscription-requests/hiu/notify to acknowledge receipt of notification.
[**v05SubscriptionsHiuOnNotifyPost_0**](HiuFacingApi.md#v05SubscriptionsHiuOnNotifyPost_0) | **POST** /v0.5/subscriptions/hiu/on-notify | Callback API for /subscriptions/hiu/notify to acknowledge receipt of notification.
[**v05UsersAuthConfirmPost_1**](HiuFacingApi.md#v05UsersAuthConfirmPost_1) | **POST** /v0.5/users/auth/confirm | Confirmation request sending token, otp or other authentication details from HIP/HIU for confirmation
[**v05UsersAuthFetchModesPost_1**](HiuFacingApi.md#v05UsersAuthFetchModesPost_1) | **POST** /v0.5/users/auth/fetch-modes | Get a patient&#39;s authentication modes relevant to specified purpose
[**v05UsersAuthInitPost_1**](HiuFacingApi.md#v05UsersAuthInitPost_1) | **POST** /v0.5/users/auth/init | Initialize authentication from HIP
[**v05UsersAuthOnNotifyPost_1**](HiuFacingApi.md#v05UsersAuthOnNotifyPost_1) | **POST** /v0.5/users/auth/on-notify | callback API by HIU/HIPs as acknowledgement of auth notification



## v05ConsentRequestsInitPost_0

> v05ConsentRequestsInitPost_0(authorization, X_CM_ID, consentRequest)

Create consent request

Creates a consent request to get data about a patient by HIU user.

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.HiuFacingApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
let consentRequest = new Gateway.ConsentRequest(); // ConsentRequest | 
apiInstance.v05ConsentRequestsInitPost_0(authorization, X_CM_ID, consentRequest, (error, data, response) => {
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
 **consentRequest** | [**ConsentRequest**](ConsentRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05ConsentRequestsStatusPost_0

> v05ConsentRequestsStatusPost_0(authorization, X_CM_ID, consentRequestStatusRequest)

Get consent request status

Get status of consent request done previously

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.HiuFacingApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
let consentRequestStatusRequest = new Gateway.ConsentRequestStatusRequest(); // ConsentRequestStatusRequest | 
apiInstance.v05ConsentRequestsStatusPost_0(authorization, X_CM_ID, consentRequestStatusRequest, (error, data, response) => {
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
 **consentRequestStatusRequest** | [**ConsentRequestStatusRequest**](ConsentRequestStatusRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05ConsentsFetchPost_0

> v05ConsentsFetchPost_0(authorization, X_CM_ID, consentFetchRequest)

Get consent artefact

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.HiuFacingApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
let consentFetchRequest = new Gateway.ConsentFetchRequest(); // ConsentFetchRequest | 
apiInstance.v05ConsentsFetchPost_0(authorization, X_CM_ID, consentFetchRequest, (error, data, response) => {
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
 **consentFetchRequest** | [**ConsentFetchRequest**](ConsentFetchRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/xml


## v05ConsentsHiuOnNotifyPost_0

> v05ConsentsHiuOnNotifyPost_0(authorization, X_CM_ID, hIUConsentNotificationResponse)

Consent notification

This API is called by HIU as acknowledgement to consent notifications, specifically for cases when consent is REVOKED or EXPIRED. 

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.HiuFacingApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
let hIUConsentNotificationResponse = new Gateway.HIUConsentNotificationResponse(); // HIUConsentNotificationResponse | 
apiInstance.v05ConsentsHiuOnNotifyPost_0(authorization, X_CM_ID, hIUConsentNotificationResponse, (error, data, response) => {
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
 **hIUConsentNotificationResponse** | [**HIUConsentNotificationResponse**](HIUConsentNotificationResponse.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/xml


## v05HealthInformationCmRequestPost_0

> v05HealthInformationCmRequestPost_0(authorization, X_CM_ID, hIRequest)

Health information data request

Request for Health information against a consent id. CM would generate a transactionId against each consent and pass it as trnasaction context / correlation id to the HIP and also return the same to HIU via /on-request.  

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.HiuFacingApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
let hIRequest = new Gateway.HIRequest(); // HIRequest | 
apiInstance.v05HealthInformationCmRequestPost_0(authorization, X_CM_ID, hIRequest, (error, data, response) => {
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


## v05HealthInformationNotifyPost_1

> v05HealthInformationNotifyPost_1(authorization, X_CM_ID, healthInformationNotification)

Notifications corresponding to events during data flow

API called by HIU and HIP during data-transfer.  1. HIP on transfer of data would send **sessionStatus** - one of [TRANSFERRED, FAILED] 2. HIP would also send **hiStatus** for each *careContextReference* - on of [DELIVERED, ERRORED] 3. HIU on receipt of data would send **sessionStatus** - one of [TRANSFERRED, FAILED]. For example, FAILED when if data was not sent or if invalid data was sent 4. HIU would also send **hiStatus** for each *careContextReference* - one of [OK, ERRORED]  

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.HiuFacingApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
let healthInformationNotification = new Gateway.HealthInformationNotification(); // HealthInformationNotification | 
apiInstance.v05HealthInformationNotifyPost_1(authorization, X_CM_ID, healthInformationNotification, (error, data, response) => {
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


## v05PatientsFindPost_0

> v05PatientsFindPost_0(authorization, X_CM_ID, patientIdentificationRequest)

Identify a patient by her consent-manager user-id

This API is meant for identify to patient given her consent-manager-user-id 

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.HiuFacingApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
let patientIdentificationRequest = new Gateway.PatientIdentificationRequest(); // PatientIdentificationRequest | 
apiInstance.v05PatientsFindPost_0(authorization, X_CM_ID, patientIdentificationRequest, (error, data, response) => {
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
 **patientIdentificationRequest** | [**PatientIdentificationRequest**](PatientIdentificationRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05SubscriptionRequestsCmInitPost_0

> v05SubscriptionRequestsCmInitPost_0(authorization, X_CM_ID, subscriptionRequest)

Request for subscription

creates a request for subscription. The subscription categories can be for care-contexts linkages or availability of data against existing care-contexts. Note that the requester must have HIU role

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.HiuFacingApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
let subscriptionRequest = new Gateway.SubscriptionRequest(); // SubscriptionRequest | 
apiInstance.v05SubscriptionRequestsCmInitPost_0(authorization, X_CM_ID, subscriptionRequest, (error, data, response) => {
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
 **subscriptionRequest** | [**SubscriptionRequest**](SubscriptionRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05SubscriptionRequestsHiuOnNotifyPost_0

> v05SubscriptionRequestsHiuOnNotifyPost_0(authorization, X_CM_ID, hIUSubscriptionRequestNotificationAcknowledgement)

Callback API for /subscription-requests/hiu/notify to acknowledge receipt of notification.

This API is called by HIU as acknowledgement to subscription request relevant notifications.  

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.HiuFacingApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
let hIUSubscriptionRequestNotificationAcknowledgement = new Gateway.HIUSubscriptionRequestNotificationAcknowledgement(); // HIUSubscriptionRequestNotificationAcknowledgement | 
apiInstance.v05SubscriptionRequestsHiuOnNotifyPost_0(authorization, X_CM_ID, hIUSubscriptionRequestNotificationAcknowledgement, (error, data, response) => {
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
 **hIUSubscriptionRequestNotificationAcknowledgement** | [**HIUSubscriptionRequestNotificationAcknowledgement**](HIUSubscriptionRequestNotificationAcknowledgement.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/xml


## v05SubscriptionsHiuOnNotifyPost_0

> v05SubscriptionsHiuOnNotifyPost_0(authorization, X_CM_ID, hIUSubscriptionNotificationAcknowledgment)

Callback API for /subscriptions/hiu/notify to acknowledge receipt of notification.

This API is called by HIU as acknowledgement to consent notifications, specifically for cases when consent is REVOKED or EXPIRED. 

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.HiuFacingApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
let hIUSubscriptionNotificationAcknowledgment = new Gateway.HIUSubscriptionNotificationAcknowledgment(); // HIUSubscriptionNotificationAcknowledgment | 
apiInstance.v05SubscriptionsHiuOnNotifyPost_0(authorization, X_CM_ID, hIUSubscriptionNotificationAcknowledgment, (error, data, response) => {
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
 **hIUSubscriptionNotificationAcknowledgment** | [**HIUSubscriptionNotificationAcknowledgment**](HIUSubscriptionNotificationAcknowledgment.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/xml


## v05UsersAuthConfirmPost_1

> v05UsersAuthConfirmPost_1(authorization, X_CM_ID, patientAuthConfirmRequest)

Confirmation request sending token, otp or other authentication details from HIP/HIU for confirmation

This API is called by HIP/HIUs to confirm authentication of users. The transactionId returned by the previous callback API /users/auth/on-init must be sent. If Authentication is successful the callback API will send an \&quot;access token\&quot; for subsequent purpose specific API calls. Note only **credential.authCode** or **credential.demographic** should be sent   1. demographic details are only required for  demographic auth as of now.    2. demographic details are required only in MEDIATED cases and if the **auth.mode** so demands. e.g. if **auth.mode** is DEMOGRAPHICS. Usually for demographic authentication, the name, gender and DOB must be exactly as specified in User Account.   3. demographic.identifier is optional, however maybe required if authentication so mandates.    4. credential.authCode is required for other MEDIATED authentication like MOBILE_OTP, AADHAAR_OTP.  

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.HiuFacingApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
let patientAuthConfirmRequest = new Gateway.PatientAuthConfirmRequest(); // PatientAuthConfirmRequest | 
apiInstance.v05UsersAuthConfirmPost_1(authorization, X_CM_ID, patientAuthConfirmRequest, (error, data, response) => {
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
 **patientAuthConfirmRequest** | [**PatientAuthConfirmRequest**](PatientAuthConfirmRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05UsersAuthFetchModesPost_1

> v05UsersAuthFetchModesPost_1(authorization, X_CM_ID, patientAuthModeQueryRequest)

Get a patient&#39;s authentication modes relevant to specified purpose

This API is meant for identify supported authentication modes for a patient given a specific purpose 

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.HiuFacingApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
let patientAuthModeQueryRequest = new Gateway.PatientAuthModeQueryRequest(); // PatientAuthModeQueryRequest | 
apiInstance.v05UsersAuthFetchModesPost_1(authorization, X_CM_ID, patientAuthModeQueryRequest, (error, data, response) => {
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
 **patientAuthModeQueryRequest** | [**PatientAuthModeQueryRequest**](PatientAuthModeQueryRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05UsersAuthInitPost_1

> v05UsersAuthInitPost_1(authorization, X_CM_ID, patientAuthInitRequest)

Initialize authentication from HIP

This API is called by HIPs to initiate authentication of users. A transactionId is retuned by the corresponding callback API for confirmation of user auth. 

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.HiuFacingApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
let patientAuthInitRequest = new Gateway.PatientAuthInitRequest(); // PatientAuthInitRequest | 
apiInstance.v05UsersAuthInitPost_1(authorization, X_CM_ID, patientAuthInitRequest, (error, data, response) => {
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
 **patientAuthInitRequest** | [**PatientAuthInitRequest**](PatientAuthInitRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05UsersAuthOnNotifyPost_1

> v05UsersAuthOnNotifyPost_1(authorization, X_CM_ID, patientAuthNotificationAcknowledgement)

callback API by HIU/HIPs as acknowledgement of auth notification

This API is called by HIU/HIPs to confirm acknowledgement for receipt of auth notification is case of DIRECT authentication.  

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.HiuFacingApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
let patientAuthNotificationAcknowledgement = new Gateway.PatientAuthNotificationAcknowledgement(); // PatientAuthNotificationAcknowledgement | 
apiInstance.v05UsersAuthOnNotifyPost_1(authorization, X_CM_ID, patientAuthNotificationAcknowledgement, (error, data, response) => {
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
 **patientAuthNotificationAcknowledgement** | [**PatientAuthNotificationAcknowledgement**](PatientAuthNotificationAcknowledgement.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

