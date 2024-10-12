# SalesLoftPlatform.CadenceImportsApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2CadenceImportsJsonPost**](CadenceImportsApi.md#v2CadenceImportsJsonPost) | **POST** /v2/cadence_imports.json | Import cadences from JSON



## v2CadenceImportsJsonPost

> CadenceImport v2CadenceImportsJsonPost(opts)

Import cadences from JSON

New cadences can be created or steps can be imported onto existing cadences which do not have steps. &lt;a href&#x3D;\&quot;/cadence-imports.html\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;Visit here for more details&lt;/a&gt;. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.CadenceImportsApi();
let opts = {
  'cadenceContent': {key: null}, // Object | Import data for cadence
  'settings': {key: null}, // Object | Settings for a cadence
  'sharingSettings': {key: null} // Object | The shared settings for a cadence
};
apiInstance.v2CadenceImportsJsonPost(opts, (error, data, response) => {
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
 **cadenceContent** | [**Object**](Object.md)| Import data for cadence | [optional] 
 **settings** | [**Object**](Object.md)| Settings for a cadence | [optional] 
 **sharingSettings** | [**Object**](Object.md)| The shared settings for a cadence | [optional] 

### Return type

[**CadenceImport**](CadenceImport.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: */*

