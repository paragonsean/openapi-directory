# EnterobaseApi.StsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV20DatabaseSchemeStsGet**](StsApi.md#apiV20DatabaseSchemeStsGet) | **GET** /api/v2.0/{database}/{scheme}/sts | 



## apiV20DatabaseSchemeStsGet

> apiV20DatabaseSchemeStsGet(database, scheme2, opts)



ST profile data

### Example

```javascript
import EnterobaseApi from 'enterobase_api';

let apiInstance = new EnterobaseApi.StsApi();
let database = "database_example"; // String | Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
let scheme2 = "scheme_example"; // String | 
let opts = {
  'barcode': ["null"], // [String] | Unique barcode for Strain records, <database prefix>_<ID code> e.g. SAL_AA0001AA
  'stId': "stId_example", // String | 
  'offset': 0, // Number | 
  'showAlleles': true, // Boolean | 
  'onlyFields': ["null"], // [String] | 
  'reldate': 56, // Number | 
  'limit': 50, // Number | 
  'scheme': "scheme_example" // String | 
};
apiInstance.apiV20DatabaseSchemeStsGet(database, scheme2, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | **String**| Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively | 
 **scheme2** | **String**|  | 
 **barcode** | [**[String]**](String.md)| Unique barcode for Strain records, &lt;database prefix&gt;_&lt;ID code&gt; e.g. SAL_AA0001AA | [optional] 
 **stId** | **String**|  | [optional] 
 **offset** | **Number**|  | [optional] [default to 0]
 **showAlleles** | **Boolean**|  | [optional] 
 **onlyFields** | [**[String]**](String.md)|  | [optional] 
 **reldate** | **Number**|  | [optional] 
 **limit** | **Number**|  | [optional] [default to 50]
 **scheme** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

