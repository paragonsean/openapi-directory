# openapi-java-client

PeerTube
- API version: 5.1.0
  - Build date: 2024-10-12T09:57:13.152727-04:00[America/New_York]
  - Generator version: 7.9.0

The PeerTube API is built on HTTP(S) and is RESTful. You can use your favorite
HTTP/REST library for your programming language to use PeerTube. The spec API is fully compatible with
[openapi-generator](https://github.com/OpenAPITools/openapi-generator/wiki/API-client-generator-HOWTO)
which generates a client SDK in the language of your choice - we generate some client SDKs automatically:

- [Python](https://framagit.org/framasoft/peertube/clients/python)
- [Go](https://framagit.org/framasoft/peertube/clients/go)
- [Kotlin](https://framagit.org/framasoft/peertube/clients/kotlin)

See the [REST API quick start](https://docs.joinpeertube.org/api/rest-getting-started) for a few
examples of using the PeerTube API.

# Authentication

When you sign up for an account on a PeerTube instance, you are given the possibility
to generate sessions on it, and authenticate there using an access token. Only __one
access token can currently be used at a time__.

## Roles

Accounts are given permissions based on their role. There are three roles on
PeerTube: Administrator, Moderator, and User. See the [roles guide](https://docs.joinpeertube.org/admin/managing-users#roles) for a detail of their permissions.

# Errors

The API uses standard HTTP status codes to indicate the success or failure
of the API call, completed by a [RFC7807-compliant](https://tools.ietf.org/html/rfc7807) response body.

```
HTTP 1.1 404 Not Found
Content-Type: application/problem+json; charset=utf-8

{
  \"detail\": \"Video not found\",
  \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",
  \"status\": 404,
  \"title\": \"Not Found\",
  \"type\": \"about:blank\"
}
```

We provide error `type` values for [a growing number of cases](https://github.com/Chocobozzz/PeerTube/blob/develop/shared/models/server/server-error-code.enum.ts),
but it is still optional. Types are used to disambiguate errors that bear the same status code
and are non-obvious:

```
HTTP 1.1 403 Forbidden
Content-Type: application/problem+json; charset=utf-8

{
  \"detail\": \"Cannot get this video regarding follow constraints\",
  \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",
  \"status\": 403,
  \"title\": \"Forbidden\",
  \"type\": \"https://docs.joinpeertube.org/api/rest-reference.html#section/Errors/does_not_respect_follow_constraints\"
}
```

Here a 403 error could otherwise mean that the video is private or blocklisted.

### Validation errors

Each parameter is evaluated on its own against a set of rules before the route validator
proceeds with potential testing involving parameter combinations. Errors coming from validation
errors appear earlier and benefit from a more detailed error description:

```
HTTP 1.1 400 Bad Request
Content-Type: application/problem+json; charset=utf-8

{
  \"detail\": \"Incorrect request parameters: id\",
  \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",
  \"instance\": \"/api/v1/videos/9c9de5e8-0a1e-484a-b099-e80766180\",
  \"invalid-params\": {
    \"id\": {
      \"location\": \"params\",
      \"msg\": \"Invalid value\",
      \"param\": \"id\",
      \"value\": \"9c9de5e8-0a1e-484a-b099-e80766180\"
    }
  },
  \"status\": 400,
  \"title\": \"Bad Request\",
  \"type\": \"about:blank\"
}
```

Where `id` is the name of the field concerned by the error, within the route definition.
`invalid-params.<field>.location` can be either 'params', 'body', 'header', 'query' or 'cookies', and
`invalid-params.<field>.value` reports the value that didn't pass validation whose `invalid-params.<field>.msg`
is about.

### Deprecated error fields

Some fields could be included with previous versions. They are still included but their use is deprecated:
- `error`: superseded by `detail`
- `code`: superseded by `type` (which is now an URI)

# Rate limits

We are rate-limiting all endpoints of PeerTube's API. Custom values can be set by administrators:

| Endpoint (prefix: `/api/v1`) | Calls         | Time frame   |
|------------------------------|---------------|--------------|
| `/_*`                         | 50            | 10 seconds   |
| `POST /users/token`          | 15            | 5 minutes    |
| `POST /users/register`       | 2<sup>*</sup> | 5 minutes    |
| `POST /users/ask-send-verify-email` | 3      | 5 minutes    |

Depending on the endpoint, <sup>*</sup>failed requests are not taken into account. A service
limit is announced by a `429 Too Many Requests` status code.

You can get details about the current state of your rate limit by reading the
following headers:

| Header                  | Description                                                |
|-------------------------|------------------------------------------------------------|
| `X-RateLimit-Limit`     | Number of max requests allowed in the current time period  |
| `X-RateLimit-Remaining` | Number of remaining requests in the current time period    |
| `X-RateLimit-Reset`     | Timestamp of end of current time period as UNIX timestamp  |
| `Retry-After`           | Seconds to delay after the first `429` is received         |

# CORS

This API features [Cross-Origin Resource Sharing (CORS)](https://fetch.spec.whatwg.org/),
allowing cross-domain communication from the browser for some routes:

| Endpoint                    |
|------------------------- ---|
| `/api/_*`                    |
| `/download/_*`               |
| `/lazy-static/_*`            |
| `/.well-known/webfinger`    |

In addition, all routes serving ActivityPub are CORS-enabled for all origins.


  For more information, please visit [https://joinpeertube.org](https://joinpeertube.org)

*Automatically generated by the [OpenAPI Generator](https://openapi-generator.tech)*


## Requirements

Building the API client library requires:
1. Java 1.8+
2. Maven (3.8.3+)/Gradle (7.2+)

## Installation

To install the API client library to your local Maven repository, simply execute:

```shell
mvn clean install
```

To deploy it to a remote Maven repository instead, configure the settings of the repository and execute:

```shell
mvn clean deploy
```

Refer to the [OSSRH Guide](http://central.sonatype.org/pages/ossrh-guide.html) for more information.

### Maven users

Add this dependency to your project's POM:

```xml
<dependency>
  <groupId>org.openapitools</groupId>
  <artifactId>openapi-java-client</artifactId>
  <version>5.1.0</version>
  <scope>compile</scope>
</dependency>
```

### Gradle users

Add this dependency to your project's build file:

```groovy
  repositories {
    mavenCentral()     // Needed if the 'openapi-java-client' jar has been published to maven central.
    mavenLocal()       // Needed if the 'openapi-java-client' jar has been published to the local maven repo.
  }

  dependencies {
     implementation "org.openapitools:openapi-java-client:5.1.0"
  }
```

### Others

At first generate the JAR by executing:

```shell
mvn clean package
```

Then manually install the following JARs:

* `target/openapi-java-client-5.1.0.jar`
* `target/lib/*.jar`

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Java code:

```java

// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.model.*;
import org.openapitools.client.api.AbusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AbusesApi apiInstance = new AbusesApi(defaultClient);
    Integer abuseId = 56; // Integer | Abuse id
    try {
      apiInstance.apiV1AbusesAbuseIdDelete(abuseId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AbusesApi#apiV1AbusesAbuseIdDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

## Documentation for API Endpoints

All URIs are relative to *https://peertube2.cpy.re*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AbusesApi* | [**apiV1AbusesAbuseIdDelete**](docs/AbusesApi.md#apiV1AbusesAbuseIdDelete) | **DELETE** /api/v1/abuses/{abuseId} | Delete an abuse
*AbusesApi* | [**apiV1AbusesAbuseIdMessagesAbuseMessageIdDelete**](docs/AbusesApi.md#apiV1AbusesAbuseIdMessagesAbuseMessageIdDelete) | **DELETE** /api/v1/abuses/{abuseId}/messages/{abuseMessageId} | Delete an abuse message
*AbusesApi* | [**apiV1AbusesAbuseIdMessagesGet**](docs/AbusesApi.md#apiV1AbusesAbuseIdMessagesGet) | **GET** /api/v1/abuses/{abuseId}/messages | List messages of an abuse
*AbusesApi* | [**apiV1AbusesAbuseIdMessagesPost**](docs/AbusesApi.md#apiV1AbusesAbuseIdMessagesPost) | **POST** /api/v1/abuses/{abuseId}/messages | Add message to an abuse
*AbusesApi* | [**apiV1AbusesAbuseIdPut**](docs/AbusesApi.md#apiV1AbusesAbuseIdPut) | **PUT** /api/v1/abuses/{abuseId} | Update an abuse
*AbusesApi* | [**apiV1AbusesPost**](docs/AbusesApi.md#apiV1AbusesPost) | **POST** /api/v1/abuses | Report an abuse
*AbusesApi* | [**getAbuses**](docs/AbusesApi.md#getAbuses) | **GET** /api/v1/abuses | List abuses
*AbusesApi* | [**getMyAbuses**](docs/AbusesApi.md#getMyAbuses) | **GET** /api/v1/users/me/abuses | List my abuses
*AccountBlocksApi* | [**apiV1BlocklistStatusGet**](docs/AccountBlocksApi.md#apiV1BlocklistStatusGet) | **GET** /api/v1/blocklist/status | Get block status of accounts/hosts
*AccountBlocksApi* | [**apiV1ServerBlocklistAccountsAccountNameDelete**](docs/AccountBlocksApi.md#apiV1ServerBlocklistAccountsAccountNameDelete) | **DELETE** /api/v1/server/blocklist/accounts/{accountName} | Unblock an account by its handle
*AccountBlocksApi* | [**apiV1ServerBlocklistAccountsGet**](docs/AccountBlocksApi.md#apiV1ServerBlocklistAccountsGet) | **GET** /api/v1/server/blocklist/accounts | List account blocks
*AccountBlocksApi* | [**apiV1ServerBlocklistAccountsPost**](docs/AccountBlocksApi.md#apiV1ServerBlocklistAccountsPost) | **POST** /api/v1/server/blocklist/accounts | Block an account
*AccountsApi* | [**apiV1AccountsNameRatingsGet**](docs/AccountsApi.md#apiV1AccountsNameRatingsGet) | **GET** /api/v1/accounts/{name}/ratings | List ratings of an account
*AccountsApi* | [**apiV1AccountsNameVideoChannelSyncsGet_1**](docs/AccountsApi.md#apiV1AccountsNameVideoChannelSyncsGet_1) | **GET** /api/v1/accounts/{name}/video-channel-syncs | List the synchronizations of video channels of an account
*AccountsApi* | [**apiV1AccountsNameVideoChannelsGet_0**](docs/AccountsApi.md#apiV1AccountsNameVideoChannelsGet_0) | **GET** /api/v1/accounts/{name}/video-channels | List video channels of an account
*AccountsApi* | [**apiV1AccountsNameVideoPlaylistsGet_0**](docs/AccountsApi.md#apiV1AccountsNameVideoPlaylistsGet_0) | **GET** /api/v1/accounts/{name}/video-playlists | List playlists of an account
*AccountsApi* | [**getAccount**](docs/AccountsApi.md#getAccount) | **GET** /api/v1/accounts/{name} | Get an account
*AccountsApi* | [**getAccountFollowers**](docs/AccountsApi.md#getAccountFollowers) | **GET** /api/v1/accounts/{name}/followers | List followers of an account
*AccountsApi* | [**getAccountVideos**](docs/AccountsApi.md#getAccountVideos) | **GET** /api/v1/accounts/{name}/videos | List videos of an account
*AccountsApi* | [**getAccounts**](docs/AccountsApi.md#getAccounts) | **GET** /api/v1/accounts | List accounts
*ChannelsSyncApi* | [**addVideoChannelSync**](docs/ChannelsSyncApi.md#addVideoChannelSync) | **POST** /api/v1/video-channel-syncs | Create a synchronization for a video channel
*ChannelsSyncApi* | [**apiV1AccountsNameVideoChannelSyncsGet_0**](docs/ChannelsSyncApi.md#apiV1AccountsNameVideoChannelSyncsGet_0) | **GET** /api/v1/accounts/{name}/video-channel-syncs | List the synchronizations of video channels of an account
*ChannelsSyncApi* | [**apiV1VideoChannelsChannelHandleImportVideosPost_0**](docs/ChannelsSyncApi.md#apiV1VideoChannelsChannelHandleImportVideosPost_0) | **POST** /api/v1/video-channels/{channelHandle}/import-videos | Import videos in channel
*ChannelsSyncApi* | [**delVideoChannelSync**](docs/ChannelsSyncApi.md#delVideoChannelSync) | **DELETE** /api/v1/video-channel-syncs/{channelSyncId} | Delete a video channel synchronization
*ChannelsSyncApi* | [**triggerVideoChannelSync**](docs/ChannelsSyncApi.md#triggerVideoChannelSync) | **POST** /api/v1/video-channel-syncs/{channelSyncId}/sync | Triggers the channel synchronization job, fetching all the videos from the remote channel
*ConfigApi* | [**delCustomConfig**](docs/ConfigApi.md#delCustomConfig) | **DELETE** /api/v1/config/custom | Delete instance runtime configuration
*ConfigApi* | [**getAbout**](docs/ConfigApi.md#getAbout) | **GET** /api/v1/config/about | Get instance \&quot;About\&quot; information
*ConfigApi* | [**getConfig**](docs/ConfigApi.md#getConfig) | **GET** /api/v1/config | Get instance public configuration
*ConfigApi* | [**getCustomConfig**](docs/ConfigApi.md#getCustomConfig) | **GET** /api/v1/config/custom | Get instance runtime configuration
*ConfigApi* | [**putCustomConfig**](docs/ConfigApi.md#putCustomConfig) | **PUT** /api/v1/config/custom | Set instance runtime configuration
*HomepageApi* | [**apiV1CustomPagesHomepageInstanceGet**](docs/HomepageApi.md#apiV1CustomPagesHomepageInstanceGet) | **GET** /api/v1/custom-pages/homepage/instance | Get instance custom homepage
*HomepageApi* | [**apiV1CustomPagesHomepageInstancePut**](docs/HomepageApi.md#apiV1CustomPagesHomepageInstancePut) | **PUT** /api/v1/custom-pages/homepage/instance | Set instance custom homepage
*InstanceFollowsApi* | [**apiV1ServerFollowersGet**](docs/InstanceFollowsApi.md#apiV1ServerFollowersGet) | **GET** /api/v1/server/followers | List instances following the server
*InstanceFollowsApi* | [**apiV1ServerFollowersNameWithHostAcceptPost**](docs/InstanceFollowsApi.md#apiV1ServerFollowersNameWithHostAcceptPost) | **POST** /api/v1/server/followers/{nameWithHost}/accept | Accept a pending follower to your server
*InstanceFollowsApi* | [**apiV1ServerFollowersNameWithHostDelete**](docs/InstanceFollowsApi.md#apiV1ServerFollowersNameWithHostDelete) | **DELETE** /api/v1/server/followers/{nameWithHost} | Remove or reject a follower to your server
*InstanceFollowsApi* | [**apiV1ServerFollowersNameWithHostRejectPost**](docs/InstanceFollowsApi.md#apiV1ServerFollowersNameWithHostRejectPost) | **POST** /api/v1/server/followers/{nameWithHost}/reject | Reject a pending follower to your server
*InstanceFollowsApi* | [**apiV1ServerFollowingGet**](docs/InstanceFollowsApi.md#apiV1ServerFollowingGet) | **GET** /api/v1/server/following | List instances followed by the server
*InstanceFollowsApi* | [**apiV1ServerFollowingHostOrHandleDelete**](docs/InstanceFollowsApi.md#apiV1ServerFollowingHostOrHandleDelete) | **DELETE** /api/v1/server/following/{hostOrHandle} | Unfollow an actor (PeerTube instance, channel or account)
*InstanceFollowsApi* | [**apiV1ServerFollowingPost**](docs/InstanceFollowsApi.md#apiV1ServerFollowingPost) | **POST** /api/v1/server/following | Follow a list of actors (PeerTube instance, channel or account)
*InstanceRedundancyApi* | [**apiV1ServerRedundancyHostPut**](docs/InstanceRedundancyApi.md#apiV1ServerRedundancyHostPut) | **PUT** /api/v1/server/redundancy/{host} | Update a server redundancy policy
*JobApi* | [**apiV1JobsPausePost**](docs/JobApi.md#apiV1JobsPausePost) | **POST** /api/v1/jobs/pause | Pause job queue
*JobApi* | [**apiV1JobsResumePost**](docs/JobApi.md#apiV1JobsResumePost) | **POST** /api/v1/jobs/resume | Resume job queue
*JobApi* | [**getJobs**](docs/JobApi.md#getJobs) | **GET** /api/v1/jobs/{state} | List instance jobs
*LiveVideosApi* | [**addLive**](docs/LiveVideosApi.md#addLive) | **POST** /api/v1/videos/live | Create a live
*LiveVideosApi* | [**apiV1VideosIdLiveSessionGet**](docs/LiveVideosApi.md#apiV1VideosIdLiveSessionGet) | **GET** /api/v1/videos/{id}/live-session | Get live session of a replay
*LiveVideosApi* | [**apiV1VideosLiveIdSessionsGet**](docs/LiveVideosApi.md#apiV1VideosLiveIdSessionsGet) | **GET** /api/v1/videos/live/{id}/sessions | List live sessions
*LiveVideosApi* | [**getLiveId**](docs/LiveVideosApi.md#getLiveId) | **GET** /api/v1/videos/live/{id} | Get information about a live
*LiveVideosApi* | [**updateLiveId**](docs/LiveVideosApi.md#updateLiveId) | **PUT** /api/v1/videos/live/{id} | Update information about a live
*LogsApi* | [**getInstanceAuditLogs**](docs/LogsApi.md#getInstanceAuditLogs) | **GET** /api/v1/server/audit-logs | Get instance audit logs
*LogsApi* | [**getInstanceLogs**](docs/LogsApi.md#getInstanceLogs) | **GET** /api/v1/server/logs | Get instance logs
*LogsApi* | [**sendClientLog**](docs/LogsApi.md#sendClientLog) | **POST** /api/v1/server/logs/client | Send client log
*MyHistoryApi* | [**apiV1UsersMeHistoryVideosGet**](docs/MyHistoryApi.md#apiV1UsersMeHistoryVideosGet) | **GET** /api/v1/users/me/history/videos | List watched videos history
*MyHistoryApi* | [**apiV1UsersMeHistoryVideosRemovePost**](docs/MyHistoryApi.md#apiV1UsersMeHistoryVideosRemovePost) | **POST** /api/v1/users/me/history/videos/remove | Clear video history
*MyHistoryApi* | [**apiV1UsersMeHistoryVideosVideoIdDelete**](docs/MyHistoryApi.md#apiV1UsersMeHistoryVideosVideoIdDelete) | **DELETE** /api/v1/users/me/history/videos/{videoId} | Delete history element
*MyNotificationsApi* | [**apiV1UsersMeNotificationSettingsPut**](docs/MyNotificationsApi.md#apiV1UsersMeNotificationSettingsPut) | **PUT** /api/v1/users/me/notification-settings | Update my notification settings
*MyNotificationsApi* | [**apiV1UsersMeNotificationsGet**](docs/MyNotificationsApi.md#apiV1UsersMeNotificationsGet) | **GET** /api/v1/users/me/notifications | List my notifications
*MyNotificationsApi* | [**apiV1UsersMeNotificationsReadAllPost**](docs/MyNotificationsApi.md#apiV1UsersMeNotificationsReadAllPost) | **POST** /api/v1/users/me/notifications/read-all | Mark all my notification as read
*MyNotificationsApi* | [**apiV1UsersMeNotificationsReadPost**](docs/MyNotificationsApi.md#apiV1UsersMeNotificationsReadPost) | **POST** /api/v1/users/me/notifications/read | Mark notifications as read by their id
*MySubscriptionsApi* | [**apiV1UsersMeSubscriptionsExistGet**](docs/MySubscriptionsApi.md#apiV1UsersMeSubscriptionsExistGet) | **GET** /api/v1/users/me/subscriptions/exist | Get if subscriptions exist for my user
*MySubscriptionsApi* | [**apiV1UsersMeSubscriptionsGet**](docs/MySubscriptionsApi.md#apiV1UsersMeSubscriptionsGet) | **GET** /api/v1/users/me/subscriptions | Get my user subscriptions
*MySubscriptionsApi* | [**apiV1UsersMeSubscriptionsPost**](docs/MySubscriptionsApi.md#apiV1UsersMeSubscriptionsPost) | **POST** /api/v1/users/me/subscriptions | Add subscription to my user
*MySubscriptionsApi* | [**apiV1UsersMeSubscriptionsSubscriptionHandleDelete**](docs/MySubscriptionsApi.md#apiV1UsersMeSubscriptionsSubscriptionHandleDelete) | **DELETE** /api/v1/users/me/subscriptions/{subscriptionHandle} | Delete subscription of my user
*MySubscriptionsApi* | [**apiV1UsersMeSubscriptionsSubscriptionHandleGet**](docs/MySubscriptionsApi.md#apiV1UsersMeSubscriptionsSubscriptionHandleGet) | **GET** /api/v1/users/me/subscriptions/{subscriptionHandle} | Get subscription of my user
*MySubscriptionsApi* | [**apiV1UsersMeSubscriptionsVideosGet**](docs/MySubscriptionsApi.md#apiV1UsersMeSubscriptionsVideosGet) | **GET** /api/v1/users/me/subscriptions/videos | List videos of subscriptions of my user
*MyUserApi* | [**apiV1UsersMeAvatarDelete**](docs/MyUserApi.md#apiV1UsersMeAvatarDelete) | **DELETE** /api/v1/users/me/avatar | Delete my avatar
*MyUserApi* | [**apiV1UsersMeAvatarPickPost**](docs/MyUserApi.md#apiV1UsersMeAvatarPickPost) | **POST** /api/v1/users/me/avatar/pick | Update my user avatar
*MyUserApi* | [**apiV1UsersMeVideoQuotaUsedGet**](docs/MyUserApi.md#apiV1UsersMeVideoQuotaUsedGet) | **GET** /api/v1/users/me/video-quota-used | Get my user used quota
*MyUserApi* | [**apiV1UsersMeVideosGet**](docs/MyUserApi.md#apiV1UsersMeVideosGet) | **GET** /api/v1/users/me/videos | Get videos of my user
*MyUserApi* | [**apiV1UsersMeVideosImportsGet_0**](docs/MyUserApi.md#apiV1UsersMeVideosImportsGet_0) | **GET** /api/v1/users/me/videos/imports | Get video imports of my user
*MyUserApi* | [**apiV1UsersMeVideosVideoIdRatingGet**](docs/MyUserApi.md#apiV1UsersMeVideosVideoIdRatingGet) | **GET** /api/v1/users/me/videos/{videoId}/rating | Get rate of my user for a video
*MyUserApi* | [**getMyAbuses_0**](docs/MyUserApi.md#getMyAbuses_0) | **GET** /api/v1/users/me/abuses | List my abuses
*MyUserApi* | [**getUserInfo**](docs/MyUserApi.md#getUserInfo) | **GET** /api/v1/users/me | Get my user information
*MyUserApi* | [**putUserInfo**](docs/MyUserApi.md#putUserInfo) | **PUT** /api/v1/users/me | Update my user information
*PluginsApi* | [**addPlugin**](docs/PluginsApi.md#addPlugin) | **POST** /api/v1/plugins/install | Install a plugin
*PluginsApi* | [**apiV1PluginsNpmNamePublicSettingsGet**](docs/PluginsApi.md#apiV1PluginsNpmNamePublicSettingsGet) | **GET** /api/v1/plugins/{npmName}/public-settings | Get a plugin&#39;s public settings
*PluginsApi* | [**apiV1PluginsNpmNameRegisteredSettingsGet**](docs/PluginsApi.md#apiV1PluginsNpmNameRegisteredSettingsGet) | **GET** /api/v1/plugins/{npmName}/registered-settings | Get a plugin&#39;s registered settings
*PluginsApi* | [**apiV1PluginsNpmNameSettingsPut**](docs/PluginsApi.md#apiV1PluginsNpmNameSettingsPut) | **PUT** /api/v1/plugins/{npmName}/settings | Set a plugin&#39;s settings
*PluginsApi* | [**getAvailablePlugins**](docs/PluginsApi.md#getAvailablePlugins) | **GET** /api/v1/plugins/available | List available plugins
*PluginsApi* | [**getPlugin**](docs/PluginsApi.md#getPlugin) | **GET** /api/v1/plugins/{npmName} | Get a plugin
*PluginsApi* | [**getPlugins**](docs/PluginsApi.md#getPlugins) | **GET** /api/v1/plugins | List plugins
*PluginsApi* | [**uninstallPlugin**](docs/PluginsApi.md#uninstallPlugin) | **POST** /api/v1/plugins/uninstall | Uninstall a plugin
*PluginsApi* | [**updatePlugin**](docs/PluginsApi.md#updatePlugin) | **POST** /api/v1/plugins/update | Update a plugin
*RegisterApi* | [**acceptRegistration**](docs/RegisterApi.md#acceptRegistration) | **POST** /api/v1/users/registrations/{registrationId}/accept | Accept registration
*RegisterApi* | [**deleteRegistration**](docs/RegisterApi.md#deleteRegistration) | **DELETE** /api/v1/users/registrations/{registrationId} | Delete registration
*RegisterApi* | [**listRegistrations**](docs/RegisterApi.md#listRegistrations) | **GET** /api/v1/users/registrations | List registrations
*RegisterApi* | [**registerUser**](docs/RegisterApi.md#registerUser) | **POST** /api/v1/users/register | Register a user
*RegisterApi* | [**rejectRegistration**](docs/RegisterApi.md#rejectRegistration) | **POST** /api/v1/users/registrations/{registrationId}/reject | Reject registration
*RegisterApi* | [**requestRegistration**](docs/RegisterApi.md#requestRegistration) | **POST** /api/v1/users/registrations/request | Request registration
*RegisterApi* | [**resendEmailToVerifyRegistration**](docs/RegisterApi.md#resendEmailToVerifyRegistration) | **POST** /api/v1/users/registrations/ask-send-verify-email | Resend verification link to registration email
*RegisterApi* | [**resendEmailToVerifyUser_0**](docs/RegisterApi.md#resendEmailToVerifyUser_0) | **POST** /api/v1/users/ask-send-verify-email | Resend user verification link
*RegisterApi* | [**verifyRegistrationEmail**](docs/RegisterApi.md#verifyRegistrationEmail) | **POST** /api/v1/users/registrations/{registrationId}/verify-email | Verify a registration email
*RegisterApi* | [**verifyUser_0**](docs/RegisterApi.md#verifyUser_0) | **POST** /api/v1/users/{id}/verify-email | Verify a user
*SearchApi* | [**searchChannels**](docs/SearchApi.md#searchChannels) | **GET** /api/v1/search/video-channels | Search channels
*SearchApi* | [**searchPlaylists**](docs/SearchApi.md#searchPlaylists) | **GET** /api/v1/search/video-playlists | Search playlists
*SearchApi* | [**searchVideos**](docs/SearchApi.md#searchVideos) | **GET** /api/v1/search/videos | Search videos
*ServerBlocksApi* | [**apiV1BlocklistStatusGet_0**](docs/ServerBlocksApi.md#apiV1BlocklistStatusGet_0) | **GET** /api/v1/blocklist/status | Get block status of accounts/hosts
*ServerBlocksApi* | [**apiV1ServerBlocklistServersGet**](docs/ServerBlocksApi.md#apiV1ServerBlocklistServersGet) | **GET** /api/v1/server/blocklist/servers | List server blocks
*ServerBlocksApi* | [**apiV1ServerBlocklistServersHostDelete**](docs/ServerBlocksApi.md#apiV1ServerBlocklistServersHostDelete) | **DELETE** /api/v1/server/blocklist/servers/{host} | Unblock a server by its domain
*ServerBlocksApi* | [**apiV1ServerBlocklistServersPost**](docs/ServerBlocksApi.md#apiV1ServerBlocklistServersPost) | **POST** /api/v1/server/blocklist/servers | Block a server
*SessionApi* | [**getOAuthClient**](docs/SessionApi.md#getOAuthClient) | **GET** /api/v1/oauth-clients/local | Login prerequisite
*SessionApi* | [**getOAuthToken**](docs/SessionApi.md#getOAuthToken) | **POST** /api/v1/users/token | Login
*SessionApi* | [**revokeOAuthToken**](docs/SessionApi.md#revokeOAuthToken) | **POST** /api/v1/users/revoke-token | Logout
*StaticVideoFilesApi* | [**staticStreamingPlaylistsHlsFilenameGet**](docs/StaticVideoFilesApi.md#staticStreamingPlaylistsHlsFilenameGet) | **GET** /static/streaming-playlists/hls/{filename} | Get public HLS video file
*StaticVideoFilesApi* | [**staticStreamingPlaylistsHlsPrivateFilenameGet**](docs/StaticVideoFilesApi.md#staticStreamingPlaylistsHlsPrivateFilenameGet) | **GET** /static/streaming-playlists/hls/private/{filename} | Get private HLS video file
*StaticVideoFilesApi* | [**staticWebseedFilenameGet**](docs/StaticVideoFilesApi.md#staticWebseedFilenameGet) | **GET** /static/webseed/{filename} | Get public WebTorrent video file
*StaticVideoFilesApi* | [**staticWebseedPrivateFilenameGet**](docs/StaticVideoFilesApi.md#staticWebseedPrivateFilenameGet) | **GET** /static/webseed/private/{filename} | Get private WebTorrent video file
*StatsApi* | [**apiV1MetricsPlaybackPost**](docs/StatsApi.md#apiV1MetricsPlaybackPost) | **POST** /api/v1/metrics/playback | Create playback metrics
*StatsApi* | [**getInstanceStats**](docs/StatsApi.md#getInstanceStats) | **GET** /api/v1/server/stats | Get instance stats
*UsersApi* | [**addUser**](docs/UsersApi.md#addUser) | **POST** /api/v1/users | Create a user
*UsersApi* | [**confirmTwoFactorRequest**](docs/UsersApi.md#confirmTwoFactorRequest) | **POST** /api/v1/users/{id}/two-factor/confirm-request | Confirm two factor auth
*UsersApi* | [**delUser**](docs/UsersApi.md#delUser) | **DELETE** /api/v1/users/{id} | Delete a user
*UsersApi* | [**disableTwoFactor**](docs/UsersApi.md#disableTwoFactor) | **POST** /api/v1/users/{id}/two-factor/disable | Disable two factor auth
*UsersApi* | [**getUser**](docs/UsersApi.md#getUser) | **GET** /api/v1/users/{id} | Get a user
*UsersApi* | [**getUsers**](docs/UsersApi.md#getUsers) | **GET** /api/v1/users | List users
*UsersApi* | [**putUser**](docs/UsersApi.md#putUser) | **PUT** /api/v1/users/{id} | Update a user
*UsersApi* | [**requestTwoFactor**](docs/UsersApi.md#requestTwoFactor) | **POST** /api/v1/users/{id}/two-factor/request | Request two factor auth
*UsersApi* | [**resendEmailToVerifyUser**](docs/UsersApi.md#resendEmailToVerifyUser) | **POST** /api/v1/users/ask-send-verify-email | Resend user verification link
*UsersApi* | [**verifyUser**](docs/UsersApi.md#verifyUser) | **POST** /api/v1/users/{id}/verify-email | Verify a user
*VideoApi* | [**addLive_0**](docs/VideoApi.md#addLive_0) | **POST** /api/v1/videos/live | Create a live
*VideoApi* | [**addView**](docs/VideoApi.md#addView) | **POST** /api/v1/videos/{id}/views | Notify user is watching a video
*VideoApi* | [**apiV1VideosIdStudioEditPost_0**](docs/VideoApi.md#apiV1VideosIdStudioEditPost_0) | **POST** /api/v1/videos/{id}/studio/edit | Create a studio task
*VideoApi* | [**apiV1VideosIdWatchingPut**](docs/VideoApi.md#apiV1VideosIdWatchingPut) | **PUT** /api/v1/videos/{id}/watching | Set watching progress of a video
*VideoApi* | [**delVideo**](docs/VideoApi.md#delVideo) | **DELETE** /api/v1/videos/{id} | Delete a video
*VideoApi* | [**getAccountVideos_0**](docs/VideoApi.md#getAccountVideos_0) | **GET** /api/v1/accounts/{name}/videos | List videos of an account
*VideoApi* | [**getCategories**](docs/VideoApi.md#getCategories) | **GET** /api/v1/videos/categories | List available video categories
*VideoApi* | [**getLanguages**](docs/VideoApi.md#getLanguages) | **GET** /api/v1/videos/languages | List available video languages
*VideoApi* | [**getLicences**](docs/VideoApi.md#getLicences) | **GET** /api/v1/videos/licences | List available video licences
*VideoApi* | [**getLiveId_0**](docs/VideoApi.md#getLiveId_0) | **GET** /api/v1/videos/live/{id} | Get information about a live
*VideoApi* | [**getVideo**](docs/VideoApi.md#getVideo) | **GET** /api/v1/videos/{id} | Get a video
*VideoApi* | [**getVideoChannelVideos**](docs/VideoApi.md#getVideoChannelVideos) | **GET** /api/v1/video-channels/{channelHandle}/videos | List videos of a video channel
*VideoApi* | [**getVideoDesc**](docs/VideoApi.md#getVideoDesc) | **GET** /api/v1/videos/{id}/description | Get complete video description
*VideoApi* | [**getVideoPrivacyPolicies**](docs/VideoApi.md#getVideoPrivacyPolicies) | **GET** /api/v1/videos/privacies | List available video privacy policies
*VideoApi* | [**getVideoSource**](docs/VideoApi.md#getVideoSource) | **POST** /api/v1/videos/{id}/source | Get video source file metadata
*VideoApi* | [**getVideos**](docs/VideoApi.md#getVideos) | **GET** /api/v1/videos | List videos
*VideoApi* | [**putVideo**](docs/VideoApi.md#putVideo) | **PUT** /api/v1/videos/{id} | Update a video
*VideoApi* | [**requestVideoToken**](docs/VideoApi.md#requestVideoToken) | **POST** /api/v1/videos/{id}/token | Request video token
*VideoApi* | [**updateLiveId_0**](docs/VideoApi.md#updateLiveId_0) | **PUT** /api/v1/videos/live/{id} | Update information about a live
*VideoApi* | [**uploadLegacy**](docs/VideoApi.md#uploadLegacy) | **POST** /api/v1/videos/upload | Upload a video
*VideoApi* | [**uploadResumable**](docs/VideoApi.md#uploadResumable) | **PUT** /api/v1/videos/upload-resumable | Send chunk for the resumable upload of a video
*VideoApi* | [**uploadResumableCancel**](docs/VideoApi.md#uploadResumableCancel) | **DELETE** /api/v1/videos/upload-resumable | Cancel the resumable upload of a video, deleting any data uploaded so far
*VideoApi* | [**uploadResumableInit**](docs/VideoApi.md#uploadResumableInit) | **POST** /api/v1/videos/upload-resumable | Initialize the resumable upload of a video
*VideoBlocksApi* | [**addVideoBlock**](docs/VideoBlocksApi.md#addVideoBlock) | **POST** /api/v1/videos/{id}/blacklist | Block a video
*VideoBlocksApi* | [**delVideoBlock**](docs/VideoBlocksApi.md#delVideoBlock) | **DELETE** /api/v1/videos/{id}/blacklist | Unblock a video by its id
*VideoBlocksApi* | [**getVideoBlocks**](docs/VideoBlocksApi.md#getVideoBlocks) | **GET** /api/v1/videos/blacklist | List video blocks
*VideoCaptionsApi* | [**addVideoCaption**](docs/VideoCaptionsApi.md#addVideoCaption) | **PUT** /api/v1/videos/{id}/captions/{captionLanguage} | Add or replace a video caption
*VideoCaptionsApi* | [**delVideoCaption**](docs/VideoCaptionsApi.md#delVideoCaption) | **DELETE** /api/v1/videos/{id}/captions/{captionLanguage} | Delete a video caption
*VideoCaptionsApi* | [**getVideoCaptions**](docs/VideoCaptionsApi.md#getVideoCaptions) | **GET** /api/v1/videos/{id}/captions | List captions of a video
*VideoChannelsApi* | [**addVideoChannel**](docs/VideoChannelsApi.md#addVideoChannel) | **POST** /api/v1/video-channels | Create a video channel
*VideoChannelsApi* | [**apiV1AccountsNameVideoChannelSyncsGet**](docs/VideoChannelsApi.md#apiV1AccountsNameVideoChannelSyncsGet) | **GET** /api/v1/accounts/{name}/video-channel-syncs | List the synchronizations of video channels of an account
*VideoChannelsApi* | [**apiV1AccountsNameVideoChannelsGet**](docs/VideoChannelsApi.md#apiV1AccountsNameVideoChannelsGet) | **GET** /api/v1/accounts/{name}/video-channels | List video channels of an account
*VideoChannelsApi* | [**apiV1VideoChannelsChannelHandleAvatarDelete**](docs/VideoChannelsApi.md#apiV1VideoChannelsChannelHandleAvatarDelete) | **DELETE** /api/v1/video-channels/{channelHandle}/avatar | Delete channel avatar
*VideoChannelsApi* | [**apiV1VideoChannelsChannelHandleAvatarPickPost**](docs/VideoChannelsApi.md#apiV1VideoChannelsChannelHandleAvatarPickPost) | **POST** /api/v1/video-channels/{channelHandle}/avatar/pick | Update channel avatar
*VideoChannelsApi* | [**apiV1VideoChannelsChannelHandleBannerDelete**](docs/VideoChannelsApi.md#apiV1VideoChannelsChannelHandleBannerDelete) | **DELETE** /api/v1/video-channels/{channelHandle}/banner | Delete channel banner
*VideoChannelsApi* | [**apiV1VideoChannelsChannelHandleBannerPickPost**](docs/VideoChannelsApi.md#apiV1VideoChannelsChannelHandleBannerPickPost) | **POST** /api/v1/video-channels/{channelHandle}/banner/pick | Update channel banner
*VideoChannelsApi* | [**apiV1VideoChannelsChannelHandleImportVideosPost**](docs/VideoChannelsApi.md#apiV1VideoChannelsChannelHandleImportVideosPost) | **POST** /api/v1/video-channels/{channelHandle}/import-videos | Import videos in channel
*VideoChannelsApi* | [**apiV1VideoChannelsChannelHandleVideoPlaylistsGet_0**](docs/VideoChannelsApi.md#apiV1VideoChannelsChannelHandleVideoPlaylistsGet_0) | **GET** /api/v1/video-channels/{channelHandle}/video-playlists | List playlists of a channel
*VideoChannelsApi* | [**delVideoChannel**](docs/VideoChannelsApi.md#delVideoChannel) | **DELETE** /api/v1/video-channels/{channelHandle} | Delete a video channel
*VideoChannelsApi* | [**getVideoChannel**](docs/VideoChannelsApi.md#getVideoChannel) | **GET** /api/v1/video-channels/{channelHandle} | Get a video channel
*VideoChannelsApi* | [**getVideoChannelFollowers**](docs/VideoChannelsApi.md#getVideoChannelFollowers) | **GET** /api/v1/video-channels/{channelHandle}/followers | List followers of a video channel
*VideoChannelsApi* | [**getVideoChannelVideos_0**](docs/VideoChannelsApi.md#getVideoChannelVideos_0) | **GET** /api/v1/video-channels/{channelHandle}/videos | List videos of a video channel
*VideoChannelsApi* | [**getVideoChannels**](docs/VideoChannelsApi.md#getVideoChannels) | **GET** /api/v1/video-channels | List video channels
*VideoChannelsApi* | [**putVideoChannel**](docs/VideoChannelsApi.md#putVideoChannel) | **PUT** /api/v1/video-channels/{channelHandle} | Update a video channel
*VideoCommentsApi* | [**apiV1VideosIdCommentThreadsGet**](docs/VideoCommentsApi.md#apiV1VideosIdCommentThreadsGet) | **GET** /api/v1/videos/{id}/comment-threads | List threads of a video
*VideoCommentsApi* | [**apiV1VideosIdCommentThreadsPost**](docs/VideoCommentsApi.md#apiV1VideosIdCommentThreadsPost) | **POST** /api/v1/videos/{id}/comment-threads | Create a thread
*VideoCommentsApi* | [**apiV1VideosIdCommentThreadsThreadIdGet**](docs/VideoCommentsApi.md#apiV1VideosIdCommentThreadsThreadIdGet) | **GET** /api/v1/videos/{id}/comment-threads/{threadId} | Get a thread
*VideoCommentsApi* | [**apiV1VideosIdCommentsCommentIdDelete**](docs/VideoCommentsApi.md#apiV1VideosIdCommentsCommentIdDelete) | **DELETE** /api/v1/videos/{id}/comments/{commentId} | Delete a comment or a reply
*VideoCommentsApi* | [**apiV1VideosIdCommentsCommentIdPost**](docs/VideoCommentsApi.md#apiV1VideosIdCommentsCommentIdPost) | **POST** /api/v1/videos/{id}/comments/{commentId} | Reply to a thread of a video
*VideoFeedsApi* | [**getSyndicatedComments**](docs/VideoFeedsApi.md#getSyndicatedComments) | **GET** /feeds/video-comments.{format} | List comments on videos
*VideoFeedsApi* | [**getSyndicatedSubscriptionVideos**](docs/VideoFeedsApi.md#getSyndicatedSubscriptionVideos) | **GET** /feeds/subscriptions.{format} | List videos of subscriptions tied to a token
*VideoFeedsApi* | [**getSyndicatedVideos**](docs/VideoFeedsApi.md#getSyndicatedVideos) | **GET** /feeds/videos.{format} | List videos
*VideoFilesApi* | [**delVideoHLS**](docs/VideoFilesApi.md#delVideoHLS) | **DELETE** /api/v1/videos/{id}/hls | Delete video HLS files
*VideoFilesApi* | [**delVideoWebTorrent**](docs/VideoFilesApi.md#delVideoWebTorrent) | **DELETE** /api/v1/videos/{id}/webtorrent | Delete video WebTorrent files
*VideoImportsApi* | [**apiV1VideosImportsIdCancelPost**](docs/VideoImportsApi.md#apiV1VideosImportsIdCancelPost) | **POST** /api/v1/videos/imports/{id}/cancel | Cancel video import
*VideoImportsApi* | [**apiV1VideosImportsIdDelete**](docs/VideoImportsApi.md#apiV1VideosImportsIdDelete) | **DELETE** /api/v1/videos/imports/{id} | Delete video import
*VideoImportsApi* | [**importVideo**](docs/VideoImportsApi.md#importVideo) | **POST** /api/v1/videos/imports | Import a video
*VideoMirroringApi* | [**delMirroredVideo**](docs/VideoMirroringApi.md#delMirroredVideo) | **DELETE** /api/v1/server/redundancy/videos/{redundancyId} | Delete a mirror done on a video
*VideoMirroringApi* | [**getMirroredVideos**](docs/VideoMirroringApi.md#getMirroredVideos) | **GET** /api/v1/server/redundancy/videos | List videos being mirrored
*VideoMirroringApi* | [**putMirroredVideo**](docs/VideoMirroringApi.md#putMirroredVideo) | **POST** /api/v1/server/redundancy/videos | Mirror a video
*VideoOwnershipChangeApi* | [**apiV1VideosIdGiveOwnershipPost**](docs/VideoOwnershipChangeApi.md#apiV1VideosIdGiveOwnershipPost) | **POST** /api/v1/videos/{id}/give-ownership | Request ownership change
*VideoOwnershipChangeApi* | [**apiV1VideosOwnershipGet**](docs/VideoOwnershipChangeApi.md#apiV1VideosOwnershipGet) | **GET** /api/v1/videos/ownership | List video ownership changes
*VideoOwnershipChangeApi* | [**apiV1VideosOwnershipIdAcceptPost**](docs/VideoOwnershipChangeApi.md#apiV1VideosOwnershipIdAcceptPost) | **POST** /api/v1/videos/ownership/{id}/accept | Accept ownership change request
*VideoOwnershipChangeApi* | [**apiV1VideosOwnershipIdRefusePost**](docs/VideoOwnershipChangeApi.md#apiV1VideosOwnershipIdRefusePost) | **POST** /api/v1/videos/ownership/{id}/refuse | Refuse ownership change request
*VideoPlaylistsApi* | [**addPlaylist**](docs/VideoPlaylistsApi.md#addPlaylist) | **POST** /api/v1/video-playlists | Create a video playlist
*VideoPlaylistsApi* | [**addVideoPlaylistVideo_0**](docs/VideoPlaylistsApi.md#addVideoPlaylistVideo_0) | **POST** /api/v1/video-playlists/{playlistId}/videos | Add a video in a playlist
*VideoPlaylistsApi* | [**apiV1AccountsNameVideoPlaylistsGet**](docs/VideoPlaylistsApi.md#apiV1AccountsNameVideoPlaylistsGet) | **GET** /api/v1/accounts/{name}/video-playlists | List playlists of an account
*VideoPlaylistsApi* | [**apiV1UsersMeVideoPlaylistsVideosExistGet**](docs/VideoPlaylistsApi.md#apiV1UsersMeVideoPlaylistsVideosExistGet) | **GET** /api/v1/users/me/video-playlists/videos-exist | Check video exists in my playlists
*VideoPlaylistsApi* | [**apiV1VideoChannelsChannelHandleVideoPlaylistsGet**](docs/VideoPlaylistsApi.md#apiV1VideoChannelsChannelHandleVideoPlaylistsGet) | **GET** /api/v1/video-channels/{channelHandle}/video-playlists | List playlists of a channel
*VideoPlaylistsApi* | [**apiV1VideoPlaylistsPlaylistIdDelete**](docs/VideoPlaylistsApi.md#apiV1VideoPlaylistsPlaylistIdDelete) | **DELETE** /api/v1/video-playlists/{playlistId} | Delete a video playlist
*VideoPlaylistsApi* | [**apiV1VideoPlaylistsPlaylistIdGet**](docs/VideoPlaylistsApi.md#apiV1VideoPlaylistsPlaylistIdGet) | **GET** /api/v1/video-playlists/{playlistId} | Get a video playlist
*VideoPlaylistsApi* | [**apiV1VideoPlaylistsPlaylistIdPut**](docs/VideoPlaylistsApi.md#apiV1VideoPlaylistsPlaylistIdPut) | **PUT** /api/v1/video-playlists/{playlistId} | Update a video playlist
*VideoPlaylistsApi* | [**delVideoPlaylistVideo**](docs/VideoPlaylistsApi.md#delVideoPlaylistVideo) | **DELETE** /api/v1/video-playlists/{playlistId}/videos/{playlistElementId} | Delete an element from a playlist
*VideoPlaylistsApi* | [**getPlaylistPrivacyPolicies**](docs/VideoPlaylistsApi.md#getPlaylistPrivacyPolicies) | **GET** /api/v1/video-playlists/privacies | List available playlist privacy policies
*VideoPlaylistsApi* | [**getPlaylists**](docs/VideoPlaylistsApi.md#getPlaylists) | **GET** /api/v1/video-playlists | List video playlists
*VideoPlaylistsApi* | [**getVideoPlaylistVideos_0**](docs/VideoPlaylistsApi.md#getVideoPlaylistVideos_0) | **GET** /api/v1/video-playlists/{playlistId}/videos | List videos of a playlist
*VideoPlaylistsApi* | [**putVideoPlaylistVideo**](docs/VideoPlaylistsApi.md#putVideoPlaylistVideo) | **PUT** /api/v1/video-playlists/{playlistId}/videos/{playlistElementId} | Update a playlist element
*VideoPlaylistsApi* | [**reorderVideoPlaylist**](docs/VideoPlaylistsApi.md#reorderVideoPlaylist) | **POST** /api/v1/video-playlists/{playlistId}/videos/reorder | Reorder a playlist
*VideoRatesApi* | [**apiV1UsersMeVideosVideoIdRatingGet_0**](docs/VideoRatesApi.md#apiV1UsersMeVideosVideoIdRatingGet_0) | **GET** /api/v1/users/me/videos/{videoId}/rating | Get rate of my user for a video
*VideoRatesApi* | [**apiV1VideosIdRatePut**](docs/VideoRatesApi.md#apiV1VideosIdRatePut) | **PUT** /api/v1/videos/{id}/rate | Like/dislike a video
*VideoStatsApi* | [**apiV1VideosIdStatsOverallGet**](docs/VideoStatsApi.md#apiV1VideosIdStatsOverallGet) | **GET** /api/v1/videos/{id}/stats/overall | Get overall stats of a video
*VideoStatsApi* | [**apiV1VideosIdStatsRetentionGet**](docs/VideoStatsApi.md#apiV1VideosIdStatsRetentionGet) | **GET** /api/v1/videos/{id}/stats/retention | Get retention stats of a video
*VideoStatsApi* | [**apiV1VideosIdStatsTimeseriesMetricGet**](docs/VideoStatsApi.md#apiV1VideosIdStatsTimeseriesMetricGet) | **GET** /api/v1/videos/{id}/stats/timeseries/{metric} | Get timeserie stats of a video
*VideoTranscodingApi* | [**apiV1VideosIdStudioEditPost**](docs/VideoTranscodingApi.md#apiV1VideosIdStudioEditPost) | **POST** /api/v1/videos/{id}/studio/edit | Create a studio task
*VideoTranscodingApi* | [**createVideoTranscoding**](docs/VideoTranscodingApi.md#createVideoTranscoding) | **POST** /api/v1/videos/{id}/transcoding | Create a transcoding job
*VideoUploadApi* | [**importVideo_0**](docs/VideoUploadApi.md#importVideo_0) | **POST** /api/v1/videos/imports | Import a video
*VideoUploadApi* | [**uploadLegacy_0**](docs/VideoUploadApi.md#uploadLegacy_0) | **POST** /api/v1/videos/upload | Upload a video
*VideoUploadApi* | [**uploadResumableCancel_0**](docs/VideoUploadApi.md#uploadResumableCancel_0) | **DELETE** /api/v1/videos/upload-resumable | Cancel the resumable upload of a video, deleting any data uploaded so far
*VideoUploadApi* | [**uploadResumableInit_0**](docs/VideoUploadApi.md#uploadResumableInit_0) | **POST** /api/v1/videos/upload-resumable | Initialize the resumable upload of a video
*VideoUploadApi* | [**uploadResumable_0**](docs/VideoUploadApi.md#uploadResumable_0) | **PUT** /api/v1/videos/upload-resumable | Send chunk for the resumable upload of a video
*VideosApi* | [**addVideoPlaylistVideo**](docs/VideosApi.md#addVideoPlaylistVideo) | **POST** /api/v1/video-playlists/{playlistId}/videos | Add a video in a playlist
*VideosApi* | [**apiV1UsersMeSubscriptionsVideosGet_0**](docs/VideosApi.md#apiV1UsersMeSubscriptionsVideosGet_0) | **GET** /api/v1/users/me/subscriptions/videos | List videos of subscriptions of my user
*VideosApi* | [**apiV1UsersMeVideosGet_0**](docs/VideosApi.md#apiV1UsersMeVideosGet_0) | **GET** /api/v1/users/me/videos | Get videos of my user
*VideosApi* | [**apiV1UsersMeVideosImportsGet**](docs/VideosApi.md#apiV1UsersMeVideosImportsGet) | **GET** /api/v1/users/me/videos/imports | Get video imports of my user
*VideosApi* | [**getVideoPlaylistVideos**](docs/VideosApi.md#getVideoPlaylistVideos) | **GET** /api/v1/video-playlists/{playlistId}/videos | List videos of a playlist


## Documentation for Models

 - [Abuse](docs/Abuse.md)
 - [AbuseMessage](docs/AbuseMessage.md)
 - [AbuseStateConstant](docs/AbuseStateConstant.md)
 - [AbuseStateSet](docs/AbuseStateSet.md)
 - [Account](docs/Account.md)
 - [AccountSummary](docs/AccountSummary.md)
 - [Actor](docs/Actor.md)
 - [ActorImage](docs/ActorImage.md)
 - [ActorInfo](docs/ActorInfo.md)
 - [AddIntroOptions](docs/AddIntroOptions.md)
 - [AddPlaylist200Response](docs/AddPlaylist200Response.md)
 - [AddPlaylist200ResponseVideoPlaylist](docs/AddPlaylist200ResponseVideoPlaylist.md)
 - [AddPluginRequest](docs/AddPluginRequest.md)
 - [AddPluginRequestOneOf](docs/AddPluginRequestOneOf.md)
 - [AddPluginRequestOneOf1](docs/AddPluginRequestOneOf1.md)
 - [AddUser](docs/AddUser.md)
 - [AddUserResponse](docs/AddUserResponse.md)
 - [AddUserResponseUser](docs/AddUserResponseUser.md)
 - [AddVideoChannel200Response](docs/AddVideoChannel200Response.md)
 - [AddVideoChannelSync200Response](docs/AddVideoChannelSync200Response.md)
 - [AddVideoPlaylistVideo200Response](docs/AddVideoPlaylistVideo200Response.md)
 - [AddVideoPlaylistVideo200ResponseVideoPlaylistElement](docs/AddVideoPlaylistVideo200ResponseVideoPlaylistElement.md)
 - [AddVideoPlaylistVideoRequest](docs/AddVideoPlaylistVideoRequest.md)
 - [AddVideoPlaylistVideoRequestVideoId](docs/AddVideoPlaylistVideoRequestVideoId.md)
 - [ApiV1AbusesAbuseIdMessagesGet200Response](docs/ApiV1AbusesAbuseIdMessagesGet200Response.md)
 - [ApiV1AbusesAbuseIdMessagesPostRequest](docs/ApiV1AbusesAbuseIdMessagesPostRequest.md)
 - [ApiV1AbusesAbuseIdPutRequest](docs/ApiV1AbusesAbuseIdPutRequest.md)
 - [ApiV1AbusesPost200Response](docs/ApiV1AbusesPost200Response.md)
 - [ApiV1AbusesPost200ResponseAbuse](docs/ApiV1AbusesPost200ResponseAbuse.md)
 - [ApiV1AbusesPostRequest](docs/ApiV1AbusesPostRequest.md)
 - [ApiV1AbusesPostRequestAccount](docs/ApiV1AbusesPostRequestAccount.md)
 - [ApiV1AbusesPostRequestComment](docs/ApiV1AbusesPostRequestComment.md)
 - [ApiV1AbusesPostRequestVideo](docs/ApiV1AbusesPostRequestVideo.md)
 - [ApiV1AccountsNameVideoPlaylistsGet200Response](docs/ApiV1AccountsNameVideoPlaylistsGet200Response.md)
 - [ApiV1CustomPagesHomepageInstancePutRequest](docs/ApiV1CustomPagesHomepageInstancePutRequest.md)
 - [ApiV1PluginsNpmNameSettingsPutRequest](docs/ApiV1PluginsNpmNameSettingsPutRequest.md)
 - [ApiV1ServerBlocklistAccountsPostRequest](docs/ApiV1ServerBlocklistAccountsPostRequest.md)
 - [ApiV1ServerBlocklistServersPostRequest](docs/ApiV1ServerBlocklistServersPostRequest.md)
 - [ApiV1ServerFollowingPostRequest](docs/ApiV1ServerFollowingPostRequest.md)
 - [ApiV1ServerRedundancyHostPutRequest](docs/ApiV1ServerRedundancyHostPutRequest.md)
 - [ApiV1UsersMeAvatarPickPost200Response](docs/ApiV1UsersMeAvatarPickPost200Response.md)
 - [ApiV1UsersMeNotificationSettingsPutRequest](docs/ApiV1UsersMeNotificationSettingsPutRequest.md)
 - [ApiV1UsersMeNotificationsReadPostRequest](docs/ApiV1UsersMeNotificationsReadPostRequest.md)
 - [ApiV1UsersMeSubscriptionsPostRequest](docs/ApiV1UsersMeSubscriptionsPostRequest.md)
 - [ApiV1UsersMeVideoPlaylistsVideosExistGet200Response](docs/ApiV1UsersMeVideoPlaylistsVideosExistGet200Response.md)
 - [ApiV1UsersMeVideoPlaylistsVideosExistGet200ResponseVideoIdInner](docs/ApiV1UsersMeVideoPlaylistsVideosExistGet200ResponseVideoIdInner.md)
 - [ApiV1UsersMeVideoQuotaUsedGet200Response](docs/ApiV1UsersMeVideoQuotaUsedGet200Response.md)
 - [ApiV1VideoChannelsChannelHandleBannerPickPost200Response](docs/ApiV1VideoChannelsChannelHandleBannerPickPost200Response.md)
 - [ApiV1VideosIdCommentThreadsPostRequest](docs/ApiV1VideosIdCommentThreadsPostRequest.md)
 - [ApiV1VideosIdRatePutRequest](docs/ApiV1VideosIdRatePutRequest.md)
 - [ApiV1VideosLiveIdSessionsGet200Response](docs/ApiV1VideosLiveIdSessionsGet200Response.md)
 - [BlockStatus](docs/BlockStatus.md)
 - [BlockStatusAccountsValue](docs/BlockStatusAccountsValue.md)
 - [BlockStatusHostsValue](docs/BlockStatusHostsValue.md)
 - [CommentThreadPostResponse](docs/CommentThreadPostResponse.md)
 - [CommentThreadResponse](docs/CommentThreadResponse.md)
 - [ConfirmTwoFactorRequestRequest](docs/ConfirmTwoFactorRequestRequest.md)
 - [CreateVideoTranscodingRequest](docs/CreateVideoTranscodingRequest.md)
 - [CustomHomepage](docs/CustomHomepage.md)
 - [CutOptions](docs/CutOptions.md)
 - [DisableTwoFactorRequest](docs/DisableTwoFactorRequest.md)
 - [FileRedundancyInformation](docs/FileRedundancyInformation.md)
 - [Follow](docs/Follow.md)
 - [GetAbuses200Response](docs/GetAbuses200Response.md)
 - [GetAccountFollowers200Response](docs/GetAccountFollowers200Response.md)
 - [GetAccountVideosCategoryOneOfParameter](docs/GetAccountVideosCategoryOneOfParameter.md)
 - [GetAccountVideosLanguageOneOfParameter](docs/GetAccountVideosLanguageOneOfParameter.md)
 - [GetAccountVideosLicenceOneOfParameter](docs/GetAccountVideosLicenceOneOfParameter.md)
 - [GetAccountVideosTagsAllOfParameter](docs/GetAccountVideosTagsAllOfParameter.md)
 - [GetAccountVideosTagsOneOfParameter](docs/GetAccountVideosTagsOneOfParameter.md)
 - [GetJobs200Response](docs/GetJobs200Response.md)
 - [GetLiveIdIdParameter](docs/GetLiveIdIdParameter.md)
 - [GetMeVideoRating](docs/GetMeVideoRating.md)
 - [GetOAuthToken200Response](docs/GetOAuthToken200Response.md)
 - [GetUser200Response](docs/GetUser200Response.md)
 - [GetVideoBlocks200Response](docs/GetVideoBlocks200Response.md)
 - [GetVideoCaptions200Response](docs/GetVideoCaptions200Response.md)
 - [ImportVideosInChannelCreate](docs/ImportVideosInChannelCreate.md)
 - [Job](docs/Job.md)
 - [ListRegistrations200Response](docs/ListRegistrations200Response.md)
 - [LiveVideoLatencyMode](docs/LiveVideoLatencyMode.md)
 - [LiveVideoReplaySettings](docs/LiveVideoReplaySettings.md)
 - [LiveVideoResponse](docs/LiveVideoResponse.md)
 - [LiveVideoSessionResponse](docs/LiveVideoSessionResponse.md)
 - [LiveVideoSessionResponseReplayVideo](docs/LiveVideoSessionResponseReplayVideo.md)
 - [LiveVideoUpdate](docs/LiveVideoUpdate.md)
 - [MRSSGroupContent](docs/MRSSGroupContent.md)
 - [MRSSPeerLink](docs/MRSSPeerLink.md)
 - [NSFWPolicy](docs/NSFWPolicy.md)
 - [Notification](docs/Notification.md)
 - [NotificationActorFollow](docs/NotificationActorFollow.md)
 - [NotificationActorFollowFollowing](docs/NotificationActorFollowFollowing.md)
 - [NotificationComment](docs/NotificationComment.md)
 - [NotificationListResponse](docs/NotificationListResponse.md)
 - [NotificationVideo](docs/NotificationVideo.md)
 - [NotificationVideoAbuse](docs/NotificationVideoAbuse.md)
 - [NotificationVideoImport](docs/NotificationVideoImport.md)
 - [OAuthClient](docs/OAuthClient.md)
 - [PlaybackMetricCreate](docs/PlaybackMetricCreate.md)
 - [PlaylistElement](docs/PlaylistElement.md)
 - [Plugin](docs/Plugin.md)
 - [PluginResponse](docs/PluginResponse.md)
 - [PutMirroredVideoRequest](docs/PutMirroredVideoRequest.md)
 - [PutVideoPlaylistVideoRequest](docs/PutVideoPlaylistVideoRequest.md)
 - [RegisterUser](docs/RegisterUser.md)
 - [RegisterUserChannel](docs/RegisterUserChannel.md)
 - [ReorderVideoPlaylistRequest](docs/ReorderVideoPlaylistRequest.md)
 - [RequestTwoFactorResponse](docs/RequestTwoFactorResponse.md)
 - [RequestTwoFactorResponseOtpRequest](docs/RequestTwoFactorResponseOtpRequest.md)
 - [ResendEmailToVerifyRegistrationRequest](docs/ResendEmailToVerifyRegistrationRequest.md)
 - [ResendEmailToVerifyUserRequest](docs/ResendEmailToVerifyUserRequest.md)
 - [SendClientLog](docs/SendClientLog.md)
 - [ServerConfig](docs/ServerConfig.md)
 - [ServerConfigAbout](docs/ServerConfigAbout.md)
 - [ServerConfigAboutInstance](docs/ServerConfigAboutInstance.md)
 - [ServerConfigAutoBlacklist](docs/ServerConfigAutoBlacklist.md)
 - [ServerConfigAutoBlacklistVideos](docs/ServerConfigAutoBlacklistVideos.md)
 - [ServerConfigAutoBlacklistVideosOfUsers](docs/ServerConfigAutoBlacklistVideosOfUsers.md)
 - [ServerConfigAvatar](docs/ServerConfigAvatar.md)
 - [ServerConfigAvatarFile](docs/ServerConfigAvatarFile.md)
 - [ServerConfigAvatarFileSize](docs/ServerConfigAvatarFileSize.md)
 - [ServerConfigCustom](docs/ServerConfigCustom.md)
 - [ServerConfigCustomAdmin](docs/ServerConfigCustomAdmin.md)
 - [ServerConfigCustomCache](docs/ServerConfigCustomCache.md)
 - [ServerConfigCustomCacheCaptions](docs/ServerConfigCustomCacheCaptions.md)
 - [ServerConfigCustomFollowers](docs/ServerConfigCustomFollowers.md)
 - [ServerConfigCustomFollowersInstance](docs/ServerConfigCustomFollowersInstance.md)
 - [ServerConfigCustomImport](docs/ServerConfigCustomImport.md)
 - [ServerConfigCustomInstance](docs/ServerConfigCustomInstance.md)
 - [ServerConfigCustomServices](docs/ServerConfigCustomServices.md)
 - [ServerConfigCustomServicesTwitter](docs/ServerConfigCustomServicesTwitter.md)
 - [ServerConfigCustomSignup](docs/ServerConfigCustomSignup.md)
 - [ServerConfigCustomTheme](docs/ServerConfigCustomTheme.md)
 - [ServerConfigCustomTranscoding](docs/ServerConfigCustomTranscoding.md)
 - [ServerConfigCustomTranscodingHls](docs/ServerConfigCustomTranscodingHls.md)
 - [ServerConfigCustomTranscodingResolutions](docs/ServerConfigCustomTranscodingResolutions.md)
 - [ServerConfigCustomTranscodingWebtorrent](docs/ServerConfigCustomTranscodingWebtorrent.md)
 - [ServerConfigCustomUser](docs/ServerConfigCustomUser.md)
 - [ServerConfigFollowings](docs/ServerConfigFollowings.md)
 - [ServerConfigFollowingsInstance](docs/ServerConfigFollowingsInstance.md)
 - [ServerConfigFollowingsInstanceAutoFollowIndex](docs/ServerConfigFollowingsInstanceAutoFollowIndex.md)
 - [ServerConfigImport](docs/ServerConfigImport.md)
 - [ServerConfigImportVideos](docs/ServerConfigImportVideos.md)
 - [ServerConfigInstance](docs/ServerConfigInstance.md)
 - [ServerConfigInstanceCustomizations](docs/ServerConfigInstanceCustomizations.md)
 - [ServerConfigPlugin](docs/ServerConfigPlugin.md)
 - [ServerConfigSearch](docs/ServerConfigSearch.md)
 - [ServerConfigSearchRemoteUri](docs/ServerConfigSearchRemoteUri.md)
 - [ServerConfigSignup](docs/ServerConfigSignup.md)
 - [ServerConfigTranscoding](docs/ServerConfigTranscoding.md)
 - [ServerConfigTrending](docs/ServerConfigTrending.md)
 - [ServerConfigTrendingVideos](docs/ServerConfigTrendingVideos.md)
 - [ServerConfigUser](docs/ServerConfigUser.md)
 - [ServerConfigVideo](docs/ServerConfigVideo.md)
 - [ServerConfigVideoCaption](docs/ServerConfigVideoCaption.md)
 - [ServerConfigVideoFile](docs/ServerConfigVideoFile.md)
 - [ServerConfigVideoImage](docs/ServerConfigVideoImage.md)
 - [ServerStats](docs/ServerStats.md)
 - [ServerStatsVideosRedundancyInner](docs/ServerStatsVideosRedundancyInner.md)
 - [UninstallPluginRequest](docs/UninstallPluginRequest.md)
 - [UpdateMe](docs/UpdateMe.md)
 - [UpdateUser](docs/UpdateUser.md)
 - [User](docs/User.md)
 - [UserAdminFlags](docs/UserAdminFlags.md)
 - [UserRegistration](docs/UserRegistration.md)
 - [UserRegistrationAcceptOrReject](docs/UserRegistrationAcceptOrReject.md)
 - [UserRegistrationRequest](docs/UserRegistrationRequest.md)
 - [UserRegistrationState](docs/UserRegistrationState.md)
 - [UserRegistrationUser](docs/UserRegistrationUser.md)
 - [UserRole](docs/UserRole.md)
 - [UserViewingVideo](docs/UserViewingVideo.md)
 - [UserWithStats](docs/UserWithStats.md)
 - [VerifyRegistrationEmailRequest](docs/VerifyRegistrationEmailRequest.md)
 - [VerifyUserRequest](docs/VerifyUserRequest.md)
 - [Video](docs/Video.md)
 - [VideoBlacklist](docs/VideoBlacklist.md)
 - [VideoCaption](docs/VideoCaption.md)
 - [VideoChannel](docs/VideoChannel.md)
 - [VideoChannelAllOfOwnerAccount](docs/VideoChannelAllOfOwnerAccount.md)
 - [VideoChannelCreate](docs/VideoChannelCreate.md)
 - [VideoChannelEdit](docs/VideoChannelEdit.md)
 - [VideoChannelList](docs/VideoChannelList.md)
 - [VideoChannelListDataInner](docs/VideoChannelListDataInner.md)
 - [VideoChannelSummary](docs/VideoChannelSummary.md)
 - [VideoChannelSync](docs/VideoChannelSync.md)
 - [VideoChannelSyncCreate](docs/VideoChannelSyncCreate.md)
 - [VideoChannelSyncList](docs/VideoChannelSyncList.md)
 - [VideoChannelSyncState](docs/VideoChannelSyncState.md)
 - [VideoChannelUpdate](docs/VideoChannelUpdate.md)
 - [VideoComment](docs/VideoComment.md)
 - [VideoCommentThreadTree](docs/VideoCommentThreadTree.md)
 - [VideoCommentsForXMLInner](docs/VideoCommentsForXMLInner.md)
 - [VideoConstantNumberCategory](docs/VideoConstantNumberCategory.md)
 - [VideoConstantNumberLicence](docs/VideoConstantNumberLicence.md)
 - [VideoConstantStringLanguage](docs/VideoConstantStringLanguage.md)
 - [VideoDetails](docs/VideoDetails.md)
 - [VideoFile](docs/VideoFile.md)
 - [VideoImport](docs/VideoImport.md)
 - [VideoImportStateConstant](docs/VideoImportStateConstant.md)
 - [VideoImportsList](docs/VideoImportsList.md)
 - [VideoInfo](docs/VideoInfo.md)
 - [VideoListResponse](docs/VideoListResponse.md)
 - [VideoPlaylist](docs/VideoPlaylist.md)
 - [VideoPlaylistPrivacyConstant](docs/VideoPlaylistPrivacyConstant.md)
 - [VideoPlaylistPrivacySet](docs/VideoPlaylistPrivacySet.md)
 - [VideoPlaylistTypeConstant](docs/VideoPlaylistTypeConstant.md)
 - [VideoPlaylistTypeSet](docs/VideoPlaylistTypeSet.md)
 - [VideoPrivacyConstant](docs/VideoPrivacyConstant.md)
 - [VideoPrivacySet](docs/VideoPrivacySet.md)
 - [VideoRating](docs/VideoRating.md)
 - [VideoRedundancy](docs/VideoRedundancy.md)
 - [VideoRedundancyRedundancies](docs/VideoRedundancyRedundancies.md)
 - [VideoResolutionConstant](docs/VideoResolutionConstant.md)
 - [VideoScheduledUpdate](docs/VideoScheduledUpdate.md)
 - [VideoSource](docs/VideoSource.md)
 - [VideoStateConstant](docs/VideoStateConstant.md)
 - [VideoStatsOverall](docs/VideoStatsOverall.md)
 - [VideoStatsOverallCountriesInner](docs/VideoStatsOverallCountriesInner.md)
 - [VideoStatsRetention](docs/VideoStatsRetention.md)
 - [VideoStatsRetentionDataInner](docs/VideoStatsRetentionDataInner.md)
 - [VideoStatsTimeserie](docs/VideoStatsTimeserie.md)
 - [VideoStatsTimeserieDataInner](docs/VideoStatsTimeserieDataInner.md)
 - [VideoStreamingPlaylists](docs/VideoStreamingPlaylists.md)
 - [VideoStreamingPlaylistsHLS](docs/VideoStreamingPlaylistsHLS.md)
 - [VideoStreamingPlaylistsHLSRedundanciesInner](docs/VideoStreamingPlaylistsHLSRedundanciesInner.md)
 - [VideoTokenResponse](docs/VideoTokenResponse.md)
 - [VideoTokenResponseFiles](docs/VideoTokenResponseFiles.md)
 - [VideoUploadRequestCommon](docs/VideoUploadRequestCommon.md)
 - [VideoUploadRequestResumable](docs/VideoUploadRequestResumable.md)
 - [VideoUploadResponse](docs/VideoUploadResponse.md)
 - [VideoUploadResponseVideo](docs/VideoUploadResponseVideo.md)
 - [VideoUserHistory](docs/VideoUserHistory.md)
 - [VideosForXMLInner](docs/VideosForXMLInner.md)
 - [VideosForXMLInnerEnclosure](docs/VideosForXMLInnerEnclosure.md)
 - [VideosForXMLInnerMediaCommunity](docs/VideosForXMLInnerMediaCommunity.md)
 - [VideosForXMLInnerMediaCommunityMediaStatistics](docs/VideosForXMLInnerMediaCommunityMediaStatistics.md)
 - [VideosForXMLInnerMediaEmbed](docs/VideosForXMLInnerMediaEmbed.md)
 - [VideosForXMLInnerMediaGroupInner](docs/VideosForXMLInnerMediaGroupInner.md)
 - [VideosForXMLInnerMediaPlayer](docs/VideosForXMLInnerMediaPlayer.md)
 - [VideosForXMLInnerMediaThumbnail](docs/VideosForXMLInnerMediaThumbnail.md)


<a id="documentation-for-authorization"></a>
## Documentation for Authorization


Authentication schemes defined for the API:
<a id="OAuth2"></a>
### OAuth2

- **Type**: OAuth
- **Flow**: password
- **Authorization URL**: 
- **Scopes**: 
  - admin: Admin scope
  - moderator: Moderator scope
  - user: User scope


## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author



