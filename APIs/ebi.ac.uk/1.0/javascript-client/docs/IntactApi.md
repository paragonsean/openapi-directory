# CrOssBarDataApi.IntactApi

All URIs are relative to *http://www.ebi.ac.uk/Tools/crossbar*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getIntactUsingGET**](IntactApi.md#getIntactUsingGET) | **GET** /intact | Molecular Interactions collected from IntAct



## getIntactUsingGET

> IntactInteractions getIntactUsingGET(opts)

Molecular Interactions collected from IntAct

### Example

```javascript
import CrOssBarDataApi from 'cr_oss_bar_data_api';

let apiInstance = new CrOssBarDataApi.IntactApi();
let opts = {
  'accession': ["null"], // [String] | accession
  'confidence': 3.4, // Number | confidence
  'gene': ["null"], // [String] | gene
  'limit': 10, // Number | limit
  'page': 0 // Number | page
};
apiInstance.getIntactUsingGET(opts, (error, data, response) => {
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
 **confidence** | **Number**| confidence | [optional] 
 **gene** | [**[String]**](String.md)| gene | [optional] 
 **limit** | **Number**| limit | [optional] [default to 10]
 **page** | **Number**| page | [optional] [default to 0]

### Return type

[**IntactInteractions**](IntactInteractions.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

