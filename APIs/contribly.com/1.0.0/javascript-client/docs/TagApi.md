# Contribly.TagApi

All URIs are relative to *https://api.contribly.com/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tagsGet**](TagApi.md#tagsGet) | **GET** /tags | List tags
[**tagsIdGet**](TagApi.md#tagsIdGet) | **GET** /tags/{id} | Retrieve a single tag by id
[**tagsPost**](TagApi.md#tagsPost) | **POST** /tags | Create a new tag
[**tagsetsGet**](TagApi.md#tagsetsGet) | **GET** /tagsets | List tag sets
[**tagsetsIdGet**](TagApi.md#tagsetsIdGet) | **GET** /tagsets/{id} | Retrieve a single tag set by id
[**tagsetsPost**](TagApi.md#tagsetsPost) | **POST** /tagsets | Create a new tag set



## tagsGet

> [Tag] tagsGet(opts)

List tags

Retrieve tags.

### Example

```javascript
import Contribly from 'contribly';

let apiInstance = new Contribly.TagApi();
let opts = {
  'ownedBy': "ownedBy_example", // String | Restrict results to those owned by this user.
  'tagSet': "tagSet_example", // String | Restrict results to tags belonging to this tag set.
  'urlWords': "urlWords_example" // String | Restrict results by urlWords. Should be used with ownedBy when searching for one of your own tags.
};
apiInstance.tagsGet(opts, (error, data, response) => {
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
 **ownedBy** | **String**| Restrict results to those owned by this user. | [optional] 
 **tagSet** | **String**| Restrict results to tags belonging to this tag set. | [optional] 
 **urlWords** | **String**| Restrict results by urlWords. Should be used with ownedBy when searching for one of your own tags. | [optional] 

### Return type

[**[Tag]**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tagsIdGet

> Tag tagsIdGet(id)

Retrieve a single tag by id

### Example

```javascript
import Contribly from 'contribly';

let apiInstance = new Contribly.TagApi();
let id = "id_example"; // String | Id of the tag to return
apiInstance.tagsIdGet(id, (error, data, response) => {
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
 **id** | **String**| Id of the tag to return | 

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tagsPost

> Tag tagsPost(tagSubmission)

Create a new tag

### Example

```javascript
import Contribly from 'contribly';

let apiInstance = new Contribly.TagApi();
let tagSubmission = new Contribly.TagSubmission(); // TagSubmission | Tag object to be created
apiInstance.tagsPost(tagSubmission, (error, data, response) => {
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
 **tagSubmission** | [**TagSubmission**](TagSubmission.md)| Tag object to be created | 

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagsetsGet

> [TagSet] tagsetsGet(opts)

List tag sets

Retrieve tag sets.

### Example

```javascript
import Contribly from 'contribly';

let apiInstance = new Contribly.TagApi();
let opts = {
  'ownedBy': "ownedBy_example", // String | Restrict results to those owned by this user.
  'urlWords': "urlWords_example" // String | Restrict results by urlWords. Should be used with ownedBy when searching for one of your own tag sets.
};
apiInstance.tagsetsGet(opts, (error, data, response) => {
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
 **ownedBy** | **String**| Restrict results to those owned by this user. | [optional] 
 **urlWords** | **String**| Restrict results by urlWords. Should be used with ownedBy when searching for one of your own tag sets. | [optional] 

### Return type

[**[TagSet]**](TagSet.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tagsetsIdGet

> TagSet tagsetsIdGet(id)

Retrieve a single tag set by id

### Example

```javascript
import Contribly from 'contribly';

let apiInstance = new Contribly.TagApi();
let id = "id_example"; // String | Id of the tag set to return
apiInstance.tagsetsIdGet(id, (error, data, response) => {
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
 **id** | **String**| Id of the tag set to return | 

### Return type

[**TagSet**](TagSet.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tagsetsPost

> TagSet tagsetsPost(tagSetSubmission)

Create a new tag set

### Example

```javascript
import Contribly from 'contribly';

let apiInstance = new Contribly.TagApi();
let tagSetSubmission = new Contribly.TagSetSubmission(); // TagSetSubmission | Tag set to be created
apiInstance.tagsetsPost(tagSetSubmission, (error, data, response) => {
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
 **tagSetSubmission** | [**TagSetSubmission**](TagSetSubmission.md)| Tag set to be created | 

### Return type

[**TagSet**](TagSet.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

