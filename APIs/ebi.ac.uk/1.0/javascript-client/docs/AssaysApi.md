# CrOssBarDataApi.AssaysApi

All URIs are relative to *http://www.ebi.ac.uk/Tools/crossbar*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAssaysUsingGET**](AssaysApi.md#getAssaysUsingGET) | **GET** /assays | Get ChEMBL assays



## getAssaysUsingGET

> Assays getAssaysUsingGET(opts)

Get ChEMBL assays

### Example

```javascript
import CrOssBarDataApi from 'cr_oss_bar_data_api';

let apiInstance = new CrOssBarDataApi.AssaysApi();
let opts = {
  'assayChemblId': ["null"], // [String] | assayChemblId
  'assayOrg': ["null"], // [String] | assayOrg
  'assayType': ["null"], // [String] | assayType
  'limit': 10, // Number | limit
  'page': 0, // Number | page
  'targetChemblId': ["null"] // [String] | targetChemblId
};
apiInstance.getAssaysUsingGET(opts, (error, data, response) => {
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
 **assayChemblId** | [**[String]**](String.md)| assayChemblId | [optional] 
 **assayOrg** | [**[String]**](String.md)| assayOrg | [optional] 
 **assayType** | [**[String]**](String.md)| assayType | [optional] 
 **limit** | **Number**| limit | [optional] [default to 10]
 **page** | **Number**| page | [optional] [default to 0]
 **targetChemblId** | [**[String]**](String.md)| targetChemblId | [optional] 

### Return type

[**Assays**](Assays.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

