# EventsApi.ApiV1Api

All URIs are relative to *https://events.1password.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAuditEvents**](ApiV1Api.md#getAuditEvents) | **POST** /api/v1/auditevents | Retrieves audit events for actions performed by team members within a 1Password account
[**getItemUsages**](ApiV1Api.md#getItemUsages) | **POST** /api/v1/itemusages | Retrieves events for each usage of an item stored in a shared vault within a 1Password account
[**getSignInAttempts**](ApiV1Api.md#getSignInAttempts) | **POST** /api/v1/signinattempts | Retrieves events for both successful and failed attempts to sign into a 1Password account



## getAuditEvents

> AuditEventItems getAuditEvents()

Retrieves audit events for actions performed by team members within a 1Password account

This endpoint requires your JSON Web Token to have the *auditevents* feature.

### Example

```javascript
import EventsApi from 'events_api';
let defaultClient = EventsApi.ApiClient.instance;
// Configure Bearer (JWT-SA) access token for authorization: jwtsa
let jwtsa = defaultClient.authentications['jwtsa'];
jwtsa.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EventsApi.ApiV1Api();
apiInstance.getAuditEvents((error, data, response) => {
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

[**AuditEventItems**](AuditEventItems.md)

### Authorization

[jwtsa](../README.md#jwtsa)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getItemUsages

> ItemUsageItems getItemUsages()

Retrieves events for each usage of an item stored in a shared vault within a 1Password account

This endpoint requires your JSON Web Token to have the *itemusages* feature.

### Example

```javascript
import EventsApi from 'events_api';
let defaultClient = EventsApi.ApiClient.instance;
// Configure Bearer (JWT-SA) access token for authorization: jwtsa
let jwtsa = defaultClient.authentications['jwtsa'];
jwtsa.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EventsApi.ApiV1Api();
apiInstance.getItemUsages((error, data, response) => {
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

[**ItemUsageItems**](ItemUsageItems.md)

### Authorization

[jwtsa](../README.md#jwtsa)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSignInAttempts

> SignInAttemptItems getSignInAttempts()

Retrieves events for both successful and failed attempts to sign into a 1Password account

This endpoint requires your JSON Web Token to have the *signinattempts* feature.

### Example

```javascript
import EventsApi from 'events_api';
let defaultClient = EventsApi.ApiClient.instance;
// Configure Bearer (JWT-SA) access token for authorization: jwtsa
let jwtsa = defaultClient.authentications['jwtsa'];
jwtsa.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EventsApi.ApiV1Api();
apiInstance.getSignInAttempts((error, data, response) => {
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

[**SignInAttemptItems**](SignInAttemptItems.md)

### Authorization

[jwtsa](../README.md#jwtsa)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

