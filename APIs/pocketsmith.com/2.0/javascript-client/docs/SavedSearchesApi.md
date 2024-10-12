# PocketSmith.SavedSearchesApi

All URIs are relative to *https://api.pocketsmith.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usersIdSavedSearchesGet**](SavedSearchesApi.md#usersIdSavedSearchesGet) | **GET** /users/{id}/saved_searches | List saved searches in user



## usersIdSavedSearchesGet

> [SavedSearch] usersIdSavedSearchesGet(id)

List saved searches in user

Lists saved searches belonging to a user by their ID.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.SavedSearchesApi();
let id = 42; // Number | The unique identifier of the user.
apiInstance.usersIdSavedSearchesGet(id, (error, data, response) => {
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
 **id** | **Number**| The unique identifier of the user. | 

### Return type

[**[SavedSearch]**](SavedSearch.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

