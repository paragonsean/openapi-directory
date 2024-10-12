# DefaultApi

All URIs are relative to *http://mastodon.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiOembedGet**](DefaultApi.md#apiOembedGet) | **GET** /api/oembed |  |
| [**apiProofsGet**](DefaultApi.md#apiProofsGet) | **GET** /api/proofs |  |
| [**apiV1AdminAccountsGet**](DefaultApi.md#apiV1AdminAccountsGet) | **GET** /api/v1/admin/accounts |  |
| [**apiV1AdminAccountsIdActionPost**](DefaultApi.md#apiV1AdminAccountsIdActionPost) | **POST** /api/v1/admin/accounts/{id}/action |  |
| [**apiV1AdminAccountsIdApprovePost**](DefaultApi.md#apiV1AdminAccountsIdApprovePost) | **POST** /api/v1/admin/accounts/{id}/approve |  |
| [**apiV1AdminAccountsIdEnablePost**](DefaultApi.md#apiV1AdminAccountsIdEnablePost) | **POST** /api/v1/admin/accounts/{id}/enable |  |
| [**apiV1AdminAccountsIdGet**](DefaultApi.md#apiV1AdminAccountsIdGet) | **GET** /api/v1/admin/accounts/{id} |  |
| [**apiV1AdminAccountsIdRejectPost**](DefaultApi.md#apiV1AdminAccountsIdRejectPost) | **POST** /api/v1/admin/accounts/{id}/reject |  |
| [**apiV1AdminAccountsIdUnsilencePost**](DefaultApi.md#apiV1AdminAccountsIdUnsilencePost) | **POST** /api/v1/admin/accounts/{id}/unsilence |  |
| [**apiV1AdminAccountsIdUnsuspendPost**](DefaultApi.md#apiV1AdminAccountsIdUnsuspendPost) | **POST** /api/v1/admin/accounts/{id}/unsuspend |  |
| [**apiV1AdminReportsGet**](DefaultApi.md#apiV1AdminReportsGet) | **GET** /api/v1/admin/reports |  |
| [**apiV1AdminReportsIdAssignToSelfPost**](DefaultApi.md#apiV1AdminReportsIdAssignToSelfPost) | **POST** /api/v1/admin/reports/{id}/assign_to_self |  |
| [**apiV1AdminReportsIdGet**](DefaultApi.md#apiV1AdminReportsIdGet) | **GET** /api/v1/admin/reports/{id} |  |
| [**apiV1AdminReportsIdReopenPost**](DefaultApi.md#apiV1AdminReportsIdReopenPost) | **POST** /api/v1/admin/reports/{id}/reopen |  |
| [**apiV1AdminReportsIdResolvePost**](DefaultApi.md#apiV1AdminReportsIdResolvePost) | **POST** /api/v1/admin/reports/{id}/resolve |  |
| [**apiV1AdminReportsIdUnassignPost**](DefaultApi.md#apiV1AdminReportsIdUnassignPost) | **POST** /api/v1/admin/reports/{id}/unassign |  |
| [**apiV1AnnouncementsGet**](DefaultApi.md#apiV1AnnouncementsGet) | **GET** /api/v1/announcements |  |
| [**apiV1AnnouncementsIdDismissPost**](DefaultApi.md#apiV1AnnouncementsIdDismissPost) | **POST** /api/v1/announcements/{id}/dismiss |  |
| [**apiV1AnnouncementsIdReactionsNameDelete**](DefaultApi.md#apiV1AnnouncementsIdReactionsNameDelete) | **DELETE** /api/v1/announcements/{id}/reactions/{name} |  |
| [**apiV1AnnouncementsIdReactionsNamePut**](DefaultApi.md#apiV1AnnouncementsIdReactionsNamePut) | **PUT** /api/v1/announcements/{id}/reactions/{name} |  |
| [**apiV1BlocksGet**](DefaultApi.md#apiV1BlocksGet) | **GET** /api/v1/blocks |  |
| [**apiV1BookmarksGet**](DefaultApi.md#apiV1BookmarksGet) | **GET** /api/v1/bookmarks |  |
| [**apiV1ConversationsGet**](DefaultApi.md#apiV1ConversationsGet) | **GET** /api/v1/conversations |  |
| [**apiV1ConversationsIdDelete**](DefaultApi.md#apiV1ConversationsIdDelete) | **DELETE** /api/v1/conversations/{id} |  |
| [**apiV1ConversationsIdReadPost**](DefaultApi.md#apiV1ConversationsIdReadPost) | **POST** /api/v1/conversations/{id}/read |  |
| [**apiV1CustomEmojisGet**](DefaultApi.md#apiV1CustomEmojisGet) | **GET** /api/v1/custom_emojis |  |
| [**apiV1DirectoryGet**](DefaultApi.md#apiV1DirectoryGet) | **GET** /api/v1/directory |  |
| [**apiV1DomainBlocksDelete**](DefaultApi.md#apiV1DomainBlocksDelete) | **DELETE** /api/v1/domain_blocks |  |
| [**apiV1DomainBlocksGet**](DefaultApi.md#apiV1DomainBlocksGet) | **GET** /api/v1/domain_blocks |  |
| [**apiV1DomainBlocksPost**](DefaultApi.md#apiV1DomainBlocksPost) | **POST** /api/v1/domain_blocks |  |
| [**apiV1EndorsementsGet**](DefaultApi.md#apiV1EndorsementsGet) | **GET** /api/v1/endorsements |  |
| [**apiV1FavouritesGet**](DefaultApi.md#apiV1FavouritesGet) | **GET** /api/v1/favourites |  |
| [**apiV1FeaturedTagsGet**](DefaultApi.md#apiV1FeaturedTagsGet) | **GET** /api/v1/featured_tags |  |
| [**apiV1FeaturedTagsIdDelete**](DefaultApi.md#apiV1FeaturedTagsIdDelete) | **DELETE** /api/v1/featured_tags/{id} |  |
| [**apiV1FeaturedTagsPost**](DefaultApi.md#apiV1FeaturedTagsPost) | **POST** /api/v1/featured_tags |  |
| [**apiV1FeaturedTagsSuggestionsGet**](DefaultApi.md#apiV1FeaturedTagsSuggestionsGet) | **GET** /api/v1/featured_tags/suggestions |  |
| [**apiV1FiltersGet**](DefaultApi.md#apiV1FiltersGet) | **GET** /api/v1/filters |  |
| [**apiV1FiltersIdDelete**](DefaultApi.md#apiV1FiltersIdDelete) | **DELETE** /api/v1/filters/{id} |  |
| [**apiV1FiltersIdGet**](DefaultApi.md#apiV1FiltersIdGet) | **GET** /api/v1/filters/{id} |  |
| [**apiV1FiltersIdPut**](DefaultApi.md#apiV1FiltersIdPut) | **PUT** /api/v1/filters/{id} |  |
| [**apiV1FiltersPost**](DefaultApi.md#apiV1FiltersPost) | **POST** /api/v1/filters |  |
| [**apiV1FollowRequestsGet**](DefaultApi.md#apiV1FollowRequestsGet) | **GET** /api/v1/follow_requests |  |
| [**apiV1FollowRequestsIdAuthorizePost**](DefaultApi.md#apiV1FollowRequestsIdAuthorizePost) | **POST** /api/v1/follow_requests/{id}/authorize |  |
| [**apiV1FollowRequestsIdRejectPost**](DefaultApi.md#apiV1FollowRequestsIdRejectPost) | **POST** /api/v1/follow_requests/{id}/reject |  |
| [**apiV1InstanceActivityGet**](DefaultApi.md#apiV1InstanceActivityGet) | **GET** /api/v1/instance/activity |  |
| [**apiV1InstanceGet**](DefaultApi.md#apiV1InstanceGet) | **GET** /api/v1/instance |  |
| [**apiV1InstancePeersGet**](DefaultApi.md#apiV1InstancePeersGet) | **GET** /api/v1/instance/peers |  |
| [**apiV1ListsDelete**](DefaultApi.md#apiV1ListsDelete) | **DELETE** /api/v1/lists |  |
| [**apiV1ListsGet**](DefaultApi.md#apiV1ListsGet) | **GET** /api/v1/lists |  |
| [**apiV1ListsIdAccountsDelete**](DefaultApi.md#apiV1ListsIdAccountsDelete) | **DELETE** /api/v1/lists/{id}/accounts |  |
| [**apiV1ListsIdAccountsGet**](DefaultApi.md#apiV1ListsIdAccountsGet) | **GET** /api/v1/lists/{id}/accounts |  |
| [**apiV1ListsIdAccountsPost**](DefaultApi.md#apiV1ListsIdAccountsPost) | **POST** /api/v1/lists/{id}/accounts |  |
| [**apiV1ListsIdGet**](DefaultApi.md#apiV1ListsIdGet) | **GET** /api/v1/lists/{id} |  |
| [**apiV1ListsPost**](DefaultApi.md#apiV1ListsPost) | **POST** /api/v1/lists |  |
| [**apiV1ListsPut**](DefaultApi.md#apiV1ListsPut) | **PUT** /api/v1/lists |  |
| [**apiV1MarkersGet**](DefaultApi.md#apiV1MarkersGet) | **GET** /api/v1/markers |  |
| [**apiV1MarkersPost**](DefaultApi.md#apiV1MarkersPost) | **POST** /api/v1/markers |  |
| [**apiV1MediaIdGet**](DefaultApi.md#apiV1MediaIdGet) | **GET** /api/v1/media/{id} |  |
| [**apiV1MediaIdPost**](DefaultApi.md#apiV1MediaIdPost) | **POST** /api/v1/media/{id} |  |
| [**apiV1MediaPost**](DefaultApi.md#apiV1MediaPost) | **POST** /api/v1/media |  |
| [**apiV1MutesGet**](DefaultApi.md#apiV1MutesGet) | **GET** /api/v1/mutes |  |
| [**apiV1NotificationsClearPost**](DefaultApi.md#apiV1NotificationsClearPost) | **POST** /api/v1/notifications/clear |  |
| [**apiV1NotificationsGet**](DefaultApi.md#apiV1NotificationsGet) | **GET** /api/v1/notifications |  |
| [**apiV1NotificationsIdDismissPost**](DefaultApi.md#apiV1NotificationsIdDismissPost) | **POST** /api/v1/notifications/{id}/dismiss |  |
| [**apiV1NotificationsIdGet**](DefaultApi.md#apiV1NotificationsIdGet) | **GET** /api/v1/notifications/{id} |  |
| [**apiV1PollsIdGet**](DefaultApi.md#apiV1PollsIdGet) | **GET** /api/v1/polls/{id} |  |
| [**apiV1PollsIdPost**](DefaultApi.md#apiV1PollsIdPost) | **POST** /api/v1/polls/{id} |  |
| [**apiV1PreferencesGet**](DefaultApi.md#apiV1PreferencesGet) | **GET** /api/v1/preferences |  |
| [**apiV1PushSubscriptionDelete**](DefaultApi.md#apiV1PushSubscriptionDelete) | **DELETE** /api/v1/push/subscription |  |
| [**apiV1PushSubscriptionGet**](DefaultApi.md#apiV1PushSubscriptionGet) | **GET** /api/v1/push/subscription |  |
| [**apiV1PushSubscriptionPost**](DefaultApi.md#apiV1PushSubscriptionPost) | **POST** /api/v1/push/subscription |  |
| [**apiV1PushSubscriptionPut**](DefaultApi.md#apiV1PushSubscriptionPut) | **PUT** /api/v1/push/subscription |  |
| [**apiV1ReportsPost**](DefaultApi.md#apiV1ReportsPost) | **POST** /api/v1/reports |  |
| [**apiV1ScheduledStatusesGet**](DefaultApi.md#apiV1ScheduledStatusesGet) | **GET** /api/v1/scheduled_statuses |  |
| [**apiV1ScheduledStatusesIdDelete**](DefaultApi.md#apiV1ScheduledStatusesIdDelete) | **DELETE** /api/v1/scheduled_statuses/{id} |  |
| [**apiV1ScheduledStatusesIdGet**](DefaultApi.md#apiV1ScheduledStatusesIdGet) | **GET** /api/v1/scheduled_statuses/{id} |  |
| [**apiV1ScheduledStatusesIdPut**](DefaultApi.md#apiV1ScheduledStatusesIdPut) | **PUT** /api/v1/scheduled_statuses/{id} |  |
| [**apiV1StatusesIdBookmarkPost**](DefaultApi.md#apiV1StatusesIdBookmarkPost) | **POST** /api/v1/statuses/{id}/bookmark |  |
| [**apiV1StatusesIdContextGet**](DefaultApi.md#apiV1StatusesIdContextGet) | **GET** /api/v1/statuses/{id}/context |  |
| [**apiV1StatusesIdDelete**](DefaultApi.md#apiV1StatusesIdDelete) | **DELETE** /api/v1/statuses/{id} |  |
| [**apiV1StatusesIdFavouritePost**](DefaultApi.md#apiV1StatusesIdFavouritePost) | **POST** /api/v1/statuses/{id}/favourite |  |
| [**apiV1StatusesIdFavouritedByGet**](DefaultApi.md#apiV1StatusesIdFavouritedByGet) | **GET** /api/v1/statuses/{id}/favourited_by |  |
| [**apiV1StatusesIdGet**](DefaultApi.md#apiV1StatusesIdGet) | **GET** /api/v1/statuses/{id} |  |
| [**apiV1StatusesIdMutePost**](DefaultApi.md#apiV1StatusesIdMutePost) | **POST** /api/v1/statuses/{id}/mute |  |
| [**apiV1StatusesIdPinPost**](DefaultApi.md#apiV1StatusesIdPinPost) | **POST** /api/v1/statuses/{id}/pin |  |
| [**apiV1StatusesIdReblogPost**](DefaultApi.md#apiV1StatusesIdReblogPost) | **POST** /api/v1/statuses/{id}/reblog |  |
| [**apiV1StatusesIdRebloggedByGet**](DefaultApi.md#apiV1StatusesIdRebloggedByGet) | **GET** /api/v1/statuses/{id}/reblogged_by |  |
| [**apiV1StatusesIdUnbookmarkPost**](DefaultApi.md#apiV1StatusesIdUnbookmarkPost) | **POST** /api/v1/statuses/{id}/unbookmark |  |
| [**apiV1StatusesIdUnfavouritePost**](DefaultApi.md#apiV1StatusesIdUnfavouritePost) | **POST** /api/v1/statuses/{id}/unfavourite |  |
| [**apiV1StatusesIdUnmutePost**](DefaultApi.md#apiV1StatusesIdUnmutePost) | **POST** /api/v1/statuses/{id}/unmute |  |
| [**apiV1StatusesIdUnpinPost**](DefaultApi.md#apiV1StatusesIdUnpinPost) | **POST** /api/v1/statuses/{id}/unpin |  |
| [**apiV1StatusesIdUnreblogPost**](DefaultApi.md#apiV1StatusesIdUnreblogPost) | **POST** /api/v1/statuses/{id}/unreblog |  |
| [**apiV1StatusesPost**](DefaultApi.md#apiV1StatusesPost) | **POST** /api/v1/statuses |  |
| [**apiV1SuggestionsGet**](DefaultApi.md#apiV1SuggestionsGet) | **GET** /api/v1/suggestions |  |
| [**apiV1SuggestionsIdDelete**](DefaultApi.md#apiV1SuggestionsIdDelete) | **DELETE** /api/v1/suggestions/{id} |  |
| [**apiV1TimelinesHomeGet**](DefaultApi.md#apiV1TimelinesHomeGet) | **GET** /api/v1/timelines/home |  |
| [**apiV1TimelinesListListIdGet**](DefaultApi.md#apiV1TimelinesListListIdGet) | **GET** /api/v1/timelines/list/{list_id} |  |
| [**apiV1TimelinesPublicGet**](DefaultApi.md#apiV1TimelinesPublicGet) | **GET** /api/v1/timelines/public |  |
| [**apiV1TimelinesTagHashtagGet**](DefaultApi.md#apiV1TimelinesTagHashtagGet) | **GET** /api/v1/timelines/tag/{hashtag} |  |
| [**apiV1TrendsGet**](DefaultApi.md#apiV1TrendsGet) | **GET** /api/v1/trends |  |
| [**apiV2SearchGet**](DefaultApi.md#apiV2SearchGet) | **GET** /api/v2/search |  |


<a id="apiOembedGet"></a>
# **apiOembedGet**
> Card apiOembedGet(url, maxwidth, maxheight)



OEmbed as JSON

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String url = "url_example"; // String | URL of a status
    Integer maxwidth = 400; // Integer | width of the iframe. Defaults to 400
    Integer maxheight = 56; // Integer | height of the iframe. Defaults to null
    try {
      Card result = apiInstance.apiOembedGet(url, maxwidth, maxheight);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiOembedGet");
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
| **url** | **String**| URL of a status | [optional] |
| **maxwidth** | **Integer**| width of the iframe. Defaults to 400 | [optional] [default to 400] |
| **maxheight** | **Integer**| height of the iframe. Defaults to null | [optional] |

### Return type

[**Card**](Card.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Not Found |  -  |

<a id="apiProofsGet"></a>
# **apiProofsGet**
> IdentityProof apiProofsGet(provider, username)



View identity proof

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String provider = "provider_example"; // String | The identity provider to be looked up. Currently only supports keybase (case-sensitive)
    String username = "username_example"; // String | The username on the selected identity provider
    try {
      IdentityProof result = apiInstance.apiProofsGet(provider, username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiProofsGet");
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
| **provider** | **String**| The identity provider to be looked up. Currently only supports keybase (case-sensitive) | [optional] |
| **username** | **String**| The username on the selected identity provider | [optional] |

### Return type

[**IdentityProof**](IdentityProof.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Not Found |  -  |

<a id="apiV1AdminAccountsGet"></a>
# **apiV1AdminAccountsGet**
> List&lt;AdminAccount&gt; apiV1AdminAccountsGet(local, remote, byDomain, active, pending, disabled, silenced, suspended, staff, username, displayName, email, ip)



View accounts matching certain criteria for filtering, up to 100 at a time. Pagination may be done with the HTTP Link header in the response.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Boolean local = true; // Boolean | Filter for local accounts?
    Boolean remote = true; // Boolean | Filter for remote accounts?
    String byDomain = "byDomain_example"; // String | Filter by the given domain
    Boolean active = true; // Boolean | Filter for currently active accounts?
    Boolean pending = true; // Boolean | Filter for currently pending accounts?
    Boolean disabled = true; // Boolean | Filter for currently disabled accounts?
    Boolean silenced = true; // Boolean | Filter for currently silenced accounts?
    Boolean suspended = true; // Boolean | Filter for currently suspended accounts?
    Boolean staff = true; // Boolean | Filter for staff accounts?
    String username = "username_example"; // String | Username to search for
    String displayName = "displayName_example"; // String | Display name to search for
    String email = "email_example"; // String | Lookup a user with this email
    String ip = "ip_example"; // String | Lookup a user with this IP
    try {
      List<AdminAccount> result = apiInstance.apiV1AdminAccountsGet(local, remote, byDomain, active, pending, disabled, silenced, suspended, staff, username, displayName, email, ip);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1AdminAccountsGet");
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
| **local** | **Boolean**| Filter for local accounts? | [optional] |
| **remote** | **Boolean**| Filter for remote accounts? | [optional] |
| **byDomain** | **String**| Filter by the given domain | [optional] |
| **active** | **Boolean**| Filter for currently active accounts? | [optional] |
| **pending** | **Boolean**| Filter for currently pending accounts? | [optional] |
| **disabled** | **Boolean**| Filter for currently disabled accounts? | [optional] |
| **silenced** | **Boolean**| Filter for currently silenced accounts? | [optional] |
| **suspended** | **Boolean**| Filter for currently suspended accounts? | [optional] |
| **staff** | **Boolean**| Filter for staff accounts? | [optional] |
| **username** | **String**| Username to search for | [optional] |
| **displayName** | **String**| Display name to search for | [optional] |
| **email** | **String**| Lookup a user with this email | [optional] |
| **ip** | **String**| Lookup a user with this IP | [optional] |

### Return type

[**List&lt;AdminAccount&gt;**](AdminAccount.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="apiV1AdminAccountsIdActionPost"></a>
# **apiV1AdminAccountsIdActionPost**
> apiV1AdminAccountsIdActionPost(id, apiV1AdminAccountsIdActionPostRequest)



Perform an action against an account and log this action in the moderation history.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | ID of the account
    ApiV1AdminAccountsIdActionPostRequest apiV1AdminAccountsIdActionPostRequest = new ApiV1AdminAccountsIdActionPostRequest(); // ApiV1AdminAccountsIdActionPostRequest | 
    try {
      apiInstance.apiV1AdminAccountsIdActionPost(id, apiV1AdminAccountsIdActionPostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1AdminAccountsIdActionPost");
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
| **id** | **String**| ID of the account | |
| **apiV1AdminAccountsIdActionPostRequest** | [**ApiV1AdminAccountsIdActionPostRequest**](ApiV1AdminAccountsIdActionPostRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="apiV1AdminAccountsIdApprovePost"></a>
# **apiV1AdminAccountsIdApprovePost**
> apiV1AdminAccountsIdApprovePost(id)



Approve the given local account if it is currently pending approval.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | ID of the account
    try {
      apiInstance.apiV1AdminAccountsIdApprovePost(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1AdminAccountsIdApprovePost");
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
| **id** | **String**| ID of the account | |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="apiV1AdminAccountsIdEnablePost"></a>
# **apiV1AdminAccountsIdEnablePost**
> apiV1AdminAccountsIdEnablePost(id)



Re-enable a local account whose login is currently disabled.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | ID of the account
    try {
      apiInstance.apiV1AdminAccountsIdEnablePost(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1AdminAccountsIdEnablePost");
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
| **id** | **String**| ID of the account | |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="apiV1AdminAccountsIdGet"></a>
# **apiV1AdminAccountsIdGet**
> AdminAccount apiV1AdminAccountsIdGet(id)



View admin-level information about the given account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | ID of the account
    try {
      AdminAccount result = apiInstance.apiV1AdminAccountsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1AdminAccountsIdGet");
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
| **id** | **String**| ID of the account | |

### Return type

[**AdminAccount**](AdminAccount.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="apiV1AdminAccountsIdRejectPost"></a>
# **apiV1AdminAccountsIdRejectPost**
> apiV1AdminAccountsIdRejectPost(id)



Reject the given local account if it is currently pending approval.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | ID of the account
    try {
      apiInstance.apiV1AdminAccountsIdRejectPost(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1AdminAccountsIdRejectPost");
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
| **id** | **String**| ID of the account | |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="apiV1AdminAccountsIdUnsilencePost"></a>
# **apiV1AdminAccountsIdUnsilencePost**
> apiV1AdminAccountsIdUnsilencePost(id)



Unsilence a currently silenced account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | ID of the account
    try {
      apiInstance.apiV1AdminAccountsIdUnsilencePost(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1AdminAccountsIdUnsilencePost");
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
| **id** | **String**| ID of the account | |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="apiV1AdminAccountsIdUnsuspendPost"></a>
# **apiV1AdminAccountsIdUnsuspendPost**
> apiV1AdminAccountsIdUnsuspendPost(id)



Unsuspend a currently suspended account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | ID of the account
    try {
      apiInstance.apiV1AdminAccountsIdUnsuspendPost(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1AdminAccountsIdUnsuspendPost");
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
| **id** | **String**| ID of the account | |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="apiV1AdminReportsGet"></a>
# **apiV1AdminReportsGet**
> List&lt;AdminReport&gt; apiV1AdminReportsGet(resolved, accountId, targetAccountId)



View all reports. Pagination may be done with HTTP Link header in the response.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Boolean resolved = true; // Boolean | 
    String accountId = "accountId_example"; // String | 
    String targetAccountId = "targetAccountId_example"; // String | 
    try {
      List<AdminReport> result = apiInstance.apiV1AdminReportsGet(resolved, accountId, targetAccountId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1AdminReportsGet");
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
| **resolved** | **Boolean**|  | [optional] |
| **accountId** | **String**|  | [optional] |
| **targetAccountId** | **String**|  | [optional] |

### Return type

[**List&lt;AdminReport&gt;**](AdminReport.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="apiV1AdminReportsIdAssignToSelfPost"></a>
# **apiV1AdminReportsIdAssignToSelfPost**
> AdminReport apiV1AdminReportsIdAssignToSelfPost(id)



Claim the handling of this report to yourself.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | ID of the report
    try {
      AdminReport result = apiInstance.apiV1AdminReportsIdAssignToSelfPost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1AdminReportsIdAssignToSelfPost");
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
| **id** | **String**| ID of the report | |

### Return type

[**AdminReport**](AdminReport.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="apiV1AdminReportsIdGet"></a>
# **apiV1AdminReportsIdGet**
> AdminReport apiV1AdminReportsIdGet(id)



View information about the report with the given ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | ID of the report
    try {
      AdminReport result = apiInstance.apiV1AdminReportsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1AdminReportsIdGet");
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
| **id** | **String**| ID of the report | |

### Return type

[**AdminReport**](AdminReport.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="apiV1AdminReportsIdReopenPost"></a>
# **apiV1AdminReportsIdReopenPost**
> AdminReport apiV1AdminReportsIdReopenPost(id)



Mark a report as resolved with no further action taken.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | ID of the report
    try {
      AdminReport result = apiInstance.apiV1AdminReportsIdReopenPost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1AdminReportsIdReopenPost");
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
| **id** | **String**| ID of the report | |

### Return type

[**AdminReport**](AdminReport.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="apiV1AdminReportsIdResolvePost"></a>
# **apiV1AdminReportsIdResolvePost**
> AdminReport apiV1AdminReportsIdResolvePost(id)



Mark a report as resolved with no further action taken.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | ID of the report
    try {
      AdminReport result = apiInstance.apiV1AdminReportsIdResolvePost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1AdminReportsIdResolvePost");
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
| **id** | **String**| ID of the report | |

### Return type

[**AdminReport**](AdminReport.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="apiV1AdminReportsIdUnassignPost"></a>
# **apiV1AdminReportsIdUnassignPost**
> AdminReport apiV1AdminReportsIdUnassignPost(id)



Unassign a report so that someone else can claim it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | ID of the report
    try {
      AdminReport result = apiInstance.apiV1AdminReportsIdUnassignPost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1AdminReportsIdUnassignPost");
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
| **id** | **String**| ID of the report | |

### Return type

[**AdminReport**](AdminReport.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="apiV1AnnouncementsGet"></a>
# **apiV1AnnouncementsGet**
> List&lt;Announcement&gt; apiV1AnnouncementsGet(withDismissed)



See all currently active announcements set by admins.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Boolean withDismissed = true; // Boolean | If true, response will include announcements dismissed by the user. Defaults to false.
    try {
      List<Announcement> result = apiInstance.apiV1AnnouncementsGet(withDismissed);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1AnnouncementsGet");
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
| **withDismissed** | **Boolean**| If true, response will include announcements dismissed by the user. Defaults to false. | [optional] |

### Return type

[**List&lt;Announcement&gt;**](Announcement.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="apiV1AnnouncementsIdDismissPost"></a>
# **apiV1AnnouncementsIdDismissPost**
> Object apiV1AnnouncementsIdDismissPost(id)



Allows a user to mark the announcement as read.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | Local ID of an announcement in the database.
    try {
      Object result = apiInstance.apiV1AnnouncementsIdDismissPost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1AnnouncementsIdDismissPost");
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
| **id** | **String**| Local ID of an announcement in the database. | |

### Return type

**Object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="apiV1AnnouncementsIdReactionsNameDelete"></a>
# **apiV1AnnouncementsIdReactionsNameDelete**
> Object apiV1AnnouncementsIdReactionsNameDelete(id, name)



Undo a react emoji to an announcement.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | Local ID of an announcement in the database.
    String name = "name_example"; // String | Unicode emoji, or shortcode of custom emoji
    try {
      Object result = apiInstance.apiV1AnnouncementsIdReactionsNameDelete(id, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1AnnouncementsIdReactionsNameDelete");
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
| **id** | **String**| Local ID of an announcement in the database. | |
| **name** | **String**| Unicode emoji, or shortcode of custom emoji | |

### Return type

**Object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="apiV1AnnouncementsIdReactionsNamePut"></a>
# **apiV1AnnouncementsIdReactionsNamePut**
> Object apiV1AnnouncementsIdReactionsNamePut(id, name)



Allows a user to mark the announcement as read.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | Local ID of an announcement in the database.
    String name = "name_example"; // String | Unicode emoji, or shortcode of custom emoji
    try {
      Object result = apiInstance.apiV1AnnouncementsIdReactionsNamePut(id, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1AnnouncementsIdReactionsNamePut");
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
| **id** | **String**| Local ID of an announcement in the database. | |
| **name** | **String**| Unicode emoji, or shortcode of custom emoji | |

### Return type

**Object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="apiV1BlocksGet"></a>
# **apiV1BlocksGet**
> List&lt;Account&gt; apiV1BlocksGet(limit, maxId, sinceId)



Get blocked users.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer limit = 56; // Integer | 
    String maxId = "maxId_example"; // String | 
    String sinceId = "sinceId_example"; // String | 
    try {
      List<Account> result = apiInstance.apiV1BlocksGet(limit, maxId, sinceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1BlocksGet");
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
| **limit** | **Integer**|  | [optional] |
| **maxId** | **String**|  | [optional] |
| **sinceId** | **String**|  | [optional] |

### Return type

[**List&lt;Account&gt;**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |
| **401** | Invalid or missing Authorization header |  -  |

<a id="apiV1BookmarksGet"></a>
# **apiV1BookmarksGet**
> List&lt;Status&gt; apiV1BookmarksGet(limit, maxId, sinceId, minId)



Statuses the user has bookmarked.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer limit = 56; // Integer | 
    String maxId = "maxId_example"; // String | 
    String sinceId = "sinceId_example"; // String | 
    String minId = "minId_example"; // String | 
    try {
      List<Status> result = apiInstance.apiV1BookmarksGet(limit, maxId, sinceId, minId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1BookmarksGet");
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
| **limit** | **Integer**|  | [optional] |
| **maxId** | **String**|  | [optional] |
| **sinceId** | **String**|  | [optional] |
| **minId** | **String**|  | [optional] |

### Return type

[**List&lt;Status&gt;**](Status.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |
| **401** | Invalid or missing Authorization header |  -  |

<a id="apiV1ConversationsGet"></a>
# **apiV1ConversationsGet**
> List&lt;Conversation&gt; apiV1ConversationsGet(limit, maxId, sinceId, minId)



Show conversation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer limit = 20; // Integer | Max number of results to return. Defaults to 20.
    String maxId = "maxId_example"; // String | Return results older than ID
    String sinceId = "sinceId_example"; // String | Return results newer than ID
    String minId = "minId_example"; // String | Return results immediately newer than ID
    try {
      List<Conversation> result = apiInstance.apiV1ConversationsGet(limit, maxId, sinceId, minId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1ConversationsGet");
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
| **limit** | **Integer**| Max number of results to return. Defaults to 20. | [optional] [default to 20] |
| **maxId** | **String**| Return results older than ID | [optional] |
| **sinceId** | **String**| Return results newer than ID | [optional] |
| **minId** | **String**| Return results immediately newer than ID | [optional] |

### Return type

[**List&lt;Conversation&gt;**](Conversation.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. |  -  |
| **401** | Invalid or missing Authorization header |  -  |

<a id="apiV1ConversationsIdDelete"></a>
# **apiV1ConversationsIdDelete**
> Object apiV1ConversationsIdDelete(id)



Remove converstation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | ID of the conversation in the database
    try {
      Object result = apiInstance.apiV1ConversationsIdDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1ConversationsIdDelete");
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
| **id** | **String**| ID of the conversation in the database | |

### Return type

**Object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. |  -  |
| **401** | Invalid or missing Authorization header |  -  |
| **404** | Not Found |  -  |

<a id="apiV1ConversationsIdReadPost"></a>
# **apiV1ConversationsIdReadPost**
> Conversation apiV1ConversationsIdReadPost(id)



Remove converstation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | ID of the conversation in the database
    try {
      Conversation result = apiInstance.apiV1ConversationsIdReadPost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1ConversationsIdReadPost");
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
| **id** | **String**| ID of the conversation in the database | |

### Return type

[**Conversation**](Conversation.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The value of unread has been changed to false.. |  -  |
| **401** | Invalid or missing Authorization header |  -  |
| **404** | Not Found |  -  |

<a id="apiV1CustomEmojisGet"></a>
# **apiV1CustomEmojisGet**
> List&lt;Emoji&gt; apiV1CustomEmojisGet()



Returns custom emojis that are available on the server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      List<Emoji> result = apiInstance.apiV1CustomEmojisGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1CustomEmojisGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;Emoji&gt;**](Emoji.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Emojis |  -  |

<a id="apiV1DirectoryGet"></a>
# **apiV1DirectoryGet**
> List&lt;Account&gt; apiV1DirectoryGet(limit, offset, order, local)



List accounts visible in the directory.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer limit = 40; // Integer | How many accounts to load. Default 40.
    Integer offset = 0; // Integer | How many accounts to skip before returning results. Default 0.
    String order = "active"; // String | the `active` to sort by most recently posted statuses (default) or `new` to sort by most recently created profiles.
    Boolean local = true; // Boolean | Only return local accounts.
    try {
      List<Account> result = apiInstance.apiV1DirectoryGet(limit, offset, order, local);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1DirectoryGet");
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
| **limit** | **Integer**| How many accounts to load. Default 40. | [optional] [default to 40] |
| **offset** | **Integer**| How many accounts to skip before returning results. Default 0. | [optional] [default to 0] |
| **order** | **String**| the &#x60;active&#x60; to sort by most recently posted statuses (default) or &#x60;new&#x60; to sort by most recently created profiles. | [optional] [default to active] [enum: active, new] |
| **local** | **Boolean**| Only return local accounts. | [optional] |

### Return type

[**List&lt;Account&gt;**](Account.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of accounts |  -  |

<a id="apiV1DomainBlocksDelete"></a>
# **apiV1DomainBlocksDelete**
> Object apiV1DomainBlocksDelete(domain)



Remove a domain block, if it exists in the user&#39;s array of blocked domains.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String domain = "domain_example"; // String | Domain to unblock.
    try {
      Object result = apiInstance.apiV1DomainBlocksDelete(domain);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1DomainBlocksDelete");
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
| **domain** | **String**| Domain to unblock. | |

### Return type

**Object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |
| **401** | Invalid or missing Authorization header |  -  |
| **422** | If &#x60;domain&#x60; is not provided or contains spaces, the request will fail. |  -  |

<a id="apiV1DomainBlocksGet"></a>
# **apiV1DomainBlocksGet**
> List&lt;String&gt; apiV1DomainBlocksGet(limit, maxId, sinceId)



View domains the user has blocked.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer limit = 56; // Integer | 
    String maxId = "maxId_example"; // String | 
    String sinceId = "sinceId_example"; // String | 
    try {
      List<String> result = apiInstance.apiV1DomainBlocksGet(limit, maxId, sinceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1DomainBlocksGet");
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
| **limit** | **Integer**|  | [optional] |
| **maxId** | **String**|  | [optional] |
| **sinceId** | **String**|  | [optional] |

### Return type

**List&lt;String&gt;**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |
| **401** | Invalid or missing Authorization header |  -  |

<a id="apiV1DomainBlocksPost"></a>
# **apiV1DomainBlocksPost**
> Object apiV1DomainBlocksPost(apiV1DomainBlocksPostRequest)



\&quot;Block a domain to: - hide all public posts from it - hide all notifications from it - remove all followers from it - prevent following new users from it (but does not remove existing follows)\&quot; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ApiV1DomainBlocksPostRequest apiV1DomainBlocksPostRequest = new ApiV1DomainBlocksPostRequest(); // ApiV1DomainBlocksPostRequest | 
    try {
      Object result = apiInstance.apiV1DomainBlocksPost(apiV1DomainBlocksPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1DomainBlocksPost");
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
| **apiV1DomainBlocksPostRequest** | [**ApiV1DomainBlocksPostRequest**](ApiV1DomainBlocksPostRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |
| **401** | Invalid or missing Authorization header |  -  |
| **422** | If &#x60;domain&#x60; is not provided or contains spaces, the request will fail. |  -  |

<a id="apiV1EndorsementsGet"></a>
# **apiV1EndorsementsGet**
> List&lt;Account&gt; apiV1EndorsementsGet(limit, maxId, sinceId)



Accounts that the user is currently featuring on their profile.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer limit = 40; // Integer | Maximum number of results to return. Defaults to 40. Paginate using the HTTP Link header.
    String maxId = "maxId_example"; // String | Internal parameter. Use HTTP Link header from response for pagination
    String sinceId = "sinceId_example"; // String | Internal parameter. Use HTTP Link header from response for pagination.
    try {
      List<Account> result = apiInstance.apiV1EndorsementsGet(limit, maxId, sinceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1EndorsementsGet");
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
| **limit** | **Integer**| Maximum number of results to return. Defaults to 40. Paginate using the HTTP Link header. | [optional] [default to 40] |
| **maxId** | **String**| Internal parameter. Use HTTP Link header from response for pagination | [optional] |
| **sinceId** | **String**| Internal parameter. Use HTTP Link header from response for pagination. | [optional] |

### Return type

[**List&lt;Account&gt;**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. Because endorsement ids are private, you must parse the HTTP Link header to find next and previous pages. |  -  |
| **401** | Invalid or missing Authorization header |  -  |

<a id="apiV1FavouritesGet"></a>
# **apiV1FavouritesGet**
> List&lt;Status&gt; apiV1FavouritesGet(limit, maxId, minId)



Statuses the user has favourited.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String limit = "limit_example"; // String | 
    String maxId = "maxId_example"; // String | 
    String minId = "minId_example"; // String | 
    try {
      List<Status> result = apiInstance.apiV1FavouritesGet(limit, maxId, minId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1FavouritesGet");
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
| **limit** | **String**|  | [optional] |
| **maxId** | **String**|  | [optional] |
| **minId** | **String**|  | [optional] |

### Return type

[**List&lt;Status&gt;**](Status.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |
| **401** | Invalid or missing Authorization header |  -  |

<a id="apiV1FeaturedTagsGet"></a>
# **apiV1FeaturedTagsGet**
> List&lt;FeaturedTag&gt; apiV1FeaturedTagsGet()



View your featured tags.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      List<FeaturedTag> result = apiInstance.apiV1FeaturedTagsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1FeaturedTagsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;FeaturedTag&gt;**](FeaturedTag.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. |  -  |
| **401** | Invalid or missing Authorization header |  -  |

<a id="apiV1FeaturedTagsIdDelete"></a>
# **apiV1FeaturedTagsIdDelete**
> Object apiV1FeaturedTagsIdDelete(id)



Unfeature a tag

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The id of the FeaturedTag to be unfeatured.
    try {
      Object result = apiInstance.apiV1FeaturedTagsIdDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1FeaturedTagsIdDelete");
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
| **id** | **String**| The id of the FeaturedTag to be unfeatured. | |

### Return type

**Object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An empty object will be returned if the featured tag was successfully deleted. |  -  |
| **404** | If the ID does not exist or is not owned by you |  -  |

<a id="apiV1FeaturedTagsPost"></a>
# **apiV1FeaturedTagsPost**
> FeaturedTag apiV1FeaturedTagsPost(apiV1FeaturedTagsPostRequest)



Create a feature a tag.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ApiV1FeaturedTagsPostRequest apiV1FeaturedTagsPostRequest = new ApiV1FeaturedTagsPostRequest(); // ApiV1FeaturedTagsPostRequest | 
    try {
      FeaturedTag result = apiInstance.apiV1FeaturedTagsPost(apiV1FeaturedTagsPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1FeaturedTagsPost");
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
| **apiV1FeaturedTagsPostRequest** | [**ApiV1FeaturedTagsPostRequest**](ApiV1FeaturedTagsPostRequest.md)|  | [optional] |

### Return type

[**FeaturedTag**](FeaturedTag.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. |  -  |
| **422** | If name is not a valid hashtag, e.g. contains illegal characters or only numbers |  -  |

<a id="apiV1FeaturedTagsSuggestionsGet"></a>
# **apiV1FeaturedTagsSuggestionsGet**
> List&lt;FeaturedTag&gt; apiV1FeaturedTagsSuggestionsGet()



Shows your 10 most-used tags, with usage history for the past week.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      List<FeaturedTag> result = apiInstance.apiV1FeaturedTagsSuggestionsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1FeaturedTagsSuggestionsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;FeaturedTag&gt;**](FeaturedTag.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. |  -  |
| **401** | Invalid or missing Authorization header |  -  |

<a id="apiV1FiltersGet"></a>
# **apiV1FiltersGet**
> List&lt;Filter&gt; apiV1FiltersGet()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      List<Filter> result = apiInstance.apiV1FiltersGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1FiltersGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;Filter&gt;**](Filter.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Excerpts of various filters in different contexts. |  -  |
| **401** | Invalid or missing Authorization header |  -  |

<a id="apiV1FiltersIdDelete"></a>
# **apiV1FiltersIdDelete**
> apiV1FiltersIdDelete(id)



Delete a filter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The id of the account in the database
    try {
      apiInstance.apiV1FiltersIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1FiltersIdDelete");
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
| **id** | **String**| The id of the account in the database | |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The filter has been deleted successfully, so an empty object will be returned. |  -  |
| **401** | Invalid or missing Authorization header |  -  |
| **404** | Filter ID does not exist, or is not owned by you |  -  |

<a id="apiV1FiltersIdGet"></a>
# **apiV1FiltersIdGet**
> Filter apiV1FiltersIdGet(id)



Get one filter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The id of the account in the database
    try {
      Filter result = apiInstance.apiV1FiltersIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1FiltersIdGet");
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
| **id** | **String**| The id of the account in the database | |

### Return type

[**Filter**](Filter.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Filter returned successfully. |  -  |
| **401** | Invalid or missing Authorization header |  -  |
| **404** | Filter ID does not exist, or is not owned by you |  -  |

<a id="apiV1FiltersIdPut"></a>
# **apiV1FiltersIdPut**
> Filter apiV1FiltersIdPut(id, apiV1FiltersPostRequest)



Update a filter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The id of the account in the database
    ApiV1FiltersPostRequest apiV1FiltersPostRequest = new ApiV1FiltersPostRequest(); // ApiV1FiltersPostRequest | 
    try {
      Filter result = apiInstance.apiV1FiltersIdPut(id, apiV1FiltersPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1FiltersIdPut");
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
| **id** | **String**| The id of the account in the database | |
| **apiV1FiltersPostRequest** | [**ApiV1FiltersPostRequest**](ApiV1FiltersPostRequest.md)|  | [optional] |

### Return type

[**Filter**](Filter.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Filter updated successfully. |  -  |
| **401** | Invalid or missing Authorization header |  -  |
| **404** | Filter ID does not exist, or is not owned by you |  -  |
| **422** | If phrase or context are not provided properly |  -  |

<a id="apiV1FiltersPost"></a>
# **apiV1FiltersPost**
> Filter apiV1FiltersPost(apiV1FiltersPostRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ApiV1FiltersPostRequest apiV1FiltersPostRequest = new ApiV1FiltersPostRequest(); // ApiV1FiltersPostRequest | 
    try {
      Filter result = apiInstance.apiV1FiltersPost(apiV1FiltersPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1FiltersPost");
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
| **apiV1FiltersPostRequest** | [**ApiV1FiltersPostRequest**](ApiV1FiltersPostRequest.md)|  | [optional] |

### Return type

[**Filter**](Filter.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The newly-created filter will be returned. |  -  |
| **401** | Invalid or missing Authorization header |  -  |
| **422** | If phrase or context are not provided properly |  -  |

<a id="apiV1FollowRequestsGet"></a>
# **apiV1FollowRequestsGet**
> List&lt;Account&gt; apiV1FollowRequestsGet(limit)



Pending Follows

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer limit = 40; // Integer | Maximum number of results to return. Defaults to 40. Paginate using the HTTP Link header.
    try {
      List<Account> result = apiInstance.apiV1FollowRequestsGet(limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1FollowRequestsGet");
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
| **limit** | **Integer**| Maximum number of results to return. Defaults to 40. Paginate using the HTTP Link header. | [optional] [default to 40] |

### Return type

[**List&lt;Account&gt;**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Accounts that are requesting a follow. |  -  |
| **401** | Invalid or missing Authorization header |  -  |

<a id="apiV1FollowRequestsIdAuthorizePost"></a>
# **apiV1FollowRequestsIdAuthorizePost**
> Relationship apiV1FollowRequestsIdAuthorizePost(id)



Accept Follow

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The id of the account in the database
    try {
      Relationship result = apiInstance.apiV1FollowRequestsIdAuthorizePost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1FollowRequestsIdAuthorizePost");
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
| **id** | **String**| The id of the account in the database | |

### Return type

[**Relationship**](Relationship.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Your Relationship with this account should be updated so that you are followed_by this account. |  -  |
| **401** | Invalid or missing Authorization header |  -  |
| **404** | No pending follow request from that user ID |  -  |

<a id="apiV1FollowRequestsIdRejectPost"></a>
# **apiV1FollowRequestsIdRejectPost**
> Relationship apiV1FollowRequestsIdRejectPost(id)



Accept Follow

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The id of the account in the database
    try {
      Relationship result = apiInstance.apiV1FollowRequestsIdRejectPost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1FollowRequestsIdRejectPost");
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
| **id** | **String**| The id of the account in the database | |

### Return type

[**Relationship**](Relationship.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Your Relationship with this Account should be unchanged. |  -  |
| **401** | Invalid or missing Authorization header |  -  |
| **404** | No pending follow request from that user ID |  -  |

<a id="apiV1InstanceActivityGet"></a>
# **apiV1InstanceActivityGet**
> List&lt;Activity&gt; apiV1InstanceActivityGet()



Instance activity over the last 3 months, binned weekly.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      List<Activity> result = apiInstance.apiV1InstanceActivityGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1InstanceActivityGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;Activity&gt;**](Activity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Domains that this instance is aware of. |  -  |

<a id="apiV1InstanceGet"></a>
# **apiV1InstanceGet**
> Instance apiV1InstanceGet()



Information about the server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      Instance result = apiInstance.apiV1InstanceGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1InstanceGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Instance**](Instance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Result |  -  |

<a id="apiV1InstancePeersGet"></a>
# **apiV1InstancePeersGet**
> List&lt;String&gt; apiV1InstancePeersGet()



Information about the server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      List<String> result = apiInstance.apiV1InstancePeersGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1InstancePeersGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Domains that this instance is aware of. |  -  |

<a id="apiV1ListsDelete"></a>
# **apiV1ListsDelete**
> Object apiV1ListsDelete()



Delete a list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      Object result = apiInstance.apiV1ListsDelete();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1ListsDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list was deleted successfully |  -  |
| **401** | Invalid or missing Authorization header |  -  |
| **404** | Not found |  -  |

<a id="apiV1ListsGet"></a>
# **apiV1ListsGet**
> List&lt;ModelList&gt; apiV1ListsGet()



Fetch all lists that the user owns.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      List<ModelList> result = apiInstance.apiV1ListsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1ListsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;ModelList&gt;**](ModelList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Use id as a parameter for related API calls. |  -  |
| **401** | Invalid or missing Authorization header |  -  |

<a id="apiV1ListsIdAccountsDelete"></a>
# **apiV1ListsIdAccountsDelete**
> Object apiV1ListsIdAccountsDelete(id, accountIds)



Remove accounts from the given list.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | ID of the list in the database
    List<String> accountIds = Arrays.asList(); // List<String> | Array of account IDs to add to the list.
    try {
      Object result = apiInstance.apiV1ListsIdAccountsDelete(id, accountIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1ListsIdAccountsDelete");
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
| **id** | **String**| ID of the list in the database | |
| **accountIds** | [**List&lt;String&gt;**](String.md)| Array of account IDs to add to the list. | |

### Return type

**Object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Account was successfully removed from the list, or it was already not in the list. |  -  |
| **401** | Invalid or missing Authorization header |  -  |
| **404** | Not Found |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="apiV1ListsIdAccountsGet"></a>
# **apiV1ListsIdAccountsGet**
> List&lt;Account&gt; apiV1ListsIdAccountsGet(id, limit, maxId, sinceId)



View accounts in List

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | ID of the list in the database
    Integer limit = 40; // Integer | Maximum number of results. Defaults to 40. Max 40. Set to 0 in order to get all accounts without pagination. Pagination is done with the HTTP Link header.
    String maxId = "maxId_example"; // String | Return results older than ID
    String sinceId = "sinceId_example"; // String | Return results newer than ID
    try {
      List<Account> result = apiInstance.apiV1ListsIdAccountsGet(id, limit, maxId, sinceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1ListsIdAccountsGet");
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
| **id** | **String**| ID of the list in the database | |
| **limit** | **Integer**| Maximum number of results. Defaults to 40. Max 40. Set to 0 in order to get all accounts without pagination. Pagination is done with the HTTP Link header. | [optional] [default to 40] |
| **maxId** | **String**| Return results older than ID | [optional] |
| **sinceId** | **String**| Return results newer than ID | [optional] |

### Return type

[**List&lt;Account&gt;**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Invalid or missing Authorization header |  -  |
| **404** | Not Found |  -  |

<a id="apiV1ListsIdAccountsPost"></a>
# **apiV1ListsIdAccountsPost**
> Object apiV1ListsIdAccountsPost(id, apiV1ListsIdAccountsPostRequest)



Add accounts to the given list. Note that the user must be following these accounts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | ID of the list in the database
    ApiV1ListsIdAccountsPostRequest apiV1ListsIdAccountsPostRequest = new ApiV1ListsIdAccountsPostRequest(); // ApiV1ListsIdAccountsPostRequest | 
    try {
      Object result = apiInstance.apiV1ListsIdAccountsPost(id, apiV1ListsIdAccountsPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1ListsIdAccountsPost");
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
| **id** | **String**| ID of the list in the database | |
| **apiV1ListsIdAccountsPostRequest** | [**ApiV1ListsIdAccountsPostRequest**](ApiV1ListsIdAccountsPostRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Invalid or missing Authorization header |  -  |
| **404** | Not Found |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="apiV1ListsIdGet"></a>
# **apiV1ListsIdGet**
> ModelList apiV1ListsIdGet(id)



Remove converstation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | ID of the list in the database
    try {
      ModelList result = apiInstance.apiV1ListsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1ListsIdGet");
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
| **id** | **String**| ID of the list in the database | |

### Return type

[**ModelList**](ModelList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The value of unread has been changed to false.. |  -  |
| **401** | Invalid or missing Authorization header |  -  |
| **404** | Not Found |  -  |

<a id="apiV1ListsPost"></a>
# **apiV1ListsPost**
> ModelList apiV1ListsPost(apiV1ListsPostRequest)



Create a new list.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ApiV1ListsPostRequest apiV1ListsPostRequest = new ApiV1ListsPostRequest(); // ApiV1ListsPostRequest | 
    try {
      ModelList result = apiInstance.apiV1ListsPost(apiV1ListsPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1ListsPost");
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
| **apiV1ListsPostRequest** | [**ApiV1ListsPostRequest**](ApiV1ListsPostRequest.md)|  | [optional] |

### Return type

[**ModelList**](ModelList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list was created successfully |  -  |
| **401** | Invalid or missing Authorization header |  -  |

<a id="apiV1ListsPut"></a>
# **apiV1ListsPut**
> ModelList apiV1ListsPut(apiV1ListsPutRequest)



Change the title of a list, or which replies to show.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ApiV1ListsPutRequest apiV1ListsPutRequest = new ApiV1ListsPutRequest(); // ApiV1ListsPutRequest | 
    try {
      ModelList result = apiInstance.apiV1ListsPut(apiV1ListsPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1ListsPut");
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
| **apiV1ListsPutRequest** | [**ApiV1ListsPutRequest**](ApiV1ListsPutRequest.md)|  | [optional] |

### Return type

[**ModelList**](ModelList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list was updated successfully |  -  |
| **401** | Invalid or missing Authorization header |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="apiV1MarkersGet"></a>
# **apiV1MarkersGet**
> Object apiV1MarkersGet(timeline)



Get saved timeline position

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    List<Object> timeline = null; // List<Object> | Array of markers to fetch. String enum anyOf home, notifications. If not provided, an empty object will be returned.
    try {
      Object result = apiInstance.apiV1MarkersGet(timeline);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1MarkersGet");
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
| **timeline** | [**List&lt;Object&gt;**](Object.md)| Array of markers to fetch. String enum anyOf home, notifications. If not provided, an empty object will be returned. | |

### Return type

**Object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Account was successfully removed from the list, or it was already not in the list. |  -  |
| **401** | Invalid or missing Authorization header |  -  |

<a id="apiV1MarkersPost"></a>
# **apiV1MarkersPost**
> Object apiV1MarkersPost(body)



Get saved timeline position

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Object body = null; // Object | 
    try {
      Object result = apiInstance.apiV1MarkersPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1MarkersPost");
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
| **body** | **Object**|  | [optional] |

### Return type

**Object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Account was successfully removed from the list, or it was already not in the list. |  -  |
| **401** | Invalid or missing Authorization header |  -  |
| **409** | Conflict, If object is stale while being updated, an error will occur. |  -  |

<a id="apiV1MediaIdGet"></a>
# **apiV1MediaIdGet**
> Attachment apiV1MediaIdGet(id)



Get an attachement.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The id of the Attachment entity to be updated.
    try {
      Attachment result = apiInstance.apiV1MediaIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1MediaIdGet");
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
| **id** | **String**| The id of the Attachment entity to be updated. | |

### Return type

[**Attachment**](Attachment.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Attachment created successfully. Note that the Attachment will be created even if the file is not understood correctly. |  -  |
| **206** | Attachment is not yet ready. |  -  |
| **401** | Invalid or missing Authorization header |  -  |
| **404** | Attachment does not exist, is deleted, or was not created by you |  -  |
| **422** | File or file type is unsupported or invalid |  -  |

<a id="apiV1MediaIdPost"></a>
# **apiV1MediaIdPost**
> Attachment apiV1MediaIdPost(id, apiV1MediaPostRequest)



Update an Attachment, before it is attached to a status and posted.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The id of the Attachment entity to be updated.
    ApiV1MediaPostRequest apiV1MediaPostRequest = new ApiV1MediaPostRequest(); // ApiV1MediaPostRequest | 
    try {
      Attachment result = apiInstance.apiV1MediaIdPost(id, apiV1MediaPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1MediaIdPost");
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
| **id** | **String**| The id of the Attachment entity to be updated. | |
| **apiV1MediaPostRequest** | [**ApiV1MediaPostRequest**](ApiV1MediaPostRequest.md)|  | [optional] |

### Return type

[**Attachment**](Attachment.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Attachment updated successfully. |  -  |
| **401** | Invalid or missing Authorization header |  -  |
| **404** | Attachment does not exist, is deleted, or was not created by you |  -  |
| **422** | File or file type is unsupported or invalid |  -  |

<a id="apiV1MediaPost"></a>
# **apiV1MediaPost**
> Attachment apiV1MediaPost(apiV1MediaPostRequest)



Creates an attachment to be used with a new status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ApiV1MediaPostRequest apiV1MediaPostRequest = new ApiV1MediaPostRequest(); // ApiV1MediaPostRequest | 
    try {
      Attachment result = apiInstance.apiV1MediaPost(apiV1MediaPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1MediaPost");
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
| **apiV1MediaPostRequest** | [**ApiV1MediaPostRequest**](ApiV1MediaPostRequest.md)|  | [optional] |

### Return type

[**Attachment**](Attachment.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Attachment created successfully. Note that the Attachment will be created even if the file is not understood correctly. |  -  |
| **401** | Invalid or missing Authorization header |  -  |
| **422** | File or file type is unsupported or invalid |  -  |

<a id="apiV1MutesGet"></a>
# **apiV1MutesGet**
> List&lt;Account&gt; apiV1MutesGet(limit, maxId, sinceId)



Accounts the user has muted.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String limit = "limit_example"; // String | 
    String maxId = "maxId_example"; // String | 
    String sinceId = "sinceId_example"; // String | 
    try {
      List<Account> result = apiInstance.apiV1MutesGet(limit, maxId, sinceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1MutesGet");
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
| **limit** | **String**|  | [optional] |
| **maxId** | **String**|  | [optional] |
| **sinceId** | **String**|  | [optional] |

### Return type

[**List&lt;Account&gt;**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |
| **401** | Invalid or missing Authorization header |  -  |

<a id="apiV1NotificationsClearPost"></a>
# **apiV1NotificationsClearPost**
> Object apiV1NotificationsClearPost()



Clear all notifications from the server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      Object result = apiInstance.apiV1NotificationsClearPost();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1NotificationsClearPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Invalid or missing Authorization header |  -  |

<a id="apiV1NotificationsGet"></a>
# **apiV1NotificationsGet**
> List&lt;Notification&gt; apiV1NotificationsGet(limit, maxId, sinceId, minId, excludeTypes, accountId)



Notifications concerning the user. This API returns Link headers containing links to the next/previous page. However, the links can also be constructed dynamically using query params and id values.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer limit = 20; // Integer | Max number of results to return. Defaults to 20.
    String maxId = "maxId_example"; // String | Return results older than ID
    String sinceId = "sinceId_example"; // String | Return results newer than ID
    String minId = "minId_example"; // String | Return results immediately newer than ID
    List<String> excludeTypes = Arrays.asList(); // List<String> | Array of types to exclude (follow, favourite, reblog, mention, poll, follow_request)
    String accountId = "accountId_example"; // String | Return only notifications received from this account
    try {
      List<Notification> result = apiInstance.apiV1NotificationsGet(limit, maxId, sinceId, minId, excludeTypes, accountId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1NotificationsGet");
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
| **limit** | **Integer**| Max number of results to return. Defaults to 20. | [optional] [default to 20] |
| **maxId** | **String**| Return results older than ID | [optional] |
| **sinceId** | **String**| Return results newer than ID | [optional] |
| **minId** | **String**| Return results immediately newer than ID | [optional] |
| **excludeTypes** | [**List&lt;String&gt;**](String.md)| Array of types to exclude (follow, favourite, reblog, mention, poll, follow_request) | [optional] |
| **accountId** | **String**| Return only notifications received from this account | [optional] |

### Return type

[**List&lt;Notification&gt;**](Notification.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Invalid or missing Authorization header |  -  |

<a id="apiV1NotificationsIdDismissPost"></a>
# **apiV1NotificationsIdDismissPost**
> Notification apiV1NotificationsIdDismissPost(id)



Clear a single notification from the server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | ID of the notification in the database.
    try {
      Notification result = apiInstance.apiV1NotificationsIdDismissPost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1NotificationsIdDismissPost");
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
| **id** | **String**| ID of the notification in the database. | |

### Return type

[**Notification**](Notification.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Notification with given ID successfully dismissed |  -  |
| **401** | Invalid or missing Authorization header |  -  |

<a id="apiV1NotificationsIdGet"></a>
# **apiV1NotificationsIdGet**
> Notification apiV1NotificationsIdGet(id)



View information about a notification with a given ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | ID of the notification in the database.
    try {
      Notification result = apiInstance.apiV1NotificationsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1NotificationsIdGet");
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
| **id** | **String**| ID of the notification in the database. | |

### Return type

[**Notification**](Notification.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Invalid or missing Authorization header |  -  |

<a id="apiV1PollsIdGet"></a>
# **apiV1PollsIdGet**
> Poll apiV1PollsIdGet(id)



View a poll.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | ID of the poll in the database.
    try {
      Poll result = apiInstance.apiV1PollsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1PollsIdGet");
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
| **id** | **String**| ID of the poll in the database. | |

### Return type

[**Poll**](Poll.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get one poll. |  -  |
| **404** | Poll does not exist, or poll&#39;s parent status is private |  -  |

<a id="apiV1PollsIdPost"></a>
# **apiV1PollsIdPost**
> Poll apiV1PollsIdPost(id, apiV1PollsIdPostRequest)



Vote on a poll.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | ID of the poll in the database.
    ApiV1PollsIdPostRequest apiV1PollsIdPostRequest = new ApiV1PollsIdPostRequest(); // ApiV1PollsIdPostRequest | 
    try {
      Poll result = apiInstance.apiV1PollsIdPost(id, apiV1PollsIdPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1PollsIdPost");
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
| **id** | **String**| ID of the poll in the database. | |
| **apiV1PollsIdPostRequest** | [**ApiV1PollsIdPostRequest**](ApiV1PollsIdPostRequest.md)|  | [optional] |

### Return type

[**Poll**](Poll.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get one poll. |  -  |
| **401** | Invalid or missing Authorization header |  -  |
| **404** | Poll does not exist, or poll&#39;s parent status is private. |  -  |
| **422** | Already voted or poll is expired. |  -  |

<a id="apiV1PreferencesGet"></a>
# **apiV1PreferencesGet**
> Preferences apiV1PreferencesGet()



Shows your 10 most-used tags, with usage history for the past week.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      Preferences result = apiInstance.apiV1PreferencesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1PreferencesGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Preferences**](Preferences.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. |  -  |
| **401** | Invalid or missing Authorization header |  -  |

<a id="apiV1PushSubscriptionDelete"></a>
# **apiV1PushSubscriptionDelete**
> Object apiV1PushSubscriptionDelete()



Updates the current push subscription. Only the data part can be updated. To change fundamentals, a new subscription must be created instead.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      Object result = apiInstance.apiV1PushSubscriptionDelete();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1PushSubscriptionDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updating a PushSubscription to only receive mention alerts |  -  |

<a id="apiV1PushSubscriptionGet"></a>
# **apiV1PushSubscriptionGet**
> PushSubscription apiV1PushSubscriptionGet()



View the PushSubscription currently associated with this access token.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      PushSubscription result = apiInstance.apiV1PushSubscriptionGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1PushSubscriptionGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PushSubscription**](PushSubscription.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get one PushSubscription |  -  |
| **404** | Not Found |  -  |

<a id="apiV1PushSubscriptionPost"></a>
# **apiV1PushSubscriptionPost**
> PushSubscription apiV1PushSubscriptionPost(apiV1PushSubscriptionPostRequest)



Add a Web Push API subscription to receive notifications. Each access token can have one push subscription. If you create a new subscription, the old subscription is deleted.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ApiV1PushSubscriptionPostRequest apiV1PushSubscriptionPostRequest = new ApiV1PushSubscriptionPostRequest(); // ApiV1PushSubscriptionPostRequest | 
    try {
      PushSubscription result = apiInstance.apiV1PushSubscriptionPost(apiV1PushSubscriptionPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1PushSubscriptionPost");
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
| **apiV1PushSubscriptionPostRequest** | [**ApiV1PushSubscriptionPostRequest**](ApiV1PushSubscriptionPostRequest.md)|  | [optional] |

### Return type

[**PushSubscription**](PushSubscription.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | PushSubscription created |  -  |
| **401** | Invalid or missing Authorization header |  -  |

<a id="apiV1PushSubscriptionPut"></a>
# **apiV1PushSubscriptionPut**
> PushSubscription apiV1PushSubscriptionPut(apiV1PushSubscriptionPutRequest)



Updates the current push subscription. Only the data part can be updated. To change fundamentals, a new subscription must be created instead.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ApiV1PushSubscriptionPutRequest apiV1PushSubscriptionPutRequest = new ApiV1PushSubscriptionPutRequest(); // ApiV1PushSubscriptionPutRequest | 
    try {
      PushSubscription result = apiInstance.apiV1PushSubscriptionPut(apiV1PushSubscriptionPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1PushSubscriptionPut");
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
| **apiV1PushSubscriptionPutRequest** | [**ApiV1PushSubscriptionPutRequest**](ApiV1PushSubscriptionPutRequest.md)|  | [optional] |

### Return type

[**PushSubscription**](PushSubscription.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updating a PushSubscription to only receive mention alerts |  -  |
| **404** | Not Found |  -  |

<a id="apiV1ReportsPost"></a>
# **apiV1ReportsPost**
> Report apiV1ReportsPost(apiV1ReportsPostRequest)



File a report.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ApiV1ReportsPostRequest apiV1ReportsPostRequest = new ApiV1ReportsPostRequest(); // ApiV1ReportsPostRequest | 
    try {
      Report result = apiInstance.apiV1ReportsPost(apiV1ReportsPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1ReportsPost");
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
| **apiV1ReportsPostRequest** | [**ApiV1ReportsPostRequest**](ApiV1ReportsPostRequest.md)|  | [optional] |

### Return type

[**Report**](Report.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully reported. |  -  |
| **401** | Invalid or missing Authorization header |  -  |

<a id="apiV1ScheduledStatusesGet"></a>
# **apiV1ScheduledStatusesGet**
> List&lt;ScheduledStatus&gt; apiV1ScheduledStatusesGet(limit, maxId, sinceId, minId)



View scheduled statuses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer limit = 20; // Integer | Max number of results to return. Defaults to 20.
    String maxId = "maxId_example"; // String | Return results older than ID
    String sinceId = "sinceId_example"; // String | Return results newer than ID
    String minId = "minId_example"; // String | Return results immediately newer than ID
    try {
      List<ScheduledStatus> result = apiInstance.apiV1ScheduledStatusesGet(limit, maxId, sinceId, minId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1ScheduledStatusesGet");
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
| **limit** | **Integer**| Max number of results to return. Defaults to 20. | [optional] [default to 20] |
| **maxId** | **String**| Return results older than ID | [optional] |
| **sinceId** | **String**| Return results newer than ID | [optional] |
| **minId** | **String**| Return results immediately newer than ID | [optional] |

### Return type

[**List&lt;ScheduledStatus&gt;**](ScheduledStatus.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get scheduled statuses. |  -  |
| **401** | Invalid or missing Authorization header |  -  |

<a id="apiV1ScheduledStatusesIdDelete"></a>
# **apiV1ScheduledStatusesIdDelete**
> Object apiV1ScheduledStatusesIdDelete(id)



Cancel a scheduled status

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | ID of the scheduled status in the database.
    try {
      Object result = apiInstance.apiV1ScheduledStatusesIdDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1ScheduledStatusesIdDelete");
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
| **id** | **String**| ID of the scheduled status in the database. | |

### Return type

**Object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. |  -  |
| **401** | Invalid or missing Authorization header |  -  |
| **404** | Not Found |  -  |

<a id="apiV1ScheduledStatusesIdGet"></a>
# **apiV1ScheduledStatusesIdGet**
> ScheduledStatus apiV1ScheduledStatusesIdGet(id)



View a single scheduled status

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | ID of the scheduled status in the database.
    try {
      ScheduledStatus result = apiInstance.apiV1ScheduledStatusesIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1ScheduledStatusesIdGet");
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
| **id** | **String**| ID of the scheduled status in the database. | |

### Return type

[**ScheduledStatus**](ScheduledStatus.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. |  -  |
| **401** | Invalid or missing Authorization header |  -  |
| **404** | Not Found |  -  |

<a id="apiV1ScheduledStatusesIdPut"></a>
# **apiV1ScheduledStatusesIdPut**
> ScheduledStatus apiV1ScheduledStatusesIdPut(id, apiV1ScheduledStatusesIdPutRequest)



View a single scheduled status

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | ID of the scheduled status in the database.
    ApiV1ScheduledStatusesIdPutRequest apiV1ScheduledStatusesIdPutRequest = new ApiV1ScheduledStatusesIdPutRequest(); // ApiV1ScheduledStatusesIdPutRequest | 
    try {
      ScheduledStatus result = apiInstance.apiV1ScheduledStatusesIdPut(id, apiV1ScheduledStatusesIdPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1ScheduledStatusesIdPut");
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
| **id** | **String**| ID of the scheduled status in the database. | |
| **apiV1ScheduledStatusesIdPutRequest** | [**ApiV1ScheduledStatusesIdPutRequest**](ApiV1ScheduledStatusesIdPutRequest.md)|  | [optional] |

### Return type

[**ScheduledStatus**](ScheduledStatus.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. |  -  |
| **401** | Invalid or missing Authorization header |  -  |
| **404** | Not Found |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="apiV1StatusesIdBookmarkPost"></a>
# **apiV1StatusesIdBookmarkPost**
> Status apiV1StatusesIdBookmarkPost(id)



Privately bookmark a status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | Local ID of a status in the database.
    try {
      Status result = apiInstance.apiV1StatusesIdBookmarkPost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1StatusesIdBookmarkPost");
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
| **id** | **String**| Local ID of a status in the database. | |

### Return type

[**Status**](Status.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status bookmarked |  -  |
| **401** | Invalid or missing Authorization header |  -  |
| **404** | Status does not exist, is deleted, or is private |  -  |

<a id="apiV1StatusesIdContextGet"></a>
# **apiV1StatusesIdContextGet**
> Context apiV1StatusesIdContextGet(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | Local ID of a status in the database.
    try {
      Context result = apiInstance.apiV1StatusesIdContextGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1StatusesIdContextGet");
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
| **id** | **String**| Local ID of a status in the database. | |

### Return type

[**Context**](Context.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Status does not exist, is deleted, or is private |  -  |

<a id="apiV1StatusesIdDelete"></a>
# **apiV1StatusesIdDelete**
> Status apiV1StatusesIdDelete(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | Local ID of a status in the database.
    try {
      Status result = apiInstance.apiV1StatusesIdDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1StatusesIdDelete");
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
| **id** | **String**| Local ID of a status in the database. | |

### Return type

[**Status**](Status.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status will be posted with chosen parameters. If scheduled_at is provided, then a ScheduledStatus will be returned instead. |  -  |
| **401** | Invalid or missing Authorization header |  -  |
| **404** | Status does not exist, is deleted, or is private. |  -  |

<a id="apiV1StatusesIdFavouritePost"></a>
# **apiV1StatusesIdFavouritePost**
> Status apiV1StatusesIdFavouritePost(id)



Add a status to your favourites list.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | Local ID of a status in the database.
    try {
      Status result = apiInstance.apiV1StatusesIdFavouritePost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1StatusesIdFavouritePost");
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
| **id** | **String**| Local ID of a status in the database. | |

### Return type

[**Status**](Status.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Invalid or missing Authorization header |  -  |
| **404** | Status does not exist, is deleted, or is private |  -  |

<a id="apiV1StatusesIdFavouritedByGet"></a>
# **apiV1StatusesIdFavouritedByGet**
> Account apiV1StatusesIdFavouritedByGet(id)



View who favourited a given status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | Local ID of a status in the database.
    try {
      Account result = apiInstance.apiV1StatusesIdFavouritedByGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1StatusesIdFavouritedByGet");
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
| **id** | **String**| Local ID of a status in the database. | |

### Return type

[**Account**](Account.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Status does not exist, is deleted, or is private |  -  |

<a id="apiV1StatusesIdGet"></a>
# **apiV1StatusesIdGet**
> Status apiV1StatusesIdGet(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | Local ID of a status in the database.
    try {
      Status result = apiInstance.apiV1StatusesIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1StatusesIdGet");
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
| **id** | **String**| Local ID of a status in the database. | |

### Return type

[**Status**](Status.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status will be posted with chosen parameters. If scheduled_at is provided, then a ScheduledStatus will be returned instead. |  -  |
| **401** | Invalid or missing Authorization header |  -  |
| **404** | Status does not exist, is deleted, or is private. |  -  |

<a id="apiV1StatusesIdMutePost"></a>
# **apiV1StatusesIdMutePost**
> Status apiV1StatusesIdMutePost(id)



Do not receive notifications for the thread that this status is part of. Must be a thread in which you are a participant.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | Local ID of a status in the database.
    try {
      Status result = apiInstance.apiV1StatusesIdMutePost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1StatusesIdMutePost");
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
| **id** | **String**| Local ID of a status in the database. | |

### Return type

[**Status**](Status.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status&#39;s conversation muted, or was already muted |  -  |
| **401** | Invalid or missing Authorization header |  -  |
| **404** | Status does not exist, is deleted, or is private |  -  |

<a id="apiV1StatusesIdPinPost"></a>
# **apiV1StatusesIdPinPost**
> Status apiV1StatusesIdPinPost(id)



Feature one of your own public statuses at the top of your profile.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | Local ID of a status in the database.
    try {
      Status result = apiInstance.apiV1StatusesIdPinPost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1StatusesIdPinPost");
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
| **id** | **String**| Local ID of a status in the database. | |

### Return type

[**Status**](Status.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status pinned. Note the status is not a reblog and its authoring account is your own. |  -  |
| **401** | Invalid or missing Authorization header |  -  |
| **404** | Status does not exist, is deleted, or is private |  -  |
| **422** | Status is not owned by you, or is not public. You cannot pin one of your private statuses because private statuses cannot be fetched from remote sites, and must be delivered. |  -  |

<a id="apiV1StatusesIdReblogPost"></a>
# **apiV1StatusesIdReblogPost**
> Status apiV1StatusesIdReblogPost(id, apiV1StatusesIdReblogPostRequest)



Reshare a status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | Local ID of a status in the database.
    ApiV1StatusesIdReblogPostRequest apiV1StatusesIdReblogPostRequest = new ApiV1StatusesIdReblogPostRequest(); // ApiV1StatusesIdReblogPostRequest | 
    try {
      Status result = apiInstance.apiV1StatusesIdReblogPost(id, apiV1StatusesIdReblogPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1StatusesIdReblogPost");
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
| **id** | **String**| Local ID of a status in the database. | |
| **apiV1StatusesIdReblogPostRequest** | [**ApiV1StatusesIdReblogPostRequest**](ApiV1StatusesIdReblogPostRequest.md)|  | [optional] |

### Return type

[**Status**](Status.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status has been reblogged. Note that the top-level id has changed. The id of the boosted status is now inside the reblog property. The top-level id is the id of the reblog itself. Also note that reblogs cannot be pinned. |  -  |
| **401** | Invalid or missing Authorization header |  -  |
| **404** | Status does not exist, is deleted, or is private |  -  |

<a id="apiV1StatusesIdRebloggedByGet"></a>
# **apiV1StatusesIdRebloggedByGet**
> Account apiV1StatusesIdRebloggedByGet(id)



View who boosted a given status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | Local ID of a status in the database.
    try {
      Account result = apiInstance.apiV1StatusesIdRebloggedByGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1StatusesIdRebloggedByGet");
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
| **id** | **String**| Local ID of a status in the database. | |

### Return type

[**Account**](Account.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Status does not exist, is deleted, or is private |  -  |

<a id="apiV1StatusesIdUnbookmarkPost"></a>
# **apiV1StatusesIdUnbookmarkPost**
> Status apiV1StatusesIdUnbookmarkPost(id)



Remove a status from your private bookmarks.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | Local ID of a status in the database.
    try {
      Status result = apiInstance.apiV1StatusesIdUnbookmarkPost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1StatusesIdUnbookmarkPost");
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
| **id** | **String**| Local ID of a status in the database. | |

### Return type

[**Status**](Status.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status unbookmarked |  -  |
| **401** | Invalid or missing Authorization header |  -  |
| **404** | Status does not exist, is deleted, or is private |  -  |

<a id="apiV1StatusesIdUnfavouritePost"></a>
# **apiV1StatusesIdUnfavouritePost**
> Status apiV1StatusesIdUnfavouritePost(id)



Remove a status from your favourites list.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | Local ID of a status in the database.
    try {
      Status result = apiInstance.apiV1StatusesIdUnfavouritePost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1StatusesIdUnfavouritePost");
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
| **id** | **String**| Local ID of a status in the database. | |

### Return type

[**Status**](Status.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Invalid or missing Authorization header |  -  |
| **404** | Status does not exist, is deleted, or is private |  -  |

<a id="apiV1StatusesIdUnmutePost"></a>
# **apiV1StatusesIdUnmutePost**
> Status apiV1StatusesIdUnmutePost(id)



Status&#39;s conversation unmuted, or was already unmuted

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | Local ID of a status in the database.
    try {
      Status result = apiInstance.apiV1StatusesIdUnmutePost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1StatusesIdUnmutePost");
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
| **id** | **String**| Local ID of a status in the database. | |

### Return type

[**Status**](Status.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status&#39;s conversation muted, or was already muted |  -  |
| **401** | Invalid or missing Authorization header |  -  |
| **404** | Status does not exist, is deleted, or is private |  -  |

<a id="apiV1StatusesIdUnpinPost"></a>
# **apiV1StatusesIdUnpinPost**
> Status apiV1StatusesIdUnpinPost(id)



Unfeature a status from the top of your profile.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | Local ID of a status in the database.
    try {
      Status result = apiInstance.apiV1StatusesIdUnpinPost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1StatusesIdUnpinPost");
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
| **id** | **String**| Local ID of a status in the database. | |

### Return type

[**Status**](Status.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status unpinned, or was already not pinned |  -  |
| **401** | Invalid or missing Authorization header |  -  |
| **404** | Status does not exist, is deleted, or is private |  -  |

<a id="apiV1StatusesIdUnreblogPost"></a>
# **apiV1StatusesIdUnreblogPost**
> Status apiV1StatusesIdUnreblogPost(id)



Undo a reshare of a status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | Local ID of a status in the database.
    try {
      Status result = apiInstance.apiV1StatusesIdUnreblogPost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1StatusesIdUnreblogPost");
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
| **id** | **String**| Local ID of a status in the database. | |

### Return type

[**Status**](Status.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status no longer reblogged |  -  |
| **401** | Invalid or missing Authorization header |  -  |
| **404** | Status does not exist, is deleted, or is private |  -  |

<a id="apiV1StatusesPost"></a>
# **apiV1StatusesPost**
> ApiV1StatusesPost200Response apiV1StatusesPost(idempotencyKey, apiV1StatusesPostRequestInner)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String idempotencyKey = "idempotencyKey_example"; // String | Prevent duplicate submissions of the same status. Idempotency keys are stored for up to 1 hour, and can be any arbitrary string. Consider using a hash or UUID generated client-side.
    List<ApiV1StatusesPostRequestInner> apiV1StatusesPostRequestInner = Arrays.asList(); // List<ApiV1StatusesPostRequestInner> | 
    try {
      ApiV1StatusesPost200Response result = apiInstance.apiV1StatusesPost(idempotencyKey, apiV1StatusesPostRequestInner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1StatusesPost");
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
| **idempotencyKey** | **String**| Prevent duplicate submissions of the same status. Idempotency keys are stored for up to 1 hour, and can be any arbitrary string. Consider using a hash or UUID generated client-side. | [optional] |
| **apiV1StatusesPostRequestInner** | [**List&lt;ApiV1StatusesPostRequestInner&gt;**](ApiV1StatusesPostRequestInner.md)|  | [optional] |

### Return type

[**ApiV1StatusesPost200Response**](ApiV1StatusesPost200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status will be posted with chosen parameters. If scheduled_at is provided, then a ScheduledStatus will be returned instead. |  -  |
| **401** | Invalid or missing Authorization header |  -  |

<a id="apiV1SuggestionsGet"></a>
# **apiV1SuggestionsGet**
> Account apiV1SuggestionsGet(limit)



Accounts the user has had past positive interactions with, but is not yet following.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer limit = 40; // Integer | Maximum number of results to return. Defaults to 40.
    try {
      Account result = apiInstance.apiV1SuggestionsGet(limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1SuggestionsGet");
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
| **limit** | **Integer**| Maximum number of results to return. Defaults to 40. | [optional] [default to 40] |

### Return type

[**Account**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. |  -  |
| **401** | Invalid or missing Authorization header |  -  |

<a id="apiV1SuggestionsIdDelete"></a>
# **apiV1SuggestionsIdDelete**
> Object apiV1SuggestionsIdDelete(id)



Delete user suggestion

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | id of the account in the database to be removed from suggestions
    try {
      Object result = apiInstance.apiV1SuggestionsIdDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1SuggestionsIdDelete");
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
| **id** | **String**| id of the account in the database to be removed from suggestions | |

### Return type

**Object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully removed |  -  |
| **401** | Invalid or missing Authorization header |  -  |

<a id="apiV1TimelinesHomeGet"></a>
# **apiV1TimelinesHomeGet**
> List&lt;Status&gt; apiV1TimelinesHomeGet(local, limit, maxId, sinceId, minId)



View statuses from followed users.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Boolean local = false; // Boolean | Show only local statuses? Defaults to false.
    Integer limit = 20; // Integer | Max number of results to return. Defaults to 20.
    String maxId = "maxId_example"; // String | Return results older than ID
    String sinceId = "sinceId_example"; // String | Return results newer than ID
    String minId = "minId_example"; // String | Return results immediately newer than ID
    try {
      List<Status> result = apiInstance.apiV1TimelinesHomeGet(local, limit, maxId, sinceId, minId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1TimelinesHomeGet");
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
| **local** | **Boolean**| Show only local statuses? Defaults to false. | [optional] [default to false] |
| **limit** | **Integer**| Max number of results to return. Defaults to 20. | [optional] [default to 20] |
| **maxId** | **String**| Return results older than ID | [optional] |
| **sinceId** | **String**| Return results newer than ID | [optional] |
| **minId** | **String**| Return results immediately newer than ID | [optional] |

### Return type

[**List&lt;Status&gt;**](Status.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get statuses for home. |  -  |
| **206** | Home feed is regenerating |  -  |
| **401** | Invalid or missing Authorization header |  -  |

<a id="apiV1TimelinesListListIdGet"></a>
# **apiV1TimelinesListListIdGet**
> List&lt;Status&gt; apiV1TimelinesListListIdGet(listId, limit, maxId, sinceId, minId)



View statuses in the given list timeline.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String listId = "listId_example"; // String | Local ID of the list in the database.
    Integer limit = 20; // Integer | Max number of results to return. Defaults to 20.
    String maxId = "maxId_example"; // String | Return results older than ID
    String sinceId = "sinceId_example"; // String | Return results newer than ID
    String minId = "minId_example"; // String | Return results immediately newer than ID
    try {
      List<Status> result = apiInstance.apiV1TimelinesListListIdGet(listId, limit, maxId, sinceId, minId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1TimelinesListListIdGet");
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
| **listId** | **String**| Local ID of the list in the database. | |
| **limit** | **Integer**| Max number of results to return. Defaults to 20. | [optional] [default to 20] |
| **maxId** | **String**| Return results older than ID | [optional] |
| **sinceId** | **String**| Return results newer than ID | [optional] |
| **minId** | **String**| Return results immediately newer than ID | [optional] |

### Return type

[**List&lt;Status&gt;**](Status.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Statuses in this list will be returned.. |  -  |
| **401** | Invalid or missing Authorization header |  -  |

<a id="apiV1TimelinesPublicGet"></a>
# **apiV1TimelinesPublicGet**
> List&lt;Status&gt; apiV1TimelinesPublicGet(local, remote, onlyMedia, limit, maxId, sinceId, minId)



Public timeline

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Boolean local = false; // Boolean | Show only local statuses? Defaults to false.
    Boolean remote = false; // Boolean | Show only local statuses? Defaults to false.
    Boolean onlyMedia = false; // Boolean | Show only statuses with media attached? Defaults to false..
    Integer limit = 20; // Integer | Max number of results to return. Defaults to 20.
    String maxId = "maxId_example"; // String | Return results older than ID
    String sinceId = "sinceId_example"; // String | Return results newer than ID
    String minId = "minId_example"; // String | Return results immediately newer than ID
    try {
      List<Status> result = apiInstance.apiV1TimelinesPublicGet(local, remote, onlyMedia, limit, maxId, sinceId, minId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1TimelinesPublicGet");
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
| **local** | **Boolean**| Show only local statuses? Defaults to false. | [optional] [default to false] |
| **remote** | **Boolean**| Show only local statuses? Defaults to false. | [optional] [default to false] |
| **onlyMedia** | **Boolean**| Show only statuses with media attached? Defaults to false.. | [optional] [default to false] |
| **limit** | **Integer**| Max number of results to return. Defaults to 20. | [optional] [default to 20] |
| **maxId** | **String**| Return results older than ID | [optional] |
| **sinceId** | **String**| Return results newer than ID | [optional] |
| **minId** | **String**| Return results immediately newer than ID | [optional] |

### Return type

[**List&lt;Status&gt;**](Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | get statuses. |  -  |

<a id="apiV1TimelinesTagHashtagGet"></a>
# **apiV1TimelinesTagHashtagGet**
> List&lt;Status&gt; apiV1TimelinesTagHashtagGet(hashtag, local, remote, onlyMedia, limit, maxId, sinceId, minId)



View public statuses containing the given hashtag.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String hashtag = "hashtag_example"; // String | Content of a `#hashtag``, not including `#` symbol..
    Boolean local = false; // Boolean | Show only local statuses? Defaults to false.
    Boolean remote = false; // Boolean | Show only local statuses? Defaults to false.
    Boolean onlyMedia = false; // Boolean | Show only statuses with media attached? Defaults to false..
    Integer limit = 20; // Integer | Max number of results to return. Defaults to 20.
    String maxId = "maxId_example"; // String | Return results older than ID
    String sinceId = "sinceId_example"; // String | Return results newer than ID
    String minId = "minId_example"; // String | Return results immediately newer than ID
    try {
      List<Status> result = apiInstance.apiV1TimelinesTagHashtagGet(hashtag, local, remote, onlyMedia, limit, maxId, sinceId, minId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1TimelinesTagHashtagGet");
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
| **hashtag** | **String**| Content of a &#x60;#hashtag&#x60;&#x60;, not including &#x60;#&#x60; symbol.. | |
| **local** | **Boolean**| Show only local statuses? Defaults to false. | [optional] [default to false] |
| **remote** | **Boolean**| Show only local statuses? Defaults to false. | [optional] [default to false] |
| **onlyMedia** | **Boolean**| Show only statuses with media attached? Defaults to false.. | [optional] [default to false] |
| **limit** | **Integer**| Max number of results to return. Defaults to 20. | [optional] [default to 20] |
| **maxId** | **String**| Return results older than ID | [optional] |
| **sinceId** | **String**| Return results newer than ID | [optional] |
| **minId** | **String**| Return results immediately newer than ID | [optional] |

### Return type

[**List&lt;Status&gt;**](Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get statuses. |  -  |

<a id="apiV1TrendsGet"></a>
# **apiV1TrendsGet**
> List&lt;Tag&gt; apiV1TrendsGet(limit)



Tags that are being used more frequently within the past week.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer limit = 10; // Integer | Max number of results to return. Defaults to 10.
    try {
      List<Tag> result = apiInstance.apiV1TrendsGet(limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1TrendsGet");
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
| **limit** | **Integer**| Max number of results to return. Defaults to 10. | [optional] [default to 10] |

### Return type

[**List&lt;Tag&gt;**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Domains that this instance is aware of. |  -  |

<a id="apiV2SearchGet"></a>
# **apiV2SearchGet**
> ApiV2SearchGet200Response apiV2SearchGet(q, limit, resolve, following, accountId, maxId, minId, type, excludeUnreviewed, offset)



Search results

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String q = "q_example"; // String | What to search for
    Integer limit = 20; // Integer | Maximum number of results. Defaults to 40.
    String resolve = "resolve_example"; // String | Attempt WebFinger lookup.
    Boolean following = true; // Boolean | Only who the user is following. Defaults to false.
    String accountId = "accountId_example"; // String | If provided, statuses returned will be authored only by this account
    String maxId = "maxId_example"; // String | Return results older than this id
    String minId = "minId_example"; // String | Return results immediately newer than this id
    String type = "accounts"; // String | Enum(accounts, hashtags, statuses)
    Boolean excludeUnreviewed = true; // Boolean | Filter out unreviewed tags? Defaults to false. Use true when trying to find trending tags.
    Integer offset = 56; // Integer | Offset in search results. Used for pagination. Defaults to 0.
    try {
      ApiV2SearchGet200Response result = apiInstance.apiV2SearchGet(q, limit, resolve, following, accountId, maxId, minId, type, excludeUnreviewed, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV2SearchGet");
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
| **q** | **String**| What to search for | |
| **limit** | **Integer**| Maximum number of results. Defaults to 40. | [optional] [default to 20] |
| **resolve** | **String**| Attempt WebFinger lookup. | [optional] |
| **following** | **Boolean**| Only who the user is following. Defaults to false. | [optional] |
| **accountId** | **String**| If provided, statuses returned will be authored only by this account | [optional] |
| **maxId** | **String**| Return results older than this id | [optional] |
| **minId** | **String**| Return results immediately newer than this id | [optional] |
| **type** | **String**| Enum(accounts, hashtags, statuses) | [optional] [enum: accounts, hashtags, statuses] |
| **excludeUnreviewed** | **Boolean**| Filter out unreviewed tags? Defaults to false. Use true when trying to find trending tags. | [optional] |
| **offset** | **Integer**| Offset in search results. Used for pagination. Defaults to 0. | [optional] |

### Return type

[**ApiV2SearchGet200Response**](ApiV2SearchGet200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Result |  -  |
| **401** | Invalid or missing Authorization header |  -  |

