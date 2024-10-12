# StatutoryInstrumentsApi.ProcedureApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getProceduresByIdV1**](ProcedureApi.md#getProceduresByIdV1) | **GET** /api/v1/Procedure/{id} | Returns procedure by ID.
[**getProceduresV1**](ProcedureApi.md#getProceduresV1) | **GET** /api/v1/Procedure | Returns all procedures.



## getProceduresByIdV1

> ProcedureDetailsResource getProceduresByIdV1(id)

Returns procedure by ID.

### Example

```javascript
import StatutoryInstrumentsApi from 'statutory_instruments_api';

let apiInstance = new StatutoryInstrumentsApi.ProcedureApi();
let id = "id_example"; // String | Procedure with the ID specified
apiInstance.getProceduresByIdV1(id, (error, data, response) => {
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
 **id** | **String**| Procedure with the ID specified | 

### Return type

[**ProcedureDetailsResource**](ProcedureDetailsResource.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## getProceduresV1

> ProcedureResourceCollection getProceduresV1()

Returns all procedures.

### Example

```javascript
import StatutoryInstrumentsApi from 'statutory_instruments_api';

let apiInstance = new StatutoryInstrumentsApi.ProcedureApi();
apiInstance.getProceduresV1((error, data, response) => {
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

[**ProcedureResourceCollection**](ProcedureResourceCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

