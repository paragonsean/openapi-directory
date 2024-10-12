# PocketSmith.AttachmentsApi

All URIs are relative to *https://api.pocketsmith.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attachmentsIdDelete**](AttachmentsApi.md#attachmentsIdDelete) | **DELETE** /attachments/{id} | Delete attachment
[**attachmentsIdGet**](AttachmentsApi.md#attachmentsIdGet) | **GET** /attachments/{id} | Get attachment
[**attachmentsIdPut**](AttachmentsApi.md#attachmentsIdPut) | **PUT** /attachments/{id} | Update attachment
[**transactionsIdAttachmentsGet**](AttachmentsApi.md#transactionsIdAttachmentsGet) | **GET** /transactions/{id}/attachments | List attachments in transaction
[**transactionsIdAttachmentsPost**](AttachmentsApi.md#transactionsIdAttachmentsPost) | **POST** /transactions/{id}/attachments | Assigns attachment to transaction
[**transactionsTransactionIdAttachmentsAttachmentIdDelete**](AttachmentsApi.md#transactionsTransactionIdAttachmentsAttachmentIdDelete) | **DELETE** /transactions/{transaction_id}/attachments/{attachment_id} | Unassigns attachment in transaction
[**usersIdAttachmentsGet**](AttachmentsApi.md#usersIdAttachmentsGet) | **GET** /users/{id}/attachments | Lists attachments in user
[**usersIdAttachmentsPost**](AttachmentsApi.md#usersIdAttachmentsPost) | **POST** /users/{id}/attachments | Create attachment in user



## attachmentsIdDelete

> attachmentsIdDelete(id)

Delete attachment

Deletes a particular attachment by its ID.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.AttachmentsApi();
let id = 42; // Number | The unique identifier of the attachment.
apiInstance.attachmentsIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| The unique identifier of the attachment. | 

### Return type

null (empty response body)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## attachmentsIdGet

> Attachment attachmentsIdGet(id)

Get attachment

Gets a particular attachment by its ID.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.AttachmentsApi();
let id = 42; // Number | The unique identifier of the attachment.
apiInstance.attachmentsIdGet(id, (error, data, response) => {
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
 **id** | **Number**| The unique identifier of the attachment. | 

### Return type

[**Attachment**](Attachment.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## attachmentsIdPut

> Attachment attachmentsIdPut(id, opts)

Update attachment

Updates the title of the attachment.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.AttachmentsApi();
let id = 42; // Number | The unique identifier of the attachment.
let opts = {
  'attachmentsIdPutRequest': new PocketSmith.AttachmentsIdPutRequest() // AttachmentsIdPutRequest | 
};
apiInstance.attachmentsIdPut(id, opts, (error, data, response) => {
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
 **id** | **Number**| The unique identifier of the attachment. | 
 **attachmentsIdPutRequest** | [**AttachmentsIdPutRequest**](AttachmentsIdPutRequest.md)|  | [optional] 

### Return type

[**Attachment**](Attachment.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transactionsIdAttachmentsGet

> [Attachment] transactionsIdAttachmentsGet(id)

List attachments in transaction

Lists attachments belonging to a transaction by their ID.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.AttachmentsApi();
let id = 42; // Number | The unique identifier of the transaction.
apiInstance.transactionsIdAttachmentsGet(id, (error, data, response) => {
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
 **id** | **Number**| The unique identifier of the transaction. | 

### Return type

[**[Attachment]**](Attachment.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## transactionsIdAttachmentsPost

> Attachment transactionsIdAttachmentsPost(id, opts)

Assigns attachment to transaction

Assigns an attachment to the transaction by their ID.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.AttachmentsApi();
let id = 42; // Number | The unique identifier of the transaction.
let opts = {
  'transactionsIdAttachmentsPostRequest': new PocketSmith.TransactionsIdAttachmentsPostRequest() // TransactionsIdAttachmentsPostRequest | 
};
apiInstance.transactionsIdAttachmentsPost(id, opts, (error, data, response) => {
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
 **id** | **Number**| The unique identifier of the transaction. | 
 **transactionsIdAttachmentsPostRequest** | [**TransactionsIdAttachmentsPostRequest**](TransactionsIdAttachmentsPostRequest.md)|  | [optional] 

### Return type

[**Attachment**](Attachment.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transactionsTransactionIdAttachmentsAttachmentIdDelete

> transactionsTransactionIdAttachmentsAttachmentIdDelete(transactionId, attachmentId)

Unassigns attachment in transaction

Unassigns a particular attachment by its ID from the transaction ID. This does not delete the attachment, it only removes its association from the transaction.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.AttachmentsApi();
let transactionId = 42; // Number | The unique identifier of the transaction.
let attachmentId = 1438154; // Number | The unique identifier of the attachment.
apiInstance.transactionsTransactionIdAttachmentsAttachmentIdDelete(transactionId, attachmentId, (error, data, response) => {
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
 **transactionId** | **Number**| The unique identifier of the transaction. | 
 **attachmentId** | **Number**| The unique identifier of the attachment. | 

### Return type

null (empty response body)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersIdAttachmentsGet

> [Attachment] usersIdAttachmentsGet(id, opts)

Lists attachments in user

Lists attachments belonging to a user by their ID.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.AttachmentsApi();
let id = 42; // Number | The unique identifier of the user.
let opts = {
  'unassigned': 1 // Number | If set, returns unassigned attachments, that are available for assigning to a transaction.
};
apiInstance.usersIdAttachmentsGet(id, opts, (error, data, response) => {
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
 **unassigned** | **Number**| If set, returns unassigned attachments, that are available for assigning to a transaction. | [optional] 

### Return type

[**[Attachment]**](Attachment.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersIdAttachmentsPost

> Attachment usersIdAttachmentsPost(id, opts)

Create attachment in user

Creates an attachment belonging to the user by their ID.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.AttachmentsApi();
let id = 42; // Number | The unique identifier of the user.
let opts = {
  'usersIdAttachmentsPostRequest': new PocketSmith.UsersIdAttachmentsPostRequest() // UsersIdAttachmentsPostRequest | 
};
apiInstance.usersIdAttachmentsPost(id, opts, (error, data, response) => {
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
 **usersIdAttachmentsPostRequest** | [**UsersIdAttachmentsPostRequest**](UsersIdAttachmentsPostRequest.md)|  | [optional] 

### Return type

[**Attachment**](Attachment.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

