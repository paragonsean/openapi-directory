# ActivityApi

All URIs are relative to *http://HOSTNAME/api/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**activityCheckRepoIsStarredByAuthenticatedUser**](ActivityApi.md#activityCheckRepoIsStarredByAuthenticatedUser) | **GET** /user/starred/{owner}/{repo} | Check if a repository is starred by the authenticated user |
| [**activityDeleteRepoSubscription**](ActivityApi.md#activityDeleteRepoSubscription) | **DELETE** /repos/{owner}/{repo}/subscription | Delete a repository subscription |
| [**activityDeleteThreadSubscription**](ActivityApi.md#activityDeleteThreadSubscription) | **DELETE** /notifications/threads/{thread_id}/subscription | Delete a thread subscription |
| [**activityGetFeeds**](ActivityApi.md#activityGetFeeds) | **GET** /feeds | Get feeds |
| [**activityGetRepoSubscription**](ActivityApi.md#activityGetRepoSubscription) | **GET** /repos/{owner}/{repo}/subscription | Get a repository subscription |
| [**activityGetThread**](ActivityApi.md#activityGetThread) | **GET** /notifications/threads/{thread_id} | Get a thread |
| [**activityGetThreadSubscriptionForAuthenticatedUser**](ActivityApi.md#activityGetThreadSubscriptionForAuthenticatedUser) | **GET** /notifications/threads/{thread_id}/subscription | Get a thread subscription for the authenticated user |
| [**activityListEventsForAuthenticatedUser**](ActivityApi.md#activityListEventsForAuthenticatedUser) | **GET** /users/{username}/events | List events for the authenticated user |
| [**activityListNotificationsForAuthenticatedUser**](ActivityApi.md#activityListNotificationsForAuthenticatedUser) | **GET** /notifications | List notifications for the authenticated user |
| [**activityListOrgEventsForAuthenticatedUser**](ActivityApi.md#activityListOrgEventsForAuthenticatedUser) | **GET** /users/{username}/events/orgs/{org} | List organization events for the authenticated user |
| [**activityListPublicEvents**](ActivityApi.md#activityListPublicEvents) | **GET** /events | List public events |
| [**activityListPublicEventsForRepoNetwork**](ActivityApi.md#activityListPublicEventsForRepoNetwork) | **GET** /networks/{owner}/{repo}/events | List public events for a network of repositories |
| [**activityListPublicEventsForUser**](ActivityApi.md#activityListPublicEventsForUser) | **GET** /users/{username}/events/public | List public events for a user |
| [**activityListPublicOrgEvents**](ActivityApi.md#activityListPublicOrgEvents) | **GET** /orgs/{org}/events | List public organization events |
| [**activityListReceivedEventsForUser**](ActivityApi.md#activityListReceivedEventsForUser) | **GET** /users/{username}/received_events | List events received by the authenticated user |
| [**activityListReceivedPublicEventsForUser**](ActivityApi.md#activityListReceivedPublicEventsForUser) | **GET** /users/{username}/received_events/public | List public events received by a user |
| [**activityListRepoEvents**](ActivityApi.md#activityListRepoEvents) | **GET** /repos/{owner}/{repo}/events | List repository events |
| [**activityListRepoNotificationsForAuthenticatedUser**](ActivityApi.md#activityListRepoNotificationsForAuthenticatedUser) | **GET** /repos/{owner}/{repo}/notifications | List repository notifications for the authenticated user |
| [**activityListReposStarredByAuthenticatedUser**](ActivityApi.md#activityListReposStarredByAuthenticatedUser) | **GET** /user/starred | List repositories starred by the authenticated user |
| [**activityListReposStarredByUser**](ActivityApi.md#activityListReposStarredByUser) | **GET** /users/{username}/starred | List repositories starred by a user |
| [**activityListReposWatchedByUser**](ActivityApi.md#activityListReposWatchedByUser) | **GET** /users/{username}/subscriptions | List repositories watched by a user |
| [**activityListStargazersForRepo**](ActivityApi.md#activityListStargazersForRepo) | **GET** /repos/{owner}/{repo}/stargazers | List stargazers |
| [**activityListWatchedReposForAuthenticatedUser**](ActivityApi.md#activityListWatchedReposForAuthenticatedUser) | **GET** /user/subscriptions | List repositories watched by the authenticated user |
| [**activityListWatchersForRepo**](ActivityApi.md#activityListWatchersForRepo) | **GET** /repos/{owner}/{repo}/subscribers | List watchers |
| [**activityMarkNotificationsAsRead**](ActivityApi.md#activityMarkNotificationsAsRead) | **PUT** /notifications | Mark notifications as read |
| [**activityMarkRepoNotificationsAsRead**](ActivityApi.md#activityMarkRepoNotificationsAsRead) | **PUT** /repos/{owner}/{repo}/notifications | Mark repository notifications as read |
| [**activityMarkThreadAsRead**](ActivityApi.md#activityMarkThreadAsRead) | **PATCH** /notifications/threads/{thread_id} | Mark a thread as read |
| [**activitySetRepoSubscription**](ActivityApi.md#activitySetRepoSubscription) | **PUT** /repos/{owner}/{repo}/subscription | Set a repository subscription |
| [**activitySetThreadSubscription**](ActivityApi.md#activitySetThreadSubscription) | **PUT** /notifications/threads/{thread_id}/subscription | Set a thread subscription |
| [**activityStarRepoForAuthenticatedUser**](ActivityApi.md#activityStarRepoForAuthenticatedUser) | **PUT** /user/starred/{owner}/{repo} | Star a repository for the authenticated user |
| [**activityUnstarRepoForAuthenticatedUser**](ActivityApi.md#activityUnstarRepoForAuthenticatedUser) | **DELETE** /user/starred/{owner}/{repo} | Unstar a repository for the authenticated user |


<a id="activityCheckRepoIsStarredByAuthenticatedUser"></a>
# **activityCheckRepoIsStarredByAuthenticatedUser**
> activityCheckRepoIsStarredByAuthenticatedUser(owner, repo)

Check if a repository is starred by the authenticated user



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ActivityApi apiInstance = new ActivityApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    try {
      apiInstance.activityCheckRepoIsStarredByAuthenticatedUser(owner, repo);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityApi#activityCheckRepoIsStarredByAuthenticatedUser");
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
| **owner** | **String**|  | |
| **repo** | **String**|  | |

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
| **204** | Response if this repository is starred by you |  -  |
| **304** | Not modified |  -  |
| **401** | Requires authentication |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found if this repository is not starred by you |  -  |

<a id="activityDeleteRepoSubscription"></a>
# **activityDeleteRepoSubscription**
> activityDeleteRepoSubscription(owner, repo)

Delete a repository subscription

This endpoint should only be used to stop watching a repository. To control whether or not you wish to receive notifications from a repository, [set the repository&#39;s subscription manually](https://docs.github.com/enterprise-server@2.22/rest/reference/activity#set-a-repository-subscription).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ActivityApi apiInstance = new ActivityApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    try {
      apiInstance.activityDeleteRepoSubscription(owner, repo);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityApi#activityDeleteRepoSubscription");
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
| **owner** | **String**|  | |
| **repo** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |

<a id="activityDeleteThreadSubscription"></a>
# **activityDeleteThreadSubscription**
> activityDeleteThreadSubscription(threadId)

Delete a thread subscription

Mutes all future notifications for a conversation until you comment on the thread or get an **@mention**. If you are watching the repository of the thread, you will still receive notifications. To ignore future notifications for a repository you are watching, use the [Set a thread subscription](https://docs.github.com/enterprise-server@2.22/rest/reference/activity#set-a-thread-subscription) endpoint and set &#x60;ignore&#x60; to &#x60;true&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ActivityApi apiInstance = new ActivityApi(defaultClient);
    Integer threadId = 56; // Integer | thread_id parameter
    try {
      apiInstance.activityDeleteThreadSubscription(threadId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityApi#activityDeleteThreadSubscription");
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
| **threadId** | **Integer**| thread_id parameter | |

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
| **204** | Response |  -  |
| **304** | Not modified |  -  |
| **401** | Requires authentication |  -  |
| **403** | Forbidden |  -  |

<a id="activityGetFeeds"></a>
# **activityGetFeeds**
> Feed activityGetFeeds()

Get feeds

GitHub Enterprise Server provides several timeline resources in [Atom](http://en.wikipedia.org/wiki/Atom_(standard)) format. The Feeds API lists all the feeds available to the authenticated user:  *   **Timeline**: The GitHub Enterprise Server global public timeline *   **User**: The public timeline for any user, using [URI template](https://docs.github.com/enterprise-server@2.22/rest/overview/resources-in-the-rest-api#hypermedia) *   **Current user public**: The public timeline for the authenticated user *   **Current user**: The private timeline for the authenticated user *   **Current user actor**: The private timeline for activity created by the authenticated user *   **Current user organizations**: The private timeline for the organizations the authenticated user is a member of. *   **Security advisories**: A collection of public announcements that provide information about security-related vulnerabilities in software on GitHub Enterprise Server.  **Note**: Private feeds are only returned when [authenticating via Basic Auth](https://docs.github.com/enterprise-server@2.22/rest/overview/other-authentication-methods#basic-authentication) since current feed URIs use the older, non revocable auth tokens.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ActivityApi apiInstance = new ActivityApi(defaultClient);
    try {
      Feed result = apiInstance.activityGetFeeds();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityApi#activityGetFeeds");
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

[**Feed**](Feed.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="activityGetRepoSubscription"></a>
# **activityGetRepoSubscription**
> RepositorySubscription activityGetRepoSubscription(owner, repo)

Get a repository subscription



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ActivityApi apiInstance = new ActivityApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    try {
      RepositorySubscription result = apiInstance.activityGetRepoSubscription(owner, repo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityApi#activityGetRepoSubscription");
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
| **owner** | **String**|  | |
| **repo** | **String**|  | |

### Return type

[**RepositorySubscription**](RepositorySubscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | if you subscribe to the repository |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found if you don&#39;t subscribe to the repository |  -  |

<a id="activityGetThread"></a>
# **activityGetThread**
> Thread activityGetThread(threadId)

Get a thread



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ActivityApi apiInstance = new ActivityApi(defaultClient);
    Integer threadId = 56; // Integer | thread_id parameter
    try {
      Thread result = apiInstance.activityGetThread(threadId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityApi#activityGetThread");
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
| **threadId** | **Integer**| thread_id parameter | |

### Return type

[**Thread**](Thread.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **304** | Not modified |  -  |
| **401** | Requires authentication |  -  |
| **403** | Forbidden |  -  |

<a id="activityGetThreadSubscriptionForAuthenticatedUser"></a>
# **activityGetThreadSubscriptionForAuthenticatedUser**
> ThreadSubscription activityGetThreadSubscriptionForAuthenticatedUser(threadId)

Get a thread subscription for the authenticated user

This checks to see if the current user is subscribed to a thread. You can also [get a repository subscription](https://docs.github.com/enterprise-server@2.22/rest/reference/activity#get-a-repository-subscription).  Note that subscriptions are only generated if a user is participating in a conversation--for example, they&#39;ve replied to the thread, were **@mentioned**, or manually subscribe to a thread.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ActivityApi apiInstance = new ActivityApi(defaultClient);
    Integer threadId = 56; // Integer | thread_id parameter
    try {
      ThreadSubscription result = apiInstance.activityGetThreadSubscriptionForAuthenticatedUser(threadId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityApi#activityGetThreadSubscriptionForAuthenticatedUser");
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
| **threadId** | **Integer**| thread_id parameter | |

### Return type

[**ThreadSubscription**](ThreadSubscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **304** | Not modified |  -  |
| **401** | Requires authentication |  -  |
| **403** | Forbidden |  -  |

<a id="activityListEventsForAuthenticatedUser"></a>
# **activityListEventsForAuthenticatedUser**
> List&lt;Event&gt; activityListEventsForAuthenticatedUser(username, perPage, page)

List events for the authenticated user

If you are authenticated as the given user, you will see your private events. Otherwise, you&#39;ll only see public events.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ActivityApi apiInstance = new ActivityApi(defaultClient);
    String username = "username_example"; // String | 
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Event> result = apiInstance.activityListEventsForAuthenticatedUser(username, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityApi#activityListEventsForAuthenticatedUser");
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
| **username** | **String**|  | |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;Event&gt;**](Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="activityListNotificationsForAuthenticatedUser"></a>
# **activityListNotificationsForAuthenticatedUser**
> List&lt;Thread&gt; activityListNotificationsForAuthenticatedUser(all, participating, since, before, perPage, page)

List notifications for the authenticated user

List all notifications for the current user, sorted by most recently updated.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ActivityApi apiInstance = new ActivityApi(defaultClient);
    Boolean all = false; // Boolean | If `true`, show notifications marked as read.
    Boolean participating = false; // Boolean | If `true`, only shows notifications in which the user is directly participating or mentioned.
    OffsetDateTime since = OffsetDateTime.now(); // OffsetDateTime | Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
    OffsetDateTime before = OffsetDateTime.now(); // OffsetDateTime | Only show notifications updated before the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Thread> result = apiInstance.activityListNotificationsForAuthenticatedUser(all, participating, since, before, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityApi#activityListNotificationsForAuthenticatedUser");
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
| **all** | **Boolean**| If &#x60;true&#x60;, show notifications marked as read. | [optional] [default to false] |
| **participating** | **Boolean**| If &#x60;true&#x60;, only shows notifications in which the user is directly participating or mentioned. | [optional] [default to false] |
| **since** | **OffsetDateTime**| Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] |
| **before** | **OffsetDateTime**| Only show notifications updated before the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;Thread&gt;**](Thread.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |
| **304** | Not modified |  -  |
| **401** | Requires authentication |  -  |
| **403** | Forbidden |  -  |
| **422** | Validation failed |  -  |

<a id="activityListOrgEventsForAuthenticatedUser"></a>
# **activityListOrgEventsForAuthenticatedUser**
> List&lt;Event&gt; activityListOrgEventsForAuthenticatedUser(username, org, perPage, page)

List organization events for the authenticated user

This is the user&#39;s organization dashboard. You must be authenticated as the user to view this.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ActivityApi apiInstance = new ActivityApi(defaultClient);
    String username = "username_example"; // String | 
    String org = "org_example"; // String | 
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Event> result = apiInstance.activityListOrgEventsForAuthenticatedUser(username, org, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityApi#activityListOrgEventsForAuthenticatedUser");
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
| **username** | **String**|  | |
| **org** | **String**|  | |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;Event&gt;**](Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="activityListPublicEvents"></a>
# **activityListPublicEvents**
> List&lt;Event&gt; activityListPublicEvents(perPage, page)

List public events

We delay the public events feed by five minutes, which means the most recent event returned by the public events API actually occurred at least five minutes ago.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ActivityApi apiInstance = new ActivityApi(defaultClient);
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Event> result = apiInstance.activityListPublicEvents(perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityApi#activityListPublicEvents");
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
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;Event&gt;**](Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **304** | Not modified |  -  |
| **403** | Forbidden |  -  |
| **503** | Service unavailable |  -  |

<a id="activityListPublicEventsForRepoNetwork"></a>
# **activityListPublicEventsForRepoNetwork**
> List&lt;Event&gt; activityListPublicEventsForRepoNetwork(owner, repo, perPage, page)

List public events for a network of repositories



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ActivityApi apiInstance = new ActivityApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Event> result = apiInstance.activityListPublicEventsForRepoNetwork(owner, repo, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityApi#activityListPublicEventsForRepoNetwork");
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
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;Event&gt;**](Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **301** | Moved permanently |  -  |
| **304** | Not modified |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |

<a id="activityListPublicEventsForUser"></a>
# **activityListPublicEventsForUser**
> List&lt;Event&gt; activityListPublicEventsForUser(username, perPage, page)

List public events for a user



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ActivityApi apiInstance = new ActivityApi(defaultClient);
    String username = "username_example"; // String | 
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Event> result = apiInstance.activityListPublicEventsForUser(username, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityApi#activityListPublicEventsForUser");
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
| **username** | **String**|  | |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;Event&gt;**](Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="activityListPublicOrgEvents"></a>
# **activityListPublicOrgEvents**
> List&lt;Event&gt; activityListPublicOrgEvents(org, perPage, page)

List public organization events



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ActivityApi apiInstance = new ActivityApi(defaultClient);
    String org = "org_example"; // String | 
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Event> result = apiInstance.activityListPublicOrgEvents(org, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityApi#activityListPublicOrgEvents");
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
| **org** | **String**|  | |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;Event&gt;**](Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="activityListReceivedEventsForUser"></a>
# **activityListReceivedEventsForUser**
> List&lt;Event&gt; activityListReceivedEventsForUser(username, perPage, page)

List events received by the authenticated user

These are events that you&#39;ve received by watching repos and following users. If you are authenticated as the given user, you will see private events. Otherwise, you&#39;ll only see public events.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ActivityApi apiInstance = new ActivityApi(defaultClient);
    String username = "username_example"; // String | 
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Event> result = apiInstance.activityListReceivedEventsForUser(username, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityApi#activityListReceivedEventsForUser");
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
| **username** | **String**|  | |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;Event&gt;**](Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="activityListReceivedPublicEventsForUser"></a>
# **activityListReceivedPublicEventsForUser**
> List&lt;Event&gt; activityListReceivedPublicEventsForUser(username, perPage, page)

List public events received by a user



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ActivityApi apiInstance = new ActivityApi(defaultClient);
    String username = "username_example"; // String | 
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Event> result = apiInstance.activityListReceivedPublicEventsForUser(username, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityApi#activityListReceivedPublicEventsForUser");
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
| **username** | **String**|  | |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;Event&gt;**](Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="activityListRepoEvents"></a>
# **activityListRepoEvents**
> List&lt;Event&gt; activityListRepoEvents(owner, repo, perPage, page)

List repository events



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ActivityApi apiInstance = new ActivityApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Event> result = apiInstance.activityListRepoEvents(owner, repo, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityApi#activityListRepoEvents");
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
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;Event&gt;**](Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="activityListRepoNotificationsForAuthenticatedUser"></a>
# **activityListRepoNotificationsForAuthenticatedUser**
> List&lt;Thread&gt; activityListRepoNotificationsForAuthenticatedUser(owner, repo, all, participating, since, before, perPage, page)

List repository notifications for the authenticated user

List all notifications for the current user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ActivityApi apiInstance = new ActivityApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Boolean all = false; // Boolean | If `true`, show notifications marked as read.
    Boolean participating = false; // Boolean | If `true`, only shows notifications in which the user is directly participating or mentioned.
    OffsetDateTime since = OffsetDateTime.now(); // OffsetDateTime | Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
    OffsetDateTime before = OffsetDateTime.now(); // OffsetDateTime | Only show notifications updated before the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Thread> result = apiInstance.activityListRepoNotificationsForAuthenticatedUser(owner, repo, all, participating, since, before, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityApi#activityListRepoNotificationsForAuthenticatedUser");
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
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **all** | **Boolean**| If &#x60;true&#x60;, show notifications marked as read. | [optional] [default to false] |
| **participating** | **Boolean**| If &#x60;true&#x60;, only shows notifications in which the user is directly participating or mentioned. | [optional] [default to false] |
| **since** | **OffsetDateTime**| Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] |
| **before** | **OffsetDateTime**| Only show notifications updated before the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;Thread&gt;**](Thread.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="activityListReposStarredByAuthenticatedUser"></a>
# **activityListReposStarredByAuthenticatedUser**
> List&lt;Repository&gt; activityListReposStarredByAuthenticatedUser(sort, direction, perPage, page)

List repositories starred by the authenticated user

Lists repositories the authenticated user has starred.  You can also find out _when_ stars were created by passing the following custom [media type](https://docs.github.com/enterprise-server@2.22/rest/overview/media-types/) via the &#x60;Accept&#x60; header:

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ActivityApi apiInstance = new ActivityApi(defaultClient);
    String sort = "created"; // String | One of `created` (when the repository was starred) or `updated` (when it was last pushed to).
    String direction = "asc"; // String | One of `asc` (ascending) or `desc` (descending).
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Repository> result = apiInstance.activityListReposStarredByAuthenticatedUser(sort, direction, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityApi#activityListReposStarredByAuthenticatedUser");
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
| **sort** | **String**| One of &#x60;created&#x60; (when the repository was starred) or &#x60;updated&#x60; (when it was last pushed to). | [optional] [default to created] [enum: created, updated] |
| **direction** | **String**| One of &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending). | [optional] [default to desc] [enum: asc, desc] |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;Repository&gt;**](Repository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.github.v3.star+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |
| **304** | Not modified |  -  |
| **401** | Requires authentication |  -  |
| **403** | Forbidden |  -  |

<a id="activityListReposStarredByUser"></a>
# **activityListReposStarredByUser**
> ActivityListReposStarredByUser200Response activityListReposStarredByUser(username, sort, direction, perPage, page)

List repositories starred by a user

Lists repositories a user has starred.  You can also find out _when_ stars were created by passing the following custom [media type](https://docs.github.com/enterprise-server@2.22/rest/overview/media-types/) via the &#x60;Accept&#x60; header:

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ActivityApi apiInstance = new ActivityApi(defaultClient);
    String username = "username_example"; // String | 
    String sort = "created"; // String | One of `created` (when the repository was starred) or `updated` (when it was last pushed to).
    String direction = "asc"; // String | One of `asc` (ascending) or `desc` (descending).
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      ActivityListReposStarredByUser200Response result = apiInstance.activityListReposStarredByUser(username, sort, direction, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityApi#activityListReposStarredByUser");
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
| **username** | **String**|  | |
| **sort** | **String**| One of &#x60;created&#x60; (when the repository was starred) or &#x60;updated&#x60; (when it was last pushed to). | [optional] [default to created] [enum: created, updated] |
| **direction** | **String**| One of &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending). | [optional] [default to desc] [enum: asc, desc] |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**ActivityListReposStarredByUser200Response**](ActivityListReposStarredByUser200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="activityListReposWatchedByUser"></a>
# **activityListReposWatchedByUser**
> List&lt;MinimalRepository&gt; activityListReposWatchedByUser(username, perPage, page)

List repositories watched by a user

Lists repositories a user is watching.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ActivityApi apiInstance = new ActivityApi(defaultClient);
    String username = "username_example"; // String | 
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<MinimalRepository> result = apiInstance.activityListReposWatchedByUser(username, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityApi#activityListReposWatchedByUser");
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
| **username** | **String**|  | |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;MinimalRepository&gt;**](MinimalRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="activityListStargazersForRepo"></a>
# **activityListStargazersForRepo**
> ActivityListStargazersForRepo200Response activityListStargazersForRepo(owner, repo, perPage, page)

List stargazers

Lists the people that have starred the repository.  You can also find out _when_ stars were created by passing the following custom [media type](https://docs.github.com/enterprise-server@2.22/rest/overview/media-types/) via the &#x60;Accept&#x60; header:

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ActivityApi apiInstance = new ActivityApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      ActivityListStargazersForRepo200Response result = apiInstance.activityListStargazersForRepo(owner, repo, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityApi#activityListStargazersForRepo");
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
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**ActivityListStargazersForRepo200Response**](ActivityListStargazersForRepo200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |
| **422** | Validation failed |  -  |

<a id="activityListWatchedReposForAuthenticatedUser"></a>
# **activityListWatchedReposForAuthenticatedUser**
> List&lt;MinimalRepository&gt; activityListWatchedReposForAuthenticatedUser(perPage, page)

List repositories watched by the authenticated user

Lists repositories the authenticated user is watching.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ActivityApi apiInstance = new ActivityApi(defaultClient);
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<MinimalRepository> result = apiInstance.activityListWatchedReposForAuthenticatedUser(perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityApi#activityListWatchedReposForAuthenticatedUser");
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
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;MinimalRepository&gt;**](MinimalRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |
| **304** | Not modified |  -  |
| **401** | Requires authentication |  -  |
| **403** | Forbidden |  -  |

<a id="activityListWatchersForRepo"></a>
# **activityListWatchersForRepo**
> List&lt;SimpleUser&gt; activityListWatchersForRepo(owner, repo, perPage, page)

List watchers

Lists the people watching the specified repository.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ActivityApi apiInstance = new ActivityApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<SimpleUser> result = apiInstance.activityListWatchersForRepo(owner, repo, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityApi#activityListWatchersForRepo");
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
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;SimpleUser&gt;**](SimpleUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="activityMarkNotificationsAsRead"></a>
# **activityMarkNotificationsAsRead**
> ActivityMarkNotificationsAsRead202Response activityMarkNotificationsAsRead(activityMarkNotificationsAsReadRequest)

Mark notifications as read

Marks all notifications as \&quot;read\&quot; removes it from the [default view on GitHub Enterprise Server](https://github.com/notifications). If the number of notifications is too large to complete in one request, you will receive a &#x60;202 Accepted&#x60; status and GitHub Enterprise Server will run an asynchronous process to mark notifications as \&quot;read.\&quot; To check whether any \&quot;unread\&quot; notifications remain, you can use the [List notifications for the authenticated user](https://docs.github.com/enterprise-server@2.22/rest/reference/activity#list-notifications-for-the-authenticated-user) endpoint and pass the query parameter &#x60;all&#x3D;false&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ActivityApi apiInstance = new ActivityApi(defaultClient);
    ActivityMarkNotificationsAsReadRequest activityMarkNotificationsAsReadRequest = new ActivityMarkNotificationsAsReadRequest(); // ActivityMarkNotificationsAsReadRequest | 
    try {
      ActivityMarkNotificationsAsRead202Response result = apiInstance.activityMarkNotificationsAsRead(activityMarkNotificationsAsReadRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityApi#activityMarkNotificationsAsRead");
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
| **activityMarkNotificationsAsReadRequest** | [**ActivityMarkNotificationsAsReadRequest**](ActivityMarkNotificationsAsReadRequest.md)|  | [optional] |

### Return type

[**ActivityMarkNotificationsAsRead202Response**](ActivityMarkNotificationsAsRead202Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Response |  -  |
| **205** | Reset Content |  -  |
| **304** | Not modified |  -  |
| **401** | Requires authentication |  -  |
| **403** | Forbidden |  -  |

<a id="activityMarkRepoNotificationsAsRead"></a>
# **activityMarkRepoNotificationsAsRead**
> EnterpriseAdminUpdateOrgName202Response activityMarkRepoNotificationsAsRead(owner, repo, activityMarkRepoNotificationsAsReadRequest)

Mark repository notifications as read

Marks all notifications in a repository as \&quot;read\&quot; removes them from the [default view on GitHub Enterprise Server](https://github.com/notifications). If the number of notifications is too large to complete in one request, you will receive a &#x60;202 Accepted&#x60; status and GitHub Enterprise Server will run an asynchronous process to mark notifications as \&quot;read.\&quot; To check whether any \&quot;unread\&quot; notifications remain, you can use the [List repository notifications for the authenticated user](https://docs.github.com/enterprise-server@2.22/rest/reference/activity#list-repository-notifications-for-the-authenticated-user) endpoint and pass the query parameter &#x60;all&#x3D;false&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ActivityApi apiInstance = new ActivityApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    ActivityMarkRepoNotificationsAsReadRequest activityMarkRepoNotificationsAsReadRequest = new ActivityMarkRepoNotificationsAsReadRequest(); // ActivityMarkRepoNotificationsAsReadRequest | 
    try {
      EnterpriseAdminUpdateOrgName202Response result = apiInstance.activityMarkRepoNotificationsAsRead(owner, repo, activityMarkRepoNotificationsAsReadRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityApi#activityMarkRepoNotificationsAsRead");
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
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **activityMarkRepoNotificationsAsReadRequest** | [**ActivityMarkRepoNotificationsAsReadRequest**](ActivityMarkRepoNotificationsAsReadRequest.md)|  | [optional] |

### Return type

[**EnterpriseAdminUpdateOrgName202Response**](EnterpriseAdminUpdateOrgName202Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Response |  -  |
| **205** | Reset Content |  -  |

<a id="activityMarkThreadAsRead"></a>
# **activityMarkThreadAsRead**
> activityMarkThreadAsRead(threadId)

Mark a thread as read



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ActivityApi apiInstance = new ActivityApi(defaultClient);
    Integer threadId = 56; // Integer | thread_id parameter
    try {
      apiInstance.activityMarkThreadAsRead(threadId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityApi#activityMarkThreadAsRead");
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
| **threadId** | **Integer**| thread_id parameter | |

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
| **205** | Reset Content |  -  |
| **304** | Not modified |  -  |
| **403** | Forbidden |  -  |

<a id="activitySetRepoSubscription"></a>
# **activitySetRepoSubscription**
> RepositorySubscription activitySetRepoSubscription(owner, repo, activitySetRepoSubscriptionRequest)

Set a repository subscription

If you would like to watch a repository, set &#x60;subscribed&#x60; to &#x60;true&#x60;. If you would like to ignore notifications made within a repository, set &#x60;ignored&#x60; to &#x60;true&#x60;. If you would like to stop watching a repository, [delete the repository&#39;s subscription](https://docs.github.com/enterprise-server@2.22/rest/reference/activity#delete-a-repository-subscription) completely.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ActivityApi apiInstance = new ActivityApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    ActivitySetRepoSubscriptionRequest activitySetRepoSubscriptionRequest = new ActivitySetRepoSubscriptionRequest(); // ActivitySetRepoSubscriptionRequest | 
    try {
      RepositorySubscription result = apiInstance.activitySetRepoSubscription(owner, repo, activitySetRepoSubscriptionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityApi#activitySetRepoSubscription");
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
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **activitySetRepoSubscriptionRequest** | [**ActivitySetRepoSubscriptionRequest**](ActivitySetRepoSubscriptionRequest.md)|  | [optional] |

### Return type

[**RepositorySubscription**](RepositorySubscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="activitySetThreadSubscription"></a>
# **activitySetThreadSubscription**
> ThreadSubscription activitySetThreadSubscription(threadId, activitySetThreadSubscriptionRequest)

Set a thread subscription

If you are watching a repository, you receive notifications for all threads by default. Use this endpoint to ignore future notifications for threads until you comment on the thread or get an **@mention**.  You can also use this endpoint to subscribe to threads that you are currently not receiving notifications for or to subscribed to threads that you have previously ignored.  Unsubscribing from a conversation in a repository that you are not watching is functionally equivalent to the [Delete a thread subscription](https://docs.github.com/enterprise-server@2.22/rest/reference/activity#delete-a-thread-subscription) endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ActivityApi apiInstance = new ActivityApi(defaultClient);
    Integer threadId = 56; // Integer | thread_id parameter
    ActivitySetThreadSubscriptionRequest activitySetThreadSubscriptionRequest = new ActivitySetThreadSubscriptionRequest(); // ActivitySetThreadSubscriptionRequest | 
    try {
      ThreadSubscription result = apiInstance.activitySetThreadSubscription(threadId, activitySetThreadSubscriptionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityApi#activitySetThreadSubscription");
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
| **threadId** | **Integer**| thread_id parameter | |
| **activitySetThreadSubscriptionRequest** | [**ActivitySetThreadSubscriptionRequest**](ActivitySetThreadSubscriptionRequest.md)|  | [optional] |

### Return type

[**ThreadSubscription**](ThreadSubscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **304** | Not modified |  -  |
| **401** | Requires authentication |  -  |
| **403** | Forbidden |  -  |

<a id="activityStarRepoForAuthenticatedUser"></a>
# **activityStarRepoForAuthenticatedUser**
> activityStarRepoForAuthenticatedUser(owner, repo)

Star a repository for the authenticated user

Note that you&#39;ll need to set &#x60;Content-Length&#x60; to zero when calling out to this endpoint. For more information, see \&quot;[HTTP verbs](https://docs.github.com/enterprise-server@2.22/rest/overview/resources-in-the-rest-api#http-verbs).\&quot;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ActivityApi apiInstance = new ActivityApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    try {
      apiInstance.activityStarRepoForAuthenticatedUser(owner, repo);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityApi#activityStarRepoForAuthenticatedUser");
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
| **owner** | **String**|  | |
| **repo** | **String**|  | |

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
| **204** | Response |  -  |
| **304** | Not modified |  -  |
| **401** | Requires authentication |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |

<a id="activityUnstarRepoForAuthenticatedUser"></a>
# **activityUnstarRepoForAuthenticatedUser**
> activityUnstarRepoForAuthenticatedUser(owner, repo)

Unstar a repository for the authenticated user



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ActivityApi apiInstance = new ActivityApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    try {
      apiInstance.activityUnstarRepoForAuthenticatedUser(owner, repo);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityApi#activityUnstarRepoForAuthenticatedUser");
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
| **owner** | **String**|  | |
| **repo** | **String**|  | |

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
| **204** | Response |  -  |
| **304** | Not modified |  -  |
| **401** | Requires authentication |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |

