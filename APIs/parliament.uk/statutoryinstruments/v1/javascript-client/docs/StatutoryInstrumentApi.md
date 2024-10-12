# StatutoryInstrumentsApi.StatutoryInstrumentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getBusinessItemsByStatutoryInstrumentId**](StatutoryInstrumentApi.md#getBusinessItemsByStatutoryInstrumentId) | **GET** /api/v1/StatutoryInstrument/{id}/BusinessItems | Returns business items belonging to statutory instrument with ID.
[**getStatutoryInstrumentById**](StatutoryInstrumentApi.md#getStatutoryInstrumentById) | **GET** /api/v1/StatutoryInstrument/{id} | Returns a statutory instrument by ID.
[**getStatutoryInstruments**](StatutoryInstrumentApi.md#getStatutoryInstruments) | **GET** /api/v1/StatutoryInstrument | Returns a list of statutory instruments.



## getBusinessItemsByStatutoryInstrumentId

> BusinessItemResourceCollection getBusinessItemsByStatutoryInstrumentId(id)

Returns business items belonging to statutory instrument with ID.

### Example

```javascript
import StatutoryInstrumentsApi from 'statutory_instruments_api';

let apiInstance = new StatutoryInstrumentsApi.StatutoryInstrumentApi();
let id = "id_example"; // String | Business items belonging to statutory instrument with the ID specified
apiInstance.getBusinessItemsByStatutoryInstrumentId(id, (error, data, response) => {
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
 **id** | **String**| Business items belonging to statutory instrument with the ID specified | 

### Return type

[**BusinessItemResourceCollection**](BusinessItemResourceCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## getStatutoryInstrumentById

> StatutoryInstrumentResource getStatutoryInstrumentById(id)

Returns a statutory instrument by ID.

### Example

```javascript
import StatutoryInstrumentsApi from 'statutory_instruments_api';

let apiInstance = new StatutoryInstrumentsApi.StatutoryInstrumentApi();
let id = "id_example"; // String | Statutory instrument with the ID specified
apiInstance.getStatutoryInstrumentById(id, (error, data, response) => {
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
 **id** | **String**| Statutory instrument with the ID specified | 

### Return type

[**StatutoryInstrumentResource**](StatutoryInstrumentResource.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## getStatutoryInstruments

> StatutoryInstrumentResourceCollection getStatutoryInstruments(opts)

Returns a list of statutory instruments.

### Example

```javascript
import StatutoryInstrumentsApi from 'statutory_instruments_api';

let apiInstance = new StatutoryInstrumentsApi.StatutoryInstrumentApi();
let opts = {
  'name': "name_example", // String | Statutory instruments with the name specified
  'statutoryInstrumentType': new StatutoryInstrumentsApi.StatutoryInstrumentType(), // StatutoryInstrumentType | Statutory instruments where the statutory instrument type is the type provided
  'scheduledDebate': true, // Boolean | Statutory instrument which contains a scheduled debate
  'motionToStop': true, // Boolean | Statutory instruments which contains a motion to stop
  'concernsRaisedByCommittee': true, // Boolean | Statutory instruments which contains concerns raised by committee
  'parliamentaryProcessConcluded': new StatutoryInstrumentsApi.ParliamentaryProcess(), // ParliamentaryProcess | Statutory instruments where the parliamentary process is concluded or notconcluded
  'departmentId': 56, // Number | Statutory instruments with the department ID specified
  'layingBodyId': "layingBodyId_example", // String | Statutory instruments with the laying body ID specified
  'house': new StatutoryInstrumentsApi.House(), // House | Statutory instruments laid in the house specified
  'skip': 56, // Number | The number of records to skip from the first, default is 0
  'take': 56 // Number | The number of records to return, default is 20
};
apiInstance.getStatutoryInstruments(opts, (error, data, response) => {
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
 **name** | **String**| Statutory instruments with the name specified | [optional] 
 **statutoryInstrumentType** | [**StatutoryInstrumentType**](.md)| Statutory instruments where the statutory instrument type is the type provided | [optional] 
 **scheduledDebate** | **Boolean**| Statutory instrument which contains a scheduled debate | [optional] 
 **motionToStop** | **Boolean**| Statutory instruments which contains a motion to stop | [optional] 
 **concernsRaisedByCommittee** | **Boolean**| Statutory instruments which contains concerns raised by committee | [optional] 
 **parliamentaryProcessConcluded** | [**ParliamentaryProcess**](.md)| Statutory instruments where the parliamentary process is concluded or notconcluded | [optional] 
 **departmentId** | **Number**| Statutory instruments with the department ID specified | [optional] 
 **layingBodyId** | **String**| Statutory instruments with the laying body ID specified | [optional] 
 **house** | [**House**](.md)| Statutory instruments laid in the house specified | [optional] 
 **skip** | **Number**| The number of records to skip from the first, default is 0 | [optional] 
 **take** | **Number**| The number of records to return, default is 20 | [optional] 

### Return type

[**StatutoryInstrumentResourceCollection**](StatutoryInstrumentResourceCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

