# WaybackApi.DefaultApi

All URIs are relative to *https://api.archive.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**waybackV1AvailableGet**](DefaultApi.md#waybackV1AvailableGet) | **GET** /wayback/v1/available | 
[**waybackV1AvailablePost**](DefaultApi.md#waybackV1AvailablePost) | **POST** /wayback/v1/available | 



## waybackV1AvailableGet

> waybackV1AvailableGet(url, opts)



### Example

```javascript
import WaybackApi from 'wayback_api';

let apiInstance = new WaybackApi.DefaultApi();
let url = "url_example"; // String | A single URL to query.
let opts = {
  'timestamp': "timestamp_example", // String | Timestamp requested in ISO 8601 format. The following formats are acceptable:  - YYYY  - YYYY-MM  - YYYY-MM-DD  - YYYY-MM-DDTHH:mm:SSz  - YYYY-MM-DD:HH:mm+00:00 
  'callback': "callback_example", // String | Specifies a JavaScript function func, for a JSON-P response. When provided, results are wrapped as `callback(data)`, and the returned MIME type is application/javascript. This causes the caller to automatically run the func with the JSON results as its argument. 
  'timeout': 5, // Number | Timeout is the maximum number of seconds to wait for the availability API to get its underlying results from the CDX server. The default value is 5.0. 
  'closest': "'either'", // String | The direction specifies whether to match archived timestamps that are before the provided one, after, or the default either (closest in either direction). Must be before, after, or either. May be overidden by individual requests. 
  'statusCode': 56, // Number | HTTP status codes to filter by. Only results with these codes will be returned 
  'tag': "tag_example" // String | The optional tag can have any value, and is returned with the results; it can be used to help collate input and output values. 
};
apiInstance.waybackV1AvailableGet(url, opts, (error, data, response) => {
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
 **url** | **String**| A single URL to query. | 
 **timestamp** | **String**| Timestamp requested in ISO 8601 format. The following formats are acceptable:  - YYYY  - YYYY-MM  - YYYY-MM-DD  - YYYY-MM-DDTHH:mm:SSz  - YYYY-MM-DD:HH:mm+00:00  | [optional] 
 **callback** | **String**| Specifies a JavaScript function func, for a JSON-P response. When provided, results are wrapped as &#x60;callback(data)&#x60;, and the returned MIME type is application/javascript. This causes the caller to automatically run the func with the JSON results as its argument.  | [optional] 
 **timeout** | **Number**| Timeout is the maximum number of seconds to wait for the availability API to get its underlying results from the CDX server. The default value is 5.0.  | [optional] [default to 5]
 **closest** | **String**| The direction specifies whether to match archived timestamps that are before the provided one, after, or the default either (closest in either direction). Must be before, after, or either. May be overidden by individual requests.  | [optional] [default to &#39;either&#39;]
 **statusCode** | **Number**| HTTP status codes to filter by. Only results with these codes will be returned  | [optional] 
 **tag** | **String**| The optional tag can have any value, and is returned with the results; it can be used to help collate input and output values.  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: applcation/json, application/javascript, application/json


## waybackV1AvailablePost

> waybackV1AvailablePost(url, opts)



### Example

```javascript
import WaybackApi from 'wayback_api';

let apiInstance = new WaybackApi.DefaultApi();
let url = "url_example"; // String | A single URL to query.
let opts = {
  'timestamp': "timestamp_example", // String | Timestamp requested in ISO 8601 format. The following formats are acceptable:  - YYYY  - YYYY-MM  - YYYY-MM-DD  - YYYY-MM-DDTHH:mm:SSz  - YYYY-MM-DD:HH:mm+00:00 
  'callback': "callback_example", // String | Specifies a JavaScript function func, for a JSON-P response. When provided, results are wrapped as `callback(data)`, and the returned MIME type is application/javascript. This causes the caller to automatically run the func with the JSON results as its argument. 
  'timeout': 5, // Number | Timeout is the maximum number of seconds to wait for the availability API to get its underlying results from the CDX server. The default value is 5.0. 
  'closest': "'either'", // String | The direction specifies whether to match archived timestamps that are before the provided one, after, or the default either (closest in either direction). Must be before, after, or either. May be overidden by individual requests. 
  'statusCode': 56, // Number | HTTP status codes to filter by. Only results with these codes will be returned 
  'tag': "tag_example", // String | The optional tag can have any value, and is returned with the results; it can be used to help collate input and output values. 
  'availabilityRequest': [new WaybackApi.AvailabilityRequest()] // [AvailabilityRequest] | 
};
apiInstance.waybackV1AvailablePost(url, opts, (error, data, response) => {
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
 **url** | **String**| A single URL to query. | 
 **timestamp** | **String**| Timestamp requested in ISO 8601 format. The following formats are acceptable:  - YYYY  - YYYY-MM  - YYYY-MM-DD  - YYYY-MM-DDTHH:mm:SSz  - YYYY-MM-DD:HH:mm+00:00  | [optional] 
 **callback** | **String**| Specifies a JavaScript function func, for a JSON-P response. When provided, results are wrapped as &#x60;callback(data)&#x60;, and the returned MIME type is application/javascript. This causes the caller to automatically run the func with the JSON results as its argument.  | [optional] 
 **timeout** | **Number**| Timeout is the maximum number of seconds to wait for the availability API to get its underlying results from the CDX server. The default value is 5.0.  | [optional] [default to 5]
 **closest** | **String**| The direction specifies whether to match archived timestamps that are before the provided one, after, or the default either (closest in either direction). Must be before, after, or either. May be overidden by individual requests.  | [optional] [default to &#39;either&#39;]
 **statusCode** | **Number**| HTTP status codes to filter by. Only results with these codes will be returned  | [optional] 
 **tag** | **String**| The optional tag can have any value, and is returned with the results; it can be used to help collate input and output values.  | [optional] 
 **availabilityRequest** | [**[AvailabilityRequest]**](AvailabilityRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, text/csv
- **Accept**: applcation/json, application/javascript, application/json

