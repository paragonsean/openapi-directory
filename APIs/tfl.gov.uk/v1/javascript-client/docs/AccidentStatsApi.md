# TransportForLondonUnifiedApi.AccidentStatsApi

All URIs are relative to *https://api.digital.tfl.gov.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accidentStatsGet**](AccidentStatsApi.md#accidentStatsGet) | **GET** /AccidentStats/{year} | Gets all accident details for accidents occuring in the specified year



## accidentStatsGet

> [TflApiPresentationEntitiesAccidentStatsAccidentDetail] accidentStatsGet(year)

Gets all accident details for accidents occuring in the specified year

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.AccidentStatsApi();
let year = 56; // Number | The year for which to filter the accidents on.
apiInstance.accidentStatsGet(year, (error, data, response) => {
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
 **year** | **Number**| The year for which to filter the accidents on. | 

### Return type

[**[TflApiPresentationEntitiesAccidentStatsAccidentDetail]**](TflApiPresentationEntitiesAccidentStatsAccidentDetail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

