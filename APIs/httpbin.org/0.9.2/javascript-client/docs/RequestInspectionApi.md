# HttpbinOrg.RequestInspectionApi

All URIs are relative to *https://httpbin.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**headersGet**](RequestInspectionApi.md#headersGet) | **GET** /headers | Return the incoming request&#39;s HTTP headers.
[**ipGet**](RequestInspectionApi.md#ipGet) | **GET** /ip | Returns the requester&#39;s IP Address.
[**userAgentGet**](RequestInspectionApi.md#userAgentGet) | **GET** /user-agent | Return the incoming requests&#39;s User-Agent header.



## headersGet

> headersGet()

Return the incoming request&#39;s HTTP headers.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.RequestInspectionApi();
apiInstance.headersGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## ipGet

> ipGet()

Returns the requester&#39;s IP Address.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.RequestInspectionApi();
apiInstance.ipGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## userAgentGet

> userAgentGet()

Return the incoming requests&#39;s User-Agent header.

### Example

```javascript
import HttpbinOrg from 'httpbin_org';

let apiInstance = new HttpbinOrg.RequestInspectionApi();
apiInstance.userAgentGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

