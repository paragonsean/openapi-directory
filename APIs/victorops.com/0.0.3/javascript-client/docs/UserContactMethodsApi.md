# VictorOps.UserContactMethodsApi

All URIs are relative to *https://api.victorops.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiPublicV1UserUserContactMethodsDevicesContactIdDelete**](UserContactMethodsApi.md#apiPublicV1UserUserContactMethodsDevicesContactIdDelete) | **DELETE** /api-public/v1/user/{user}/contact-methods/devices/{contactId} | Delete a contact device for a user
[**apiPublicV1UserUserContactMethodsDevicesContactIdGet**](UserContactMethodsApi.md#apiPublicV1UserUserContactMethodsDevicesContactIdGet) | **GET** /api-public/v1/user/{user}/contact-methods/devices/{contactId} | Get the indicated contact device for a user
[**apiPublicV1UserUserContactMethodsDevicesContactIdPut**](UserContactMethodsApi.md#apiPublicV1UserUserContactMethodsDevicesContactIdPut) | **PUT** /api-public/v1/user/{user}/contact-methods/devices/{contactId} | Update a contact device for a user
[**apiPublicV1UserUserContactMethodsDevicesGet**](UserContactMethodsApi.md#apiPublicV1UserUserContactMethodsDevicesGet) | **GET** /api-public/v1/user/{user}/contact-methods/devices | Get a list of all contact devices for a user
[**apiPublicV1UserUserContactMethodsEmailsContactIdDelete**](UserContactMethodsApi.md#apiPublicV1UserUserContactMethodsEmailsContactIdDelete) | **DELETE** /api-public/v1/user/{user}/contact-methods/emails/{contactId} | Delete a contact email for a user
[**apiPublicV1UserUserContactMethodsEmailsContactIdGet**](UserContactMethodsApi.md#apiPublicV1UserUserContactMethodsEmailsContactIdGet) | **GET** /api-public/v1/user/{user}/contact-methods/emails/{contactId} | Get the indicated contact email for a user
[**apiPublicV1UserUserContactMethodsEmailsGet**](UserContactMethodsApi.md#apiPublicV1UserUserContactMethodsEmailsGet) | **GET** /api-public/v1/user/{user}/contact-methods/emails | Get a list of all contact emails for a user
[**apiPublicV1UserUserContactMethodsEmailsPost**](UserContactMethodsApi.md#apiPublicV1UserUserContactMethodsEmailsPost) | **POST** /api-public/v1/user/{user}/contact-methods/emails | Create a contact emails for a user
[**apiPublicV1UserUserContactMethodsGet**](UserContactMethodsApi.md#apiPublicV1UserUserContactMethodsGet) | **GET** /api-public/v1/user/{user}/contact-methods | Get a list of all contact methods for a user
[**apiPublicV1UserUserContactMethodsPhonesContactIdDelete**](UserContactMethodsApi.md#apiPublicV1UserUserContactMethodsPhonesContactIdDelete) | **DELETE** /api-public/v1/user/{user}/contact-methods/phones/{contactId} | Delete a contact phone for a user
[**apiPublicV1UserUserContactMethodsPhonesContactIdGet**](UserContactMethodsApi.md#apiPublicV1UserUserContactMethodsPhonesContactIdGet) | **GET** /api-public/v1/user/{user}/contact-methods/phones/{contactId} | Get the indicated contact phone for a user
[**apiPublicV1UserUserContactMethodsPhonesGet**](UserContactMethodsApi.md#apiPublicV1UserUserContactMethodsPhonesGet) | **GET** /api-public/v1/user/{user}/contact-methods/phones | Get a list of all contact phones for a user
[**apiPublicV1UserUserContactMethodsPhonesPost**](UserContactMethodsApi.md#apiPublicV1UserUserContactMethodsPhonesPost) | **POST** /api-public/v1/user/{user}/contact-methods/phones | Create a contact phones for a user



## apiPublicV1UserUserContactMethodsDevicesContactIdDelete

> ContactDevice apiPublicV1UserUserContactMethodsDevicesContactIdDelete(xVOApiId, xVOApiKey, user, contactId)

Delete a contact device for a user

Delete a contact device for a user  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.UserContactMethodsApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let user = "user_example"; // String | The VictorOps user ID
let contactId = "contactId_example"; // String | The unique contact identifier
apiInstance.apiPublicV1UserUserContactMethodsDevicesContactIdDelete(xVOApiId, xVOApiKey, user, contactId, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **user** | **String**| The VictorOps user ID | 
 **contactId** | **String**| The unique contact identifier | 

### Return type

[**ContactDevice**](ContactDevice.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1UserUserContactMethodsDevicesContactIdGet

> [ContactDevice] apiPublicV1UserUserContactMethodsDevicesContactIdGet(xVOApiId, xVOApiKey, user, contactId)

Get the indicated contact device for a user

Get the indicated contact device for a user  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.UserContactMethodsApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let user = "user_example"; // String | The VictorOps user ID
let contactId = "contactId_example"; // String | The unique contact identifier
apiInstance.apiPublicV1UserUserContactMethodsDevicesContactIdGet(xVOApiId, xVOApiKey, user, contactId, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **user** | **String**| The VictorOps user ID | 
 **contactId** | **String**| The unique contact identifier | 

### Return type

[**[ContactDevice]**](ContactDevice.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1UserUserContactMethodsDevicesContactIdPut

> ContactDevice apiPublicV1UserUserContactMethodsDevicesContactIdPut(xVOApiId, xVOApiKey, user, contactId, body)

Update a contact device for a user

Update a contact device for a user  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.UserContactMethodsApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let user = "user_example"; // String | The VictorOps user ID
let contactId = "contactId_example"; // String | The unique contact identifier
let body = new VictorOps.ContactDeviceAdd(); // ContactDeviceAdd | The contact device
apiInstance.apiPublicV1UserUserContactMethodsDevicesContactIdPut(xVOApiId, xVOApiKey, user, contactId, body, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **user** | **String**| The VictorOps user ID | 
 **contactId** | **String**| The unique contact identifier | 
 **body** | [**ContactDeviceAdd**](ContactDeviceAdd.md)| The contact device | 

### Return type

[**ContactDevice**](ContactDevice.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1UserUserContactMethodsDevicesGet

> [ContactDevice] apiPublicV1UserUserContactMethodsDevicesGet(xVOApiId, xVOApiKey, user)

Get a list of all contact devices for a user

Get the contact methods for a user  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.UserContactMethodsApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let user = "user_example"; // String | The VictorOps user ID
apiInstance.apiPublicV1UserUserContactMethodsDevicesGet(xVOApiId, xVOApiKey, user, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **user** | **String**| The VictorOps user ID | 

### Return type

[**[ContactDevice]**](ContactDevice.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1UserUserContactMethodsEmailsContactIdDelete

> UserContact apiPublicV1UserUserContactMethodsEmailsContactIdDelete(xVOApiId, xVOApiKey, user, contactId)

Delete a contact email for a user

Delete the indicated contact email for the user  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.UserContactMethodsApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let user = "user_example"; // String | The VictorOps user ID
let contactId = "contactId_example"; // String | The unique contact identifier
apiInstance.apiPublicV1UserUserContactMethodsEmailsContactIdDelete(xVOApiId, xVOApiKey, user, contactId, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **user** | **String**| The VictorOps user ID | 
 **contactId** | **String**| The unique contact identifier | 

### Return type

[**UserContact**](UserContact.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1UserUserContactMethodsEmailsContactIdGet

> [UserContact] apiPublicV1UserUserContactMethodsEmailsContactIdGet(xVOApiId, xVOApiKey, user, contactId)

Get the indicated contact email for a user

Get the indicated contact email for a user  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.UserContactMethodsApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let user = "user_example"; // String | The VictorOps user ID
let contactId = "contactId_example"; // String | The unique contact identifier
apiInstance.apiPublicV1UserUserContactMethodsEmailsContactIdGet(xVOApiId, xVOApiKey, user, contactId, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **user** | **String**| The VictorOps user ID | 
 **contactId** | **String**| The unique contact identifier | 

### Return type

[**[UserContact]**](UserContact.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1UserUserContactMethodsEmailsGet

> [UserContact] apiPublicV1UserUserContactMethodsEmailsGet(xVOApiId, xVOApiKey, user)

Get a list of all contact emails for a user

Get the contact emails for a user  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.UserContactMethodsApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let user = "user_example"; // String | The VictorOps user ID
apiInstance.apiPublicV1UserUserContactMethodsEmailsGet(xVOApiId, xVOApiKey, user, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **user** | **String**| The VictorOps user ID | 

### Return type

[**[UserContact]**](UserContact.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1UserUserContactMethodsEmailsPost

> UserContact apiPublicV1UserUserContactMethodsEmailsPost(xVOApiId, xVOApiKey, user, body)

Create a contact emails for a user

Create a contact email for a user  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.UserContactMethodsApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let user = "user_example"; // String | The VictorOps user ID
let body = new VictorOps.ContactEmailAdd(); // ContactEmailAdd | The contact email
apiInstance.apiPublicV1UserUserContactMethodsEmailsPost(xVOApiId, xVOApiKey, user, body, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **user** | **String**| The VictorOps user ID | 
 **body** | [**ContactEmailAdd**](ContactEmailAdd.md)| The contact email | 

### Return type

[**UserContact**](UserContact.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1UserUserContactMethodsGet

> ApiPublicV1UserUserContactMethodsGet200Response apiPublicV1UserUserContactMethodsGet(xVOApiId, xVOApiKey, user)

Get a list of all contact methods for a user

Get the contact methods for a user  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.UserContactMethodsApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let user = "user_example"; // String | The VictorOps user ID
apiInstance.apiPublicV1UserUserContactMethodsGet(xVOApiId, xVOApiKey, user, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **user** | **String**| The VictorOps user ID | 

### Return type

[**ApiPublicV1UserUserContactMethodsGet200Response**](ApiPublicV1UserUserContactMethodsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1UserUserContactMethodsPhonesContactIdDelete

> UserContact apiPublicV1UserUserContactMethodsPhonesContactIdDelete(xVOApiId, xVOApiKey, user, contactId)

Delete a contact phone for a user

Delete the indicated contact phone for the user  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.UserContactMethodsApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let user = "user_example"; // String | The VictorOps user ID
let contactId = "contactId_example"; // String | The unique contact identifier
apiInstance.apiPublicV1UserUserContactMethodsPhonesContactIdDelete(xVOApiId, xVOApiKey, user, contactId, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **user** | **String**| The VictorOps user ID | 
 **contactId** | **String**| The unique contact identifier | 

### Return type

[**UserContact**](UserContact.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1UserUserContactMethodsPhonesContactIdGet

> [UserContact] apiPublicV1UserUserContactMethodsPhonesContactIdGet(xVOApiId, xVOApiKey, user, contactId)

Get the indicated contact phone for a user

Get the indicated contact phone for a user  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.UserContactMethodsApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let user = "user_example"; // String | The VictorOps user ID
let contactId = "contactId_example"; // String | The unique contact identifier
apiInstance.apiPublicV1UserUserContactMethodsPhonesContactIdGet(xVOApiId, xVOApiKey, user, contactId, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **user** | **String**| The VictorOps user ID | 
 **contactId** | **String**| The unique contact identifier | 

### Return type

[**[UserContact]**](UserContact.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1UserUserContactMethodsPhonesGet

> [UserContact] apiPublicV1UserUserContactMethodsPhonesGet(xVOApiId, xVOApiKey, user)

Get a list of all contact phones for a user

Get the contact phones for a user  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.UserContactMethodsApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let user = "user_example"; // String | The VictorOps user ID
apiInstance.apiPublicV1UserUserContactMethodsPhonesGet(xVOApiId, xVOApiKey, user, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **user** | **String**| The VictorOps user ID | 

### Return type

[**[UserContact]**](UserContact.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1UserUserContactMethodsPhonesPost

> UserContact apiPublicV1UserUserContactMethodsPhonesPost(xVOApiId, xVOApiKey, user, body)

Create a contact phones for a user

Create a contact phone for a user  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.UserContactMethodsApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let user = "user_example"; // String | The VictorOps user ID
let body = new VictorOps.ContactPhoneAdd(); // ContactPhoneAdd | The contact phone
apiInstance.apiPublicV1UserUserContactMethodsPhonesPost(xVOApiId, xVOApiKey, user, body, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **user** | **String**| The VictorOps user ID | 
 **body** | [**ContactPhoneAdd**](ContactPhoneAdd.md)| The contact phone | 

### Return type

[**UserContact**](UserContact.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

