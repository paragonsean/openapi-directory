# YouTubeAnalyticsApi.ReportsApi

All URIs are relative to *https://youtubeanalytics.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**youtubeAnalyticsReportsQuery**](ReportsApi.md#youtubeAnalyticsReportsQuery) | **GET** /v2/reports | 



## youtubeAnalyticsReportsQuery

> QueryResponse youtubeAnalyticsReportsQuery(opts)



Retrieve your YouTube Analytics reports.

### Example

```javascript
import YouTubeAnalyticsApi from 'you_tube_analytics_api';
let defaultClient = YouTubeAnalyticsApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new YouTubeAnalyticsApi.ReportsApi();
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'currency': "currency_example", // String | The currency to which financial metrics should be converted. The default is US Dollar (USD). If the result contains no financial metrics, this flag will be ignored. Responds with an error if the specified currency is not recognized.\", pattern: [A-Z]{3}
  'dimensions': "dimensions_example", // String | A comma-separated list of YouTube Analytics dimensions, such as `views` or `ageGroup,gender`. See the [Available Reports](/youtube/analytics/v2/available_reports) document for a list of the reports that you can retrieve and the dimensions used for those reports. Also see the [Dimensions](/youtube/analytics/v2/dimsmets/dims) document for definitions of those dimensions.\" pattern: [0-9a-zA-Z,]+
  'endDate': "endDate_example", // String | The end date for fetching YouTube Analytics data. The value should be in `YYYY-MM-DD` format. required: true, pattern: [0-9]{4}-[0-9]{2}-[0-9]{2}
  'filters': "filters_example", // String | A list of filters that should be applied when retrieving YouTube Analytics data. The [Available Reports](/youtube/analytics/v2/available_reports) document identifies the dimensions that can be used to filter each report, and the [Dimensions](/youtube/analytics/v2/dimsmets/dims) document defines those dimensions. If a request uses multiple filters, join them together with a semicolon (`;`), and the returned result table will satisfy both filters. For example, a filters parameter value of `video==dMH0bHeiRNg;country==IT` restricts the result set to include data for the given video in Italy.\",
  'ids': "ids_example", // String | Identifies the YouTube channel or content owner for which you are retrieving YouTube Analytics data. - To request data for a YouTube user, set the `ids` parameter value to `channel==CHANNEL_ID`, where `CHANNEL_ID` specifies the unique YouTube channel ID. - To request data for a YouTube CMS content owner, set the `ids` parameter value to `contentOwner==OWNER_NAME`, where `OWNER_NAME` is the CMS name of the content owner. required: true, pattern: [a-zA-Z]+==[a-zA-Z0-9_+-]+
  'includeHistoricalChannelData': true, // Boolean | If set to true historical data (i.e. channel data from before the linking of the channel to the content owner) will be retrieved.\",
  'maxResults': 56, // Number | The maximum number of rows to include in the response.\", minValue: 1
  'metrics': "metrics_example", // String | A comma-separated list of YouTube Analytics metrics, such as `views` or `likes,dislikes`. See the [Available Reports](/youtube/analytics/v2/available_reports) document for a list of the reports that you can retrieve and the metrics available in each report, and see the [Metrics](/youtube/analytics/v2/dimsmets/mets) document for definitions of those metrics. required: true, pattern: [0-9a-zA-Z,]+
  'sort': "sort_example", // String | A comma-separated list of dimensions or metrics that determine the sort order for YouTube Analytics data. By default the sort order is ascending. The '`-`' prefix causes descending sort order.\", pattern: [-0-9a-zA-Z,]+
  'startDate': "startDate_example", // String | The start date for fetching YouTube Analytics data. The value should be in `YYYY-MM-DD` format. required: true, pattern: \"[0-9]{4}-[0-9]{2}-[0-9]{2}
  'startIndex': 56 // Number | An index of the first entity to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter (one-based, inclusive).\", minValue: 1
};
apiInstance.youtubeAnalyticsReportsQuery(opts, (error, data, response) => {
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
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **currency** | **String**| The currency to which financial metrics should be converted. The default is US Dollar (USD). If the result contains no financial metrics, this flag will be ignored. Responds with an error if the specified currency is not recognized.\&quot;, pattern: [A-Z]{3} | [optional] 
 **dimensions** | **String**| A comma-separated list of YouTube Analytics dimensions, such as &#x60;views&#x60; or &#x60;ageGroup,gender&#x60;. See the [Available Reports](/youtube/analytics/v2/available_reports) document for a list of the reports that you can retrieve and the dimensions used for those reports. Also see the [Dimensions](/youtube/analytics/v2/dimsmets/dims) document for definitions of those dimensions.\&quot; pattern: [0-9a-zA-Z,]+ | [optional] 
 **endDate** | **String**| The end date for fetching YouTube Analytics data. The value should be in &#x60;YYYY-MM-DD&#x60; format. required: true, pattern: [0-9]{4}-[0-9]{2}-[0-9]{2} | [optional] 
 **filters** | **String**| A list of filters that should be applied when retrieving YouTube Analytics data. The [Available Reports](/youtube/analytics/v2/available_reports) document identifies the dimensions that can be used to filter each report, and the [Dimensions](/youtube/analytics/v2/dimsmets/dims) document defines those dimensions. If a request uses multiple filters, join them together with a semicolon (&#x60;;&#x60;), and the returned result table will satisfy both filters. For example, a filters parameter value of &#x60;video&#x3D;&#x3D;dMH0bHeiRNg;country&#x3D;&#x3D;IT&#x60; restricts the result set to include data for the given video in Italy.\&quot;, | [optional] 
 **ids** | **String**| Identifies the YouTube channel or content owner for which you are retrieving YouTube Analytics data. - To request data for a YouTube user, set the &#x60;ids&#x60; parameter value to &#x60;channel&#x3D;&#x3D;CHANNEL_ID&#x60;, where &#x60;CHANNEL_ID&#x60; specifies the unique YouTube channel ID. - To request data for a YouTube CMS content owner, set the &#x60;ids&#x60; parameter value to &#x60;contentOwner&#x3D;&#x3D;OWNER_NAME&#x60;, where &#x60;OWNER_NAME&#x60; is the CMS name of the content owner. required: true, pattern: [a-zA-Z]+&#x3D;&#x3D;[a-zA-Z0-9_+-]+ | [optional] 
 **includeHistoricalChannelData** | **Boolean**| If set to true historical data (i.e. channel data from before the linking of the channel to the content owner) will be retrieved.\&quot;, | [optional] 
 **maxResults** | **Number**| The maximum number of rows to include in the response.\&quot;, minValue: 1 | [optional] 
 **metrics** | **String**| A comma-separated list of YouTube Analytics metrics, such as &#x60;views&#x60; or &#x60;likes,dislikes&#x60;. See the [Available Reports](/youtube/analytics/v2/available_reports) document for a list of the reports that you can retrieve and the metrics available in each report, and see the [Metrics](/youtube/analytics/v2/dimsmets/mets) document for definitions of those metrics. required: true, pattern: [0-9a-zA-Z,]+ | [optional] 
 **sort** | **String**| A comma-separated list of dimensions or metrics that determine the sort order for YouTube Analytics data. By default the sort order is ascending. The &#39;&#x60;-&#x60;&#39; prefix causes descending sort order.\&quot;, pattern: [-0-9a-zA-Z,]+ | [optional] 
 **startDate** | **String**| The start date for fetching YouTube Analytics data. The value should be in &#x60;YYYY-MM-DD&#x60; format. required: true, pattern: \&quot;[0-9]{4}-[0-9]{2}-[0-9]{2} | [optional] 
 **startIndex** | **Number**| An index of the first entity to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter (one-based, inclusive).\&quot;, minValue: 1 | [optional] 

### Return type

[**QueryResponse**](QueryResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

