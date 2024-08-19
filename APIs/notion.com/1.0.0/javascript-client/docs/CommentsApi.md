# NotionApi.CommentsApi

All URIs are relative to *https://api.notion.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieveComments**](CommentsApi.md#retrieveComments) | **GET** /v1/comments | Retrieve comments



## retrieveComments

> RetrieveComments200Response retrieveComments(opts)

Retrieve comments

Retrieve a user object using the ID specified in the request path.

### Example

```javascript
import NotionApi from 'notion_api';

let apiInstance = new NotionApi.CommentsApi();
let opts = {
  'blockId': "{{BLOCK_ID}}", // String | 
  'pageSize': "100", // String | 
  'notionVersion': "{{NOTION_VERSION}}" // String | 
};
apiInstance.retrieveComments(opts, (error, data, response) => {
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
 **blockId** | **String**|  | [optional] 
 **pageSize** | **String**|  | [optional] 
 **notionVersion** | **String**|  | [optional] 

### Return type

[**RetrieveComments200Response**](RetrieveComments200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

