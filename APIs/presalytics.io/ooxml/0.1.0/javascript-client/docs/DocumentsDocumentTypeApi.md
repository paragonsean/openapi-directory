# OoxmlAutomation.DocumentsDocumentTypeApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**documentsDocumenttypeGet**](DocumentsDocumentTypeApi.md#documentsDocumenttypeGet) | **GET** /Documents/DocumentType | DocumentType: List All Possible Types
[**documentsDocumenttypeGetId**](DocumentsDocumentTypeApi.md#documentsDocumenttypeGetId) | **GET** /Documents/DocumentType/{id} | DocumentType: Get by Id
[**documentsDocumenttypeTypeidGetTypeId**](DocumentsDocumentTypeApi.md#documentsDocumenttypeTypeidGetTypeId) | **GET** /Documents/DocumentType/TypeId/{type_id} | DocumentType: Get By Type Id



## documentsDocumenttypeGet

> [DocumentType] documentsDocumenttypeGet()

DocumentType: List All Possible Types

List Types: Use this method to retreive a list of possible options for the DocumentType type. Use the Id from oneof the returned elements on to make changes to elements in the Documents object space.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.DocumentsDocumentTypeApi();
apiInstance.documentsDocumenttypeGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[DocumentType]**](DocumentType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## documentsDocumenttypeGetId

> DocumentType documentsDocumenttypeGetId(id)

DocumentType: Get by Id

Get by Id: Use this method to retrieve a DocumentType object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.DocumentsDocumentTypeApi();
let id = "id_example"; // String | 
apiInstance.documentsDocumenttypeGetId(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**DocumentType**](DocumentType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## documentsDocumenttypeTypeidGetTypeId

> DocumentType documentsDocumenttypeTypeidGetTypeId(typeId)

DocumentType: Get By Type Id

This endpoint returns Type metadata from an integer type_id that can found on objects throughout the api.

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.DocumentsDocumentTypeApi();
let typeId = 56; // Number | 
apiInstance.documentsDocumenttypeTypeidGetTypeId(typeId, (error, data, response) => {
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
 **typeId** | **Number**|  | 

### Return type

[**DocumentType**](DocumentType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

