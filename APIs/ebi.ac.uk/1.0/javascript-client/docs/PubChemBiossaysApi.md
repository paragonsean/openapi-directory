# CrOssBarDataApi.PubChemBiossaysApi

All URIs are relative to *http://www.ebi.ac.uk/Tools/crossbar*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getBioassaysUsingGET**](PubChemBiossaysApi.md#getBioassaysUsingGET) | **GET** /pubchem/bioassays | Get pubchem bioassays



## getBioassaysUsingGET

> Bioassays getBioassaysUsingGET(opts)

Get pubchem bioassays

### Example

```javascript
import CrOssBarDataApi from 'cr_oss_bar_data_api';

let apiInstance = new CrOssBarDataApi.PubChemBiossaysApi();
let opts = {
  'accession': ["null"], // [String] | accession
  'assayPubchemId': ["null"], // [String] | assayPubchemId
  'limit': 1, // Number | limit
  'ncbiProteinId': ["null"], // [String] | ncbiProteinId
  'page': 0 // Number | page
};
apiInstance.getBioassaysUsingGET(opts, (error, data, response) => {
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
 **accession** | [**[String]**](String.md)| accession | [optional] 
 **assayPubchemId** | [**[String]**](String.md)| assayPubchemId | [optional] 
 **limit** | **Number**| limit | [optional] [default to 1]
 **ncbiProteinId** | [**[String]**](String.md)| ncbiProteinId | [optional] 
 **page** | **Number**| page | [optional] [default to 0]

### Return type

[**Bioassays**](Bioassays.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

