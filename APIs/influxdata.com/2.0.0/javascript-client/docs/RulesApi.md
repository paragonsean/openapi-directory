# InfluxOssApiService.RulesApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNotificationRulesIDQuery**](RulesApi.md#getNotificationRulesIDQuery) | **GET** /notificationRules/{ruleID}/query | Retrieve a notification rule query



## getNotificationRulesIDQuery

> FluxResponse getNotificationRulesIDQuery(ruleID, opts)

Retrieve a notification rule query

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.RulesApi();
let ruleID = "ruleID_example"; // String | The notification rule ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getNotificationRulesIDQuery(ruleID, opts, (error, data, response) => {
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
 **ruleID** | **String**| The notification rule ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**FluxResponse**](FluxResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

