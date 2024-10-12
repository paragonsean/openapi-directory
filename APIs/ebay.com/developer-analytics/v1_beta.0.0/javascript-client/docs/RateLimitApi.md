# AnalyticsApi.RateLimitApi

All URIs are relative to *https://api.ebay.com/developer/analytics/v1_beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getRateLimits**](RateLimitApi.md#getRateLimits) | **GET** /rate_limit/ | 



## getRateLimits

> RateLimitsResponse getRateLimits(opts)



This method retrieves the call limit and utilization data for an application. The data is retrieved for all RESTful APIs and the legacy Trading API.  &lt;br&gt;&lt;br&gt;The response from &lt;b&gt;getRateLimits&lt;/b&gt; includes a list of the applicable resources and the \&quot;call limit\&quot;, or quota, that is set for each resource. In addition to quota information, the response also includes the number of remaining calls available before the limit is reached, the time remaining before the quota resets, and the length of the \&quot;time window\&quot; to which the quota applies.  &lt;br&gt;&lt;br&gt;By default, this method returns utilization data for all RESTful API and the legacy Trading API resources. Use the &lt;b&gt;api_name&lt;/b&gt; and &lt;b&gt;api_context&lt;/b&gt; query parameters to filter the response to only the desired APIs.  &lt;br&gt;&lt;br&gt;For more on call limits, see &lt;a href&#x3D;\&quot;https://developer.ebay.com/support/app-check \&quot; target&#x3D;\&quot;_blank\&quot;&gt;Compatible Application Check&lt;/a&gt;.

### Example

```javascript
import AnalyticsApi from 'analytics_api';
let defaultClient = AnalyticsApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AnalyticsApi.RateLimitApi();
let opts = {
  'apiContext': "apiContext_example", // String | This optional query parameter filters the result to include only the specified API context. <br><br><b>Valid values:</b> <ul><li><code>buy</code></li><li><code>sell</code></li> <li><code>commerce</code></li><li><code>developer</code></li><li><code>tradingapi</code></li></ul>
  'apiName': "apiName_example" // String | This optional query parameter filters the result to include only the APIs specified. <br><br><b>Example values:</b> <ul> <li><code>browse</code> for the <a href=\"/../develop/apis/restful-apis/buy-apis#buy-apis\" target=\"_blank\">Buy APIs</a></li> <li><code>inventory</code> for the <a href=\"/../develop/apis/restful-apis/sell-apis#sell-apis\" target=\"_blank\">Sell APIs</a></li>  <li><code>taxonomy</code> for the <a href=\"/../develop/apis/restful-apis/commerce-apis#commerce-apis\" target=\"_blank\">Commerce APIs</a></li>  <li><code>tradingapi</code> for the <a href=\"/../Devzone/XML/docs/Reference/eBay/index.html\" target=\"_blank\">Trading APIs</a></li></ul>
};
apiInstance.getRateLimits(opts, (error, data, response) => {
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
 **apiContext** | **String**| This optional query parameter filters the result to include only the specified API context. &lt;br&gt;&lt;br&gt;&lt;b&gt;Valid values:&lt;/b&gt; &lt;ul&gt;&lt;li&gt;&lt;code&gt;buy&lt;/code&gt;&lt;/li&gt;&lt;li&gt;&lt;code&gt;sell&lt;/code&gt;&lt;/li&gt; &lt;li&gt;&lt;code&gt;commerce&lt;/code&gt;&lt;/li&gt;&lt;li&gt;&lt;code&gt;developer&lt;/code&gt;&lt;/li&gt;&lt;li&gt;&lt;code&gt;tradingapi&lt;/code&gt;&lt;/li&gt;&lt;/ul&gt; | [optional] 
 **apiName** | **String**| This optional query parameter filters the result to include only the APIs specified. &lt;br&gt;&lt;br&gt;&lt;b&gt;Example values:&lt;/b&gt; &lt;ul&gt; &lt;li&gt;&lt;code&gt;browse&lt;/code&gt; for the &lt;a href&#x3D;\&quot;/../develop/apis/restful-apis/buy-apis#buy-apis\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Buy APIs&lt;/a&gt;&lt;/li&gt; &lt;li&gt;&lt;code&gt;inventory&lt;/code&gt; for the &lt;a href&#x3D;\&quot;/../develop/apis/restful-apis/sell-apis#sell-apis\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Sell APIs&lt;/a&gt;&lt;/li&gt;  &lt;li&gt;&lt;code&gt;taxonomy&lt;/code&gt; for the &lt;a href&#x3D;\&quot;/../develop/apis/restful-apis/commerce-apis#commerce-apis\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Commerce APIs&lt;/a&gt;&lt;/li&gt;  &lt;li&gt;&lt;code&gt;tradingapi&lt;/code&gt; for the &lt;a href&#x3D;\&quot;/../Devzone/XML/docs/Reference/eBay/index.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Trading APIs&lt;/a&gt;&lt;/li&gt;&lt;/ul&gt; | [optional] 

### Return type

[**RateLimitsResponse**](RateLimitsResponse.md)

### Authorization

[api_auth](../README.md#api_auth), [api_auth](../README.md#api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

