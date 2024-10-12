# ReviewsApi

All URIs are relative to *https://www.googleapis.com/androidpublisher/v2/applications*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**androidpublisherReviewsGet**](ReviewsApi.md#androidpublisherReviewsGet) | **GET** /{packageName}/reviews/{reviewId} |  |
| [**androidpublisherReviewsList**](ReviewsApi.md#androidpublisherReviewsList) | **GET** /{packageName}/reviews |  |
| [**androidpublisherReviewsReply**](ReviewsApi.md#androidpublisherReviewsReply) | **POST** /{packageName}/reviews/{reviewId}:reply |  |


<a id="androidpublisherReviewsGet"></a>
# **androidpublisherReviewsGet**
> Review androidpublisherReviewsGet(packageName, reviewId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, translationLanguage)



Returns a single review.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReviewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ReviewsApi apiInstance = new ReviewsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app for which we want reviews; for example, \"com.spiffygame\".
    String reviewId = "reviewId_example"; // String | 
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    String translationLanguage = "translationLanguage_example"; // String | 
    try {
      Review result = apiInstance.androidpublisherReviewsGet(packageName, reviewId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, translationLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReviewsApi#androidpublisherReviewsGet");
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
| **packageName** | **String**| Unique identifier for the Android app for which we want reviews; for example, \&quot;com.spiffygame\&quot;. | |
| **reviewId** | **String**|  | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **translationLanguage** | **String**|  | [optional] |

### Return type

[**Review**](Review.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherReviewsList"></a>
# **androidpublisherReviewsList**
> ReviewsListResponse androidpublisherReviewsList(packageName, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, maxResults, startIndex, token, translationLanguage)



Returns a list of reviews. Only reviews from last week will be returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReviewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ReviewsApi apiInstance = new ReviewsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app for which we want reviews; for example, \"com.spiffygame\".
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Integer maxResults = 56; // Integer | 
    Integer startIndex = 56; // Integer | 
    String token = "token_example"; // String | 
    String translationLanguage = "translationLanguage_example"; // String | 
    try {
      ReviewsListResponse result = apiInstance.androidpublisherReviewsList(packageName, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, maxResults, startIndex, token, translationLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReviewsApi#androidpublisherReviewsList");
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
| **packageName** | **String**| Unique identifier for the Android app for which we want reviews; for example, \&quot;com.spiffygame\&quot;. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **maxResults** | **Integer**|  | [optional] |
| **startIndex** | **Integer**|  | [optional] |
| **token** | **String**|  | [optional] |
| **translationLanguage** | **String**|  | [optional] |

### Return type

[**ReviewsListResponse**](ReviewsListResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherReviewsReply"></a>
# **androidpublisherReviewsReply**
> ReviewsReplyResponse androidpublisherReviewsReply(packageName, reviewId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, reviewsReplyRequest)



Reply to a single review, or update an existing reply.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReviewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ReviewsApi apiInstance = new ReviewsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app for which we want reviews; for example, \"com.spiffygame\".
    String reviewId = "reviewId_example"; // String | 
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    ReviewsReplyRequest reviewsReplyRequest = new ReviewsReplyRequest(); // ReviewsReplyRequest | 
    try {
      ReviewsReplyResponse result = apiInstance.androidpublisherReviewsReply(packageName, reviewId, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, reviewsReplyRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReviewsApi#androidpublisherReviewsReply");
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
| **packageName** | **String**| Unique identifier for the Android app for which we want reviews; for example, \&quot;com.spiffygame\&quot;. | |
| **reviewId** | **String**|  | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **reviewsReplyRequest** | [**ReviewsReplyRequest**](ReviewsReplyRequest.md)|  | [optional] |

### Return type

[**ReviewsReplyResponse**](ReviewsReplyResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

