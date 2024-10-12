# EveSwaggerInterface.IncursionsApi

All URIs are relative to *https://esi.evetech.net/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getIncursions**](IncursionsApi.md#getIncursions) | **GET** /incursions/ | List incursions



## getIncursions

> [GetIncursions200Ok] getIncursions(opts)

List incursions

Return a list of current incursions  --- Alternate route: &#x60;/dev/incursions/&#x60;  Alternate route: &#x60;/legacy/incursions/&#x60;  Alternate route: &#x60;/v1/incursions/&#x60;  --- This route is cached for up to 300 seconds

### Example

```javascript
import EveSwaggerInterface from 'eve_swagger_interface';

let apiInstance = new EveSwaggerInterface.IncursionsApi();
let opts = {
  'datasource': "'tranquility'", // String | The server name you would like data from
  'ifNoneMatch': "ifNoneMatch_example" // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
};
apiInstance.getIncursions(opts, (error, data, response) => {
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
 **datasource** | **String**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **ifNoneMatch** | **String**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**[GetIncursions200Ok]**](GetIncursions200Ok.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

