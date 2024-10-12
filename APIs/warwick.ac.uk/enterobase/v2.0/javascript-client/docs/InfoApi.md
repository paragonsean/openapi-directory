# EnterobaseApi.InfoApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV20Get**](InfoApi.md#apiV20Get) | **GET** /api/v2.0 | 



## apiV20Get

> apiV20Get(opts)



Top level information about EnteroBase databases

### Example

```javascript
import EnterobaseApi from 'enterobase_api';

let apiInstance = new EnterobaseApi.InfoApi();
let opts = {
  'name': "name_example", // String | Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
  'prefix': "prefix_example", // String | Database prefix, e.g. SAL for Salmonella
  'description': "description_example" // String | Database description
};
apiInstance.apiV20Get(opts, (error, data, response) => {
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
 **name** | **String**| Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively | [optional] 
 **prefix** | **String**| Database prefix, e.g. SAL for Salmonella | [optional] 
 **description** | **String**| Database description | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

