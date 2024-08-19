# LgtmApiSpecification.APIRootApi

All URIs are relative to *https://lgtm.com/api/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSpec**](APIRootApi.md#getSpec) | **GET** /openapi | API specification
[**getVersion**](APIRootApi.md#getVersion) | **GET** / | Version information



## getSpec

> Object getSpec()

API specification

Get the specification of this API in [OpenAPI](https://github.com/OAI/OpenAPI-Specification) format. This endpoint does not require an access token. This makes it easier for you to use the specification with third-party tools.

### Example

```javascript
import LgtmApiSpecification from 'lgtm_api_specification';

let apiInstance = new LgtmApiSpecification.APIRootApi();
apiInstance.getSpec((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVersion

> Version getVersion()

Version information

Get the version information of this API.

### Example

```javascript
import LgtmApiSpecification from 'lgtm_api_specification';
let defaultClient = LgtmApiSpecification.ApiClient.instance;
// Configure Bearer access token for authorization: access-token
let access-token = defaultClient.authentications['access-token'];
access-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new LgtmApiSpecification.APIRootApi();
apiInstance.getVersion((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**Version**](Version.md)

### Authorization

[access-token](../README.md#access-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

