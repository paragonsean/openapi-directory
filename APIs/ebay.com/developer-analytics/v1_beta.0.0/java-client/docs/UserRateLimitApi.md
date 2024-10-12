# UserRateLimitApi

All URIs are relative to *https://api.ebay.com/developer/analytics/v1_beta*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getUserRateLimits**](UserRateLimitApi.md#getUserRateLimits) | **GET** /user_rate_limit/ |  |


<a id="getUserRateLimits"></a>
# **getUserRateLimits**
> RateLimitsResponse getUserRateLimits(apiContext, apiName)



This method retrieves the call limit and utilization data for an application user. The call-limit data is returned for all RESTful APIs and the legacy Trading API that limit calls on a per-user basis.  &lt;br&gt;&lt;br&gt;The response from &lt;b&gt;getUserRateLimits&lt;/b&gt; includes a list of the applicable resources and the \&quot;call limit\&quot;, or quota, that is set for each resource. In addition to quota information, the response also includes the number of remaining calls available before the limit is reached, the time remaining before the quota resets, and the length of the \&quot;time window\&quot; to which the quota applies.  &lt;br&gt;&lt;br&gt;By default, this method returns utilization data for all RESTful APIs resources and the legacy Trading API calls that limit request access by user. Use the &lt;b&gt;api_name&lt;/b&gt; and &lt;b&gt;api_context&lt;/b&gt; query parameters to filter the response to only the desired APIs.  &lt;br&gt;&lt;br&gt;For more on call limits, see &lt;a href&#x3D;\&quot;https://developer.ebay.com/support/app-check \&quot; target&#x3D;\&quot;_blank\&quot;&gt;Compatible Application Check&lt;/a&gt;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserRateLimitApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ebay.com/developer/analytics/v1_beta");
    
    // Configure OAuth2 access token for authorization: api_auth
    OAuth api_auth = (OAuth) defaultClient.getAuthentication("api_auth");
    api_auth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: api_auth
    OAuth api_auth = (OAuth) defaultClient.getAuthentication("api_auth");
    api_auth.setAccessToken("YOUR ACCESS TOKEN");

    UserRateLimitApi apiInstance = new UserRateLimitApi(defaultClient);
    String apiContext = "apiContext_example"; // String | This optional query parameter filters the result to include only the specified API context. <br><br><b>Valid values:</b> <ul><li><code>buy</code></li> <li><code>sell</code></li> <li><code>commerce</code></li> <li><code>developer</code></li> <li><code>tradingapi</code></li></ul>
    String apiName = "apiName_example"; // String | This optional query parameter filters the result to include only the APIs specified. <br><br><b>Example values:</b> <ul><li><code>browse</code> for the <a href=\"/../develop/apis/restful-apis/buy-apis#buy-apis\" target=\"_blank\">Buy APIs</a></li> <li><code>inventory</code> for the <a href=\"/../develop/apis/restful-apis/sell-apis#sell-apis\" target=\"_blank\">Sell APIs</a></li>  <li><code>taxonomy</code> for the <a href=\"/../develop/apis/restful-apis/commerce-apis#commerce-apis\" target=\"_blank\">Commerce APIs</a></li>  <li><code>tradingapi</code> for the <a href=\"/../Devzone/XML/docs/Reference/eBay/index.html\" target=\"_blank\">Trading APIs</a></li></ul>
    try {
      RateLimitsResponse result = apiInstance.getUserRateLimits(apiContext, apiName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserRateLimitApi#getUserRateLimits");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **apiContext** | **String**| This optional query parameter filters the result to include only the specified API context. &lt;br&gt;&lt;br&gt;&lt;b&gt;Valid values:&lt;/b&gt; &lt;ul&gt;&lt;li&gt;&lt;code&gt;buy&lt;/code&gt;&lt;/li&gt; &lt;li&gt;&lt;code&gt;sell&lt;/code&gt;&lt;/li&gt; &lt;li&gt;&lt;code&gt;commerce&lt;/code&gt;&lt;/li&gt; &lt;li&gt;&lt;code&gt;developer&lt;/code&gt;&lt;/li&gt; &lt;li&gt;&lt;code&gt;tradingapi&lt;/code&gt;&lt;/li&gt;&lt;/ul&gt; | [optional] |
| **apiName** | **String**| This optional query parameter filters the result to include only the APIs specified. &lt;br&gt;&lt;br&gt;&lt;b&gt;Example values:&lt;/b&gt; &lt;ul&gt;&lt;li&gt;&lt;code&gt;browse&lt;/code&gt; for the &lt;a href&#x3D;\&quot;/../develop/apis/restful-apis/buy-apis#buy-apis\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Buy APIs&lt;/a&gt;&lt;/li&gt; &lt;li&gt;&lt;code&gt;inventory&lt;/code&gt; for the &lt;a href&#x3D;\&quot;/../develop/apis/restful-apis/sell-apis#sell-apis\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Sell APIs&lt;/a&gt;&lt;/li&gt;  &lt;li&gt;&lt;code&gt;taxonomy&lt;/code&gt; for the &lt;a href&#x3D;\&quot;/../develop/apis/restful-apis/commerce-apis#commerce-apis\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Commerce APIs&lt;/a&gt;&lt;/li&gt;  &lt;li&gt;&lt;code&gt;tradingapi&lt;/code&gt; for the &lt;a href&#x3D;\&quot;/../Devzone/XML/docs/Reference/eBay/index.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Trading APIs&lt;/a&gt;&lt;/li&gt;&lt;/ul&gt; | [optional] |

### Return type

[**RateLimitsResponse**](RateLimitsResponse.md)

### Authorization

[api_auth](../README.md#api_auth), [api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | No Content |  -  |
| **500** | Internal Server Error |  -  |

