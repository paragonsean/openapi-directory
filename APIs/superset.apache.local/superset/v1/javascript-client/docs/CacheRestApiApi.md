# Superset.CacheRestApiApi

All URIs are relative to *http://superset.apache.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cachekeyInvalidatePost**](CacheRestApiApi.md#cachekeyInvalidatePost) | **POST** /cachekey/invalidate | 



## cachekeyInvalidatePost

> cachekeyInvalidatePost(cacheInvalidationRequestSchema)



Takes a list of datasources, finds the associated cache records and invalidates them and removes the database records

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.CacheRestApiApi();
let cacheInvalidationRequestSchema = new Superset.CacheInvalidationRequestSchema(); // CacheInvalidationRequestSchema | A list of datasources uuid or the tuples of database and datasource names
apiInstance.cachekeyInvalidatePost(cacheInvalidationRequestSchema, (error, data, response) => {
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
 **cacheInvalidationRequestSchema** | [**CacheInvalidationRequestSchema**](CacheInvalidationRequestSchema.md)| A list of datasources uuid or the tuples of database and datasource names | 

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

