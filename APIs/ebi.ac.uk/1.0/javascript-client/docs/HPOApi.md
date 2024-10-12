# CrOssBarDataApi.HPOApi

All URIs are relative to *http://www.ebi.ac.uk/Tools/crossbar*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getHpoUsingGET**](HPOApi.md#getHpoUsingGET) | **GET** /hpo | Get HPO phenotypes data



## getHpoUsingGET

> HpoEntities getHpoUsingGET(opts)

Get HPO phenotypes data

### Example

```javascript
import CrOssBarDataApi from 'cr_oss_bar_data_api';

let apiInstance = new CrOssBarDataApi.HPOApi();
let opts = {
  'genesymbol': ["null"], // [String] | genesymbol
  'hpotermname': ["null"], // [String] | hpotermname
  'limit': 10, // Number | limit
  'page': 0, // Number | page
  'synonym': ["null"] // [String] | synonym
};
apiInstance.getHpoUsingGET(opts, (error, data, response) => {
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
 **genesymbol** | [**[String]**](String.md)| genesymbol | [optional] 
 **hpotermname** | [**[String]**](String.md)| hpotermname | [optional] 
 **limit** | **Number**| limit | [optional] [default to 10]
 **page** | **Number**| page | [optional] [default to 0]
 **synonym** | [**[String]**](String.md)| synonym | [optional] 

### Return type

[**HpoEntities**](HpoEntities.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

