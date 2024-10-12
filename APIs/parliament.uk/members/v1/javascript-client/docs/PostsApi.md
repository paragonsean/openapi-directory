# MembersApi.PostsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiPostsDepartmentsTypeGet**](PostsApi.md#apiPostsDepartmentsTypeGet) | **GET** /api/Posts/Departments/{type} | Returns a list of departments.
[**apiPostsGovernmentPostsGet**](PostsApi.md#apiPostsGovernmentPostsGet) | **GET** /api/Posts/GovernmentPosts | Returns a list of government posts.
[**apiPostsOppositionPostsGet**](PostsApi.md#apiPostsOppositionPostsGet) | **GET** /api/Posts/OppositionPosts | Returns a list of opposition posts.
[**apiPostsSpeakerAndDeputiesForDateGet**](PostsApi.md#apiPostsSpeakerAndDeputiesForDateGet) | **GET** /api/Posts/SpeakerAndDeputies/{forDate} | Returns a list containing the speaker and deputy speakers.
[**apiPostsSpokespersonsGet**](PostsApi.md#apiPostsSpokespersonsGet) | **GET** /api/Posts/Spokespersons | Returns a list of spokespersons.



## apiPostsDepartmentsTypeGet

> [GovernmentDepartment] apiPostsDepartmentsTypeGet(type)

Returns a list of departments.

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.PostsApi();
let type = new MembersApi.PostType(); // PostType | Departments by type
apiInstance.apiPostsDepartmentsTypeGet(type, (error, data, response) => {
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
 **type** | [**PostType**](.md)| Departments by type | 

### Return type

[**[GovernmentDepartment]**](GovernmentDepartment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiPostsGovernmentPostsGet

> [GovernmentOppositionPostItem] apiPostsGovernmentPostsGet(opts)

Returns a list of government posts.

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.PostsApi();
let opts = {
  'departmentId': 56 // Number | Government posts by department ID
};
apiInstance.apiPostsGovernmentPostsGet(opts, (error, data, response) => {
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
 **departmentId** | **Number**| Government posts by department ID | [optional] 

### Return type

[**[GovernmentOppositionPostItem]**](GovernmentOppositionPostItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiPostsOppositionPostsGet

> [GovernmentOppositionPostItem] apiPostsOppositionPostsGet(opts)

Returns a list of opposition posts.

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.PostsApi();
let opts = {
  'departmentId': 56 // Number | Opposition posts by department ID
};
apiInstance.apiPostsOppositionPostsGet(opts, (error, data, response) => {
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
 **departmentId** | **Number**| Opposition posts by department ID | [optional] 

### Return type

[**[GovernmentOppositionPostItem]**](GovernmentOppositionPostItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiPostsSpeakerAndDeputiesForDateGet

> [MemberItem] apiPostsSpeakerAndDeputiesForDateGet(forDate)

Returns a list containing the speaker and deputy speakers.

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.PostsApi();
let forDate = new Date("2013-10-20T19:20:30+01:00"); // Date | Speaker and deputy speakers for date specified
apiInstance.apiPostsSpeakerAndDeputiesForDateGet(forDate, (error, data, response) => {
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
 **forDate** | **Date**| Speaker and deputy speakers for date specified | 

### Return type

[**[MemberItem]**](MemberItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiPostsSpokespersonsGet

> [GovernmentOppositionPostItem] apiPostsSpokespersonsGet(opts)

Returns a list of spokespersons.

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.PostsApi();
let opts = {
  'partyId': 56 // Number | Spokespersons by party ID
};
apiInstance.apiPostsSpokespersonsGet(opts, (error, data, response) => {
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
 **partyId** | **Number**| Spokespersons by party ID | [optional] 

### Return type

[**[GovernmentOppositionPostItem]**](GovernmentOppositionPostItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

