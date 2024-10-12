# DeedApi.DeedApi

All URIs are relative to *https://api.landregistry.gov.uk/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deedDeedReferenceGet**](DeedApi.md#deedDeedReferenceGet) | **GET** /deed/{deed_reference} | Deed



## deedDeedReferenceGet

> OperativeDeed deedDeedReferenceGet(deedReference)

Deed

The Deed endpoint returns details of a specific deed based on the unique deed reference. The response includes the Title Number, Property information, Borrower(s) information and deed information. 

### Example

```javascript
import DeedApi from 'deed_api';

let apiInstance = new DeedApi.DeedApi();
let deedReference = "deedReference_example"; // String | Unique reference of the deed.
apiInstance.deedDeedReferenceGet(deedReference, (error, data, response) => {
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
 **deedReference** | **String**| Unique reference of the deed. | 

### Return type

[**OperativeDeed**](OperativeDeed.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

