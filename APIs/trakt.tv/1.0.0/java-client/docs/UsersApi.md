# UsersApi

All URIs are relative to *https://api.trakt.tv*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addHiddenItems**](UsersApi.md#addHiddenItems) | **POST** /users/hidden/{section} | Add hidden items |
| [**addItemsToPersonalList**](UsersApi.md#addItemsToPersonalList) | **POST** /users/{id}/lists/{list_id}/items | Add items to personal list |
| [**approveFollowRequest**](UsersApi.md#approveFollowRequest) | **POST** /users/requests/{id} | Approve follow request |
| [**createPersonalList**](UsersApi.md#createPersonalList) | **POST** /users/{id}/lists | Create personal list |
| [**deleteAUsersPersonalList**](UsersApi.md#deleteAUsersPersonalList) | **DELETE** /users/{id}/lists/{list_id} | Delete a user&#39;s personal list |
| [**denyFollowRequest**](UsersApi.md#denyFollowRequest) | **DELETE** /users/requests/{id} | Deny follow request |
| [**followThisUser**](UsersApi.md#followThisUser) | **POST** /users/{id}/follow | Follow this user |
| [**getAUsersPersonalLists**](UsersApi.md#getAUsersPersonalLists) | **GET** /users/{id}/lists | Get a user&#39;s personal lists |
| [**getAllListsAUserCanCollaborateOn**](UsersApi.md#getAllListsAUserCanCollaborateOn) | **GET** /users/{id}/lists/collaborations | Get all lists a user can collaborate on |
| [**getComments**](UsersApi.md#getComments) | **GET** /users/{id}/comments/{comment_type}/{type} | Get comments |
| [**getFollowRequests**](UsersApi.md#getFollowRequests) | **GET** /users/requests | Get follow requests |
| [**getFollowers**](UsersApi.md#getFollowers) | **GET** /users/{id}/followers | Get followers |
| [**getFollowing**](UsersApi.md#getFollowing) | **GET** /users/{id}/following | Get following |
| [**getFriends**](UsersApi.md#getFriends) | **GET** /users/{id}/friends | Get friends |
| [**getHiddenItems**](UsersApi.md#getHiddenItems) | **GET** /users/hidden/{section} | Get hidden items |
| [**getItemsOnAPersonalList**](UsersApi.md#getItemsOnAPersonalList) | **GET** /users/{id}/lists/{list_id}/items/{type} | Get items on a personal list |
| [**getLikes**](UsersApi.md#getLikes) | **GET** /users/{id}/likes/{type} | Get likes |
| [**getPendingFollowingRequests**](UsersApi.md#getPendingFollowingRequests) | **GET** /users/requests/following | Get pending following requests |
| [**getPersonalList**](UsersApi.md#getPersonalList) | **GET** /users/{id}/lists/{list_id} | Get personal list |
| [**getSavedFilters**](UsersApi.md#getSavedFilters) | **GET** /users/saved_filters/{section} | Get saved filters |
| [**getStats**](UsersApi.md#getStats) | **GET** /users/{id}/stats | Get stats |
| [**getUserProfile**](UsersApi.md#getUserProfile) | **GET** /users/{id} | Get user profile |
| [**getWatching**](UsersApi.md#getWatching) | **GET** /users/{id}/watching | Get watching |
| [**likeAList**](UsersApi.md#likeAList) | **POST** /users/{id}/lists/{list_id}/like | Like a list |
| [**removeHiddenItems**](UsersApi.md#removeHiddenItems) | **POST** /users/hidden/{section}/remove | Remove hidden items |
| [**removeItemsFromPersonalList**](UsersApi.md#removeItemsFromPersonalList) | **POST** /users/{id}/lists/{list_id}/items/remove | Remove items from personal list |
| [**removeLikeOnAList**](UsersApi.md#removeLikeOnAList) | **DELETE** /users/{id}/lists/{list_id}/like | Remove like on a list |
| [**reorderAUsersLists**](UsersApi.md#reorderAUsersLists) | **POST** /users/{id}/lists/reorder | Reorder a user&#39;s lists |
| [**reorderItemsOnAList**](UsersApi.md#reorderItemsOnAList) | **POST** /users/{id}/lists/{list_id}/items/reorder | Reorder items on a list |
| [**retrieveSettings**](UsersApi.md#retrieveSettings) | **GET** /users/settings | Retrieve settings |
| [**unfollowThisUser**](UsersApi.md#unfollowThisUser) | **DELETE** /users/{id}/follow | Unfollow this user |
| [**updatePersonalList**](UsersApi.md#updatePersonalList) | **PUT** /users/{id}/lists/{list_id} | Update personal list |
| [**usersIdCollectionTypeGet**](UsersApi.md#usersIdCollectionTypeGet) | **GET** /users/{id}/collection/{type} | Get collection |
| [**usersIdHistoryTypeItemIdGet**](UsersApi.md#usersIdHistoryTypeItemIdGet) | **GET** /users/{id}/history/{type}/{item_id} | Get watched history |
| [**usersIdListsListIdCommentsSortGet**](UsersApi.md#usersIdListsListIdCommentsSortGet) | **GET** /users/{id}/lists/{list_id}/comments/{sort} | Get all list comments |
| [**usersIdListsListIdLikesGet**](UsersApi.md#usersIdListsListIdLikesGet) | **GET** /users/{id}/lists/{list_id}/likes | Get all users who liked a list |
| [**usersIdRatingsTypeRatingGet**](UsersApi.md#usersIdRatingsTypeRatingGet) | **GET** /users/{id}/ratings/{type}/{rating} | Get ratings |
| [**usersIdRecommendationsTypeSortGet**](UsersApi.md#usersIdRecommendationsTypeSortGet) | **GET** /users/{id}/recommendations/{type}/{sort} | Get personal recommendations |
| [**usersIdWatchedTypeGet**](UsersApi.md#usersIdWatchedTypeGet) | **GET** /users/{id}/watched/{type} | Get watched |
| [**usersIdWatchlistTypeSortGet**](UsersApi.md#usersIdWatchlistTypeSortGet) | **GET** /users/{id}/watchlist/{type}/{sort} | Get watchlist |


<a id="addHiddenItems"></a>
# **addHiddenItems**
> addHiddenItems(section, traktApiVersion, traktApiKey, addHiddenItemsRequest)

Add hidden items

#### &amp;#128274; OAuth Required  Hide items for a specific section. Here&#39;s what type of items can hidden for each section.  #### Hideable Media Objects  | Section | Objects | |---|---|---| | &#x60;calendar&#x60; | &#x60;movie&#x60;, &#x60;show&#x60; | | &#x60;progress_watched&#x60; | &#x60;show&#x60;, &#x60;season&#x60; | | &#x60;progress_collected&#x60; | &#x60;show&#x60;, &#x60;season&#x60; | | &#x60;recommendations&#x60; | &#x60;movie&#x60;, &#x60;show&#x60; | | &#x60;comments&#x60; | &#x60;user&#x60; |  #### JSON POST Data  | Key | Type | Value | |---|---|---| | &#x60;movies&#x60; | array | Array of &#x60;movie&#x60; objects. (see examples &amp;#8594;) | | &#x60;shows&#x60; | array | Array of &#x60;show&#x60; objects. | | &#x60;seasons&#x60; | array | Array of &#x60;season&#x60; objects. | | &#x60;users&#x60; | array | Array of &#x60;user&#x60; objects. |

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
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String section = "calendar"; // String | 
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    AddHiddenItemsRequest addHiddenItemsRequest = new AddHiddenItemsRequest(); // AddHiddenItemsRequest | 
    try {
      apiInstance.addHiddenItems(section, traktApiVersion, traktApiKey, addHiddenItemsRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#addHiddenItems");
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
| **section** | **String**|  | [enum: calendar, progress_watched, progress_collected, recommendations] |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |
| **addHiddenItemsRequest** | [**AddHiddenItemsRequest**](AddHiddenItemsRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="addItemsToPersonalList"></a>
# **addItemsToPersonalList**
> addItemsToPersonalList(id, listId, traktApiVersion, traktApiKey, addItemsToPersonalListRequest)

Add items to personal list

#### &amp;#128274; OAuth Required &amp;#128513; Emojis 🔥 VIP Enhanced  Add one or more items to a personal list. Items can be movies, shows, seasons, episodes, or people.  #### Notes  Each list item can optionally accept a &#x60;notes&#x60; *(255 maximum characters)* field with custom text. The user must be a [**Trakt VIP**](https://trakt.tv/vip) to send &#x60;notes&#x60;.  #### Limits  If the user&#39;s list item limit is exceeded, a &#x60;420&#x60; HTTP error code is returned. Use the [**_/users/settings**](/reference/users/settings) method to get all limits for a user account. In most cases, upgrading to [**Trakt VIP**](https://trakt.tv/vip) will increase the limits.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | &#x60;movies&#x60; | array | Array of &#x60;movie&#x60; objects. (see examples &amp;#8594;) | | &#x60;shows&#x60; | array | Array of &#x60;show&#x60; objects. | | &#x60;seasons&#x60; | array | Array of &#x60;season&#x60; objects. | | &#x60;episodes&#x60; | array | Array of &#x60;episode&#x60; objects. | | &#x60;people&#x60; | array | Array of &#x60;person&#x60; objects. |

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
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "sean"; // String | User slug
    String listId = "star-wars-in-machete-order"; // String | Trakt ID or Trakt slug
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    AddItemsToPersonalListRequest addItemsToPersonalListRequest = new AddItemsToPersonalListRequest(); // AddItemsToPersonalListRequest | 
    try {
      apiInstance.addItemsToPersonalList(id, listId, traktApiVersion, traktApiKey, addItemsToPersonalListRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#addItemsToPersonalList");
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
| **id** | **String**| User slug | |
| **listId** | **String**| Trakt ID or Trakt slug | |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |
| **addItemsToPersonalListRequest** | [**AddItemsToPersonalListRequest**](AddItemsToPersonalListRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **420** |  |  * X-Account-Limit -  <br>  * X-Upgrade-URL -  <br>  * X-VIP-User -  <br>  |

<a id="approveFollowRequest"></a>
# **approveFollowRequest**
> approveFollowRequest(id, traktApiVersion, traktApiKey)

Approve follow request

#### &amp;#128274; OAuth Required  Approve a follower using the &#x60;id&#x60; of the request. If the &#x60;id&#x60; is not found, was already approved, or was already denied, a &#x60;404&#x60; error will be returned.

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
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "123"; // String | ID of the follower request.
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.approveFollowRequest(id, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#approveFollowRequest");
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
| **id** | **String**| ID of the follower request. | |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="createPersonalList"></a>
# **createPersonalList**
> createPersonalList(id, traktApiVersion, traktApiKey, createPersonalListRequest)

Create personal list

#### &amp;#128274; OAuth Required 🔥 VIP Enhanced  Create a new personal list. The &#x60;name&#x60; is the only required field, but the other info is recommended to ask for.  #### Limits  If the user&#39;s list limit is exceeded, a &#x60;420&#x60; HTTP error code is returned. Use the [**_/users/settings**](/reference/users/settings) method to get all limits for a user account. In most cases, upgrading to [**Trakt VIP**](https://trakt.tv/vip) will increase the limits.  #### Privacy  Lists will be &#x60;private&#x60; by default. Here is what each value means.  | Value | Privacy impact... | |---|---| | &#x60;private&#x60; | Only you can see the list. | | &#x60;link&#x60; | Anyone with the &#x60;share_link&#x60; can see the list. | | &#x60;friends&#x60; | Only your friends can see the list. | | &#x60;public&#x60; | Anyone can see the list. |  #### JSON POST Data  | Key | Type | Default | Value | |---|---|---|---| | &#x60;name&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | string |  | Name of the list. | | &#x60;description&#x60; | string |  | Description for this list. | | &#x60;privacy&#x60; | string | &#x60;private&#x60; | &#x60;private&#x60;, &#x60;link&#x60;, &#x60;friends&#x60;, &#x60;public&#x60; | | &#x60;display_numbers&#x60; | boolean | &#x60;false&#x60; | Should each item be numbered? | | &#x60;allow_comments&#x60; | boolean | &#x60;true&#x60; | Are comments allowed? | | &#x60;sort_by&#x60; | string | &#x60;rank&#x60; | &#x60;rank&#x60;, &#x60;added&#x60;, &#x60;title&#x60;, &#x60;released&#x60;, &#x60;runtime&#x60;, &#x60;popularity&#x60;, &#x60;percentage&#x60;, &#x60;votes&#x60;, &#x60;my_rating&#x60;, &#x60;random&#x60;, &#x60;watched&#x60;, &#x60;collected&#x60; | | &#x60;sort_how&#x60; | string | &#x60;asc&#x60; | &#x60;asc&#x60;, &#x60;desc&#x60; |

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
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "id_example"; // String | Automatically added
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    CreatePersonalListRequest createPersonalListRequest = new CreatePersonalListRequest(); // CreatePersonalListRequest | 
    try {
      apiInstance.createPersonalList(id, traktApiVersion, traktApiKey, createPersonalListRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#createPersonalList");
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
| **id** | **String**| Automatically added | |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |
| **createPersonalListRequest** | [**CreatePersonalListRequest**](CreatePersonalListRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **420** |  |  * X-Account-Limit -  <br>  * X-Upgrade-URL -  <br>  * X-VIP-User -  <br>  |

<a id="deleteAUsersPersonalList"></a>
# **deleteAUsersPersonalList**
> deleteAUsersPersonalList(id, listId, traktApiVersion, traktApiKey)

Delete a user&#39;s personal list

#### &amp;#128274; OAuth Required  Remove a personal list and all items it contains.

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
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "id_example"; // String | Automatically added
    String listId = "listId_example"; // String | Automatically added
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.deleteAUsersPersonalList(id, listId, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#deleteAUsersPersonalList");
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
| **id** | **String**| Automatically added | |
| **listId** | **String**| Automatically added | |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="denyFollowRequest"></a>
# **denyFollowRequest**
> denyFollowRequest(id, traktApiVersion, traktApiKey)

Deny follow request

#### &amp;#128274; OAuth Required  Deny a follower using the &#x60;id&#x60; of the request. If the &#x60;id&#x60; is not found, was already approved, or was already denied, a &#x60;404&#x60; error will be returned.

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
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "id_example"; // String | Automatically added
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.denyFollowRequest(id, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#denyFollowRequest");
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
| **id** | **String**| Automatically added | |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="followThisUser"></a>
# **followThisUser**
> followThisUser(id, traktApiVersion, traktApiKey)

Follow this user

#### &amp;#128274; OAuth Required  If the user has a private profile, the follow request will require approval (&#x60;approved_at&#x60; will be null). If a user is public, they will be followed immediately (&#x60;approved_at&#x60; will have a date).  **Note:** If this user is already being followed, a &#x60;409&#x60; HTTP status code will returned.

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
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "sean"; // String | User slug
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.followThisUser(id, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#followThisUser");
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
| **id** | **String**| User slug | |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="getAUsersPersonalLists"></a>
# **getAUsersPersonalLists**
> getAUsersPersonalLists(id, traktApiVersion, traktApiKey)

Get a user&#39;s personal lists

#### &amp;#128275; OAuth Optional &amp;#128513; Emojis  Returns all personal lists for a user. Use the [**_/users/:id/lists/:list_id/items**](#reference/users/list-items) method to get the actual items a specific list contains.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "sean"; // String | User slug
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getAUsersPersonalLists(id, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getAUsersPersonalLists");
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
| **id** | **String**| User slug | |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getAllListsAUserCanCollaborateOn"></a>
# **getAllListsAUserCanCollaborateOn**
> getAllListsAUserCanCollaborateOn(id, traktApiVersion, traktApiKey)

Get all lists a user can collaborate on

#### &amp;#128275; OAuth Optional  Returns all lists a user can collaborate on. This gives full access to add, remove, and re-order list items. It essentially works just like a list owned by the user, just make sure to use the correct list owner &#x60;user&#x60; when building the API URLs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "sean"; // String | User slug
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getAllListsAUserCanCollaborateOn(id, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getAllListsAUserCanCollaborateOn");
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
| **id** | **String**| User slug | |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getComments"></a>
# **getComments**
> getComments(id, commentType, type, includeReplies, traktApiVersion, traktApiKey)

Get comments

#### &amp;#128275; OAuth Optional &amp;#128196; Pagination &amp;#10024; Extended Info  Returns the most recently written comments for the user. You can optionally filter by the &#x60;comment_type&#x60; and media &#x60;type&#x60; to limit what gets returned.  By default, only top level comments are returned. Set &#x60;?include_replies&#x3D;true&#x60; to return replies in addition to top level comments. Set &#x60;?include_replies&#x3D;only&#x60; to return only replies and no top level comments.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "sean"; // String | User slug
    String commentType = "all"; // String | 
    String type = "all"; // String | 
    String includeReplies = "true"; // String | include comment replies
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getComments(id, commentType, type, includeReplies, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getComments");
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
| **id** | **String**| User slug | |
| **commentType** | **String**|  | [enum: all, reviews, shouts] |
| **type** | **String**|  | [enum: all, movies, shows, seasons, episodes, lists] |
| **includeReplies** | **String**| include comment replies | [optional] [enum: true, false, only] |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | &#x60;&#x60;&#x60; /users/sean/comments &#x60;&#x60;&#x60; |  * X-Pagination-Item-Count -  <br>  * X-Pagination-Limit -  <br>  * X-Pagination-Page -  <br>  * X-Pagination-Page-Count -  <br>  |

<a id="getFollowRequests"></a>
# **getFollowRequests**
> getFollowRequests(traktApiVersion, traktApiKey)

Get follow requests

#### &amp;#128274; OAuth Required &amp;#10024; Extended Info  List a user&#39;s pending follow requests so they can either approve or deny them.

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
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getFollowRequests(traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getFollowRequests");
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
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getFollowers"></a>
# **getFollowers**
> getFollowers(id, traktApiVersion, traktApiKey)

Get followers

#### &amp;#128275; OAuth Optional &amp;#10024; Extended Info  Returns all followers including when the relationship began.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "sean"; // String | User slug
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getFollowers(id, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getFollowers");
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
| **id** | **String**| User slug | |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getFollowing"></a>
# **getFollowing**
> getFollowing(id, traktApiVersion, traktApiKey)

Get following

#### &amp;#128275; OAuth Optional &amp;#10024; Extended Info  Returns all user&#39;s they follow including when the relationship began.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "sean"; // String | User slug
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getFollowing(id, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getFollowing");
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
| **id** | **String**| User slug | |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getFriends"></a>
# **getFriends**
> getFriends(id, traktApiVersion, traktApiKey)

Get friends

#### &amp;#128275; OAuth Optional &amp;#10024; Extended Info  Returns all friends for a user including when the relationship began. Friendship is a 2 way relationship where each user follows the other.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "sean"; // String | User slug
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getFriends(id, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getFriends");
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
| **id** | **String**| User slug | |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getHiddenItems"></a>
# **getHiddenItems**
> getHiddenItems(section, type, traktApiVersion, traktApiKey)

Get hidden items

#### &amp;#128274; OAuth Required &amp;#128196; Pagination &amp;#10024; Extended Info  Get hidden items for a section. This will return an array of standard media objects. You can optionally limit the &#x60;type&#x60; of results to return.

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
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String section = "calendar"; // String | 
    String type = "movie"; // String | Narrow down by element type.
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getHiddenItems(section, type, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getHiddenItems");
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
| **section** | **String**|  | [enum: calendar, progress_watched, progress_watched_reset, progress_collected, recommendations, comments] |
| **type** | **String**| Narrow down by element type. | [optional] [enum: movie, show, season, user] |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-Pagination-Item-Count -  <br>  * X-Pagination-Limit -  <br>  * X-Pagination-Page -  <br>  * X-Pagination-Page-Count -  <br>  |

<a id="getItemsOnAPersonalList"></a>
# **getItemsOnAPersonalList**
> getItemsOnAPersonalList(id, listId, type, traktApiVersion, traktApiKey)

Get items on a personal list

#### &amp;#128275; OAuth Optional &amp;#128196; Pagination Optional &amp;#10024; Extended Info &amp;#128513; Emojis  Get all items on a personal list. Items can be a &#x60;movie&#x60;, &#x60;show&#x60;, &#x60;season&#x60;, &#x60;episode&#x60;, or &#x60;person&#x60;. You can optionally specify the &#x60;type&#x60; parameter with a single value or comma delimited string for multiple item types.  #### Notes  Each list item contains a &#x60;notes&#x60; field with text entered by the user.  #### Sorting Headers  All list items are sorted by ascending &#x60;rank&#x60;. We also send &#x60;X-Sort-By&#x60; and &#x60;X-Sort-How&#x60; headers which can be used to custom sort the list _**in your app**_ based on the user&#39;s preference. Values for &#x60;X-Sort-By&#x60; include &#x60;rank&#x60;, &#x60;added&#x60;, &#x60;title&#x60;, &#x60;released&#x60;, &#x60;runtime&#x60;, &#x60;popularity&#x60;, &#x60;percentage&#x60;, &#x60;votes&#x60;, &#x60;my_rating&#x60;, &#x60;random&#x60;, &#x60;watched&#x60;, and &#x60;collected&#x60;. Values for &#x60;X-Sort-How&#x60; include &#x60;asc&#x60; and &#x60;desc&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "sean"; // String | User slug
    String listId = "star-wars-in-machete-order"; // String | Trakt ID or Trakt slug
    String type = "movie"; // String | Filter for a specific item type
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getItemsOnAPersonalList(id, listId, type, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getItemsOnAPersonalList");
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
| **id** | **String**| User slug | |
| **listId** | **String**| Trakt ID or Trakt slug | |
| **type** | **String**| Filter for a specific item type | [enum: movie, show, season, episode, person] |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-Private-User -  <br>  * X-Sort-By -  <br>  * X-Sort-How -  <br>  |

<a id="getLikes"></a>
# **getLikes**
> getLikes(id, type, traktApiVersion, traktApiKey)

Get likes

#### &amp;#128274; OAuth Optional &amp;#128196; Pagination  Get items a user likes. This will return an array of standard media objects. You can optionally limit the &#x60;type&#x60; of results to return.  #### Comment Media Objects  If you add &#x60;?extended&#x3D;comments&#x60; to the URL, it will return media objects for each comment like.  **Note:** This returns a lot of data, so please only use this extended parameter if you actually need it!

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
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "sean"; // String | User slug
    String type = "comments"; // String | 
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getLikes(id, type, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getLikes");
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
| **id** | **String**| User slug | |
| **type** | **String**|  | [enum: comments, lists] |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | &#x60;&#x60;&#x60; /users/sean/likes/lists &#x60;&#x60;&#x60; |  * X-Pagination-Item-Count -  <br>  * X-Pagination-Limit -  <br>  * X-Pagination-Page -  <br>  * X-Pagination-Page-Count -  <br>  |

<a id="getPendingFollowingRequests"></a>
# **getPendingFollowingRequests**
> getPendingFollowingRequests(traktApiVersion, traktApiKey)

Get pending following requests

#### &amp;#128274; OAuth Required &amp;#10024; Extended Info  List a user&#39;s pending following requests that they&#39;re waiting for the other user&#39;s to approve.

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
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getPendingFollowingRequests(traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getPendingFollowingRequests");
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
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getPersonalList"></a>
# **getPersonalList**
> getPersonalList(id, listId, traktApiVersion, traktApiKey)

Get personal list

#### &amp;#128275; OAuth Optional &amp;#128513; Emojis  Returns a single personal list. Use the [**_/users/:id/lists/:list_id/items**](#reference/users/list-items) method to get the actual items this list contains.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "sean"; // String | User slug
    String listId = "star-wars-in-machete-order"; // String | Trakt ID or Trakt slug
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getPersonalList(id, listId, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getPersonalList");
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
| **id** | **String**| User slug | |
| **listId** | **String**| Trakt ID or Trakt slug | |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-Sort-By -  <br>  * X-Sort-How -  <br>  |

<a id="getSavedFilters"></a>
# **getSavedFilters**
> getSavedFilters(section, traktApiVersion, traktApiKey)

Get saved filters

#### &amp;#128274; OAuth Required &amp;#128196; Pagination 🔥 VIP Only  Get all saved filters a user has created. The &#x60;path&#x60; and &#x60;query&#x60; can be used to construct an API path to retrieve the saved data. Think of this like a dynamically updated list.

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
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String section = "movies"; // String | 
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getSavedFilters(section, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getSavedFilters");
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
| **section** | **String**|  | [enum: movies, shows, calendars, search] |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-Pagination-Item-Count -  <br>  * X-Pagination-Limit -  <br>  * X-Pagination-Page -  <br>  * X-Pagination-Page-Count -  <br>  |

<a id="getStats"></a>
# **getStats**
> getStats(id, traktApiVersion, traktApiKey)

Get stats

#### &amp;#128275; OAuth Optional  Returns stats about the movies, shows, and episodes a user has watched, collected, and rated.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "sean"; // String | User slug
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getStats(id, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getStats");
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
| **id** | **String**| User slug | |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getUserProfile"></a>
# **getUserProfile**
> getUserProfile(id, traktApiVersion, traktApiKey)

Get user profile

#### &amp;#128275; OAuth Optional &amp;#10024; Extended Info  Get a user&#39;s profile information. If the user is private, info will only be returned if you send OAuth and are either that user or an approved follower. Adding &#x60;?extended&#x3D;vip&#x60; will return some additional VIP related fields so you can display the user&#39;s Trakt VIP status and year count.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "sean"; // String | User slug
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getUserProfile(id, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getUserProfile");
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
| **id** | **String**| User slug | |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | &#x60;&#x60;&#x60; /users/sean?extended&#x3D;vip &#x60;&#x60;&#x60; |  -  |

<a id="getWatching"></a>
# **getWatching**
> getWatching(id, traktApiVersion, traktApiKey)

Get watching

#### &amp;#128275; OAuth Optional &amp;#10024; Extended Info  Returns a movie or episode if the user is currently watching something.  If they are not, it returns no data and a &#x60;204&#x60; HTTP status code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "sean"; // String | User slug
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getWatching(id, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getWatching");
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
| **id** | **String**| User slug | |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Currently watching a &#x60;movie&#x60;. |  -  |
| **204** | Not watching anything. |  -  |

<a id="likeAList"></a>
# **likeAList**
> likeAList(id, listId, traktApiVersion, traktApiKey)

Like a list

#### &amp;#128274; OAuth Required  Votes help determine popular lists. Only one like is allowed per list per user.

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
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "sean"; // String | User slug
    String listId = "star-wars-in-machete-order"; // String | Trakt ID or Trakt slug
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.likeAList(id, listId, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#likeAList");
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
| **id** | **String**| User slug | |
| **listId** | **String**| Trakt ID or Trakt slug | |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="removeHiddenItems"></a>
# **removeHiddenItems**
> removeHiddenItems(section, traktApiVersion, traktApiKey, addHiddenItemsRequest)

Remove hidden items

#### &amp;#128274; OAuth Required  Unhide items for a specific section. Here&#39;s what type of items can unhidden for each section.  #### Unhideable Media Objects  | Section | Objects | |---|---|---| | &#x60;calendar&#x60; | &#x60;movie&#x60;, &#x60;show&#x60; | | &#x60;progress_watched&#x60; | &#x60;show&#x60;, &#x60;season&#x60; | | &#x60;progress_collected&#x60; | &#x60;show&#x60;, &#x60;season&#x60; | | &#x60;recommendations&#x60; | &#x60;movie&#x60;, &#x60;show&#x60; | | &#x60;comments&#x60; | &#x60;user&#x60; |  #### JSON POST Data  | Key | Type | Value | |---|---|---| | &#x60;movies&#x60; | array | Array of &#x60;movie&#x60; objects. (see examples &amp;#8594;) | | &#x60;shows&#x60; | array | Array of &#x60;show&#x60; objects. | | &#x60;seasons&#x60; | array | Array of &#x60;season&#x60; objects. | | &#x60;users&#x60; | array | Array of &#x60;user&#x60; objects. |

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
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String section = "calendar"; // String | 
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    AddHiddenItemsRequest addHiddenItemsRequest = new AddHiddenItemsRequest(); // AddHiddenItemsRequest | 
    try {
      apiInstance.removeHiddenItems(section, traktApiVersion, traktApiKey, addHiddenItemsRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#removeHiddenItems");
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
| **section** | **String**|  | [enum: calendar, progress_watched, progress_collected, recommendations, comments] |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |
| **addHiddenItemsRequest** | [**AddHiddenItemsRequest**](AddHiddenItemsRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="removeItemsFromPersonalList"></a>
# **removeItemsFromPersonalList**
> removeItemsFromPersonalList(id, listId, traktApiVersion, traktApiKey, removeItemsFromPersonalListRequest)

Remove items from personal list

#### &amp;#128274; OAuth Required  Remove one or more items from a personal list.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | &#x60;movies&#x60; | array | Array of &#x60;movie&#x60; objects. (see examples &amp;#8594;) | | &#x60;shows&#x60; | array | Array of &#x60;show&#x60; objects. | | &#x60;seasons&#x60; | array | Array of &#x60;season&#x60; objects. | | &#x60;episodes&#x60; | array | Array of &#x60;episode&#x60; objects. | | &#x60;people&#x60; | array | Array of &#x60;person&#x60; objects. |

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
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "sean"; // String | User slug
    String listId = "star-wars-in-machete-order"; // String | Trakt ID or Trakt slug
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    RemoveItemsFromPersonalListRequest removeItemsFromPersonalListRequest = new RemoveItemsFromPersonalListRequest(); // RemoveItemsFromPersonalListRequest | 
    try {
      apiInstance.removeItemsFromPersonalList(id, listId, traktApiVersion, traktApiKey, removeItemsFromPersonalListRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#removeItemsFromPersonalList");
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
| **id** | **String**| User slug | |
| **listId** | **String**| Trakt ID or Trakt slug | |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |
| **removeItemsFromPersonalListRequest** | [**RemoveItemsFromPersonalListRequest**](RemoveItemsFromPersonalListRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="removeLikeOnAList"></a>
# **removeLikeOnAList**
> removeLikeOnAList(id, listId, traktApiVersion, traktApiKey)

Remove like on a list

#### &amp;#128274; OAuth Required  Remove a like on a list.

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
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "id_example"; // String | Automatically added
    String listId = "listId_example"; // String | Automatically added
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.removeLikeOnAList(id, listId, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#removeLikeOnAList");
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
| **id** | **String**| Automatically added | |
| **listId** | **String**| Automatically added | |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="reorderAUsersLists"></a>
# **reorderAUsersLists**
> reorderAUsersLists(id, traktApiVersion, traktApiKey, reorderAUserSListsRequest)

Reorder a user&#39;s lists

#### &amp;#128274; OAuth Required  Reorder all lists by sending the updated &#x60;rank&#x60; of list ids. Use the [**_/users/:id/lists**](#reference/users/lists) method to get all list ids.

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
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "sean"; // String | User slug
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    ReorderAUserSListsRequest reorderAUserSListsRequest = new ReorderAUserSListsRequest(); // ReorderAUserSListsRequest | 
    try {
      apiInstance.reorderAUsersLists(id, traktApiVersion, traktApiKey, reorderAUserSListsRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#reorderAUsersLists");
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
| **id** | **String**| User slug | |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |
| **reorderAUserSListsRequest** | [**ReorderAUserSListsRequest**](ReorderAUserSListsRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="reorderItemsOnAList"></a>
# **reorderItemsOnAList**
> reorderItemsOnAList(id, listId, traktApiVersion, traktApiKey, reorderPersonallyRecommendedItemsRequest)

Reorder items on a list

#### &amp;#128274; OAuth Required  Reorder all items on a list by sending the updated &#x60;rank&#x60; of list item ids. Use the [**_/users/:id/lists/:list_id/items**](#reference/users/list-items) method to get all list item ids.

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
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "sean"; // String | User slug
    String listId = "star-wars-in-machete-order"; // String | Trakt ID or Trakt slug
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    ReorderPersonallyRecommendedItemsRequest reorderPersonallyRecommendedItemsRequest = new ReorderPersonallyRecommendedItemsRequest(); // ReorderPersonallyRecommendedItemsRequest | 
    try {
      apiInstance.reorderItemsOnAList(id, listId, traktApiVersion, traktApiKey, reorderPersonallyRecommendedItemsRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#reorderItemsOnAList");
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
| **id** | **String**| User slug | |
| **listId** | **String**| Trakt ID or Trakt slug | |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |
| **reorderPersonallyRecommendedItemsRequest** | [**ReorderPersonallyRecommendedItemsRequest**](ReorderPersonallyRecommendedItemsRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="retrieveSettings"></a>
# **retrieveSettings**
> retrieveSettings(traktApiVersion, traktApiKey)

Retrieve settings

#### &amp;#128274; OAuth Required  Get the user&#39;s settings so you can align your app&#39;s experience with what they&#39;re used to on the trakt website. A globally unique &#x60;uuid&#x60; is also returned, which can be used to identify the user locally in your app if needed. However, the &#x60;uuid&#x60; can&#39;t be used to retrieve data from the Trakt API.

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
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.retrieveSettings(traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#retrieveSettings");
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
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="unfollowThisUser"></a>
# **unfollowThisUser**
> unfollowThisUser(id, traktApiVersion, traktApiKey)

Unfollow this user

#### &amp;#128274; OAuth Required  Unfollow someone you already follow.

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
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "id_example"; // String | Automatically added
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.unfollowThisUser(id, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#unfollowThisUser");
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
| **id** | **String**| Automatically added | |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="updatePersonalList"></a>
# **updatePersonalList**
> updatePersonalList(id, listId, traktApiVersion, traktApiKey, updatePersonalListRequest)

Update personal list

#### &amp;#128274; OAuth Required  Update a personal list by sending 1 or more parameters. If you update the list name, the original slug will still be retained so existing references to this list won&#39;t break.  #### Privacy  Lists will be &#x60;private&#x60; by default. Here is what each value means.  | Value | Privacy impact... | |---|---| | &#x60;private&#x60; | Only you can see the list. | | &#x60;link&#x60; | Anyone with the &#x60;share_link&#x60; can see the list. | | &#x60;friends&#x60; | Only your friends can see the list. | | &#x60;public&#x60; | Anyone can see the list. |  #### JSON POST Data  | Key | Type | Value | |---|---|---|---| | &#x60;name&#x60; | string | Name of the list. | | &#x60;description&#x60; | string | Description for this list. | | &#x60;privacy&#x60; | string | &#x60;private&#x60;, &#x60;link&#x60;, &#x60;friends&#x60;, &#x60;public&#x60; | | &#x60;display_numbers&#x60; | boolean | Should each item be numbered? | | &#x60;allow_comments&#x60; | boolean | Are comments allowed? | | &#x60;sort_by&#x60; | string | &#x60;rank&#x60;, &#x60;added&#x60;, &#x60;title&#x60;, &#x60;released&#x60;, &#x60;runtime&#x60;, &#x60;popularity&#x60;, &#x60;percentage&#x60;, &#x60;votes&#x60;, &#x60;my_rating&#x60;, &#x60;random&#x60;, &#x60;watched&#x60;, &#x60;collected&#x60; | | &#x60;sort_how&#x60; | string | &#x60;asc&#x60;, &#x60;desc&#x60; |

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
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "id_example"; // String | Automatically added
    String listId = "listId_example"; // String | Automatically added
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    UpdatePersonalListRequest updatePersonalListRequest = new UpdatePersonalListRequest(); // UpdatePersonalListRequest | 
    try {
      apiInstance.updatePersonalList(id, listId, traktApiVersion, traktApiKey, updatePersonalListRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#updatePersonalList");
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
| **id** | **String**| Automatically added | |
| **listId** | **String**| Automatically added | |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |
| **updatePersonalListRequest** | [**UpdatePersonalListRequest**](UpdatePersonalListRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="usersIdCollectionTypeGet"></a>
# **usersIdCollectionTypeGet**
> usersIdCollectionTypeGet(id, type, traktApiVersion, traktApiKey)

Get collection

#### &amp;#128275; OAuth Optional &amp;#10024; Extended Info  Get all collected items in a user&#39;s collection. A collected item indicates availability to watch digitally or on physical media.  Each &#x60;movie&#x60; object contains &#x60;collected_at&#x60; and &#x60;updated_at&#x60; timestamps. Since users can set custom dates when they collected movies, it is possible for &#x60;collected_at&#x60; to be in the past. We also include &#x60;updated_at&#x60; to help sync Trakt data with your app. Cache this timestamp locally and only re-process the movie if you see a newer timestamp.  Each &#x60;show&#x60; object contains &#x60;last_collected_at&#x60; and &#x60;last_updated_at&#x60; timestamps. Since users can set custom dates when they collected episodes, it is possible for &#x60;last_collected_at&#x60; to be in the past. We also include &#x60;last_updated_at&#x60; to help sync Trakt data with your app. Cache this timestamp locally and only re-process the show if you see a newer timestamp.  If you add &#x60;?extended&#x3D;metadata&#x60; to the URL, it will return the additional &#x60;media_type&#x60;, &#x60;resolution&#x60;, &#x60;hdr&#x60;, &#x60;audio&#x60;, &#x60;audio_channels&#x60; and &#39;3d&#39; metadata. It will use &#x60;null&#x60; if the metadata isn&#39;t set for an item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "sean"; // String | User slug
    String type = "movies"; // String | 
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.usersIdCollectionTypeGet(id, type, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersIdCollectionTypeGet");
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
| **id** | **String**| User slug | |
| **type** | **String**|  | [enum: movies, shows] |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | &#x60;&#x60;&#x60; /users/sean/collection/shows?extended&#x3D;metadata &#x60;&#x60;&#x60; |  -  |

<a id="usersIdHistoryTypeItemIdGet"></a>
# **usersIdHistoryTypeItemIdGet**
> usersIdHistoryTypeItemIdGet(id, type, itemId, startAt, endAt, traktApiVersion, traktApiKey)

Get watched history

#### &amp;#128275; OAuth Optional &amp;#128196; Pagination &amp;#10024; Extended Info  Returns movies and episodes that a user has watched, sorted by most recent. You can optionally limit the &#x60;type&#x60; to &#x60;movies&#x60; or &#x60;episodes&#x60;. The &#x60;id&#x60; _(64-bit integer)_ in each history item uniquely identifies the event and can be used to remove individual events by using the [**_/sync/history/remove**](#reference/sync/remove-from-history/get-watched-history) method. The &#x60;action&#x60; will be set to &#x60;scrobble&#x60;, &#x60;checkin&#x60;, or &#x60;watch&#x60;.  Specify a &#x60;type&#x60; and trakt &#x60;item_id&#x60; to limit the history for just that item. If the &#x60;item_id&#x60; is valid, but there is no history, an empty array will be returned.  | Example URL | Returns watches for... | |---|---| | &#x60;/history/movies/12601&#x60; | TRON: Legacy | | &#x60;/history/shows/1388&#x60; | All episodes of Breaking Bad | | &#x60;/history/seasons/3950&#x60; | All episodes of Breaking Bad: Season 1 | | &#x60;/history/episodes/73482&#x60; | Only episode 1 for Breaking Bad: Season 1 |

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "sean"; // String | User slug
    String type = "movies"; // String | 
    Integer itemId = 123; // Integer | Trakt ID for a specific item.
    String startAt = "2016-06-01T00:00:00.000Z"; // String | Starting date.
    String endAt = "2016-07-01T23:59:59.000Z"; // String | Ending date.
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.usersIdHistoryTypeItemIdGet(id, type, itemId, startAt, endAt, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersIdHistoryTypeItemIdGet");
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
| **id** | **String**| User slug | |
| **type** | **String**|  | [enum: movies, shows, seasons, episodes] |
| **itemId** | **Integer**| Trakt ID for a specific item. | |
| **startAt** | **String**| Starting date. | [optional] |
| **endAt** | **String**| Ending date. | [optional] |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | &#x60;&#x60;&#x60; /users/sean/history/episodes &#x60;&#x60;&#x60; |  * X-Pagination-Item-Count -  <br>  * X-Pagination-Limit -  <br>  * X-Pagination-Page -  <br>  * X-Pagination-Page-Count -  <br>  |

<a id="usersIdListsListIdCommentsSortGet"></a>
# **usersIdListsListIdCommentsSortGet**
> usersIdListsListIdCommentsSortGet(id, listId, sort, traktApiVersion, traktApiKey)

Get all list comments

#### &amp;#128275; OAuth Optional &amp;#128196; Pagination &amp;#128513; Emojis  Returns all top level comments for a list. By default, the &#x60;newest&#x60; comments are returned first. Other sorting options include &#x60;oldest&#x60;, most &#x60;likes&#x60;, and most &#x60;replies&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "sean"; // String | User slug
    String listId = "star-wars-in-machete-order"; // String | Trakt ID or Trakt slug
    String sort = "newest"; // String | how to sort
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.usersIdListsListIdCommentsSortGet(id, listId, sort, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersIdListsListIdCommentsSortGet");
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
| **id** | **String**| User slug | |
| **listId** | **String**| Trakt ID or Trakt slug | |
| **sort** | **String**| how to sort | [enum: newest, oldest, likes, replies] |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-Pagination-Item-Count -  <br>  * X-Pagination-Limit -  <br>  * X-Pagination-Page -  <br>  * X-Pagination-Page-Count -  <br>  |

<a id="usersIdListsListIdLikesGet"></a>
# **usersIdListsListIdLikesGet**
> usersIdListsListIdLikesGet(id, listId, traktApiVersion, traktApiKey)

Get all users who liked a list

#### &amp;#128275; OAuth Optional &amp;#128196; Pagination  Returns all users who liked a list.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "sean"; // String | User slug
    String listId = "star-wars-in-machete-order"; // String | Trakt ID or Trakt slug
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.usersIdListsListIdLikesGet(id, listId, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersIdListsListIdLikesGet");
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
| **id** | **String**| User slug | |
| **listId** | **String**| Trakt ID or Trakt slug | |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-Pagination-Item-Count -  <br>  * X-Pagination-Limit -  <br>  * X-Pagination-Page -  <br>  * X-Pagination-Page-Count -  <br>  |

<a id="usersIdRatingsTypeRatingGet"></a>
# **usersIdRatingsTypeRatingGet**
> usersIdRatingsTypeRatingGet(id, type, rating, traktApiVersion, traktApiKey)

Get ratings

#### &amp;#128275; OAuth Optional &amp;#128196; Pagination Optional &amp;#10024; Extended Info  Get a user&#39;s ratings filtered by &#x60;type&#x60;. You can optionally filter for a specific &#x60;rating&#x60; between 1 and 10. Send a comma separated string for &#x60;rating&#x60; if you need multiple ratings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "sean"; // String | User slug
    String type = "movies"; // String | 
    Integer rating = 1; // Integer | Filter for a specific rating.
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.usersIdRatingsTypeRatingGet(id, type, rating, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersIdRatingsTypeRatingGet");
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
| **id** | **String**| User slug | |
| **type** | **String**|  | [enum: movies, shows, seasons, episodes, all] |
| **rating** | **Integer**| Filter for a specific rating. | [enum: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | &#x60;&#x60;&#x60; /users/sean/ratings/episodes &#x60;&#x60;&#x60; |  -  |

<a id="usersIdRecommendationsTypeSortGet"></a>
# **usersIdRecommendationsTypeSortGet**
> usersIdRecommendationsTypeSortGet(id, type, sort, traktApiVersion, traktApiKey)

Get personal recommendations

#### &amp;#128274; OAuth Required &amp;#128196; Pagination Optional &amp;#10024; Extended Info &amp;#128513; Emojis  Returns the top 50 items a user personally recommendeds to others. These recommendations are used to enchance Trakt&#39;s social recommendation algorithm. Apps should encourage user&#39;s to build their personal recommendations so the algorithm keeps getting better.  #### Notes  Each recommendation contains a &#x60;notes&#x60; field explaining why the user recommended the item.

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
    defaultClient.setBasePath("https://api.trakt.tv");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "sean"; // String | User slug
    String type = "movies"; // String | Filter for a specific item type
    String sort = "rank"; // String | How to sort (only if type is also sent)
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.usersIdRecommendationsTypeSortGet(id, type, sort, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersIdRecommendationsTypeSortGet");
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
| **id** | **String**| User slug | |
| **type** | **String**| Filter for a specific item type | [enum: movies, shows] |
| **sort** | **String**| How to sort (only if type is also sent) | [enum: rank, added, released, title] |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | &#x60;&#x60;&#x60; /users/justin/recommendations/shows &#x60;&#x60;&#x60; |  * X-Sort-By -  <br>  * X-Sort-How -  <br>  |

<a id="usersIdWatchedTypeGet"></a>
# **usersIdWatchedTypeGet**
> usersIdWatchedTypeGet(id, type, traktApiVersion, traktApiKey)

Get watched

#### &amp;#128275; OAuth Optional &amp;#10024; Extended Info  Returns all movies or shows a user has watched sorted by most plays.  If &#x60;type&#x60; is set to _shows_ and you add &#x60;?extended&#x3D;noseasons&#x60; to the URL, it won&#39;t return season or episode info.  Each &#x60;movie&#x60; and &#x60;show&#x60; object contains &#x60;last_watched_at&#x60; and &#x60;last_updated_at&#x60; timestamps. Since users can set custom dates when they watched movies and episodes, it is possible for &#x60;last_watched_at&#x60; to be in the past. We also include &#x60;last_updated_at&#x60; to help sync Trakt data with your app. Cache this timestamp locally and only re-process the movies and shows if you see a newer timestamp.  Each &#x60;show&#x60; object contains a &#x60;reset_at&#x60; timestamp. If not &#x60;null&#x60;, this is when the user started re-watching the show. Your app can adjust the progress by ignoring episodes with a &#x60;last_watched_at&#x60; prior to the &#x60;reset_at&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "sean"; // String | User slug
    String type = "movies"; // String | 
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.usersIdWatchedTypeGet(id, type, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersIdWatchedTypeGet");
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
| **id** | **String**| User slug | |
| **type** | **String**|  | [enum: movies, shows] |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | &#x60;&#x60;&#x60; /users/sean/watched/shows?extended&#x3D;noseasons &#x60;&#x60;&#x60; |  -  |

<a id="usersIdWatchlistTypeSortGet"></a>
# **usersIdWatchlistTypeSortGet**
> usersIdWatchlistTypeSortGet(id, type, sort, traktApiVersion, traktApiKey)

Get watchlist

#### &amp;#128275; OAuth Optional &amp;#128196; Pagination Optional &amp;#10024; Extended Info &amp;#128513; Emojis  Returns all items in a user&#39;s watchlist filtered by type.  #### Notes  Each watchlist item contains a &#x60;notes&#x60; field with text entered by the user.  #### Sorting Headers  By default, all list items are sorted by &#x60;rank&#x60; &#x60;asc&#x60;. We send &#x60;X-Applied-Sort-By&#x60; and &#x60;X-Applied-Sort-How&#x60; headers to indicate how the results are actually being sorted.  We also send &#x60;X-Sort-By&#x60; and &#x60;X-Sort-How&#x60; headers which indicate the user&#39;s sort preference. Use these to to custom sort the watchlist _**in your app**_ for more advanced sort abilities we can&#39;t do in the API. Values for &#x60;X-Sort-By&#x60; include &#x60;rank&#x60;, &#x60;added&#x60;, &#x60;title&#x60;, &#x60;released&#x60;, &#x60;runtime&#x60;, &#x60;popularity&#x60;, &#x60;percentage&#x60;, and &#x60;votes&#x60;. Values for &#x60;X-Sort-How&#x60; include &#x60;asc&#x60; and &#x60;desc&#x60;.  #### Auto Removal  When an item is watched, it will be automatically removed from the watchlist. For shows and seasons, watching 1 episode will remove the entire show or season.  _**The watchlist should not be used as a list of what the user is actively watching.**_  Use a combination of the [**_/sync/watched**](/reference/sync/get-watched) and [**_/shows/:id/progress**](/reference/shows/watched-progress) methods to get what the user is actively watching.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.trakt.tv");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "sean"; // String | User slug
    String type = "movies"; // String | Filter for a specific item type
    String sort = "rank"; // String | How to sort (only if type is also sent)
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.usersIdWatchlistTypeSortGet(id, type, sort, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersIdWatchlistTypeSortGet");
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
| **id** | **String**| User slug | |
| **type** | **String**| Filter for a specific item type | [enum: movies, shows, seasons, episodes] |
| **sort** | **String**| How to sort (only if type is also sent) | [enum: rank, added, released, title] |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | &#x60;&#x60;&#x60; /users/sean/watchlist/episodes &#x60;&#x60;&#x60; |  * X-Private-User -  <br>  * X-Sort-By -  <br>  * X-Sort-How -  <br>  |

