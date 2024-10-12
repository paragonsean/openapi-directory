# EnterobaseApi.TracesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV20DatabaseTracesBarcodeGet**](TracesApi.md#apiV20DatabaseTracesBarcodeGet) | **GET** /api/v2.0/{database}/traces/{barcode} | 
[**apiV20DatabaseTracesBarcodePost**](TracesApi.md#apiV20DatabaseTracesBarcodePost) | **POST** /api/v2.0/{database}/traces/{barcode} | 
[**apiV20DatabaseTracesBarcodePut**](TracesApi.md#apiV20DatabaseTracesBarcodePut) | **PUT** /api/v2.0/{database}/traces/{barcode} | 
[**apiV20DatabaseTracesGet**](TracesApi.md#apiV20DatabaseTracesGet) | **GET** /api/v2.0/{database}/traces | 



## apiV20DatabaseTracesBarcodeGet

> apiV20DatabaseTracesBarcodeGet(database, barcode, opts)



Traces (sequence-reads) metadata

### Example

```javascript
import EnterobaseApi from 'enterobase_api';

let apiInstance = new EnterobaseApi.TracesApi();
let database = "database_example"; // String | Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
let barcode = "barcode_example"; // String | Unique barcode for Traces records, <database prefix>_<ID code>_TR e.g. SAL_AA0001AA_TR
let opts = {
  'apiV20DatabaseTracesBarcodeGetRequest': new EnterobaseApi.ApiV20DatabaseTracesBarcodeGetRequest() // ApiV20DatabaseTracesBarcodeGetRequest | 
};
apiInstance.apiV20DatabaseTracesBarcodeGet(database, barcode, opts, (error, data, response) => {
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
 **barcode** | **String**| Unique barcode for Traces records, &lt;database prefix&gt;_&lt;ID code&gt;_TR e.g. SAL_AA0001AA_TR | 
 **apiV20DatabaseTracesBarcodeGetRequest** | [**ApiV20DatabaseTracesBarcodeGetRequest**](ApiV20DatabaseTracesBarcodeGetRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## apiV20DatabaseTracesBarcodePost

> apiV20DatabaseTracesBarcodePost(database, barcode, opts)



Traces (sequence-reads) metadata

### Example

```javascript
import EnterobaseApi from 'enterobase_api';

let apiInstance = new EnterobaseApi.TracesApi();
let database = "database_example"; // String | Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
let barcode = "barcode_example"; // String | Unique barcode for Traces records, <database prefix>_<ID code>_TR e.g. SAL_AA0001AA_TR
let opts = {
  'apiV20DatabaseTracesBarcodeGetRequest': new EnterobaseApi.ApiV20DatabaseTracesBarcodeGetRequest() // ApiV20DatabaseTracesBarcodeGetRequest | 
};
apiInstance.apiV20DatabaseTracesBarcodePost(database, barcode, opts, (error, data, response) => {
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
 **barcode** | **String**| Unique barcode for Traces records, &lt;database prefix&gt;_&lt;ID code&gt;_TR e.g. SAL_AA0001AA_TR | 
 **apiV20DatabaseTracesBarcodeGetRequest** | [**ApiV20DatabaseTracesBarcodeGetRequest**](ApiV20DatabaseTracesBarcodeGetRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## apiV20DatabaseTracesBarcodePut

> apiV20DatabaseTracesBarcodePut(database, barcode, opts)



Traces (sequence-reads) metadata

### Example

```javascript
import EnterobaseApi from 'enterobase_api';

let apiInstance = new EnterobaseApi.TracesApi();
let database = "database_example"; // String | Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
let barcode = "barcode_example"; // String | Unique barcode for Traces records, <database prefix>_<ID code>_TR e.g. SAL_AA0001AA_TR
let opts = {
  'apiV20DatabaseTracesBarcodeGetRequest': new EnterobaseApi.ApiV20DatabaseTracesBarcodeGetRequest() // ApiV20DatabaseTracesBarcodeGetRequest | 
};
apiInstance.apiV20DatabaseTracesBarcodePut(database, barcode, opts, (error, data, response) => {
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
 **barcode** | **String**| Unique barcode for Traces records, &lt;database prefix&gt;_&lt;ID code&gt;_TR e.g. SAL_AA0001AA_TR | 
 **apiV20DatabaseTracesBarcodeGetRequest** | [**ApiV20DatabaseTracesBarcodeGetRequest**](ApiV20DatabaseTracesBarcodeGetRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## apiV20DatabaseTracesGet

> apiV20DatabaseTracesGet(database, opts)



Traces (sequence-reads) metadata

### Example

```javascript
import EnterobaseApi from 'enterobase_api';

let apiInstance = new EnterobaseApi.TracesApi();
let database = "database_example"; // String | Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
let opts = {
  'barcode': ["null"], // [String] | Unique barcode for Traces records, <database prefix>_<ID code>_TR e.g. SAL_AA0001AA_TR
  'orderby': "'barcode'", // String | Field to order by. Default: barcode
  'offset': 0, // Number | Cursor position in results
  'onlyFields': ["null"], // [String] | 
  'sortorder': "'asc'", // String | Order of search results: asc or desc
  'limit': 50 // Number | Number of results per page
};
apiInstance.apiV20DatabaseTracesGet(database, opts, (error, data, response) => {
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
 **barcode** | [**[String]**](String.md)| Unique barcode for Traces records, &lt;database prefix&gt;_&lt;ID code&gt;_TR e.g. SAL_AA0001AA_TR | [optional] 
 **orderby** | **String**| Field to order by. Default: barcode | [optional] [default to &#39;barcode&#39;]
 **offset** | **Number**| Cursor position in results | [optional] [default to 0]
 **onlyFields** | [**[String]**](String.md)|  | [optional] 
 **sortorder** | **String**| Order of search results: asc or desc | [optional] [default to &#39;asc&#39;]
 **limit** | **Number**| Number of results per page | [optional] [default to 50]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

