# ContentDepot.MetaPubApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV2MetapubProgramInformationBatchBatchIdGet**](MetaPubApi.md#apiV2MetapubProgramInformationBatchBatchIdGet) | **GET** /api/v2/metapub/program-information/batch/{batch-id} | Get an EPG batch operation.
[**apiV2MetapubProgramInformationBatchPost**](MetaPubApi.md#apiV2MetapubProgramInformationBatchPost) | **POST** /api/v2/metapub/program-information/batch | Create a batch operation on EPG information.



## apiV2MetapubProgramInformationBatchBatchIdGet

> ProgramInformationBatch apiV2MetapubProgramInformationBatchBatchIdGet(batchId)

Get an EPG batch operation.

Gets the batch information which can be used to check the status of the operation or retrieve more details if the batch fails.

### Example

```javascript
import ContentDepot from 'content_depot';
let defaultClient = ContentDepot.ApiClient.instance;
// Configure OAuth2 access token for authorization: cd_oauth2
let cd_oauth2 = defaultClient.authentications['cd_oauth2'];
cd_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContentDepot.MetaPubApi();
let batchId = 789; // Number | 
apiInstance.apiV2MetapubProgramInformationBatchBatchIdGet(batchId, (error, data, response) => {
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
 **batchId** | **Number**|  | 

### Return type

[**ProgramInformationBatch**](ProgramInformationBatch.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV2MetapubProgramInformationBatchPost

> ProgramInformationBatch apiV2MetapubProgramInformationBatchPost(opts)

Create a batch operation on EPG information.

Create a batch to process the metadata of one or more electronic program guide (EPG) programs using metadata that has been uploaded to the customer&#39;s CD Drive. If multiple EPG programs are present in the metadata, they will all be updated, however updates across programs are not atomic. Note that an EPG program maps to the ContentDepot concept of an episode which is also known as a \&quot;program instance\&quot;.  A batch operation must be explicitly created rather than the server attempting to detect new metadata in order to allow for all the content to be uploaded including any supporting content like images. A batch operation is accepted and queued for asynchronous processing at a later time. A client can poll the batch periodically to determine when it completes and the resulting state. 

### Example

```javascript
import ContentDepot from 'content_depot';
let defaultClient = ContentDepot.ApiClient.instance;
// Configure OAuth2 access token for authorization: cd_oauth2
let cd_oauth2 = defaultClient.authentications['cd_oauth2'];
cd_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContentDepot.MetaPubApi();
let opts = {
  'apiV2MetapubProgramInformationBatchPostRequest': new ContentDepot.ApiV2MetapubProgramInformationBatchPostRequest() // ApiV2MetapubProgramInformationBatchPostRequest | 
};
apiInstance.apiV2MetapubProgramInformationBatchPost(opts, (error, data, response) => {
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
 **apiV2MetapubProgramInformationBatchPostRequest** | [**ApiV2MetapubProgramInformationBatchPostRequest**](ApiV2MetapubProgramInformationBatchPostRequest.md)|  | [optional] 

### Return type

[**ProgramInformationBatch**](ProgramInformationBatch.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

