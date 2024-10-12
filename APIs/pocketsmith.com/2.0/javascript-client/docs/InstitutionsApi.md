# PocketSmith.InstitutionsApi

All URIs are relative to *https://api.pocketsmith.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**institutionsIdDelete**](InstitutionsApi.md#institutionsIdDelete) | **DELETE** /institutions/{id} | Delete institution
[**institutionsIdGet**](InstitutionsApi.md#institutionsIdGet) | **GET** /institutions/{id} | Get institution
[**institutionsIdPut**](InstitutionsApi.md#institutionsIdPut) | **PUT** /institutions/{id} | Update institution
[**usersIdInstitutionsGet**](InstitutionsApi.md#usersIdInstitutionsGet) | **GET** /users/{id}/institutions | List institutions in user
[**usersIdInstitutionsPost**](InstitutionsApi.md#usersIdInstitutionsPost) | **POST** /users/{id}/institutions | Create institution in user



## institutionsIdDelete

> institutionsIdDelete(id, opts)

Delete institution

Deletes an institution and all data within. Alternatively, another institution can be provided to merge the data into to avoid losing it.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.InstitutionsApi();
let id = 42; // Number | The unique identifier of the institution.
let opts = {
  'mergeIntoInstitutionId': 44 // Number | The unique identifier of the institution to merge into.
};
apiInstance.institutionsIdDelete(id, opts, (error, data, response) => {
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
 **id** | **Number**| The unique identifier of the institution. | 
 **mergeIntoInstitutionId** | **Number**| The unique identifier of the institution to merge into. | [optional] 

### Return type

null (empty response body)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## institutionsIdGet

> Institution institutionsIdGet(id)

Get institution

Gets an institution by its ID.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.InstitutionsApi();
let id = 42; // Number | The unique identifier of the institution.
apiInstance.institutionsIdGet(id, (error, data, response) => {
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
 **id** | **Number**| The unique identifier of the institution. | 

### Return type

[**Institution**](Institution.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## institutionsIdPut

> Institution institutionsIdPut(id, opts)

Update institution

Updates the title and currency code for an institution.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.InstitutionsApi();
let id = 42; // Number | The unique identifier of the institution.
let opts = {
  'institutionsIdPutRequest': new PocketSmith.InstitutionsIdPutRequest() // InstitutionsIdPutRequest | 
};
apiInstance.institutionsIdPut(id, opts, (error, data, response) => {
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
 **id** | **Number**| The unique identifier of the institution. | 
 **institutionsIdPutRequest** | [**InstitutionsIdPutRequest**](InstitutionsIdPutRequest.md)|  | [optional] 

### Return type

[**Institution**](Institution.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersIdInstitutionsGet

> [Institution] usersIdInstitutionsGet(id)

List institutions in user

Lists all the institutions belonging to the user.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.InstitutionsApi();
let id = 42; // Number | The unique identifier of the user
apiInstance.usersIdInstitutionsGet(id, (error, data, response) => {
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
 **id** | **Number**| The unique identifier of the user | 

### Return type

[**[Institution]**](Institution.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersIdInstitutionsPost

> Institution usersIdInstitutionsPost(id, opts)

Create institution in user

Creates an institution belonging to a user.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.InstitutionsApi();
let id = 42; // Number | The unique identifier of the user
let opts = {
  'usersIdInstitutionsPostRequest': new PocketSmith.UsersIdInstitutionsPostRequest() // UsersIdInstitutionsPostRequest | 
};
apiInstance.usersIdInstitutionsPost(id, opts, (error, data, response) => {
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
 **id** | **Number**| The unique identifier of the user | 
 **usersIdInstitutionsPostRequest** | [**UsersIdInstitutionsPostRequest**](UsersIdInstitutionsPostRequest.md)|  | [optional] 

### Return type

[**Institution**](Institution.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

