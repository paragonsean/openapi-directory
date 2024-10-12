# SlackWebApi.FilesApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filesCommentsDelete_0**](FilesApi.md#filesCommentsDelete_0) | **POST** /files.comments.delete | 
[**filesDelete**](FilesApi.md#filesDelete) | **POST** /files.delete | 
[**filesInfo**](FilesApi.md#filesInfo) | **GET** /files.info | 
[**filesList**](FilesApi.md#filesList) | **GET** /files.list | 
[**filesRemoteAdd_0**](FilesApi.md#filesRemoteAdd_0) | **POST** /files.remote.add | 
[**filesRemoteInfo_0**](FilesApi.md#filesRemoteInfo_0) | **GET** /files.remote.info | 
[**filesRemoteList_0**](FilesApi.md#filesRemoteList_0) | **GET** /files.remote.list | 
[**filesRemoteRemove_0**](FilesApi.md#filesRemoteRemove_0) | **POST** /files.remote.remove | 
[**filesRemoteShare_0**](FilesApi.md#filesRemoteShare_0) | **GET** /files.remote.share | 
[**filesRemoteUpdate_0**](FilesApi.md#filesRemoteUpdate_0) | **POST** /files.remote.update | 
[**filesRevokePublicURL**](FilesApi.md#filesRevokePublicURL) | **POST** /files.revokePublicURL | 
[**filesSharedPublicURL**](FilesApi.md#filesSharedPublicURL) | **POST** /files.sharedPublicURL | 
[**filesUpload**](FilesApi.md#filesUpload) | **POST** /files.upload | 



## filesCommentsDelete_0

> FilesCommentsDeleteSchema filesCommentsDelete_0(opts)



Deletes an existing comment on a file.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.FilesApi();
let opts = {
  'token': "token_example", // String | Authentication token. Requires scope: `files:write:user`
  'file': "file_example", // String | File to delete a comment from.
  'id': "id_example" // String | The comment to delete.
};
apiInstance.filesCommentsDelete_0(opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;files:write:user&#x60; | [optional] 
 **file** | **String**| File to delete a comment from. | [optional] 
 **id** | **String**| The comment to delete. | [optional] 

### Return type

[**FilesCommentsDeleteSchema**](FilesCommentsDeleteSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## filesDelete

> FilesDeleteSchema filesDelete(opts)



Deletes a file.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.FilesApi();
let opts = {
  'token': "token_example", // String | Authentication token. Requires scope: `files:write:user`
  'file': "file_example" // String | ID of file to delete.
};
apiInstance.filesDelete(opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;files:write:user&#x60; | [optional] 
 **file** | **String**| ID of file to delete. | [optional] 

### Return type

[**FilesDeleteSchema**](FilesDeleteSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## filesInfo

> FilesInfoSchema filesInfo(opts)



Gets information about a file.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.FilesApi();
let opts = {
  'token': "token_example", // String | Authentication token. Requires scope: `files:read`
  'file': "file_example", // String | Specify a file by providing its ID.
  'count': "count_example", // String | 
  'page': "page_example", // String | 
  'limit': 56, // Number | The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn't been reached.
  'cursor': "cursor_example" // String | Parameter for pagination. File comments are paginated for a single file. Set `cursor` equal to the `next_cursor` attribute returned by the previous request's `response_metadata`. This parameter is optional, but pagination is mandatory: the default value simply fetches the first \"page\" of the collection of comments. See [pagination](/docs/pagination) for more details.
};
apiInstance.filesInfo(opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;files:read&#x60; | [optional] 
 **file** | **String**| Specify a file by providing its ID. | [optional] 
 **count** | **String**|  | [optional] 
 **page** | **String**|  | [optional] 
 **limit** | **Number**| The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn&#39;t been reached. | [optional] 
 **cursor** | **String**| Parameter for pagination. File comments are paginated for a single file. Set &#x60;cursor&#x60; equal to the &#x60;next_cursor&#x60; attribute returned by the previous request&#39;s &#x60;response_metadata&#x60;. This parameter is optional, but pagination is mandatory: the default value simply fetches the first \&quot;page\&quot; of the collection of comments. See [pagination](/docs/pagination) for more details. | [optional] 

### Return type

[**FilesInfoSchema**](FilesInfoSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## filesList

> FilesListSchema filesList(opts)



List for a team, in a channel, or from a user with applied filters.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.FilesApi();
let opts = {
  'token': "token_example", // String | Authentication token. Requires scope: `files:read`
  'user': "user_example", // String | Filter files created by a single user.
  'channel': "channel_example", // String | Filter files appearing in a specific channel, indicated by its ID.
  'tsFrom': 3.4, // Number | Filter files created after this timestamp (inclusive).
  'tsTo': 3.4, // Number | Filter files created before this timestamp (inclusive).
  'types': "types_example", // String | Filter files by type ([see below](#file_types)). You can pass multiple values in the types argument, like `types=spaces,snippets`.The default value is `all`, which does not filter the list.
  'count': "count_example", // String | 
  'page': "page_example", // String | 
  'showFilesHiddenByLimit': true // Boolean | Show truncated file info for files hidden due to being too old, and the team who owns the file being over the file limit.
};
apiInstance.filesList(opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;files:read&#x60; | [optional] 
 **user** | **String**| Filter files created by a single user. | [optional] 
 **channel** | **String**| Filter files appearing in a specific channel, indicated by its ID. | [optional] 
 **tsFrom** | **Number**| Filter files created after this timestamp (inclusive). | [optional] 
 **tsTo** | **Number**| Filter files created before this timestamp (inclusive). | [optional] 
 **types** | **String**| Filter files by type ([see below](#file_types)). You can pass multiple values in the types argument, like &#x60;types&#x3D;spaces,snippets&#x60;.The default value is &#x60;all&#x60;, which does not filter the list. | [optional] 
 **count** | **String**|  | [optional] 
 **page** | **String**|  | [optional] 
 **showFilesHiddenByLimit** | **Boolean**| Show truncated file info for files hidden due to being too old, and the team who owns the file being over the file limit. | [optional] 

### Return type

[**FilesListSchema**](FilesListSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## filesRemoteAdd_0

> DefaultSuccessTemplate filesRemoteAdd_0(opts)



Adds a file from a remote service

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.FilesApi();
let opts = {
  'externalId': "externalId_example", // String | Creator defined GUID for the file.
  'externalUrl': "externalUrl_example", // String | URL of the remote file.
  'filetype': "filetype_example", // String | type of file
  'indexableFileContents': "indexableFileContents_example", // String | A text file (txt, pdf, doc, etc.) containing textual search terms that are used to improve discovery of the remote file.
  'previewImage': "previewImage_example", // String | Preview of the document via `multipart/form-data`.
  'title': "title_example", // String | Title of the file being shared.
  'token': "token_example" // String | Authentication token. Requires scope: `remote_files:write`
};
apiInstance.filesRemoteAdd_0(opts, (error, data, response) => {
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


## filesRemoteInfo_0

> DefaultSuccessTemplate filesRemoteInfo_0(opts)



Retrieve information about a remote file added to Slack

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.FilesApi();
let opts = {
  'token': "token_example", // String | Authentication token. Requires scope: `remote_files:read`
  'file': "file_example", // String | Specify a file by providing its ID.
  'externalId': "externalId_example" // String | Creator defined GUID for the file.
};
apiInstance.filesRemoteInfo_0(opts, (error, data, response) => {
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


## filesRemoteList_0

> DefaultSuccessTemplate filesRemoteList_0(opts)



Retrieve information about a remote file added to Slack

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.FilesApi();
let opts = {
  'token': "token_example", // String | Authentication token. Requires scope: `remote_files:read`
  'channel': "channel_example", // String | Filter files appearing in a specific channel, indicated by its ID.
  'tsFrom': 3.4, // Number | Filter files created after this timestamp (inclusive).
  'tsTo': 3.4, // Number | Filter files created before this timestamp (inclusive).
  'limit': 56, // Number | The maximum number of items to return.
  'cursor': "cursor_example" // String | Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. Default value fetches the first \"page\" of the collection. See [pagination](/docs/pagination) for more detail.
};
apiInstance.filesRemoteList_0(opts, (error, data, response) => {
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


## filesRemoteRemove_0

> DefaultSuccessTemplate filesRemoteRemove_0(opts)



Remove a remote file.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.FilesApi();
let opts = {
  'externalId': "externalId_example", // String | Creator defined GUID for the file.
  'file': "file_example", // String | Specify a file by providing its ID.
  'token': "token_example" // String | Authentication token. Requires scope: `remote_files:write`
};
apiInstance.filesRemoteRemove_0(opts, (error, data, response) => {
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


## filesRemoteShare_0

> DefaultSuccessTemplate filesRemoteShare_0(opts)



Share a remote file into a channel.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.FilesApi();
let opts = {
  'token': "token_example", // String | Authentication token. Requires scope: `remote_files:share`
  'file': "file_example", // String | Specify a file registered with Slack by providing its ID. Either this field or `external_id` or both are required.
  'externalId': "externalId_example", // String | The globally unique identifier (GUID) for the file, as set by the app registering the file with Slack.  Either this field or `file` or both are required.
  'channels': "channels_example" // String | Comma-separated list of channel IDs where the file will be shared.
};
apiInstance.filesRemoteShare_0(opts, (error, data, response) => {
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


## filesRemoteUpdate_0

> DefaultSuccessTemplate filesRemoteUpdate_0(opts)



Updates an existing remote file.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.FilesApi();
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
apiInstance.filesRemoteUpdate_0(opts, (error, data, response) => {
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


## filesRevokePublicURL

> FilesRevokePublicURLSchema filesRevokePublicURL(opts)



Revokes public/external sharing access for a file

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.FilesApi();
let opts = {
  'token': "token_example", // String | Authentication token. Requires scope: `files:write:user`
  'file': "file_example" // String | File to revoke
};
apiInstance.filesRevokePublicURL(opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;files:write:user&#x60; | [optional] 
 **file** | **String**| File to revoke | [optional] 

### Return type

[**FilesRevokePublicURLSchema**](FilesRevokePublicURLSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## filesSharedPublicURL

> FilesSharedPublicURLSchema filesSharedPublicURL(opts)



Enables a file for public/external sharing.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.FilesApi();
let opts = {
  'token': "token_example", // String | Authentication token. Requires scope: `files:write:user`
  'file': "file_example" // String | File to share
};
apiInstance.filesSharedPublicURL(opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;files:write:user&#x60; | [optional] 
 **file** | **String**| File to share | [optional] 

### Return type

[**FilesSharedPublicURLSchema**](FilesSharedPublicURLSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## filesUpload

> FilesUploadSchema filesUpload(opts)



Uploads or creates a file.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.FilesApi();
let opts = {
  'channels': "channels_example", // String | Comma-separated list of channel names or IDs where the file will be shared.
  'content': "content_example", // String | File contents via a POST variable. If omitting this parameter, you must provide a `file`.
  'file': "file_example", // String | File contents via `multipart/form-data`. If omitting this parameter, you must submit `content`.
  'filename': "filename_example", // String | Filename of file.
  'filetype': "filetype_example", // String | A [file type](/types/file#file_types) identifier.
  'initialComment': "initialComment_example", // String | The message text introducing the file in specified `channels`.
  'threadTs': 3.4, // Number | Provide another message's `ts` value to upload this file as a reply. Never use a reply's `ts` value; use its parent instead.
  'title': "title_example", // String | Title of file.
  'token': "token_example" // String | Authentication token. Requires scope: `files:write:user`
};
apiInstance.filesUpload(opts, (error, data, response) => {
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
 **channels** | **String**| Comma-separated list of channel names or IDs where the file will be shared. | [optional] 
 **content** | **String**| File contents via a POST variable. If omitting this parameter, you must provide a &#x60;file&#x60;. | [optional] 
 **file** | **String**| File contents via &#x60;multipart/form-data&#x60;. If omitting this parameter, you must submit &#x60;content&#x60;. | [optional] 
 **filename** | **String**| Filename of file. | [optional] 
 **filetype** | **String**| A [file type](/types/file#file_types) identifier. | [optional] 
 **initialComment** | **String**| The message text introducing the file in specified &#x60;channels&#x60;. | [optional] 
 **threadTs** | **Number**| Provide another message&#39;s &#x60;ts&#x60; value to upload this file as a reply. Never use a reply&#39;s &#x60;ts&#x60; value; use its parent instead. | [optional] 
 **title** | **String**| Title of file. | [optional] 
 **token** | **String**| Authentication token. Requires scope: &#x60;files:write:user&#x60; | [optional] 

### Return type

[**FilesUploadSchema**](FilesUploadSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

