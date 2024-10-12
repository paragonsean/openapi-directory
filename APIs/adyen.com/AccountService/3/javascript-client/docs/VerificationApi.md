# AccountApi.VerificationApi

All URIs are relative to *https://cal-test.adyen.com/cal/services/Account/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postDeleteBankAccounts**](VerificationApi.md#postDeleteBankAccounts) | **POST** /deleteBankAccounts | Delete bank accounts
[**postDeleteLegalArrangements**](VerificationApi.md#postDeleteLegalArrangements) | **POST** /deleteLegalArrangements | Delete legal arrangements
[**postDeleteShareholders**](VerificationApi.md#postDeleteShareholders) | **POST** /deleteShareholders | Delete shareholders
[**postDeleteSignatories**](VerificationApi.md#postDeleteSignatories) | **POST** /deleteSignatories | Delete signatories
[**postGetUploadedDocuments**](VerificationApi.md#postGetUploadedDocuments) | **POST** /getUploadedDocuments | Get documents
[**postUploadDocument**](VerificationApi.md#postUploadDocument) | **POST** /uploadDocument | Upload a document



## postDeleteBankAccounts

> GenericResponse postDeleteBankAccounts(opts)

Delete bank accounts

Deletes bank accounts associated with an account holder. 

### Example

```javascript
import AccountApi from 'account_api';
let defaultClient = AccountApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AccountApi.VerificationApi();
let opts = {
  'deleteBankAccountRequest': new AccountApi.DeleteBankAccountRequest() // DeleteBankAccountRequest | 
};
apiInstance.postDeleteBankAccounts(opts, (error, data, response) => {
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
 **deleteBankAccountRequest** | [**DeleteBankAccountRequest**](DeleteBankAccountRequest.md)|  | [optional] 

### Return type

[**GenericResponse**](GenericResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postDeleteLegalArrangements

> GenericResponse postDeleteLegalArrangements(opts)

Delete legal arrangements

Deletes legal arrangements and/or legal arrangement entities associated with an account holder.

### Example

```javascript
import AccountApi from 'account_api';
let defaultClient = AccountApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AccountApi.VerificationApi();
let opts = {
  'deleteLegalArrangementRequest': new AccountApi.DeleteLegalArrangementRequest() // DeleteLegalArrangementRequest | 
};
apiInstance.postDeleteLegalArrangements(opts, (error, data, response) => {
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
 **deleteLegalArrangementRequest** | [**DeleteLegalArrangementRequest**](DeleteLegalArrangementRequest.md)|  | [optional] 

### Return type

[**GenericResponse**](GenericResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postDeleteShareholders

> GenericResponse postDeleteShareholders(opts)

Delete shareholders

Deletes shareholders associated with an account holder.

### Example

```javascript
import AccountApi from 'account_api';
let defaultClient = AccountApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AccountApi.VerificationApi();
let opts = {
  'deleteShareholderRequest': new AccountApi.DeleteShareholderRequest() // DeleteShareholderRequest | 
};
apiInstance.postDeleteShareholders(opts, (error, data, response) => {
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
 **deleteShareholderRequest** | [**DeleteShareholderRequest**](DeleteShareholderRequest.md)|  | [optional] 

### Return type

[**GenericResponse**](GenericResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postDeleteSignatories

> GenericResponse postDeleteSignatories(opts)

Delete signatories

Deletes signatories associated with an account holder.

### Example

```javascript
import AccountApi from 'account_api';
let defaultClient = AccountApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AccountApi.VerificationApi();
let opts = {
  'deleteSignatoriesRequest': new AccountApi.DeleteSignatoriesRequest() // DeleteSignatoriesRequest | 
};
apiInstance.postDeleteSignatories(opts, (error, data, response) => {
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
 **deleteSignatoriesRequest** | [**DeleteSignatoriesRequest**](DeleteSignatoriesRequest.md)|  | [optional] 

### Return type

[**GenericResponse**](GenericResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postGetUploadedDocuments

> GetUploadedDocumentsResponse postGetUploadedDocuments(opts)

Get documents

Returns documents that were previously uploaded for an account holder. Adyen uses the documents during the [verification process](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process). 

### Example

```javascript
import AccountApi from 'account_api';
let defaultClient = AccountApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AccountApi.VerificationApi();
let opts = {
  'getUploadedDocumentsRequest': new AccountApi.GetUploadedDocumentsRequest() // GetUploadedDocumentsRequest | 
};
apiInstance.postGetUploadedDocuments(opts, (error, data, response) => {
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
 **getUploadedDocumentsRequest** | [**GetUploadedDocumentsRequest**](GetUploadedDocumentsRequest.md)|  | [optional] 

### Return type

[**GetUploadedDocumentsResponse**](GetUploadedDocumentsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postUploadDocument

> UpdateAccountHolderResponse postUploadDocument(opts)

Upload a document

Uploads a document for an account holder. Adyen uses the documents during the [verification process](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process).

### Example

```javascript
import AccountApi from 'account_api';
let defaultClient = AccountApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AccountApi.VerificationApi();
let opts = {
  'uploadDocumentRequest': new AccountApi.UploadDocumentRequest() // UploadDocumentRequest | 
};
apiInstance.postUploadDocument(opts, (error, data, response) => {
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
 **uploadDocumentRequest** | [**UploadDocumentRequest**](UploadDocumentRequest.md)|  | [optional] 

### Return type

[**UpdateAccountHolderResponse**](UpdateAccountHolderResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

