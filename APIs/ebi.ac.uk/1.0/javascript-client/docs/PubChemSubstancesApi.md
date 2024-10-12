# CrOssBarDataApi.PubChemSubstancesApi

All URIs are relative to *http://www.ebi.ac.uk/Tools/crossbar*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSubstancesUsingGET**](PubChemSubstancesApi.md#getSubstancesUsingGET) | **GET** /pubchem/substances | Get pubchem substances



## getSubstancesUsingGET

> PubchemSubstances getSubstancesUsingGET(opts)

Get pubchem substances

### Example

```javascript
import CrOssBarDataApi from 'cr_oss_bar_data_api';

let apiInstance = new CrOssBarDataApi.PubChemSubstancesApi();
let opts = {
  'cid': ["null"], // [String] | cid
  'limit': 10, // Number | limit
  'page': 0, // Number | page
  'sid': ["null"] // [String] | sid
};
apiInstance.getSubstancesUsingGET(opts, (error, data, response) => {
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
 **cid** | [**[String]**](String.md)| cid | [optional] 
 **limit** | **Number**| limit | [optional] [default to 10]
 **page** | **Number**| page | [optional] [default to 0]
 **sid** | [**[String]**](String.md)| sid | [optional] 

### Return type

[**PubchemSubstances**](PubchemSubstances.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

