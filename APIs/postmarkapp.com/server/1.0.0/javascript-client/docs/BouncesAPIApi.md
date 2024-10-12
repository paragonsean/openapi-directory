# PostmarkApi.BouncesAPIApi

All URIs are relative to *http://api.postmarkapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activateBounce**](BouncesAPIApi.md#activateBounce) | **PUT** /bounces/{bounceid}/activate | Activate a bounce
[**bouncesBounceidDumpGet**](BouncesAPIApi.md#bouncesBounceidDumpGet) | **GET** /bounces/{bounceid}/dump | Get bounce dump
[**getBounces**](BouncesAPIApi.md#getBounces) | **GET** /bounces | Get bounces
[**getDeliveryStats**](BouncesAPIApi.md#getDeliveryStats) | **GET** /deliverystats | Get delivery stats
[**getSingleBounce**](BouncesAPIApi.md#getSingleBounce) | **GET** /bounces/{bounceid} | Get a single bounce



## activateBounce

> BounceActivationResponse activateBounce(xPostmarkServerToken, bounceid)

Activate a bounce

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.BouncesAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let bounceid = 789; // Number | The ID of the Bounce to activate.
apiInstance.activateBounce(xPostmarkServerToken, bounceid, (error, data, response) => {
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
 **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | 
 **bounceid** | **Number**| The ID of the Bounce to activate. | 

### Return type

[**BounceActivationResponse**](BounceActivationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## bouncesBounceidDumpGet

> BounceDumpResponse bouncesBounceidDumpGet(xPostmarkServerToken, bounceid)

Get bounce dump

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.BouncesAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let bounceid = 789; // Number | The ID for the bounce dump to retrieve.
apiInstance.bouncesBounceidDumpGet(xPostmarkServerToken, bounceid, (error, data, response) => {
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
 **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | 
 **bounceid** | **Number**| The ID for the bounce dump to retrieve. | 

### Return type

[**BounceDumpResponse**](BounceDumpResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBounces

> BounceSearchResponse getBounces(xPostmarkServerToken, count, offset, opts)

Get bounces

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.BouncesAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let count = 56; // Number | Number of bounces to return per request. Max 500.
let offset = 56; // Number | Number of bounces to skip.
let opts = {
  'type': "type_example", // String | Filter by type of bounce
  'inactive': true, // Boolean | Filter by emails that were deactivated by Postmark due to the bounce. Set to true or false. If this isn't specified it will return both active and inactive.
  'emailFilter': "emailFilter_example", // String | Filter by email address
  'messageID': "messageID_example", // String | Filter by messageID
  'tag': "tag_example", // String | Filter by tag
  'todate': new Date("2013-10-20"), // Date | Filter messages up to the date specified. e.g. `2014-02-01`
  'fromdate': new Date("2013-10-20") // Date | Filter messages starting from the date specified. e.g. `2014-02-01`
};
apiInstance.getBounces(xPostmarkServerToken, count, offset, opts, (error, data, response) => {
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
 **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | 
 **count** | **Number**| Number of bounces to return per request. Max 500. | 
 **offset** | **Number**| Number of bounces to skip. | 
 **type** | **String**| Filter by type of bounce | [optional] 
 **inactive** | **Boolean**| Filter by emails that were deactivated by Postmark due to the bounce. Set to true or false. If this isn&#39;t specified it will return both active and inactive. | [optional] 
 **emailFilter** | **String**| Filter by email address | [optional] 
 **messageID** | **String**| Filter by messageID | [optional] 
 **tag** | **String**| Filter by tag | [optional] 
 **todate** | **Date**| Filter messages up to the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] 
 **fromdate** | **Date**| Filter messages starting from the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] 

### Return type

[**BounceSearchResponse**](BounceSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeliveryStats

> DeliveryStatsResponse getDeliveryStats(xPostmarkServerToken)

Get delivery stats

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.BouncesAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
apiInstance.getDeliveryStats(xPostmarkServerToken, (error, data, response) => {
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
 **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | 

### Return type

[**DeliveryStatsResponse**](DeliveryStatsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSingleBounce

> BounceInfoResponse getSingleBounce(xPostmarkServerToken, bounceid)

Get a single bounce

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.BouncesAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let bounceid = 789; // Number | The ID of the bounce to retrieve.
apiInstance.getSingleBounce(xPostmarkServerToken, bounceid, (error, data, response) => {
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
 **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | 
 **bounceid** | **Number**| The ID of the bounce to retrieve. | 

### Return type

[**BounceInfoResponse**](BounceInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

