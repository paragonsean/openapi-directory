# EnterobaseApi.LookupApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV20LookupBarcodeGet**](LookupApi.md#apiV20LookupBarcodeGet) | **GET** /api/v2.0/lookup/{barcode} | 
[**apiV20LookupBarcodePost**](LookupApi.md#apiV20LookupBarcodePost) | **POST** /api/v2.0/lookup/{barcode} | 
[**apiV20LookupGet**](LookupApi.md#apiV20LookupGet) | **GET** /api/v2.0/lookup | 



## apiV20LookupBarcodeGet

> apiV20LookupBarcodeGet(barcode)



Generic endpoint for lookup of barcodes

### Example

```javascript
import EnterobaseApi from 'enterobase_api';

let apiInstance = new EnterobaseApi.LookupApi();
let barcode = "barcode_example"; // String | Unique barcode for Traces records, <database prefix>_<ID code>_<Table code> e.g. SAL_AA0001AA_ST
apiInstance.apiV20LookupBarcodeGet(barcode, (error, data, response) => {
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
 **barcode** | **String**| Unique barcode for Traces records, &lt;database prefix&gt;_&lt;ID code&gt;_&lt;Table code&gt; e.g. SAL_AA0001AA_ST | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiV20LookupBarcodePost

> apiV20LookupBarcodePost(barcode, opts)



Generic endpoint for lookup of barcodes

### Example

```javascript
import EnterobaseApi from 'enterobase_api';

let apiInstance = new EnterobaseApi.LookupApi();
let barcode = "barcode_example"; // String | Unique barcode for Traces records, <database prefix>_<ID code>_<Table code> e.g. SAL_AA0001AA_ST
let opts = {
  'apiV20LookupBarcodePostRequest': new EnterobaseApi.ApiV20LookupBarcodePostRequest() // ApiV20LookupBarcodePostRequest | 
};
apiInstance.apiV20LookupBarcodePost(barcode, opts, (error, data, response) => {
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
 **barcode** | **String**| Unique barcode for Traces records, &lt;database prefix&gt;_&lt;ID code&gt;_&lt;Table code&gt; e.g. SAL_AA0001AA_ST | 
 **apiV20LookupBarcodePostRequest** | [**ApiV20LookupBarcodePostRequest**](ApiV20LookupBarcodePostRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## apiV20LookupGet

> apiV20LookupGet(opts)



Generic endpoint for lookup list of barcodes

### Example

```javascript
import EnterobaseApi from 'enterobase_api';

let apiInstance = new EnterobaseApi.LookupApi();
let opts = {
  'barcode': "barcode_example" // String | Unique barcode for Traces records, <database prefix>_<ID code>_<Table code> e.g. SAL_AA0001AA_ST
};
apiInstance.apiV20LookupGet(opts, (error, data, response) => {
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
 **barcode** | **String**| Unique barcode for Traces records, &lt;database prefix&gt;_&lt;ID code&gt;_&lt;Table code&gt; e.g. SAL_AA0001AA_ST | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

