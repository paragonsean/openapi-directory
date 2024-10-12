# StatutoryInstrumentsApi.ProposedNegativeStatutoryInstrumentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getBusinessItemsByProposedNegativeStatutoryInstrumentId**](ProposedNegativeStatutoryInstrumentApi.md#getBusinessItemsByProposedNegativeStatutoryInstrumentId) | **GET** /api/v1/ProposedNegativeStatutoryInstrument/{id}/BusinessItems | Returns business items belonging to a proposed negative statutory instrument.
[**getProposedNegativeStatutoryInstrumentById**](ProposedNegativeStatutoryInstrumentApi.md#getProposedNegativeStatutoryInstrumentById) | **GET** /api/v1/ProposedNegativeStatutoryInstrument/{id} | Returns proposed negative statutory instrument by ID.
[**getProposedNegativeStatutoryInstruments**](ProposedNegativeStatutoryInstrumentApi.md#getProposedNegativeStatutoryInstruments) | **GET** /api/v1/ProposedNegativeStatutoryInstrument | Returns a list of proposed negative statutory instruments.



## getBusinessItemsByProposedNegativeStatutoryInstrumentId

> BusinessItemResourceCollection getBusinessItemsByProposedNegativeStatutoryInstrumentId(id)

Returns business items belonging to a proposed negative statutory instrument.

### Example

```javascript
import StatutoryInstrumentsApi from 'statutory_instruments_api';

let apiInstance = new StatutoryInstrumentsApi.ProposedNegativeStatutoryInstrumentApi();
let id = "id_example"; // String | Business items belonging to proposed negative statutory instrument with the ID specified
apiInstance.getBusinessItemsByProposedNegativeStatutoryInstrumentId(id, (error, data, response) => {
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
 **id** | **String**| Business items belonging to proposed negative statutory instrument with the ID specified | 

### Return type

[**BusinessItemResourceCollection**](BusinessItemResourceCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## getProposedNegativeStatutoryInstrumentById

> ProposedNegativeStatutoryInstrumentResource getProposedNegativeStatutoryInstrumentById(id)

Returns proposed negative statutory instrument by ID.

### Example

```javascript
import StatutoryInstrumentsApi from 'statutory_instruments_api';

let apiInstance = new StatutoryInstrumentsApi.ProposedNegativeStatutoryInstrumentApi();
let id = "id_example"; // String | Proposed negative statutory instrument with the ID specified
apiInstance.getProposedNegativeStatutoryInstrumentById(id, (error, data, response) => {
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
 **id** | **String**| Proposed negative statutory instrument with the ID specified | 

### Return type

[**ProposedNegativeStatutoryInstrumentResource**](ProposedNegativeStatutoryInstrumentResource.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## getProposedNegativeStatutoryInstruments

> ProposedNegativeStatutoryInstrumentResourceCollection getProposedNegativeStatutoryInstruments(opts)

Returns a list of proposed negative statutory instruments.

### Example

```javascript
import StatutoryInstrumentsApi from 'statutory_instruments_api';

let apiInstance = new StatutoryInstrumentsApi.ProposedNegativeStatutoryInstrumentApi();
let opts = {
  'name': "name_example", // String | Proposed negative statutory instruments with the name provided
  'recommendedForProcedureChange': true, // Boolean | Proposed negative statutory instruments recommended for procedure change
  'departmentId': 56, // Number | Proposed negative statutory instruments with the department ID specified
  'layingBodyId': "layingBodyId_example", // String | Proposed negative statutory instruments with the laying body ID specified
  'skip': 56, // Number | The number of records to skip from the first, default is 0
  'take': 56 // Number | The number of records to return, default is 20
};
apiInstance.getProposedNegativeStatutoryInstruments(opts, (error, data, response) => {
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
 **name** | **String**| Proposed negative statutory instruments with the name provided | [optional] 
 **recommendedForProcedureChange** | **Boolean**| Proposed negative statutory instruments recommended for procedure change | [optional] 
 **departmentId** | **Number**| Proposed negative statutory instruments with the department ID specified | [optional] 
 **layingBodyId** | **String**| Proposed negative statutory instruments with the laying body ID specified | [optional] 
 **skip** | **Number**| The number of records to skip from the first, default is 0 | [optional] 
 **take** | **Number**| The number of records to return, default is 20 | [optional] 

### Return type

[**ProposedNegativeStatutoryInstrumentResourceCollection**](ProposedNegativeStatutoryInstrumentResourceCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

