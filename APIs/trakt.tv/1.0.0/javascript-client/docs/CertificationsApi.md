# TraktApi.CertificationsApi

All URIs are relative to *https://api.trakt.tv*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCertifications**](CertificationsApi.md#getCertifications) | **GET** /certifications/{type} | Get certifications



## getCertifications

> getCertifications(type, opts)

Get certifications

Get a list of all certifications, including names, slugs, and descriptions.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.CertificationsApi();
let type = "movies"; // String | 
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getCertifications(type, opts, (error, data, response) => {
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
 **type** | **String**|  | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

