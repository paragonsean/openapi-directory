# BcGeographicalNamesWebServiceRestApi.NameAuthorityApi

All URIs are relative to *https://apps.gov.bc.ca/pub/bcgnws*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nameAuthoritiesGet**](NameAuthorityApi.md#nameAuthoritiesGet) | **GET** /nameAuthorities | Get all name authorities



## nameAuthoritiesGet

> nameAuthoritiesGet(outputFormat)

Get all name authorities

Gets a list of all name authorities responsible for naming decisions of the geographical names in the BC Geographical Names Information System (BCGNIS)

### Example

```javascript
import BcGeographicalNamesWebServiceRestApi from 'bc_geographical_names_web_service_rest_api';

let apiInstance = new BcGeographicalNamesWebServiceRestApi.NameAuthorityApi();
let outputFormat = "json"; // String | The format of the output.
apiInstance.nameAuthoritiesGet(outputFormat, (error, data, response) => {
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
 **outputFormat** | **String**| The format of the output. | [default to &#39;json&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

