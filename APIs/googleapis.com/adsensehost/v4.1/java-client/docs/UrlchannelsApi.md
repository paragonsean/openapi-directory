# UrlchannelsApi

All URIs are relative to *https://www.googleapis.com/adsensehost/v4.1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**adsensehostUrlchannelsDelete**](UrlchannelsApi.md#adsensehostUrlchannelsDelete) | **DELETE** /adclients/{adClientId}/urlchannels/{urlChannelId} |  |
| [**adsensehostUrlchannelsInsert**](UrlchannelsApi.md#adsensehostUrlchannelsInsert) | **POST** /adclients/{adClientId}/urlchannels |  |
| [**adsensehostUrlchannelsList**](UrlchannelsApi.md#adsensehostUrlchannelsList) | **GET** /adclients/{adClientId}/urlchannels |  |


<a id="adsensehostUrlchannelsDelete"></a>
# **adsensehostUrlchannelsDelete**
> UrlChannel adsensehostUrlchannelsDelete(adClientId, urlChannelId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Delete a URL channel from the host AdSense account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UrlchannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/adsensehost/v4.1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UrlchannelsApi apiInstance = new UrlchannelsApi(defaultClient);
    String adClientId = "adClientId_example"; // String | Ad client from which to delete the URL channel.
    String urlChannelId = "urlChannelId_example"; // String | URL channel to delete.
    String alt = "csv"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      UrlChannel result = apiInstance.adsensehostUrlchannelsDelete(adClientId, urlChannelId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UrlchannelsApi#adsensehostUrlchannelsDelete");
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
| **adClientId** | **String**| Ad client from which to delete the URL channel. | |
| **urlChannelId** | **String**| URL channel to delete. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: csv, json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

[**UrlChannel**](UrlChannel.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="adsensehostUrlchannelsInsert"></a>
# **adsensehostUrlchannelsInsert**
> UrlChannel adsensehostUrlchannelsInsert(adClientId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, urlChannel)



Add a new URL channel to the host AdSense account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UrlchannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/adsensehost/v4.1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UrlchannelsApi apiInstance = new UrlchannelsApi(defaultClient);
    String adClientId = "adClientId_example"; // String | Ad client to which the new URL channel will be added.
    String alt = "csv"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    UrlChannel urlChannel = new UrlChannel(); // UrlChannel | 
    try {
      UrlChannel result = apiInstance.adsensehostUrlchannelsInsert(adClientId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, urlChannel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UrlchannelsApi#adsensehostUrlchannelsInsert");
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
| **adClientId** | **String**| Ad client to which the new URL channel will be added. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: csv, json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **urlChannel** | [**UrlChannel**](UrlChannel.md)|  | [optional] |

### Return type

[**UrlChannel**](UrlChannel.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="adsensehostUrlchannelsList"></a>
# **adsensehostUrlchannelsList**
> UrlChannels adsensehostUrlchannelsList(adClientId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, maxResults, pageToken)



List all host URL channels in the host AdSense account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UrlchannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/adsensehost/v4.1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UrlchannelsApi apiInstance = new UrlchannelsApi(defaultClient);
    String adClientId = "adClientId_example"; // String | Ad client for which to list URL channels.
    String alt = "csv"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Integer maxResults = 56; // Integer | The maximum number of URL channels to include in the response, used for paging.
    String pageToken = "pageToken_example"; // String | A continuation token, used to page through URL channels. To retrieve the next page, set this parameter to the value of \"nextPageToken\" from the previous response.
    try {
      UrlChannels result = apiInstance.adsensehostUrlchannelsList(adClientId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, maxResults, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UrlchannelsApi#adsensehostUrlchannelsList");
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
| **adClientId** | **String**| Ad client for which to list URL channels. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: csv, json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **maxResults** | **Integer**| The maximum number of URL channels to include in the response, used for paging. | [optional] |
| **pageToken** | **String**| A continuation token, used to page through URL channels. To retrieve the next page, set this parameter to the value of \&quot;nextPageToken\&quot; from the previous response. | [optional] |

### Return type

[**UrlChannels**](UrlChannels.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

