# Superset.OpenApiApi

All URIs are relative to *http://superset.apache.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**openapiVersionOpenapiGet**](OpenApiApi.md#openapiVersionOpenapiGet) | **GET** /openapi/{version}/_openapi | 



## openapiVersionOpenapiGet

> Object openapiVersionOpenapiGet(version)



Get the OpenAPI spec for a specific API version

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.OpenApiApi();
let version = "version_example"; // String | 
apiInstance.openapiVersionOpenapiGet(version, (error, data, response) => {
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
 **version** | **String**|  | 

### Return type

**Object**

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

