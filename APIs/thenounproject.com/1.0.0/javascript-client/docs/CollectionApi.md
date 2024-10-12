# TheNounProject.CollectionApi

All URIs are relative to *http://api.thenounproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCollectionById**](CollectionApi.md#getCollectionById) | **GET** /collection/{id} | Get collection by id
[**getCollectionBySlug**](CollectionApi.md#getCollectionBySlug) | **GET** /collection/{slug} | Get collection by slug
[**getCollectionIconsById**](CollectionApi.md#getCollectionIconsById) | **GET** /collection/{id}/icons | Get collection icons by id
[**getCollectionIconsBySlug**](CollectionApi.md#getCollectionIconsBySlug) | **GET** /collection/{slug}/icons | Get collection icons by slug



## getCollectionById

> getCollectionById(id)

Get collection by id

Returns a single collection

### Example

```javascript
import TheNounProject from 'the_noun_project';

let apiInstance = new TheNounProject.CollectionApi();
let id = 56; // Number | Collection id
apiInstance.getCollectionById(id, (error, data, response) => {
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
 **id** | **Number**| Collection id | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getCollectionBySlug

> getCollectionBySlug(slug)

Get collection by slug

Returns a single collection

### Example

```javascript
import TheNounProject from 'the_noun_project';

let apiInstance = new TheNounProject.CollectionApi();
let slug = "slug_example"; // String | Collection slug
apiInstance.getCollectionBySlug(slug, (error, data, response) => {
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
 **slug** | **String**| Collection slug | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getCollectionIconsById

> getCollectionIconsById(id, opts)

Get collection icons by id

Returns a list of icons associated with a collection

### Example

```javascript
import TheNounProject from 'the_noun_project';

let apiInstance = new TheNounProject.CollectionApi();
let id = 56; // Number | Collection id
let opts = {
  'limit': 56, // Number | Maximum number of results
  'offset': 56, // Number | Number of results to displace or skip over
  'page': 56 // Number | Number of results of limit length to displace or skip over
};
apiInstance.getCollectionIconsById(id, opts, (error, data, response) => {
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
 **id** | **Number**| Collection id | 
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


## getCollectionIconsBySlug

> getCollectionIconsBySlug(slug, opts)

Get collection icons by slug

Returns a list of icons associated with a collection

### Example

```javascript
import TheNounProject from 'the_noun_project';

let apiInstance = new TheNounProject.CollectionApi();
let slug = "slug_example"; // String | Collection slug
let opts = {
  'limit': 56, // Number | Maximum number of results
  'offset': 56, // Number | Number of results to displace or skip over
  'page': 56 // Number | Number of results of limit length to displace or skip over
};
apiInstance.getCollectionIconsBySlug(slug, opts, (error, data, response) => {
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
 **slug** | **String**| Collection slug | 
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

