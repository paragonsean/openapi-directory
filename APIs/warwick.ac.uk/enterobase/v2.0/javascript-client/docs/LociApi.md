# EnterobaseApi.LociApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV20DatabaseSchemeLociGet**](LociApi.md#apiV20DatabaseSchemeLociGet) | **GET** /api/v2.0/{database}/{scheme}/loci | 



## apiV20DatabaseSchemeLociGet

> apiV20DatabaseSchemeLociGet(database, scheme2, opts)



Loci 

### Example

```javascript
import EnterobaseApi from 'enterobase_api';

let apiInstance = new EnterobaseApi.LociApi();
let database = "database_example"; // String | Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
let scheme2 = "scheme_example"; // String | 
let opts = {
  'barcode': ["null"], // [String] | Unique barcode for Strain records, <database prefix>_<ID code> e.g. SAL_AA0001AA
  'locus': "locus_example", // String | 
  'offset': 0, // Number | 
  'createTime': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'onlyFields': ["null"], // [String] | 
  'limit': 50, // Number | 
  'scheme': "scheme_example" // String | 
};
apiInstance.apiV20DatabaseSchemeLociGet(database, scheme2, opts, (error, data, response) => {
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
 **locus** | **String**|  | [optional] 
 **offset** | **Number**|  | [optional] [default to 0]
 **createTime** | **Date**|  | [optional] 
 **onlyFields** | [**[String]**](String.md)|  | [optional] 
 **limit** | **Number**|  | [optional] [default to 50]
 **scheme** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

