# EnterobaseApi.AssembliesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV20DatabaseAssembliesBarcodeGet**](AssembliesApi.md#apiV20DatabaseAssembliesBarcodeGet) | **GET** /api/v2.0/{database}/assemblies/{barcode} | 
[**apiV20DatabaseAssembliesBarcodePost**](AssembliesApi.md#apiV20DatabaseAssembliesBarcodePost) | **POST** /api/v2.0/{database}/assemblies/{barcode} | 
[**apiV20DatabaseAssembliesBarcodePut**](AssembliesApi.md#apiV20DatabaseAssembliesBarcodePut) | **PUT** /api/v2.0/{database}/assemblies/{barcode} | 
[**apiV20DatabaseAssembliesGet**](AssembliesApi.md#apiV20DatabaseAssembliesGet) | **GET** /api/v2.0/{database}/assemblies | 



## apiV20DatabaseAssembliesBarcodeGet

> apiV20DatabaseAssembliesBarcodeGet(database, barcode, opts)



Genome assemblies

### Example

```javascript
import EnterobaseApi from 'enterobase_api';

let apiInstance = new EnterobaseApi.AssembliesApi();
let database = "database_example"; // String | Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
let barcode = "barcode_example"; // String | Unique barcode for Traces records, <database prefix>_<ID code>_AS e.g. SAL_AA0001AA_AS
let opts = {
  'apiV20DatabaseAssembliesBarcodeGetRequest': new EnterobaseApi.ApiV20DatabaseAssembliesBarcodeGetRequest() // ApiV20DatabaseAssembliesBarcodeGetRequest | 
};
apiInstance.apiV20DatabaseAssembliesBarcodeGet(database, barcode, opts, (error, data, response) => {
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
 **barcode** | **String**| Unique barcode for Traces records, &lt;database prefix&gt;_&lt;ID code&gt;_AS e.g. SAL_AA0001AA_AS | 
 **apiV20DatabaseAssembliesBarcodeGetRequest** | [**ApiV20DatabaseAssembliesBarcodeGetRequest**](ApiV20DatabaseAssembliesBarcodeGetRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## apiV20DatabaseAssembliesBarcodePost

> apiV20DatabaseAssembliesBarcodePost(database, barcode, opts)



Genome assemblies

### Example

```javascript
import EnterobaseApi from 'enterobase_api';

let apiInstance = new EnterobaseApi.AssembliesApi();
let database = "database_example"; // String | Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
let barcode = "barcode_example"; // String | Unique barcode for Traces records, <database prefix>_<ID code>_AS e.g. SAL_AA0001AA_AS
let opts = {
  'apiV20DatabaseAssembliesBarcodeGetRequest': new EnterobaseApi.ApiV20DatabaseAssembliesBarcodeGetRequest() // ApiV20DatabaseAssembliesBarcodeGetRequest | 
};
apiInstance.apiV20DatabaseAssembliesBarcodePost(database, barcode, opts, (error, data, response) => {
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
 **barcode** | **String**| Unique barcode for Traces records, &lt;database prefix&gt;_&lt;ID code&gt;_AS e.g. SAL_AA0001AA_AS | 
 **apiV20DatabaseAssembliesBarcodeGetRequest** | [**ApiV20DatabaseAssembliesBarcodeGetRequest**](ApiV20DatabaseAssembliesBarcodeGetRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## apiV20DatabaseAssembliesBarcodePut

> apiV20DatabaseAssembliesBarcodePut(database, barcode, opts)



Genome assemblies

### Example

```javascript
import EnterobaseApi from 'enterobase_api';

let apiInstance = new EnterobaseApi.AssembliesApi();
let database = "database_example"; // String | Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
let barcode = "barcode_example"; // String | Unique barcode for Traces records, <database prefix>_<ID code>_AS e.g. SAL_AA0001AA_AS
let opts = {
  'apiV20DatabaseAssembliesBarcodeGetRequest': new EnterobaseApi.ApiV20DatabaseAssembliesBarcodeGetRequest() // ApiV20DatabaseAssembliesBarcodeGetRequest | 
};
apiInstance.apiV20DatabaseAssembliesBarcodePut(database, barcode, opts, (error, data, response) => {
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
 **barcode** | **String**| Unique barcode for Traces records, &lt;database prefix&gt;_&lt;ID code&gt;_AS e.g. SAL_AA0001AA_AS | 
 **apiV20DatabaseAssembliesBarcodeGetRequest** | [**ApiV20DatabaseAssembliesBarcodeGetRequest**](ApiV20DatabaseAssembliesBarcodeGetRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## apiV20DatabaseAssembliesGet

> apiV20DatabaseAssembliesGet(database, opts)



Genome assemblies

### Example

```javascript
import EnterobaseApi from 'enterobase_api';

let apiInstance = new EnterobaseApi.AssembliesApi();
let database = "database_example"; // String | Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
let opts = {
  'n50': 56, // Number | 
  'barcode': ["null"], // [String] | Unique barcode for Traces records, <database prefix>_<ID code>_AS e.g. SAL_AA0001AA_AS
  'orderby': "'barcode'", // String | Field to order by. Default: barcode
  'offset': 0, // Number | Cursor position in results
  'assemblyStatus': "assemblyStatus_example", // String | 
  'uberstrain': "uberstrain_example", // String | 
  'topSpecies': "topSpecies_example", // String | 
  'onlyFields': ["null"], // [String] | 
  'reldate': 56, // Number | 
  'sortorder': "'asc'", // String | Order of search results: asc or desc
  'limit': 50, // Number | Number of results per page
  'version': 56 // Number | 
};
apiInstance.apiV20DatabaseAssembliesGet(database, opts, (error, data, response) => {
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
 **n50** | **Number**|  | [optional] 
 **barcode** | [**[String]**](String.md)| Unique barcode for Traces records, &lt;database prefix&gt;_&lt;ID code&gt;_AS e.g. SAL_AA0001AA_AS | [optional] 
 **orderby** | **String**| Field to order by. Default: barcode | [optional] [default to &#39;barcode&#39;]
 **offset** | **Number**| Cursor position in results | [optional] [default to 0]
 **assemblyStatus** | **String**|  | [optional] 
 **uberstrain** | **String**|  | [optional] 
 **topSpecies** | **String**|  | [optional] 
 **onlyFields** | [**[String]**](String.md)|  | [optional] 
 **reldate** | **Number**|  | [optional] 
 **sortorder** | **String**| Order of search results: asc or desc | [optional] [default to &#39;asc&#39;]
 **limit** | **Number**| Number of results per page | [optional] [default to 50]
 **version** | **Number**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

