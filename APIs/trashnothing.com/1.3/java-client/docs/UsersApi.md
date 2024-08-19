# UsersApi

All URIs are relative to *https://trashnothing.com/api/v1.3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getUserPosts**](UsersApi.md#getUserPosts) | **GET** /users/{user_id}/posts | List posts by a user |
| [**searchUserPosts**](UsersApi.md#searchUserPosts) | **GET** /users/{user_id}/posts/search | Search posts by a user |


<a id="getUserPosts"></a>
# **getUserPosts**
> GetPosts200Response getUserPosts(userId, types, sources, sortBy, groupIds, perPage, page, devicePixelRatio, latitude, longitude, radius, dateMin, dateMax, outcomes, includeReposts)

List posts by a user



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trashnothing.com/api/v1.3");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String userId = "userId_example"; // String | The user ID of the user whose posts will be retrieved. Using 'me' as the user_id will return the posts for the current user. 
    String types = "types_example"; // String | A comma separated list of the post types to return.  The available post types are: offer, taken, wanted, received, admin 
    String sources = "sources_example"; // String | A comma separated list of the post sources to retrieve posts from. The available sources are: groups, trashnothing, open_archive_groups. The trashnothing source is for public posts that are posted on trash nothing but are not associated with any group. The open_archive_groups source provides a way to easily request posts from groups that have open_archives set to true without having to pass a group_ids parameter.  When passed, it will automatically return posts from open archive groups that are within the area specified by the latitude, longitude and radius parameters (or all the open archive groups the requested user has posted to if latitude, longitude and radius aren't passed). <br /><br /> NOTE: For requests using an api key instead of oauth, passing the trashnothing source or the open_archive_groups source makes the latitude, longitude and radius parameters required. 
    String sortBy = "date"; // String | How to sort the posts that are returned.  One of: date, active, distance <br /><br /> Date sorting will sort posts from newest to oldest. Active sorting will sort active posts before satisfied, withdrawn and expired posts and then sort by date. Distance sorting will sort the closest posts first. 
    String groupIds = "The group IDs of every group the current user is a member of."; // String | A comma separated list of the group IDs to retrieve posts from. This parameter is only used if the 'groups' source is passed in the sources parameter and only groups that the current user is a member of or that are open archives groups will be used (the group IDs of other groups will be silently discarded*). <br /><br /> NOTE: For requests using an api key instead of oauth, this field is required if the 'groups' source is passed. In addition, only posts from groups that have open_archives set to true will be used (the group IDS of other groups will be silently discarded*). <br /><br/> *To determine which group IDs were used and which were discarded, use the group_ids field in the response. 
    Integer perPage = 20; // Integer | The number of posts to return per page (must be >= 1 and <= 100).
    Integer page = 1; // Integer | The page of posts to return.
    BigDecimal devicePixelRatio = new BigDecimal("1"); // BigDecimal | Client device pixel ratio used to determine thumbnail size (default 1.0).
    BigDecimal latitude = new BigDecimal(78); // BigDecimal | The latitude of a point around which to return posts. 
    BigDecimal longitude = new BigDecimal(78); // BigDecimal | The longitude of a point around which to return posts. 
    BigDecimal radius = new BigDecimal(78); // BigDecimal | The radius in meters of a circle centered at the point defined by the latitude and longitude parameters. When latitude, longitude and radius are passed, only posts within the circle defined by these parameters will be returned. 
    OffsetDateTime dateMin = OffsetDateTime.now(); // OffsetDateTime | Only posts newer than or equal to this UTC date and time will be returned. 
    OffsetDateTime dateMax = OffsetDateTime.now(); // OffsetDateTime | Only posts older than this UTC date and time will be returned.
    String outcomes = ""; // String | A comma separated list of the post outcomes to return.  The available post outcomes are: satisfied, withdrawn <br /><br /> There are also a couple special values that can be passed.  If set to an empty string (the default), only posts that are not satisfied and not withdrawn and not expired are returned. If set to 'all', all posts will be returned no matter what outcome the posts have. If set to 'not-promised', only posts that are not satisfied ant not withdrawn and not expired and not promised are returned. 
    Integer includeReposts = 1; // Integer | If set to 1 (the default), posts that are reposts will be included. If set to 0, reposts will be excluded. See the repost_count field of post objects for details about how reposts are identified. 
    try {
      GetPosts200Response result = apiInstance.getUserPosts(userId, types, sources, sortBy, groupIds, perPage, page, devicePixelRatio, latitude, longitude, radius, dateMin, dateMax, outcomes, includeReposts);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getUserPosts");
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
| **userId** | **String**| The user ID of the user whose posts will be retrieved. Using &#39;me&#39; as the user_id will return the posts for the current user.  | |
| **types** | **String**| A comma separated list of the post types to return.  The available post types are: offer, taken, wanted, received, admin  | |
| **sources** | **String**| A comma separated list of the post sources to retrieve posts from. The available sources are: groups, trashnothing, open_archive_groups. The trashnothing source is for public posts that are posted on trash nothing but are not associated with any group. The open_archive_groups source provides a way to easily request posts from groups that have open_archives set to true without having to pass a group_ids parameter.  When passed, it will automatically return posts from open archive groups that are within the area specified by the latitude, longitude and radius parameters (or all the open archive groups the requested user has posted to if latitude, longitude and radius aren&#39;t passed). &lt;br /&gt;&lt;br /&gt; NOTE: For requests using an api key instead of oauth, passing the trashnothing source or the open_archive_groups source makes the latitude, longitude and radius parameters required.  | |
| **sortBy** | **String**| How to sort the posts that are returned.  One of: date, active, distance &lt;br /&gt;&lt;br /&gt; Date sorting will sort posts from newest to oldest. Active sorting will sort active posts before satisfied, withdrawn and expired posts and then sort by date. Distance sorting will sort the closest posts first.  | [optional] [default to date] |
| **groupIds** | **String**| A comma separated list of the group IDs to retrieve posts from. This parameter is only used if the &#39;groups&#39; source is passed in the sources parameter and only groups that the current user is a member of or that are open archives groups will be used (the group IDs of other groups will be silently discarded*). &lt;br /&gt;&lt;br /&gt; NOTE: For requests using an api key instead of oauth, this field is required if the &#39;groups&#39; source is passed. In addition, only posts from groups that have open_archives set to true will be used (the group IDS of other groups will be silently discarded*). &lt;br /&gt;&lt;br/&gt; *To determine which group IDs were used and which were discarded, use the group_ids field in the response.  | [optional] [default to The group IDs of every group the current user is a member of.] |
| **perPage** | **Integer**| The number of posts to return per page (must be &gt;&#x3D; 1 and &lt;&#x3D; 100). | [optional] [default to 20] |
| **page** | **Integer**| The page of posts to return. | [optional] [default to 1] |
| **devicePixelRatio** | **BigDecimal**| Client device pixel ratio used to determine thumbnail size (default 1.0). | [optional] [default to 1] |
| **latitude** | **BigDecimal**| The latitude of a point around which to return posts.  | [optional] |
| **longitude** | **BigDecimal**| The longitude of a point around which to return posts.  | [optional] |
| **radius** | **BigDecimal**| The radius in meters of a circle centered at the point defined by the latitude and longitude parameters. When latitude, longitude and radius are passed, only posts within the circle defined by these parameters will be returned.  | [optional] |
| **dateMin** | **OffsetDateTime**| Only posts newer than or equal to this UTC date and time will be returned.  | [optional] |
| **dateMax** | **OffsetDateTime**| Only posts older than this UTC date and time will be returned. | [optional] |
| **outcomes** | **String**| A comma separated list of the post outcomes to return.  The available post outcomes are: satisfied, withdrawn &lt;br /&gt;&lt;br /&gt; There are also a couple special values that can be passed.  If set to an empty string (the default), only posts that are not satisfied and not withdrawn and not expired are returned. If set to &#39;all&#39;, all posts will be returned no matter what outcome the posts have. If set to &#39;not-promised&#39;, only posts that are not satisfied ant not withdrawn and not expired and not promised are returned.  | [optional] [default to ] |
| **includeReposts** | **Integer**| If set to 1 (the default), posts that are reposts will be included. If set to 0, reposts will be excluded. See the repost_count field of post objects for details about how reposts are identified.  | [optional] [default to 1] |

### Return type

[**GetPosts200Response**](GetPosts200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The posts and paging data. |  -  |
| **400** | Missing or invalid parameters. |  -  |

<a id="searchUserPosts"></a>
# **searchUserPosts**
> SearchPosts200Response searchUserPosts(userId, search, types, sources, sortBy, groupIds, perPage, page, devicePixelRatio, latitude, longitude, radius, dateMin, dateMax, outcomes, includeReposts)

Search posts by a user

Searching posts takes the same arguments as listing posts except for the addition of the search and sort_by parameters. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trashnothing.com/api/v1.3");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String userId = "userId_example"; // String | The user ID of the user whose posts will be retrieved. Using 'me' as the user_id will return the posts for the current user. 
    String search = "search_example"; // String | The search query used to find posts.
    String types = "types_example"; // String | A comma separated list of the post types to return.  The available post types are: offer, taken, wanted, received, admin 
    String sources = "sources_example"; // String | A comma separated list of the post sources to retrieve posts from. The available sources are: groups, trashnothing, open_archive_groups. The trashnothing source is for public posts that are posted on trash nothing but are not associated with any group. The open_archive_groups source provides a way to easily request posts from groups that have open_archives set to true without having to pass a group_ids parameter.  When passed, it will automatically return posts from open archive groups that are within the area specified by the latitude, longitude and radius parameters (or all the open archive groups the requested user has posted to if latitude, longitude and radius aren't passed). <br /><br /> NOTE: For requests using an api key instead of oauth, passing the trashnothing source or the open_archive_groups source makes the latitude, longitude and radius parameters required. 
    String sortBy = "relevance"; // String | How to sort the posts that are returned.  One of: relevance, date, active, distance <br /><br /> Relevance sorting will sort the posts that best match the search query first. Date sorting will sort posts from newest to oldest. Active sorting will sort active posts before satisfied, withdrawn and expired posts and then sort by date. Distance sorting will sort the closest posts first. 
    String groupIds = "The group IDs of every group the current user is a member of."; // String | A comma separated list of the group IDs to retrieve posts from. This parameter is only used if the 'groups' source is passed in the sources parameter and only groups that the current user is a member of or that are open archives groups will be used (the group IDs of other groups will be silently discarded*). <br /><br /> NOTE: For requests using an api key instead of oauth, this field is required if the 'groups' source is passed. In addition, only posts from groups that have open_archives set to true will be used (the group IDS of other groups will be silently discarded*). <br /><br/> *To determine which group IDs were used and which were discarded, use the group_ids field in the response. 
    Integer perPage = 20; // Integer | The number of posts to return per page (must be >= 1 and <= 100).
    Integer page = 1; // Integer | The page of posts to return.
    BigDecimal devicePixelRatio = new BigDecimal("1"); // BigDecimal | Client device pixel ratio used to determine thumbnail size (default 1.0).
    BigDecimal latitude = new BigDecimal(78); // BigDecimal | The latitude of a point around which to return posts. 
    BigDecimal longitude = new BigDecimal(78); // BigDecimal | The longitude of a point around which to return posts. 
    BigDecimal radius = new BigDecimal(78); // BigDecimal | The radius in meters of a circle centered at the point defined by the latitude and longitude parameters. When latitude, longitude and radius are passed, only posts within the circle defined by these parameters will be returned. 
    OffsetDateTime dateMin = OffsetDateTime.now(); // OffsetDateTime | Only posts newer than or equal to this UTC date and time will be returned. 
    OffsetDateTime dateMax = OffsetDateTime.now(); // OffsetDateTime | Only posts older than this UTC date and time will be returned.
    String outcomes = ""; // String | A comma separated list of the post outcomes to return.  The available post outcomes are: satisfied, withdrawn <br /><br /> There are also a couple special values that can be passed.  If set to an empty string (the default), only posts that are not satisfied and not withdrawn and not expired are returned. If set to 'all', all posts will be returned no matter what outcome the posts have. If set to 'not-promised', only posts that are not satisfied ant not withdrawn and not expired and not promised are returned. 
    Integer includeReposts = 1; // Integer | If set to 1 (the default), posts that are reposts will be included. If set to 0, reposts will be excluded. See the repost_count field of post objects for details about how reposts are identified. 
    try {
      SearchPosts200Response result = apiInstance.searchUserPosts(userId, search, types, sources, sortBy, groupIds, perPage, page, devicePixelRatio, latitude, longitude, radius, dateMin, dateMax, outcomes, includeReposts);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#searchUserPosts");
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
| **userId** | **String**| The user ID of the user whose posts will be retrieved. Using &#39;me&#39; as the user_id will return the posts for the current user.  | |
| **search** | **String**| The search query used to find posts. | |
| **types** | **String**| A comma separated list of the post types to return.  The available post types are: offer, taken, wanted, received, admin  | |
| **sources** | **String**| A comma separated list of the post sources to retrieve posts from. The available sources are: groups, trashnothing, open_archive_groups. The trashnothing source is for public posts that are posted on trash nothing but are not associated with any group. The open_archive_groups source provides a way to easily request posts from groups that have open_archives set to true without having to pass a group_ids parameter.  When passed, it will automatically return posts from open archive groups that are within the area specified by the latitude, longitude and radius parameters (or all the open archive groups the requested user has posted to if latitude, longitude and radius aren&#39;t passed). &lt;br /&gt;&lt;br /&gt; NOTE: For requests using an api key instead of oauth, passing the trashnothing source or the open_archive_groups source makes the latitude, longitude and radius parameters required.  | |
| **sortBy** | **String**| How to sort the posts that are returned.  One of: relevance, date, active, distance &lt;br /&gt;&lt;br /&gt; Relevance sorting will sort the posts that best match the search query first. Date sorting will sort posts from newest to oldest. Active sorting will sort active posts before satisfied, withdrawn and expired posts and then sort by date. Distance sorting will sort the closest posts first.  | [optional] [default to relevance] |
| **groupIds** | **String**| A comma separated list of the group IDs to retrieve posts from. This parameter is only used if the &#39;groups&#39; source is passed in the sources parameter and only groups that the current user is a member of or that are open archives groups will be used (the group IDs of other groups will be silently discarded*). &lt;br /&gt;&lt;br /&gt; NOTE: For requests using an api key instead of oauth, this field is required if the &#39;groups&#39; source is passed. In addition, only posts from groups that have open_archives set to true will be used (the group IDS of other groups will be silently discarded*). &lt;br /&gt;&lt;br/&gt; *To determine which group IDs were used and which were discarded, use the group_ids field in the response.  | [optional] [default to The group IDs of every group the current user is a member of.] |
| **perPage** | **Integer**| The number of posts to return per page (must be &gt;&#x3D; 1 and &lt;&#x3D; 100). | [optional] [default to 20] |
| **page** | **Integer**| The page of posts to return. | [optional] [default to 1] |
| **devicePixelRatio** | **BigDecimal**| Client device pixel ratio used to determine thumbnail size (default 1.0). | [optional] [default to 1] |
| **latitude** | **BigDecimal**| The latitude of a point around which to return posts.  | [optional] |
| **longitude** | **BigDecimal**| The longitude of a point around which to return posts.  | [optional] |
| **radius** | **BigDecimal**| The radius in meters of a circle centered at the point defined by the latitude and longitude parameters. When latitude, longitude and radius are passed, only posts within the circle defined by these parameters will be returned.  | [optional] |
| **dateMin** | **OffsetDateTime**| Only posts newer than or equal to this UTC date and time will be returned.  | [optional] |
| **dateMax** | **OffsetDateTime**| Only posts older than this UTC date and time will be returned. | [optional] |
| **outcomes** | **String**| A comma separated list of the post outcomes to return.  The available post outcomes are: satisfied, withdrawn &lt;br /&gt;&lt;br /&gt; There are also a couple special values that can be passed.  If set to an empty string (the default), only posts that are not satisfied and not withdrawn and not expired are returned. If set to &#39;all&#39;, all posts will be returned no matter what outcome the posts have. If set to &#39;not-promised&#39;, only posts that are not satisfied ant not withdrawn and not expired and not promised are returned.  | [optional] [default to ] |
| **includeReposts** | **Integer**| If set to 1 (the default), posts that are reposts will be included. If set to 0, reposts will be excluded. See the repost_count field of post objects for details about how reposts are identified.  | [optional] [default to 1] |

### Return type

[**SearchPosts200Response**](SearchPosts200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The posts and paging data. |  -  |
| **400** | Missing or invalid parameters. |  -  |

