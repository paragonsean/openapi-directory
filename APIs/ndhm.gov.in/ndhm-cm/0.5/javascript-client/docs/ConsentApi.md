# HealthDataConsentManager.ConsentApi

All URIs are relative to *https://dev.ndhm.gov.in/cm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05ConsentRequestsInitPost**](ConsentApi.md#v05ConsentRequestsInitPost) | **POST** /v0.5/consent-requests/init | Create consent request
[**v05ConsentRequestsStatusPost**](ConsentApi.md#v05ConsentRequestsStatusPost) | **POST** /v0.5/consent-requests/status | Get consent request status
[**v05ConsentsFetchPost**](ConsentApi.md#v05ConsentsFetchPost) | **POST** /v0.5/consents/fetch | Get consent artefact
[**v05ConsentsHipOnNotifyPost**](ConsentApi.md#v05ConsentsHipOnNotifyPost) | **POST** /v0.5/consents/hip/on-notify | Consent notification
[**v05ConsentsHiuOnNotifyPost**](ConsentApi.md#v05ConsentsHiuOnNotifyPost) | **POST** /v0.5/consents/hiu/on-notify | Consent notification



## v05ConsentRequestsInitPost

> v05ConsentRequestsInitPost(authorization, consentRequest)

Create consent request

Creates a consent request to get data about a patient by HIU user. CM should call Gateway - ***_/v0.5/consent-requests/on-init*** API with the consent-request-id

### Example

```javascript
import HealthDataConsentManager from 'health_data_consent_manager';

let apiInstance = new HealthDataConsentManager.ConsentApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let consentRequest = new HealthDataConsentManager.ConsentRequest(); // ConsentRequest | 
apiInstance.v05ConsentRequestsInitPost(authorization, consentRequest, (error, data, response) => {
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
 **consentRequest** | [**ConsentRequest**](ConsentRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05ConsentRequestsStatusPost

> v05ConsentRequestsStatusPost(authorization, consentRequestStatusRequest)

Get consent request status

Get status of consent request done previously. CM responds by calling Gateway API - ***_/v0.5/consent-requests/on-status***

### Example

```javascript
import HealthDataConsentManager from 'health_data_consent_manager';

let apiInstance = new HealthDataConsentManager.ConsentApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let consentRequestStatusRequest = new HealthDataConsentManager.ConsentRequestStatusRequest(); // ConsentRequestStatusRequest | 
apiInstance.v05ConsentRequestsStatusPost(authorization, consentRequestStatusRequest, (error, data, response) => {
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
 **consentRequestStatusRequest** | [**ConsentRequestStatusRequest**](ConsentRequestStatusRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05ConsentsFetchPost

> v05ConsentsFetchPost(authorization, consentFetchRequest)

Get consent artefact

This API is called when a HIU makes a request to get a consent artefact. For response please refer to the Gateway ***_/v0.5/consents/on-fetch***

### Example

```javascript
import HealthDataConsentManager from 'health_data_consent_manager';

let apiInstance = new HealthDataConsentManager.ConsentApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let consentFetchRequest = new HealthDataConsentManager.ConsentFetchRequest(); // ConsentFetchRequest | 
apiInstance.v05ConsentsFetchPost(authorization, consentFetchRequest, (error, data, response) => {
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
 **consentFetchRequest** | [**ConsentFetchRequest**](ConsentFetchRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/xml


## v05ConsentsHipOnNotifyPost

> v05ConsentsHipOnNotifyPost(authorization, hIPConsentNotificationResponse)

Consent notification

This API is called by HIP as acknowledgement to notification of consents, in cases of consent revocation and expiration, notified by CM earlier via Gateway API - ***_/v0.5/consents/hip/notify***.  

### Example

```javascript
import HealthDataConsentManager from 'health_data_consent_manager';

let apiInstance = new HealthDataConsentManager.ConsentApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let hIPConsentNotificationResponse = new HealthDataConsentManager.HIPConsentNotificationResponse(); // HIPConsentNotificationResponse | 
apiInstance.v05ConsentsHipOnNotifyPost(authorization, hIPConsentNotificationResponse, (error, data, response) => {
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
 **hIPConsentNotificationResponse** | [**HIPConsentNotificationResponse**](HIPConsentNotificationResponse.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## v05ConsentsHiuOnNotifyPost

> v05ConsentsHiuOnNotifyPost(authorization, hIUConsentNotificationResponse)

Consent notification

This API is called by HIU as acknowledgement to consent notifications, specifically for cases when consent is REVOKED or EXPIRED, notified by CM earlier via Gateway API - ***_/v0.5/consents/hiu/notify***. 

### Example

```javascript
import HealthDataConsentManager from 'health_data_consent_manager';

let apiInstance = new HealthDataConsentManager.ConsentApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let hIUConsentNotificationResponse = new HealthDataConsentManager.HIUConsentNotificationResponse(); // HIUConsentNotificationResponse | 
apiInstance.v05ConsentsHiuOnNotifyPost(authorization, hIUConsentNotificationResponse, (error, data, response) => {
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
 **hIUConsentNotificationResponse** | [**HIUConsentNotificationResponse**](HIUConsentNotificationResponse.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/xml

