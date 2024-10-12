# CrOssBarDataApi.PubChemBioassaySidsApi

All URIs are relative to *http://www.ebi.ac.uk/Tools/crossbar*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getBioassaysUsingGET1**](PubChemBioassaySidsApi.md#getBioassaysUsingGET1) | **GET** /pubchem/bioassays/sids | Get pubchem bioassays associated to particular substance ids (sid) &amp; outcome



## getBioassaysUsingGET1

> Bioassays getBioassaysUsingGET1(opts)

Get pubchem bioassays associated to particular substance ids (sid) &amp; outcome

### Example

```javascript
import CrOssBarDataApi from 'cr_oss_bar_data_api';

let apiInstance = new CrOssBarDataApi.PubChemBioassaySidsApi();
let opts = {
  'limit': 10, // Number | limit
  'outcome': "outcome_example", // String | outcome
  'page': 0, // Number | page
  'sids': ["null"] // [String] | sids
};
apiInstance.getBioassaysUsingGET1(opts, (error, data, response) => {
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
 **limit** | **Number**| limit | [optional] [default to 10]
 **outcome** | **String**| outcome | [optional] 
 **page** | **Number**| page | [optional] [default to 0]
 **sids** | [**[String]**](String.md)| sids | [optional] 

### Return type

[**Bioassays**](Bioassays.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

