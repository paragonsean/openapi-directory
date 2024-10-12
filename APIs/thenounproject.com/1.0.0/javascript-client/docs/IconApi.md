# TheNounProject.IconApi

All URIs are relative to *http://api.thenounproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getIconById**](IconApi.md#getIconById) | **GET** /icon/{id} | Get icon by id
[**getIconByTerm**](IconApi.md#getIconByTerm) | **GET** /icon/{term} | Get icon by term



## getIconById

> getIconById(id)

Get icon by id

Returns a single icon

### Example

```javascript
import TheNounProject from 'the_noun_project';

let apiInstance = new TheNounProject.IconApi();
let id = 56; // Number | Icon id
apiInstance.getIconById(id, (error, data, response) => {
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
 **id** | **Number**| Icon id | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getIconByTerm

> getIconByTerm(term)

Get icon by term

Returns a single icon

### Example

```javascript
import TheNounProject from 'the_noun_project';

let apiInstance = new TheNounProject.IconApi();
let term = "term_example"; // String | Icon term
apiInstance.getIconByTerm(term, (error, data, response) => {
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
 **term** | **String**| Icon term | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

