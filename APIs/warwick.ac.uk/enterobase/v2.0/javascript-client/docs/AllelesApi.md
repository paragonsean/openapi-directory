# EnterobaseApi.AllelesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV20DatabaseSchemeAllelesGet**](AllelesApi.md#apiV20DatabaseSchemeAllelesGet) | **GET** /api/v2.0/{database}/{scheme}/alleles | 



## apiV20DatabaseSchemeAllelesGet

> apiV20DatabaseSchemeAllelesGet(locus, database, scheme, opts)



Alleles  data 

### Example

```javascript
import EnterobaseApi from 'enterobase_api';

let apiInstance = new EnterobaseApi.AllelesApi();
let locus = "locus_example"; // String | 
let database = "database_example"; // String | Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
let scheme = "scheme_example"; // String | 
let opts = {
  'barcode': ["null"], // [String] | Unique barcode for Strain records, <database prefix>_<ID code> e.g. SAL_AA0001AA
  'offset': 0, // Number | 
  'alleleId': "alleleId_example", // String | 
  'onlyFields': ["null"], // [String] | 
  'seq': "seq_example", // String | 
  'reldate': 56, // Number | 
  'limit': 50 // Number | 
};
apiInstance.apiV20DatabaseSchemeAllelesGet(locus, database, scheme, opts, (error, data, response) => {
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
 **locus** | **String**|  | 
 **database** | **String**| Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively | 
 **scheme** | **String**|  | 
 **barcode** | [**[String]**](String.md)| Unique barcode for Strain records, &lt;database prefix&gt;_&lt;ID code&gt; e.g. SAL_AA0001AA | [optional] 
 **offset** | **Number**|  | [optional] [default to 0]
 **alleleId** | **String**|  | [optional] 
 **onlyFields** | [**[String]**](String.md)|  | [optional] 
 **seq** | **String**|  | [optional] 
 **reldate** | **Number**|  | [optional] 
 **limit** | **Number**|  | [optional] [default to 50]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

