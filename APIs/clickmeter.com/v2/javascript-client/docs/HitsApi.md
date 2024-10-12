# ClickMeterApi.HitsApi

All URIs are relative to *http://apiv2.clickmeter.com:80*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hitsGetHits**](HitsApi.md#hitsGetHits) | **GET** /hits | Retrieve the list of events related to this account.



## hitsGetHits

> ApiCoreDtoClickStreamHitListPage hitsGetHits(timeframe, opts)

Retrieve the list of events related to this account.

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.HitsApi();
let timeframe = "timeframe_example"; // String | Timeframe of the request. See list at $timeframeList
let opts = {
  'limit': 56, // Number | Limit results to this number
  'offset': "offset_example", // String | Offset where to start from (it's the lastKey field in the response object)
  'fromDay': "fromDay_example", // String | If using a \"custom\" timeFrame you can specify the starting day (YYYYMMDD)
  'toDay': "toDay_example", // String | If using a \"custom\" timeFrame you can specify the ending day (YYYYMMDD)
  'filter': "filter_example" // String | Filter event type (\"spiders\"/\"uniques\"/\"nonuniques\"/\"conversions\")
};
apiInstance.hitsGetHits(timeframe, opts, (error, data, response) => {
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
 **timeframe** | **String**| Timeframe of the request. See list at $timeframeList | 
 **limit** | **Number**| Limit results to this number | [optional] 
 **offset** | **String**| Offset where to start from (it&#39;s the lastKey field in the response object) | [optional] 
 **fromDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the starting day (YYYYMMDD) | [optional] 
 **toDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the ending day (YYYYMMDD) | [optional] 
 **filter** | **String**| Filter event type (\&quot;spiders\&quot;/\&quot;uniques\&quot;/\&quot;nonuniques\&quot;/\&quot;conversions\&quot;) | [optional] 

### Return type

[**ApiCoreDtoClickStreamHitListPage**](ApiCoreDtoClickStreamHitListPage.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

