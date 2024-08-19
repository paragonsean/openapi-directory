# SnykApi.MonitorApi

All URIs are relative to *https://api.snyk.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**monitorDepGraph**](MonitorApi.md#monitorDepGraph) | **POST** /monitor/dep-graph | Monitor Dep Graph



## monitorDepGraph

> monitorDepGraph(opts)

Monitor Dep Graph

Use this endpoint to monitor a [DepGraph data object](https://github.com/snyk/dep-graph#depgraphdata).

### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.MonitorApi();
let opts = {
  'org': "9695cbb1-3a87-4d6f-8ae1-61a1c37ee9f7", // String | The organization to test the package with. See \"The Snyk organization for a request\" above.
  'monitorDepGraphRequest': new SnykApi.MonitorDepGraphRequest() // MonitorDepGraphRequest | 
};
apiInstance.monitorDepGraph(opts, (error, data, response) => {
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
 **org** | **String**| The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. | [optional] 
 **monitorDepGraphRequest** | [**MonitorDepGraphRequest**](MonitorDepGraphRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8

