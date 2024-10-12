# PostmarkApi.StatsAPIApi

All URIs are relative to *http://api.postmarkapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getBounceCounts**](StatsAPIApi.md#getBounceCounts) | **GET** /stats/outbound/bounces | Get bounce counts
[**getOutboundClickCounts**](StatsAPIApi.md#getOutboundClickCounts) | **GET** /stats/outbound/clicks | Get click counts
[**getOutboundClickCountsByBrowserFamily**](StatsAPIApi.md#getOutboundClickCountsByBrowserFamily) | **GET** /stats/outbound/clicks/browserfamilies | Get browser usage by family
[**getOutboundClickCountsByLocation**](StatsAPIApi.md#getOutboundClickCountsByLocation) | **GET** /stats/outbound/clicks/location | Get clicks by body location
[**getOutboundClickCountsByPlatform**](StatsAPIApi.md#getOutboundClickCountsByPlatform) | **GET** /stats/outbound/clicks/platforms | Get browser plaform usage
[**getOutboundOpenCounts**](StatsAPIApi.md#getOutboundOpenCounts) | **GET** /stats/outbound/opens | Get email open counts
[**getOutboundOpenCountsByEmailClient**](StatsAPIApi.md#getOutboundOpenCountsByEmailClient) | **GET** /stats/outbound/opens/emailclients | Get email client usage
[**getOutboundOpenCountsByPlatform**](StatsAPIApi.md#getOutboundOpenCountsByPlatform) | **GET** /stats/outbound/opens/platforms | Get email platform usage
[**getOutboundOverviewStatistics**](StatsAPIApi.md#getOutboundOverviewStatistics) | **GET** /stats/outbound | Get outbound overview
[**getSentCounts**](StatsAPIApi.md#getSentCounts) | **GET** /stats/outbound/sends | Get sent counts
[**getSpamComplaints**](StatsAPIApi.md#getSpamComplaints) | **GET** /stats/outbound/spam | Get spam complaints
[**getTrackedEmailCounts**](StatsAPIApi.md#getTrackedEmailCounts) | **GET** /stats/outbound/tracked | Get tracked email counts



## getBounceCounts

> GetBounceCounts200Response getBounceCounts(xPostmarkServerToken, opts)

Get bounce counts

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.StatsAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let opts = {
  'tag': "tag_example", // String | Filter by tag
  'fromdate': new Date("2013-10-20"), // Date | Filter stats starting from the date specified. e.g. `2014-01-01`
  'todate': new Date("2013-10-20") // Date | Filter stats up to the date specified. e.g. `2014-02-01`
};
apiInstance.getBounceCounts(xPostmarkServerToken, opts, (error, data, response) => {
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
 **tag** | **String**| Filter by tag | [optional] 
 **fromdate** | **Date**| Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60; | [optional] 
 **todate** | **Date**| Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] 

### Return type

[**GetBounceCounts200Response**](GetBounceCounts200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOutboundClickCounts

> Object getOutboundClickCounts(xPostmarkServerToken, opts)

Get click counts

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.StatsAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let opts = {
  'tag': "tag_example", // String | Filter by tag
  'fromdate': new Date("2013-10-20"), // Date | Filter stats starting from the date specified. e.g. `2014-01-01`
  'todate': new Date("2013-10-20") // Date | Filter stats up to the date specified. e.g. `2014-02-01`
};
apiInstance.getOutboundClickCounts(xPostmarkServerToken, opts, (error, data, response) => {
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
 **tag** | **String**| Filter by tag | [optional] 
 **fromdate** | **Date**| Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60; | [optional] 
 **todate** | **Date**| Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOutboundClickCountsByBrowserFamily

> Object getOutboundClickCountsByBrowserFamily(xPostmarkServerToken, opts)

Get browser usage by family

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.StatsAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let opts = {
  'tag': "tag_example", // String | Filter by tag
  'fromdate': new Date("2013-10-20"), // Date | Filter stats starting from the date specified. e.g. `2014-01-01`
  'todate': new Date("2013-10-20") // Date | Filter stats up to the date specified. e.g. `2014-02-01`
};
apiInstance.getOutboundClickCountsByBrowserFamily(xPostmarkServerToken, opts, (error, data, response) => {
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
 **tag** | **String**| Filter by tag | [optional] 
 **fromdate** | **Date**| Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60; | [optional] 
 **todate** | **Date**| Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOutboundClickCountsByLocation

> Object getOutboundClickCountsByLocation(xPostmarkServerToken, opts)

Get clicks by body location

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.StatsAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let opts = {
  'tag': "tag_example", // String | Filter by tag
  'fromdate': new Date("2013-10-20"), // Date | Filter stats starting from the date specified. e.g. `2014-01-01`
  'todate': new Date("2013-10-20") // Date | Filter stats up to the date specified. e.g. `2014-02-01`
};
apiInstance.getOutboundClickCountsByLocation(xPostmarkServerToken, opts, (error, data, response) => {
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
 **tag** | **String**| Filter by tag | [optional] 
 **fromdate** | **Date**| Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60; | [optional] 
 **todate** | **Date**| Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOutboundClickCountsByPlatform

> Object getOutboundClickCountsByPlatform(xPostmarkServerToken, opts)

Get browser plaform usage

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.StatsAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let opts = {
  'tag': "tag_example", // String | Filter by tag
  'fromdate': new Date("2013-10-20"), // Date | Filter stats starting from the date specified. e.g. `2014-01-01`
  'todate': new Date("2013-10-20") // Date | Filter stats up to the date specified. e.g. `2014-02-01`
};
apiInstance.getOutboundClickCountsByPlatform(xPostmarkServerToken, opts, (error, data, response) => {
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
 **tag** | **String**| Filter by tag | [optional] 
 **fromdate** | **Date**| Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60; | [optional] 
 **todate** | **Date**| Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOutboundOpenCounts

> GetOutboundOpenCounts200Response getOutboundOpenCounts(xPostmarkServerToken, opts)

Get email open counts

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.StatsAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let opts = {
  'tag': "tag_example", // String | Filter by tag
  'fromdate': new Date("2013-10-20"), // Date | Filter stats starting from the date specified. e.g. `2014-01-01`
  'todate': new Date("2013-10-20") // Date | Filter stats up to the date specified. e.g. `2014-02-01`
};
apiInstance.getOutboundOpenCounts(xPostmarkServerToken, opts, (error, data, response) => {
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
 **tag** | **String**| Filter by tag | [optional] 
 **fromdate** | **Date**| Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60; | [optional] 
 **todate** | **Date**| Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] 

### Return type

[**GetOutboundOpenCounts200Response**](GetOutboundOpenCounts200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOutboundOpenCountsByEmailClient

> GetOutboundOpenCountsByEmailClient200Response getOutboundOpenCountsByEmailClient(xPostmarkServerToken, opts)

Get email client usage

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.StatsAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let opts = {
  'tag': "tag_example", // String | Filter by tag
  'fromdate': new Date("2013-10-20"), // Date | Filter stats starting from the date specified. e.g. `2014-01-01`
  'todate': new Date("2013-10-20") // Date | Filter stats up to the date specified. e.g. `2014-02-01`
};
apiInstance.getOutboundOpenCountsByEmailClient(xPostmarkServerToken, opts, (error, data, response) => {
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
 **tag** | **String**| Filter by tag | [optional] 
 **fromdate** | **Date**| Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60; | [optional] 
 **todate** | **Date**| Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] 

### Return type

[**GetOutboundOpenCountsByEmailClient200Response**](GetOutboundOpenCountsByEmailClient200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOutboundOpenCountsByPlatform

> GetOutboundOpenCountsByPlatform200Response getOutboundOpenCountsByPlatform(xPostmarkServerToken, opts)

Get email platform usage

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.StatsAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let opts = {
  'tag': "tag_example", // String | Filter by tag
  'fromdate': new Date("2013-10-20"), // Date | Filter stats starting from the date specified. e.g. `2014-01-01`
  'todate': new Date("2013-10-20") // Date | Filter stats up to the date specified. e.g. `2014-02-01`
};
apiInstance.getOutboundOpenCountsByPlatform(xPostmarkServerToken, opts, (error, data, response) => {
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
 **tag** | **String**| Filter by tag | [optional] 
 **fromdate** | **Date**| Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60; | [optional] 
 **todate** | **Date**| Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] 

### Return type

[**GetOutboundOpenCountsByPlatform200Response**](GetOutboundOpenCountsByPlatform200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOutboundOverviewStatistics

> OutboundOverviewStatsResponse getOutboundOverviewStatistics(xPostmarkServerToken, opts)

Get outbound overview

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.StatsAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let opts = {
  'tag': "tag_example", // String | Filter by tag
  'fromdate': new Date("2013-10-20"), // Date | Filter stats starting from the date specified. e.g. `2014-01-01`
  'todate': new Date("2013-10-20") // Date | Filter stats up to the date specified. e.g. `2014-02-01`
};
apiInstance.getOutboundOverviewStatistics(xPostmarkServerToken, opts, (error, data, response) => {
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
 **tag** | **String**| Filter by tag | [optional] 
 **fromdate** | **Date**| Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60; | [optional] 
 **todate** | **Date**| Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] 

### Return type

[**OutboundOverviewStatsResponse**](OutboundOverviewStatsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSentCounts

> SentCountsResponse getSentCounts(xPostmarkServerToken, opts)

Get sent counts

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.StatsAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let opts = {
  'tag': "tag_example", // String | Filter by tag
  'fromdate': new Date("2013-10-20"), // Date | Filter stats starting from the date specified. e.g. `2014-01-01`
  'todate': new Date("2013-10-20") // Date | Filter stats up to the date specified. e.g. `2014-02-01`
};
apiInstance.getSentCounts(xPostmarkServerToken, opts, (error, data, response) => {
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
 **tag** | **String**| Filter by tag | [optional] 
 **fromdate** | **Date**| Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60; | [optional] 
 **todate** | **Date**| Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] 

### Return type

[**SentCountsResponse**](SentCountsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSpamComplaints

> GetSpamComplaints200Response getSpamComplaints(xPostmarkServerToken, opts)

Get spam complaints

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.StatsAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let opts = {
  'tag': "tag_example", // String | Filter by tag
  'fromdate': new Date("2013-10-20"), // Date | Filter stats starting from the date specified. e.g. `2014-01-01`
  'todate': new Date("2013-10-20") // Date | Filter stats up to the date specified. e.g. `2014-02-01`
};
apiInstance.getSpamComplaints(xPostmarkServerToken, opts, (error, data, response) => {
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
 **tag** | **String**| Filter by tag | [optional] 
 **fromdate** | **Date**| Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60; | [optional] 
 **todate** | **Date**| Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] 

### Return type

[**GetSpamComplaints200Response**](GetSpamComplaints200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTrackedEmailCounts

> GetTrackedEmailCounts200Response getTrackedEmailCounts(xPostmarkServerToken, opts)

Get tracked email counts

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.StatsAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let opts = {
  'tag': "tag_example", // String | Filter by tag
  'fromdate': new Date("2013-10-20"), // Date | Filter stats starting from the date specified. e.g. `2014-01-01`
  'todate': new Date("2013-10-20") // Date | Filter stats starting from the date specified. e.g. `2014-01-01`
};
apiInstance.getTrackedEmailCounts(xPostmarkServerToken, opts, (error, data, response) => {
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
 **tag** | **String**| Filter by tag | [optional] 
 **fromdate** | **Date**| Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60; | [optional] 
 **todate** | **Date**| Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60; | [optional] 

### Return type

[**GetTrackedEmailCounts200Response**](GetTrackedEmailCounts200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

