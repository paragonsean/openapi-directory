# TwitterApi.DefaultApi

All URIs are relative to *https://api.twitter.com/1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountSettingsGet**](DefaultApi.md#accountSettingsGet) | **GET** /account/settings.json | 
[**accountSettingsPost**](DefaultApi.md#accountSettingsPost) | **POST** /account/settings.json | 
[**accountUpdateDeliveryDevice**](DefaultApi.md#accountUpdateDeliveryDevice) | **POST** /account/update_delivery_device.json | 
[**accountUpdateProfile**](DefaultApi.md#accountUpdateProfile) | **POST** /account/update_profile.json | 
[**accountsUpdateProfileBackgroundImage**](DefaultApi.md#accountsUpdateProfileBackgroundImage) | **POST** /account/update_profile_background_image.json | 
[**accountsUpdateProfileColors**](DefaultApi.md#accountsUpdateProfileColors) | **POST** /account/update_profile_colors.json | 
[**accountsUpdateProfileImage**](DefaultApi.md#accountsUpdateProfileImage) | **POST** /account/update_profile_image.json | 
[**applicationRateLimitStatus**](DefaultApi.md#applicationRateLimitStatus) | **GET** /application/rate_limit_status.json | 
[**blocksCreate**](DefaultApi.md#blocksCreate) | **POST** /blocks/create.json | 
[**blocksDestroy**](DefaultApi.md#blocksDestroy) | **POST** /blocks/destroy.json | 
[**blocksIds**](DefaultApi.md#blocksIds) | **GET** /blocks/ids.json | 
[**blocksList**](DefaultApi.md#blocksList) | **GET** /blocks/list.json | 
[**directMessages**](DefaultApi.md#directMessages) | **GET** /direct_messages.json | 
[**directMessagesDestroy**](DefaultApi.md#directMessagesDestroy) | **POST** /direct_messages/destroy.json | 
[**directMessagesNew**](DefaultApi.md#directMessagesNew) | **POST** /direct_messages/new.json | 
[**directMessagesSent**](DefaultApi.md#directMessagesSent) | **GET** /direct_messages/sent.json | 
[**directMessagesShow**](DefaultApi.md#directMessagesShow) | **GET** /direct_messages/show.json | 
[**favoritesCreate**](DefaultApi.md#favoritesCreate) | **POST** /favorites/create.json | 
[**favoritesDestroy**](DefaultApi.md#favoritesDestroy) | **POST** /favorites/destroy.json | 
[**favoritesList**](DefaultApi.md#favoritesList) | **GET** /favorites/list.json | 
[**followersIds**](DefaultApi.md#followersIds) | **GET** /followers/ids.json | 
[**friendsIds**](DefaultApi.md#friendsIds) | **GET** /friends/ids.json | 
[**friendshipsCreate**](DefaultApi.md#friendshipsCreate) | **POST** /friendships/create.json | 
[**friendshipsDestroy**](DefaultApi.md#friendshipsDestroy) | **POST** /friendships/destroy.json | 
[**friendshipsIncoming**](DefaultApi.md#friendshipsIncoming) | **GET** /friendships/incoming.json | 
[**friendshipsLookup**](DefaultApi.md#friendshipsLookup) | **GET** /friendships/lookup.json | 
[**friendshipsOutgoing**](DefaultApi.md#friendshipsOutgoing) | **GET** /friendships/outgoing.json | 
[**friendshipsShow**](DefaultApi.md#friendshipsShow) | **GET** /friendships/show.json | 
[**friendshipsUpdate**](DefaultApi.md#friendshipsUpdate) | **POST** /friendships/update.json | 
[**geoPlaceId**](DefaultApi.md#geoPlaceId) | **GET** /geo/id/{place_id}.json | 
[**geoPlaces**](DefaultApi.md#geoPlaces) | **POST** /geo/places.json | 
[**geoReverseGeocode**](DefaultApi.md#geoReverseGeocode) | **GET** /geo/reverse_geocode.json | 
[**geoSearch**](DefaultApi.md#geoSearch) | **GET** /geo/search.json | 
[**geoSimilarPlaces**](DefaultApi.md#geoSimilarPlaces) | **GET** /geo/similar_places.json | 
[**helpConfigurations**](DefaultApi.md#helpConfigurations) | **GET** /help/configuration.json | 
[**helpLanguages**](DefaultApi.md#helpLanguages) | **GET** /help/languages.json | 
[**helpPrivacy**](DefaultApi.md#helpPrivacy) | **GET** /help/privacy.json | 
[**helpTos**](DefaultApi.md#helpTos) | **GET** /help/tos.json | 
[**listsCreate**](DefaultApi.md#listsCreate) | **POST** /lists/create.json | 
[**listsDestroy**](DefaultApi.md#listsDestroy) | **POST** /lists/destroy.json | 
[**listsList**](DefaultApi.md#listsList) | **GET** /lists/list.json | 
[**listsMembers**](DefaultApi.md#listsMembers) | **GET** /lists/members.json | 
[**listsMembersCreate**](DefaultApi.md#listsMembersCreate) | **POST** /lists/members/create.json | 
[**listsMembersCreateAll**](DefaultApi.md#listsMembersCreateAll) | **POST** /lists/members/create_all.json | 
[**listsMembersDestroy**](DefaultApi.md#listsMembersDestroy) | **POST** /lists/members/destroy.json | 
[**listsMembersDestroyAll**](DefaultApi.md#listsMembersDestroyAll) | **POST** /lists/members/destroy_all.json | 
[**listsMembersShow**](DefaultApi.md#listsMembersShow) | **GET** /lists/members/show.json | 
[**listsMemberships**](DefaultApi.md#listsMemberships) | **GET** /lists/memberships.json | 
[**listsShow**](DefaultApi.md#listsShow) | **GET** /lists/show.json | 
[**listsStatuses**](DefaultApi.md#listsStatuses) | **GET** /lists/statuses.json | 
[**listsSubscribers**](DefaultApi.md#listsSubscribers) | **GET** /lists/subscribers.json | 
[**listsSubscribersCreate**](DefaultApi.md#listsSubscribersCreate) | **POST** /lists/subscribers/create.json | 
[**listsSubscribersDestroy**](DefaultApi.md#listsSubscribersDestroy) | **POST** /lists/subscribers/destroy.json | 
[**listsSubscribersShow**](DefaultApi.md#listsSubscribersShow) | **GET** /lists/subscribers/show.json | 
[**listsSubscriptions**](DefaultApi.md#listsSubscriptions) | **GET** /lists/subscriptions.json | 
[**listsUpdate**](DefaultApi.md#listsUpdate) | **POST** /lists/update.json | 
[**savedSearchesCreate**](DefaultApi.md#savedSearchesCreate) | **POST** /saved_searches/create.json | 
[**savedSearchesDestroy**](DefaultApi.md#savedSearchesDestroy) | **POST** /saved_searches/destroy/{id}.json | 
[**savedSearchesList**](DefaultApi.md#savedSearchesList) | **GET** /saved_searches/list.json | 
[**savedsearchesid**](DefaultApi.md#savedsearchesid) | **GET** /saved_searches/show/{id}.json | 
[**searchTweets**](DefaultApi.md#searchTweets) | **GET** /search/tweets.json | 
[**statusesDestroy**](DefaultApi.md#statusesDestroy) | **POST** /statuses/destroy/{id}.json | 
[**statusesHomeTimeline**](DefaultApi.md#statusesHomeTimeline) | **GET** /statuses/home_timeline.json | 
[**statusesMentionsTimeline**](DefaultApi.md#statusesMentionsTimeline) | **GET** /statuses/mentions_timeline.json | 
[**statusesOembed**](DefaultApi.md#statusesOembed) | **GET** /statuses/oembed.json | 
[**statusesRetweets**](DefaultApi.md#statusesRetweets) | **GET** /statuses/retweets/{id}.json | 
[**statusesShow**](DefaultApi.md#statusesShow) | **GET** /statuses/show/{id}.json | 
[**statusesUpdate**](DefaultApi.md#statusesUpdate) | **POST** /statuses/update.json | 
[**statusesUpdateWithMedia**](DefaultApi.md#statusesUpdateWithMedia) | **POST** /statuses/update_with_media.json | 
[**statusesUserTimeline**](DefaultApi.md#statusesUserTimeline) | **GET** /statuses/user_timeline.json | 
[**statusesretweetid**](DefaultApi.md#statusesretweetid) | **POST** /statuses/retweet/{id}.json | 
[**trendsAvailable**](DefaultApi.md#trendsAvailable) | **GET** /trends/available.json | 
[**trendsClosest**](DefaultApi.md#trendsClosest) | **GET** /trends/closest.json | 
[**trendsPlace**](DefaultApi.md#trendsPlace) | **GET** /trends/place.json | 
[**usersContributees**](DefaultApi.md#usersContributees) | **GET** /users/contributees.json | 
[**usersContributors**](DefaultApi.md#usersContributors) | **GET** /users/contributors.json | 
[**usersLookup**](DefaultApi.md#usersLookup) | **GET** /users/lookup.json | 
[**usersReportSpam**](DefaultApi.md#usersReportSpam) | **POST** /users/report_spam.json | 
[**usersSearch**](DefaultApi.md#usersSearch) | **GET** /users/search.json | 
[**usersShow**](DefaultApi.md#usersShow) | **GET** /users/show.json | 
[**usersSuggestions**](DefaultApi.md#usersSuggestions) | **GET** /users/suggestions.json | 
[**usersSuggestionsSlug**](DefaultApi.md#usersSuggestionsSlug) | **GET** /users/suggestions/{slug}.json | 
[**usersSuggestionsslugmembers**](DefaultApi.md#usersSuggestionsslugmembers) | **GET** /users/suggestions/{slug}/members.json | 



## accountSettingsGet

> accountSettingsGet(opts)



Returns settings (including current trend, geo and sleep time information) for the authenticating user.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'trendLocationWoeid': "trendLocationWoeid_example", // String | The Yahoo! Where On Earth ID to use as the user's default trend location. Global information is available by using 1 as the WOEID. The woeid must be one of the locations returned by GET trends/available.  Example Values: 1
  'sleepTimeEnabled': "sleepTimeEnabled_example", // String | When set to true, t or 1, will enable sleep time for the user. Sleep time is the time when push or SMS notifications should not be sent to the user.  Example Values: true
  'startSleepTime': "startSleepTime_example", // String | The hour that sleep time should begin if it is enabled. The value for this parameter should be provided in ISO8601 format (i.e. 00-23). The time is considered to be in the same timezone as the user's time_zone setting.  Example Values: 13
  'endSleepTime': "endSleepTime_example", // String | The hour that sleep time should end if it is enabled. The value for this parameter should be provided in ISO8601 format (i.e. 00-23). The time is considered to be in the same timezone as the user's time_zone setting.  Example Values: 13
  'timeZone': "timeZone_example", // String | The timezone dates and times should be displayed in for the user. The timezone must be one of the Rails TimeZone names.  Example Values: Europe/Copenhagen, Pacific/Tongatapu
  'lang': "lang_example" // String | The language which Twitter should render in for this user. The language must be specified by the appropriate two letter ISO 639-1 representation. Currently supported languages are provided by GET help/languages.  Example Values: it, en, es
};
apiInstance.accountSettingsGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trendLocationWoeid** | **String**| The Yahoo! Where On Earth ID to use as the user&#39;s default trend location. Global information is available by using 1 as the WOEID. The woeid must be one of the locations returned by GET trends/available.  Example Values: 1 | [optional] 
 **sleepTimeEnabled** | **String**| When set to true, t or 1, will enable sleep time for the user. Sleep time is the time when push or SMS notifications should not be sent to the user.  Example Values: true | [optional] 
 **startSleepTime** | **String**| The hour that sleep time should begin if it is enabled. The value for this parameter should be provided in ISO8601 format (i.e. 00-23). The time is considered to be in the same timezone as the user&#39;s time_zone setting.  Example Values: 13 | [optional] 
 **endSleepTime** | **String**| The hour that sleep time should end if it is enabled. The value for this parameter should be provided in ISO8601 format (i.e. 00-23). The time is considered to be in the same timezone as the user&#39;s time_zone setting.  Example Values: 13 | [optional] 
 **timeZone** | **String**| The timezone dates and times should be displayed in for the user. The timezone must be one of the Rails TimeZone names.  Example Values: Europe/Copenhagen, Pacific/Tongatapu | [optional] 
 **lang** | **String**| The language which Twitter should render in for this user. The language must be specified by the appropriate two letter ISO 639-1 representation. Currently supported languages are provided by GET help/languages.  Example Values: it, en, es | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## accountSettingsPost

> accountSettingsPost(opts)



Updates the authenticating user&#39;s settings.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'trendLocationWoeid': "trendLocationWoeid_example", // String | The Yahoo! Where On Earth ID to use as the user's default trend location. Global information is available by using 1 as the WOEID. The woeid must be one of the locations returned by GET trends/available.  Example Values: 1
  'sleepTimeEnabled': "sleepTimeEnabled_example", // String | When set to true, t or 1, will enable sleep time for the user. Sleep time is the time when push or SMS notifications should not be sent to the user.  Example Values: true
  'startSleepTime': "startSleepTime_example", // String | The hour that sleep time should begin if it is enabled. The value for this parameter should be provided in ISO8601 format (i.e. 00-23). The time is considered to be in the same timezone as the user's time_zone setting.  Example Values: 13
  'endSleepTime': "endSleepTime_example", // String | The hour that sleep time should end if it is enabled. The value for this parameter should be provided in ISO8601 format (i.e. 00-23). The time is considered to be in the same timezone as the user's time_zone setting.  Example Values: 13
  'timeZone': "timeZone_example", // String | The timezone dates and times should be displayed in for the user. The timezone must be one of the Rails TimeZone names.  Example Values: Europe/Copenhagen, Pacific/Tongatapu
  'lang': "lang_example" // String | The language which Twitter should render in for this user. The language must be specified by the appropriate two letter ISO 639-1 representation. Currently supported languages are provided by GET help/languages.  Example Values: it, en, es
};
apiInstance.accountSettingsPost(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trendLocationWoeid** | **String**| The Yahoo! Where On Earth ID to use as the user&#39;s default trend location. Global information is available by using 1 as the WOEID. The woeid must be one of the locations returned by GET trends/available.  Example Values: 1 | [optional] 
 **sleepTimeEnabled** | **String**| When set to true, t or 1, will enable sleep time for the user. Sleep time is the time when push or SMS notifications should not be sent to the user.  Example Values: true | [optional] 
 **startSleepTime** | **String**| The hour that sleep time should begin if it is enabled. The value for this parameter should be provided in ISO8601 format (i.e. 00-23). The time is considered to be in the same timezone as the user&#39;s time_zone setting.  Example Values: 13 | [optional] 
 **endSleepTime** | **String**| The hour that sleep time should end if it is enabled. The value for this parameter should be provided in ISO8601 format (i.e. 00-23). The time is considered to be in the same timezone as the user&#39;s time_zone setting.  Example Values: 13 | [optional] 
 **timeZone** | **String**| The timezone dates and times should be displayed in for the user. The timezone must be one of the Rails TimeZone names.  Example Values: Europe/Copenhagen, Pacific/Tongatapu | [optional] 
 **lang** | **String**| The language which Twitter should render in for this user. The language must be specified by the appropriate two letter ISO 639-1 representation. Currently supported languages are provided by GET help/languages.  Example Values: it, en, es | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## accountUpdateDeliveryDevice

> accountUpdateDeliveryDevice(device, opts)



Sets which device Twitter delivers updates to for the authenticating user. Sending none as the device parameter will disable SMS updates.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let device = "device_example"; // String | Must be one of: sms, none.  Example Values: sms
let opts = {
  'includeEntities': "includeEntities_example" // String | When set to either true, t or 1, each tweet will include a node called \"entities,\". This node offers a variety of metadata about the tweet in a discreet structure, including: user_mentions, urls, and hashtags. While entities are opt-in on timelines at present, they will be made a default component of output in the future. See Tweet Entities for more detail on entities.  Example Values: true
};
apiInstance.accountUpdateDeliveryDevice(device, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | **String**| Must be one of: sms, none.  Example Values: sms | 
 **includeEntities** | **String**| When set to either true, t or 1, each tweet will include a node called \&quot;entities,\&quot;. This node offers a variety of metadata about the tweet in a discreet structure, including: user_mentions, urls, and hashtags. While entities are opt-in on timelines at present, they will be made a default component of output in the future. See Tweet Entities for more detail on entities.  Example Values: true | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## accountUpdateProfile

> accountUpdateProfile(opts)



Sets values that users are able to set under the Account tab of their settings page. Only the parameters specified will be updated.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'name': "name_example", // String | Full name associated with the profile. Maximum of 20 characters.  Example Values: Marcel Molina
  'url': "url_example", // String | URL associated with the profile. Will be prepended with \"http://\" if not present. Maximum of 100 characters.  Example Values: http://project.ioni.st
  'location': "location_example", // String | The city or country describing where the user of the account is located. The contents are not normalized or geocoded in any way. Maximum of 30 characters.  Example Values: San Francisco, CA
  'description': "description_example", // String | A description of the user owning the account. Maximum of 160 characters.  Example Values: Flipped my wig at age 22 and it never grew back. Also: I work at Twitter.
  'includeEntities': "includeEntities_example", // String | The entities node will not be included when set to false.  Example Values: false
  'skipStatus': "skipStatus_example" // String | When set to either true, t or 1 statuses will not be included in the returned user objects.
};
apiInstance.accountUpdateProfile(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| Full name associated with the profile. Maximum of 20 characters.  Example Values: Marcel Molina | [optional] 
 **url** | **String**| URL associated with the profile. Will be prepended with \&quot;http://\&quot; if not present. Maximum of 100 characters.  Example Values: http://project.ioni.st | [optional] 
 **location** | **String**| The city or country describing where the user of the account is located. The contents are not normalized or geocoded in any way. Maximum of 30 characters.  Example Values: San Francisco, CA | [optional] 
 **description** | **String**| A description of the user owning the account. Maximum of 160 characters.  Example Values: Flipped my wig at age 22 and it never grew back. Also: I work at Twitter. | [optional] 
 **includeEntities** | **String**| The entities node will not be included when set to false.  Example Values: false | [optional] 
 **skipStatus** | **String**| When set to either true, t or 1 statuses will not be included in the returned user objects. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## accountsUpdateProfileBackgroundImage

> accountsUpdateProfileBackgroundImage(contentType, opts)



Updates the authenticating user&#39;s profile background image. This method can also be used to enable or disable the profile background image. Although each parameter is marked as optional, at least one of image, tile or use must be provided when making this request.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let contentType = "'multipart/form-data'"; // String | Content type header
let opts = {
  'tile': "tile_example", // String | Whether or not to tile the background image. If set to true, t or 1 the background image will be displayed tiled. The image will not be tiled otherwise.
  'use': "use_example", // String | Determines whether to display the profile background image or not. When set to true, t or 1 the background image will be displayed if an image is being uploaded with the request, or has been uploaded previously. An error will be returned if you try to use a background image when one is not being uploaded or does not exist. If this parameter is defined but set to anything other than true, t or 1, the background image will stop being used.
  'includeEntities': "includeEntities_example", // String | The entities node will not be included when set to false.  Example Values: false
  'skipStatus': "skipStatus_example" // String | When set to either true, t or 1 statuses will not be included in the returned user objects.
};
apiInstance.accountsUpdateProfileBackgroundImage(contentType, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contentType** | **String**| Content type header | [default to &#39;multipart/form-data&#39;]
 **tile** | **String**| Whether or not to tile the background image. If set to true, t or 1 the background image will be displayed tiled. The image will not be tiled otherwise. | [optional] 
 **use** | **String**| Determines whether to display the profile background image or not. When set to true, t or 1 the background image will be displayed if an image is being uploaded with the request, or has been uploaded previously. An error will be returned if you try to use a background image when one is not being uploaded or does not exist. If this parameter is defined but set to anything other than true, t or 1, the background image will stop being used. | [optional] 
 **includeEntities** | **String**| The entities node will not be included when set to false.  Example Values: false | [optional] 
 **skipStatus** | **String**| When set to either true, t or 1 statuses will not be included in the returned user objects. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## accountsUpdateProfileColors

> accountsUpdateProfileColors(opts)



Sets one or more hex values that control the color scheme of the authenticating user&#39;s profile page on twitter.com. Each parameter&#39;s value must be a valid hexidecimal value, and may be either three or six characters (ex: #fff or #ffffff).

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'profileBackgroundColor': "profileBackgroundColor_example", // String | Profile background color. Example Values: 3D3D3D
  'profileLinkColor': "profileLinkColor_example", // String | Profile link color.Example Values: 0000FF
  'profileSidebarBorderColor': "profileSidebarBorderColor_example", // String | Profile sidebar's border color. Example Values: 0F0F0F
  'profileSidebarFillColor': "profileSidebarFillColor_example", // String | Profile sidebar's background color. Example Values: 00FF00
  'profileTextColor': "profileTextColor_example", // String | Profile text color. Example Values: 000000
  'includeEntities': "includeEntities_example", // String | The entities node will not be included when set to false. Example Values: false
  'skipStatus': "skipStatus_example" // String | When set to either true, t or 1 statuses will not be included in the returned user objects.
};
apiInstance.accountsUpdateProfileColors(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profileBackgroundColor** | **String**| Profile background color. Example Values: 3D3D3D | [optional] 
 **profileLinkColor** | **String**| Profile link color.Example Values: 0000FF | [optional] 
 **profileSidebarBorderColor** | **String**| Profile sidebar&#39;s border color. Example Values: 0F0F0F | [optional] 
 **profileSidebarFillColor** | **String**| Profile sidebar&#39;s background color. Example Values: 00FF00 | [optional] 
 **profileTextColor** | **String**| Profile text color. Example Values: 000000 | [optional] 
 **includeEntities** | **String**| The entities node will not be included when set to false. Example Values: false | [optional] 
 **skipStatus** | **String**| When set to either true, t or 1 statuses will not be included in the returned user objects. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## accountsUpdateProfileImage

> accountsUpdateProfileImage(contentType, opts)



Updates the authenticating user&#39;s profile image. Note that this method expects raw multipart data, not a URL to an image. This method asynchronously processes the uploaded file before updating the user&#39;s profile image URL. You can either update your local cache the next time you request the user&#39;s information, or, at least 5 seconds after uploading the image, ask for the updated URL using GET users/profile_image/:screen_name (https://dev.twitter.com/docs/api/1/get/users/profile_image/:screen_name).

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let contentType = "'multipart/form-data'"; // String | Content type header
let opts = {
  'skipStatus': "skipStatus_example" // String | When set to either true, t or 1 statuses will not be included in the returned user objects.
};
apiInstance.accountsUpdateProfileImage(contentType, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contentType** | **String**| Content type header | [default to &#39;multipart/form-data&#39;]
 **skipStatus** | **String**| When set to either true, t or 1 statuses will not be included in the returned user objects. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## applicationRateLimitStatus

> applicationRateLimitStatus(opts)



Returns the current rate limits for methods belonging to the specified resource families.  Each 1.1 API resource belongs to a \&quot;resource family\&quot; which is indicated in its method documentation. You can typically determine a method&#39;s resource family from the first component of the path after the resource version.  This method responds with a map of methods belonging to the families specified by the resources parameter, the current remaining uses for each of those resources within the current rate limiting window, and its expiration time in epoch time. It also includes a rate_limit_context field that indicates the current access token context.  You may also issue requests to this method without any parameters to receive a map of all rate limited GET methods. If your application only uses a few of methods, please explicitly provide a resources parameter with the specified resource families you work with.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'resources': "resources_example" // String | A comma-separated list of resource families you want to know the current rate limit disposition for. For best performance, only specify the resource families pertinent to your application.Example Values: statuses,friends,trends,help
};
apiInstance.applicationRateLimitStatus(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resources** | **String**| A comma-separated list of resource families you want to know the current rate limit disposition for. For best performance, only specify the resource families pertinent to your application.Example Values: statuses,friends,trends,help | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## blocksCreate

> blocksCreate(opts)



Blocks the specified user from following the authenticating user. In addition the blocked user will not show in the authenticating users mentions or timeline (unless retweeted by another user). If a follow or friend relationship exists it is destroyed.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'includeEntities': "includeEntities_example", // String | The entities node will not be included when set to false.  Example Values: false
  'skipStatus': "skipStatus_example" // String | When set to either true, t or 1 statuses will not be included in the returned user objects.
};
apiInstance.blocksCreate(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **includeEntities** | **String**| The entities node will not be included when set to false.  Example Values: false | [optional] 
 **skipStatus** | **String**| When set to either true, t or 1 statuses will not be included in the returned user objects. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## blocksDestroy

> blocksDestroy(opts)



Un-blocks the user specified in the ID parameter for the authenticating user. Returns the un-blocked user in the requested format when successful. If relationships existed before the block was instated, they will not be restored.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'includeEntities': "includeEntities_example", // String | The entities node will not be included when set to false.  Example Values: false
  'skipStatus': "skipStatus_example" // String | When set to either true, t or 1 statuses will not be included in the returned user objects.
};
apiInstance.blocksDestroy(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **includeEntities** | **String**| The entities node will not be included when set to false.  Example Values: false | [optional] 
 **skipStatus** | **String**| When set to either true, t or 1 statuses will not be included in the returned user objects. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## blocksIds

> blocksIds(opts)



Returns an array of numeric user ids the authenticating user is blocking.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'stringifyIds': "stringifyIds_example", // String | Many programming environments will not consume our ids due to their size. Provide this option to have ids returned as strings instead. Read more about Twitter IDs, JSON and Snowflake.  Example Values: true
  'cursor': "cursor_example" // String | Causes the list of blocked users to be broken into pages of no more than 5000 IDs at a time. The number of IDs returned is not guaranteed to be 5000 as suspended users are filtered out after connections are queried. If no cursor is provided, a value of -1 will be assumed, which is the first \"page.\"  The response from the API will include a previous_cursor and next_cursor to allow paging back and forth. See Using cursors to navigate collections for more information.  Example Values: 12893764510938
};
apiInstance.blocksIds(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stringifyIds** | **String**| Many programming environments will not consume our ids due to their size. Provide this option to have ids returned as strings instead. Read more about Twitter IDs, JSON and Snowflake.  Example Values: true | [optional] 
 **cursor** | **String**| Causes the list of blocked users to be broken into pages of no more than 5000 IDs at a time. The number of IDs returned is not guaranteed to be 5000 as suspended users are filtered out after connections are queried. If no cursor is provided, a value of -1 will be assumed, which is the first \&quot;page.\&quot;  The response from the API will include a previous_cursor and next_cursor to allow paging back and forth. See Using cursors to navigate collections for more information.  Example Values: 12893764510938 | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## blocksList

> blocksList(opts)



Allows one to enable or disable retweets and device notifications from the specified user.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'includeEntities': "includeEntities_example", // String | The entities node will not be included when set to false. Example Values: false
  'skipStatus': "skipStatus_example", // String | When set to either true, t or 1 statuses will not be included in the returned user objects.
  'cursor': "cursor_example" // String | Causes the list of blocked users to be broken into pages of no more than 5000 IDs at a time. The number of IDs returned is not guaranteed to be 5000 as suspended users are filtered out after connections are queried. If no cursor is provided, a value of -1 will be assumed, which is the first \"page.\"  The response from the API will include a previous_cursor and next_cursor to allow paging back and forth. See Using cursors to navigate collections for more information.  Example Values: 12893764510938
};
apiInstance.blocksList(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **includeEntities** | **String**| The entities node will not be included when set to false. Example Values: false | [optional] 
 **skipStatus** | **String**| When set to either true, t or 1 statuses will not be included in the returned user objects. | [optional] 
 **cursor** | **String**| Causes the list of blocked users to be broken into pages of no more than 5000 IDs at a time. The number of IDs returned is not guaranteed to be 5000 as suspended users are filtered out after connections are queried. If no cursor is provided, a value of -1 will be assumed, which is the first \&quot;page.\&quot;  The response from the API will include a previous_cursor and next_cursor to allow paging back and forth. See Using cursors to navigate collections for more information.  Example Values: 12893764510938 | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## directMessages

> directMessages(opts)



Returns the 20 most recent direct messages sent to the authenticating user. Includes detailed information about the sender and recipient user. You can request up to 200 direct messages per call, up to a maximum of 800 incoming DMs.  Important: This method requires an access token with RWD (read, write and direct message) permissions. Consult The Application Permission Model for more information.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'count': "count_example", // String | Specifies the number of direct messages to try and retrieve, up to a maximum of 200. The value of count is best thought of as a limit to the number of Tweets to return because suspended or deleted content is removed after the count has been applied.  Example Values: 5
  'sinceId': "sinceId_example", // String | Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occured since the since_id, the since_id will be forced to the oldest ID available. Example Values: 12345
  'maxId': "maxId_example", // String | Returns results with an ID less than (that is, older than) or equal to the specified ID.  Example Values: 54321
  'includeEntities': "includeEntities_example", // String | The entities node will not be included when set to false.  Example Values: false
  'page': "page_example", // String | Specifies the page of results to retrieve.  Example Values: 3
  'skipStatus': "skipStatus_example" // String | When set to either true, t or 1 statuses will not be included in the returned user objects.
};
apiInstance.directMessages(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **String**| Specifies the number of direct messages to try and retrieve, up to a maximum of 200. The value of count is best thought of as a limit to the number of Tweets to return because suspended or deleted content is removed after the count has been applied.  Example Values: 5 | [optional] 
 **sinceId** | **String**| Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occured since the since_id, the since_id will be forced to the oldest ID available. Example Values: 12345 | [optional] 
 **maxId** | **String**| Returns results with an ID less than (that is, older than) or equal to the specified ID.  Example Values: 54321 | [optional] 
 **includeEntities** | **String**| The entities node will not be included when set to false.  Example Values: false | [optional] 
 **page** | **String**| Specifies the page of results to retrieve.  Example Values: 3 | [optional] 
 **skipStatus** | **String**| When set to either true, t or 1 statuses will not be included in the returned user objects. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## directMessagesDestroy

> directMessagesDestroy(id, opts)



Destroys the direct message specified in the required ID parameter. The authenticating user must be the recipient of the specified direct message.  Important: This method requires an access token with RWD (read, write and direct message) permissions. Consult The Application Permission Model for more information.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let id = "id_example"; // String | The ID of the direct message to delete.  Example Values: 1270516771
let opts = {
  'includeEntities': "includeEntities_example" // String | The entities node will not be included when set to false.  Example Values: false
};
apiInstance.directMessagesDestroy(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The ID of the direct message to delete.  Example Values: 1270516771 | 
 **includeEntities** | **String**| The entities node will not be included when set to false.  Example Values: false | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## directMessagesNew

> directMessagesNew(text)



Sends a new direct message to the specified user from the authenticating user. Requires both the user and text parameters and must be a POST. Returns the sent message in the requested format if successful.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let text = "text_example"; // String | The text of your direct message. Be sure to URL encode as necessary, and keep the message under 140 characters.  Example Values: Meet me behind the cafeteria after school
apiInstance.directMessagesNew(text, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **String**| The text of your direct message. Be sure to URL encode as necessary, and keep the message under 140 characters.  Example Values: Meet me behind the cafeteria after school | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## directMessagesSent

> directMessagesSent(opts)



Returns the 20 most recent direct messages sent by the authenticating user. Includes detailed information about the sender and recipient user. You can request up to 200 direct messages per call, up to a maximum of 800 outgoing DMs.  Important: This method requires an access token with RWD (read, write and direct message) permissions. Consult The Application Permission Model for more information.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'count': "count_example", // String | Specifies the number of direct messages to try and retrieve, up to a maximum of 200. The value of count is best thought of as a limit to the number of Tweets to return because suspended or deleted content is removed after the count has been applied.  Example Values: 5
  'sinceId': "sinceId_example", // String | Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occured since the since_id, the since_id will be forced to the oldest ID available.  Example Values: 12345
  'maxId': "maxId_example", // String | Returns results with an ID less than (that is, older than) or equal to the specified ID.  Example Values: 54321
  'includeEntities': "includeEntities_example", // String | The entities node will not be included when set to false.  Example Values: false
  'page': "page_example" // String | Specifies the page of results to retrieve.  Example Values: 3
};
apiInstance.directMessagesSent(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **String**| Specifies the number of direct messages to try and retrieve, up to a maximum of 200. The value of count is best thought of as a limit to the number of Tweets to return because suspended or deleted content is removed after the count has been applied.  Example Values: 5 | [optional] 
 **sinceId** | **String**| Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occured since the since_id, the since_id will be forced to the oldest ID available.  Example Values: 12345 | [optional] 
 **maxId** | **String**| Returns results with an ID less than (that is, older than) or equal to the specified ID.  Example Values: 54321 | [optional] 
 **includeEntities** | **String**| The entities node will not be included when set to false.  Example Values: false | [optional] 
 **page** | **String**| Specifies the page of results to retrieve.  Example Values: 3 | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## directMessagesShow

> directMessagesShow(id)



Returns a single direct message, specified by an id parameter. Like the /1.1/direct_messages.format request, this method will include the user objects of the sender and recipient.  Important: This method requires an access token with RWD (read, write and direct message) permissions. Consult The Application Permission Model for more information.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let id = "id_example"; // String | The ID of the direct message.  Example Values: 587424932
apiInstance.directMessagesShow(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The ID of the direct message.  Example Values: 587424932 | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## favoritesCreate

> favoritesCreate(id, opts)



Favorites the status specified in the ID parameter as the authenticating user. Returns the favorite status when successful.  This process invoked by this method is asynchronous. The immediately returned status may not indicate the resultant favorited status of the tweet. A 200 OK response from this method will indicate whether the intended action was successful or not.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let id = "id_example"; // String | The numerical ID of the desired status.  Example Values: 123
let opts = {
  'includeEntities': "includeEntities_example" // String | The entities node will be omitted when set to false.  Example Values: false
};
apiInstance.favoritesCreate(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The numerical ID of the desired status.  Example Values: 123 | 
 **includeEntities** | **String**| The entities node will be omitted when set to false.  Example Values: false | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## favoritesDestroy

> favoritesDestroy(id, opts)



Un-favorites the status specified in the ID parameter as the authenticating user. Returns the un-favorited status in the requested format when successful.  This process invoked by this method is asynchronous. The immediately returned status may not indicate the resultant favorited status of the tweet. A 200 OK response from this method will indicate whether the intended action was successful or not.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let id = "id_example"; // String | The numerical ID of the desired status.  Example Values: 123
let opts = {
  'includeEntities': "includeEntities_example" // String | The entities node will be omitted when set to false.  Example Values: false
};
apiInstance.favoritesDestroy(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The numerical ID of the desired status.  Example Values: 123 | 
 **includeEntities** | **String**| The entities node will be omitted when set to false.  Example Values: false | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## favoritesList

> favoritesList(opts)



Returns the 20 most recent Tweets favorited by the authenticating or specified user.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'count': "count_example", // String | Specifies the number of records to retrieve. Must be less than or equal to 200. Defaults to 20.  Example Values: 5
  'sinceId': "sinceId_example", // String | Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occured since the since_id, the since_id will be forced to the oldest ID available.  Example Values: 12345
  'maxId': "maxId_example", // String | Returns results with an ID less than (that is, older than) or equal to the specified ID.  Example Values: 54321
  'includeEntities': "includeEntities_example" // String | The entities node will be omitted when set to false.  Example Values: false
};
apiInstance.favoritesList(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **String**| Specifies the number of records to retrieve. Must be less than or equal to 200. Defaults to 20.  Example Values: 5 | [optional] 
 **sinceId** | **String**| Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occured since the since_id, the since_id will be forced to the oldest ID available.  Example Values: 12345 | [optional] 
 **maxId** | **String**| Returns results with an ID less than (that is, older than) or equal to the specified ID.  Example Values: 54321 | [optional] 
 **includeEntities** | **String**| The entities node will be omitted when set to false.  Example Values: false | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## followersIds

> followersIds(opts)



Returns a cursored collection of user IDs for every user following the specified user.  At this time, results are ordered with the most recent following first — however, this ordering is subject to unannounced change and eventual consistency issues. Results are given in groups of 5,000 user IDs and multiple \&quot;pages\&quot; of results can be navigated through using the next_cursor value in subsequent requests. See Using cursors to navigate collections for more information.  This method is especially powerful when used in conjunction with GET users/lookup, a method that allows you to convert user IDs into full user objects in bulk.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'stringifyIds': "stringifyIds_example", // String | Many programming environments will not consume our Tweet ids due to their size. Provide this option to have ids returned as strings instead. Example Values: true
  'cursor': "cursor_example" // String | Causes the list of connections to be broken into pages of no more than 5000 IDs at a time. The number of IDs returned is not guaranteed to be 5000 as suspended users are filtered out after connections are queried. If no cursor is provided, a value of -1 will be assumed, which is the first \"page.\"  The response from the API will include a previous_cursor and next_cursor to allow paging back and forth.Example Values: 12893764510938
};
apiInstance.followersIds(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stringifyIds** | **String**| Many programming environments will not consume our Tweet ids due to their size. Provide this option to have ids returned as strings instead. Example Values: true | [optional] 
 **cursor** | **String**| Causes the list of connections to be broken into pages of no more than 5000 IDs at a time. The number of IDs returned is not guaranteed to be 5000 as suspended users are filtered out after connections are queried. If no cursor is provided, a value of -1 will be assumed, which is the first \&quot;page.\&quot;  The response from the API will include a previous_cursor and next_cursor to allow paging back and forth.Example Values: 12893764510938 | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## friendsIds

> friendsIds(opts)



Returns a cursored collection of user IDs for every user the specified user is following (otherwise known as their \&quot;friends\&quot;).  At this time, results are ordered with the most recent following first — however, this ordering is subject to unannounced change and eventual consistency issues. Results are given in groups of 5,000 user IDs and multiple \&quot;pages\&quot; of results can be navigated through using the next_cursor value in subsequent requests. See Using cursors to navigate collections for more information.  This method is especially powerful when used in conjunction with GET users/lookup, a method that allows you to convert user IDs into full user objects in bulk.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'stringifyIds': "stringifyIds_example", // String | Many programming environments will not consume our Tweet ids due to their size. Provide this option to have ids returned as strings instead. Example Values: true
  'cursor': "cursor_example" // String | Causes the list of connections to be broken into pages of no more than 5000 IDs at a time. The number of IDs returned is not guaranteed to be 5000 as suspended users are filtered out after connections are queried. If no cursor is provided, a value of -1 will be assumed, which is the first \"page.\"  The response from the API will include a previous_cursor and next_cursor to allow paging back and forth.Example Values: 12893764510938
};
apiInstance.friendsIds(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stringifyIds** | **String**| Many programming environments will not consume our Tweet ids due to their size. Provide this option to have ids returned as strings instead. Example Values: true | [optional] 
 **cursor** | **String**| Causes the list of connections to be broken into pages of no more than 5000 IDs at a time. The number of IDs returned is not guaranteed to be 5000 as suspended users are filtered out after connections are queried. If no cursor is provided, a value of -1 will be assumed, which is the first \&quot;page.\&quot;  The response from the API will include a previous_cursor and next_cursor to allow paging back and forth.Example Values: 12893764510938 | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## friendshipsCreate

> friendshipsCreate(opts)



Allows the authenticating users to follow the user specified in the ID parameter.  Returns the befriended user in the requested format when successful. Returns a string describing the failure condition when unsuccessful. If you are already friends with the user a HTTP 403 may be returned, though for performance reasons you may get a 200 OK message even if the friendship already exists.  Actions taken in this method are asynchronous and changes will be eventually consistent.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'follow': "follow_example" // String | Enable notifications for the target user. Example Values: true
};
apiInstance.friendshipsCreate(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **follow** | **String**| Enable notifications for the target user. Example Values: true | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## friendshipsDestroy

> friendshipsDestroy()



Allows the authenticating user to unfollow the user specified in the ID parameter.  Returns the unfollowed user in the requested format when successful. Returns a string describing the failure condition when unsuccessful.  Actions taken in this method are asynchronous and changes will be eventually consistent.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
apiInstance.friendshipsDestroy((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## friendshipsIncoming

> friendshipsIncoming(opts)



Returns the relationships of the authenticating user to the comma-separated list of up to 100 screen_names or user_ids provided. Values for connections can be: following, following_requested, followed_by, none.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'stringifyIds': "stringifyIds_example", // String | Many programming environments will not consume our Tweet ids due to their size. Provide this option to have ids returned as strings instead. Example Values: true
  'cursor': "cursor_example" // String | Causes the list of connections to be broken into pages of no more than 5000 IDs at a time. The number of IDs returned is not guaranteed to be 5000 as suspended users are filtered out after connections are queried. If no cursor is provided, a value of -1 will be assumed, which is the first \"page.\"  The response from the API will include a previous_cursor and next_cursor to allow paging back and forth.Example Values: 12893764510938
};
apiInstance.friendshipsIncoming(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stringifyIds** | **String**| Many programming environments will not consume our Tweet ids due to their size. Provide this option to have ids returned as strings instead. Example Values: true | [optional] 
 **cursor** | **String**| Causes the list of connections to be broken into pages of no more than 5000 IDs at a time. The number of IDs returned is not guaranteed to be 5000 as suspended users are filtered out after connections are queried. If no cursor is provided, a value of -1 will be assumed, which is the first \&quot;page.\&quot;  The response from the API will include a previous_cursor and next_cursor to allow paging back and forth.Example Values: 12893764510938 | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## friendshipsLookup

> friendshipsLookup()



Returns the relationships of the authenticating user to the comma-separated list of up to 100 screen_names or user_ids provided. Values for connections can be: following, following_requested, followed_by, none.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
apiInstance.friendshipsLookup((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## friendshipsOutgoing

> friendshipsOutgoing(opts)



Returns a collection of numeric IDs for every protected user for whom the authenticating user has a pending follow request.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'stringifyIds': "stringifyIds_example", // String | Many programming environments will not consume our Tweet ids due to their size. Provide this option to have ids returned as strings instead. Example Values: true
  'cursor': "cursor_example" // String | Causes the list of connections to be broken into pages of no more than 5000 IDs at a time. The number of IDs returned is not guaranteed to be 5000 as suspended users are filtered out after connections are queried. If no cursor is provided, a value of -1 will be assumed, which is the first \"page.\"  The response from the API will include a previous_cursor and next_cursor to allow paging back and forth.Example Values: 12893764510938
};
apiInstance.friendshipsOutgoing(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stringifyIds** | **String**| Many programming environments will not consume our Tweet ids due to their size. Provide this option to have ids returned as strings instead. Example Values: true | [optional] 
 **cursor** | **String**| Causes the list of connections to be broken into pages of no more than 5000 IDs at a time. The number of IDs returned is not guaranteed to be 5000 as suspended users are filtered out after connections are queried. If no cursor is provided, a value of -1 will be assumed, which is the first \&quot;page.\&quot;  The response from the API will include a previous_cursor and next_cursor to allow paging back and forth.Example Values: 12893764510938 | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## friendshipsShow

> friendshipsShow(targetId, targetScreenName, opts)



Returns detailed information about the relationship between two arbitrary users.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let targetId = "targetId_example"; // String | The user_id of the target user.  Example Values: 20
let targetScreenName = "targetScreenName_example"; // String | The screen_name of the target user.  Example Values: noradio
let opts = {
  'sourceId': "sourceId_example", // String | The user_id of the subject user.  Example Values: 3191321
  'sourceScreenName': "sourceScreenName_example" // String | The screen_name of the subject user.  Example Values: raffi
};
apiInstance.friendshipsShow(targetId, targetScreenName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **targetId** | **String**| The user_id of the target user.  Example Values: 20 | 
 **targetScreenName** | **String**| The screen_name of the target user.  Example Values: noradio | 
 **sourceId** | **String**| The user_id of the subject user.  Example Values: 3191321 | [optional] 
 **sourceScreenName** | **String**| The screen_name of the subject user.  Example Values: raffi | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## friendshipsUpdate

> friendshipsUpdate(device, retweets)



Allows one to enable or disable retweets and device notifications from the specified user.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let device = "device_example"; // String | Enable/disable device notifications from the target user. Example Values: true, false
let retweets = "retweets_example"; // String | Enable/disable retweets from the target user. Example Values: true, false
apiInstance.friendshipsUpdate(device, retweets, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | **String**| Enable/disable device notifications from the target user. Example Values: true, false | 
 **retweets** | **String**| Enable/disable retweets from the target user. Example Values: true, false | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## geoPlaceId

> geoPlaceId(placeId)



Returns all the information about a known place.Example Values: df51dec6f4ee2b2c

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let placeId = "placeId_example"; // String | A place in the world. These IDs can be retrieved from geo/reverse_geocode.  Example Values: df51dec6f4ee2b2c
apiInstance.geoPlaceId(placeId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **placeId** | **String**| A place in the world. These IDs can be retrieved from geo/reverse_geocode.  Example Values: df51dec6f4ee2b2c | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## geoPlaces

> geoPlaces(opts)



Creates a new place object at the given latitude and longitude.  Before creating a place you need to query GET geo/similar_places with the latitude, longitude and name of the place you wish to create. The query will return an array of places which are similar to the one you wish to create, and a token. If the place you wish to create isn&#39;t in the returned array you can use the token with this method to create a new one.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'attributestreetAddress': "attributestreetAddress_example", // String | This parameter searches for places which have this given street address. There are other well-known, and application specific attributes available. Custom attributes are also permitted. Learn more about Place Attributes.  Example Values: 795%20Folsom%20St
  'callback': "callback_example" // String | If supplied, the response will use the JSONP format with a callback of the given name.
};
apiInstance.geoPlaces(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attributestreetAddress** | **String**| This parameter searches for places which have this given street address. There are other well-known, and application specific attributes available. Custom attributes are also permitted. Learn more about Place Attributes.  Example Values: 795%20Folsom%20St | [optional] 
 **callback** | **String**| If supplied, the response will use the JSONP format with a callback of the given name. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## geoReverseGeocode

> geoReverseGeocode(lat, _long, opts)



Given a latitude and a longitude, searches for up to 20 places that can be used as a place_id when updating a status.  This request is an informative call and will deliver generalized results about geography

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let lat = "lat_example"; // String | The latitude to search around. This parameter will be ignored unless it is inside the range -90.0 to +90.0 (North is positive) inclusive. It will also be ignored if there isn't a corresponding long parameter.  Example Values: 37.7821120598956
let _long = "_long_example"; // String | The longitude to search around. The valid ranges for longitude is -180.0 to +180.0 (East is positive) inclusive. This parameter will be ignored if outside that range, if it is not a number, if geo_enabled is disabled, or if there not a corresponding lat parameter.  Example Values: -122.400612831116
let opts = {
  'accuracy': "accuracy_example", // String | A hint on the \"region\" in which to search. If a number, then this is a radius in meters, but it can also take a string that is suffixed with ft to specify feet. If this is not passed in, then it is assumed to be 0m. If coming from a device, in practice, this value is whatever accuracy the device has measuring its location (whether it be coming from a GPS, WiFi triangulation, etc.).  Example Values: 5ft
  'granularity': "granularity_example", // String | This is the minimal granularity of place types to return and must be one of: poi, neighborhood, city, admin or country. If no granularity is provided for the request neighborhood is assumed. Setting this to city, for example, will find places which have a type of city, admin or country.  Example Values: city
  'maxResults': "maxResults_example", // String | A hint as to the number of results to return. This does not guarantee that the number of results returned will equal max_results, but instead informs how many \"nearby\" results to return. Ideally, only pass in the number of places you intend to display to the user here.  Example Values: 3
  'callback': "callback_example" // String | If supplied, the response will use the JSONP format with a callback of the given name.
};
apiInstance.geoReverseGeocode(lat, _long, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lat** | **String**| The latitude to search around. This parameter will be ignored unless it is inside the range -90.0 to +90.0 (North is positive) inclusive. It will also be ignored if there isn&#39;t a corresponding long parameter.  Example Values: 37.7821120598956 | 
 **_long** | **String**| The longitude to search around. The valid ranges for longitude is -180.0 to +180.0 (East is positive) inclusive. This parameter will be ignored if outside that range, if it is not a number, if geo_enabled is disabled, or if there not a corresponding lat parameter.  Example Values: -122.400612831116 | 
 **accuracy** | **String**| A hint on the \&quot;region\&quot; in which to search. If a number, then this is a radius in meters, but it can also take a string that is suffixed with ft to specify feet. If this is not passed in, then it is assumed to be 0m. If coming from a device, in practice, this value is whatever accuracy the device has measuring its location (whether it be coming from a GPS, WiFi triangulation, etc.).  Example Values: 5ft | [optional] 
 **granularity** | **String**| This is the minimal granularity of place types to return and must be one of: poi, neighborhood, city, admin or country. If no granularity is provided for the request neighborhood is assumed. Setting this to city, for example, will find places which have a type of city, admin or country.  Example Values: city | [optional] 
 **maxResults** | **String**| A hint as to the number of results to return. This does not guarantee that the number of results returned will equal max_results, but instead informs how many \&quot;nearby\&quot; results to return. Ideally, only pass in the number of places you intend to display to the user here.  Example Values: 3 | [optional] 
 **callback** | **String**| If supplied, the response will use the JSONP format with a callback of the given name. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## geoSearch

> geoSearch(opts)



Search for places that can be attached to a statuses/update. Given a latitude and a longitude pair, an IP address, or a name, this request will return a list of all the valid places that can be used as the place_id when updating a status.  Conceptually, a query can be made from the user&#39;s location, retrieve a list of places, have the user validate the location he or she is at, and then send the ID of this location with a call to POST statuses/update.  This is the recommended method to use find places that can be attached to statuses/update. Unlike GET geo/reverse_geocode which provides raw data access, this endpoint can potentially re-order places with regards to the user who is authenticated. This approach is also preferred for interactive place matching with the user.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'accuracy': "accuracy_example", // String | A hint on the \"region\" in which to search. If a number, then this is a radius in meters, but it can also take a string that is suffixed with ft to specify feet. If this is not passed in, then it is assumed to be 0m. If coming from a device, in practice, this value is whatever accuracy the device has measuring its location (whether it be coming from a GPS, WiFi triangulation, etc.).  Example Values: 5ft
  'granularity': "granularity_example", // String | This is the minimal granularity of place types to return and must be one of: poi, neighborhood, city, admin or country. If no granularity is provided for the request neighborhood is assumed. Setting this to city, for example, will find places which have a type of city, admin or country.  Example Values: city
  'containedWithin': "containedWithin_example", // String | This is the place_id which you would like to restrict the search results to. Setting this value means only places within the given place_id will be found.  Specify a place_id. For example, to scope all results to places within \"San Francisco, CA USA\", you would specify a place_id of \"5a110d312052166f\"  Example Values: 247f43d441defc03
  'attributestreetAddress': "attributestreetAddress_example", // String | This parameter searches for places which have this given street address. There are other well-known, and application specific attributes available. Custom attributes are also permitted. Learn more about Place Attributes.  Example Values: 795%20Folsom%20St
  'callback': "callback_example" // String | If supplied, the response will use the JSONP format with a callback of the given name.
};
apiInstance.geoSearch(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accuracy** | **String**| A hint on the \&quot;region\&quot; in which to search. If a number, then this is a radius in meters, but it can also take a string that is suffixed with ft to specify feet. If this is not passed in, then it is assumed to be 0m. If coming from a device, in practice, this value is whatever accuracy the device has measuring its location (whether it be coming from a GPS, WiFi triangulation, etc.).  Example Values: 5ft | [optional] 
 **granularity** | **String**| This is the minimal granularity of place types to return and must be one of: poi, neighborhood, city, admin or country. If no granularity is provided for the request neighborhood is assumed. Setting this to city, for example, will find places which have a type of city, admin or country.  Example Values: city | [optional] 
 **containedWithin** | **String**| This is the place_id which you would like to restrict the search results to. Setting this value means only places within the given place_id will be found.  Specify a place_id. For example, to scope all results to places within \&quot;San Francisco, CA USA\&quot;, you would specify a place_id of \&quot;5a110d312052166f\&quot;  Example Values: 247f43d441defc03 | [optional] 
 **attributestreetAddress** | **String**| This parameter searches for places which have this given street address. There are other well-known, and application specific attributes available. Custom attributes are also permitted. Learn more about Place Attributes.  Example Values: 795%20Folsom%20St | [optional] 
 **callback** | **String**| If supplied, the response will use the JSONP format with a callback of the given name. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## geoSimilarPlaces

> geoSimilarPlaces(opts)



Locates places near the given coordinates which are similar in name.  Conceptually you would use this method to get a list of known places to choose from first. Then, if the desired place doesn&#39;t exist, make a request to POST geo/place to create a new one.  The token contained in the response is the token needed to be able to create a new place.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'containedWithin': "containedWithin_example", // String | This is the place_id which you would like to restrict the search results to. Setting this value means only places within the given place_id will be found.  Specify a place_id. For example, to scope all results to places within \"San Francisco, CA USA\", you would specify a place_id of \"5a110d312052166f\"  Example Values: 247f43d441defc03
  'attributestreetAddress': "attributestreetAddress_example", // String | This parameter searches for places which have this given street address. There are other well-known, and application specific attributes available. Custom attributes are also permitted. Learn more about Place Attributes.  Example Values: 795%20Folsom%20St
  'callback': "callback_example" // String | If supplied, the response will use the JSONP format with a callback of the given name.
};
apiInstance.geoSimilarPlaces(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **containedWithin** | **String**| This is the place_id which you would like to restrict the search results to. Setting this value means only places within the given place_id will be found.  Specify a place_id. For example, to scope all results to places within \&quot;San Francisco, CA USA\&quot;, you would specify a place_id of \&quot;5a110d312052166f\&quot;  Example Values: 247f43d441defc03 | [optional] 
 **attributestreetAddress** | **String**| This parameter searches for places which have this given street address. There are other well-known, and application specific attributes available. Custom attributes are also permitted. Learn more about Place Attributes.  Example Values: 795%20Folsom%20St | [optional] 
 **callback** | **String**| If supplied, the response will use the JSONP format with a callback of the given name. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## helpConfigurations

> helpConfigurations()



Returns the current configuration used by Twitter including twitter.com slugs which are not usernames, maximum photo resolutions, and t.co URL lengths.  It is recommended applications request this endpoint when they are loaded, but no more than once a day.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
apiInstance.helpConfigurations((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## helpLanguages

> helpLanguages()



Returns the list of languages supported by Twitter along with their ISO 639-1 code. The ISO 639-1 code is the two letter value to use if you include lang with any of your requests.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
apiInstance.helpLanguages((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## helpPrivacy

> helpPrivacy()



Returns Twitter&#39;s Privacy Policy

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
apiInstance.helpPrivacy((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## helpTos

> helpTos()



Returns the Twitter Terms of Service in the requested format. These are not the same as the Developer Rules of the Road.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
apiInstance.helpTos((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listsCreate

> listsCreate(name, opts)



Creates a new list for the authenticated user. Note that you can&#39;t create more than 20 lists per account.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let name = "name_example"; // String | The name for the list.A list's name must start with a letter and can consist only of 25 or fewer letters, numbers, \"-\", or \"_\" characters.
let opts = {
  'mode': "mode_example", // String | Whether your list is public or private. Values can be public or private. If no mode is specified the list will be public.
  'description': "description_example" // String | The description to give the list.
};
apiInstance.listsCreate(name, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| The name for the list.A list&#39;s name must start with a letter and can consist only of 25 or fewer letters, numbers, \&quot;-\&quot;, or \&quot;_\&quot; characters. | 
 **mode** | **String**| Whether your list is public or private. Values can be public or private. If no mode is specified the list will be public. | [optional] 
 **description** | **String**| The description to give the list. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listsDestroy

> listsDestroy(opts)



Deletes the specified list. The authenticated user must own the list to be able to destroy it.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'ownerScreenName': "ownerScreenName_example", // String | The screen name of the user who owns the list being requested by a slug.
  'ownerId': "ownerId_example" // String | The user ID of the user who owns the list being requested by a slug.
};
apiInstance.listsDestroy(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownerScreenName** | **String**| The screen name of the user who owns the list being requested by a slug. | [optional] 
 **ownerId** | **String**| The user ID of the user who owns the list being requested by a slug. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listsList

> listsList(screenName, userId)



Returns all lists the authenticating or specified user subscribes to, including their own. The user is specified using the user_id or screen_name parameters. If no user is given, the authenticating user is used.  This method used to be GET lists in version 1.0 of the API and has been renamed for consistency with other call.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let screenName = "screenName_example"; // String | The screen name of the user for whom to return results for. Helpful for disambiguating when a valid screen name is also a user ID.  Example Values: noradio
let userId = "userId_example"; // String | The ID of the user for whom to return results for. Helpful for disambiguating when a valid user ID is also a valid screen name.  Example Values: 12345  Note:: Specifies the ID of the user to get lists from. Helpful for disambiguating when a valid user ID is also a valid screen name.
apiInstance.listsList(screenName, userId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **screenName** | **String**| The screen name of the user for whom to return results for. Helpful for disambiguating when a valid screen name is also a user ID.  Example Values: noradio | 
 **userId** | **String**| The ID of the user for whom to return results for. Helpful for disambiguating when a valid user ID is also a valid screen name.  Example Values: 12345  Note:: Specifies the ID of the user to get lists from. Helpful for disambiguating when a valid user ID is also a valid screen name. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listsMembers

> listsMembers(opts)



Returns the members of the specified list. Private list members will only be shown if the authenticated user owns the specified list.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'ownerScreenName': "ownerScreenName_example", // String | The screen name of the user who owns the list being requested by a slug.
  'ownerId': "ownerId_example", // String | The user ID of the user who owns the list being requested by a slug.
  'includeEntities': "includeEntities_example", // String | The entities node will be disincluded when set to false.  Example Values: false
  'skipStatus': "skipStatus_example", // String | When set to either true, t or 1 statuses will not be included in the returned user objects.
  'cursor': "cursor_example" // String | Causes the collection of list members to be broken into \"pages\" of somewhat consistent size. If no cursor is provided, a value of -1 will be assumed, which is the first \"page.\"  The response from the API will include a previous_cursor and next_cursor to allow paging back and forth. See Using cursors to navigate collections for more information.  Example Values: 12893764510938
};
apiInstance.listsMembers(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownerScreenName** | **String**| The screen name of the user who owns the list being requested by a slug. | [optional] 
 **ownerId** | **String**| The user ID of the user who owns the list being requested by a slug. | [optional] 
 **includeEntities** | **String**| The entities node will be disincluded when set to false.  Example Values: false | [optional] 
 **skipStatus** | **String**| When set to either true, t or 1 statuses will not be included in the returned user objects. | [optional] 
 **cursor** | **String**| Causes the collection of list members to be broken into \&quot;pages\&quot; of somewhat consistent size. If no cursor is provided, a value of -1 will be assumed, which is the first \&quot;page.\&quot;  The response from the API will include a previous_cursor and next_cursor to allow paging back and forth. See Using cursors to navigate collections for more information.  Example Values: 12893764510938 | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listsMembersCreate

> listsMembersCreate(opts)



Add a member to a list. The authenticated user must own the list to be able to add members to it. Note that lists can&#39;t have more than 500 members.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'ownerScreenName': "ownerScreenName_example", // String | The screen name of the user who owns the list being requested by a slug.
  'ownerId': "ownerId_example" // String | The user ID of the user who owns the list being requested by a slug.
};
apiInstance.listsMembersCreate(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownerScreenName** | **String**| The screen name of the user who owns the list being requested by a slug. | [optional] 
 **ownerId** | **String**| The user ID of the user who owns the list being requested by a slug. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listsMembersCreateAll

> listsMembersCreateAll(opts)



Adds multiple members to a list, by specifying a comma-separated list of member ids or screen names. The authenticated user must own the list to be able to add members to it. Note that lists can&#39;t have more than 500 members, and you are limited to adding up to 100 members to a list at a time with this method.  Please note that there can be issues with lists that rapidly remove and add memberships. Take care when using these methods such that you are not too rapidly switching between removals and adds on the same list.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'ownerScreenName': "ownerScreenName_example", // String | The screen name of the user who owns the list being requested by a slug.
  'ownerId': "ownerId_example", // String | The user ID of the user who owns the list being requested by a slug.
  'userId': "userId_example", // String | A comma separated list of user IDs, up to 100 are allowed in a single request.
  'screenName': "screenName_example" // String | A comma separated list of screen names, up to 100 are allowed in a single request.
};
apiInstance.listsMembersCreateAll(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownerScreenName** | **String**| The screen name of the user who owns the list being requested by a slug. | [optional] 
 **ownerId** | **String**| The user ID of the user who owns the list being requested by a slug. | [optional] 
 **userId** | **String**| A comma separated list of user IDs, up to 100 are allowed in a single request. | [optional] 
 **screenName** | **String**| A comma separated list of screen names, up to 100 are allowed in a single request. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listsMembersDestroy

> listsMembersDestroy(listId, slug, opts)



Removes the specified member from the list. The authenticated user must be the list&#39;s owner to remove members from the list.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let listId = "listId_example"; // String | The numerical id of the list.
let slug = "slug_example"; // String | You can identify a list by its slug instead of its numerical id. If you decide to do so, note that you'll also have to specify the list owner using the owner_id or owner_screen_name parameters.
let opts = {
  'ownerScreenName': "ownerScreenName_example", // String | The screen name of the user who owns the list being requested by a slug.
  'ownerId': "ownerId_example", // String | The user ID of the user who owns the list being requested by a slug.
  'userId': "userId_example", // String | The ID of the user to remove from the list. Helpful for disambiguating when a valid user ID is also a valid screen name.
  'screenName': "screenName_example" // String | The screen name of the user for whom to remove from the list. Helpful for disambiguating when a valid screen name is also a user ID.
};
apiInstance.listsMembersDestroy(listId, slug, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listId** | **String**| The numerical id of the list. | 
 **slug** | **String**| You can identify a list by its slug instead of its numerical id. If you decide to do so, note that you&#39;ll also have to specify the list owner using the owner_id or owner_screen_name parameters. | 
 **ownerScreenName** | **String**| The screen name of the user who owns the list being requested by a slug. | [optional] 
 **ownerId** | **String**| The user ID of the user who owns the list being requested by a slug. | [optional] 
 **userId** | **String**| The ID of the user to remove from the list. Helpful for disambiguating when a valid user ID is also a valid screen name. | [optional] 
 **screenName** | **String**| The screen name of the user for whom to remove from the list. Helpful for disambiguating when a valid screen name is also a user ID. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listsMembersDestroyAll

> listsMembersDestroyAll(opts)



Removes multiple members from a list, by specifying a comma-separated list of member ids or screen names. The authenticated user must own the list to be able to remove members from it. Note that lists can&#39;t have more than 500 members, and you are limited to removing up to 100 members to a list at a time with this method.  Please note that there can be issues with lists that rapidly remove and add memberships. Take care when using these methods such that you are not too rapidly switching between removals and adds on the same list.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'ownerScreenName': "ownerScreenName_example", // String | The screen name of the user who owns the list being requested by a slug.
  'ownerId': "ownerId_example", // String | The user ID of the user who owns the list being requested by a slug.
  'screenName': "screenName_example", // String | A comma separated list of screen names, up to 100 are allowed in a single request.
  'userId': "userId_example" // String | A comma separated list of user IDs, up to 100 are allowed in a single request.
};
apiInstance.listsMembersDestroyAll(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownerScreenName** | **String**| The screen name of the user who owns the list being requested by a slug. | [optional] 
 **ownerId** | **String**| The user ID of the user who owns the list being requested by a slug. | [optional] 
 **screenName** | **String**| A comma separated list of screen names, up to 100 are allowed in a single request. | [optional] 
 **userId** | **String**| A comma separated list of user IDs, up to 100 are allowed in a single request. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listsMembersShow

> listsMembersShow(opts)



Check if the specified user is a member of the specified list.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'ownerScreenName': "ownerScreenName_example", // String | The screen name of the user who owns the list being requested by a slug.
  'ownerId': "ownerId_example", // String | The user ID of the user who owns the list being requested by a slug.
  'includeEntities': "includeEntities_example", // String | When set to either true, t or 1, each tweet will include a node called \"entities\". This node offers a variety of metadata about the tweet in a discreet structure, including: user_mentions, urls, and hashtags. While entities are opt-in on timelines at present, they will be made a default component of output in the future.
  'skipStatus': "skipStatus_example" // String | When set to either true, t or 1 statuses will not be included in the returned user objects.
};
apiInstance.listsMembersShow(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownerScreenName** | **String**| The screen name of the user who owns the list being requested by a slug. | [optional] 
 **ownerId** | **String**| The user ID of the user who owns the list being requested by a slug. | [optional] 
 **includeEntities** | **String**| When set to either true, t or 1, each tweet will include a node called \&quot;entities\&quot;. This node offers a variety of metadata about the tweet in a discreet structure, including: user_mentions, urls, and hashtags. While entities are opt-in on timelines at present, they will be made a default component of output in the future. | [optional] 
 **skipStatus** | **String**| When set to either true, t or 1 statuses will not be included in the returned user objects. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listsMemberships

> listsMemberships(opts)



Returns the lists the specified user has been added to. If user_id or screen_name are not provided the memberships for the authenticating user are returned.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'userId': "userId_example", // String | The ID of the user for whom to return results for. Helpful for disambiguating when a valid user ID is also a valid screen name.
  'screenName': "screenName_example", // String | The screen name of the user for whom to return results for. Helpful for disambiguating when a valid screen name is also a user ID.
  'cursor': "cursor_example", // String | Breaks the results into pages. A single page contains 20 lists. Provide a value of -1 to begin paging. Provide values as returned in the response body's next_cursor and previous_cursor attributes to page back and forth in the list.
  'filterToOwnedLists': "filterToOwnedLists_example" // String | When set to true, t or 1, will return just lists the authenticating user owns, and the user represented by user_id or screen_name is a member of.
};
apiInstance.listsMemberships(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userId** | **String**| The ID of the user for whom to return results for. Helpful for disambiguating when a valid user ID is also a valid screen name. | [optional] 
 **screenName** | **String**| The screen name of the user for whom to return results for. Helpful for disambiguating when a valid screen name is also a user ID. | [optional] 
 **cursor** | **String**| Breaks the results into pages. A single page contains 20 lists. Provide a value of -1 to begin paging. Provide values as returned in the response body&#39;s next_cursor and previous_cursor attributes to page back and forth in the list. | [optional] 
 **filterToOwnedLists** | **String**| When set to true, t or 1, will return just lists the authenticating user owns, and the user represented by user_id or screen_name is a member of. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listsShow

> listsShow(opts)



Returns the specified list. Private lists will only be shown if the authenticated user owns the specified list.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'ownerScreenName': "ownerScreenName_example", // String | The screen name of the user who owns the list being requested by a slug.
  'ownerId': "ownerId_example" // String | The user ID of the user who owns the list being requested by a slug.
};
apiInstance.listsShow(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownerScreenName** | **String**| The screen name of the user who owns the list being requested by a slug. | [optional] 
 **ownerId** | **String**| The user ID of the user who owns the list being requested by a slug. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listsStatuses

> listsStatuses(includeRts, opts)



Returns tweet timeline for members of the specified list. Retweets are included by default. You can use the include_rts&#x3D;false parameter to omit retweet objects.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let includeRts = "includeRts_example"; // String | When set to either true, t or 1, the list timeline will contain native retweets (if they exist) in addition to the standard stream of tweets. The output format of retweeted tweets is identical to the representation you see in home_timeline.
let opts = {
  'ownerScreenName': "ownerScreenName_example", // String | The screen name of the user who owns the list being requested by a slug.
  'ownerId': "ownerId_example", // String | The user ID of the user who owns the list being requested by a slug.
  'sinceId': "sinceId_example", // String | Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occured since the since_id, the since_id will be forced to the oldest ID available.
  'maxId': "maxId_example", // String | Returns results with an ID less than (that is, older than) or equal to the specified ID.
  'count': "count_example", // String | Specifies the number of results to retrieve per \"page.
  'includeEntities': "includeEntities_example" // String | Entities are ON by default in API 1.1, each tweet includes a node called \"entities\". This node offers a variety of metadata about the tweet in a discreet structure, including: user_mentions, urls, and hashtags. You can omit entities from the result by using include_entities=false
};
apiInstance.listsStatuses(includeRts, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **includeRts** | **String**| When set to either true, t or 1, the list timeline will contain native retweets (if they exist) in addition to the standard stream of tweets. The output format of retweeted tweets is identical to the representation you see in home_timeline. | 
 **ownerScreenName** | **String**| The screen name of the user who owns the list being requested by a slug. | [optional] 
 **ownerId** | **String**| The user ID of the user who owns the list being requested by a slug. | [optional] 
 **sinceId** | **String**| Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occured since the since_id, the since_id will be forced to the oldest ID available. | [optional] 
 **maxId** | **String**| Returns results with an ID less than (that is, older than) or equal to the specified ID. | [optional] 
 **count** | **String**| Specifies the number of results to retrieve per \&quot;page. | [optional] 
 **includeEntities** | **String**| Entities are ON by default in API 1.1, each tweet includes a node called \&quot;entities\&quot;. This node offers a variety of metadata about the tweet in a discreet structure, including: user_mentions, urls, and hashtags. You can omit entities from the result by using include_entities&#x3D;false | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listsSubscribers

> listsSubscribers(opts)



Returns the subscribers of the specified list. Private list subscribers will only be shown if the authenticated user owns the specified list.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'ownerScreenName': "ownerScreenName_example", // String | The screen name of the user who owns the list being requested by a slug.
  'ownerId': "ownerId_example", // String | The user ID of the user who owns the list being requested by a slug.
  'cursor': "cursor_example", // String | Breaks the results into pages. A single page contains 20 lists. Provide a value of -1 to begin paging. Provide values as returned in the response body's next_cursor and previous_cursor attributes to page back and forth in the list.
  'includeEntities': "includeEntities_example", // String | When set to either true, t or 1, each tweet will include a node called \"entities\". This node offers a variety of metadata about the tweet in a discreet structure, including: user_mentions, urls, and hashtags. While entities are opt-in on timelines at present, they will be made a default component of output in the future. See Tweet Entities for more details.
  'skipStatus': "skipStatus_example" // String | When set to either true, t or 1 statuses will not be included in the returned user objects.
};
apiInstance.listsSubscribers(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownerScreenName** | **String**| The screen name of the user who owns the list being requested by a slug. | [optional] 
 **ownerId** | **String**| The user ID of the user who owns the list being requested by a slug. | [optional] 
 **cursor** | **String**| Breaks the results into pages. A single page contains 20 lists. Provide a value of -1 to begin paging. Provide values as returned in the response body&#39;s next_cursor and previous_cursor attributes to page back and forth in the list. | [optional] 
 **includeEntities** | **String**| When set to either true, t or 1, each tweet will include a node called \&quot;entities\&quot;. This node offers a variety of metadata about the tweet in a discreet structure, including: user_mentions, urls, and hashtags. While entities are opt-in on timelines at present, they will be made a default component of output in the future. See Tweet Entities for more details. | [optional] 
 **skipStatus** | **String**| When set to either true, t or 1 statuses will not be included in the returned user objects. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listsSubscribersCreate

> listsSubscribersCreate(opts)



Subscribes the authenticated user to the specified list.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'ownerScreenName': "ownerScreenName_example", // String | The screen name of the user who owns the list being requested by a slug.
  'ownerId': "ownerId_example" // String | The user ID of the user who owns the list being requested by a slug.
};
apiInstance.listsSubscribersCreate(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownerScreenName** | **String**| The screen name of the user who owns the list being requested by a slug. | [optional] 
 **ownerId** | **String**| The user ID of the user who owns the list being requested by a slug. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listsSubscribersDestroy

> listsSubscribersDestroy(opts)



Unsubscribes the authenticated user from the specified list.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'ownerScreenName': "ownerScreenName_example", // String | The screen name of the user who owns the list being requested by a slug.
  'ownerId': "ownerId_example" // String | The user ID of the user who owns the list being requested by a slug.
};
apiInstance.listsSubscribersDestroy(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownerScreenName** | **String**| The screen name of the user who owns the list being requested by a slug. | [optional] 
 **ownerId** | **String**| The user ID of the user who owns the list being requested by a slug. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listsSubscribersShow

> listsSubscribersShow(opts)



Check if the specified user is a subscriber of the specified list. Returns the user if they are subscriber.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'ownerScreenName': "ownerScreenName_example", // String | The screen name of the user who owns the list being requested by a slug.
  'ownerId': "ownerId_example", // String | The user ID of the user who owns the list being requested by a slug.
  'includeEntities': "includeEntities_example", // String | When set to either true, t or 1, each tweet will include a node called \"entities\". This node offers a variety of metadata about the tweet in a discreet structure, including: user_mentions, urls, and hashtags. While entities are opt-in on timelines at present, they will be made a default component of output in the future. See Tweet Entities for more details.
  'skipStatus': "skipStatus_example" // String | When set to either true, t or 1 statuses will not be included in the returned user objects.
};
apiInstance.listsSubscribersShow(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownerScreenName** | **String**| The screen name of the user who owns the list being requested by a slug. | [optional] 
 **ownerId** | **String**| The user ID of the user who owns the list being requested by a slug. | [optional] 
 **includeEntities** | **String**| When set to either true, t or 1, each tweet will include a node called \&quot;entities\&quot;. This node offers a variety of metadata about the tweet in a discreet structure, including: user_mentions, urls, and hashtags. While entities are opt-in on timelines at present, they will be made a default component of output in the future. See Tweet Entities for more details. | [optional] 
 **skipStatus** | **String**| When set to either true, t or 1 statuses will not be included in the returned user objects. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listsSubscriptions

> listsSubscriptions(opts)



Obtain a collection of the lists the specified user is subscribed to, 20 lists per page by default. Does not include the user&#39;s own lists.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'count': "count_example", // String | The amount of results to return per page. Defaults to 20. Maximum of 1,000 when using cursors.
  'cursor': "cursor_example" // String | Breaks the results into pages. A single page contains 20 lists. Provide a value of -1 to begin paging. Provide values as returned in the response body's next_cursor and previous_cursor attributes to page back and forth in the list. It is recommended to always use cursors when the method supports them.
};
apiInstance.listsSubscriptions(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **String**| The amount of results to return per page. Defaults to 20. Maximum of 1,000 when using cursors. | [optional] 
 **cursor** | **String**| Breaks the results into pages. A single page contains 20 lists. Provide a value of -1 to begin paging. Provide values as returned in the response body&#39;s next_cursor and previous_cursor attributes to page back and forth in the list. It is recommended to always use cursors when the method supports them. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listsUpdate

> listsUpdate(opts)



Updates the specified list. The authenticated user must own the list to be able to update it.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'ownerScreenName': "ownerScreenName_example", // String | The screen name of the user who owns the list being requested by a slug.
  'ownerId': "ownerId_example", // String | The user ID of the user who owns the list being requested by a slug.
  'name': "name_example", // String | The name for the list.
  'mode': "mode_example", // String | Whether your list is public or private. Values can be public or private. If no mode is specified the list will be public.
  'description': "description_example" // String | The description to give the list.
};
apiInstance.listsUpdate(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ownerScreenName** | **String**| The screen name of the user who owns the list being requested by a slug. | [optional] 
 **ownerId** | **String**| The user ID of the user who owns the list being requested by a slug. | [optional] 
 **name** | **String**| The name for the list. | [optional] 
 **mode** | **String**| Whether your list is public or private. Values can be public or private. If no mode is specified the list will be public. | [optional] 
 **description** | **String**| The description to give the list. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## savedSearchesCreate

> savedSearchesCreate(query)



Create a new saved search for the authenticated user. A user may only have 25 saved searches.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let query = "query_example"; // String | The query of the search the user would like to save.
apiInstance.savedSearchesCreate(query, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **String**| The query of the search the user would like to save. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## savedSearchesDestroy

> savedSearchesDestroy(id)



Destroys a saved search for the authenticating user. The authenticating user must be the owner of saved search id being destroyed.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let id = "id_example"; // String | The ID of the saved search.  Example Values: 313006
apiInstance.savedSearchesDestroy(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The ID of the saved search.  Example Values: 313006 | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## savedSearchesList

> savedSearchesList()



Returns the authenticated user&#39;s saved search queries.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
apiInstance.savedSearchesList((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## savedsearchesid

> savedsearchesid(id)



Returns the authenticated user&#39;s saved search queries.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let id = "id_example"; // String | The ID of the saved search.  Example Values: 313006
apiInstance.savedsearchesid(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The ID of the saved search.  Example Values: 313006 | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## searchTweets

> searchTweets(q, opts)



Returns a collection of relevant Tweets matching a specified query.  Please note that Twitter&#39;s search service and, by extension, the Search API is not meant to be an exhaustive source of Tweets. Not all Tweets will be indexed or made available via the search interface.  In API v1.1, the response format of the Search API has been improved to return Tweet objects more similar to the objects you&#39;ll find across the REST API and platform. You may need to tolerate some inconsistencies and variance in perspectival values (fields that pertain to the perspective of the authenticating user) and embedded user objects.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let q = "q_example"; // String | A UTF-8, URL-encoded search query of 1,000 characters maximum, including operators. Queries may additionally be limited by complexity.Example: @noradio.
let opts = {
  'geocode': "geocode_example", // String | Returns tweets by users located within a given radius of the given latitude/longitude. The location is preferentially taking from the Geotagging API, but will fall back to their Twitter profile. The parameter value is specified by \"latitude,longitude,radius\", where radius units must be specified as either \"mi\" (miles) or \"km\" (kilometers). Note that you cannot use the near operator via the API to geocode arbitrary locations; however you can use this geocode parameter to search near geocodes directly. A maximum of 1,000 distinct \"sub-regions\" will be considered when using the radius modifier.
  'lang': "lang_example", // String | Restricts tweets to the given language, given by an ISO 639-1 code. Language detection is best-effort.Example Values: eu
  'locale': "locale_example", // String | Specify the language of the query you are sending (only ja is currently effective). This is intended for language-specific consumers and the default should work in the majority of cases.Example Values: ja
  'resultType': "resultType_example", // String | Optional. Specifies what type of search results you would prefer to receive. The current default is \"mixed.\" Valid values include: * mixed: Include both popular and real time results in the response. * recent: return only the most recent results in the response * popular: return only the most popular results in the response. Example Values: mixed, recent, popular
  'count': "count_example", // String | The number of tweets to return per page, up to a maximum of 100. Defaults to 15. This was formerly the \"rpp\" parameter in the old Search API. Example Values: 100
  'until': "until_example", // String | Returns tweets generated before the given date. Date should be formatted as YYYY-MM-DD. Keep in mind that the search index may not go back as far as the date you specify here. Example Values: 2012-09-01
  'sinceId': "sinceId_example", // String | Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occured since the since_id, the since_id will be forced to the oldest ID available. Example Values: 12345
  'maxId': "maxId_example", // String | Returns results with an ID less than (that is, older than) or equal to the specified ID. Example Values: 12345
  'includeEntities': "includeEntities_example", // String | The entities node will be disincluded when set to false. Example Values: false
  'callback': "callback_example" // String | If supplied, the response will use the JSONP format with a callback of the given name. The usefulness of this parameter is somewhat diminished by the requirement of authentication for requests to this endpoint. Example Values: processTweets
};
apiInstance.searchTweets(q, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **String**| A UTF-8, URL-encoded search query of 1,000 characters maximum, including operators. Queries may additionally be limited by complexity.Example: @noradio. | 
 **geocode** | **String**| Returns tweets by users located within a given radius of the given latitude/longitude. The location is preferentially taking from the Geotagging API, but will fall back to their Twitter profile. The parameter value is specified by \&quot;latitude,longitude,radius\&quot;, where radius units must be specified as either \&quot;mi\&quot; (miles) or \&quot;km\&quot; (kilometers). Note that you cannot use the near operator via the API to geocode arbitrary locations; however you can use this geocode parameter to search near geocodes directly. A maximum of 1,000 distinct \&quot;sub-regions\&quot; will be considered when using the radius modifier. | [optional] 
 **lang** | **String**| Restricts tweets to the given language, given by an ISO 639-1 code. Language detection is best-effort.Example Values: eu | [optional] 
 **locale** | **String**| Specify the language of the query you are sending (only ja is currently effective). This is intended for language-specific consumers and the default should work in the majority of cases.Example Values: ja | [optional] 
 **resultType** | **String**| Optional. Specifies what type of search results you would prefer to receive. The current default is \&quot;mixed.\&quot; Valid values include: * mixed: Include both popular and real time results in the response. * recent: return only the most recent results in the response * popular: return only the most popular results in the response. Example Values: mixed, recent, popular | [optional] 
 **count** | **String**| The number of tweets to return per page, up to a maximum of 100. Defaults to 15. This was formerly the \&quot;rpp\&quot; parameter in the old Search API. Example Values: 100 | [optional] 
 **until** | **String**| Returns tweets generated before the given date. Date should be formatted as YYYY-MM-DD. Keep in mind that the search index may not go back as far as the date you specify here. Example Values: 2012-09-01 | [optional] 
 **sinceId** | **String**| Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occured since the since_id, the since_id will be forced to the oldest ID available. Example Values: 12345 | [optional] 
 **maxId** | **String**| Returns results with an ID less than (that is, older than) or equal to the specified ID. Example Values: 12345 | [optional] 
 **includeEntities** | **String**| The entities node will be disincluded when set to false. Example Values: false | [optional] 
 **callback** | **String**| If supplied, the response will use the JSONP format with a callback of the given name. The usefulness of this parameter is somewhat diminished by the requirement of authentication for requests to this endpoint. Example Values: processTweets | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## statusesDestroy

> statusesDestroy(id, opts)



Destroys the status specified by the required ID parameter. The authenticating user must be the author of the specified status. Returns the destroyed status if successful.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let id = "id_example"; // String | The numerical ID of the desired status.
let opts = {
  'trimUser': "trimUser_example" // String | When set to either true, t or 1, each tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object.
};
apiInstance.statusesDestroy(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The numerical ID of the desired status. | 
 **trimUser** | **String**| When set to either true, t or 1, each tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## statusesHomeTimeline

> statusesHomeTimeline(opts)



Returns a collection of the most recent Tweets and retweets posted by the authenticating user and the users they follow. The home timeline is central to how most users interact with the Twitter service.  Up to 800 Tweets are obtainable on the home timeline. It is more volatile for users that follow many users or follow users who tweet frequently.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'count': 56, // Number | Specifies the number of records to retrieve. Must be less than or equal to 200.
  'maxId': 789, // Number | Returns results with an ID less than (that is, older than) or equal to the specified ID.
  'sinceId': 789, // Number | Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occured since the since_id, the since_id will be forced to the oldest ID available.
  'trimUser': "trimUser_example", // String | When set to either true, t or 1, each tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object.
  'excludeReplies': "excludeReplies_example", // String | This parameter will prevent replies from appearing in the returned timeline. Using exclude_replies with the count parameter will mean you will receive up-to count tweets — this is because the count parameter retrieves that many tweets before filtering out retweets and replies.
  'contributorDetails': "contributorDetails_example" // String | This parameter enhances the contributors element of the status response to include the screen_name of the contributor. By default only the user_id of the contributor is included.
};
apiInstance.statusesHomeTimeline(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **Number**| Specifies the number of records to retrieve. Must be less than or equal to 200. | [optional] 
 **maxId** | **Number**| Returns results with an ID less than (that is, older than) or equal to the specified ID. | [optional] 
 **sinceId** | **Number**| Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occured since the since_id, the since_id will be forced to the oldest ID available. | [optional] 
 **trimUser** | **String**| When set to either true, t or 1, each tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object. | [optional] 
 **excludeReplies** | **String**| This parameter will prevent replies from appearing in the returned timeline. Using exclude_replies with the count parameter will mean you will receive up-to count tweets — this is because the count parameter retrieves that many tweets before filtering out retweets and replies. | [optional] 
 **contributorDetails** | **String**| This parameter enhances the contributors element of the status response to include the screen_name of the contributor. By default only the user_id of the contributor is included. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## statusesMentionsTimeline

> statusesMentionsTimeline(opts)



Returns the 20 most recent mentions (tweets containing a users&#39;s @screen_name) for the authenticating user.The timeline returned is the equivalent of the one seen when you view your mentions on twitter.com.This method can only return up to 800 statuses.This method will include retweets in the JSON response regardless of whether the include_rts parameter is set.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'count': 56, // Number | Specifies the number of tweets to try and retrieve, up to a maximum of 200. The value of count is best thought of as a limit to the number of tweets to return because suspended or deleted content is removed after the count has been applied. We include retweets in the count, even if include_rts is not supplied. It is recommended you always send include_rts=1 when using this API method.
  'sinceId': 789, // Number | Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occured since the since_id, the since_id will be forced to the oldest ID available.
  'maxId': 789, // Number | Returns results with an ID less than (that is, older than) or equal to the specified ID.
  'trimUser': "trimUser_example", // String | When set to either true, t or 1, each tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object.
  'contributorDetails': "contributorDetails_example", // String | This parameter enhances the contributors element of the status response to include the screen_name of the contributor. By default only the user_id of the contributor is included.
  'includeEntities': true // Boolean | The entities node will be disincluded when set to false.
};
apiInstance.statusesMentionsTimeline(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **Number**| Specifies the number of tweets to try and retrieve, up to a maximum of 200. The value of count is best thought of as a limit to the number of tweets to return because suspended or deleted content is removed after the count has been applied. We include retweets in the count, even if include_rts is not supplied. It is recommended you always send include_rts&#x3D;1 when using this API method. | [optional] 
 **sinceId** | **Number**| Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occured since the since_id, the since_id will be forced to the oldest ID available. | [optional] 
 **maxId** | **Number**| Returns results with an ID less than (that is, older than) or equal to the specified ID. | [optional] 
 **trimUser** | **String**| When set to either true, t or 1, each tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object. | [optional] 
 **contributorDetails** | **String**| This parameter enhances the contributors element of the status response to include the screen_name of the contributor. By default only the user_id of the contributor is included. | [optional] 
 **includeEntities** | **Boolean**| The entities node will be disincluded when set to false. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## statusesOembed

> statusesOembed(opts)



Returns information allowing the creation of an embedded representation of a Tweet on third party sites. See the oEmbed specification (http://oembed.com) for information about the response format. Either the id or url parameters must be specified in a request, it is not necessary to include both. While this endpoint allows a bit of customization for the final appearance of the embedded Tweet, be aware that the appearance of the rendered Tweet may change over time to be consistent with Twitter&#39;s Display Guidelines (https://dev.twitter.com/terms/display-guidelines). Do not rely on any class or id parameters to stay constant in the returned markup.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'maxwidth': 56, // Number | The maximum width in pixels that the embed should be rendered at. This value is constrained to be between 250 and 550 pixels. Note that Twitter does not support the oEmbed maxheight parameter. Tweets are fundamentally text, and are therefore of unpredictable height that cannot be scaled like an image or video. Relatedly, the oEmbed response will not provide a value for height. Implementations that need consistent heights for Tweets should refer to the hide_thread and hide_media parameters below.
  'hideMedia': "hideMedia_example", // String | Specifies whether the embedded Tweet should automatically expand images which were uploaded via POST statuses/update_with_media. When set to either true, t or 1 images will not be expanded. Defaults to false.
  'hideThread': "hideThread_example", // String | Specifies whether the embedded Tweet should automatically show the original message in the case that the embedded Tweet is a reply. When set to either true, t or 1 the original Tweet will not be shown. Defaults to false.
  'omitScript': "omitScript_example", // String | Specifies whether the embedded Tweet HTML should include a 'script' element pointing to widgets.js. In cases where a page already includes widgets.js, setting this value to true will prevent a redundant script element from being included. When set to either true, t or 1 the 'script'element will not be included in the embed HTML, meaning that pages must include a reference to widgets.js manually. Defaults to false.
  'align': "align_example", // String | Specifies whether the embedded Tweet should be left aligned, right aligned, or centered in the page. Valid values are left, right, center, and none. Defaults to none, meaning no alignment styles are specified for the Tweet.
  'related': "related_example", // String | A value for the TWT related parameter, as described in Web Intents (https://dev.twitter.com/docs/intents). This value will be forwarded to all Web Intents calls. Example values: twitterapi, twittermedia, twitter.
  'lang': "lang_example" // String | Language code for the rendered embed. This will affect the text and localization of the rendered HTML. Example value: fr
};
apiInstance.statusesOembed(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **maxwidth** | **Number**| The maximum width in pixels that the embed should be rendered at. This value is constrained to be between 250 and 550 pixels. Note that Twitter does not support the oEmbed maxheight parameter. Tweets are fundamentally text, and are therefore of unpredictable height that cannot be scaled like an image or video. Relatedly, the oEmbed response will not provide a value for height. Implementations that need consistent heights for Tweets should refer to the hide_thread and hide_media parameters below. | [optional] 
 **hideMedia** | **String**| Specifies whether the embedded Tweet should automatically expand images which were uploaded via POST statuses/update_with_media. When set to either true, t or 1 images will not be expanded. Defaults to false. | [optional] 
 **hideThread** | **String**| Specifies whether the embedded Tweet should automatically show the original message in the case that the embedded Tweet is a reply. When set to either true, t or 1 the original Tweet will not be shown. Defaults to false. | [optional] 
 **omitScript** | **String**| Specifies whether the embedded Tweet HTML should include a &#39;script&#39; element pointing to widgets.js. In cases where a page already includes widgets.js, setting this value to true will prevent a redundant script element from being included. When set to either true, t or 1 the &#39;script&#39;element will not be included in the embed HTML, meaning that pages must include a reference to widgets.js manually. Defaults to false. | [optional] 
 **align** | **String**| Specifies whether the embedded Tweet should be left aligned, right aligned, or centered in the page. Valid values are left, right, center, and none. Defaults to none, meaning no alignment styles are specified for the Tweet. | [optional] 
 **related** | **String**| A value for the TWT related parameter, as described in Web Intents (https://dev.twitter.com/docs/intents). This value will be forwarded to all Web Intents calls. Example values: twitterapi, twittermedia, twitter. | [optional] 
 **lang** | **String**| Language code for the rendered embed. This will affect the text and localization of the rendered HTML. Example value: fr | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## statusesRetweets

> statusesRetweets(id, opts)



Returns up to 100 of the first retweets of a given tweet.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let id = "id_example"; // String | The numerical ID of the desired status.
let opts = {
  'count': "count_example", // String | Specifies the number of records to retrieve. Must be less than or equal to 100.
  'trimUser': "trimUser_example" // String | When set to either true, t or 1, each tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object.
};
apiInstance.statusesRetweets(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The numerical ID of the desired status. | 
 **count** | **String**| Specifies the number of records to retrieve. Must be less than or equal to 100. | [optional] 
 **trimUser** | **String**| When set to either true, t or 1, each tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## statusesShow

> statusesShow(id, opts)



Returns a single status, specified by the id parameter below. The status&#39;s author will be returned inline.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let id = "id_example"; // String | The numerical ID of the desired status.
let opts = {
  'trimUser': "trimUser_example", // String | When set to either true, t or 1, each tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object.
  'includeMyRetweet': "includeMyRetweet_example", // String | When set to either true, t or 1, any Tweets returned that have been retweeted by the authenticating user will include an additional current_user_retweet node, containing the ID of the source status for the retweet.
  'includeEntities': "includeEntities_example" // String | The entities node will be disincluded when set to false.
};
apiInstance.statusesShow(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The numerical ID of the desired status. | 
 **trimUser** | **String**| When set to either true, t or 1, each tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object. | [optional] 
 **includeMyRetweet** | **String**| When set to either true, t or 1, any Tweets returned that have been retweeted by the authenticating user will include an additional current_user_retweet node, containing the ID of the source status for the retweet. | [optional] 
 **includeEntities** | **String**| The entities node will be disincluded when set to false. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## statusesUpdate

> statusesUpdate(status, opts)



Updates the authenticating user&#39;s status, also known as tweeting. To upload an image to accompany the tweet, use POST statuses/update_with_media (https://dev.twitter.com/docs/api/1/post/statuses/update_with_media). For each update attempt, the update text is compared with the authenticating user&#39;s recent tweets. Any attempt that would result in duplication will be blocked, resulting in a 403 error. Therefore, a user cannot submit the same status twice in a row. While not rate limited by the API a user is limited in the number of tweets they can create at a time. If the number of updates posted by the user reaches the current allowed limit this method will return an HTTP 403 error.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let status = "'Posting from @apigee's API test console. It's like a command line for the Twitter API! #apitools'"; // String | The text of your status update, typically up to 140 characters. URL encode as necessary. t.co link short-url wrapping (https://dev.twitter.com/docs/tco-link-wrapper/faq) may effect character counts.
let opts = {
  'inReplyToStatusId': "inReplyToStatusId_example", // String | The ID of an existing status that the update is in reply to. Note: This parameter will be ignored unless the author of the tweet this parameter references is mentioned within the status text. Therefore, you must include @username, where username is the author of the referenced tweet, within the update.
  'lat': "'37.426363'", // String | The latitude of the location this tweet refers to. This parameter will be ignored unless it is inside the range -90.0 to +90.0 (North is positive) inclusive. It will also be ignored if there isn't a corresponding long parameter.
  '_long': "'-122.141114'", // String | The longitude of the location this tweet refers to. The valid ranges for longitude is -180.0 to +180.0 (East is positive) inclusive. This parameter will be ignored if outside that range, if it is not a number, if geo_enabled is disabled, or if there not a corresponding lat parameter.
  'placeId': "placeId_example", // String | A place in the world. These IDs can be retrieved from GET geo/reverse_geocode (https://dev.twitter.com/docs/api/1/get/geo/reverse_geocode).
  'displayCoordinates': "'false'", // String | Whether or not to put a pin on the exact coordinates a tweet has been sent from.
  'trimUser': "trimUser_example" // String | When set to either true, t or 1, each tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object.
};
apiInstance.statusesUpdate(status, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **String**| The text of your status update, typically up to 140 characters. URL encode as necessary. t.co link short-url wrapping (https://dev.twitter.com/docs/tco-link-wrapper/faq) may effect character counts. | [default to &#39;Posting from @apigee&#39;s API test console. It&#39;s like a command line for the Twitter API! #apitools&#39;]
 **inReplyToStatusId** | **String**| The ID of an existing status that the update is in reply to. Note: This parameter will be ignored unless the author of the tweet this parameter references is mentioned within the status text. Therefore, you must include @username, where username is the author of the referenced tweet, within the update. | [optional] 
 **lat** | **String**| The latitude of the location this tweet refers to. This parameter will be ignored unless it is inside the range -90.0 to +90.0 (North is positive) inclusive. It will also be ignored if there isn&#39;t a corresponding long parameter. | [optional] [default to &#39;37.426363&#39;]
 **_long** | **String**| The longitude of the location this tweet refers to. The valid ranges for longitude is -180.0 to +180.0 (East is positive) inclusive. This parameter will be ignored if outside that range, if it is not a number, if geo_enabled is disabled, or if there not a corresponding lat parameter. | [optional] [default to &#39;-122.141114&#39;]
 **placeId** | **String**| A place in the world. These IDs can be retrieved from GET geo/reverse_geocode (https://dev.twitter.com/docs/api/1/get/geo/reverse_geocode). | [optional] 
 **displayCoordinates** | **String**| Whether or not to put a pin on the exact coordinates a tweet has been sent from. | [optional] [default to &#39;false&#39;]
 **trimUser** | **String**| When set to either true, t or 1, each tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## statusesUpdateWithMedia

> statusesUpdateWithMedia(status, media, contentType, opts)



Updates the authenticating user&#39;s status and attaches media for upload. Unlike POST statuses/update (https://dev.twitter.com/docs/api/1.1/post/statuses/update), this method expects raw multipart data. Your POST request&#39;s Content-Type should be set to multipart/form-data with the media[] parameter. The Tweet text will be rewritten to include the media URL(s), which will reduce the number of characters allowed in the Tweet text. If the URL(s) cannot be appended without text truncation, the tweet will be rejected and this method will return an HTTP 403 error. Important: Make sure that you&#39;re using upload.twitter.com as your host while posting statuses with media. It is strongly recommended to use SSL with this method.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let status = "status_example"; // String | The text of your status update. URL encode as necessary. t.co link wrapping (https://dev.twitter.com/docs/tco-link-wrapper/faq) may affect character counts if the post contains URLs. You must additionally account for the characters_reserved_per_media per uploaded media, additionally accounting for space characters in between finalized URLs. Note: Request the GET help/configuration (https://dev.twitter.com/docs/api/1.1/get/help/configuration) endpoint to get the current characters_reserved_per_media and max_media_per_upload values.
let media = "media_example"; // String | Up to max_media_per_upload files may be specified in the request, each named media[]. Supported image formats are PNG, JPG and GIF. Animated GIFs are not supported. Note: Request the GET help/configuration (https://dev.twitter.com/docs/api/1.1/get/help/configuration) endpoint to get the current max_media_per_upload and photo_size_limit values.
let contentType = "'multipart/form-data'"; // String | Content type.
let opts = {
  'possiblySensitive': "possiblySensitive_example", // String | Set to true for content which may not be suitable for every audience.
  'inReplyToStatusId': "inReplyToStatusId_example", // String | The ID of an existing status that the update is in reply to. Note: This parameter will be ignored unless the author of the tweet this parameter references is mentioned within the status text. Therefore, you must include @username, where username is the author of the referenced tweet, within the update.
  'lat': "lat_example", // String | The latitude of the location this tweet refers to. This parameter will be ignored unless it is inside the range -90.0 to +90.0 (North is positive) inclusive. It will also be ignored if there isn't a corresponding long parameter. Example value: 37.7821120598956.
  '_long': "_long_example", // String | The longitude of the location this tweet refers to. The valid ranges for longitude is -180.0 to +180.0 (East is positive) inclusive. This parameter will be ignored if outside that range, not a number, geo_enabled is disabled, or if there not a corresponding lat parameter. Example value: -122.400612831116.
  'placeId': "placeId_example", // String | A place in the world identified by a Twitter place ID. Place IDs can be retrieved from geo/reverse_geocode.
  'displayCoordinates': "displayCoordinates_example" // String | Whether or not to put a pin on the exact coordinates a tweet has been sent from.
};
apiInstance.statusesUpdateWithMedia(status, media, contentType, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **String**| The text of your status update. URL encode as necessary. t.co link wrapping (https://dev.twitter.com/docs/tco-link-wrapper/faq) may affect character counts if the post contains URLs. You must additionally account for the characters_reserved_per_media per uploaded media, additionally accounting for space characters in between finalized URLs. Note: Request the GET help/configuration (https://dev.twitter.com/docs/api/1.1/get/help/configuration) endpoint to get the current characters_reserved_per_media and max_media_per_upload values. | 
 **media** | **String**| Up to max_media_per_upload files may be specified in the request, each named media[]. Supported image formats are PNG, JPG and GIF. Animated GIFs are not supported. Note: Request the GET help/configuration (https://dev.twitter.com/docs/api/1.1/get/help/configuration) endpoint to get the current max_media_per_upload and photo_size_limit values. | 
 **contentType** | **String**| Content type. | [default to &#39;multipart/form-data&#39;]
 **possiblySensitive** | **String**| Set to true for content which may not be suitable for every audience. | [optional] 
 **inReplyToStatusId** | **String**| The ID of an existing status that the update is in reply to. Note: This parameter will be ignored unless the author of the tweet this parameter references is mentioned within the status text. Therefore, you must include @username, where username is the author of the referenced tweet, within the update. | [optional] 
 **lat** | **String**| The latitude of the location this tweet refers to. This parameter will be ignored unless it is inside the range -90.0 to +90.0 (North is positive) inclusive. It will also be ignored if there isn&#39;t a corresponding long parameter. Example value: 37.7821120598956. | [optional] 
 **_long** | **String**| The longitude of the location this tweet refers to. The valid ranges for longitude is -180.0 to +180.0 (East is positive) inclusive. This parameter will be ignored if outside that range, not a number, geo_enabled is disabled, or if there not a corresponding lat parameter. Example value: -122.400612831116. | [optional] 
 **placeId** | **String**| A place in the world identified by a Twitter place ID. Place IDs can be retrieved from geo/reverse_geocode. | [optional] 
 **displayCoordinates** | **String**| Whether or not to put a pin on the exact coordinates a tweet has been sent from. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## statusesUserTimeline

> statusesUserTimeline(opts)



Returns the 20 most recent statuses posted by the authenticating user. It is also possible to request another user&#39;s timeline by using the screen_name or user_id parameter. The other users timeline will only be visible if they are not protected, or if the authenticating user&#39;s follow request was accepted by the protected user. The timeline returned is the equivalent of the one seen when you view a user&#39;s profile on twitter.com. This method can only return up to 3,200 of a user&#39;s most recent statuses. Native retweets of other statuses by the user is included in this total, regardless of whether include_rts is specified when requesting this resource. This method will not include retweets in the XML and JSON responses unless the include_rts parameter is set. The RSS and Atom responses will always include retweets as statuses prefixed with RT, regardless of provided parameters. Always specify either an user_id or screen_name when requesting a user timeline.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'count': 56, // Number | Specifies the number of tweets to try and retrieve, up to a maximum of 200. The value of count is best thought of as a limit to the number of tweets to return because suspended or deleted content is removed after the count has been applied. We include retweets in the count, even if include_rts is not supplied. It is recommended you always send include_rts=1 when using this API method.
  'sinceId': 789, // Number | Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occured since the since_id, the since_id will be forced to the oldest ID available.
  'maxId': 789, // Number | Returns results with an ID less than (that is, older than) or equal to the specified ID.
  'trimUser': "trimUser_example", // String | When set to either true, t or 1, each tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object.
  'excludeReplies': true, // Boolean | This parameter will prevent replies from appearing in the returned timeline. Using exclude_replies with the count parameter will mean you will receive up-to count tweets — this is because the count parameter retrieves that many tweets before filtering out retweets and replies. This parameter is only supported for JSON and XML responses.
  'contributorDetails': true, // Boolean | This parameter enhances the contributors element of the status response to include the screen_name of the contributor. By default only the user_id of the contributor is included.
  'includeRts': true // Boolean | When set to false, the timeline will strip any native retweets (though they will still count toward both the maximal length of the timeline and the slice selected by the count parameter). Note: If you're using the trim_user parameter in conjunction with include_rts, the retweets will still contain a full user object.
};
apiInstance.statusesUserTimeline(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **Number**| Specifies the number of tweets to try and retrieve, up to a maximum of 200. The value of count is best thought of as a limit to the number of tweets to return because suspended or deleted content is removed after the count has been applied. We include retweets in the count, even if include_rts is not supplied. It is recommended you always send include_rts&#x3D;1 when using this API method. | [optional] 
 **sinceId** | **Number**| Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occured since the since_id, the since_id will be forced to the oldest ID available. | [optional] 
 **maxId** | **Number**| Returns results with an ID less than (that is, older than) or equal to the specified ID. | [optional] 
 **trimUser** | **String**| When set to either true, t or 1, each tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object. | [optional] 
 **excludeReplies** | **Boolean**| This parameter will prevent replies from appearing in the returned timeline. Using exclude_replies with the count parameter will mean you will receive up-to count tweets — this is because the count parameter retrieves that many tweets before filtering out retweets and replies. This parameter is only supported for JSON and XML responses. | [optional] 
 **contributorDetails** | **Boolean**| This parameter enhances the contributors element of the status response to include the screen_name of the contributor. By default only the user_id of the contributor is included. | [optional] 
 **includeRts** | **Boolean**| When set to false, the timeline will strip any native retweets (though they will still count toward both the maximal length of the timeline and the slice selected by the count parameter). Note: If you&#39;re using the trim_user parameter in conjunction with include_rts, the retweets will still contain a full user object. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## statusesretweetid

> statusesretweetid(id, opts)



Retweets a tweet. Returns the original tweet with retweet details embedded.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let id = "id_example"; // String | The numerical ID of the desired status.
let opts = {
  'trimUser': "trimUser_example" // String | When set to either true, t or 1, each tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object.
};
apiInstance.statusesretweetid(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The numerical ID of the desired status. | 
 **trimUser** | **String**| When set to either true, t or 1, each tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## trendsAvailable

> trendsAvailable()



Returns the locations that Twitter has trending topic information for.  The response is an array of \&quot;locations\&quot; that encode the location&#39;s WOEID and some other human-readable information such as a canonical name and country the location belongs in.  A WOEID is a Yahoo! Where On Earth ID.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
apiInstance.trendsAvailable((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## trendsClosest

> trendsClosest(opts)



Returns the locations that Twitter has trending topic information for, closest to a specified location.  The response is an array of \&quot;locations\&quot; that encode the location&#39;s WOEID and some other human-readable information such as a canonical name and country the location belongs in.  A WOEID is a Yahoo! Where On Earth ID.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'lat': "lat_example", // String | If provided with a long parameter the available trend locations will be sorted by distance, nearest to furthest, to the co-ordinate pair. The valid ranges for longitude is -180.0 to +180.0 (West is negative, East is positive) inclusive.  Example Values: 37.781157
  '_long': "_long_example" // String | If provided with a lat parameter the available trend locations will be sorted by distance, nearest to furthest, to the co-ordinate pair. The valid ranges for longitude is -180.0 to +180.0 (West is negative, East is positive) inclusive.  Example Values: -122.400612831116
};
apiInstance.trendsClosest(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lat** | **String**| If provided with a long parameter the available trend locations will be sorted by distance, nearest to furthest, to the co-ordinate pair. The valid ranges for longitude is -180.0 to +180.0 (West is negative, East is positive) inclusive.  Example Values: 37.781157 | [optional] 
 **_long** | **String**| If provided with a lat parameter the available trend locations will be sorted by distance, nearest to furthest, to the co-ordinate pair. The valid ranges for longitude is -180.0 to +180.0 (West is negative, East is positive) inclusive.  Example Values: -122.400612831116 | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## trendsPlace

> trendsPlace(id, opts)



Returns the top 10 trending topics for a specific WOEID, if trending information is available for it.  The response is an array of \&quot;trend\&quot; objects that encode the name of the trending topic, the query parameter that can be used to search for the topic on Twitter Search, and the Twitter Search URL.  This information is cached for 5 minutes. Requesting more frequently than that will not return any more data, and will count against your rate limit usage.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let id = "id_example"; // String | The Yahoo! Where On Earth ID of the location to return trending information for. Global information is available by using 1 as the WOEID.
let opts = {
  'exclude': "exclude_example" // String | Setting this equal to hashtags will remove all hashtags from the trends list.
};
apiInstance.trendsPlace(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The Yahoo! Where On Earth ID of the location to return trending information for. Global information is available by using 1 as the WOEID. | 
 **exclude** | **String**| Setting this equal to hashtags will remove all hashtags from the trends list. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## usersContributees

> usersContributees(opts)



Returns a collection of users that the specified user can contribute to.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'includeEntities': "includeEntities_example", // String | The entities node will be disincluded when set to false. Example Values: false
  'skipStatus': "skipStatus_example" // String | When set to either true, t or 1 statuses will not be included in the returned user objects.
};
apiInstance.usersContributees(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **includeEntities** | **String**| The entities node will be disincluded when set to false. Example Values: false | [optional] 
 **skipStatus** | **String**| When set to either true, t or 1 statuses will not be included in the returned user objects. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## usersContributors

> usersContributors(opts)



Returns a collection of users who can contribute to the specified account.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'includeEntities': "includeEntities_example", // String | The entities node will be disincluded when set to false. Example Values: false
  'skipStatus': "skipStatus_example" // String | When set to either true, t or 1 statuses will not be included in the returned user objects.
};
apiInstance.usersContributors(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **includeEntities** | **String**| The entities node will be disincluded when set to false. Example Values: false | [optional] 
 **skipStatus** | **String**| When set to either true, t or 1 statuses will not be included in the returned user objects. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## usersLookup

> usersLookup(opts)



Returns fully-hydrated user objects for up to 100 users per request, as specified by comma-separated values passed to the user_id and/or screen_name parameters.  This method is especially useful when used in conjunction with collections of user IDs returned from GET friends/ids and GET followers/ids.  GET users/show is used to retrieve a single user object.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'screenName': "screenName_example", // String | A comma separated list of screen names, up to 100 are allowed in a single request. You are strongly encouraged to use a POST for larger (up to 100 screen names) requests.  Example Values: twitterapi,twitter
  'userId': "userId_example", // String | A comma separated list of user IDs, up to 100 are allowed in a single request. You are strongly encouraged to use a POST for larger requests.  Example Values: 783214,6253282
  'includeEntities': "includeEntities_example" // String | The entities node that may appear within embedded statuses will be disincluded when set to false.  Example Values: false
};
apiInstance.usersLookup(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **screenName** | **String**| A comma separated list of screen names, up to 100 are allowed in a single request. You are strongly encouraged to use a POST for larger (up to 100 screen names) requests.  Example Values: twitterapi,twitter | [optional] 
 **userId** | **String**| A comma separated list of user IDs, up to 100 are allowed in a single request. You are strongly encouraged to use a POST for larger requests.  Example Values: 783214,6253282 | [optional] 
 **includeEntities** | **String**| The entities node that may appear within embedded statuses will be disincluded when set to false.  Example Values: false | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## usersReportSpam

> usersReportSpam()



The user specified in the id is blocked by the authenticated user and reported as a spammer.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
apiInstance.usersReportSpam((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## usersSearch

> usersSearch(q, opts)



Provides a simple, relevance-based search interface to public user accounts on Twitter. Try querying by topical interest, full name, company name, location, or other criteria. Exact match searches are not supported.  Only the first 1,000 matching results are available.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let q = "q_example"; // String | The search query to run against people search.  Example Values: Twitter%20API
let opts = {
  'page': "page_example", // String | Specifies the page of results to retrieve.  Example Values: 3
  'count': "count_example", // String | The number of potential user results to retrieve per page. This value has a maximum of 20.  Example Values: 5
  'includeEntities': "includeEntities_example" // String | The entities node will be disincluded when set to false.  Example Values: false
};
apiInstance.usersSearch(q, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **String**| The search query to run against people search.  Example Values: Twitter%20API | 
 **page** | **String**| Specifies the page of results to retrieve.  Example Values: 3 | [optional] 
 **count** | **String**| The number of potential user results to retrieve per page. This value has a maximum of 20.  Example Values: 5 | [optional] 
 **includeEntities** | **String**| The entities node will be disincluded when set to false.  Example Values: false | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## usersShow

> usersShow(screenName, userId, opts)



Returns a variety of information about the user specified by the required user_id or screen_name parameter. The author&#39;s most recent Tweet will be returned inline when possible.  GET users/lookup is used to retrieve a bulk collection of user objects.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let screenName = "screenName_example"; // String | The screen name of the user for whom to return results for. Either a id or screen_name is required for this method.  Example Values: noradio
let userId = "userId_example"; // String | The ID of the user for whom to return results for. Either an id or screen_name is required for this method.  Example Values: 12345
let opts = {
  'includeEntities': "includeEntities_example" // String | The entities node will be disincluded when set to false.  Example Values: false
};
apiInstance.usersShow(screenName, userId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **screenName** | **String**| The screen name of the user for whom to return results for. Either a id or screen_name is required for this method.  Example Values: noradio | 
 **userId** | **String**| The ID of the user for whom to return results for. Either an id or screen_name is required for this method.  Example Values: 12345 | 
 **includeEntities** | **String**| The entities node will be disincluded when set to false.  Example Values: false | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## usersSuggestions

> usersSuggestions(opts)



Access to Twitter&#39;s suggested user list. This returns the list of suggested user categories. The category can be used in GET users/suggestions/:slug to get the users in that category.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let opts = {
  'lang': "lang_example" // String | Restricts the suggested categories to the requested language. The language must be specified by the appropriate two letter ISO 639-1 representation. Currently supported languages are provided by the GET help/languages API request. Unsupported language codes will receive English (en) results. If you use lang in this request, ensure you also include it when requesting the GET users/suggestions/:slug list.
};
apiInstance.usersSuggestions(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **String**| Restricts the suggested categories to the requested language. The language must be specified by the appropriate two letter ISO 639-1 representation. Currently supported languages are provided by the GET help/languages API request. Unsupported language codes will receive English (en) results. If you use lang in this request, ensure you also include it when requesting the GET users/suggestions/:slug list. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## usersSuggestionsSlug

> usersSuggestionsSlug(slug, opts)



Access the users in a given category of the Twitter suggested user list. It is recommended that applications cache this data for no more than one hour.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let slug = "slug_example"; // String | The short name of list or a category  Example Values: twitter
let opts = {
  'lang': "lang_example" // String | Restricts the suggested categories to the requested language. The language must be specified by the appropriate two letter ISO 639-1 representation. Currently supported languages are provided by the GET help/languages API request. Unsupported language codes will receive English (en) results. If you use lang in this request, ensure you also include it when requesting the GET users/suggestions/:slug list.
};
apiInstance.usersSuggestionsSlug(slug, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **String**| The short name of list or a category  Example Values: twitter | 
 **lang** | **String**| Restricts the suggested categories to the requested language. The language must be specified by the appropriate two letter ISO 639-1 representation. Currently supported languages are provided by the GET help/languages API request. Unsupported language codes will receive English (en) results. If you use lang in this request, ensure you also include it when requesting the GET users/suggestions/:slug list. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## usersSuggestionsslugmembers

> usersSuggestionsslugmembers(slug)



Access the users in a given category of the Twitter suggested user list and return their most recent status if they are not a protected user.

### Example

```javascript
import TwitterApi from 'twitter_api';

let apiInstance = new TwitterApi.DefaultApi();
let slug = "slug_example"; // String | The short name of list or a category  Example Values: twitter
apiInstance.usersSuggestionsslugmembers(slug, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **String**| The short name of list or a category  Example Values: twitter | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

