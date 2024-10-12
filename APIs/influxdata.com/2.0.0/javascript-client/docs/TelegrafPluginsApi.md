# InfluxOssApiService.TelegrafPluginsApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getTelegrafPlugins**](TelegrafPluginsApi.md#getTelegrafPlugins) | **GET** /telegraf/plugins | List all Telegraf plugins



## getTelegrafPlugins

> TelegrafPlugins getTelegrafPlugins(opts)

List all Telegraf plugins

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TelegrafPluginsApi();
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}", // String | OpenTracing span context
  'type': "type_example" // String | The type of plugin desired.
};
apiInstance.getTelegrafPlugins(opts, (error, data, response) => {
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
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 
 **type** | **String**| The type of plugin desired. | [optional] 

### Return type

[**TelegrafPlugins**](TelegrafPlugins.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

