# UuidGenerationApi.UUIDGenerationApi

All URIs are relative to *https://api.fungenerators.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**uuidGet**](UUIDGenerationApi.md#uuidGet) | **GET** /uuid | 
[**uuidVersionVersionGet**](UUIDGenerationApi.md#uuidVersionVersionGet) | **GET** /uuid/version/{version} | 



## uuidGet

> uuidGet(opts)



Generate a random UUID (v4).

### Example

```javascript
import UuidGenerationApi from 'uuid_generation_api';
let defaultClient = UuidGenerationApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new UuidGenerationApi.UUIDGenerationApi();
let opts = {
  'count': 56 // Number | Number of UUID's to generate (defaults to 1)
};
apiInstance.uuidGet(opts, (error, data, response) => {
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
 **count** | **Number**| Number of UUID&#39;s to generate (defaults to 1) | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## uuidVersionVersionGet

> uuidVersionVersionGet(version, opts)



Generate a random UUID (v4).

### Example

```javascript
import UuidGenerationApi from 'uuid_generation_api';
let defaultClient = UuidGenerationApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new UuidGenerationApi.UUIDGenerationApi();
let version = 56; // Number | Version of the UUID spec to use. (0-5), Use '0' for nil (00000000-0000-0000-0000-000000000000) UUID.
let opts = {
  'count': 56, // Number | Number of UUID's to generate (defaults to 1)
  'type': "type_example", // String | For v3 and v5 of UUID Spec you can supply the type (dns/url/oid/x500/nil).
  'text': "text_example" // String | For v3 and v5 of UUID Spec supply the text value for the type specified dns/url/oid/x500/nil. For example specify a dns/domain string if the type is \"dns\"
};
apiInstance.uuidVersionVersionGet(version, opts, (error, data, response) => {
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
 **version** | **Number**| Version of the UUID spec to use. (0-5), Use &#39;0&#39; for nil (00000000-0000-0000-0000-000000000000) UUID. | 
 **count** | **Number**| Number of UUID&#39;s to generate (defaults to 1) | [optional] 
 **type** | **String**| For v3 and v5 of UUID Spec you can supply the type (dns/url/oid/x500/nil). | [optional] 
 **text** | **String**| For v3 and v5 of UUID Spec supply the text value for the type specified dns/url/oid/x500/nil. For example specify a dns/domain string if the type is \&quot;dns\&quot; | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

