# CrOssBarDataApi.ActivitiesApi

All URIs are relative to *http://www.ebi.ac.uk/Tools/crossbar*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getActivitiesUsingGET**](ActivitiesApi.md#getActivitiesUsingGET) | **GET** /activities | Get ChEMBL activities



## getActivitiesUsingGET

> Activities getActivitiesUsingGET(opts)

Get ChEMBL activities

### Example

```javascript
import CrOssBarDataApi from 'cr_oss_bar_data_api';

let apiInstance = new CrOssBarDataApi.ActivitiesApi();
let opts = {
  'assayChemblId': ["null"], // [String] | assayChemblId
  'limit': 10, // Number | limit
  'moleculeChemblId': ["null"], // [String] | moleculeChemblId
  'page': 0, // Number | page
  'pchemblValue': 3.4, // Number | pchemblValue
  'targetChemblId': ["null"] // [String] | targetChemblId
};
apiInstance.getActivitiesUsingGET(opts, (error, data, response) => {
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
 **limit** | **Number**| limit | [optional] [default to 10]
 **moleculeChemblId** | [**[String]**](String.md)| moleculeChemblId | [optional] 
 **page** | **Number**| page | [optional] [default to 0]
 **pchemblValue** | **Number**| pchemblValue | [optional] 
 **targetChemblId** | [**[String]**](String.md)| targetChemblId | [optional] 

### Return type

[**Activities**](Activities.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

