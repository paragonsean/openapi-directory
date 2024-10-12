# VocaDbWeb.PVApiApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiPvsForSongsGet**](PVApiApi.md#apiPvsForSongsGet) | **GET** /api/pvs/for-songs | 



## apiPvsForSongsGet

> PVForSongContractPartialFindResult apiPvsForSongsGet(opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.PVApiApi();
let opts = {
  'name': "name_example", // String | 
  'author': "author_example", // String | 
  'service': new VocaDbWeb.PVService(), // PVService | 
  'maxResults': 10, // Number | 
  'getTotalCount': false, // Boolean | 
  'lang': new VocaDbWeb.ContentLanguagePreference() // ContentLanguagePreference | 
};
apiInstance.apiPvsForSongsGet(opts, (error, data, response) => {
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
 **name** | **String**|  | [optional] 
 **author** | **String**|  | [optional] 
 **service** | [**PVService**](.md)|  | [optional] 
 **maxResults** | **Number**|  | [optional] [default to 10]
 **getTotalCount** | **Boolean**|  | [optional] [default to false]
 **lang** | [**ContentLanguagePreference**](.md)|  | [optional] 

### Return type

[**PVForSongContractPartialFindResult**](PVForSongContractPartialFindResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

