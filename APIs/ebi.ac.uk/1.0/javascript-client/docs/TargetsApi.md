# CrOssBarDataApi.TargetsApi

All URIs are relative to *http://www.ebi.ac.uk/Tools/crossbar*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getTargetsUsingGET**](TargetsApi.md#getTargetsUsingGET) | **GET** /targets | Get ChEMBL targets



## getTargetsUsingGET

> Targets getTargetsUsingGET(opts)

Get ChEMBL targets

### Example

```javascript
import CrOssBarDataApi from 'cr_oss_bar_data_api';

let apiInstance = new CrOssBarDataApi.TargetsApi();
let opts = {
  'accession': ["null"], // [String] | accession
  'limit': 10, // Number | limit
  'page': 0, // Number | page
  'targetIds': ["null"] // [String] | targetIds
};
apiInstance.getTargetsUsingGET(opts, (error, data, response) => {
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
 **limit** | **Number**| limit | [optional] [default to 10]
 **page** | **Number**| page | [optional] [default to 0]
 **targetIds** | [**[String]**](String.md)| targetIds | [optional] 

### Return type

[**Targets**](Targets.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

