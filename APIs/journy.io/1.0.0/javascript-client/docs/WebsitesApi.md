# DeveloperDocumentation.WebsitesApi

All URIs are relative to *https://api.journy.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getTrackingSnippet**](WebsitesApi.md#getTrackingSnippet) | **GET** /tracking/snippet | Get snippet for a website



## getTrackingSnippet

> GetTrackingSnippet200Response getTrackingSnippet(domain)

Get snippet for a website

Endpoint used to get a snippet for a website.

### Example

```javascript
import DeveloperDocumentation from 'developer_documentation';

let apiInstance = new DeveloperDocumentation.WebsitesApi();
let domain = "domain_example"; // String | The domain you want to receive a snippet for
apiInstance.getTrackingSnippet(domain, (error, data, response) => {
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
 **domain** | **String**| The domain you want to receive a snippet for | 

### Return type

[**GetTrackingSnippet200Response**](GetTrackingSnippet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

