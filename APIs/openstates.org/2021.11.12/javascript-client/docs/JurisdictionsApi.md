# OpenStatesApiV3.JurisdictionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jurisdictionDetailJurisdictionsJurisdictionIdGet**](JurisdictionsApi.md#jurisdictionDetailJurisdictionsJurisdictionIdGet) | **GET** /jurisdictions/{jurisdiction_id} | Jurisdiction Detail
[**jurisdictionListJurisdictionsGet**](JurisdictionsApi.md#jurisdictionListJurisdictionsGet) | **GET** /jurisdictions | Jurisdiction List



## jurisdictionDetailJurisdictionsJurisdictionIdGet

> Jurisdiction jurisdictionDetailJurisdictionsJurisdictionIdGet(jurisdictionId, opts)

Jurisdiction Detail

Get details on a single Jurisdiction (e.g. state or municipality).

### Example

```javascript
import OpenStatesApiV3 from 'open_states_api_v3';

let apiInstance = new OpenStatesApiV3.JurisdictionsApi();
let jurisdictionId = "jurisdictionId_example"; // String | 
let opts = {
  'include': [new OpenStatesApiV3.JurisdictionInclude()], // [JurisdictionInclude] | Additional includes for the Jurisdiction response.
  'apikey': "apikey_example", // String | 
  'xApiKey': "xApiKey_example" // String | 
};
apiInstance.jurisdictionDetailJurisdictionsJurisdictionIdGet(jurisdictionId, opts, (error, data, response) => {
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
 **jurisdictionId** | **String**|  | 
 **include** | [**[JurisdictionInclude]**](JurisdictionInclude.md)| Additional includes for the Jurisdiction response. | [optional] 
 **apikey** | **String**|  | [optional] 
 **xApiKey** | **String**|  | [optional] 

### Return type

[**Jurisdiction**](Jurisdiction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jurisdictionListJurisdictionsGet

> JurisdictionList jurisdictionListJurisdictionsGet(opts)

Jurisdiction List

Get list of supported Jurisdictions, a Jurisdiction is a state or municipality.

### Example

```javascript
import OpenStatesApiV3 from 'open_states_api_v3';

let apiInstance = new OpenStatesApiV3.JurisdictionsApi();
let opts = {
  'classification': new OpenStatesApiV3.JurisdictionClassification(), // JurisdictionClassification | Filter returned jurisdictions by type.
  'include': [new OpenStatesApiV3.JurisdictionInclude()], // [JurisdictionInclude] | Additional information to include in response.
  'page': 1, // Number | 
  'perPage': 52, // Number | 
  'apikey': "apikey_example", // String | 
  'xApiKey': "xApiKey_example" // String | 
};
apiInstance.jurisdictionListJurisdictionsGet(opts, (error, data, response) => {
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
 **classification** | [**JurisdictionClassification**](.md)| Filter returned jurisdictions by type. | [optional] 
 **include** | [**[JurisdictionInclude]**](JurisdictionInclude.md)| Additional information to include in response. | [optional] 
 **page** | **Number**|  | [optional] [default to 1]
 **perPage** | **Number**|  | [optional] [default to 52]
 **apikey** | **String**|  | [optional] 
 **xApiKey** | **String**|  | [optional] 

### Return type

[**JurisdictionList**](JurisdictionList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

