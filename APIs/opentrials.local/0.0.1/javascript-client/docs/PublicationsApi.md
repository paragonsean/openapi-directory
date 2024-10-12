# OpenTrialsApi.PublicationsApi

All URIs are relative to *http://opentrials.local/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPublication**](PublicationsApi.md#getPublication) | **GET** /publications/{id} | 



## getPublication

> Publication getPublication(id)



Returns publication details

### Example

```javascript
import OpenTrialsApi from 'open_trials_api';

let apiInstance = new OpenTrialsApi.PublicationsApi();
let id = "id_example"; // String | ID of the publication
apiInstance.getPublication(id, (error, data, response) => {
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
 **id** | **String**| ID of the publication | 

### Return type

[**Publication**](Publication.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

