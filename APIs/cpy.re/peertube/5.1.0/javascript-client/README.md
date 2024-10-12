# peer_tube

PeerTube - JavaScript client for peer_tube
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

This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 5.1.0
- Package version: 5.1.0
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.JavascriptClientCodegen
For more information, please visit [https://joinpeertube.org](https://joinpeertube.org)

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/), please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install peer_tube --save
```

Finally, you need to build the module:

```shell
npm run build
```

##### Local development

To use the library locally without publishing to a remote npm registry, first install the dependencies by changing into the directory containing `package.json` (and this README). Let's call this `JAVASCRIPT_CLIENT_DIR`. Then run:

```shell
npm install
```

Next, [link](https://docs.npmjs.com/cli/link) it globally in npm with the following, also from `JAVASCRIPT_CLIENT_DIR`:

```shell
npm link
```

To use the link you just defined in your project, switch to the directory you want to use your peer_tube from, and run:

```shell
npm link /path/to/<JAVASCRIPT_CLIENT_DIR>
```

Finally, you need to build the module:

```shell
npm run build
```

#### git

If the library is hosted at a git repository, e.g.https://github.com/GIT_USER_ID/GIT_REPO_ID
then install it via:

```shell
    npm install GIT_USER_ID/GIT_REPO_ID --save
```

### For browser

The library also works in the browser environment via npm and [browserify](http://browserify.org/). After following
the above steps with Node.js and installing browserify with `npm install -g browserify`,
perform the following (assuming *main.js* is your entry file):

```shell
browserify main.js > bundle.js
```

Then include *bundle.js* in the HTML pages.

### Webpack Configuration

Using Webpack you may encounter the following error: "Module not found: Error:
Cannot resolve module", most certainly you should disable AMD loader. Add/merge
the following section to your webpack config:

```javascript
module: {
  rules: [
    {
      parser: {
        amd: false
      }
    }
  ]
}
```

## Getting Started

Please follow the [installation](#installation) instruction and execute the following JS code:

```javascript
var PeerTube = require('peer_tube');

var defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
var OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = "YOUR ACCESS TOKEN"

var api = new PeerTube.AbusesApi()
var abuseId = 56; // {Number} Abuse id
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
api.apiV1AbusesAbuseIdDelete(abuseId, callback);

