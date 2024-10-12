# TheNounProject.UserApi

All URIs are relative to *http://api.thenounproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getUserCollection**](UserApi.md#getUserCollection) | **GET** /user/{user_id}/collections/{slug} | Get user collection
[**getUserCollections**](UserApi.md#getUserCollections) | **GET** /user/{user_id}/collections | Get user collections
[**getUserUploadsWithUser**](UserApi.md#getUserUploadsWithUser) | **GET** /user/{username}/uploads | Get user uploads with user



## getUserCollection

> getUserCollection(userId, slug)

Get user collection

Returns a single collection associated with a user

### Example

```javascript
import TheNounProject from 'the_noun_project';

let apiInstance = new TheNounProject.UserApi();
let userId = 56; // Number | User id
let slug = "slug_example"; // String | Collection slug
apiInstance.getUserCollection(userId, slug, (error, data, response) => {
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
 **userId** | **Number**| User id | 
 **slug** | **String**| Collection slug | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getUserCollections

> getUserCollections(userId)

Get user collections

Returns a list of collections associated with a user

### Example

```javascript
import TheNounProject from 'the_noun_project';

let apiInstance = new TheNounProject.UserApi();
let userId = 56; // Number | User id
apiInstance.getUserCollections(userId, (error, data, response) => {
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
 **userId** | **Number**| User id | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getUserUploadsWithUser

> getUserUploadsWithUser(username, opts)

Get user uploads with user

Returns a list of uploads associated with a user

### Example

```javascript
import TheNounProject from 'the_noun_project';

let apiInstance = new TheNounProject.UserApi();
let username = "username_example"; // String | Username
let opts = {
  'limit': 56, // Number | Maximum number of results
  'offset': 56, // Number | Number of results to displace or skip over
  'page': 56 // Number | Number of results of limit length to displace or skip over
};
apiInstance.getUserUploadsWithUser(username, opts, (error, data, response) => {
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
 **username** | **String**| Username | 
 **limit** | **Number**| Maximum number of results | [optional] 
 **offset** | **Number**| Number of results to displace or skip over | [optional] 
 **page** | **Number**| Number of results of limit length to displace or skip over | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

