# OpenTrialsApi.DocumentsApi

All URIs are relative to *http://opentrials.local/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDocument**](DocumentsApi.md#getDocument) | **GET** /documents/{id} | 
[**listDocuments**](DocumentsApi.md#listDocuments) | **GET** /documents | 



## getDocument

> Document getDocument(id)



Returns details of a document

### Example

```javascript
import OpenTrialsApi from 'open_trials_api';

let apiInstance = new OpenTrialsApi.DocumentsApi();
let id = "id_example"; // String | ID of the document
apiInstance.getDocument(id, (error, data, response) => {
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
 **id** | **String**| ID of the document | 

### Return type

[**Document**](Document.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDocuments

> DocumentList listDocuments(opts)



Returns documents

### Example

```javascript
import OpenTrialsApi from 'open_trials_api';

let apiInstance = new OpenTrialsApi.DocumentsApi();
let opts = {
  'page': 1, // Number | The page number
  'perPage': 20 // Number | Number of items per page
};
apiInstance.listDocuments(opts, (error, data, response) => {
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
 **page** | **Number**| The page number | [optional] [default to 1]
 **perPage** | **Number**| Number of items per page | [optional] [default to 20]

### Return type

[**DocumentList**](DocumentList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

