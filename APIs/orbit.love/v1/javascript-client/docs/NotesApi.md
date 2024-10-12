# OrbitApi.NotesApi

All URIs are relative to *https://app.orbit.love/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workspaceSlugMembersMemberSlugNotesGet**](NotesApi.md#workspaceSlugMembersMemberSlugNotesGet) | **GET** /{workspace_slug}/members/{member_slug}/notes | Get the member&#39;s notes
[**workspaceSlugMembersMemberSlugNotesIdPut**](NotesApi.md#workspaceSlugMembersMemberSlugNotesIdPut) | **PUT** /{workspace_slug}/members/{member_slug}/notes/{id} | Update a note
[**workspaceSlugMembersMemberSlugNotesPost**](NotesApi.md#workspaceSlugMembersMemberSlugNotesPost) | **POST** /{workspace_slug}/members/{member_slug}/notes | Create a note



## workspaceSlugMembersMemberSlugNotesGet

> workspaceSlugMembersMemberSlugNotesGet(workspaceSlug, memberSlug, opts)

Get the member&#39;s notes

### Example

```javascript
import OrbitApi from 'orbit_api';
let defaultClient = OrbitApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new OrbitApi.NotesApi();
let workspaceSlug = "workspaceSlug_example"; // String | 
let memberSlug = "memberSlug_example"; // String | 
let opts = {
  'page': "page_example" // String | 
};
apiInstance.workspaceSlugMembersMemberSlugNotesGet(workspaceSlug, memberSlug, opts, (error, data, response) => {
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
 **workspaceSlug** | **String**|  | 
 **memberSlug** | **String**|  | 
 **page** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspaceSlugMembersMemberSlugNotesIdPut

> workspaceSlugMembersMemberSlugNotesIdPut(workspaceSlug, memberSlug, id, opts)

Update a note

### Example

```javascript
import OrbitApi from 'orbit_api';
let defaultClient = OrbitApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new OrbitApi.NotesApi();
let workspaceSlug = "workspaceSlug_example"; // String | 
let memberSlug = "memberSlug_example"; // String | 
let id = "id_example"; // String | 
let opts = {
  'note': new OrbitApi.Note() // Note | 
};
apiInstance.workspaceSlugMembersMemberSlugNotesIdPut(workspaceSlug, memberSlug, id, opts, (error, data, response) => {
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
 **workspaceSlug** | **String**|  | 
 **memberSlug** | **String**|  | 
 **id** | **String**|  | 
 **note** | [**Note**](Note.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## workspaceSlugMembersMemberSlugNotesPost

> workspaceSlugMembersMemberSlugNotesPost(workspaceSlug, memberSlug, opts)

Create a note

### Example

```javascript
import OrbitApi from 'orbit_api';
let defaultClient = OrbitApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new OrbitApi.NotesApi();
let workspaceSlug = "workspaceSlug_example"; // String | 
let memberSlug = "memberSlug_example"; // String | 
let opts = {
  'note': new OrbitApi.Note() // Note | 
};
apiInstance.workspaceSlugMembersMemberSlugNotesPost(workspaceSlug, memberSlug, opts, (error, data, response) => {
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
 **workspaceSlug** | **String**|  | 
 **memberSlug** | **String**|  | 
 **note** | [**Note**](Note.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

