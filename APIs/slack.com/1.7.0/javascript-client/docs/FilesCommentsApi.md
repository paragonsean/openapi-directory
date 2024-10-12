# SlackWebApi.FilesCommentsApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filesCommentsDelete**](FilesCommentsApi.md#filesCommentsDelete) | **POST** /files.comments.delete | 



## filesCommentsDelete

> FilesCommentsDeleteSchema filesCommentsDelete(opts)



Deletes an existing comment on a file.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.FilesCommentsApi();
let opts = {
  'token': "token_example", // String | Authentication token. Requires scope: `files:write:user`
  'file': "file_example", // String | File to delete a comment from.
  'id': "id_example" // String | The comment to delete.
};
apiInstance.filesCommentsDelete(opts, (error, data, response) => {
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

