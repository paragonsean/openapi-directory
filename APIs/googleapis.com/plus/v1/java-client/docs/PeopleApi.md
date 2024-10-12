# PeopleApi

All URIs are relative to *https://www.googleapis.com/plus/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**plusPeopleGet**](PeopleApi.md#plusPeopleGet) | **GET** /people/{userId} |  |
| [**plusPeopleList**](PeopleApi.md#plusPeopleList) | **GET** /people/{userId}/people/{collection} |  |
| [**plusPeopleListByActivity**](PeopleApi.md#plusPeopleListByActivity) | **GET** /activities/{activityId}/people/{collection} |  |
| [**plusPeopleSearch**](PeopleApi.md#plusPeopleSearch) | **GET** /people |  |


<a id="plusPeopleGet"></a>
# **plusPeopleGet**
> Person plusPeopleGet(userId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Get a person&#39;s profile. If your app uses scope https://www.googleapis.com/auth/plus.login, this method is guaranteed to return ageRange and language.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeopleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/plus/v1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PeopleApi apiInstance = new PeopleApi(defaultClient);
    String userId = "userId_example"; // String | The ID of the person to get the profile for. The special value \"me\" can be used to indicate the authenticated user.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      Person result = apiInstance.plusPeopleGet(userId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeopleApi#plusPeopleGet");
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
| **userId** | **String**| The ID of the person to get the profile for. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

[**Person**](Person.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="plusPeopleList"></a>
# **plusPeopleList**
> PeopleFeed plusPeopleList(userId, collection, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, maxResults, orderBy, pageToken)



List all of the people in the specified collection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeopleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/plus/v1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PeopleApi apiInstance = new PeopleApi(defaultClient);
    String userId = "userId_example"; // String | Get the collection of people for the person identified. Use \"me\" to indicate the authenticated user.
    String collection = "connected"; // String | The collection of people to list.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Integer maxResults = 56; // Integer | The maximum number of people to include in the response, which is used for paging. For any response, the actual number returned might be less than the specified maxResults.
    String orderBy = "alphabetical"; // String | The order to return people in.
    String pageToken = "pageToken_example"; // String | The continuation token, which is used to page through large result sets. To get the next page of results, set this parameter to the value of \"nextPageToken\" from the previous response.
    try {
      PeopleFeed result = apiInstance.plusPeopleList(userId, collection, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, maxResults, orderBy, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeopleApi#plusPeopleList");
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
| **userId** | **String**| Get the collection of people for the person identified. Use \&quot;me\&quot; to indicate the authenticated user. | |
| **collection** | **String**| The collection of people to list. | [enum: connected, visible] |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **maxResults** | **Integer**| The maximum number of people to include in the response, which is used for paging. For any response, the actual number returned might be less than the specified maxResults. | [optional] |
| **orderBy** | **String**| The order to return people in. | [optional] [enum: alphabetical, best] |
| **pageToken** | **String**| The continuation token, which is used to page through large result sets. To get the next page of results, set this parameter to the value of \&quot;nextPageToken\&quot; from the previous response. | [optional] |

### Return type

[**PeopleFeed**](PeopleFeed.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="plusPeopleListByActivity"></a>
# **plusPeopleListByActivity**
> PeopleFeed plusPeopleListByActivity(activityId, collection, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, maxResults, pageToken)



Shut down. See https://developers.google.com/+/api-shutdown for more details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeopleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/plus/v1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PeopleApi apiInstance = new PeopleApi(defaultClient);
    String activityId = "activityId_example"; // String | The ID of the activity to get the list of people for.
    String collection = "plusoners"; // String | The collection of people to list.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Integer maxResults = 56; // Integer | The maximum number of people to include in the response, which is used for paging. For any response, the actual number returned might be less than the specified maxResults.
    String pageToken = "pageToken_example"; // String | The continuation token, which is used to page through large result sets. To get the next page of results, set this parameter to the value of \"nextPageToken\" from the previous response.
    try {
      PeopleFeed result = apiInstance.plusPeopleListByActivity(activityId, collection, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, maxResults, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeopleApi#plusPeopleListByActivity");
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
| **activityId** | **String**| The ID of the activity to get the list of people for. | |
| **collection** | **String**| The collection of people to list. | [enum: plusoners, resharers] |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **maxResults** | **Integer**| The maximum number of people to include in the response, which is used for paging. For any response, the actual number returned might be less than the specified maxResults. | [optional] |
| **pageToken** | **String**| The continuation token, which is used to page through large result sets. To get the next page of results, set this parameter to the value of \&quot;nextPageToken\&quot; from the previous response. | [optional] |

### Return type

[**PeopleFeed**](PeopleFeed.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="plusPeopleSearch"></a>
# **plusPeopleSearch**
> PeopleFeed plusPeopleSearch(query, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, language, maxResults, pageToken)



Shut down. See https://developers.google.com/+/api-shutdown for more details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeopleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/plus/v1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PeopleApi apiInstance = new PeopleApi(defaultClient);
    String query = "query_example"; // String | Specify a query string for full text search of public text in all profiles.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String language = "language_example"; // String | Specify the preferred language to search with. See search language codes for available values.
    Integer maxResults = 56; // Integer | The maximum number of people to include in the response, which is used for paging. For any response, the actual number returned might be less than the specified maxResults.
    String pageToken = "pageToken_example"; // String | The continuation token, which is used to page through large result sets. To get the next page of results, set this parameter to the value of \"nextPageToken\" from the previous response. This token can be of any length.
    try {
      PeopleFeed result = apiInstance.plusPeopleSearch(query, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, language, maxResults, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeopleApi#plusPeopleSearch");
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
| **query** | **String**| Specify a query string for full text search of public text in all profiles. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **language** | **String**| Specify the preferred language to search with. See search language codes for available values. | [optional] |
| **maxResults** | **Integer**| The maximum number of people to include in the response, which is used for paging. For any response, the actual number returned might be less than the specified maxResults. | [optional] |
| **pageToken** | **String**| The continuation token, which is used to page through large result sets. To get the next page of results, set this parameter to the value of \&quot;nextPageToken\&quot; from the previous response. This token can be of any length. | [optional] |

### Return type

[**PeopleFeed**](PeopleFeed.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

