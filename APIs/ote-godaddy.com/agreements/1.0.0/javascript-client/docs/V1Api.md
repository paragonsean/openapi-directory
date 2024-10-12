# OpenapiJsClient.V1Api

All URIs are relative to *http://api.ote-godaddy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](V1Api.md#get) | **GET** /v1/agreements | Retrieve Legal Agreements for provided agreements keys



## get

> [LegalAgreement] get(keys, opts)

Retrieve Legal Agreements for provided agreements keys

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V1Api();
let keys = ["null"]; // [String] | Keys for Agreements whose details are to be retrieved
let opts = {
  'xPrivateLabelId': 56, // Number | PrivateLabelId to operate as, if different from JWT
  'xMarketId': "'en-US'" // String | Unique identifier of the Market used to retrieve/translate Legal Agreements
};
apiInstance.get(keys, opts, (error, data, response) => {
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
 **keys** | [**[String]**](String.md)| Keys for Agreements whose details are to be retrieved | 
 **xPrivateLabelId** | **Number**| PrivateLabelId to operate as, if different from JWT | [optional] 
 **xMarketId** | **String**| Unique identifier of the Market used to retrieve/translate Legal Agreements | [optional] [default to &#39;en-US&#39;]

### Return type

[**[LegalAgreement]**](LegalAgreement.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/javascript, application/json, application/xml, text/javascript, text/xml

