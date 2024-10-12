# CrOssBarDataApi.DrugsApi

All URIs are relative to *http://www.ebi.ac.uk/Tools/crossbar*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDrugsUsingGET**](DrugsApi.md#getDrugsUsingGET) | **GET** /drugs | drugs collected from Drugbank



## getDrugsUsingGET

> Drugs getDrugsUsingGET(opts)

drugs collected from Drugbank

### Example

```javascript
import CrOssBarDataApi from 'cr_oss_bar_data_api';

let apiInstance = new CrOssBarDataApi.DrugsApi();
let opts = {
  'accession': ["null"], // [String] | accession
  'chemblId': ["null"], // [String] | chemblId
  'identifier': ["null"], // [String] | identifier
  'limit': 10, // Number | limit
  'name': ["null"], // [String] | name
  'page': 0, // Number | page
  'pubchemCid': ["null"] // [String] | pubchemCid
};
apiInstance.getDrugsUsingGET(opts, (error, data, response) => {
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
 **chemblId** | [**[String]**](String.md)| chemblId | [optional] 
 **identifier** | [**[String]**](String.md)| identifier | [optional] 
 **limit** | **Number**| limit | [optional] [default to 10]
 **name** | [**[String]**](String.md)| name | [optional] 
 **page** | **Number**| page | [optional] [default to 0]
 **pubchemCid** | [**[String]**](String.md)| pubchemCid | [optional] 

### Return type

[**Drugs**](Drugs.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

