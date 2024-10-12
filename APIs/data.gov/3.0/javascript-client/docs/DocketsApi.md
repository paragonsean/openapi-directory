# RegulationsGov.DocketsApi

All URIs are relative to *https://api.data.gov/regulations/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**docket**](DocketsApi.md#docket) | **GET** /docket.{response_format} | Returns Docket information



## docket

> docket(responseFormat, docketId)

Returns Docket information

### Example

```javascript
import RegulationsGov from 'regulations_gov';
let defaultClient = RegulationsGov.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new RegulationsGov.DocketsApi();
let responseFormat = "'json'"; // String | Format
let docketId = "'EPA-HQ-OAR-2011-0028'"; // String | Docket ID
apiInstance.docket(responseFormat, docketId, (error, data, response) => {
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
 **responseFormat** | **String**| Format | [default to &#39;json&#39;]
 **docketId** | **String**| Docket ID | [default to &#39;EPA-HQ-OAR-2011-0028&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

