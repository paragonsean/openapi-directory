# WireMock.NearMissesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adminNearMissesRequestPatternPost**](NearMissesApi.md#adminNearMissesRequestPatternPost) | **POST** /__admin/near-misses/request-pattern | Find near misses matching request pattern
[**adminNearMissesRequestPost**](NearMissesApi.md#adminNearMissesRequestPost) | **POST** /__admin/near-misses/request | Find near misses matching specific request
[**adminRequestsUnmatchedNearMissesGet**](NearMissesApi.md#adminRequestsUnmatchedNearMissesGet) | **GET** /__admin/requests/unmatched/near-misses | 



## adminNearMissesRequestPatternPost

> AdminNearMissesRequestPost200Response adminNearMissesRequestPatternPost(adminMappingsGet200ResponseMappingsInnerRequest)

Find near misses matching request pattern

Find at most 3 near misses for closest logged requests to the specified request pattern

### Example

```javascript
import WireMock from 'wire_mock';

let apiInstance = new WireMock.NearMissesApi();
let adminMappingsGet200ResponseMappingsInnerRequest = {"headers":{"Content-Type":{"matches":".*/xml"}},"method":"POST","url":"/resource"}; // AdminMappingsGet200ResponseMappingsInnerRequest | 
apiInstance.adminNearMissesRequestPatternPost(adminMappingsGet200ResponseMappingsInnerRequest, (error, data, response) => {
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
 **adminMappingsGet200ResponseMappingsInnerRequest** | [**AdminMappingsGet200ResponseMappingsInnerRequest**](AdminMappingsGet200ResponseMappingsInnerRequest.md)|  | 

### Return type

[**AdminNearMissesRequestPost200Response**](AdminNearMissesRequestPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## adminNearMissesRequestPost

> AdminNearMissesRequestPost200Response adminNearMissesRequestPost(adminNearMissesRequestPostRequest)

Find near misses matching specific request

Find at most 3 near misses for closest stub mappings to the specified request

### Example

```javascript
import WireMock from 'wire_mock';

let apiInstance = new WireMock.NearMissesApi();
let adminNearMissesRequestPostRequest = {"absoluteUrl":"http://localhost:8080/actual","body":"","bodyAsBase64":"","browserProxyRequest":false,"clientIp":"0:0:0:0:0:0:0:1","cookies":{},"headers":{"Accept":"*/*","Host":"localhost:8080","User-Agent":"curl/7.30.0"},"loggedDate":1467402464520,"loggedDateString":"2016-07-01T19:47:44Z","method":"GET","url":"/actual"}; // AdminNearMissesRequestPostRequest | 
apiInstance.adminNearMissesRequestPost(adminNearMissesRequestPostRequest, (error, data, response) => {
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
 **adminNearMissesRequestPostRequest** | [**AdminNearMissesRequestPostRequest**](AdminNearMissesRequestPostRequest.md)|  | 

### Return type

[**AdminNearMissesRequestPost200Response**](AdminNearMissesRequestPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## adminRequestsUnmatchedNearMissesGet

> AdminNearMissesRequestPost200Response adminRequestsUnmatchedNearMissesGet()



Retrieve near-misses for all unmatched requests

### Example

```javascript
import WireMock from 'wire_mock';

let apiInstance = new WireMock.NearMissesApi();
apiInstance.adminRequestsUnmatchedNearMissesGet((error, data, response) => {
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

[**AdminNearMissesRequestPost200Response**](AdminNearMissesRequestPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

