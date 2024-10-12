# AirflowApiStable.ImportErrorApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getImportError**](ImportErrorApi.md#getImportError) | **GET** /importErrors/{import_error_id} | Get an import error
[**getImportErrors**](ImportErrorApi.md#getImportErrors) | **GET** /importErrors | List import errors



## getImportError

> ImportError getImportError(importErrorId)

Get an import error

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.ImportErrorApi();
let importErrorId = 56; // Number | The import error ID.
apiInstance.getImportError(importErrorId, (error, data, response) => {
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
 **importErrorId** | **Number**| The import error ID. | 

### Return type

[**ImportError**](ImportError.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getImportErrors

> ImportErrorCollection getImportErrors(opts)

List import errors

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.ImportErrorApi();
let opts = {
  'limit': 100, // Number | The numbers of items to return.
  'offset': 56, // Number | The number of items to skip before starting to collect the result set.
  'orderBy': "orderBy_example" // String | The name of the field to order the results by. Prefix a field name with `-` to reverse the sort order.  *New in version 2.1.0* 
};
apiInstance.getImportErrors(opts, (error, data, response) => {
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
 **limit** | **Number**| The numbers of items to return. | [optional] [default to 100]
 **offset** | **Number**| The number of items to skip before starting to collect the result set. | [optional] 
 **orderBy** | **String**| The name of the field to order the results by. Prefix a field name with &#x60;-&#x60; to reverse the sort order.  *New in version 2.1.0*  | [optional] 

### Return type

[**ImportErrorCollection**](ImportErrorCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

