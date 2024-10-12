# EnterobaseApi.SchemesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV20DatabaseSchemesBarcodeGet**](SchemesApi.md#apiV20DatabaseSchemesBarcodeGet) | **GET** /api/v2.0/{database}/schemes/{barcode} | 
[**apiV20DatabaseSchemesBarcodePost**](SchemesApi.md#apiV20DatabaseSchemesBarcodePost) | **POST** /api/v2.0/{database}/schemes/{barcode} | 
[**apiV20DatabaseSchemesBarcodePut**](SchemesApi.md#apiV20DatabaseSchemesBarcodePut) | **PUT** /api/v2.0/{database}/schemes/{barcode} | 
[**apiV20DatabaseSchemesGet**](SchemesApi.md#apiV20DatabaseSchemesGet) | **GET** /api/v2.0/{database}/schemes | 



## apiV20DatabaseSchemesBarcodeGet

> apiV20DatabaseSchemesBarcodeGet(database, barcode, opts)



Genotyping schemes

### Example

```javascript
import EnterobaseApi from 'enterobase_api';

let apiInstance = new EnterobaseApi.SchemesApi();
let database = "database_example"; // String | Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
let barcode = "barcode_example"; // String | Unique barcode for Strain records, <database prefix>_<ID code> e.g. SAL_AA0001AA
let opts = {
  'apiV20DatabaseSchemesBarcodeGetRequest': new EnterobaseApi.ApiV20DatabaseSchemesBarcodeGetRequest() // ApiV20DatabaseSchemesBarcodeGetRequest | 
};
apiInstance.apiV20DatabaseSchemesBarcodeGet(database, barcode, opts, (error, data, response) => {
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
 **barcode** | **String**| Unique barcode for Strain records, &lt;database prefix&gt;_&lt;ID code&gt; e.g. SAL_AA0001AA | 
 **apiV20DatabaseSchemesBarcodeGetRequest** | [**ApiV20DatabaseSchemesBarcodeGetRequest**](ApiV20DatabaseSchemesBarcodeGetRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## apiV20DatabaseSchemesBarcodePost

> apiV20DatabaseSchemesBarcodePost(database, barcode, opts)



Genotyping schemes

### Example

```javascript
import EnterobaseApi from 'enterobase_api';

let apiInstance = new EnterobaseApi.SchemesApi();
let database = "database_example"; // String | Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
let barcode = "barcode_example"; // String | Unique barcode for Strain records, <database prefix>_<ID code> e.g. SAL_AA0001AA
let opts = {
  'apiV20DatabaseSchemesBarcodeGetRequest': new EnterobaseApi.ApiV20DatabaseSchemesBarcodeGetRequest() // ApiV20DatabaseSchemesBarcodeGetRequest | 
};
apiInstance.apiV20DatabaseSchemesBarcodePost(database, barcode, opts, (error, data, response) => {
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
 **barcode** | **String**| Unique barcode for Strain records, &lt;database prefix&gt;_&lt;ID code&gt; e.g. SAL_AA0001AA | 
 **apiV20DatabaseSchemesBarcodeGetRequest** | [**ApiV20DatabaseSchemesBarcodeGetRequest**](ApiV20DatabaseSchemesBarcodeGetRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## apiV20DatabaseSchemesBarcodePut

> apiV20DatabaseSchemesBarcodePut(database, barcode, opts)



Genotyping schemes

### Example

```javascript
import EnterobaseApi from 'enterobase_api';

let apiInstance = new EnterobaseApi.SchemesApi();
let database = "database_example"; // String | Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
let barcode = "barcode_example"; // String | Unique barcode for Strain records, <database prefix>_<ID code> e.g. SAL_AA0001AA
let opts = {
  'apiV20DatabaseSchemesBarcodeGetRequest': new EnterobaseApi.ApiV20DatabaseSchemesBarcodeGetRequest() // ApiV20DatabaseSchemesBarcodeGetRequest | 
};
apiInstance.apiV20DatabaseSchemesBarcodePut(database, barcode, opts, (error, data, response) => {
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
 **barcode** | **String**| Unique barcode for Strain records, &lt;database prefix&gt;_&lt;ID code&gt; e.g. SAL_AA0001AA | 
 **apiV20DatabaseSchemesBarcodeGetRequest** | [**ApiV20DatabaseSchemesBarcodeGetRequest**](ApiV20DatabaseSchemesBarcodeGetRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## apiV20DatabaseSchemesGet

> apiV20DatabaseSchemesGet(database, opts)



Genotyping schemes

### Example

```javascript
import EnterobaseApi from 'enterobase_api';

let apiInstance = new EnterobaseApi.SchemesApi();
let database = "database_example"; // String | Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
let opts = {
  'barcode': ["null"], // [String] | Unique barcode for Strain records, <database prefix>_<ID code> e.g. SAL_AA0001AA
  'orderby': "'barcode'", // String | Field to order by. Default: barcode
  'offset': 0, // Number | Cursor position in results
  'label': "label_example", // String | 
  'onlyFields': ["null"], // [String] | 
  'created': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'lastmodified': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'sortorder': "'asc'", // String | Order of search results: asc or desc
  'limit': 50, // Number | Number of results per page
  'schemeName': "schemeName_example", // String | 
  'version': 56 // Number | 
};
apiInstance.apiV20DatabaseSchemesGet(database, opts, (error, data, response) => {
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
 **barcode** | [**[String]**](String.md)| Unique barcode for Strain records, &lt;database prefix&gt;_&lt;ID code&gt; e.g. SAL_AA0001AA | [optional] 
 **orderby** | **String**| Field to order by. Default: barcode | [optional] [default to &#39;barcode&#39;]
 **offset** | **Number**| Cursor position in results | [optional] [default to 0]
 **label** | **String**|  | [optional] 
 **onlyFields** | [**[String]**](String.md)|  | [optional] 
 **created** | **Date**|  | [optional] 
 **lastmodified** | **Date**|  | [optional] 
 **sortorder** | **String**| Order of search results: asc or desc | [optional] [default to &#39;asc&#39;]
 **limit** | **Number**| Number of results per page | [optional] [default to 50]
 **schemeName** | **String**|  | [optional] 
 **version** | **Number**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

