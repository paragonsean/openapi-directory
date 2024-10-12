# XtrfHomePortalApi.QuotesSmartV2Api

All URIs are relative to *https://presentation.s.xtrf.eu/home-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addFiles2**](QuotesSmartV2Api.md#addFiles2) | **PUT** /v2/quotes/{quoteId}/files/add | Adds files to the quote as added by PM.
[**archive1**](QuotesSmartV2Api.md#archive1) | **POST** /v2/quotes/files/archive | Prepares a ZIP archive that contains the specified files.
[**changeStatus3**](QuotesSmartV2Api.md#changeStatus3) | **PUT** /v2/quotes/{quoteId}/status | Changes quote status if possible (400 Bad Request is returned otherwise).
[**create7**](QuotesSmartV2Api.md#create7) | **POST** /v2/quotes | Creates a new Smart Quote.
[**createPayable3**](QuotesSmartV2Api.md#createPayable3) | **POST** /v2/quotes/{quoteId}/finance/payables | Adds a payable to a quote.
[**createReceivable3**](QuotesSmartV2Api.md#createReceivable3) | **POST** /v2/quotes/{quoteId}/finance/receivables | Adds a receivable to a quote.
[**deletePayable3**](QuotesSmartV2Api.md#deletePayable3) | **DELETE** /v2/quotes/{quoteId}/finance/payables/{payableId} | Deletes a payable.
[**deleteReceivable3**](QuotesSmartV2Api.md#deleteReceivable3) | **DELETE** /v2/quotes/{quoteId}/finance/receivables/{receivableId} | Deletes a receivable.
[**getById10**](QuotesSmartV2Api.md#getById10) | **GET** /v2/quotes/{quoteId} | Returns quote details.
[**getContacts3**](QuotesSmartV2Api.md#getContacts3) | **GET** /v2/quotes/{quoteId}/clientContacts | Returns Client Contacts information for a quote.
[**getCustomFields9**](QuotesSmartV2Api.md#getCustomFields9) | **GET** /v2/quotes/{quoteId}/customFields | Returns a list of custom field keys and values for a project.
[**getFileById3**](QuotesSmartV2Api.md#getFileById3) | **GET** /v2/quotes/files/{fileId} | Returns details of a file.
[**getFileContentById1**](QuotesSmartV2Api.md#getFileContentById1) | **GET** /v2/quotes/files/{fileId}/download/{fileName} | Downloads a file content.
[**getFiles1**](QuotesSmartV2Api.md#getFiles1) | **GET** /v2/quotes/{quoteId}/files | Returns list of files in a quote.
[**getFinance3**](QuotesSmartV2Api.md#getFinance3) | **GET** /v2/quotes/{quoteId}/finance | Returns finance information for a quote.
[**getJobs1**](QuotesSmartV2Api.md#getJobs1) | **GET** /v2/quotes/{quoteId}/jobs | Returns list of jobs in a quote.
[**updateBusinessDays**](QuotesSmartV2Api.md#updateBusinessDays) | **PUT** /v2/quotes/{quoteId}/businessDays | Updates Business Days for a quote.
[**updateClientNotes1**](QuotesSmartV2Api.md#updateClientNotes1) | **PUT** /v2/quotes/{quoteId}/clientNotes | Updates Client Notes for a quote.
[**updateClientReferenceNumber1**](QuotesSmartV2Api.md#updateClientReferenceNumber1) | **PUT** /v2/quotes/{quoteId}/clientReferenceNumber | Updates Client Reference Number for a quote.
[**updateContacts3**](QuotesSmartV2Api.md#updateContacts3) | **PUT** /v2/quotes/{quoteId}/clientContacts | Updates Client Contacts for a quote.
[**updateCustomField3**](QuotesSmartV2Api.md#updateCustomField3) | **PUT** /v2/quotes/{quoteId}/customFields/{key} | Updates a custom field with a specified key in a quote.
[**updateExpectedDeliveryDate**](QuotesSmartV2Api.md#updateExpectedDeliveryDate) | **PUT** /v2/quotes/{quoteId}/expectedDeliveryDate | Updates Expected Delivery Date for a quote.
[**updateInternalNotes1**](QuotesSmartV2Api.md#updateInternalNotes1) | **PUT** /v2/quotes/{quoteId}/internalNotes | Updates Internal Notes for a quote.
[**updatePayable3**](QuotesSmartV2Api.md#updatePayable3) | **PUT** /v2/quotes/{quoteId}/finance/payables/{payableId} | Updates a payable.
[**updateQuoteExpiry**](QuotesSmartV2Api.md#updateQuoteExpiry) | **PUT** /v2/quotes/{quoteId}/quoteExpiry | Updates Quote Expiry Date for a quote.
[**updateReceivable3**](QuotesSmartV2Api.md#updateReceivable3) | **PUT** /v2/quotes/{quoteId}/finance/receivables/{receivableId} | Updates a receivable.
[**updateSourceLanguage1**](QuotesSmartV2Api.md#updateSourceLanguage1) | **PUT** /v2/quotes/{quoteId}/sourceLanguage | Updates source language for a quote.
[**updateSpecialization1**](QuotesSmartV2Api.md#updateSpecialization1) | **PUT** /v2/quotes/{quoteId}/specialization | Updates specialization for a quote.
[**updateTargetLanguages1**](QuotesSmartV2Api.md#updateTargetLanguages1) | **PUT** /v2/quotes/{quoteId}/targetLanguages | Updates target languages for a quote.
[**updateVendorInstructions1**](QuotesSmartV2Api.md#updateVendorInstructions1) | **PUT** /v2/quotes/{quoteId}/vendorInstructions | Updates instructions for all vendors performing the jobs in a quote.
[**updateVolume1**](QuotesSmartV2Api.md#updateVolume1) | **PUT** /v2/quotes/{quoteId}/volume | Updates volume for a quote.
[**uploadFile3**](QuotesSmartV2Api.md#uploadFile3) | **POST** /v2/quotes/{quoteId}/files/upload | Uploads file to the quote as a file uploaded by PM.



## addFiles2

> addFiles2(quoteId, timeDTO)

Adds files to the quote as added by PM.

Adds files to the quote as added by PM. The files have to be uploaded beforehand (see \&quot;POST v2/quotes/{quoteId}/files/upload\&quot; operation). The following properties can be specified for each file:&lt;ul&gt;&lt;li&gt;category (required, 400 Bad Request is returned otherwise)&lt;/li&gt;&lt;li&gt;languageIds – when the file category depends on a list of languages&lt;/li&gt;&lt;li&gt;languageCombinationIds – when the file category depends on a list of language combinations&lt;/li&gt;&lt;/ul&gt;

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesSmartV2Api();
let quoteId = "quoteId_example"; // String | quote's internal identifier
let timeDTO = /home-api/assets/examples/v2/quotes/addFiles.json#requestBody; // TimeDTO | Added files to the quote as added by PM.
apiInstance.addFiles2(quoteId, timeDTO, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 
 **timeDTO** | [**TimeDTO**](TimeDTO.md)| Added files to the quote as added by PM. | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## archive1

> FilesArchiveDto archive1(filesDto)

Prepares a ZIP archive that contains the specified files.

Prepares a ZIP archive that contains the specified files.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesSmartV2Api();
let filesDto = /home-api/assets/examples/v2/quotes/archive.json#requestBody; // FilesDto | Prepared ZIP archive that contains the specified files.
apiInstance.archive1(filesDto, (error, data, response) => {
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
 **filesDto** | [**FilesDto**](FilesDto.md)| Prepared ZIP archive that contains the specified files. | 

### Return type

[**FilesArchiveDto**](FilesArchiveDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json;charset=UTF-8
- **Accept**: application/json;charset=UTF-8


## changeStatus3

> changeStatus3(quoteId, projectStatusDTO)

Changes quote status if possible (400 Bad Request is returned otherwise).

Changes quote status if possible (400 Bad Request is returned otherwise). The status has to be specified using one of the following keys: &lt;ul&gt;&lt;li&gt;PENDING – available when the job has one of the following statuses: REQUESTED, REJECTED&lt;/li&gt;&lt;li&gt;SENT – available when the job has one of the following statuses: PENDING&lt;/li&gt;&lt;li&gt;APPROVED – available when the job has one of the following statuses: REQUESTED, PENDING, SENT, APPROVED_BY_CLIENT&lt;/li&gt;&lt;li&gt;REJECTED – available when the job has one of the following statuses: REQUESTED, PENDING, SENT&lt;/li&gt;&lt;/ul&gt;

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesSmartV2Api();
let quoteId = "quoteId_example"; // String | quote's internal identifier
let projectStatusDTO = /home-api/assets/examples/v2/quotes/changeStatus.json#requestBody; // ProjectStatusDTO | Changed Quote status.
apiInstance.changeStatus3(quoteId, projectStatusDTO, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 
 **projectStatusDTO** | [**ProjectStatusDTO**](ProjectStatusDTO.md)| Changed Quote status. | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## create7

> QuoteDTOv2 create7(opts)

Creates a new Smart Quote.

Creates a new Smart Quote. If the specified service ID refers to Classic Quote, 400 Bad Request is returned instead.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesSmartV2Api();
let opts = {
  'quoteCreateDTO': new XtrfHomePortalApi.QuoteCreateDTO() // QuoteCreateDTO | Project to create
};
apiInstance.create7(opts, (error, data, response) => {
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
 **quoteCreateDTO** | [**QuoteCreateDTO**](QuoteCreateDTO.md)| Project to create | [optional] 

### Return type

[**QuoteDTOv2**](QuoteDTOv2.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json;charset=UTF-8


## createPayable3

> PayableDTO createPayable3(quoteId, payableCreateDTO)

Adds a payable to a quote.

Adds a payable to a quote.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesSmartV2Api();
let quoteId = "quoteId_example"; // String | quote's internal identifier
let payableCreateDTO = /home-api/assets/examples/v2/quotes/createPayable.json#requestBody; // PayableCreateDTO | 
apiInstance.createPayable3(quoteId, payableCreateDTO, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 
 **payableCreateDTO** | [**PayableCreateDTO**](PayableCreateDTO.md)|  | 

### Return type

[**PayableDTO**](PayableDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createReceivable3

> ReceivableDTO createReceivable3(quoteId, receivableCreateDTO)

Adds a receivable to a quote.

Adds a receivable to a quote.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesSmartV2Api();
let quoteId = "quoteId_example"; // String | quote's internal identifier
let receivableCreateDTO = /home-api/assets/examples/v2/quotes/createReceivable.json#requestBody; // ReceivableCreateDTO | 
apiInstance.createReceivable3(quoteId, receivableCreateDTO, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 
 **receivableCreateDTO** | [**ReceivableCreateDTO**](ReceivableCreateDTO.md)|  | 

### Return type

[**ReceivableDTO**](ReceivableDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deletePayable3

> deletePayable3(quoteId, payableId)

Deletes a payable.

Deletes a payable.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesSmartV2Api();
let quoteId = "quoteId_example"; // String | quote's internal identifier
let payableId = 789; // Number | payable's internal identifier
apiInstance.deletePayable3(quoteId, payableId, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 
 **payableId** | **Number**| payable&#39;s internal identifier | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteReceivable3

> deleteReceivable3(quoteId, receivableId)

Deletes a receivable.

Deletes a receivable.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesSmartV2Api();
let quoteId = "quoteId_example"; // String | quote's internal identifier
let receivableId = 789; // Number | receivable's internal identifier
apiInstance.deleteReceivable3(quoteId, receivableId, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 
 **receivableId** | **Number**| receivable&#39;s internal identifier | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getById10

> QuoteDTOv2 getById10(quoteId)

Returns quote details.

Returns quote details. If the specified quote ID refers to Classic Quote, 400 Bad Request is returned instead.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesSmartV2Api();
let quoteId = "quoteId_example"; // String | quote's internal identifier
apiInstance.getById10(quoteId, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 

### Return type

[**QuoteDTOv2**](QuoteDTOv2.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getContacts3

> SmartContactsDTO getContacts3(quoteId)

Returns Client Contacts information for a quote.

Returns Client Contacts information for a quote.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesSmartV2Api();
let quoteId = "quoteId_example"; // String | quote's internal identifier
apiInstance.getContacts3(quoteId, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 

### Return type

[**SmartContactsDTO**](SmartContactsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getCustomFields9

> [CustomFieldDTO] getCustomFields9(quoteId)

Returns a list of custom field keys and values for a project.

Returns a list of custom field keys and values for a project.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesSmartV2Api();
let quoteId = "quoteId_example"; // String | quote's internal identifier
apiInstance.getCustomFields9(quoteId, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 

### Return type

[**[CustomFieldDTO]**](CustomFieldDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getFileById3

> ProjectFileDto getFileById3(fileId)

Returns details of a file.

Returns details of a file.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesSmartV2Api();
let fileId = "fileId_example"; // String | file's internal identifier
apiInstance.getFileById3(fileId, (error, data, response) => {
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
 **fileId** | **String**| file&#39;s internal identifier | 

### Return type

[**ProjectFileDto**](ProjectFileDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getFileContentById1

> getFileContentById1(fileId, fileName)

Downloads a file content.

Downloads a file content.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesSmartV2Api();
let fileId = "fileId_example"; // String | file's internal identifier
let fileName = "fileName_example"; // String | file's name
apiInstance.getFileContentById1(fileId, fileName, (error, data, response) => {
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
 **fileId** | **String**| file&#39;s internal identifier | 
 **fileName** | **String**| file&#39;s name | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: multipart/form-data


## getFiles1

> [ProjectFileDto] getFiles1(quoteId)

Returns list of files in a quote.

Returns list of files in a quote. Only files added to the quote (i.e. files that have assigned category and languages) are listed.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesSmartV2Api();
let quoteId = "quoteId_example"; // String | quote's internal identifier
apiInstance.getFiles1(quoteId, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 

### Return type

[**[ProjectFileDto]**](ProjectFileDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getFinance3

> FinanceDTO getFinance3(quoteId)

Returns finance information for a quote.

Returns finance information for a quote.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesSmartV2Api();
let quoteId = "quoteId_example"; // String | quote's internal identifier
apiInstance.getFinance3(quoteId, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 

### Return type

[**FinanceDTO**](FinanceDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getJobs1

> [JobDto] getJobs1(quoteId)

Returns list of jobs in a quote.

Returns list of jobs in a quote.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesSmartV2Api();
let quoteId = "quoteId_example"; // String | quote's internal identifier
apiInstance.getJobs1(quoteId, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 

### Return type

[**[JobDto]**](JobDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## updateBusinessDays

> updateBusinessDays(quoteId, body)

Updates Business Days for a quote.

Updates Business Days for a quote.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesSmartV2Api();
let quoteId = "quoteId_example"; // String | quote's internal identifier
let body = /home-api/assets/examples/v2/quotes/updateBusinessDays.json#requestBody; // Number | Updated Business Days for a quote.
apiInstance.updateBusinessDays(quoteId, body, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 
 **body** | **Number**| Updated Business Days for a quote. | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateClientNotes1

> updateClientNotes1(quoteId, stringDTO)

Updates Client Notes for a quote.

Updates Client Notes for a quote.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesSmartV2Api();
let quoteId = "quoteId_example"; // String | quote's internal identifier
let stringDTO = /home-api/assets/examples/v2/quotes/updateClientNotes.json#requestBody; // StringDTO | Updated Client Notes for a quote.
apiInstance.updateClientNotes1(quoteId, stringDTO, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 
 **stringDTO** | [**StringDTO**](StringDTO.md)| Updated Client Notes for a quote. | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateClientReferenceNumber1

> updateClientReferenceNumber1(quoteId, stringDTO)

Updates Client Reference Number for a quote.

Updates Client Reference Number for a quote.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesSmartV2Api();
let quoteId = "quoteId_example"; // String | quote's internal identifier
let stringDTO = /home-api/assets/examples/v2/quotes/updateClientReferenceNumber.json#requestBody; // StringDTO | Updated Client Reference Number for a quote.
apiInstance.updateClientReferenceNumber1(quoteId, stringDTO, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 
 **stringDTO** | [**StringDTO**](StringDTO.md)| Updated Client Reference Number for a quote. | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateContacts3

> SmartContactsDTO updateContacts3(quoteId, smartContactsDTO)

Updates Client Contacts for a quote.

Updates Client Contacts for a quote.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesSmartV2Api();
let quoteId = "quoteId_example"; // String | quote's internal identifier
let smartContactsDTO = /home-api/assets/examples/v2/quotes/updateClientContacts.json#requestBody; // SmartContactsDTO | Updated Client Contacts for a quote.
apiInstance.updateContacts3(quoteId, smartContactsDTO, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 
 **smartContactsDTO** | [**SmartContactsDTO**](SmartContactsDTO.md)| Updated Client Contacts for a quote. | 

### Return type

[**SmartContactsDTO**](SmartContactsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json;charset=UTF-8
- **Accept**: application/json;charset=UTF-8


## updateCustomField3

> updateCustomField3(quoteId, key, smartCustomFieldDTO)

Updates a custom field with a specified key in a quote.

Updates a custom field with a specified key in a quote.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesSmartV2Api();
let quoteId = "quoteId_example"; // String | quote's internal identifier
let key = "key_example"; // String | custom field's key
let smartCustomFieldDTO = /home-api/assets/examples/v2/quotes/updateCustomField.json#requestBody; // SmartCustomFieldDTO | Updated custom field with a specified key in a quote.
apiInstance.updateCustomField3(quoteId, key, smartCustomFieldDTO, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 
 **key** | **String**| custom field&#39;s key | 
 **smartCustomFieldDTO** | [**SmartCustomFieldDTO**](SmartCustomFieldDTO.md)| Updated custom field with a specified key in a quote. | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateExpectedDeliveryDate

> updateExpectedDeliveryDate(quoteId, timeDTO)

Updates Expected Delivery Date for a quote.

Updates Expected Delivery Date for a quote.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesSmartV2Api();
let quoteId = "quoteId_example"; // String | quote's internal identifier
let timeDTO = /home-api/assets/examples/v2/quotes/updateExpectedDeliveryDate.json#requestBody; // TimeDTO | Updated Expected Delivery Date for a quote.
apiInstance.updateExpectedDeliveryDate(quoteId, timeDTO, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 
 **timeDTO** | [**TimeDTO**](TimeDTO.md)| Updated Expected Delivery Date for a quote. | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateInternalNotes1

> updateInternalNotes1(quoteId, stringDTO)

Updates Internal Notes for a quote.

Updates Internal Notes for a quote.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesSmartV2Api();
let quoteId = "quoteId_example"; // String | quote's internal identifier
let stringDTO = /home-api/assets/examples/v2/quotes/updateInternalNotes.json#requestBody; // StringDTO | Updated Internal Notes for a quote.
apiInstance.updateInternalNotes1(quoteId, stringDTO, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 
 **stringDTO** | [**StringDTO**](StringDTO.md)| Updated Internal Notes for a quote. | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updatePayable3

> PayableDTO updatePayable3(quoteId, payableId, payableDTO)

Updates a payable.

Updates a payable.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesSmartV2Api();
let quoteId = "quoteId_example"; // String | quote's internal identifier
let payableId = 789; // Number | payable's internal identifier
let payableDTO = /home-api/assets/examples/v2/quotes/updatePayable.json#requestBody; // PayableDTO | 
apiInstance.updatePayable3(quoteId, payableId, payableDTO, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 
 **payableId** | **Number**| payable&#39;s internal identifier | 
 **payableDTO** | [**PayableDTO**](PayableDTO.md)|  | 

### Return type

[**PayableDTO**](PayableDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateQuoteExpiry

> updateQuoteExpiry(quoteId, timeDTO)

Updates Quote Expiry Date for a quote.

Updates Quote Expiry Date for a quote.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesSmartV2Api();
let quoteId = "quoteId_example"; // String | quote's internal identifier
let timeDTO = /home-api/assets/examples/v2/quotes/updateQuoteExpiry.json#requestBody; // TimeDTO | Updated Quote Expiry Date for a quote.
apiInstance.updateQuoteExpiry(quoteId, timeDTO, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 
 **timeDTO** | [**TimeDTO**](TimeDTO.md)| Updated Quote Expiry Date for a quote. | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateReceivable3

> ReceivableDTO updateReceivable3(quoteId, receivableId, receivableDTO)

Updates a receivable.

Updates a receivable.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesSmartV2Api();
let quoteId = "quoteId_example"; // String | quote's internal identifier
let receivableId = 789; // Number | receivable's internal identifier
let receivableDTO = /home-api/assets/examples/v2/quotes/updateReceivable.json#requestBody; // ReceivableDTO | 
apiInstance.updateReceivable3(quoteId, receivableId, receivableDTO, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 
 **receivableId** | **Number**| receivable&#39;s internal identifier | 
 **receivableDTO** | [**ReceivableDTO**](ReceivableDTO.md)|  | 

### Return type

[**ReceivableDTO**](ReceivableDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateSourceLanguage1

> updateSourceLanguage1(quoteId, sourceLanguageDTO)

Updates source language for a quote.

Updates source language for a quote.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesSmartV2Api();
let quoteId = "quoteId_example"; // String | quote's internal identifier
let sourceLanguageDTO = /home-api/assets/examples/v2/quotes/updateSourceLanguage.json#requestBody; // SourceLanguageDTO | Updated source language for a quote.
apiInstance.updateSourceLanguage1(quoteId, sourceLanguageDTO, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 
 **sourceLanguageDTO** | [**SourceLanguageDTO**](SourceLanguageDTO.md)| Updated source language for a quote. | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateSpecialization1

> updateSpecialization1(quoteId, specializationDTO)

Updates specialization for a quote.

Updates specialization for a quote.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesSmartV2Api();
let quoteId = "quoteId_example"; // String | quote's internal identifier
let specializationDTO = /home-api/assets/examples/v2/quotes/updateSpecialization.json#requestBody; // SpecializationDTO | Updated specialization for a quote.
apiInstance.updateSpecialization1(quoteId, specializationDTO, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 
 **specializationDTO** | [**SpecializationDTO**](SpecializationDTO.md)| Updated specialization for a quote. | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateTargetLanguages1

> updateTargetLanguages1(quoteId, targetLanguagesDTO)

Updates target languages for a quote.

Updates target languages for a quote.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesSmartV2Api();
let quoteId = "quoteId_example"; // String | quote's internal identifier
let targetLanguagesDTO = /home-api/assets/examples/v2/quotes/updateTargetLanguages.json#requestBody; // TargetLanguagesDTO | Updated target languages for a quote.
apiInstance.updateTargetLanguages1(quoteId, targetLanguagesDTO, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 
 **targetLanguagesDTO** | [**TargetLanguagesDTO**](TargetLanguagesDTO.md)| Updated target languages for a quote. | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateVendorInstructions1

> updateVendorInstructions1(quoteId, stringDTO)

Updates instructions for all vendors performing the jobs in a quote.

Updates instructions for all vendors performing the jobs in a quote. See also \&quot;PUT /jobs/{jobId}/instructions\&quot; for updating instructions for a specific job in a project or quote.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesSmartV2Api();
let quoteId = "quoteId_example"; // String | quote's internal identifier
let stringDTO = /home-api/assets/examples/v2/quotes/updateInstructionsForAllJobs.json#requestBody; // StringDTO | Updated instructions for all vendors performing the jobs in a quote.
apiInstance.updateVendorInstructions1(quoteId, stringDTO, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 
 **stringDTO** | [**StringDTO**](StringDTO.md)| Updated instructions for all vendors performing the jobs in a quote. | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateVolume1

> updateVolume1(quoteId, bigDecimalDTO)

Updates volume for a quote.

Updates volume for a quote.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesSmartV2Api();
let quoteId = "quoteId_example"; // String | quote's internal identifier
let bigDecimalDTO = /home-api/assets/examples/v2/quotes/updateVolume.json#requestBody; // BigDecimalDTO | Updated volume for a quote.
apiInstance.updateVolume1(quoteId, bigDecimalDTO, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 
 **bigDecimalDTO** | [**BigDecimalDTO**](BigDecimalDTO.md)| Updated volume for a quote. | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## uploadFile3

> FileDto uploadFile3(quoteId, opts)

Uploads file to the quote as a file uploaded by PM.

Uploads file to the quote as a file uploaded by PM. Only one file can be uploaded at once. When the upload is finished the file has to be added by specifying its category and languages (see \&quot;PUT /v2/quotes/{quoteId}/files/add\&quot; operation).

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesSmartV2Api();
let quoteId = "quoteId_example"; // String | quote's internal identifier
let opts = {
  'file': "/path/to/file" // File | 
};
apiInstance.uploadFile3(quoteId, opts, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 
 **file** | **File**|  | [optional] 

### Return type

[**FileDto**](FileDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json;charset=UTF-8