```

## Documentation for API Endpoints

All URIs are relative to *https://peertube2.cpy.re*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*PeerTube.AbusesApi* | [**apiV1AbusesAbuseIdDelete**](docs/AbusesApi.md#apiV1AbusesAbuseIdDelete) | **DELETE** /api/v1/abuses/{abuseId} | Delete an abuse
*PeerTube.AbusesApi* | [**apiV1AbusesAbuseIdMessagesAbuseMessageIdDelete**](docs/AbusesApi.md#apiV1AbusesAbuseIdMessagesAbuseMessageIdDelete) | **DELETE** /api/v1/abuses/{abuseId}/messages/{abuseMessageId} | Delete an abuse message
*PeerTube.AbusesApi* | [**apiV1AbusesAbuseIdMessagesGet**](docs/AbusesApi.md#apiV1AbusesAbuseIdMessagesGet) | **GET** /api/v1/abuses/{abuseId}/messages | List messages of an abuse
*PeerTube.AbusesApi* | [**apiV1AbusesAbuseIdMessagesPost**](docs/AbusesApi.md#apiV1AbusesAbuseIdMessagesPost) | **POST** /api/v1/abuses/{abuseId}/messages | Add message to an abuse
*PeerTube.AbusesApi* | [**apiV1AbusesAbuseIdPut**](docs/AbusesApi.md#apiV1AbusesAbuseIdPut) | **PUT** /api/v1/abuses/{abuseId} | Update an abuse
*PeerTube.AbusesApi* | [**apiV1AbusesPost**](docs/AbusesApi.md#apiV1AbusesPost) | **POST** /api/v1/abuses | Report an abuse
*PeerTube.AbusesApi* | [**getAbuses**](docs/AbusesApi.md#getAbuses) | **GET** /api/v1/abuses | List abuses
*PeerTube.AbusesApi* | [**getMyAbuses**](docs/AbusesApi.md#getMyAbuses) | **GET** /api/v1/users/me/abuses | List my abuses
*PeerTube.AccountBlocksApi* | [**apiV1BlocklistStatusGet**](docs/AccountBlocksApi.md#apiV1BlocklistStatusGet) | **GET** /api/v1/blocklist/status | Get block status of accounts/hosts
*PeerTube.AccountBlocksApi* | [**apiV1ServerBlocklistAccountsAccountNameDelete**](docs/AccountBlocksApi.md#apiV1ServerBlocklistAccountsAccountNameDelete) | **DELETE** /api/v1/server/blocklist/accounts/{accountName} | Unblock an account by its handle
*PeerTube.AccountBlocksApi* | [**apiV1ServerBlocklistAccountsGet**](docs/AccountBlocksApi.md#apiV1ServerBlocklistAccountsGet) | **GET** /api/v1/server/blocklist/accounts | List account blocks
*PeerTube.AccountBlocksApi* | [**apiV1ServerBlocklistAccountsPost**](docs/AccountBlocksApi.md#apiV1ServerBlocklistAccountsPost) | **POST** /api/v1/server/blocklist/accounts | Block an account
*PeerTube.AccountsApi* | [**apiV1AccountsNameRatingsGet**](docs/AccountsApi.md#apiV1AccountsNameRatingsGet) | **GET** /api/v1/accounts/{name}/ratings | List ratings of an account
*PeerTube.AccountsApi* | [**apiV1AccountsNameVideoChannelSyncsGet_1**](docs/AccountsApi.md#apiV1AccountsNameVideoChannelSyncsGet_1) | **GET** /api/v1/accounts/{name}/video-channel-syncs | List the synchronizations of video channels of an account
*PeerTube.AccountsApi* | [**apiV1AccountsNameVideoChannelsGet_0**](docs/AccountsApi.md#apiV1AccountsNameVideoChannelsGet_0) | **GET** /api/v1/accounts/{name}/video-channels | List video channels of an account
*PeerTube.AccountsApi* | [**apiV1AccountsNameVideoPlaylistsGet_0**](docs/AccountsApi.md#apiV1AccountsNameVideoPlaylistsGet_0) | **GET** /api/v1/accounts/{name}/video-playlists | List playlists of an account
*PeerTube.AccountsApi* | [**getAccount**](docs/AccountsApi.md#getAccount) | **GET** /api/v1/accounts/{name} | Get an account
*PeerTube.AccountsApi* | [**getAccountFollowers**](docs/AccountsApi.md#getAccountFollowers) | **GET** /api/v1/accounts/{name}/followers | List followers of an account
*PeerTube.AccountsApi* | [**getAccountVideos**](docs/AccountsApi.md#getAccountVideos) | **GET** /api/v1/accounts/{name}/videos | List videos of an account
*PeerTube.AccountsApi* | [**getAccounts**](docs/AccountsApi.md#getAccounts) | **GET** /api/v1/accounts | List accounts
*PeerTube.ChannelsSyncApi* | [**addVideoChannelSync**](docs/ChannelsSyncApi.md#addVideoChannelSync) | **POST** /api/v1/video-channel-syncs | Create a synchronization for a video channel
*PeerTube.ChannelsSyncApi* | [**apiV1AccountsNameVideoChannelSyncsGet_0**](docs/ChannelsSyncApi.md#apiV1AccountsNameVideoChannelSyncsGet_0) | **GET** /api/v1/accounts/{name}/video-channel-syncs | List the synchronizations of video channels of an account
*PeerTube.ChannelsSyncApi* | [**apiV1VideoChannelsChannelHandleImportVideosPost_0**](docs/ChannelsSyncApi.md#apiV1VideoChannelsChannelHandleImportVideosPost_0) | **POST** /api/v1/video-channels/{channelHandle}/import-videos | Import videos in channel
*PeerTube.ChannelsSyncApi* | [**delVideoChannelSync**](docs/ChannelsSyncApi.md#delVideoChannelSync) | **DELETE** /api/v1/video-channel-syncs/{channelSyncId} | Delete a video channel synchronization
*PeerTube.ChannelsSyncApi* | [**triggerVideoChannelSync**](docs/ChannelsSyncApi.md#triggerVideoChannelSync) | **POST** /api/v1/video-channel-syncs/{channelSyncId}/sync | Triggers the channel synchronization job, fetching all the videos from the remote channel
*PeerTube.ConfigApi* | [**delCustomConfig**](docs/ConfigApi.md#delCustomConfig) | **DELETE** /api/v1/config/custom | Delete instance runtime configuration
*PeerTube.ConfigApi* | [**getAbout**](docs/ConfigApi.md#getAbout) | **GET** /api/v1/config/about | Get instance \&quot;About\&quot; information
*PeerTube.ConfigApi* | [**getConfig**](docs/ConfigApi.md#getConfig) | **GET** /api/v1/config | Get instance public configuration
*PeerTube.ConfigApi* | [**getCustomConfig**](docs/ConfigApi.md#getCustomConfig) | **GET** /api/v1/config/custom | Get instance runtime configuration
*PeerTube.ConfigApi* | [**putCustomConfig**](docs/ConfigApi.md#putCustomConfig) | **PUT** /api/v1/config/custom | Set instance runtime configuration
*PeerTube.HomepageApi* | [**apiV1CustomPagesHomepageInstanceGet**](docs/HomepageApi.md#apiV1CustomPagesHomepageInstanceGet) | **GET** /api/v1/custom-pages/homepage/instance | Get instance custom homepage
*PeerTube.HomepageApi* | [**apiV1CustomPagesHomepageInstancePut**](docs/HomepageApi.md#apiV1CustomPagesHomepageInstancePut) | **PUT** /api/v1/custom-pages/homepage/instance | Set instance custom homepage
*PeerTube.InstanceFollowsApi* | [**apiV1ServerFollowersGet**](docs/InstanceFollowsApi.md#apiV1ServerFollowersGet) | **GET** /api/v1/server/followers | List instances following the server
*PeerTube.InstanceFollowsApi* | [**apiV1ServerFollowersNameWithHostAcceptPost**](docs/InstanceFollowsApi.md#apiV1ServerFollowersNameWithHostAcceptPost) | **POST** /api/v1/server/followers/{nameWithHost}/accept | Accept a pending follower to your server
*PeerTube.InstanceFollowsApi* | [**apiV1ServerFollowersNameWithHostDelete**](docs/InstanceFollowsApi.md#apiV1ServerFollowersNameWithHostDelete) | **DELETE** /api/v1/server/followers/{nameWithHost} | Remove or reject a follower to your server
*PeerTube.InstanceFollowsApi* | [**apiV1ServerFollowersNameWithHostRejectPost**](docs/InstanceFollowsApi.md#apiV1ServerFollowersNameWithHostRejectPost) | **POST** /api/v1/server/followers/{nameWithHost}/reject | Reject a pending follower to your server
*PeerTube.InstanceFollowsApi* | [**apiV1ServerFollowingGet**](docs/InstanceFollowsApi.md#apiV1ServerFollowingGet) | **GET** /api/v1/server/following | List instances followed by the server
*PeerTube.InstanceFollowsApi* | [**apiV1ServerFollowingHostOrHandleDelete**](docs/InstanceFollowsApi.md#apiV1ServerFollowingHostOrHandleDelete) | **DELETE** /api/v1/server/following/{hostOrHandle} | Unfollow an actor (PeerTube instance, channel or account)
*PeerTube.InstanceFollowsApi* | [**apiV1ServerFollowingPost**](docs/InstanceFollowsApi.md#apiV1ServerFollowingPost) | **POST** /api/v1/server/following | Follow a list of actors (PeerTube instance, channel or account)
*PeerTube.InstanceRedundancyApi* | [**apiV1ServerRedundancyHostPut**](docs/InstanceRedundancyApi.md#apiV1ServerRedundancyHostPut) | **PUT** /api/v1/server/redundancy/{host} | Update a server redundancy policy
*PeerTube.JobApi* | [**apiV1JobsPausePost**](docs/JobApi.md#apiV1JobsPausePost) | **POST** /api/v1/jobs/pause | Pause job queue
*PeerTube.JobApi* | [**apiV1JobsResumePost**](docs/JobApi.md#apiV1JobsResumePost) | **POST** /api/v1/jobs/resume | Resume job queue
*PeerTube.JobApi* | [**getJobs**](docs/JobApi.md#getJobs) | **GET** /api/v1/jobs/{state} | List instance jobs
*PeerTube.LiveVideosApi* | [**addLive**](docs/LiveVideosApi.md#addLive) | **POST** /api/v1/videos/live | Create a live
*PeerTube.LiveVideosApi* | [**apiV1VideosIdLiveSessionGet**](docs/LiveVideosApi.md#apiV1VideosIdLiveSessionGet) | **GET** /api/v1/videos/{id}/live-session | Get live session of a replay
*PeerTube.LiveVideosApi* | [**apiV1VideosLiveIdSessionsGet**](docs/LiveVideosApi.md#apiV1VideosLiveIdSessionsGet) | **GET** /api/v1/videos/live/{id}/sessions | List live sessions
*PeerTube.LiveVideosApi* | [**getLiveId**](docs/LiveVideosApi.md#getLiveId) | **GET** /api/v1/videos/live/{id} | Get information about a live
*PeerTube.LiveVideosApi* | [**updateLiveId**](docs/LiveVideosApi.md#updateLiveId) | **PUT** /api/v1/videos/live/{id} | Update information about a live
*PeerTube.LogsApi* | [**getInstanceAuditLogs**](docs/LogsApi.md#getInstanceAuditLogs) | **GET** /api/v1/server/audit-logs | Get instance audit logs
*PeerTube.LogsApi* | [**getInstanceLogs**](docs/LogsApi.md#getInstanceLogs) | **GET** /api/v1/server/logs | Get instance logs
*PeerTube.LogsApi* | [**sendClientLog**](docs/LogsApi.md#sendClientLog) | **POST** /api/v1/server/logs/client | Send client log
*PeerTube.MyHistoryApi* | [**apiV1UsersMeHistoryVideosGet**](docs/MyHistoryApi.md#apiV1UsersMeHistoryVideosGet) | **GET** /api/v1/users/me/history/videos | List watched videos history
*PeerTube.MyHistoryApi* | [**apiV1UsersMeHistoryVideosRemovePost**](docs/MyHistoryApi.md#apiV1UsersMeHistoryVideosRemovePost) | **POST** /api/v1/users/me/history/videos/remove | Clear video history
*PeerTube.MyHistoryApi* | [**apiV1UsersMeHistoryVideosVideoIdDelete**](docs/MyHistoryApi.md#apiV1UsersMeHistoryVideosVideoIdDelete) | **DELETE** /api/v1/users/me/history/videos/{videoId} | Delete history element
*PeerTube.MyNotificationsApi* | [**apiV1UsersMeNotificationSettingsPut**](docs/MyNotificationsApi.md#apiV1UsersMeNotificationSettingsPut) | **PUT** /api/v1/users/me/notification-settings | Update my notification settings
*PeerTube.MyNotificationsApi* | [**apiV1UsersMeNotificationsGet**](docs/MyNotificationsApi.md#apiV1UsersMeNotificationsGet) | **GET** /api/v1/users/me/notifications | List my notifications
*PeerTube.MyNotificationsApi* | [**apiV1UsersMeNotificationsReadAllPost**](docs/MyNotificationsApi.md#apiV1UsersMeNotificationsReadAllPost) | **POST** /api/v1/users/me/notifications/read-all | Mark all my notification as read
*PeerTube.MyNotificationsApi* | [**apiV1UsersMeNotificationsReadPost**](docs/MyNotificationsApi.md#apiV1UsersMeNotificationsReadPost) | **POST** /api/v1/users/me/notifications/read | Mark notifications as read by their id
*PeerTube.MySubscriptionsApi* | [**apiV1UsersMeSubscriptionsExistGet**](docs/MySubscriptionsApi.md#apiV1UsersMeSubscriptionsExistGet) | **GET** /api/v1/users/me/subscriptions/exist | Get if subscriptions exist for my user
*PeerTube.MySubscriptionsApi* | [**apiV1UsersMeSubscriptionsGet**](docs/MySubscriptionsApi.md#apiV1UsersMeSubscriptionsGet) | **GET** /api/v1/users/me/subscriptions | Get my user subscriptions
*PeerTube.MySubscriptionsApi* | [**apiV1UsersMeSubscriptionsPost**](docs/MySubscriptionsApi.md#apiV1UsersMeSubscriptionsPost) | **POST** /api/v1/users/me/subscriptions | Add subscription to my user
*PeerTube.MySubscriptionsApi* | [**apiV1UsersMeSubscriptionsSubscriptionHandleDelete**](docs/MySubscriptionsApi.md#apiV1UsersMeSubscriptionsSubscriptionHandleDelete) | **DELETE** /api/v1/users/me/subscriptions/{subscriptionHandle} | Delete subscription of my user
*PeerTube.MySubscriptionsApi* | [**apiV1UsersMeSubscriptionsSubscriptionHandleGet**](docs/MySubscriptionsApi.md#apiV1UsersMeSubscriptionsSubscriptionHandleGet) | **GET** /api/v1/users/me/subscriptions/{subscriptionHandle} | Get subscription of my user
*PeerTube.MySubscriptionsApi* | [**apiV1UsersMeSubscriptionsVideosGet**](docs/MySubscriptionsApi.md#apiV1UsersMeSubscriptionsVideosGet) | **GET** /api/v1/users/me/subscriptions/videos | List videos of subscriptions of my user
*PeerTube.MyUserApi* | [**apiV1UsersMeAvatarDelete**](docs/MyUserApi.md#apiV1UsersMeAvatarDelete) | **DELETE** /api/v1/users/me/avatar | Delete my avatar
*PeerTube.MyUserApi* | [**apiV1UsersMeAvatarPickPost**](docs/MyUserApi.md#apiV1UsersMeAvatarPickPost) | **POST** /api/v1/users/me/avatar/pick | Update my user avatar
*PeerTube.MyUserApi* | [**apiV1UsersMeVideoQuotaUsedGet**](docs/MyUserApi.md#apiV1UsersMeVideoQuotaUsedGet) | **GET** /api/v1/users/me/video-quota-used | Get my user used quota
*PeerTube.MyUserApi* | [**apiV1UsersMeVideosGet**](docs/MyUserApi.md#apiV1UsersMeVideosGet) | **GET** /api/v1/users/me/videos | Get videos of my user
*PeerTube.MyUserApi* | [**apiV1UsersMeVideosImportsGet_0**](docs/MyUserApi.md#apiV1UsersMeVideosImportsGet_0) | **GET** /api/v1/users/me/videos/imports | Get video imports of my user
*PeerTube.MyUserApi* | [**apiV1UsersMeVideosVideoIdRatingGet**](docs/MyUserApi.md#apiV1UsersMeVideosVideoIdRatingGet) | **GET** /api/v1/users/me/videos/{videoId}/rating | Get rate of my user for a video
*PeerTube.MyUserApi* | [**getMyAbuses_0**](docs/MyUserApi.md#getMyAbuses_0) | **GET** /api/v1/users/me/abuses | List my abuses
*PeerTube.MyUserApi* | [**getUserInfo**](docs/MyUserApi.md#getUserInfo) | **GET** /api/v1/users/me | Get my user information
*PeerTube.MyUserApi* | [**putUserInfo**](docs/MyUserApi.md#putUserInfo) | **PUT** /api/v1/users/me | Update my user information
*PeerTube.PluginsApi* | [**addPlugin**](docs/PluginsApi.md#addPlugin) | **POST** /api/v1/plugins/install | Install a plugin
*PeerTube.PluginsApi* | [**apiV1PluginsNpmNamePublicSettingsGet**](docs/PluginsApi.md#apiV1PluginsNpmNamePublicSettingsGet) | **GET** /api/v1/plugins/{npmName}/public-settings | Get a plugin&#39;s public settings
*PeerTube.PluginsApi* | [**apiV1PluginsNpmNameRegisteredSettingsGet**](docs/PluginsApi.md#apiV1PluginsNpmNameRegisteredSettingsGet) | **GET** /api/v1/plugins/{npmName}/registered-settings | Get a plugin&#39;s registered settings
*PeerTube.PluginsApi* | [**apiV1PluginsNpmNameSettingsPut**](docs/PluginsApi.md#apiV1PluginsNpmNameSettingsPut) | **PUT** /api/v1/plugins/{npmName}/settings | Set a plugin&#39;s settings
*PeerTube.PluginsApi* | [**getAvailablePlugins**](docs/PluginsApi.md#getAvailablePlugins) | **GET** /api/v1/plugins/available | List available plugins
*PeerTube.PluginsApi* | [**getPlugin**](docs/PluginsApi.md#getPlugin) | **GET** /api/v1/plugins/{npmName} | Get a plugin
*PeerTube.PluginsApi* | [**getPlugins**](docs/PluginsApi.md#getPlugins) | **GET** /api/v1/plugins | List plugins
*PeerTube.PluginsApi* | [**uninstallPlugin**](docs/PluginsApi.md#uninstallPlugin) | **POST** /api/v1/plugins/uninstall | Uninstall a plugin
*PeerTube.PluginsApi* | [**updatePlugin**](docs/PluginsApi.md#updatePlugin) | **POST** /api/v1/plugins/update | Update a plugin
*PeerTube.RegisterApi* | [**acceptRegistration**](docs/RegisterApi.md#acceptRegistration) | **POST** /api/v1/users/registrations/{registrationId}/accept | Accept registration
*PeerTube.RegisterApi* | [**deleteRegistration**](docs/RegisterApi.md#deleteRegistration) | **DELETE** /api/v1/users/registrations/{registrationId} | Delete registration
*PeerTube.RegisterApi* | [**listRegistrations**](docs/RegisterApi.md#listRegistrations) | **GET** /api/v1/users/registrations | List registrations
*PeerTube.RegisterApi* | [**registerUser**](docs/RegisterApi.md#registerUser) | **POST** /api/v1/users/register | Register a user
*PeerTube.RegisterApi* | [**rejectRegistration**](docs/RegisterApi.md#rejectRegistration) | **POST** /api/v1/users/registrations/{registrationId}/reject | Reject registration
*PeerTube.RegisterApi* | [**requestRegistration**](docs/RegisterApi.md#requestRegistration) | **POST** /api/v1/users/registrations/request | Request registration
*PeerTube.RegisterApi* | [**resendEmailToVerifyRegistration**](docs/RegisterApi.md#resendEmailToVerifyRegistration) | **POST** /api/v1/users/registrations/ask-send-verify-email | Resend verification link to registration email
*PeerTube.RegisterApi* | [**resendEmailToVerifyUser_0**](docs/RegisterApi.md#resendEmailToVerifyUser_0) | **POST** /api/v1/users/ask-send-verify-email | Resend user verification link
*PeerTube.RegisterApi* | [**verifyRegistrationEmail**](docs/RegisterApi.md#verifyRegistrationEmail) | **POST** /api/v1/users/registrations/{registrationId}/verify-email | Verify a registration email
*PeerTube.RegisterApi* | [**verifyUser_0**](docs/RegisterApi.md#verifyUser_0) | **POST** /api/v1/users/{id}/verify-email | Verify a user
*PeerTube.SearchApi* | [**searchChannels**](docs/SearchApi.md#searchChannels) | **GET** /api/v1/search/video-channels | Search channels
*PeerTube.SearchApi* | [**searchPlaylists**](docs/SearchApi.md#searchPlaylists) | **GET** /api/v1/search/video-playlists | Search playlists
*PeerTube.SearchApi* | [**searchVideos**](docs/SearchApi.md#searchVideos) | **GET** /api/v1/search/videos | Search videos
*PeerTube.ServerBlocksApi* | [**apiV1BlocklistStatusGet_0**](docs/ServerBlocksApi.md#apiV1BlocklistStatusGet_0) | **GET** /api/v1/blocklist/status | Get block status of accounts/hosts
*PeerTube.ServerBlocksApi* | [**apiV1ServerBlocklistServersGet**](docs/ServerBlocksApi.md#apiV1ServerBlocklistServersGet) | **GET** /api/v1/server/blocklist/servers | List server blocks
*PeerTube.ServerBlocksApi* | [**apiV1ServerBlocklistServersHostDelete**](docs/ServerBlocksApi.md#apiV1ServerBlocklistServersHostDelete) | **DELETE** /api/v1/server/blocklist/servers/{host} | Unblock a server by its domain
*PeerTube.ServerBlocksApi* | [**apiV1ServerBlocklistServersPost**](docs/ServerBlocksApi.md#apiV1ServerBlocklistServersPost) | **POST** /api/v1/server/blocklist/servers | Block a server
*PeerTube.SessionApi* | [**getOAuthClient**](docs/SessionApi.md#getOAuthClient) | **GET** /api/v1/oauth-clients/local | Login prerequisite
*PeerTube.SessionApi* | [**getOAuthToken**](docs/SessionApi.md#getOAuthToken) | **POST** /api/v1/users/token | Login
*PeerTube.SessionApi* | [**revokeOAuthToken**](docs/SessionApi.md#revokeOAuthToken) | **POST** /api/v1/users/revoke-token | Logout
*PeerTube.StaticVideoFilesApi* | [**staticStreamingPlaylistsHlsFilenameGet**](docs/StaticVideoFilesApi.md#staticStreamingPlaylistsHlsFilenameGet) | **GET** /static/streaming-playlists/hls/{filename} | Get public HLS video file
*PeerTube.StaticVideoFilesApi* | [**staticStreamingPlaylistsHlsPrivateFilenameGet**](docs/StaticVideoFilesApi.md#staticStreamingPlaylistsHlsPrivateFilenameGet) | **GET** /static/streaming-playlists/hls/private/{filename} | Get private HLS video file
*PeerTube.StaticVideoFilesApi* | [**staticWebseedFilenameGet**](docs/StaticVideoFilesApi.md#staticWebseedFilenameGet) | **GET** /static/webseed/{filename} | Get public WebTorrent video file
*PeerTube.StaticVideoFilesApi* | [**staticWebseedPrivateFilenameGet**](docs/StaticVideoFilesApi.md#staticWebseedPrivateFilenameGet) | **GET** /static/webseed/private/{filename} | Get private WebTorrent video file
*PeerTube.StatsApi* | [**apiV1MetricsPlaybackPost**](docs/StatsApi.md#apiV1MetricsPlaybackPost) | **POST** /api/v1/metrics/playback | Create playback metrics
*PeerTube.StatsApi* | [**getInstanceStats**](docs/StatsApi.md#getInstanceStats) | **GET** /api/v1/server/stats | Get instance stats
*PeerTube.UsersApi* | [**addUser**](docs/UsersApi.md#addUser) | **POST** /api/v1/users | Create a user
*PeerTube.UsersApi* | [**confirmTwoFactorRequest**](docs/UsersApi.md#confirmTwoFactorRequest) | **POST** /api/v1/users/{id}/two-factor/confirm-request | Confirm two factor auth
*PeerTube.UsersApi* | [**delUser**](docs/UsersApi.md#delUser) | **DELETE** /api/v1/users/{id} | Delete a user
*PeerTube.UsersApi* | [**disableTwoFactor**](docs/UsersApi.md#disableTwoFactor) | **POST** /api/v1/users/{id}/two-factor/disable | Disable two factor auth
*PeerTube.UsersApi* | [**getUser**](docs/UsersApi.md#getUser) | **GET** /api/v1/users/{id} | Get a user
*PeerTube.UsersApi* | [**getUsers**](docs/UsersApi.md#getUsers) | **GET** /api/v1/users | List users
*PeerTube.UsersApi* | [**putUser**](docs/UsersApi.md#putUser) | **PUT** /api/v1/users/{id} | Update a user
*PeerTube.UsersApi* | [**requestTwoFactor**](docs/UsersApi.md#requestTwoFactor) | **POST** /api/v1/users/{id}/two-factor/request | Request two factor auth
*PeerTube.UsersApi* | [**resendEmailToVerifyUser**](docs/UsersApi.md#resendEmailToVerifyUser) | **POST** /api/v1/users/ask-send-verify-email | Resend user verification link
*PeerTube.UsersApi* | [**verifyUser**](docs/UsersApi.md#verifyUser) | **POST** /api/v1/users/{id}/verify-email | Verify a user
*PeerTube.VideoApi* | [**addLive_0**](docs/VideoApi.md#addLive_0) | **POST** /api/v1/videos/live | Create a live
*PeerTube.VideoApi* | [**addView**](docs/VideoApi.md#addView) | **POST** /api/v1/videos/{id}/views | Notify user is watching a video
*PeerTube.VideoApi* | [**apiV1VideosIdStudioEditPost_0**](docs/VideoApi.md#apiV1VideosIdStudioEditPost_0) | **POST** /api/v1/videos/{id}/studio/edit | Create a studio task
*PeerTube.VideoApi* | [**apiV1VideosIdWatchingPut**](docs/VideoApi.md#apiV1VideosIdWatchingPut) | **PUT** /api/v1/videos/{id}/watching | Set watching progress of a video
*PeerTube.VideoApi* | [**delVideo**](docs/VideoApi.md#delVideo) | **DELETE** /api/v1/videos/{id} | Delete a video
*PeerTube.VideoApi* | [**getAccountVideos_0**](docs/VideoApi.md#getAccountVideos_0) | **GET** /api/v1/accounts/{name}/videos | List videos of an account
*PeerTube.VideoApi* | [**getCategories**](docs/VideoApi.md#getCategories) | **GET** /api/v1/videos/categories | List available video categories
*PeerTube.VideoApi* | [**getLanguages**](docs/VideoApi.md#getLanguages) | **GET** /api/v1/videos/languages | List available video languages
*PeerTube.VideoApi* | [**getLicences**](docs/VideoApi.md#getLicences) | **GET** /api/v1/videos/licences | List available video licences
*PeerTube.VideoApi* | [**getLiveId_0**](docs/VideoApi.md#getLiveId_0) | **GET** /api/v1/videos/live/{id} | Get information about a live
*PeerTube.VideoApi* | [**getVideo**](docs/VideoApi.md#getVideo) | **GET** /api/v1/videos/{id} | Get a video
*PeerTube.VideoApi* | [**getVideoChannelVideos**](docs/VideoApi.md#getVideoChannelVideos) | **GET** /api/v1/video-channels/{channelHandle}/videos | List videos of a video channel
*PeerTube.VideoApi* | [**getVideoDesc**](docs/VideoApi.md#getVideoDesc) | **GET** /api/v1/videos/{id}/description | Get complete video description
*PeerTube.VideoApi* | [**getVideoPrivacyPolicies**](docs/VideoApi.md#getVideoPrivacyPolicies) | **GET** /api/v1/videos/privacies | List available video privacy policies
*PeerTube.VideoApi* | [**getVideoSource**](docs/VideoApi.md#getVideoSource) | **POST** /api/v1/videos/{id}/source | Get video source file metadata
*PeerTube.VideoApi* | [**getVideos**](docs/VideoApi.md#getVideos) | **GET** /api/v1/videos | List videos
*PeerTube.VideoApi* | [**putVideo**](docs/VideoApi.md#putVideo) | **PUT** /api/v1/videos/{id} | Update a video
*PeerTube.VideoApi* | [**requestVideoToken**](docs/VideoApi.md#requestVideoToken) | **POST** /api/v1/videos/{id}/token | Request video token
*PeerTube.VideoApi* | [**updateLiveId_0**](docs/VideoApi.md#updateLiveId_0) | **PUT** /api/v1/videos/live/{id} | Update information about a live
*PeerTube.VideoApi* | [**uploadLegacy**](docs/VideoApi.md#uploadLegacy) | **POST** /api/v1/videos/upload | Upload a video
*PeerTube.VideoApi* | [**uploadResumable**](docs/VideoApi.md#uploadResumable) | **PUT** /api/v1/videos/upload-resumable | Send chunk for the resumable upload of a video
*PeerTube.VideoApi* | [**uploadResumableCancel**](docs/VideoApi.md#uploadResumableCancel) | **DELETE** /api/v1/videos/upload-resumable | Cancel the resumable upload of a video, deleting any data uploaded so far
*PeerTube.VideoApi* | [**uploadResumableInit**](docs/VideoApi.md#uploadResumableInit) | **POST** /api/v1/videos/upload-resumable | Initialize the resumable upload of a video
*PeerTube.VideoBlocksApi* | [**addVideoBlock**](docs/VideoBlocksApi.md#addVideoBlock) | **POST** /api/v1/videos/{id}/blacklist | Block a video
*PeerTube.VideoBlocksApi* | [**delVideoBlock**](docs/VideoBlocksApi.md#delVideoBlock) | **DELETE** /api/v1/videos/{id}/blacklist | Unblock a video by its id
*PeerTube.VideoBlocksApi* | [**getVideoBlocks**](docs/VideoBlocksApi.md#getVideoBlocks) | **GET** /api/v1/videos/blacklist | List video blocks
*PeerTube.VideoCaptionsApi* | [**addVideoCaption**](docs/VideoCaptionsApi.md#addVideoCaption) | **PUT** /api/v1/videos/{id}/captions/{captionLanguage} | Add or replace a video caption
*PeerTube.VideoCaptionsApi* | [**delVideoCaption**](docs/VideoCaptionsApi.md#delVideoCaption) | **DELETE** /api/v1/videos/{id}/captions/{captionLanguage} | Delete a video caption
*PeerTube.VideoCaptionsApi* | [**getVideoCaptions**](docs/VideoCaptionsApi.md#getVideoCaptions) | **GET** /api/v1/videos/{id}/captions | List captions of a video
*PeerTube.VideoChannelsApi* | [**addVideoChannel**](docs/VideoChannelsApi.md#addVideoChannel) | **POST** /api/v1/video-channels | Create a video channel
*PeerTube.VideoChannelsApi* | [**apiV1AccountsNameVideoChannelSyncsGet**](docs/VideoChannelsApi.md#apiV1AccountsNameVideoChannelSyncsGet) | **GET** /api/v1/accounts/{name}/video-channel-syncs | List the synchronizations of video channels of an account
*PeerTube.VideoChannelsApi* | [**apiV1AccountsNameVideoChannelsGet**](docs/VideoChannelsApi.md#apiV1AccountsNameVideoChannelsGet) | **GET** /api/v1/accounts/{name}/video-channels | List video channels of an account
*PeerTube.VideoChannelsApi* | [**apiV1VideoChannelsChannelHandleAvatarDelete**](docs/VideoChannelsApi.md#apiV1VideoChannelsChannelHandleAvatarDelete) | **DELETE** /api/v1/video-channels/{channelHandle}/avatar | Delete channel avatar
*PeerTube.VideoChannelsApi* | [**apiV1VideoChannelsChannelHandleAvatarPickPost**](docs/VideoChannelsApi.md#apiV1VideoChannelsChannelHandleAvatarPickPost) | **POST** /api/v1/video-channels/{channelHandle}/avatar/pick | Update channel avatar
*PeerTube.VideoChannelsApi* | [**apiV1VideoChannelsChannelHandleBannerDelete**](docs/VideoChannelsApi.md#apiV1VideoChannelsChannelHandleBannerDelete) | **DELETE** /api/v1/video-channels/{channelHandle}/banner | Delete channel banner
*PeerTube.VideoChannelsApi* | [**apiV1VideoChannelsChannelHandleBannerPickPost**](docs/VideoChannelsApi.md#apiV1VideoChannelsChannelHandleBannerPickPost) | **POST** /api/v1/video-channels/{channelHandle}/banner/pick | Update channel banner
*PeerTube.VideoChannelsApi* | [**apiV1VideoChannelsChannelHandleImportVideosPost**](docs/VideoChannelsApi.md#apiV1VideoChannelsChannelHandleImportVideosPost) | **POST** /api/v1/video-channels/{channelHandle}/import-videos | Import videos in channel
*PeerTube.VideoChannelsApi* | [**apiV1VideoChannelsChannelHandleVideoPlaylistsGet_0**](docs/VideoChannelsApi.md#apiV1VideoChannelsChannelHandleVideoPlaylistsGet_0) | **GET** /api/v1/video-channels/{channelHandle}/video-playlists | List playlists of a channel
*PeerTube.VideoChannelsApi* | [**delVideoChannel**](docs/VideoChannelsApi.md#delVideoChannel) | **DELETE** /api/v1/video-channels/{channelHandle} | Delete a video channel
*PeerTube.VideoChannelsApi* | [**getVideoChannel**](docs/VideoChannelsApi.md#getVideoChannel) | **GET** /api/v1/video-channels/{channelHandle} | Get a video channel
*PeerTube.VideoChannelsApi* | [**getVideoChannelFollowers**](docs/VideoChannelsApi.md#getVideoChannelFollowers) | **GET** /api/v1/video-channels/{channelHandle}/followers | List followers of a video channel
*PeerTube.VideoChannelsApi* | [**getVideoChannelVideos_0**](docs/VideoChannelsApi.md#getVideoChannelVideos_0) | **GET** /api/v1/video-channels/{channelHandle}/videos | List videos of a video channel
*PeerTube.VideoChannelsApi* | [**getVideoChannels**](docs/VideoChannelsApi.md#getVideoChannels) | **GET** /api/v1/video-channels | List video channels
*PeerTube.VideoChannelsApi* | [**putVideoChannel**](docs/VideoChannelsApi.md#putVideoChannel) | **PUT** /api/v1/video-channels/{channelHandle} | Update a video channel
*PeerTube.VideoCommentsApi* | [**apiV1VideosIdCommentThreadsGet**](docs/VideoCommentsApi.md#apiV1VideosIdCommentThreadsGet) | **GET** /api/v1/videos/{id}/comment-threads | List threads of a video
*PeerTube.VideoCommentsApi* | [**apiV1VideosIdCommentThreadsPost**](docs/VideoCommentsApi.md#apiV1VideosIdCommentThreadsPost) | **POST** /api/v1/videos/{id}/comment-threads | Create a thread
*PeerTube.VideoCommentsApi* | [**apiV1VideosIdCommentThreadsThreadIdGet**](docs/VideoCommentsApi.md#apiV1VideosIdCommentThreadsThreadIdGet) | **GET** /api/v1/videos/{id}/comment-threads/{threadId} | Get a thread
*PeerTube.VideoCommentsApi* | [**apiV1VideosIdCommentsCommentIdDelete**](docs/VideoCommentsApi.md#apiV1VideosIdCommentsCommentIdDelete) | **DELETE** /api/v1/videos/{id}/comments/{commentId} | Delete a comment or a reply
*PeerTube.VideoCommentsApi* | [**apiV1VideosIdCommentsCommentIdPost**](docs/VideoCommentsApi.md#apiV1VideosIdCommentsCommentIdPost) | **POST** /api/v1/videos/{id}/comments/{commentId} | Reply to a thread of a video
*PeerTube.VideoFeedsApi* | [**getSyndicatedComments**](docs/VideoFeedsApi.md#getSyndicatedComments) | **GET** /feeds/video-comments.{format} | List comments on videos
*PeerTube.VideoFeedsApi* | [**getSyndicatedSubscriptionVideos**](docs/VideoFeedsApi.md#getSyndicatedSubscriptionVideos) | **GET** /feeds/subscriptions.{format} | List videos of subscriptions tied to a token
*PeerTube.VideoFeedsApi* | [**getSyndicatedVideos**](docs/VideoFeedsApi.md#getSyndicatedVideos) | **GET** /feeds/videos.{format} | List videos
*PeerTube.VideoFilesApi* | [**delVideoHLS**](docs/VideoFilesApi.md#delVideoHLS) | **DELETE** /api/v1/videos/{id}/hls | Delete video HLS files
*PeerTube.VideoFilesApi* | [**delVideoWebTorrent**](docs/VideoFilesApi.md#delVideoWebTorrent) | **DELETE** /api/v1/videos/{id}/webtorrent | Delete video WebTorrent files
*PeerTube.VideoImportsApi* | [**apiV1VideosImportsIdCancelPost**](docs/VideoImportsApi.md#apiV1VideosImportsIdCancelPost) | **POST** /api/v1/videos/imports/{id}/cancel | Cancel video import
*PeerTube.VideoImportsApi* | [**apiV1VideosImportsIdDelete**](docs/VideoImportsApi.md#apiV1VideosImportsIdDelete) | **DELETE** /api/v1/videos/imports/{id} | Delete video import
*PeerTube.VideoImportsApi* | [**importVideo**](docs/VideoImportsApi.md#importVideo) | **POST** /api/v1/videos/imports | Import a video
*PeerTube.VideoMirroringApi* | [**delMirroredVideo**](docs/VideoMirroringApi.md#delMirroredVideo) | **DELETE** /api/v1/server/redundancy/videos/{redundancyId} | Delete a mirror done on a video
*PeerTube.VideoMirroringApi* | [**getMirroredVideos**](docs/VideoMirroringApi.md#getMirroredVideos) | **GET** /api/v1/server/redundancy/videos | List videos being mirrored
*PeerTube.VideoMirroringApi* | [**putMirroredVideo**](docs/VideoMirroringApi.md#putMirroredVideo) | **POST** /api/v1/server/redundancy/videos | Mirror a video
*PeerTube.VideoOwnershipChangeApi* | [**apiV1VideosIdGiveOwnershipPost**](docs/VideoOwnershipChangeApi.md#apiV1VideosIdGiveOwnershipPost) | **POST** /api/v1/videos/{id}/give-ownership | Request ownership change
*PeerTube.VideoOwnershipChangeApi* | [**apiV1VideosOwnershipGet**](docs/VideoOwnershipChangeApi.md#apiV1VideosOwnershipGet) | **GET** /api/v1/videos/ownership | List video ownership changes
*PeerTube.VideoOwnershipChangeApi* | [**apiV1VideosOwnershipIdAcceptPost**](docs/VideoOwnershipChangeApi.md#apiV1VideosOwnershipIdAcceptPost) | **POST** /api/v1/videos/ownership/{id}/accept | Accept ownership change request
*PeerTube.VideoOwnershipChangeApi* | [**apiV1VideosOwnershipIdRefusePost**](docs/VideoOwnershipChangeApi.md#apiV1VideosOwnershipIdRefusePost) | **POST** /api/v1/videos/ownership/{id}/refuse | Refuse ownership change request
*PeerTube.VideoPlaylistsApi* | [**addPlaylist**](docs/VideoPlaylistsApi.md#addPlaylist) | **POST** /api/v1/video-playlists | Create a video playlist
*PeerTube.VideoPlaylistsApi* | [**addVideoPlaylistVideo_0**](docs/VideoPlaylistsApi.md#addVideoPlaylistVideo_0) | **POST** /api/v1/video-playlists/{playlistId}/videos | Add a video in a playlist
*PeerTube.VideoPlaylistsApi* | [**apiV1AccountsNameVideoPlaylistsGet**](docs/VideoPlaylistsApi.md#apiV1AccountsNameVideoPlaylistsGet) | **GET** /api/v1/accounts/{name}/video-playlists | List playlists of an account
*PeerTube.VideoPlaylistsApi* | [**apiV1UsersMeVideoPlaylistsVideosExistGet**](docs/VideoPlaylistsApi.md#apiV1UsersMeVideoPlaylistsVideosExistGet) | **GET** /api/v1/users/me/video-playlists/videos-exist | Check video exists in my playlists
*PeerTube.VideoPlaylistsApi* | [**apiV1VideoChannelsChannelHandleVideoPlaylistsGet**](docs/VideoPlaylistsApi.md#apiV1VideoChannelsChannelHandleVideoPlaylistsGet) | **GET** /api/v1/video-channels/{channelHandle}/video-playlists | List playlists of a channel
*PeerTube.VideoPlaylistsApi* | [**apiV1VideoPlaylistsPlaylistIdDelete**](docs/VideoPlaylistsApi.md#apiV1VideoPlaylistsPlaylistIdDelete) | **DELETE** /api/v1/video-playlists/{playlistId} | Delete a video playlist
*PeerTube.VideoPlaylistsApi* | [**apiV1VideoPlaylistsPlaylistIdGet**](docs/VideoPlaylistsApi.md#apiV1VideoPlaylistsPlaylistIdGet) | **GET** /api/v1/video-playlists/{playlistId} | Get a video playlist
*PeerTube.VideoPlaylistsApi* | [**apiV1VideoPlaylistsPlaylistIdPut**](docs/VideoPlaylistsApi.md#apiV1VideoPlaylistsPlaylistIdPut) | **PUT** /api/v1/video-playlists/{playlistId} | Update a video playlist
*PeerTube.VideoPlaylistsApi* | [**delVideoPlaylistVideo**](docs/VideoPlaylistsApi.md#delVideoPlaylistVideo) | **DELETE** /api/v1/video-playlists/{playlistId}/videos/{playlistElementId} | Delete an element from a playlist
*PeerTube.VideoPlaylistsApi* | [**getPlaylistPrivacyPolicies**](docs/VideoPlaylistsApi.md#getPlaylistPrivacyPolicies) | **GET** /api/v1/video-playlists/privacies | List available playlist privacy policies
*PeerTube.VideoPlaylistsApi* | [**getPlaylists**](docs/VideoPlaylistsApi.md#getPlaylists) | **GET** /api/v1/video-playlists | List video playlists
*PeerTube.VideoPlaylistsApi* | [**getVideoPlaylistVideos_0**](docs/VideoPlaylistsApi.md#getVideoPlaylistVideos_0) | **GET** /api/v1/video-playlists/{playlistId}/videos | List videos of a playlist
*PeerTube.VideoPlaylistsApi* | [**putVideoPlaylistVideo**](docs/VideoPlaylistsApi.md#putVideoPlaylistVideo) | **PUT** /api/v1/video-playlists/{playlistId}/videos/{playlistElementId} | Update a playlist element
*PeerTube.VideoPlaylistsApi* | [**reorderVideoPlaylist**](docs/VideoPlaylistsApi.md#reorderVideoPlaylist) | **POST** /api/v1/video-playlists/{playlistId}/videos/reorder | Reorder a playlist
*PeerTube.VideoRatesApi* | [**apiV1UsersMeVideosVideoIdRatingGet_0**](docs/VideoRatesApi.md#apiV1UsersMeVideosVideoIdRatingGet_0) | **GET** /api/v1/users/me/videos/{videoId}/rating | Get rate of my user for a video
*PeerTube.VideoRatesApi* | [**apiV1VideosIdRatePut**](docs/VideoRatesApi.md#apiV1VideosIdRatePut) | **PUT** /api/v1/videos/{id}/rate | Like/dislike a video
*PeerTube.VideoStatsApi* | [**apiV1VideosIdStatsOverallGet**](docs/VideoStatsApi.md#apiV1VideosIdStatsOverallGet) | **GET** /api/v1/videos/{id}/stats/overall | Get overall stats of a video
*PeerTube.VideoStatsApi* | [**apiV1VideosIdStatsRetentionGet**](docs/VideoStatsApi.md#apiV1VideosIdStatsRetentionGet) | **GET** /api/v1/videos/{id}/stats/retention | Get retention stats of a video
*PeerTube.VideoStatsApi* | [**apiV1VideosIdStatsTimeseriesMetricGet**](docs/VideoStatsApi.md#apiV1VideosIdStatsTimeseriesMetricGet) | **GET** /api/v1/videos/{id}/stats/timeseries/{metric} | Get timeserie stats of a video
*PeerTube.VideoTranscodingApi* | [**apiV1VideosIdStudioEditPost**](docs/VideoTranscodingApi.md#apiV1VideosIdStudioEditPost) | **POST** /api/v1/videos/{id}/studio/edit | Create a studio task
*PeerTube.VideoTranscodingApi* | [**createVideoTranscoding**](docs/VideoTranscodingApi.md#createVideoTranscoding) | **POST** /api/v1/videos/{id}/transcoding | Create a transcoding job
*PeerTube.VideoUploadApi* | [**importVideo_0**](docs/VideoUploadApi.md#importVideo_0) | **POST** /api/v1/videos/imports | Import a video
*PeerTube.VideoUploadApi* | [**uploadLegacy_0**](docs/VideoUploadApi.md#uploadLegacy_0) | **POST** /api/v1/videos/upload | Upload a video
*PeerTube.VideoUploadApi* | [**uploadResumableCancel_0**](docs/VideoUploadApi.md#uploadResumableCancel_0) | **DELETE** /api/v1/videos/upload-resumable | Cancel the resumable upload of a video, deleting any data uploaded so far
*PeerTube.VideoUploadApi* | [**uploadResumableInit_0**](docs/VideoUploadApi.md#uploadResumableInit_0) | **POST** /api/v1/videos/upload-resumable | Initialize the resumable upload of a video
*PeerTube.VideoUploadApi* | [**uploadResumable_0**](docs/VideoUploadApi.md#uploadResumable_0) | **PUT** /api/v1/videos/upload-resumable | Send chunk for the resumable upload of a video
*PeerTube.VideosApi* | [**addVideoPlaylistVideo**](docs/VideosApi.md#addVideoPlaylistVideo) | **POST** /api/v1/video-playlists/{playlistId}/videos | Add a video in a playlist
*PeerTube.VideosApi* | [**apiV1UsersMeSubscriptionsVideosGet_0**](docs/VideosApi.md#apiV1UsersMeSubscriptionsVideosGet_0) | **GET** /api/v1/users/me/subscriptions/videos | List videos of subscriptions of my user
*PeerTube.VideosApi* | [**apiV1UsersMeVideosGet_0**](docs/VideosApi.md#apiV1UsersMeVideosGet_0) | **GET** /api/v1/users/me/videos | Get videos of my user
*PeerTube.VideosApi* | [**apiV1UsersMeVideosImportsGet**](docs/VideosApi.md#apiV1UsersMeVideosImportsGet) | **GET** /api/v1/users/me/videos/imports | Get video imports of my user
*PeerTube.VideosApi* | [**getVideoPlaylistVideos**](docs/VideosApi.md#getVideoPlaylistVideos) | **GET** /api/v1/video-playlists/{playlistId}/videos | List videos of a playlist


## Documentation for Models

 - [PeerTube.Abuse](docs/Abuse.md)
 - [PeerTube.AbuseMessage](docs/AbuseMessage.md)
 - [PeerTube.AbuseStateConstant](docs/AbuseStateConstant.md)
 - [PeerTube.AbuseStateSet](docs/AbuseStateSet.md)
 - [PeerTube.Account](docs/Account.md)
 - [PeerTube.AccountSummary](docs/AccountSummary.md)
 - [PeerTube.Actor](docs/Actor.md)
 - [PeerTube.ActorImage](docs/ActorImage.md)
 - [PeerTube.ActorInfo](docs/ActorInfo.md)
 - [PeerTube.AddIntroOptions](docs/AddIntroOptions.md)
 - [PeerTube.AddPlaylist200Response](docs/AddPlaylist200Response.md)
 - [PeerTube.AddPlaylist200ResponseVideoPlaylist](docs/AddPlaylist200ResponseVideoPlaylist.md)
 - [PeerTube.AddPluginRequest](docs/AddPluginRequest.md)
 - [PeerTube.AddPluginRequestOneOf](docs/AddPluginRequestOneOf.md)
 - [PeerTube.AddPluginRequestOneOf1](docs/AddPluginRequestOneOf1.md)
 - [PeerTube.AddUser](docs/AddUser.md)
 - [PeerTube.AddUserResponse](docs/AddUserResponse.md)
 - [PeerTube.AddUserResponseUser](docs/AddUserResponseUser.md)
 - [PeerTube.AddVideoChannel200Response](docs/AddVideoChannel200Response.md)
 - [PeerTube.AddVideoChannelSync200Response](docs/AddVideoChannelSync200Response.md)
 - [PeerTube.AddVideoPlaylistVideo200Response](docs/AddVideoPlaylistVideo200Response.md)
 - [PeerTube.AddVideoPlaylistVideo200ResponseVideoPlaylistElement](docs/AddVideoPlaylistVideo200ResponseVideoPlaylistElement.md)
 - [PeerTube.AddVideoPlaylistVideoRequest](docs/AddVideoPlaylistVideoRequest.md)
 - [PeerTube.AddVideoPlaylistVideoRequestVideoId](docs/AddVideoPlaylistVideoRequestVideoId.md)
 - [PeerTube.ApiV1AbusesAbuseIdMessagesGet200Response](docs/ApiV1AbusesAbuseIdMessagesGet200Response.md)
 - [PeerTube.ApiV1AbusesAbuseIdMessagesPostRequest](docs/ApiV1AbusesAbuseIdMessagesPostRequest.md)
 - [PeerTube.ApiV1AbusesAbuseIdPutRequest](docs/ApiV1AbusesAbuseIdPutRequest.md)
 - [PeerTube.ApiV1AbusesPost200Response](docs/ApiV1AbusesPost200Response.md)
 - [PeerTube.ApiV1AbusesPost200ResponseAbuse](docs/ApiV1AbusesPost200ResponseAbuse.md)
 - [PeerTube.ApiV1AbusesPostRequest](docs/ApiV1AbusesPostRequest.md)
 - [PeerTube.ApiV1AbusesPostRequestAccount](docs/ApiV1AbusesPostRequestAccount.md)
 - [PeerTube.ApiV1AbusesPostRequestComment](docs/ApiV1AbusesPostRequestComment.md)
 - [PeerTube.ApiV1AbusesPostRequestVideo](docs/ApiV1AbusesPostRequestVideo.md)
 - [PeerTube.ApiV1AccountsNameVideoPlaylistsGet200Response](docs/ApiV1AccountsNameVideoPlaylistsGet200Response.md)
 - [PeerTube.ApiV1CustomPagesHomepageInstancePutRequest](docs/ApiV1CustomPagesHomepageInstancePutRequest.md)
 - [PeerTube.ApiV1PluginsNpmNameSettingsPutRequest](docs/ApiV1PluginsNpmNameSettingsPutRequest.md)
 - [PeerTube.ApiV1ServerBlocklistAccountsPostRequest](docs/ApiV1ServerBlocklistAccountsPostRequest.md)
 - [PeerTube.ApiV1ServerBlocklistServersPostRequest](docs/ApiV1ServerBlocklistServersPostRequest.md)
 - [PeerTube.ApiV1ServerFollowingPostRequest](docs/ApiV1ServerFollowingPostRequest.md)
 - [PeerTube.ApiV1ServerRedundancyHostPutRequest](docs/ApiV1ServerRedundancyHostPutRequest.md)
 - [PeerTube.ApiV1UsersMeAvatarPickPost200Response](docs/ApiV1UsersMeAvatarPickPost200Response.md)
 - [PeerTube.ApiV1UsersMeNotificationSettingsPutRequest](docs/ApiV1UsersMeNotificationSettingsPutRequest.md)
 - [PeerTube.ApiV1UsersMeNotificationsReadPostRequest](docs/ApiV1UsersMeNotificationsReadPostRequest.md)
 - [PeerTube.ApiV1UsersMeSubscriptionsPostRequest](docs/ApiV1UsersMeSubscriptionsPostRequest.md)
 - [PeerTube.ApiV1UsersMeVideoPlaylistsVideosExistGet200Response](docs/ApiV1UsersMeVideoPlaylistsVideosExistGet200Response.md)
 - [PeerTube.ApiV1UsersMeVideoPlaylistsVideosExistGet200ResponseVideoIdInner](docs/ApiV1UsersMeVideoPlaylistsVideosExistGet200ResponseVideoIdInner.md)
 - [PeerTube.ApiV1UsersMeVideoQuotaUsedGet200Response](docs/ApiV1UsersMeVideoQuotaUsedGet200Response.md)
 - [PeerTube.ApiV1VideoChannelsChannelHandleBannerPickPost200Response](docs/ApiV1VideoChannelsChannelHandleBannerPickPost200Response.md)
 - [PeerTube.ApiV1VideosIdCommentThreadsPostRequest](docs/ApiV1VideosIdCommentThreadsPostRequest.md)
 - [PeerTube.ApiV1VideosIdRatePutRequest](docs/ApiV1VideosIdRatePutRequest.md)
 - [PeerTube.ApiV1VideosLiveIdSessionsGet200Response](docs/ApiV1VideosLiveIdSessionsGet200Response.md)
 - [PeerTube.BlockStatus](docs/BlockStatus.md)
 - [PeerTube.BlockStatusAccountsValue](docs/BlockStatusAccountsValue.md)
 - [PeerTube.BlockStatusHostsValue](docs/BlockStatusHostsValue.md)
 - [PeerTube.CommentThreadPostResponse](docs/CommentThreadPostResponse.md)
 - [PeerTube.CommentThreadResponse](docs/CommentThreadResponse.md)
 - [PeerTube.ConfirmTwoFactorRequestRequest](docs/ConfirmTwoFactorRequestRequest.md)
 - [PeerTube.CreateVideoTranscodingRequest](docs/CreateVideoTranscodingRequest.md)
 - [PeerTube.CustomHomepage](docs/CustomHomepage.md)
 - [PeerTube.CutOptions](docs/CutOptions.md)
 - [PeerTube.DisableTwoFactorRequest](docs/DisableTwoFactorRequest.md)
 - [PeerTube.FileRedundancyInformation](docs/FileRedundancyInformation.md)
 - [PeerTube.Follow](docs/Follow.md)
 - [PeerTube.GetAbuses200Response](docs/GetAbuses200Response.md)
 - [PeerTube.GetAccountFollowers200Response](docs/GetAccountFollowers200Response.md)
 - [PeerTube.GetAccountVideosCategoryOneOfParameter](docs/GetAccountVideosCategoryOneOfParameter.md)
 - [PeerTube.GetAccountVideosLanguageOneOfParameter](docs/GetAccountVideosLanguageOneOfParameter.md)
 - [PeerTube.GetAccountVideosLicenceOneOfParameter](docs/GetAccountVideosLicenceOneOfParameter.md)
 - [PeerTube.GetAccountVideosTagsAllOfParameter](docs/GetAccountVideosTagsAllOfParameter.md)
 - [PeerTube.GetAccountVideosTagsOneOfParameter](docs/GetAccountVideosTagsOneOfParameter.md)
 - [PeerTube.GetJobs200Response](docs/GetJobs200Response.md)
 - [PeerTube.GetLiveIdIdParameter](docs/GetLiveIdIdParameter.md)
 - [PeerTube.GetMeVideoRating](docs/GetMeVideoRating.md)
 - [PeerTube.GetOAuthToken200Response](docs/GetOAuthToken200Response.md)
 - [PeerTube.GetUser200Response](docs/GetUser200Response.md)
 - [PeerTube.GetVideoBlocks200Response](docs/GetVideoBlocks200Response.md)
 - [PeerTube.GetVideoCaptions200Response](docs/GetVideoCaptions200Response.md)
 - [PeerTube.ImportVideosInChannelCreate](docs/ImportVideosInChannelCreate.md)
 - [PeerTube.Job](docs/Job.md)
 - [PeerTube.ListRegistrations200Response](docs/ListRegistrations200Response.md)
 - [PeerTube.LiveVideoLatencyMode](docs/LiveVideoLatencyMode.md)
 - [PeerTube.LiveVideoReplaySettings](docs/LiveVideoReplaySettings.md)
 - [PeerTube.LiveVideoResponse](docs/LiveVideoResponse.md)
 - [PeerTube.LiveVideoSessionResponse](docs/LiveVideoSessionResponse.md)
 - [PeerTube.LiveVideoSessionResponseReplayVideo](docs/LiveVideoSessionResponseReplayVideo.md)
 - [PeerTube.LiveVideoUpdate](docs/LiveVideoUpdate.md)
 - [PeerTube.MRSSGroupContent](docs/MRSSGroupContent.md)
 - [PeerTube.MRSSPeerLink](docs/MRSSPeerLink.md)
 - [PeerTube.NSFWPolicy](docs/NSFWPolicy.md)
 - [PeerTube.Notification](docs/Notification.md)
 - [PeerTube.NotificationActorFollow](docs/NotificationActorFollow.md)
 - [PeerTube.NotificationActorFollowFollowing](docs/NotificationActorFollowFollowing.md)
 - [PeerTube.NotificationComment](docs/NotificationComment.md)
 - [PeerTube.NotificationListResponse](docs/NotificationListResponse.md)
 - [PeerTube.NotificationVideo](docs/NotificationVideo.md)
 - [PeerTube.NotificationVideoAbuse](docs/NotificationVideoAbuse.md)
 - [PeerTube.NotificationVideoImport](docs/NotificationVideoImport.md)
 - [PeerTube.OAuthClient](docs/OAuthClient.md)
 - [PeerTube.PlaybackMetricCreate](docs/PlaybackMetricCreate.md)
 - [PeerTube.PlaylistElement](docs/PlaylistElement.md)
 - [PeerTube.Plugin](docs/Plugin.md)
 - [PeerTube.PluginResponse](docs/PluginResponse.md)
 - [PeerTube.PutMirroredVideoRequest](docs/PutMirroredVideoRequest.md)
 - [PeerTube.PutVideoPlaylistVideoRequest](docs/PutVideoPlaylistVideoRequest.md)
 - [PeerTube.RegisterUser](docs/RegisterUser.md)
 - [PeerTube.RegisterUserChannel](docs/RegisterUserChannel.md)
 - [PeerTube.ReorderVideoPlaylistRequest](docs/ReorderVideoPlaylistRequest.md)
 - [PeerTube.RequestTwoFactorResponse](docs/RequestTwoFactorResponse.md)
 - [PeerTube.RequestTwoFactorResponseOtpRequest](docs/RequestTwoFactorResponseOtpRequest.md)
 - [PeerTube.ResendEmailToVerifyRegistrationRequest](docs/ResendEmailToVerifyRegistrationRequest.md)
 - [PeerTube.ResendEmailToVerifyUserRequest](docs/ResendEmailToVerifyUserRequest.md)
 - [PeerTube.SendClientLog](docs/SendClientLog.md)
 - [PeerTube.ServerConfig](docs/ServerConfig.md)
 - [PeerTube.ServerConfigAbout](docs/ServerConfigAbout.md)
 - [PeerTube.ServerConfigAboutInstance](docs/ServerConfigAboutInstance.md)
 - [PeerTube.ServerConfigAutoBlacklist](docs/ServerConfigAutoBlacklist.md)
 - [PeerTube.ServerConfigAutoBlacklistVideos](docs/ServerConfigAutoBlacklistVideos.md)
 - [PeerTube.ServerConfigAutoBlacklistVideosOfUsers](docs/ServerConfigAutoBlacklistVideosOfUsers.md)
 - [PeerTube.ServerConfigAvatar](docs/ServerConfigAvatar.md)
 - [PeerTube.ServerConfigAvatarFile](docs/ServerConfigAvatarFile.md)
 - [PeerTube.ServerConfigAvatarFileSize](docs/ServerConfigAvatarFileSize.md)
 - [PeerTube.ServerConfigCustom](docs/ServerConfigCustom.md)
 - [PeerTube.ServerConfigCustomAdmin](docs/ServerConfigCustomAdmin.md)
 - [PeerTube.ServerConfigCustomCache](docs/ServerConfigCustomCache.md)
 - [PeerTube.ServerConfigCustomCacheCaptions](docs/ServerConfigCustomCacheCaptions.md)
 - [PeerTube.ServerConfigCustomFollowers](docs/ServerConfigCustomFollowers.md)
 - [PeerTube.ServerConfigCustomFollowersInstance](docs/ServerConfigCustomFollowersInstance.md)
 - [PeerTube.ServerConfigCustomImport](docs/ServerConfigCustomImport.md)
 - [PeerTube.ServerConfigCustomInstance](docs/ServerConfigCustomInstance.md)
 - [PeerTube.ServerConfigCustomServices](docs/ServerConfigCustomServices.md)
 - [PeerTube.ServerConfigCustomServicesTwitter](docs/ServerConfigCustomServicesTwitter.md)
 - [PeerTube.ServerConfigCustomSignup](docs/ServerConfigCustomSignup.md)
 - [PeerTube.ServerConfigCustomTheme](docs/ServerConfigCustomTheme.md)
 - [PeerTube.ServerConfigCustomTranscoding](docs/ServerConfigCustomTranscoding.md)
 - [PeerTube.ServerConfigCustomTranscodingHls](docs/ServerConfigCustomTranscodingHls.md)
 - [PeerTube.ServerConfigCustomTranscodingResolutions](docs/ServerConfigCustomTranscodingResolutions.md)
 - [PeerTube.ServerConfigCustomTranscodingWebtorrent](docs/ServerConfigCustomTranscodingWebtorrent.md)
 - [PeerTube.ServerConfigCustomUser](docs/ServerConfigCustomUser.md)
 - [PeerTube.ServerConfigFollowings](docs/ServerConfigFollowings.md)
 - [PeerTube.ServerConfigFollowingsInstance](docs/ServerConfigFollowingsInstance.md)
 - [PeerTube.ServerConfigFollowingsInstanceAutoFollowIndex](docs/ServerConfigFollowingsInstanceAutoFollowIndex.md)
 - [PeerTube.ServerConfigImport](docs/ServerConfigImport.md)
 - [PeerTube.ServerConfigImportVideos](docs/ServerConfigImportVideos.md)
 - [PeerTube.ServerConfigInstance](docs/ServerConfigInstance.md)
 - [PeerTube.ServerConfigInstanceCustomizations](docs/ServerConfigInstanceCustomizations.md)
 - [PeerTube.ServerConfigPlugin](docs/ServerConfigPlugin.md)
 - [PeerTube.ServerConfigSearch](docs/ServerConfigSearch.md)
 - [PeerTube.ServerConfigSearchRemoteUri](docs/ServerConfigSearchRemoteUri.md)
 - [PeerTube.ServerConfigSignup](docs/ServerConfigSignup.md)
 - [PeerTube.ServerConfigTranscoding](docs/ServerConfigTranscoding.md)
 - [PeerTube.ServerConfigTrending](docs/ServerConfigTrending.md)
 - [PeerTube.ServerConfigTrendingVideos](docs/ServerConfigTrendingVideos.md)
 - [PeerTube.ServerConfigUser](docs/ServerConfigUser.md)
 - [PeerTube.ServerConfigVideo](docs/ServerConfigVideo.md)
 - [PeerTube.ServerConfigVideoCaption](docs/ServerConfigVideoCaption.md)
 - [PeerTube.ServerConfigVideoFile](docs/ServerConfigVideoFile.md)
 - [PeerTube.ServerConfigVideoImage](docs/ServerConfigVideoImage.md)
 - [PeerTube.ServerStats](docs/ServerStats.md)
 - [PeerTube.ServerStatsVideosRedundancyInner](docs/ServerStatsVideosRedundancyInner.md)
 - [PeerTube.UninstallPluginRequest](docs/UninstallPluginRequest.md)
 - [PeerTube.UpdateMe](docs/UpdateMe.md)
 - [PeerTube.UpdateUser](docs/UpdateUser.md)
 - [PeerTube.User](docs/User.md)
 - [PeerTube.UserAdminFlags](docs/UserAdminFlags.md)
 - [PeerTube.UserRegistration](docs/UserRegistration.md)
 - [PeerTube.UserRegistrationAcceptOrReject](docs/UserRegistrationAcceptOrReject.md)
 - [PeerTube.UserRegistrationRequest](docs/UserRegistrationRequest.md)
 - [PeerTube.UserRegistrationState](docs/UserRegistrationState.md)
 - [PeerTube.UserRegistrationUser](docs/UserRegistrationUser.md)
 - [PeerTube.UserRole](docs/UserRole.md)
 - [PeerTube.UserViewingVideo](docs/UserViewingVideo.md)
 - [PeerTube.UserWithStats](docs/UserWithStats.md)
 - [PeerTube.VerifyRegistrationEmailRequest](docs/VerifyRegistrationEmailRequest.md)
 - [PeerTube.VerifyUserRequest](docs/VerifyUserRequest.md)
 - [PeerTube.Video](docs/Video.md)
 - [PeerTube.VideoBlacklist](docs/VideoBlacklist.md)
 - [PeerTube.VideoCaption](docs/VideoCaption.md)
 - [PeerTube.VideoChannel](docs/VideoChannel.md)
 - [PeerTube.VideoChannelAllOfOwnerAccount](docs/VideoChannelAllOfOwnerAccount.md)
 - [PeerTube.VideoChannelCreate](docs/VideoChannelCreate.md)
 - [PeerTube.VideoChannelEdit](docs/VideoChannelEdit.md)
 - [PeerTube.VideoChannelList](docs/VideoChannelList.md)
 - [PeerTube.VideoChannelListDataInner](docs/VideoChannelListDataInner.md)
 - [PeerTube.VideoChannelSummary](docs/VideoChannelSummary.md)
 - [PeerTube.VideoChannelSync](docs/VideoChannelSync.md)
 - [PeerTube.VideoChannelSyncCreate](docs/VideoChannelSyncCreate.md)
 - [PeerTube.VideoChannelSyncList](docs/VideoChannelSyncList.md)
 - [PeerTube.VideoChannelSyncState](docs/VideoChannelSyncState.md)
 - [PeerTube.VideoChannelUpdate](docs/VideoChannelUpdate.md)
 - [PeerTube.VideoComment](docs/VideoComment.md)
 - [PeerTube.VideoCommentThreadTree](docs/VideoCommentThreadTree.md)
 - [PeerTube.VideoCommentsForXMLInner](docs/VideoCommentsForXMLInner.md)
 - [PeerTube.VideoConstantNumberCategory](docs/VideoConstantNumberCategory.md)
 - [PeerTube.VideoConstantNumberLicence](docs/VideoConstantNumberLicence.md)
 - [PeerTube.VideoConstantStringLanguage](docs/VideoConstantStringLanguage.md)
 - [PeerTube.VideoDetails](docs/VideoDetails.md)
 - [PeerTube.VideoFile](docs/VideoFile.md)
 - [PeerTube.VideoImport](docs/VideoImport.md)
 - [PeerTube.VideoImportStateConstant](docs/VideoImportStateConstant.md)
 - [PeerTube.VideoImportsList](docs/VideoImportsList.md)
 - [PeerTube.VideoInfo](docs/VideoInfo.md)
 - [PeerTube.VideoListResponse](docs/VideoListResponse.md)
 - [PeerTube.VideoPlaylist](docs/VideoPlaylist.md)
 - [PeerTube.VideoPlaylistPrivacyConstant](docs/VideoPlaylistPrivacyConstant.md)
 - [PeerTube.VideoPlaylistPrivacySet](docs/VideoPlaylistPrivacySet.md)
 - [PeerTube.VideoPlaylistTypeConstant](docs/VideoPlaylistTypeConstant.md)
 - [PeerTube.VideoPlaylistTypeSet](docs/VideoPlaylistTypeSet.md)
 - [PeerTube.VideoPrivacyConstant](docs/VideoPrivacyConstant.md)
 - [PeerTube.VideoPrivacySet](docs/VideoPrivacySet.md)
 - [PeerTube.VideoRating](docs/VideoRating.md)
 - [PeerTube.VideoRedundancy](docs/VideoRedundancy.md)
 - [PeerTube.VideoRedundancyRedundancies](docs/VideoRedundancyRedundancies.md)
 - [PeerTube.VideoResolutionConstant](docs/VideoResolutionConstant.md)
 - [PeerTube.VideoScheduledUpdate](docs/VideoScheduledUpdate.md)
 - [PeerTube.VideoSource](docs/VideoSource.md)
 - [PeerTube.VideoStateConstant](docs/VideoStateConstant.md)
 - [PeerTube.VideoStatsOverall](docs/VideoStatsOverall.md)
 - [PeerTube.VideoStatsOverallCountriesInner](docs/VideoStatsOverallCountriesInner.md)
 - [PeerTube.VideoStatsRetention](docs/VideoStatsRetention.md)
 - [PeerTube.VideoStatsRetentionDataInner](docs/VideoStatsRetentionDataInner.md)
 - [PeerTube.VideoStatsTimeserie](docs/VideoStatsTimeserie.md)
 - [PeerTube.VideoStatsTimeserieDataInner](docs/VideoStatsTimeserieDataInner.md)
 - [PeerTube.VideoStreamingPlaylists](docs/VideoStreamingPlaylists.md)
 - [PeerTube.VideoStreamingPlaylistsHLS](docs/VideoStreamingPlaylistsHLS.md)
 - [PeerTube.VideoStreamingPlaylistsHLSRedundanciesInner](docs/VideoStreamingPlaylistsHLSRedundanciesInner.md)
 - [PeerTube.VideoTokenResponse](docs/VideoTokenResponse.md)
 - [PeerTube.VideoTokenResponseFiles](docs/VideoTokenResponseFiles.md)
 - [PeerTube.VideoUploadRequestCommon](docs/VideoUploadRequestCommon.md)
 - [PeerTube.VideoUploadRequestResumable](docs/VideoUploadRequestResumable.md)
 - [PeerTube.VideoUploadResponse](docs/VideoUploadResponse.md)
 - [PeerTube.VideoUploadResponseVideo](docs/VideoUploadResponseVideo.md)
 - [PeerTube.VideoUserHistory](docs/VideoUserHistory.md)
 - [PeerTube.VideosForXMLInner](docs/VideosForXMLInner.md)
 - [PeerTube.VideosForXMLInnerEnclosure](docs/VideosForXMLInnerEnclosure.md)
 - [PeerTube.VideosForXMLInnerMediaCommunity](docs/VideosForXMLInnerMediaCommunity.md)
 - [PeerTube.VideosForXMLInnerMediaCommunityMediaStatistics](docs/VideosForXMLInnerMediaCommunityMediaStatistics.md)
 - [PeerTube.VideosForXMLInnerMediaEmbed](docs/VideosForXMLInnerMediaEmbed.md)
 - [PeerTube.VideosForXMLInnerMediaGroupInner](docs/VideosForXMLInnerMediaGroupInner.md)
 - [PeerTube.VideosForXMLInnerMediaPlayer](docs/VideosForXMLInnerMediaPlayer.md)
 - [PeerTube.VideosForXMLInnerMediaThumbnail](docs/VideosForXMLInnerMediaThumbnail.md)


## Documentation for Authorization


Authentication schemes defined for the API:
### OAuth2


- **Type**: OAuth
- **Flow**: password
- **Authorization URL**: 
- **Scopes**: 
  - admin: Admin scope
  - moderator: Moderator scope
  - user: User scope

