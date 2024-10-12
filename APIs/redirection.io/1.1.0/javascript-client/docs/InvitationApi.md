# RedirectionIo.InvitationApi

All URIs are relative to *https://api.redirection.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acceptInvitationItem**](InvitationApi.md#acceptInvitationItem) | **POST** /invitations/accept/{token} | Creates a Invitation resource.
[**deleteInvitationItem**](InvitationApi.md#deleteInvitationItem) | **DELETE** /invitations/{id} | Removes the Invitation resource.
[**getInvitationCollection**](InvitationApi.md#getInvitationCollection) | **GET** /invitations | Retrieves the collection of Invitation resources.
[**getInvitationItem**](InvitationApi.md#getInvitationItem) | **GET** /invitations/{id} | Retrieves a Invitation resource.
[**postInvitationCollection**](InvitationApi.md#postInvitationCollection) | **POST** /invitations | Creates a Invitation resource.



## acceptInvitationItem

> InvitationRead acceptInvitationItem(token, invitation)

Creates a Invitation resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.InvitationApi();
let token = "token_example"; // String | The invitation acceptation token
let invitation = new RedirectionIo.Invitation(); // Invitation | The new Invitation resource
apiInstance.acceptInvitationItem(token, invitation, (error, data, response) => {
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
 **token** | **String**| The invitation acceptation token | 
 **invitation** | [**Invitation**](Invitation.md)| The new Invitation resource | 

### Return type

[**InvitationRead**](InvitationRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/ld+json, application/json, text/html, text/csv
- **Accept**: application/ld+json, application/json, text/html, text/csv


## deleteInvitationItem

> deleteInvitationItem(id)

Removes the Invitation resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.InvitationApi();
let id = "id_example"; // String | 
apiInstance.deleteInvitationItem(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getInvitationCollection

> [InvitationRead] getInvitationCollection(targetId, targetType)

Retrieves the collection of Invitation resources.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.InvitationApi();
let targetId = "targetId_example"; // String | 
let targetType = "targetType_example"; // String | 
apiInstance.getInvitationCollection(targetId, targetType, (error, data, response) => {
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
 **targetId** | **String**|  | 
 **targetType** | **String**|  | 

### Return type

[**[InvitationRead]**](InvitationRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/ld+json, application/json, text/html, text/csv


## getInvitationItem

> InvitationRead getInvitationItem(id)

Retrieves a Invitation resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.InvitationApi();
let id = "id_example"; // String | 
apiInstance.getInvitationItem(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**InvitationRead**](InvitationRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/ld+json, application/json, text/html, text/csv


## postInvitationCollection

> InvitationRead postInvitationCollection(opts)

Creates a Invitation resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.InvitationApi();
let opts = {
  'invitation': new RedirectionIo.InvitationWrite() // InvitationWrite | The new Invitation resource
};
apiInstance.postInvitationCollection(opts, (error, data, response) => {
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
 **invitation** | [**InvitationWrite**](InvitationWrite.md)| The new Invitation resource | [optional] 

### Return type

[**InvitationRead**](InvitationRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/ld+json, application/json, text/html, text/csv
- **Accept**: application/ld+json, application/json, text/html, text/csv

