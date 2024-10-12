# AvazaApiDocumentation.CreditNoteApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**creditNoteGet**](CreditNoteApi.md#creditNoteGet) | **GET** /api/CreditNote | Gets list of CreditNotes
[**creditNoteGetByID**](CreditNoteApi.md#creditNoteGetByID) | **GET** /api/CreditNote/{id} | Gets Credit Note by CreditNoteID



## creditNoteGet

> CreditNoteList creditNoteGet(opts)

Gets list of CreditNotes

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.CreditNoteApi();
let opts = {
  'updatedAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'pageSize': 56, // Number | Number of items per page (max 1000)
  'pageNumber': 56 // Number | Page to display. Starts from 1.
};
apiInstance.creditNoteGet(opts, (error, data, response) => {
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
 **updatedAfter** | **Date**|  | [optional] 
 **pageSize** | **Number**| Number of items per page (max 1000) | [optional] 
 **pageNumber** | **Number**| Page to display. Starts from 1. | [optional] 

### Return type

[**CreditNoteList**](CreditNoteList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## creditNoteGetByID

> CreditNote creditNoteGetByID(id)

Gets Credit Note by CreditNoteID

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.CreditNoteApi();
let id = 789; // Number | Credit Note ID Number
apiInstance.creditNoteGetByID(id, (error, data, response) => {
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
 **id** | **Number**| Credit Note ID Number | 

### Return type

[**CreditNote**](CreditNote.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml

