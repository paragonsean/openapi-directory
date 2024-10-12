# CustomchannelsApi

All URIs are relative to *https://www.googleapis.com/adsensehost/v4.1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**adsensehostCustomchannelsDelete**](CustomchannelsApi.md#adsensehostCustomchannelsDelete) | **DELETE** /adclients/{adClientId}/customchannels/{customChannelId} |  |
| [**adsensehostCustomchannelsGet**](CustomchannelsApi.md#adsensehostCustomchannelsGet) | **GET** /adclients/{adClientId}/customchannels/{customChannelId} |  |
| [**adsensehostCustomchannelsInsert**](CustomchannelsApi.md#adsensehostCustomchannelsInsert) | **POST** /adclients/{adClientId}/customchannels |  |
| [**adsensehostCustomchannelsList**](CustomchannelsApi.md#adsensehostCustomchannelsList) | **GET** /adclients/{adClientId}/customchannels |  |
| [**adsensehostCustomchannelsPatch**](CustomchannelsApi.md#adsensehostCustomchannelsPatch) | **PATCH** /adclients/{adClientId}/customchannels |  |
| [**adsensehostCustomchannelsUpdate**](CustomchannelsApi.md#adsensehostCustomchannelsUpdate) | **PUT** /adclients/{adClientId}/customchannels |  |


<a id="adsensehostCustomchannelsDelete"></a>
# **adsensehostCustomchannelsDelete**
> CustomChannel adsensehostCustomchannelsDelete(adClientId, customChannelId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Delete a specific custom channel from the host AdSense account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomchannelsApi;

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

    CustomchannelsApi apiInstance = new CustomchannelsApi(defaultClient);
    String adClientId = "adClientId_example"; // String | Ad client from which to delete the custom channel.
    String customChannelId = "customChannelId_example"; // String | Custom channel to delete.
    String alt = "csv"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      CustomChannel result = apiInstance.adsensehostCustomchannelsDelete(adClientId, customChannelId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomchannelsApi#adsensehostCustomchannelsDelete");
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
| **adClientId** | **String**| Ad client from which to delete the custom channel. | |
| **customChannelId** | **String**| Custom channel to delete. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: csv, json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

[**CustomChannel**](CustomChannel.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="adsensehostCustomchannelsGet"></a>
# **adsensehostCustomchannelsGet**
> CustomChannel adsensehostCustomchannelsGet(adClientId, customChannelId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Get a specific custom channel from the host AdSense account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomchannelsApi;

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

    CustomchannelsApi apiInstance = new CustomchannelsApi(defaultClient);
    String adClientId = "adClientId_example"; // String | Ad client from which to get the custom channel.
    String customChannelId = "customChannelId_example"; // String | Custom channel to get.
    String alt = "csv"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      CustomChannel result = apiInstance.adsensehostCustomchannelsGet(adClientId, customChannelId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomchannelsApi#adsensehostCustomchannelsGet");
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
| **adClientId** | **String**| Ad client from which to get the custom channel. | |
| **customChannelId** | **String**| Custom channel to get. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: csv, json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

[**CustomChannel**](CustomChannel.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="adsensehostCustomchannelsInsert"></a>
# **adsensehostCustomchannelsInsert**
> CustomChannel adsensehostCustomchannelsInsert(adClientId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, customChannel)



Add a new custom channel to the host AdSense account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomchannelsApi;

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

    CustomchannelsApi apiInstance = new CustomchannelsApi(defaultClient);
    String adClientId = "adClientId_example"; // String | Ad client to which the new custom channel will be added.
    String alt = "csv"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    CustomChannel customChannel = new CustomChannel(); // CustomChannel | 
    try {
      CustomChannel result = apiInstance.adsensehostCustomchannelsInsert(adClientId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, customChannel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomchannelsApi#adsensehostCustomchannelsInsert");
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
| **adClientId** | **String**| Ad client to which the new custom channel will be added. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: csv, json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **customChannel** | [**CustomChannel**](CustomChannel.md)|  | [optional] |

### Return type

[**CustomChannel**](CustomChannel.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="adsensehostCustomchannelsList"></a>
# **adsensehostCustomchannelsList**
> CustomChannels adsensehostCustomchannelsList(adClientId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, maxResults, pageToken)



List all host custom channels in this AdSense account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomchannelsApi;

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

    CustomchannelsApi apiInstance = new CustomchannelsApi(defaultClient);
    String adClientId = "adClientId_example"; // String | Ad client for which to list custom channels.
    String alt = "csv"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Integer maxResults = 56; // Integer | The maximum number of custom channels to include in the response, used for paging.
    String pageToken = "pageToken_example"; // String | A continuation token, used to page through custom channels. To retrieve the next page, set this parameter to the value of \"nextPageToken\" from the previous response.
    try {
      CustomChannels result = apiInstance.adsensehostCustomchannelsList(adClientId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, maxResults, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomchannelsApi#adsensehostCustomchannelsList");
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
| **adClientId** | **String**| Ad client for which to list custom channels. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: csv, json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **maxResults** | **Integer**| The maximum number of custom channels to include in the response, used for paging. | [optional] |
| **pageToken** | **String**| A continuation token, used to page through custom channels. To retrieve the next page, set this parameter to the value of \&quot;nextPageToken\&quot; from the previous response. | [optional] |

### Return type

[**CustomChannels**](CustomChannels.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="adsensehostCustomchannelsPatch"></a>
# **adsensehostCustomchannelsPatch**
> CustomChannel adsensehostCustomchannelsPatch(adClientId, customChannelId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, customChannel)



Update a custom channel in the host AdSense account. This method supports patch semantics.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomchannelsApi;

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

    CustomchannelsApi apiInstance = new CustomchannelsApi(defaultClient);
    String adClientId = "adClientId_example"; // String | Ad client in which the custom channel will be updated.
    String customChannelId = "customChannelId_example"; // String | Custom channel to get.
    String alt = "csv"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    CustomChannel customChannel = new CustomChannel(); // CustomChannel | 
    try {
      CustomChannel result = apiInstance.adsensehostCustomchannelsPatch(adClientId, customChannelId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, customChannel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomchannelsApi#adsensehostCustomchannelsPatch");
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
| **adClientId** | **String**| Ad client in which the custom channel will be updated. | |
| **customChannelId** | **String**| Custom channel to get. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: csv, json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **customChannel** | [**CustomChannel**](CustomChannel.md)|  | [optional] |

### Return type

[**CustomChannel**](CustomChannel.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="adsensehostCustomchannelsUpdate"></a>
# **adsensehostCustomchannelsUpdate**
> CustomChannel adsensehostCustomchannelsUpdate(adClientId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, customChannel)



Update a custom channel in the host AdSense account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomchannelsApi;

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

    CustomchannelsApi apiInstance = new CustomchannelsApi(defaultClient);
    String adClientId = "adClientId_example"; // String | Ad client in which the custom channel will be updated.
    String alt = "csv"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    CustomChannel customChannel = new CustomChannel(); // CustomChannel | 
    try {
      CustomChannel result = apiInstance.adsensehostCustomchannelsUpdate(adClientId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, customChannel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomchannelsApi#adsensehostCustomchannelsUpdate");
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
| **adClientId** | **String**| Ad client in which the custom channel will be updated. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: csv, json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **customChannel** | [**CustomChannel**](CustomChannel.md)|  | [optional] |

### Return type

[**CustomChannel**](CustomChannel.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

