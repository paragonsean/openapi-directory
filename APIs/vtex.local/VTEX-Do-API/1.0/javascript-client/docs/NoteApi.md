# VtexDoApi.NoteApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNote**](NoteApi.md#getNote) | **GET** /notes/{noteId} | Retrieve Note
[**getNotesbyorderId**](NoteApi.md#getNotesbyorderId) | **GET** /notes | Get Notes by orderId
[**newNote**](NoteApi.md#newNote) | **POST** /notes | Create Note



## getNote

> Object getNote(accept, contentType, noteId, opts)

Retrieve Note

Retrieves a given note in VTEX DO, filtering by &#x60;noteId&#x60;.

### Example

```javascript
import VtexDoApi from 'vtex_do_api';
let defaultClient = VtexDoApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new VtexDoApi.NoteApi();
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "application/json"; // String | Type of the content being sent.
let noteId = "654321cba"; // String | Note's ID.
let opts = {
  'reason': "data-validation" // String | This parameter is relevant only for PII-compliant accounts. When sending requests to this endpoint, PII-compliant accounts can use this parameter to declare the reason for requesting unmasked data. Otherwise, this endpoint will return masked PII data.
};
apiInstance.getNote(accept, contentType, noteId, opts, (error, data, response) => {
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
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | 
 **contentType** | **String**| Type of the content being sent. | 
 **noteId** | **String**| Note&#39;s ID. | 
 **reason** | **String**| This parameter is relevant only for PII-compliant accounts. When sending requests to this endpoint, PII-compliant accounts can use this parameter to declare the reason for requesting unmasked data. Otherwise, this endpoint will return masked PII data. | [optional] 

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNotesbyorderId

> Object getNotesbyorderId(targetId, accept, contentType, opts)

Get Notes by orderId

Retrieves notes related to a specific &#x60;orderId&#x60;.

### Example

```javascript
import VtexDoApi from 'vtex_do_api';
let defaultClient = VtexDoApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new VtexDoApi.NoteApi();
let targetId = "1172452900788-01"; // String | ID of the order.
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "application/json"; // String | Type of the content being sent.
let opts = {
  'perPage': 20, // Number | Number of notes per page. Maximum: 30.
  'page': 3, // Number | Number of the page to be retrieved.
  'reason': "data-validation" // String | This parameter is relevant only for PII-compliant accounts. When sending requests to this endpoint, PII-compliant accounts can use this parameter to declare the reason for requesting unmasked data. Otherwise, this endpoint will return masked PII data.
};
apiInstance.getNotesbyorderId(targetId, accept, contentType, opts, (error, data, response) => {
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
 **targetId** | **String**| ID of the order. | 
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | 
 **contentType** | **String**| Type of the content being sent. | 
 **perPage** | **Number**| Number of notes per page. Maximum: 30. | [optional] 
 **page** | **Number**| Number of the page to be retrieved. | [optional] 
 **reason** | **String**| This parameter is relevant only for PII-compliant accounts. When sending requests to this endpoint, PII-compliant accounts can use this parameter to declare the reason for requesting unmasked data. Otherwise, this endpoint will return masked PII data. | [optional] 

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## newNote

> Object newNote(accept, contentType, opts)

Create Note

This endpoint creates a new note in VTEX DO. Be aware of the following limitations:    - The maximum number of notes for an order is 30.    - The maximum number of characters in a note&#39;s description is 2000.

### Example

```javascript
import VtexDoApi from 'vtex_do_api';
let defaultClient = VtexDoApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new VtexDoApi.NoteApi();
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "application/json"; // String | Type of the content being sent.
let opts = {
  'newNoteRequest': new VtexDoApi.NewNoteRequest() // NewNoteRequest | 
};
apiInstance.newNote(accept, contentType, opts, (error, data, response) => {
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
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | 
 **contentType** | **String**| Type of the content being sent. | 
 **newNoteRequest** | [**NewNoteRequest**](NewNoteRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

