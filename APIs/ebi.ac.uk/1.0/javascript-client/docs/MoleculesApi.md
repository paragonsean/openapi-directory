# CrOssBarDataApi.MoleculesApi

All URIs are relative to *http://www.ebi.ac.uk/Tools/crossbar*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getMoleculesUsingGET**](MoleculesApi.md#getMoleculesUsingGET) | **GET** /molecules | Get ChEMBL molecules



## getMoleculesUsingGET

> Molecules getMoleculesUsingGET(opts)

Get ChEMBL molecules

### Example

```javascript
import CrOssBarDataApi from 'cr_oss_bar_data_api';

let apiInstance = new CrOssBarDataApi.MoleculesApi();
let opts = {
  'canonicalSmiles': ["null"], // [String] | canonicalSmiles
  'inchiKey': ["null"], // [String] | inchiKey
  'limit': 10, // Number | limit
  'moleculeChemblId': ["null"], // [String] | moleculeChemblId
  'page': 0 // Number | page
};
apiInstance.getMoleculesUsingGET(opts, (error, data, response) => {
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
 **inchiKey** | [**[String]**](String.md)| inchiKey | [optional] 
 **limit** | **Number**| limit | [optional] [default to 10]
 **moleculeChemblId** | [**[String]**](String.md)| moleculeChemblId | [optional] 
 **page** | **Number**| page | [optional] [default to 0]

### Return type

[**Molecules**](Molecules.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

