# IsbNdbApi.SubjectApi

All URIs are relative to *https://api.isbndb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subjectNameGet**](SubjectApi.md#subjectNameGet) | **GET** /subject/{name} | Gets subject details
[**subjectsQueryGet**](SubjectApi.md#subjectsQueryGet) | **GET** /subjects/{query} | Search subjects



## subjectNameGet

> Subject subjectNameGet(name)

Gets subject details

Returns details and a list of books with subject.

### Example

```javascript
import IsbNdbApi from 'isb_ndb_api';
let defaultClient = IsbNdbApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new IsbNdbApi.SubjectApi();
let name = "name_example"; // String | A subject in the Subject's database
apiInstance.subjectNameGet(name, (error, data, response) => {
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
 **name** | **String**| A subject in the Subject&#39;s database | 

### Return type

[**Subject**](Subject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## subjectsQueryGet

> subjectsQueryGet(query, opts)

Search subjects

This returns a list of subjects that match the given query

### Example

```javascript
import IsbNdbApi from 'isb_ndb_api';
let defaultClient = IsbNdbApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new IsbNdbApi.SubjectApi();
let query = "query_example"; // String | A string to search for in the Subject’s database
let opts = {
  'pageSize': "pageSize_example", // String | How many items should be returned per page, maximum of 1,000
  'page': "page_example" // String | The number of page to retrieve, please note the API will not return more than 10,000 results no matter how you paginate them
};
apiInstance.subjectsQueryGet(query, opts, (error, data, response) => {
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
 **query** | **String**| A string to search for in the Subject’s database | 
 **pageSize** | **String**| How many items should be returned per page, maximum of 1,000 | [optional] 
 **page** | **String**| The number of page to retrieve, please note the API will not return more than 10,000 results no matter how you paginate them | [optional] 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

