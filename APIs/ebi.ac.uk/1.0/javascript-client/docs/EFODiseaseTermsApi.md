# CrOssBarDataApi.EFODiseaseTermsApi

All URIs are relative to *http://www.ebi.ac.uk/Tools/crossbar*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getEFOUsingGET**](EFODiseaseTermsApi.md#getEFOUsingGET) | **GET** /efo | Get EFO diseases data



## getEFOUsingGET

> EFOEntities getEFOUsingGET(opts)

Get EFO diseases data

### Example

```javascript
import CrOssBarDataApi from 'cr_oss_bar_data_api';

let apiInstance = new CrOssBarDataApi.EFODiseaseTermsApi();
let opts = {
  'doid': ["null"], // [String] | doid
  'label': ["null"], // [String] | label
  'limit': 10, // Number | limit
  'mesh': ["null"], // [String] | mesh
  'oboId': ["null"], // [String] | oboId
  'omimId': ["null"], // [String] | omimId
  'page': 0, // Number | page
  'synonym': ["null"] // [String] | synonym
};
apiInstance.getEFOUsingGET(opts, (error, data, response) => {
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
 **doid** | [**[String]**](String.md)| doid | [optional] 
 **label** | [**[String]**](String.md)| label | [optional] 
 **limit** | **Number**| limit | [optional] [default to 10]
 **mesh** | [**[String]**](String.md)| mesh | [optional] 
 **oboId** | [**[String]**](String.md)| oboId | [optional] 
 **omimId** | [**[String]**](String.md)| omimId | [optional] 
 **page** | **Number**| page | [optional] [default to 0]
 **synonym** | [**[String]**](String.md)| synonym | [optional] 

### Return type

[**EFOEntities**](EFOEntities.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

