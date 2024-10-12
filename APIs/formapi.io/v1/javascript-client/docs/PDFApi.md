# ApiV1.PDFApi

All URIs are relative to *https://api.docspring.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addFieldsToTemplate**](PDFApi.md#addFieldsToTemplate) | **PUT** /templates/{template_id}/add_fields | Add new fields to a Template
[**batchGeneratePdfV1**](PDFApi.md#batchGeneratePdfV1) | **POST** /templates/{template_id}/submissions/batch | Generates multiple PDFs
[**batchGeneratePdfs**](PDFApi.md#batchGeneratePdfs) | **POST** /submissions/batches | Generates multiple PDFs
[**combinePdfs**](PDFApi.md#combinePdfs) | **POST** /combined_submissions?v&#x3D;2 | Merge submission PDFs, template PDFs, or custom files
[**combineSubmissions**](PDFApi.md#combineSubmissions) | **POST** /combined_submissions | Merge generated PDFs together
[**copyTemplate**](PDFApi.md#copyTemplate) | **POST** /templates/{template_id}/copy | Copy a Template
[**createCustomFileFromUpload**](PDFApi.md#createCustomFileFromUpload) | **POST** /custom_files | Create a new custom file from a cached presign upload
[**createDataRequestToken**](PDFApi.md#createDataRequestToken) | **POST** /data_requests/{data_request_id}/tokens | Creates a new data request token for form authentication
[**createFolder**](PDFApi.md#createFolder) | **POST** /folders/ | Create a folder
[**createHTMLTemplate**](PDFApi.md#createHTMLTemplate) | **POST** /templates?desc&#x3D;html | Create a new HTML template
[**createPDFTemplate**](PDFApi.md#createPDFTemplate) | **POST** /templates | Create a new PDF template with a form POST file upload
[**createPDFTemplateFromUpload**](PDFApi.md#createPDFTemplateFromUpload) | **POST** /templates?desc&#x3D;cached_upload | Create a new PDF template from a cached presign upload
[**deleteFolder**](PDFApi.md#deleteFolder) | **DELETE** /folders/{folder_id} | Delete a folder
[**expireCombinedSubmission**](PDFApi.md#expireCombinedSubmission) | **DELETE** /combined_submissions/{combined_submission_id} | Expire a combined submission
[**expireSubmission**](PDFApi.md#expireSubmission) | **DELETE** /submissions/{submission_id} | Expire a PDF submission
[**generatePDF**](PDFApi.md#generatePDF) | **POST** /templates/{template_id}/submissions | Generates a new PDF
[**getCombinedSubmission**](PDFApi.md#getCombinedSubmission) | **GET** /combined_submissions/{combined_submission_id} | Check the status of a combined submission (merged PDFs)
[**getDataRequest**](PDFApi.md#getDataRequest) | **GET** /data_requests/{data_request_id} | Look up a submission data request
[**getFullTemplate**](PDFApi.md#getFullTemplate) | **GET** /templates/{template_id}?full&#x3D;true | Fetch the full template attributes
[**getPresignUrl**](PDFApi.md#getPresignUrl) | **GET** /uploads/presign | Get a presigned URL so that you can upload a file to our AWS S3 bucket
[**getSubmission**](PDFApi.md#getSubmission) | **GET** /submissions/{submission_id} | Check the status of a PDF
[**getSubmissionBatch**](PDFApi.md#getSubmissionBatch) | **GET** /submissions/batches/{submission_batch_id} | Check the status of a submission batch job
[**getTemplate**](PDFApi.md#getTemplate) | **GET** /templates/{template_id} | Check the status of an uploaded template
[**getTemplateSchema**](PDFApi.md#getTemplateSchema) | **GET** /templates/{template_id}/schema | Fetch the JSON schema for a template
[**listCombinedSubmissions**](PDFApi.md#listCombinedSubmissions) | **GET** /combined_submissions | Get a list of all combined submissions
[**listFolders**](PDFApi.md#listFolders) | **GET** /folders/ | Get a list of all folders
[**listSubmissions**](PDFApi.md#listSubmissions) | **GET** /submissions | List all submissions
[**listTemplates**](PDFApi.md#listTemplates) | **GET** /templates | Get a list of all templates
[**moveFolderToFolder**](PDFApi.md#moveFolderToFolder) | **POST** /folders/{folder_id}/move | Move a folder
[**moveTemplateToFolder**](PDFApi.md#moveTemplateToFolder) | **POST** /templates/{template_id}/move | Move Template to folder
[**renameFolder**](PDFApi.md#renameFolder) | **POST** /folders/{folder_id}/rename | Rename a folder
[**templatesTemplateIdSubmissionsGet**](PDFApi.md#templatesTemplateIdSubmissionsGet) | **GET** /templates/{template_id}/submissions | List all submissions for a given template
[**testAuthentication**](PDFApi.md#testAuthentication) | **GET** /authentication | Test Authentication
[**updateDataRequest**](PDFApi.md#updateDataRequest) | **PUT** /data_requests/{data_request_id} | Update a submission data request
[**updateTemplate**](PDFApi.md#updateTemplate) | **PUT** /templates/{template_id} | Update a Template



## addFieldsToTemplate

> AddFieldsTemplateResponse addFieldsToTemplate(templateId, addFieldsData)

Add new fields to a Template

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: api_token_basic
let api_token_basic = defaultClient.authentications['api_token_basic'];
api_token_basic.username = 'YOUR USERNAME';
api_token_basic.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.PDFApi();
let templateId = "tpl_000000000000000002"; // String | 
let addFieldsData = new ApiV1.AddFieldsData(); // AddFieldsData | 
apiInstance.addFieldsToTemplate(templateId, addFieldsData, (error, data, response) => {
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
 **templateId** | **String**|  | 
 **addFieldsData** | [**AddFieldsData**](AddFieldsData.md)|  | 

### Return type

[**AddFieldsTemplateResponse**](AddFieldsTemplateResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchGeneratePdfV1

> [CreateSubmissionResponse1] batchGeneratePdfV1(templateId, requestBody)

Generates multiple PDFs

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: api_token_basic
let api_token_basic = defaultClient.authentications['api_token_basic'];
api_token_basic.username = 'YOUR USERNAME';
api_token_basic.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.PDFApi();
let templateId = "tpl_000000000000000001"; // String | 
let requestBody = null; // [Object] | 
apiInstance.batchGeneratePdfV1(templateId, requestBody, (error, data, response) => {
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
 **templateId** | **String**|  | 
 **requestBody** | [**[Object]**](Object.md)|  | 

### Return type

[**[CreateSubmissionResponse1]**](CreateSubmissionResponse1.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchGeneratePdfs

> CreateSubmissionBatchResponse batchGeneratePdfs(submissionBatchData)

Generates multiple PDFs

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: api_token_basic
let api_token_basic = defaultClient.authentications['api_token_basic'];
api_token_basic.username = 'YOUR USERNAME';
api_token_basic.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.PDFApi();
let submissionBatchData = new ApiV1.SubmissionBatchData(); // SubmissionBatchData | 
apiInstance.batchGeneratePdfs(submissionBatchData, (error, data, response) => {
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
 **submissionBatchData** | [**SubmissionBatchData**](SubmissionBatchData.md)|  | 

### Return type

[**CreateSubmissionBatchResponse**](CreateSubmissionBatchResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## combinePdfs

> CreateCombinedSubmissionResponse combinePdfs(combinePdfsData)

Merge submission PDFs, template PDFs, or custom files

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: api_token_basic
let api_token_basic = defaultClient.authentications['api_token_basic'];
api_token_basic.username = 'YOUR USERNAME';
api_token_basic.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.PDFApi();
let combinePdfsData = new ApiV1.CombinePdfsData(); // CombinePdfsData | 
apiInstance.combinePdfs(combinePdfsData, (error, data, response) => {
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
 **combinePdfsData** | [**CombinePdfsData**](CombinePdfsData.md)|  | 

### Return type

[**CreateCombinedSubmissionResponse**](CreateCombinedSubmissionResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## combineSubmissions

> CreateCombinedSubmissionResponse combineSubmissions(combinedSubmissionData)

Merge generated PDFs together

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: api_token_basic
let api_token_basic = defaultClient.authentications['api_token_basic'];
api_token_basic.username = 'YOUR USERNAME';
api_token_basic.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.PDFApi();
let combinedSubmissionData = new ApiV1.CombinedSubmissionData(); // CombinedSubmissionData | 
apiInstance.combineSubmissions(combinedSubmissionData, (error, data, response) => {
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
 **combinedSubmissionData** | [**CombinedSubmissionData**](CombinedSubmissionData.md)|  | 

### Return type

[**CreateCombinedSubmissionResponse**](CreateCombinedSubmissionResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## copyTemplate

> Template copyTemplate(templateId, opts)

Copy a Template

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: api_token_basic
let api_token_basic = defaultClient.authentications['api_token_basic'];
api_token_basic.username = 'YOUR USERNAME';
api_token_basic.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.PDFApi();
let templateId = "tpl_000000000000000001"; // String | 
let opts = {
  'copyTemplateData': new ApiV1.CopyTemplateData() // CopyTemplateData | 
};
apiInstance.copyTemplate(templateId, opts, (error, data, response) => {
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
 **templateId** | **String**|  | 
 **copyTemplateData** | [**CopyTemplateData**](CopyTemplateData.md)|  | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createCustomFileFromUpload

> CreateCustomFileResponse createCustomFileFromUpload(createCustomFileData)

Create a new custom file from a cached presign upload

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: api_token_basic
let api_token_basic = defaultClient.authentications['api_token_basic'];
api_token_basic.username = 'YOUR USERNAME';
api_token_basic.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.PDFApi();
let createCustomFileData = new ApiV1.CreateCustomFileData(); // CreateCustomFileData | 
apiInstance.createCustomFileFromUpload(createCustomFileData, (error, data, response) => {
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
 **createCustomFileData** | [**CreateCustomFileData**](CreateCustomFileData.md)|  | 

### Return type

[**CreateCustomFileResponse**](CreateCustomFileResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createDataRequestToken

> CreateSubmissionDataRequestTokenResponse createDataRequestToken(dataRequestId)

Creates a new data request token for form authentication

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: api_token_basic
let api_token_basic = defaultClient.authentications['api_token_basic'];
api_token_basic.username = 'YOUR USERNAME';
api_token_basic.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.PDFApi();
let dataRequestId = "drq_000000000000000001"; // String | 
apiInstance.createDataRequestToken(dataRequestId, (error, data, response) => {
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
 **dataRequestId** | **String**|  | 

### Return type

[**CreateSubmissionDataRequestTokenResponse**](CreateSubmissionDataRequestTokenResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createFolder

> Folder createFolder(createFolderData)

Create a folder

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: api_token_basic
let api_token_basic = defaultClient.authentications['api_token_basic'];
api_token_basic.username = 'YOUR USERNAME';
api_token_basic.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.PDFApi();
let createFolderData = new ApiV1.CreateFolderData(); // CreateFolderData | 
apiInstance.createFolder(createFolderData, (error, data, response) => {
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
 **createFolderData** | [**CreateFolderData**](CreateFolderData.md)|  | 

### Return type

[**Folder**](Folder.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createHTMLTemplate

> PendingTemplate createHTMLTemplate(createHtmlTemplateData)

Create a new HTML template

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: api_token_basic
let api_token_basic = defaultClient.authentications['api_token_basic'];
api_token_basic.username = 'YOUR USERNAME';
api_token_basic.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.PDFApi();
let createHtmlTemplateData = new ApiV1.CreateHtmlTemplateData(); // CreateHtmlTemplateData | 
apiInstance.createHTMLTemplate(createHtmlTemplateData, (error, data, response) => {
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
 **createHtmlTemplateData** | [**CreateHtmlTemplateData**](CreateHtmlTemplateData.md)|  | 

### Return type

[**PendingTemplate**](PendingTemplate.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createPDFTemplate

> PendingTemplate createPDFTemplate(templateDocument, templateName, opts)

Create a new PDF template with a form POST file upload

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: api_token_basic
let api_token_basic = defaultClient.authentications['api_token_basic'];
api_token_basic.username = 'YOUR USERNAME';
api_token_basic.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.PDFApi();
let templateDocument = "/path/to/file"; // File | 
let templateName = "templateName_example"; // String | 
let opts = {
  'templateParentFolderId': "templateParentFolderId_example" // String | 
};
apiInstance.createPDFTemplate(templateDocument, templateName, opts, (error, data, response) => {
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
 **templateDocument** | **File**|  | 
 **templateName** | **String**|  | 
 **templateParentFolderId** | **String**|  | [optional] 

### Return type

[**PendingTemplate**](PendingTemplate.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## createPDFTemplateFromUpload

> PendingTemplate createPDFTemplateFromUpload(createTemplateFromUploadData)

Create a new PDF template from a cached presign upload

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: api_token_basic
let api_token_basic = defaultClient.authentications['api_token_basic'];
api_token_basic.username = 'YOUR USERNAME';
api_token_basic.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.PDFApi();
let createTemplateFromUploadData = new ApiV1.CreateTemplateFromUploadData(); // CreateTemplateFromUploadData | 
apiInstance.createPDFTemplateFromUpload(createTemplateFromUploadData, (error, data, response) => {
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
 **createTemplateFromUploadData** | [**CreateTemplateFromUploadData**](CreateTemplateFromUploadData.md)|  | 

### Return type

[**PendingTemplate**](PendingTemplate.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteFolder

> Folder deleteFolder(folderId)

Delete a folder

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: api_token_basic
let api_token_basic = defaultClient.authentications['api_token_basic'];
api_token_basic.username = 'YOUR USERNAME';
api_token_basic.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.PDFApi();
let folderId = "fld_000000000000000001"; // String | 
apiInstance.deleteFolder(folderId, (error, data, response) => {
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
 **folderId** | **String**|  | 

### Return type

[**Folder**](Folder.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## expireCombinedSubmission

> CombinedSubmission expireCombinedSubmission(combinedSubmissionId)

Expire a combined submission

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: api_token_basic
let api_token_basic = defaultClient.authentications['api_token_basic'];
api_token_basic.username = 'YOUR USERNAME';
api_token_basic.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.PDFApi();
let combinedSubmissionId = "com_000000000000000001"; // String | 
apiInstance.expireCombinedSubmission(combinedSubmissionId, (error, data, response) => {
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
 **combinedSubmissionId** | **String**|  | 

### Return type

[**CombinedSubmission**](CombinedSubmission.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## expireSubmission

> Submission expireSubmission(submissionId)

Expire a PDF submission

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: api_token_basic
let api_token_basic = defaultClient.authentications['api_token_basic'];
api_token_basic.username = 'YOUR USERNAME';
api_token_basic.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.PDFApi();
let submissionId = "sub_000000000000000001"; // String | 
apiInstance.expireSubmission(submissionId, (error, data, response) => {
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
 **submissionId** | **String**|  | 

### Return type

[**Submission**](Submission.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## generatePDF

> CreateSubmissionResponse generatePDF(templateId, submissionData)

Generates a new PDF

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: api_token_basic
let api_token_basic = defaultClient.authentications['api_token_basic'];
api_token_basic.username = 'YOUR USERNAME';
api_token_basic.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.PDFApi();
let templateId = "tpl_000000000000000001"; // String | 
let submissionData = new ApiV1.SubmissionData(); // SubmissionData | 
apiInstance.generatePDF(templateId, submissionData, (error, data, response) => {
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
 **templateId** | **String**|  | 
 **submissionData** | [**SubmissionData**](SubmissionData.md)|  | 

### Return type

[**CreateSubmissionResponse**](CreateSubmissionResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getCombinedSubmission

> CombinedSubmission getCombinedSubmission(combinedSubmissionId)

Check the status of a combined submission (merged PDFs)

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: api_token_basic
let api_token_basic = defaultClient.authentications['api_token_basic'];
api_token_basic.username = 'YOUR USERNAME';
api_token_basic.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.PDFApi();
let combinedSubmissionId = "com_000000000000000001"; // String | 
apiInstance.getCombinedSubmission(combinedSubmissionId, (error, data, response) => {
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
 **combinedSubmissionId** | **String**|  | 

### Return type

[**CombinedSubmission**](CombinedSubmission.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDataRequest

> SubmissionDataRequest getDataRequest(dataRequestId)

Look up a submission data request

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: api_token_basic
let api_token_basic = defaultClient.authentications['api_token_basic'];
api_token_basic.username = 'YOUR USERNAME';
api_token_basic.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.PDFApi();
let dataRequestId = "drq_000000000000000001"; // String | 
apiInstance.getDataRequest(dataRequestId, (error, data, response) => {
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
 **dataRequestId** | **String**|  | 

### Return type

[**SubmissionDataRequest**](SubmissionDataRequest.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFullTemplate

> FullTemplate getFullTemplate(templateId)

Fetch the full template attributes

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: api_token_basic
let api_token_basic = defaultClient.authentications['api_token_basic'];
api_token_basic.username = 'YOUR USERNAME';
api_token_basic.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.PDFApi();
let templateId = "tpl_000000000000000001"; // String | 
apiInstance.getFullTemplate(templateId, (error, data, response) => {
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
 **templateId** | **String**|  | 

### Return type

[**FullTemplate**](FullTemplate.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPresignUrl

> UploadPresign getPresignUrl()

Get a presigned URL so that you can upload a file to our AWS S3 bucket

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: api_token_basic
let api_token_basic = defaultClient.authentications['api_token_basic'];
api_token_basic.username = 'YOUR USERNAME';
api_token_basic.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.PDFApi();
apiInstance.getPresignUrl((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**UploadPresign**](UploadPresign.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSubmission

> Submission getSubmission(submissionId, opts)

Check the status of a PDF

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: api_token_basic
let api_token_basic = defaultClient.authentications['api_token_basic'];
api_token_basic.username = 'YOUR USERNAME';
api_token_basic.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.PDFApi();
let submissionId = "sub_000000000000000001"; // String | 
let opts = {
  'includeData': true // Boolean | 
};
apiInstance.getSubmission(submissionId, opts, (error, data, response) => {
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
 **submissionId** | **String**|  | 
 **includeData** | **Boolean**|  | [optional] 

### Return type

[**Submission**](Submission.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSubmissionBatch

> SubmissionBatch getSubmissionBatch(submissionBatchId, opts)

Check the status of a submission batch job

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: api_token_basic
let api_token_basic = defaultClient.authentications['api_token_basic'];
api_token_basic.username = 'YOUR USERNAME';
api_token_basic.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.PDFApi();
let submissionBatchId = "sbb_000000000000000001"; // String | 
let opts = {
  'includeSubmissions': true // Boolean | 
};
apiInstance.getSubmissionBatch(submissionBatchId, opts, (error, data, response) => {
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
 **submissionBatchId** | **String**|  | 
 **includeSubmissions** | **Boolean**|  | [optional] 

### Return type

[**SubmissionBatch**](SubmissionBatch.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTemplate

> Template getTemplate(templateId)

Check the status of an uploaded template

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: api_token_basic
let api_token_basic = defaultClient.authentications['api_token_basic'];
api_token_basic.username = 'YOUR USERNAME';
api_token_basic.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.PDFApi();
let templateId = "tpl_000000000000000001"; // String | 
apiInstance.getTemplate(templateId, (error, data, response) => {
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
 **templateId** | **String**|  | 

### Return type

[**Template**](Template.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTemplateSchema

> TemplateSchema getTemplateSchema(templateId)

Fetch the JSON schema for a template

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: api_token_basic
let api_token_basic = defaultClient.authentications['api_token_basic'];
api_token_basic.username = 'YOUR USERNAME';
api_token_basic.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.PDFApi();
let templateId = "tpl_000000000000000001"; // String | 
apiInstance.getTemplateSchema(templateId, (error, data, response) => {
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
 **templateId** | **String**|  | 

### Return type

[**TemplateSchema**](TemplateSchema.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listCombinedSubmissions

> [CombinedSubmission] listCombinedSubmissions(opts)

Get a list of all combined submissions

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: api_token_basic
let api_token_basic = defaultClient.authentications['api_token_basic'];
api_token_basic.username = 'YOUR USERNAME';
api_token_basic.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.PDFApi();
let opts = {
  'page': 2, // Number | Default: 1
  'perPage': 1 // Number | Default: 50
};
apiInstance.listCombinedSubmissions(opts, (error, data, response) => {
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
 **page** | **Number**| Default: 1 | [optional] 
 **perPage** | **Number**| Default: 50 | [optional] 

### Return type

[**[CombinedSubmission]**](CombinedSubmission.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listFolders

> [Folder] listFolders(opts)

Get a list of all folders

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: api_token_basic
let api_token_basic = defaultClient.authentications['api_token_basic'];
api_token_basic.username = 'YOUR USERNAME';
api_token_basic.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.PDFApi();
let opts = {
  'parentFolderId': "fld_000000000000000002" // String | Filter By Folder Id
};
apiInstance.listFolders(opts, (error, data, response) => {
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
 **parentFolderId** | **String**| Filter By Folder Id | [optional] 

### Return type

[**[Folder]**](Folder.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSubmissions

> ListSubmissionsResponse listSubmissions(opts)

List all submissions

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: api_token_basic
let api_token_basic = defaultClient.authentications['api_token_basic'];
api_token_basic.username = 'YOUR USERNAME';
api_token_basic.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.PDFApi();
let opts = {
  'cursor': "sub_list_000012", // String | 
  'limit': 3, // Number | 
  'createdAfter': "2019-01-01T09:00:00-05:00", // String | 
  'createdBefore': "2020-01-01T09:00:00-05:00", // String | 
  'type': "test", // String | 
  'includeData': true // Boolean | 
};
apiInstance.listSubmissions(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] 
 **createdAfter** | **String**|  | [optional] 
 **createdBefore** | **String**|  | [optional] 
 **type** | **String**|  | [optional] 
 **includeData** | **Boolean**|  | [optional] 

### Return type

[**ListSubmissionsResponse**](ListSubmissionsResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTemplates

> [Template] listTemplates(opts)

Get a list of all templates

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: api_token_basic
let api_token_basic = defaultClient.authentications['api_token_basic'];
api_token_basic.username = 'YOUR USERNAME';
api_token_basic.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.PDFApi();
let opts = {
  'query': "2", // String | Search By Name
  'parentFolderId': "fld_000000000000000001", // String | Filter By Folder Id
  'page': 2, // Number | Default: 1
  'perPage': 1 // Number | Default: 50
};
apiInstance.listTemplates(opts, (error, data, response) => {
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
 **query** | **String**| Search By Name | [optional] 
 **parentFolderId** | **String**| Filter By Folder Id | [optional] 
 **page** | **Number**| Default: 1 | [optional] 
 **perPage** | **Number**| Default: 50 | [optional] 

### Return type

[**[Template]**](Template.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## moveFolderToFolder

> Folder moveFolderToFolder(folderId, moveFolderData)

Move a folder

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: api_token_basic
let api_token_basic = defaultClient.authentications['api_token_basic'];
api_token_basic.username = 'YOUR USERNAME';
api_token_basic.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.PDFApi();
let folderId = "fld_000000000000000001"; // String | 
let moveFolderData = new ApiV1.MoveFolderData(); // MoveFolderData | 
apiInstance.moveFolderToFolder(folderId, moveFolderData, (error, data, response) => {
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
 **folderId** | **String**|  | 
 **moveFolderData** | [**MoveFolderData**](MoveFolderData.md)|  | 

### Return type

[**Folder**](Folder.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## moveTemplateToFolder

> Template moveTemplateToFolder(templateId, moveTemplateData)

Move Template to folder

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: api_token_basic
let api_token_basic = defaultClient.authentications['api_token_basic'];
api_token_basic.username = 'YOUR USERNAME';
api_token_basic.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.PDFApi();
let templateId = "tpl_000000000000000001"; // String | 
let moveTemplateData = new ApiV1.MoveTemplateData(); // MoveTemplateData | 
apiInstance.moveTemplateToFolder(templateId, moveTemplateData, (error, data, response) => {
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
 **templateId** | **String**|  | 
 **moveTemplateData** | [**MoveTemplateData**](MoveTemplateData.md)|  | 

### Return type

[**Template**](Template.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## renameFolder

> renameFolder(folderId, renameFolderData)

Rename a folder

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: api_token_basic
let api_token_basic = defaultClient.authentications['api_token_basic'];
api_token_basic.username = 'YOUR USERNAME';
api_token_basic.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.PDFApi();
let folderId = "fld_000000000000000001"; // String | 
let renameFolderData = new ApiV1.RenameFolderData(); // RenameFolderData | 
apiInstance.renameFolder(folderId, renameFolderData, (error, data, response) => {
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
 **folderId** | **String**|  | 
 **renameFolderData** | [**RenameFolderData**](RenameFolderData.md)|  | 

### Return type

null (empty response body)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## templatesTemplateIdSubmissionsGet

> ListSubmissionsResponse templatesTemplateIdSubmissionsGet(templateId, opts)

List all submissions for a given template

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: api_token_basic
let api_token_basic = defaultClient.authentications['api_token_basic'];
api_token_basic.username = 'YOUR USERNAME';
api_token_basic.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.PDFApi();
let templateId = "tpl_000000000000000002"; // String | 
let opts = {
  'cursor': "cursor_example", // String | 
  'limit': 3.4, // Number | 
  'createdAfter': "createdAfter_example", // String | 
  'createdBefore': "createdBefore_example", // String | 
  'type': "type_example", // String | 
  'includeData': true // Boolean | 
};
apiInstance.templatesTemplateIdSubmissionsGet(templateId, opts, (error, data, response) => {
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
 **templateId** | **String**|  | 
 **cursor** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] 
 **createdAfter** | **String**|  | [optional] 
 **createdBefore** | **String**|  | [optional] 
 **type** | **String**|  | [optional] 
 **includeData** | **Boolean**|  | [optional] 

### Return type

[**ListSubmissionsResponse**](ListSubmissionsResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## testAuthentication

> AuthenticationSuccessResponse testAuthentication()

Test Authentication

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: api_token_basic
let api_token_basic = defaultClient.authentications['api_token_basic'];
api_token_basic.username = 'YOUR USERNAME';
api_token_basic.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.PDFApi();
apiInstance.testAuthentication((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**AuthenticationSuccessResponse**](AuthenticationSuccessResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateDataRequest

> UpdateDataRequestResponse updateDataRequest(dataRequestId, updateSubmissionDataRequestData)

Update a submission data request

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: api_token_basic
let api_token_basic = defaultClient.authentications['api_token_basic'];
api_token_basic.username = 'YOUR USERNAME';
api_token_basic.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.PDFApi();
let dataRequestId = "drq_000000000000000001"; // String | 
let updateSubmissionDataRequestData = new ApiV1.UpdateSubmissionDataRequestData(); // UpdateSubmissionDataRequestData | 
apiInstance.updateDataRequest(dataRequestId, updateSubmissionDataRequestData, (error, data, response) => {
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
 **dataRequestId** | **String**|  | 
 **updateSubmissionDataRequestData** | [**UpdateSubmissionDataRequestData**](UpdateSubmissionDataRequestData.md)|  | 

### Return type

[**UpdateDataRequestResponse**](UpdateDataRequestResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateTemplate

> UpdateTemplateResponse updateTemplate(templateId, updateTemplateData)

Update a Template

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure HTTP basic authorization: api_token_basic
let api_token_basic = defaultClient.authentications['api_token_basic'];
api_token_basic.username = 'YOUR USERNAME';
api_token_basic.password = 'YOUR PASSWORD';

let apiInstance = new ApiV1.PDFApi();
let templateId = "tpl_000000000000000003"; // String | 
let updateTemplateData = new ApiV1.UpdateTemplateData(); // UpdateTemplateData | 
apiInstance.updateTemplate(templateId, updateTemplateData, (error, data, response) => {
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
 **templateId** | **String**|  | 
 **updateTemplateData** | [**UpdateTemplateData**](UpdateTemplateData.md)|  | 

### Return type

[**UpdateTemplateResponse**](UpdateTemplateResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

