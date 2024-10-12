# SlackWebApi.FilesRemoteApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filesRemoteAdd**](FilesRemoteApi.md#filesRemoteAdd) | **POST** /files.remote.add | 
[**filesRemoteInfo**](FilesRemoteApi.md#filesRemoteInfo) | **GET** /files.remote.info | 
[**filesRemoteList**](FilesRemoteApi.md#filesRemoteList) | **GET** /files.remote.list | 
[**filesRemoteRemove**](FilesRemoteApi.md#filesRemoteRemove) | **POST** /files.remote.remove | 
[**filesRemoteShare**](FilesRemoteApi.md#filesRemoteShare) | **GET** /files.remote.share | 
[**filesRemoteUpdate**](FilesRemoteApi.md#filesRemoteUpdate) | **POST** /files.remote.update | 



## filesRemoteAdd

> DefaultSuccessTemplate filesRemoteAdd(opts)



Adds a file from a remote service

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.FilesRemoteApi();
let opts = {
  'externalId': "externalId_example", // String | Creator defined GUID for the file.
  'externalUrl': "externalUrl_example", // String | URL of the remote file.
  'filetype': "filetype_example", // String | type of file
  'indexableFileContents': "indexableFileContents_example", // String | A text file (txt, pdf, doc, etc.) containing textual search terms that are used to improve discovery of the remote file.
  'previewImage': "previewImage_example", // String | Preview of the document via `multipart/form-data`.
  'title': "title_example", // String | Title of the file being shared.
  'token': "token_example" // String | Authentication token. Requires scope: `remote_files:write`
};
apiInstance.filesRemoteAdd(opts, (error, data, response) => {
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
 **externalId** | **String**| Creator defined GUID for the file. | [optional] 
 **externalUrl** | **String**| URL of the remote file. | [optional] 
 **filetype** | **String**| type of file | [optional] 
 **indexableFileContents** | **String**| A text file (txt, pdf, doc, etc.) containing textual search terms that are used to improve discovery of the remote file. | [optional] 
 **previewImage** | **String**| Preview of the document via &#x60;multipart/form-data&#x60;. | [optional] 
 **title** | **String**| Title of the file being shared. | [optional] 
 **token** | **String**| Authentication token. Requires scope: &#x60;remote_files:write&#x60; | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## filesRemoteInfo

> DefaultSuccessTemplate filesRemoteInfo(opts)



Retrieve information about a remote file added to Slack

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.FilesRemoteApi();
let opts = {
  'token': "token_example", // String | Authentication token. Requires scope: `remote_files:read`
  'file': "file_example", // String | Specify a file by providing its ID.
  'externalId': "externalId_example" // String | Creator defined GUID for the file.
};
apiInstance.filesRemoteInfo(opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;remote_files:read&#x60; | [optional] 
 **file** | **String**| Specify a file by providing its ID. | [optional] 
 **externalId** | **String**| Creator defined GUID for the file. | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## filesRemoteList

> DefaultSuccessTemplate filesRemoteList(opts)



Retrieve information about a remote file added to Slack

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.FilesRemoteApi();
let opts = {
  'token': "token_example", // String | Authentication token. Requires scope: `remote_files:read`
  'channel': "channel_example", // String | Filter files appearing in a specific channel, indicated by its ID.
  'tsFrom': 3.4, // Number | Filter files created after this timestamp (inclusive).
  'tsTo': 3.4, // Number | Filter files created before this timestamp (inclusive).
  'limit': 56, // Number | The maximum number of items to return.
  'cursor': "cursor_example" // String | Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. Default value fetches the first \"page\" of the collection. See [pagination](/docs/pagination) for more detail.
};
apiInstance.filesRemoteList(opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;remote_files:read&#x60; | [optional] 
 **channel** | **String**| Filter files appearing in a specific channel, indicated by its ID. | [optional] 
 **tsFrom** | **Number**| Filter files created after this timestamp (inclusive). | [optional] 
 **tsTo** | **Number**| Filter files created before this timestamp (inclusive). | [optional] 
 **limit** | **Number**| The maximum number of items to return. | [optional] 
 **cursor** | **String**| Paginate through collections of data by setting the &#x60;cursor&#x60; parameter to a &#x60;next_cursor&#x60; attribute returned by a previous request&#39;s &#x60;response_metadata&#x60;. Default value fetches the first \&quot;page\&quot; of the collection. See [pagination](/docs/pagination) for more detail. | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## filesRemoteRemove

> DefaultSuccessTemplate filesRemoteRemove(opts)



Remove a remote file.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.FilesRemoteApi();
let opts = {
  'externalId': "externalId_example", // String | Creator defined GUID for the file.
  'file': "file_example", // String | Specify a file by providing its ID.
  'token': "token_example" // String | Authentication token. Requires scope: `remote_files:write`
};
apiInstance.filesRemoteRemove(opts, (error, data, response) => {
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
 **externalId** | **String**| Creator defined GUID for the file. | [optional] 
 **file** | **String**| Specify a file by providing its ID. | [optional] 
 **token** | **String**| Authentication token. Requires scope: &#x60;remote_files:write&#x60; | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## filesRemoteShare

> DefaultSuccessTemplate filesRemoteShare(opts)



Share a remote file into a channel.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.FilesRemoteApi();
let opts = {
  'token': "token_example", // String | Authentication token. Requires scope: `remote_files:share`
  'file': "file_example", // String | Specify a file registered with Slack by providing its ID. Either this field or `external_id` or both are required.
  'externalId': "externalId_example", // String | The globally unique identifier (GUID) for the file, as set by the app registering the file with Slack.  Either this field or `file` or both are required.
  'channels': "channels_example" // String | Comma-separated list of channel IDs where the file will be shared.
};
apiInstance.filesRemoteShare(opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;remote_files:share&#x60; | [optional] 
 **file** | **String**| Specify a file registered with Slack by providing its ID. Either this field or &#x60;external_id&#x60; or both are required. | [optional] 
 **externalId** | **String**| The globally unique identifier (GUID) for the file, as set by the app registering the file with Slack.  Either this field or &#x60;file&#x60; or both are required. | [optional] 
 **channels** | **String**| Comma-separated list of channel IDs where the file will be shared. | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## filesRemoteUpdate

> DefaultSuccessTemplate filesRemoteUpdate(opts)



Updates an existing remote file.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.FilesRemoteApi();
let opts = {
  'externalId': "externalId_example", // String | Creator defined GUID for the file.
  'externalUrl': "externalUrl_example", // String | URL of the remote file.
  'file': "file_example", // String | Specify a file by providing its ID.
  'filetype': "filetype_example", // String | type of file
  'indexableFileContents': "indexableFileContents_example", // String | File containing contents that can be used to improve searchability for the remote file.
  'previewImage': "previewImage_example", // String | Preview of the document via `multipart/form-data`.
  'title': "title_example", // String | Title of the file being shared.
  'token': "token_example" // String | Authentication token. Requires scope: `remote_files:write`
};
apiInstance.filesRemoteUpdate(opts, (error, data, response) => {
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
 **externalId** | **String**| Creator defined GUID for the file. | [optional] 
 **externalUrl** | **String**| URL of the remote file. | [optional] 
 **file** | **String**| Specify a file by providing its ID. | [optional] 
 **filetype** | **String**| type of file | [optional] 
 **indexableFileContents** | **String**| File containing contents that can be used to improve searchability for the remote file. | [optional] 
 **previewImage** | **String**| Preview of the document via &#x60;multipart/form-data&#x60;. | [optional] 
 **title** | **String**| Title of the file being shared. | [optional] 
 **token** | **String**| Authentication token. Requires scope: &#x60;remote_files:write&#x60; | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

