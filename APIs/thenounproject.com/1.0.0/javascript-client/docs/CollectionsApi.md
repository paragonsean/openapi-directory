# TheNounProject.CollectionsApi

All URIs are relative to *http://api.thenounproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAllCollections**](CollectionsApi.md#getAllCollections) | **GET** /collections | Get all collections



## getAllCollections

> getAllCollections(opts)

Get all collections

Return&#39;s a list of all collections

### Example

```javascript
import TheNounProject from 'the_noun_project';

let apiInstance = new TheNounProject.CollectionsApi();
let opts = {
  'limit': 56, // Number | Maximum number of results
  'offset': 56, // Number | Number of results to displace or skip over
  'page': 56 // Number | Number of results of limit length to displace or skip over
};
apiInstance.getAllCollections(opts, (error, data, response) => {
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

