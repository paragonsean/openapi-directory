# CrOssBarDataApi.PubChemCompoundsApi

All URIs are relative to *http://www.ebi.ac.uk/Tools/crossbar*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCompoundsUsingGET**](PubChemCompoundsApi.md#getCompoundsUsingGET) | **GET** /pubchem/compounds | Get pubchem compounds



## getCompoundsUsingGET

> PubchemCompounds getCompoundsUsingGET(opts)

Get pubchem compounds

### Example

```javascript
import CrOssBarDataApi from 'cr_oss_bar_data_api';

let apiInstance = new CrOssBarDataApi.PubChemCompoundsApi();
let opts = {
  'canonicalSmiles': ["null"], // [String] | canonicalSmiles
  'cid': ["null"], // [String] | cid
  'inchiKey': ["null"], // [String] | inchiKey
  'limit': 10, // Number | limit
  'page': 0 // Number | page
};
apiInstance.getCompoundsUsingGET(opts, (error, data, response) => {
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
 **canonicalSmiles** | [**[String]**](String.md)| canonicalSmiles | [optional] 
 **cid** | [**[String]**](String.md)| cid | [optional] 
 **inchiKey** | [**[String]**](String.md)| inchiKey | [optional] 
 **limit** | **Number**| limit | [optional] [default to 10]
 **page** | **Number**| page | [optional] [default to 0]

### Return type

[**PubchemCompounds**](PubchemCompounds.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

