# ClickMeterApi.ClickStreamApi

All URIs are relative to *http://apiv2.clickmeter.com:80*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clickStreamGet**](ClickStreamApi.md#clickStreamGet) | **GET** /clickstream | Retrieve the latest list of events of this account. Limited to last 100.



## clickStreamGet

> ApiCoreResponsesEntitiesResponseApiCoreDtoClickStreamHit clickStreamGet(opts)

Retrieve the latest list of events of this account. Limited to last 100.

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.ClickStreamApi();
let opts = {
  'group': 789, // Number | Filter by this group id (mutually exclusive with \"datapoint\" and \"conversion\")
  'datapoint': 789, // Number | Filter by this datapoint id (mutually exclusive with \"group\" and \"conversion\")
  'conversion': 789, // Number | Filter by this conversion id (mutually exclusive with \"datapoint\" and \"group\")
  'pageSize': 50, // Number | Limit results to this number
  'filter': "filter_example" // String | Filter event type (\"spiders\"/\"uniques\"/\"nonuniques\"/\"conversions\")
};
apiInstance.clickStreamGet(opts, (error, data, response) => {
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
 **group** | **Number**| Filter by this group id (mutually exclusive with \&quot;datapoint\&quot; and \&quot;conversion\&quot;) | [optional] 
 **datapoint** | **Number**| Filter by this datapoint id (mutually exclusive with \&quot;group\&quot; and \&quot;conversion\&quot;) | [optional] 
 **conversion** | **Number**| Filter by this conversion id (mutually exclusive with \&quot;datapoint\&quot; and \&quot;group\&quot;) | [optional] 
 **pageSize** | **Number**| Limit results to this number | [optional] [default to 50]
 **filter** | **String**| Filter event type (\&quot;spiders\&quot;/\&quot;uniques\&quot;/\&quot;nonuniques\&quot;/\&quot;conversions\&quot;) | [optional] 

### Return type

[**ApiCoreResponsesEntitiesResponseApiCoreDtoClickStreamHit**](ApiCoreResponsesEntitiesResponseApiCoreDtoClickStreamHit.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

