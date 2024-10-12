# VestorlyApi.PostsApi

All URIs are relative to *https://staging.vestorly.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createPost**](PostsApi.md#createPost) | **POST** /posts | 
[**findPosts**](PostsApi.md#findPosts) | **GET** /posts | 
[**getPostByID**](PostsApi.md#getPostByID) | **GET** /posts/{id} | 
[**updatePostByID**](PostsApi.md#updatePostByID) | **PUT** /posts/{id} | 



## createPost

> Postresponse createPost(vestorlyAuth, post, opts)



Create a new post in the Vestorly Platform

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.PostsApi();
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let post = new VestorlyApi.PostInput(); // PostInput | Post you want to create
let opts = {
  'accessToken': "accessToken_example" // String | OAuth Token
};
apiInstance.createPost(vestorlyAuth, post, opts, (error, data, response) => {
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
 **vestorlyAuth** | **String**| Vestorly Auth Token | 
 **post** | [**PostInput**](PostInput.md)| Post you want to create | 
 **accessToken** | **String**| OAuth Token | [optional] 

### Return type

[**Postresponse**](Postresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## findPosts

> Posts findPosts(vestorlyAuth, opts)



Query all posts

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.PostsApi();
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let opts = {
  'accessToken': "accessToken_example", // String | OAuth Token
  'textQuery': "textQuery_example", // String | Filter post by parameters
  'externalUrl': "externalUrl_example", // String | Filter by External URL
  'isPublished': "isPublished_example" // String | Filter by is_published boolean
};
apiInstance.findPosts(vestorlyAuth, opts, (error, data, response) => {
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
 **vestorlyAuth** | **String**| Vestorly Auth Token | 
 **accessToken** | **String**| OAuth Token | [optional] 
 **textQuery** | **String**| Filter post by parameters | [optional] 
 **externalUrl** | **String**| Filter by External URL | [optional] 
 **isPublished** | **String**| Filter by is_published boolean | [optional] 

### Return type

[**Posts**](Posts.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getPostByID

> Postresponse getPostByID(vestorlyAuth, id, opts)



Query all posts

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.PostsApi();
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let id = "id_example"; // String | ID of post to fetch
let opts = {
  'accessToken': "accessToken_example" // String | OAuth Token
};
apiInstance.getPostByID(vestorlyAuth, id, opts, (error, data, response) => {
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
 **vestorlyAuth** | **String**| Vestorly Auth Token | 
 **id** | **String**| ID of post to fetch | 
 **accessToken** | **String**| OAuth Token | [optional] 

### Return type

[**Postresponse**](Postresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## updatePostByID

> Postresponse updatePostByID(vestorlyAuth, id, post, opts)



Update A Post

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.PostsApi();
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let id = "id_example"; // String | id of post to update
let post = new VestorlyApi.Post(); // Post | Post you want to update
let opts = {
  'accessToken': "accessToken_example" // String | OAuth Token
};
apiInstance.updatePostByID(vestorlyAuth, id, post, opts, (error, data, response) => {
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
 **vestorlyAuth** | **String**| Vestorly Auth Token | 
 **id** | **String**| id of post to update | 
 **post** | [**Post**](Post.md)| Post you want to update | 
 **accessToken** | **String**| OAuth Token | [optional] 

### Return type

[**Postresponse**](Postresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

