# PeerTube.RegisterApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acceptRegistration**](RegisterApi.md#acceptRegistration) | **POST** /api/v1/users/registrations/{registrationId}/accept | Accept registration
[**deleteRegistration**](RegisterApi.md#deleteRegistration) | **DELETE** /api/v1/users/registrations/{registrationId} | Delete registration
[**listRegistrations**](RegisterApi.md#listRegistrations) | **GET** /api/v1/users/registrations | List registrations
[**registerUser**](RegisterApi.md#registerUser) | **POST** /api/v1/users/register | Register a user
[**rejectRegistration**](RegisterApi.md#rejectRegistration) | **POST** /api/v1/users/registrations/{registrationId}/reject | Reject registration
[**requestRegistration**](RegisterApi.md#requestRegistration) | **POST** /api/v1/users/registrations/request | Request registration
[**resendEmailToVerifyRegistration**](RegisterApi.md#resendEmailToVerifyRegistration) | **POST** /api/v1/users/registrations/ask-send-verify-email | Resend verification link to registration email
[**resendEmailToVerifyUser_0**](RegisterApi.md#resendEmailToVerifyUser_0) | **POST** /api/v1/users/ask-send-verify-email | Resend user verification link
[**verifyRegistrationEmail**](RegisterApi.md#verifyRegistrationEmail) | **POST** /api/v1/users/registrations/{registrationId}/verify-email | Verify a registration email
[**verifyUser_0**](RegisterApi.md#verifyUser_0) | **POST** /api/v1/users/{id}/verify-email | Verify a user



## acceptRegistration

> acceptRegistration(registrationId, opts)

Accept registration

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.RegisterApi();
let registrationId = 56; // Number | Registration ID
let opts = {
  'userRegistrationAcceptOrReject': new PeerTube.UserRegistrationAcceptOrReject() // UserRegistrationAcceptOrReject | 
};
apiInstance.acceptRegistration(registrationId, opts, (error, data, response) => {
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
 **registrationId** | **Number**| Registration ID | 
 **userRegistrationAcceptOrReject** | [**UserRegistrationAcceptOrReject**](UserRegistrationAcceptOrReject.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## deleteRegistration

> deleteRegistration(registrationId)

Delete registration

Delete the registration entry. It will not remove the user associated with this registration (if any)

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.RegisterApi();
let registrationId = 56; // Number | Registration ID
apiInstance.deleteRegistration(registrationId, (error, data, response) => {
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
 **registrationId** | **Number**| Registration ID | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listRegistrations

> ListRegistrations200Response listRegistrations(opts)

List registrations

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.RegisterApi();
let opts = {
  'start': 56, // Number | Offset used to paginate results
  'count': 15, // Number | Number of items to return
  'search': "search_example", // String | 
  'sort': "sort_example" // String | 
};
apiInstance.listRegistrations(opts, (error, data, response) => {
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
 **start** | **Number**| Offset used to paginate results | [optional] 
 **count** | **Number**| Number of items to return | [optional] [default to 15]
 **search** | **String**|  | [optional] 
 **sort** | **String**|  | [optional] 

### Return type

[**ListRegistrations200Response**](ListRegistrations200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## registerUser

> registerUser(registerUser)

Register a user

Signup has to be enabled and signup approval is not required

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.RegisterApi();
let registerUser = new PeerTube.RegisterUser(); // RegisterUser | 
apiInstance.registerUser(registerUser, (error, data, response) => {
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
 **registerUser** | [**RegisterUser**](RegisterUser.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## rejectRegistration

> rejectRegistration(registrationId, opts)

Reject registration

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.RegisterApi();
let registrationId = 56; // Number | Registration ID
let opts = {
  'userRegistrationAcceptOrReject': new PeerTube.UserRegistrationAcceptOrReject() // UserRegistrationAcceptOrReject | 
};
apiInstance.rejectRegistration(registrationId, opts, (error, data, response) => {
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
 **registrationId** | **Number**| Registration ID | 
 **userRegistrationAcceptOrReject** | [**UserRegistrationAcceptOrReject**](UserRegistrationAcceptOrReject.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## requestRegistration

> UserRegistration requestRegistration(opts)

Request registration

Signup has to be enabled and require approval on the instance

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.RegisterApi();
let opts = {
  'userRegistrationRequest': new PeerTube.UserRegistrationRequest() // UserRegistrationRequest | 
};
apiInstance.requestRegistration(opts, (error, data, response) => {
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
 **userRegistrationRequest** | [**UserRegistrationRequest**](UserRegistrationRequest.md)|  | [optional] 

### Return type

[**UserRegistration**](UserRegistration.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## resendEmailToVerifyRegistration

> resendEmailToVerifyRegistration(opts)

Resend verification link to registration email

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.RegisterApi();
let opts = {
  'resendEmailToVerifyRegistrationRequest': new PeerTube.ResendEmailToVerifyRegistrationRequest() // ResendEmailToVerifyRegistrationRequest | 
};
apiInstance.resendEmailToVerifyRegistration(opts, (error, data, response) => {
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
 **resendEmailToVerifyRegistrationRequest** | [**ResendEmailToVerifyRegistrationRequest**](ResendEmailToVerifyRegistrationRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## resendEmailToVerifyUser_0

> resendEmailToVerifyUser_0(opts)

Resend user verification link

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.RegisterApi();
let opts = {
  'resendEmailToVerifyUserRequest': new PeerTube.ResendEmailToVerifyUserRequest() // ResendEmailToVerifyUserRequest | 
};
apiInstance.resendEmailToVerifyUser_0(opts, (error, data, response) => {
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
 **resendEmailToVerifyUserRequest** | [**ResendEmailToVerifyUserRequest**](ResendEmailToVerifyUserRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## verifyRegistrationEmail

> verifyRegistrationEmail(registrationId, opts)

Verify a registration email

Following a user registration request, the user will receive an email asking to click a link containing a secret. 

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.RegisterApi();
let registrationId = 56; // Number | Registration ID
let opts = {
  'verifyRegistrationEmailRequest': new PeerTube.VerifyRegistrationEmailRequest() // VerifyRegistrationEmailRequest | 
};
apiInstance.verifyRegistrationEmail(registrationId, opts, (error, data, response) => {
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
 **registrationId** | **Number**| Registration ID | 
 **verifyRegistrationEmailRequest** | [**VerifyRegistrationEmailRequest**](VerifyRegistrationEmailRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## verifyUser_0

> verifyUser_0(id, opts)

Verify a user

Following a user registration, the new user will receive an email asking to click a link containing a secret. This endpoint can also be used to verify a new email set in the user account. 

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.RegisterApi();
let id = 56; // Number | Entity id
let opts = {
  'verifyUserRequest': new PeerTube.VerifyUserRequest() // VerifyUserRequest | 
};
apiInstance.verifyUser_0(id, opts, (error, data, response) => {
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
 **id** | **Number**| Entity id | 
 **verifyUserRequest** | [**VerifyUserRequest**](VerifyUserRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

