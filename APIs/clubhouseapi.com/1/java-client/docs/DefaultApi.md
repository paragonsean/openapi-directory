# DefaultApi

All URIs are relative to *https://www.clubhouseapi.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**callPhoneNumberAuthPost**](DefaultApi.md#callPhoneNumberAuthPost) | **POST** /call_phone_number_auth | Call phone number auth. |
| [**checkForUpdateGet**](DefaultApi.md#checkForUpdateGet) | **GET** /check_for_update | Clubhouse uses this to check for updates when app is not installed from App Store (eg TestFlight) |
| [**checkWaitlistStatusPost**](DefaultApi.md#checkWaitlistStatusPost) | **POST** /check_waitlist_status | checks waitlist status. |
| [**completePhoneNumberAuthPost**](DefaultApi.md#completePhoneNumberAuthPost) | **POST** /complete_phone_number_auth | Call phone number auth. |
| [**createChannelPost**](DefaultApi.md#createChannelPost) | **POST** /create_channel | creates a channel |
| [**followPost**](DefaultApi.md#followPost) | **POST** /follow | follows a user |
| [**getActionableNotificationsGet**](DefaultApi.md#getActionableNotificationsGet) | **GET** /get_actionable_notifications | get actionable notifications (the bell again) |
| [**getAllTopicsGet**](DefaultApi.md#getAllTopicsGet) | **GET** /get_all_topics | gets all topics. |
| [**getChannelsGet**](DefaultApi.md#getChannelsGet) | **GET** /get_channels | get all channels |
| [**getClubPost**](DefaultApi.md#getClubPost) | **POST** /get_club | gets club by id |
| [**getClubsForTopicPost**](DefaultApi.md#getClubsForTopicPost) | **POST** /get_clubs_for_topic | looks up clubs by topic. |
| [**getCreateChannelTargetsPost**](DefaultApi.md#getCreateChannelTargetsPost) | **POST** /get_create_channel_targets | is fetched when you tap Create Room |
| [**getEventsGet**](DefaultApi.md#getEventsGet) | **GET** /get_events | the Upcoming for You page |
| [**getFollowingPost**](DefaultApi.md#getFollowingPost) | **POST** /get_following | get a list of the users and clubs that this user is following. Returned users have bios truncated to ~80 characters. |
| [**getNotificationsGet**](DefaultApi.md#getNotificationsGet) | **GET** /get_notifications | get notifications (the bell icon) |
| [**getOnlineFriendsPost**](DefaultApi.md#getOnlineFriendsPost) | **POST** /get_online_friends | gets online friends on the app homepage. |
| [**getProfilePost**](DefaultApi.md#getProfilePost) | **POST** /get_profile | looks up user profile by ID. |
| [**getReleaseNotesPost**](DefaultApi.md#getReleaseNotesPost) | **POST** /get_release_notes | gets release notes. |
| [**getSettingsGet**](DefaultApi.md#getSettingsGet) | **GET** /get_settings | get notification settings |
| [**getSuggestedClubInvitesPost**](DefaultApi.md#getSuggestedClubInvitesPost) | **POST** /get_suggested_club_invites | find users to invite to clubs based on phone number |
| [**getSuggestedFollowsAllGet**](DefaultApi.md#getSuggestedFollowsAllGet) | **GET** /get_suggested_follows_all | gets suggested follows during signup |
| [**getSuggestedFollowsFriendsOnlyPost**](DefaultApi.md#getSuggestedFollowsFriendsOnlyPost) | **POST** /get_suggested_follows_friends_only | find people to follow by uploading contacts during signup |
| [**getSuggestedFollowsSimilarPost**](DefaultApi.md#getSuggestedFollowsSimilarPost) | **POST** /get_suggested_follows_similar | find similar users. (The Sparkles button on Clubhouse&#39;s profile page) |
| [**getSuggestedInvitesPost**](DefaultApi.md#getSuggestedInvitesPost) | **POST** /get_suggested_invites | find users to invite based on phone number. |
| [**getSuggestedSpeakersPost**](DefaultApi.md#getSuggestedSpeakersPost) | **POST** /get_suggested_speakers | gets suggested users when you start a private room |
| [**getTopicPost**](DefaultApi.md#getTopicPost) | **POST** /get_topic | looks up topic by ID. |
| [**getUsersForTopicGet**](DefaultApi.md#getUsersForTopicGet) | **GET** /get_users_for_topic | looks up users by topic. |
| [**getWelcomeChannelGet**](DefaultApi.md#getWelcomeChannelGet) | **GET** /get_welcome_channel | called during signup |
| [**inviteFromWaitlistPost**](DefaultApi.md#inviteFromWaitlistPost) | **POST** /invite_from_waitlist | wave to another user on the waitlist to give them access |
| [**inviteToAppPost**](DefaultApi.md#inviteToAppPost) | **POST** /invite_to_app | invite a user to the app, using one of your invites |
| [**joinChannelPost**](DefaultApi.md#joinChannelPost) | **POST** /join_channel | join a channel. |
| [**leaveChannelPost**](DefaultApi.md#leaveChannelPost) | **POST** /leave_channel | leave a channel. |
| [**mePost**](DefaultApi.md#mePost) | **POST** /me | gets user |
| [**recordActionTrailsPost**](DefaultApi.md#recordActionTrailsPost) | **POST** /record_action_trails | analytics |
| [**refreshTokenPost**](DefaultApi.md#refreshTokenPost) | **POST** /refresh_token | gets an access_token from a refresh_token. |
| [**resendPhoneNumberAuthPost**](DefaultApi.md#resendPhoneNumberAuthPost) | **POST** /resend_phone_number_auth | Resend phone number auth. |
| [**searchClubsPost**](DefaultApi.md#searchClubsPost) | **POST** /search_clubs | search clubs. |
| [**searchUsersPost**](DefaultApi.md#searchUsersPost) | **POST** /search_users | search for users |
| [**startPhoneNumberAuthPost**](DefaultApi.md#startPhoneNumberAuthPost) | **POST** /start_phone_number_auth | Starts phone number auth. |
| [**updateNotificationsPost**](DefaultApi.md#updateNotificationsPost) | **POST** /update_notifications | updates notification during signup. |
| [**updateUsernamePost**](DefaultApi.md#updateUsernamePost) | **POST** /update_username | edits username. |


<a id="callPhoneNumberAuthPost"></a>
# **callPhoneNumberAuthPost**
> callPhoneNumberAuthPost(body)

Call phone number auth.

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
    defaultClient.setBasePath("https://www.clubhouseapi.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Object body = {}; // Object | 
    try {
      apiInstance.callPhoneNumberAuthPost(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#callPhoneNumberAuthPost");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |

<a id="checkForUpdateGet"></a>
# **checkForUpdateGet**
> checkForUpdateGet(isTestflight)

Clubhouse uses this to check for updates when app is not installed from App Store (eg TestFlight)

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
    defaultClient.setBasePath("https://www.clubhouseapi.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer isTestflight = 1; // Integer | 
    try {
      apiInstance.checkForUpdateGet(isTestflight);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#checkForUpdateGet");
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
| **isTestflight** | **Integer**|  | [optional] |

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
| **200** | successful response |  -  |

<a id="checkWaitlistStatusPost"></a>
# **checkWaitlistStatusPost**
> checkWaitlistStatusPost()

checks waitlist status.

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
    defaultClient.setBasePath("https://www.clubhouseapi.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.checkWaitlistStatusPost();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#checkWaitlistStatusPost");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | got waitlist status |  -  |
| **401** | authorization not provided |  -  |

<a id="completePhoneNumberAuthPost"></a>
# **completePhoneNumberAuthPost**
> completePhoneNumberAuthPost(body)

Call phone number auth.

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
    defaultClient.setBasePath("https://www.clubhouseapi.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Object body = {"phone_number":"+1234567890","verification_code":"1234"}; // Object | 
    try {
      apiInstance.completePhoneNumberAuthPost(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#completePhoneNumberAuthPost");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |

<a id="createChannelPost"></a>
# **createChannelPost**
> createChannelPost(body)

creates a channel

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
    defaultClient.setBasePath("https://www.clubhouseapi.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Object body = {"club_id":null,"event_id":null,"is_private":false,"is_social_mode":false,"topic":null,"user_ids":[]}; // Object | 
    try {
      apiInstance.createChannelPost(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createChannelPost");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | waitlisted |  -  |

<a id="followPost"></a>
# **followPost**
> followPost(body)

follows a user

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
    defaultClient.setBasePath("https://www.clubhouseapi.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Object body = {"user_id":1234}; // Object | 
    try {
      apiInstance.followPost(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#followPost");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **401** | waitlisted |  -  |

<a id="getActionableNotificationsGet"></a>
# **getActionableNotificationsGet**
> getActionableNotificationsGet()

get actionable notifications (the bell again)

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
    defaultClient.setBasePath("https://www.clubhouseapi.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getActionableNotificationsGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getActionableNotificationsGet");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a list of actionable notifications. |  -  |

<a id="getAllTopicsGet"></a>
# **getAllTopicsGet**
> getAllTopicsGet()

gets all topics.

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
    defaultClient.setBasePath("https://www.clubhouseapi.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getAllTopicsGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAllTopicsGet");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | a list of topics |  -  |

<a id="getChannelsGet"></a>
# **getChannelsGet**
> getChannelsGet()

get all channels

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
    defaultClient.setBasePath("https://www.clubhouseapi.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getChannelsGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getChannelsGet");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list of channels |  -  |

<a id="getClubPost"></a>
# **getClubPost**
> getClubPost(body)

gets club by id

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
    defaultClient.setBasePath("https://www.clubhouseapi.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Object body = {"club_id":1234}; // Object | 
    try {
      apiInstance.getClubPost(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getClubPost");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | returns club object |  -  |

<a id="getClubsForTopicPost"></a>
# **getClubsForTopicPost**
> getClubsForTopicPost(body)

looks up clubs by topic.

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
    defaultClient.setBasePath("https://www.clubhouseapi.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Object body = {"topic_id":140}; // Object | 
    try {
      apiInstance.getClubsForTopicPost(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getClubsForTopicPost");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | returns list of clubs with pagination |  -  |

<a id="getCreateChannelTargetsPost"></a>
# **getCreateChannelTargetsPost**
> getCreateChannelTargetsPost(body)

is fetched when you tap Create Room

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
    defaultClient.setBasePath("https://www.clubhouseapi.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Object body = {}; // Object | 
    try {
      apiInstance.getCreateChannelTargetsPost(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getCreateChannelTargetsPost");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | waitlisted |  -  |

<a id="getEventsGet"></a>
# **getEventsGet**
> getEventsGet(isFiltered, pageSize, page)

the Upcoming for You page

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
    defaultClient.setBasePath("https://www.clubhouseapi.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Boolean isFiltered = true; // Boolean | 
    Integer pageSize = 25; // Integer | 
    Integer page = 1; // Integer | 
    try {
      apiInstance.getEventsGet(isFiltered, pageSize, page);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getEventsGet");
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
| **isFiltered** | **Boolean**|  | [optional] |
| **pageSize** | **Integer**|  | [optional] |
| **page** | **Integer**|  | [optional] |

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
| **200** | a list of events |  -  |

<a id="getFollowingPost"></a>
# **getFollowingPost**
> getFollowingPost(body)

get a list of the users and clubs that this user is following. Returned users have bios truncated to ~80 characters.

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
    defaultClient.setBasePath("https://www.clubhouseapi.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Object body = {"user_id":1234}; // Object | 
    try {
      apiInstance.getFollowingPost(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getFollowingPost");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | returns list of users and clubs |  -  |

<a id="getNotificationsGet"></a>
# **getNotificationsGet**
> getNotificationsGet(pageSize, page)

get notifications (the bell icon)

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
    defaultClient.setBasePath("https://www.clubhouseapi.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer pageSize = 20; // Integer | 
    Integer page = 1; // Integer | 
    try {
      apiInstance.getNotificationsGet(pageSize, page);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getNotificationsGet");
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
| **pageSize** | **Integer**|  | [optional] |
| **page** | **Integer**|  | [optional] |

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
| **200** | Returns a list of notifications. |  -  |

<a id="getOnlineFriendsPost"></a>
# **getOnlineFriendsPost**
> getOnlineFriendsPost(body)

gets online friends on the app homepage.

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
    defaultClient.setBasePath("https://www.clubhouseapi.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Object body = {}; // Object | 
    try {
      apiInstance.getOnlineFriendsPost(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getOnlineFriendsPost");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | a list of online clubs and users. |  -  |

<a id="getProfilePost"></a>
# **getProfilePost**
> getProfilePost(body)

looks up user profile by ID.

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
    defaultClient.setBasePath("https://www.clubhouseapi.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Object body = {"user_id":4075733}; // Object | 
    try {
      apiInstance.getProfilePost(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getProfilePost");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | returns user profile info |  -  |

<a id="getReleaseNotesPost"></a>
# **getReleaseNotesPost**
> getReleaseNotesPost()

gets release notes.

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
    defaultClient.setBasePath("https://www.clubhouseapi.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getReleaseNotesPost();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getReleaseNotesPost");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the response |  -  |

<a id="getSettingsGet"></a>
# **getSettingsGet**
> getSettingsGet()

get notification settings

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
    defaultClient.setBasePath("https://www.clubhouseapi.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getSettingsGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getSettingsGet");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | notification settings |  -  |

<a id="getSuggestedClubInvitesPost"></a>
# **getSuggestedClubInvitesPost**
> getSuggestedClubInvitesPost(body)

find users to invite to clubs based on phone number

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
    defaultClient.setBasePath("https://www.clubhouseapi.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Object body = {"contacts":[{"name":"aaa","phone_number":"+11234567890"}],"upload_contacts":true}; // Object | 
    try {
      apiInstance.getSuggestedClubInvitesPost(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getSuggestedClubInvitesPost");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | returns list of suggested invites. |  -  |

<a id="getSuggestedFollowsAllGet"></a>
# **getSuggestedFollowsAllGet**
> getSuggestedFollowsAllGet(inOnboarding, pageSize, page)

gets suggested follows during signup

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
    defaultClient.setBasePath("https://www.clubhouseapi.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Boolean inOnboarding = true; // Boolean | 
    Integer pageSize = 50; // Integer | 
    Integer page = 1; // Integer | 
    try {
      apiInstance.getSuggestedFollowsAllGet(inOnboarding, pageSize, page);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getSuggestedFollowsAllGet");
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
| **inOnboarding** | **Boolean**|  | [optional] |
| **pageSize** | **Integer**|  | [optional] |
| **page** | **Integer**|  | [optional] |

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
| **200** | a list of users to follow. bios truncated to 80 chars. |  -  |

<a id="getSuggestedFollowsFriendsOnlyPost"></a>
# **getSuggestedFollowsFriendsOnlyPost**
> getSuggestedFollowsFriendsOnlyPost(body)

find people to follow by uploading contacts during signup

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
    defaultClient.setBasePath("https://www.clubhouseapi.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Object body = {"club_id":null,"contacts":[],"upload_contacts":true}; // Object | 
    try {
      apiInstance.getSuggestedFollowsFriendsOnlyPost(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getSuggestedFollowsFriendsOnlyPost");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | returns list of users and clubs |  -  |

<a id="getSuggestedFollowsSimilarPost"></a>
# **getSuggestedFollowsSimilarPost**
> getSuggestedFollowsSimilarPost(body)

find similar users. (The Sparkles button on Clubhouse&#39;s profile page)

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
    defaultClient.setBasePath("https://www.clubhouseapi.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Object body = {"user_id":4}; // Object | 
    try {
      apiInstance.getSuggestedFollowsSimilarPost(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getSuggestedFollowsSimilarPost");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a list of users. Bios truncated to 80 chars. |  -  |

<a id="getSuggestedInvitesPost"></a>
# **getSuggestedInvitesPost**
> getSuggestedInvitesPost(body)

find users to invite based on phone number.

(also see https://zerforschung.org/posts/clubhouse-telefonnummern-en/ for @zerforschung&#39;s analysis of the privacy implications of this API)

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
    defaultClient.setBasePath("https://www.clubhouseapi.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Object body = {"club_id":null,"contacts":[{"phone_number":"+11234567890"}],"upload_contacts":false}; // Object | 
    try {
      apiInstance.getSuggestedInvitesPost(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getSuggestedInvitesPost");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | returns list of users that can be invited. |  -  |

<a id="getSuggestedSpeakersPost"></a>
# **getSuggestedSpeakersPost**
> getSuggestedSpeakersPost(body)

gets suggested users when you start a private room

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
    defaultClient.setBasePath("https://www.clubhouseapi.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Object body = {"channel":null}; // Object | 
    try {
      apiInstance.getSuggestedSpeakersPost(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getSuggestedSpeakersPost");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a list of actionable notifications. |  -  |

<a id="getTopicPost"></a>
# **getTopicPost**
> getTopicPost(body)

looks up topic by ID.

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
    defaultClient.setBasePath("https://www.clubhouseapi.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Object body = {"topic_id":140}; // Object | 
    try {
      apiInstance.getTopicPost(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getTopicPost");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | returns topic info |  -  |

<a id="getUsersForTopicGet"></a>
# **getUsersForTopicGet**
> getUsersForTopicGet(topicId, pageSize, page)

looks up users by topic.

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
    defaultClient.setBasePath("https://www.clubhouseapi.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer topicId = 140; // Integer | 
    Integer pageSize = 25; // Integer | 
    Integer page = 1; // Integer | 
    try {
      apiInstance.getUsersForTopicGet(topicId, pageSize, page);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getUsersForTopicGet");
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
| **topicId** | **Integer**|  | [optional] |
| **pageSize** | **Integer**|  | [optional] |
| **page** | **Integer**|  | [optional] |

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
| **200** | returns list of users with pagination. Bios truncated to 80 chars. |  -  |

<a id="getWelcomeChannelGet"></a>
# **getWelcomeChannelGet**
> getWelcomeChannelGet()

called during signup

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
    defaultClient.setBasePath("https://www.clubhouseapi.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getWelcomeChannelGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getWelcomeChannelGet");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | empty??? |  -  |

<a id="inviteFromWaitlistPost"></a>
# **inviteFromWaitlistPost**
> inviteFromWaitlistPost(body)

wave to another user on the waitlist to give them access

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
    defaultClient.setBasePath("https://www.clubhouseapi.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Object body = {"user_id":1234}; // Object | 
    try {
      apiInstance.inviteFromWaitlistPost(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#inviteFromWaitlistPost");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | your own account is waitlisted, or some other error occurred |  -  |

<a id="inviteToAppPost"></a>
# **inviteToAppPost**
> inviteToAppPost(body)

invite a user to the app, using one of your invites

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
    defaultClient.setBasePath("https://www.clubhouseapi.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Object body = {"message":null,"name":"John Smith","phone_number":"+11234567890"}; // Object | 
    try {
      apiInstance.inviteToAppPost(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#inviteToAppPost");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | your own account doesn&#39;t have an invite either |  -  |

<a id="joinChannelPost"></a>
# **joinChannelPost**
> joinChannelPost(body)

join a channel.

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
    defaultClient.setBasePath("https://www.clubhouseapi.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Object body = {"attribution_details":"eyJpc19leHBsb3JlIjpmYWxzZSwicmFuayI6MX0=","attribution_source":"feed","channel":"abcdefgh"}; // Object | 
    try {
      apiInstance.joinChannelPost(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#joinChannelPost");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | stuff needed to actually join a channel |  -  |
| **400** | cannot join |  -  |

<a id="leaveChannelPost"></a>
# **leaveChannelPost**
> leaveChannelPost(body)

leave a channel.

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
    defaultClient.setBasePath("https://www.clubhouseapi.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Object body = {"channel":"abcdefgh"}; // Object | 
    try {
      apiInstance.leaveChannelPost(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#leaveChannelPost");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | left the channel |  -  |

<a id="mePost"></a>
# **mePost**
> mePost(body)

gets user

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
    defaultClient.setBasePath("https://www.clubhouseapi.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Object body = {"return_blocked_ids":true,"return_following_ids":true,"timezone_identifier":"America/Los_Angeles"}; // Object | 
    try {
      apiInstance.mePost(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#mePost");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the response |  -  |
| **403** | error response - happens if account is banned (is_blocked) |  -  |

<a id="recordActionTrailsPost"></a>
# **recordActionTrailsPost**
> recordActionTrailsPost(body)

analytics

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
    defaultClient.setBasePath("https://www.clubhouseapi.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Object body = {"action_trails":[{"blob_data":{},"client_time_created":1612971962,"trail_type":"app_opened"}]}; // Object | 
    try {
      apiInstance.recordActionTrailsPost(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#recordActionTrailsPost");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | always empty |  -  |

<a id="refreshTokenPost"></a>
# **refreshTokenPost**
> refreshTokenPost(body)

gets an access_token from a refresh_token.

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
    defaultClient.setBasePath("https://www.clubhouseapi.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Object body = {"refresh":"<refresh_token>"}; // Object | 
    try {
      apiInstance.refreshTokenPost(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#refreshTokenPost");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | returns new access and refresh token |  -  |
| **401** | invalid refresh token |  -  |

<a id="resendPhoneNumberAuthPost"></a>
# **resendPhoneNumberAuthPost**
> resendPhoneNumberAuthPost(body)

Resend phone number auth.

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
    defaultClient.setBasePath("https://www.clubhouseapi.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Object body = {}; // Object | 
    try {
      apiInstance.resendPhoneNumberAuthPost(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#resendPhoneNumberAuthPost");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |

<a id="searchClubsPost"></a>
# **searchClubsPost**
> searchClubsPost(body)

search clubs.

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
    defaultClient.setBasePath("https://www.clubhouseapi.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Object body = {"cofollows_only":false,"followers_only":false,"following_only":false,"query":"rohan"}; // Object | 
    try {
      apiInstance.searchClubsPost(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#searchClubsPost");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a list of clubs. |  -  |

<a id="searchUsersPost"></a>
# **searchUsersPost**
> searchUsersPost(body)

search for users

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
    defaultClient.setBasePath("https://www.clubhouseapi.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Object body = {"cofollows_only":false,"followers_only":false,"following_only":false,"query":"johnsmith"}; // Object | 
    try {
      apiInstance.searchUsersPost(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#searchUsersPost");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a list of users. |  -  |

<a id="startPhoneNumberAuthPost"></a>
# **startPhoneNumberAuthPost**
> startPhoneNumberAuthPost(body)

Starts phone number auth.

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
    defaultClient.setBasePath("https://www.clubhouseapi.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Object body = {"phone_number":"+11234567890"}; // Object | 
    try {
      apiInstance.startPhoneNumberAuthPost(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#startPhoneNumberAuthPost");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |

<a id="updateNotificationsPost"></a>
# **updateNotificationsPost**
> updateNotificationsPost(body)

updates notification during signup.

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
    defaultClient.setBasePath("https://www.clubhouseapi.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Object body = {"apn_token":null,"enable_trending":-1,"frequency":-1,"is_sandbox":false,"pause_till":-1,"system_enabled":2}; // Object | 
    try {
      apiInstance.updateNotificationsPost(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateNotificationsPost");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | waitlisted |  -  |

<a id="updateUsernamePost"></a>
# **updateUsernamePost**
> updateUsernamePost(body)

edits username.

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
    defaultClient.setBasePath("https://www.clubhouseapi.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Object body = {"username":"hipsterhouse"}; // Object | 
    try {
      apiInstance.updateUsernamePost(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateUsernamePost");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | username successfully set |  -  |
| **400** | invalid/taken username (eg empty string) |  -  |

