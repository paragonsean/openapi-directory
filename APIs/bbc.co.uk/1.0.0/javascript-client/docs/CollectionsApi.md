# RadioMusicServices.CollectionsApi

All URIs are relative to *https://rms.api.bbc.co.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCollectionMembers**](CollectionsApi.md#getCollectionMembers) | **GET** /collections/{pid}/members | Collection Members



## getCollectionMembers

> ProgrammesResponse getCollectionMembers(xAPIKey, pid, opts)

Collection Members

Episodes and Clips from Collection 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.CollectionsApi();
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let pid = "pid_example"; // String | pid
let opts = {
  'offset': 56, // Number | Paginated results offset
  'limit': 56 // Number | Paginated results limit
};
apiInstance.getCollectionMembers(xAPIKey, pid, opts, (error, data, response) => {
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
 **xAPIKey** | **String**| API_KEY | 
 **pid** | **String**| pid | 
 **offset** | **Number**| Paginated results offset | [optional] 
 **limit** | **Number**| Paginated results limit | [optional] 

### Return type

[**ProgrammesResponse**](ProgrammesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

