# GeodesystemsCom443.ServiceMediaTabularExtractsheetApi

All URIs are relative to *https://geodesystems.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mediaTabularExtractsheet**](ServiceMediaTabularExtractsheetApi.md#mediaTabularExtractsheet) | **GET** /repository/entry/show | API for Extract sheets



## mediaTabularExtractsheet

> mediaTabularExtractsheet(output, entryid, opts)

API for Extract sheets

API to call: Extract sheets

### Example

```javascript
import GeodesystemsCom443 from 'geodesystems_com443';

let apiInstance = new GeodesystemsCom443.ServiceMediaTabularExtractsheetApi();
let output = "'media_tabular_extractsheet'"; // String | Output type  -don't change
let entryid = "entryid_example"; // String | Entry ID
let opts = {
  'arg1': "arg1_example" // String | Sheets
};
apiInstance.mediaTabularExtractsheet(output, entryid, opts, (error, data, response) => {
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
 **output** | **String**| Output type  -don&#39;t change | [default to &#39;media_tabular_extractsheet&#39;]
 **entryid** | **String**| Entry ID | 
 **arg1** | **String**| Sheets | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

