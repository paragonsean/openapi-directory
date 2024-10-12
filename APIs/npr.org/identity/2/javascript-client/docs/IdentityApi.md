# NprIdentityService.IdentityApi

All URIs are relative to *https://identity.api.npr.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteUser**](IdentityApi.md#deleteUser) | **DELETE** /v2/user | Delete the user&#39;s account
[**getUser**](IdentityApi.md#getUser) | **GET** /v2/user | Get the latest state information about the logged-in user
[**inheritFromTempUser**](IdentityApi.md#inheritFromTempUser) | **POST** /v2/user/inherit | Copy listening data from a temporary user account to the logged-in user&#39;s account
[**postFollowing**](IdentityApi.md#postFollowing) | **POST** /v2/following | Update the following status of the logged-in user for a particular aggregation
[**updateStations**](IdentityApi.md#updateStations) | **PUT** /v2/stations | Update the logged-in user&#39;s favorite station(s)



## deleteUser

> UserDocument deleteUser(authorization)

Delete the user&#39;s account

Use with caution as some steps are irreverisble. Initiates the user account deletion process, including removal of all user PII and account access.

### Example

```javascript
import NprIdentityService from 'npr_identity_service';
let defaultClient = NprIdentityService.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NprIdentityService.IdentityApi();
let authorization = "authorization_example"; // String | Your access token from the Authorization Service. Should start with `Bearer`, followed by a space, followed by the token.
apiInstance.deleteUser(authorization, (error, data, response) => {
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
 **authorization** | **String**| Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token. | 

### Return type

[**UserDocument**](UserDocument.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/vnd.collection.doc+json


## getUser

> UserDocument getUser(authorization)

Get the latest state information about the logged-in user

After a successful login, the client should send a &#x60;GET&#x60; call approximately once an hour to refresh the user data.

### Example

```javascript
import NprIdentityService from 'npr_identity_service';
let defaultClient = NprIdentityService.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NprIdentityService.IdentityApi();
let authorization = "authorization_example"; // String | Your access token from the Authorization Service. Should start with `Bearer`, followed by a space, followed by the token.
apiInstance.getUser(authorization, (error, data, response) => {
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
 **authorization** | **String**| Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token. | 

### Return type

[**UserDocument**](UserDocument.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/vnd.collection.doc+json


## inheritFromTempUser

> UserDocument inheritFromTempUser(authorization, tempUser)

Copy listening data from a temporary user account to the logged-in user&#39;s account

This can and should only be used by clients who have access to the &#x60;temporary_user&#x60; grant type.     Third-party developers do not have access to this grant type by default, and will not need this endpoint.

### Example

```javascript
import NprIdentityService from 'npr_identity_service';
let defaultClient = NprIdentityService.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NprIdentityService.IdentityApi();
let authorization = "authorization_example"; // String | Your access token from the Authorization Service. Should start with `Bearer`, followed by a space, followed by the token.
let tempUser = 56; // Number | The temporary user's ID before the user registered or logged in
apiInstance.inheritFromTempUser(authorization, tempUser, (error, data, response) => {
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
 **authorization** | **String**| Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token. | 
 **tempUser** | **Number**| The temporary user&#39;s ID before the user registered or logged in | 

### Return type

[**UserDocument**](UserDocument.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/vnd.collection.doc+json


## postFollowing

> UserDocument postFollowing(authorization, body)

Update the following status of the logged-in user for a particular aggregation

After a successful call, this returns a User document with an updated list of affiliations.

### Example

```javascript
import NprIdentityService from 'npr_identity_service';
let defaultClient = NprIdentityService.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NprIdentityService.IdentityApi();
let authorization = "authorization_example"; // String | Your access token from the Authorization Service. Should start with `Bearer`, followed by a space, followed by the token.
let body = new NprIdentityService.Affiliation(); // Affiliation | A JSON-serialized object which contains data about a user affiliation such as the aggregation ID, affiliation rating, aggregation URL, days since last listen, and following status.
apiInstance.postFollowing(authorization, body, (error, data, response) => {
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
 **authorization** | **String**| Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token. | 
 **body** | [**Affiliation**](Affiliation.md)| A JSON-serialized object which contains data about a user affiliation such as the aggregation ID, affiliation rating, aggregation URL, days since last listen, and following status. | 

### Return type

[**UserDocument**](UserDocument.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/vnd.collection.doc+json


## updateStations

> UserDocument updateStations(authorization, opts)

Update the logged-in user&#39;s favorite station(s)

Right now, only the primary station can be changed. Previously selected stations will not be deleted, but the new station will be moved to first in the array.

### Example

```javascript
import NprIdentityService from 'npr_identity_service';
let defaultClient = NprIdentityService.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NprIdentityService.IdentityApi();
let authorization = "authorization_example"; // String | Your access token from the Authorization Service. Should start with `Bearer`, followed by a space, followed by the token.
let opts = {
  'body': [null] // [Number] | A JSON-serialized array of station IDs
};
apiInstance.updateStations(authorization, opts, (error, data, response) => {
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
 **authorization** | **String**| Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token. | 
 **body** | [**[Number]**](Number.md)| A JSON-serialized array of station IDs | [optional] 

### Return type

[**UserDocument**](UserDocument.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json, application/vnd.collection.doc+json
- **Accept**: application/json, application/vnd.collection.doc+json

