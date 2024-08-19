# BookmarksApi

All URIs are relative to *https://api.twitter.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getUsersIdBookmarks**](BookmarksApi.md#getUsersIdBookmarks) | **GET** /2/users/{id}/bookmarks | Bookmarks by User |
| [**postUsersIdBookmarks**](BookmarksApi.md#postUsersIdBookmarks) | **POST** /2/users/{id}/bookmarks | Add Tweet to Bookmarks |
| [**usersIdBookmarksDelete**](BookmarksApi.md#usersIdBookmarksDelete) | **DELETE** /2/users/{id}/bookmarks/{tweet_id} | Remove a bookmarked Tweet |


<a id="getUsersIdBookmarks"></a>
# **getUsersIdBookmarks**
> Get2UsersIdBookmarksResponse getUsersIdBookmarks(id, maxResults, paginationToken, tweetFields, expansions, mediaFields, pollFields, userFields, placeFields)

Bookmarks by User

Returns Tweet objects that have been bookmarked by the requesting User

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookmarksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twitter.com");
    
    // Configure OAuth2 access token for authorization: OAuth2UserToken
    OAuth OAuth2UserToken = (OAuth) defaultClient.getAuthentication("OAuth2UserToken");
    OAuth2UserToken.setAccessToken("YOUR ACCESS TOKEN");

    BookmarksApi apiInstance = new BookmarksApi(defaultClient);
    String id = "id_example"; // String | The ID of the authenticated source User for whom to return results.
    Integer maxResults = 56; // Integer | The maximum number of results.
    String paginationToken = "paginationToken_example"; // String | This parameter is used to get the next 'page' of results.
    Set<String> tweetFields = Arrays.asList(); // Set<String> | A comma separated list of Tweet fields to display.
    Set<String> expansions = Arrays.asList(); // Set<String> | A comma separated list of fields to expand.
    Set<String> mediaFields = Arrays.asList(); // Set<String> | A comma separated list of Media fields to display.
    Set<String> pollFields = Arrays.asList(); // Set<String> | A comma separated list of Poll fields to display.
    Set<String> userFields = Arrays.asList(); // Set<String> | A comma separated list of User fields to display.
    Set<String> placeFields = Arrays.asList(); // Set<String> | A comma separated list of Place fields to display.
    try {
      Get2UsersIdBookmarksResponse result = apiInstance.getUsersIdBookmarks(id, maxResults, paginationToken, tweetFields, expansions, mediaFields, pollFields, userFields, placeFields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookmarksApi#getUsersIdBookmarks");
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
| **id** | **String**| The ID of the authenticated source User for whom to return results. | |
| **maxResults** | **Integer**| The maximum number of results. | [optional] |
| **paginationToken** | **String**| This parameter is used to get the next &#39;page&#39; of results. | [optional] |
| **tweetFields** | [**Set&lt;String&gt;**](String.md)| A comma separated list of Tweet fields to display. | [optional] [enum: attachments, author_id, context_annotations, conversation_id, created_at, edit_controls, edit_history_tweet_ids, entities, geo, id, in_reply_to_user_id, lang, non_public_metrics, organic_metrics, possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets, reply_settings, source, text, withheld] |
| **expansions** | [**Set&lt;String&gt;**](String.md)| A comma separated list of fields to expand. | [optional] [enum: attachments.media_keys, attachments.poll_ids, author_id, edit_history_tweet_ids, entities.mentions.username, geo.place_id, in_reply_to_user_id, referenced_tweets.id, referenced_tweets.id.author_id] |
| **mediaFields** | [**Set&lt;String&gt;**](String.md)| A comma separated list of Media fields to display. | [optional] [enum: alt_text, duration_ms, height, media_key, non_public_metrics, organic_metrics, preview_image_url, promoted_metrics, public_metrics, type, url, variants, width] |
| **pollFields** | [**Set&lt;String&gt;**](String.md)| A comma separated list of Poll fields to display. | [optional] [enum: duration_minutes, end_datetime, id, options, voting_status] |
| **userFields** | [**Set&lt;String&gt;**](String.md)| A comma separated list of User fields to display. | [optional] [enum: created_at, description, entities, id, location, name, pinned_tweet_id, profile_image_url, protected, public_metrics, url, username, verified, verified_type, withheld] |
| **placeFields** | [**Set&lt;String&gt;**](String.md)| A comma separated list of Place fields to display. | [optional] [enum: contained_within, country, country_code, full_name, geo, id, name, place_type] |

### Return type

[**Get2UsersIdBookmarksResponse**](Get2UsersIdBookmarksResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request has succeeded. |  -  |
| **0** | The request has failed. |  -  |

<a id="postUsersIdBookmarks"></a>
# **postUsersIdBookmarks**
> BookmarkMutationResponse postUsersIdBookmarks(id, bookmarkAddRequest)

Add Tweet to Bookmarks

Adds a Tweet (ID in the body) to the requesting User&#39;s (in the path) bookmarks

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookmarksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twitter.com");
    
    // Configure OAuth2 access token for authorization: OAuth2UserToken
    OAuth OAuth2UserToken = (OAuth) defaultClient.getAuthentication("OAuth2UserToken");
    OAuth2UserToken.setAccessToken("YOUR ACCESS TOKEN");

    BookmarksApi apiInstance = new BookmarksApi(defaultClient);
    String id = "id_example"; // String | The ID of the authenticated source User for whom to add bookmarks.
    BookmarkAddRequest bookmarkAddRequest = new BookmarkAddRequest(); // BookmarkAddRequest | 
    try {
      BookmarkMutationResponse result = apiInstance.postUsersIdBookmarks(id, bookmarkAddRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookmarksApi#postUsersIdBookmarks");
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
| **id** | **String**| The ID of the authenticated source User for whom to add bookmarks. | |
| **bookmarkAddRequest** | [**BookmarkAddRequest**](BookmarkAddRequest.md)|  | |

### Return type

[**BookmarkMutationResponse**](BookmarkMutationResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request has succeeded. |  -  |
| **0** | The request has failed. |  -  |

<a id="usersIdBookmarksDelete"></a>
# **usersIdBookmarksDelete**
> BookmarkMutationResponse usersIdBookmarksDelete(id, tweetId)

Remove a bookmarked Tweet

Removes a Tweet from the requesting User&#39;s bookmarked Tweets.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookmarksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twitter.com");
    
    // Configure OAuth2 access token for authorization: OAuth2UserToken
    OAuth OAuth2UserToken = (OAuth) defaultClient.getAuthentication("OAuth2UserToken");
    OAuth2UserToken.setAccessToken("YOUR ACCESS TOKEN");

    BookmarksApi apiInstance = new BookmarksApi(defaultClient);
    String id = "id_example"; // String | The ID of the authenticated source User whose bookmark is to be removed.
    String tweetId = "tweetId_example"; // String | The ID of the Tweet that the source User is removing from bookmarks.
    try {
      BookmarkMutationResponse result = apiInstance.usersIdBookmarksDelete(id, tweetId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookmarksApi#usersIdBookmarksDelete");
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
| **id** | **String**| The ID of the authenticated source User whose bookmark is to be removed. | |
| **tweetId** | **String**| The ID of the Tweet that the source User is removing from bookmarks. | |

### Return type

[**BookmarkMutationResponse**](BookmarkMutationResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request has succeeded. |  -  |
| **0** | The request has failed. |  -  |

