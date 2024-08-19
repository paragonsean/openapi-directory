# NotionApi.UsersApi

All URIs are relative to *https://api.notion.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieveAUser**](UsersApi.md#retrieveAUser) | **GET** /v1/users/{id} | Retrieve a user



## retrieveAUser

> RetrieveAUser200Response retrieveAUser(id, opts)

Retrieve a user

Retrieve a user object using the ID specified in the request path.

### Example

```javascript
import NotionApi from 'notion_api';

let apiInstance = new NotionApi.UsersApi();
let id = "{{USER_ID}}"; // String | 
let opts = {
  'notionVersion': "{{NOTION_VERSION}}" // String | 
};
apiInstance.retrieveAUser(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **notionVersion** | **String**|  | [optional] 

### Return type

[**RetrieveAUser200Response**](RetrieveAUser200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

