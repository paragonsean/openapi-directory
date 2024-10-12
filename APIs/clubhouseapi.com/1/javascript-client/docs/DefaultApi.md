# ClubhouseApi.DefaultApi

All URIs are relative to *https://www.clubhouseapi.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**callPhoneNumberAuthPost**](DefaultApi.md#callPhoneNumberAuthPost) | **POST** /call_phone_number_auth | Call phone number auth.
[**checkForUpdateGet**](DefaultApi.md#checkForUpdateGet) | **GET** /check_for_update | Clubhouse uses this to check for updates when app is not installed from App Store (eg TestFlight)
[**checkWaitlistStatusPost**](DefaultApi.md#checkWaitlistStatusPost) | **POST** /check_waitlist_status | checks waitlist status.
[**completePhoneNumberAuthPost**](DefaultApi.md#completePhoneNumberAuthPost) | **POST** /complete_phone_number_auth | Call phone number auth.
[**createChannelPost**](DefaultApi.md#createChannelPost) | **POST** /create_channel | creates a channel
[**followPost**](DefaultApi.md#followPost) | **POST** /follow | follows a user
[**getActionableNotificationsGet**](DefaultApi.md#getActionableNotificationsGet) | **GET** /get_actionable_notifications | get actionable notifications (the bell again)
[**getAllTopicsGet**](DefaultApi.md#getAllTopicsGet) | **GET** /get_all_topics | gets all topics.
[**getChannelsGet**](DefaultApi.md#getChannelsGet) | **GET** /get_channels | get all channels
[**getClubPost**](DefaultApi.md#getClubPost) | **POST** /get_club | gets club by id
[**getClubsForTopicPost**](DefaultApi.md#getClubsForTopicPost) | **POST** /get_clubs_for_topic | looks up clubs by topic.
[**getCreateChannelTargetsPost**](DefaultApi.md#getCreateChannelTargetsPost) | **POST** /get_create_channel_targets | is fetched when you tap Create Room
[**getEventsGet**](DefaultApi.md#getEventsGet) | **GET** /get_events | the Upcoming for You page
[**getFollowingPost**](DefaultApi.md#getFollowingPost) | **POST** /get_following | get a list of the users and clubs that this user is following. Returned users have bios truncated to ~80 characters.
[**getNotificationsGet**](DefaultApi.md#getNotificationsGet) | **GET** /get_notifications | get notifications (the bell icon)
[**getOnlineFriendsPost**](DefaultApi.md#getOnlineFriendsPost) | **POST** /get_online_friends | gets online friends on the app homepage.
[**getProfilePost**](DefaultApi.md#getProfilePost) | **POST** /get_profile | looks up user profile by ID.
[**getReleaseNotesPost**](DefaultApi.md#getReleaseNotesPost) | **POST** /get_release_notes | gets release notes.
[**getSettingsGet**](DefaultApi.md#getSettingsGet) | **GET** /get_settings | get notification settings
[**getSuggestedClubInvitesPost**](DefaultApi.md#getSuggestedClubInvitesPost) | **POST** /get_suggested_club_invites | find users to invite to clubs based on phone number
[**getSuggestedFollowsAllGet**](DefaultApi.md#getSuggestedFollowsAllGet) | **GET** /get_suggested_follows_all | gets suggested follows during signup
[**getSuggestedFollowsFriendsOnlyPost**](DefaultApi.md#getSuggestedFollowsFriendsOnlyPost) | **POST** /get_suggested_follows_friends_only | find people to follow by uploading contacts during signup
[**getSuggestedFollowsSimilarPost**](DefaultApi.md#getSuggestedFollowsSimilarPost) | **POST** /get_suggested_follows_similar | find similar users. (The Sparkles button on Clubhouse&#39;s profile page)
[**getSuggestedInvitesPost**](DefaultApi.md#getSuggestedInvitesPost) | **POST** /get_suggested_invites | find users to invite based on phone number.
[**getSuggestedSpeakersPost**](DefaultApi.md#getSuggestedSpeakersPost) | **POST** /get_suggested_speakers | gets suggested users when you start a private room
[**getTopicPost**](DefaultApi.md#getTopicPost) | **POST** /get_topic | looks up topic by ID.
[**getUsersForTopicGet**](DefaultApi.md#getUsersForTopicGet) | **GET** /get_users_for_topic | looks up users by topic.
[**getWelcomeChannelGet**](DefaultApi.md#getWelcomeChannelGet) | **GET** /get_welcome_channel | called during signup
[**inviteFromWaitlistPost**](DefaultApi.md#inviteFromWaitlistPost) | **POST** /invite_from_waitlist | wave to another user on the waitlist to give them access
[**inviteToAppPost**](DefaultApi.md#inviteToAppPost) | **POST** /invite_to_app | invite a user to the app, using one of your invites
[**joinChannelPost**](DefaultApi.md#joinChannelPost) | **POST** /join_channel | join a channel.
[**leaveChannelPost**](DefaultApi.md#leaveChannelPost) | **POST** /leave_channel | leave a channel.
[**mePost**](DefaultApi.md#mePost) | **POST** /me | gets user
[**recordActionTrailsPost**](DefaultApi.md#recordActionTrailsPost) | **POST** /record_action_trails | analytics
[**refreshTokenPost**](DefaultApi.md#refreshTokenPost) | **POST** /refresh_token | gets an access_token from a refresh_token.
[**resendPhoneNumberAuthPost**](DefaultApi.md#resendPhoneNumberAuthPost) | **POST** /resend_phone_number_auth | Resend phone number auth.
[**searchClubsPost**](DefaultApi.md#searchClubsPost) | **POST** /search_clubs | search clubs.
[**searchUsersPost**](DefaultApi.md#searchUsersPost) | **POST** /search_users | search for users
[**startPhoneNumberAuthPost**](DefaultApi.md#startPhoneNumberAuthPost) | **POST** /start_phone_number_auth | Starts phone number auth.
[**updateNotificationsPost**](DefaultApi.md#updateNotificationsPost) | **POST** /update_notifications | updates notification during signup.
[**updateUsernamePost**](DefaultApi.md#updateUsernamePost) | **POST** /update_username | edits username.



## callPhoneNumberAuthPost

> callPhoneNumberAuthPost(opts)

Call phone number auth.

### Example

```javascript
import ClubhouseApi from 'clubhouse_api';

let apiInstance = new ClubhouseApi.DefaultApi();
let opts = {
  'body': {} // Object | 
};
apiInstance.callPhoneNumberAuthPost(opts, (error, data, response) => {
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
 **body** | **Object**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## checkForUpdateGet

> checkForUpdateGet(opts)

Clubhouse uses this to check for updates when app is not installed from App Store (eg TestFlight)

### Example

```javascript
import ClubhouseApi from 'clubhouse_api';

let apiInstance = new ClubhouseApi.DefaultApi();
let opts = {
  'isTestflight': 1 // Number | 
};
apiInstance.checkForUpdateGet(opts, (error, data, response) => {
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
 **isTestflight** | **Number**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## checkWaitlistStatusPost

> checkWaitlistStatusPost()

checks waitlist status.

### Example

```javascript
import ClubhouseApi from 'clubhouse_api';

let apiInstance = new ClubhouseApi.DefaultApi();
apiInstance.checkWaitlistStatusPost((error, data, response) => {
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
- **Accept**: application/json


## completePhoneNumberAuthPost

> completePhoneNumberAuthPost(opts)

Call phone number auth.

### Example

```javascript
import ClubhouseApi from 'clubhouse_api';

let apiInstance = new ClubhouseApi.DefaultApi();
let opts = {
  'body': {"phone_number":"+1234567890","verification_code":"1234"} // Object | 
};
apiInstance.completePhoneNumberAuthPost(opts, (error, data, response) => {
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
 **body** | **Object**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createChannelPost

> createChannelPost(opts)

creates a channel

### Example

```javascript
import ClubhouseApi from 'clubhouse_api';

let apiInstance = new ClubhouseApi.DefaultApi();
let opts = {
  'body': {"club_id":null,"event_id":null,"is_private":false,"is_social_mode":false,"topic":null,"user_ids":[]} // Object | 
};
apiInstance.createChannelPost(opts, (error, data, response) => {
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
 **body** | **Object**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## followPost

> followPost(opts)

follows a user

### Example

```javascript
import ClubhouseApi from 'clubhouse_api';

let apiInstance = new ClubhouseApi.DefaultApi();
let opts = {
  'body': {"user_id":1234} // Object | 
};
apiInstance.followPost(opts, (error, data, response) => {
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
 **body** | **Object**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getActionableNotificationsGet

> getActionableNotificationsGet()

get actionable notifications (the bell again)

### Example

```javascript
import ClubhouseApi from 'clubhouse_api';

let apiInstance = new ClubhouseApi.DefaultApi();
apiInstance.getActionableNotificationsGet((error, data, response) => {
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
- **Accept**: application/json


## getAllTopicsGet

> getAllTopicsGet()

gets all topics.

### Example

```javascript
import ClubhouseApi from 'clubhouse_api';

let apiInstance = new ClubhouseApi.DefaultApi();
apiInstance.getAllTopicsGet((error, data, response) => {
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
- **Accept**: application/json


## getChannelsGet

> getChannelsGet()

get all channels

### Example

```javascript
import ClubhouseApi from 'clubhouse_api';

let apiInstance = new ClubhouseApi.DefaultApi();
apiInstance.getChannelsGet((error, data, response) => {
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
- **Accept**: application/json


## getClubPost

> getClubPost(opts)

gets club by id

### Example

```javascript
import ClubhouseApi from 'clubhouse_api';

let apiInstance = new ClubhouseApi.DefaultApi();
let opts = {
  'body': {"club_id":1234} // Object | 
};
apiInstance.getClubPost(opts, (error, data, response) => {
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
 **body** | **Object**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getClubsForTopicPost

> getClubsForTopicPost(opts)

looks up clubs by topic.

### Example

```javascript
import ClubhouseApi from 'clubhouse_api';

let apiInstance = new ClubhouseApi.DefaultApi();
let opts = {
  'body': {"topic_id":140} // Object | 
};
apiInstance.getClubsForTopicPost(opts, (error, data, response) => {
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
 **body** | **Object**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getCreateChannelTargetsPost

> getCreateChannelTargetsPost(opts)

is fetched when you tap Create Room

### Example

```javascript
import ClubhouseApi from 'clubhouse_api';

let apiInstance = new ClubhouseApi.DefaultApi();
let opts = {
  'body': {} // Object | 
};
apiInstance.getCreateChannelTargetsPost(opts, (error, data, response) => {
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
 **body** | **Object**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getEventsGet

> getEventsGet(opts)

the Upcoming for You page

### Example

```javascript
import ClubhouseApi from 'clubhouse_api';

let apiInstance = new ClubhouseApi.DefaultApi();
let opts = {
  'isFiltered': true, // Boolean | 
  'pageSize': 25, // Number | 
  'page': 1 // Number | 
};
apiInstance.getEventsGet(opts, (error, data, response) => {
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
 **isFiltered** | **Boolean**|  | [optional] 
 **pageSize** | **Number**|  | [optional] 
 **page** | **Number**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFollowingPost

> getFollowingPost(opts)

get a list of the users and clubs that this user is following. Returned users have bios truncated to ~80 characters.

### Example

```javascript
import ClubhouseApi from 'clubhouse_api';

let apiInstance = new ClubhouseApi.DefaultApi();
let opts = {
  'body': {"user_id":1234} // Object | 
};
apiInstance.getFollowingPost(opts, (error, data, response) => {
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
 **body** | **Object**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getNotificationsGet

> getNotificationsGet(opts)

get notifications (the bell icon)

### Example

```javascript
import ClubhouseApi from 'clubhouse_api';

let apiInstance = new ClubhouseApi.DefaultApi();
let opts = {
  'pageSize': 20, // Number | 
  'page': 1 // Number | 
};
apiInstance.getNotificationsGet(opts, (error, data, response) => {
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
 **pageSize** | **Number**|  | [optional] 
 **page** | **Number**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOnlineFriendsPost

> getOnlineFriendsPost(opts)

gets online friends on the app homepage.

### Example

```javascript
import ClubhouseApi from 'clubhouse_api';

let apiInstance = new ClubhouseApi.DefaultApi();
let opts = {
  'body': {} // Object | 
};
apiInstance.getOnlineFriendsPost(opts, (error, data, response) => {
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
 **body** | **Object**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getProfilePost

> getProfilePost(opts)

looks up user profile by ID.

### Example

```javascript
import ClubhouseApi from 'clubhouse_api';

let apiInstance = new ClubhouseApi.DefaultApi();
let opts = {
  'body': {"user_id":4075733} // Object | 
};
apiInstance.getProfilePost(opts, (error, data, response) => {
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
 **body** | **Object**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getReleaseNotesPost

> getReleaseNotesPost()

gets release notes.

### Example

```javascript
import ClubhouseApi from 'clubhouse_api';

let apiInstance = new ClubhouseApi.DefaultApi();
apiInstance.getReleaseNotesPost((error, data, response) => {
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
- **Accept**: application/json


## getSettingsGet

> getSettingsGet()

get notification settings

### Example

```javascript
import ClubhouseApi from 'clubhouse_api';

let apiInstance = new ClubhouseApi.DefaultApi();
apiInstance.getSettingsGet((error, data, response) => {
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
- **Accept**: application/json


## getSuggestedClubInvitesPost

> getSuggestedClubInvitesPost(opts)

find users to invite to clubs based on phone number

### Example

```javascript
import ClubhouseApi from 'clubhouse_api';

let apiInstance = new ClubhouseApi.DefaultApi();
let opts = {
  'body': {"contacts":[{"name":"aaa","phone_number":"+11234567890"}],"upload_contacts":true} // Object | 
};
apiInstance.getSuggestedClubInvitesPost(opts, (error, data, response) => {
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
 **body** | **Object**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getSuggestedFollowsAllGet

> getSuggestedFollowsAllGet(opts)

gets suggested follows during signup

### Example

```javascript
import ClubhouseApi from 'clubhouse_api';

let apiInstance = new ClubhouseApi.DefaultApi();
let opts = {
  'inOnboarding': true, // Boolean | 
  'pageSize': 50, // Number | 
  'page': 1 // Number | 
};
apiInstance.getSuggestedFollowsAllGet(opts, (error, data, response) => {
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
 **inOnboarding** | **Boolean**|  | [optional] 
 **pageSize** | **Number**|  | [optional] 
 **page** | **Number**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSuggestedFollowsFriendsOnlyPost

> getSuggestedFollowsFriendsOnlyPost(opts)

find people to follow by uploading contacts during signup

### Example

```javascript
import ClubhouseApi from 'clubhouse_api';

let apiInstance = new ClubhouseApi.DefaultApi();
let opts = {
  'body': {"club_id":null,"contacts":[],"upload_contacts":true} // Object | 
};
apiInstance.getSuggestedFollowsFriendsOnlyPost(opts, (error, data, response) => {
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
 **body** | **Object**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getSuggestedFollowsSimilarPost

> getSuggestedFollowsSimilarPost(opts)

find similar users. (The Sparkles button on Clubhouse&#39;s profile page)

### Example

```javascript
import ClubhouseApi from 'clubhouse_api';

let apiInstance = new ClubhouseApi.DefaultApi();
let opts = {
  'body': {"user_id":4} // Object | 
};
apiInstance.getSuggestedFollowsSimilarPost(opts, (error, data, response) => {
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
 **body** | **Object**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getSuggestedInvitesPost

> getSuggestedInvitesPost(opts)

find users to invite based on phone number.

(also see https://zerforschung.org/posts/clubhouse-telefonnummern-en/ for @zerforschung&#39;s analysis of the privacy implications of this API)

### Example

```javascript
import ClubhouseApi from 'clubhouse_api';

let apiInstance = new ClubhouseApi.DefaultApi();
let opts = {
  'body': {"club_id":null,"contacts":[{"phone_number":"+11234567890"}],"upload_contacts":false} // Object | 
};
apiInstance.getSuggestedInvitesPost(opts, (error, data, response) => {
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
 **body** | **Object**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getSuggestedSpeakersPost

> getSuggestedSpeakersPost(opts)

gets suggested users when you start a private room

### Example

```javascript
import ClubhouseApi from 'clubhouse_api';

let apiInstance = new ClubhouseApi.DefaultApi();
let opts = {
  'body': {"channel":null} // Object | 
};
apiInstance.getSuggestedSpeakersPost(opts, (error, data, response) => {
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
 **body** | **Object**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getTopicPost

> getTopicPost(opts)

looks up topic by ID.

### Example

```javascript
import ClubhouseApi from 'clubhouse_api';

let apiInstance = new ClubhouseApi.DefaultApi();
let opts = {
  'body': {"topic_id":140} // Object | 
};
apiInstance.getTopicPost(opts, (error, data, response) => {
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
 **body** | **Object**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getUsersForTopicGet

> getUsersForTopicGet(opts)

looks up users by topic.

### Example

```javascript
import ClubhouseApi from 'clubhouse_api';

let apiInstance = new ClubhouseApi.DefaultApi();
let opts = {
  'topicId': 140, // Number | 
  'pageSize': 25, // Number | 
  'page': 1 // Number | 
};
apiInstance.getUsersForTopicGet(opts, (error, data, response) => {
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
 **topicId** | **Number**|  | [optional] 
 **pageSize** | **Number**|  | [optional] 
 **page** | **Number**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getWelcomeChannelGet

> getWelcomeChannelGet()

called during signup

### Example

```javascript
import ClubhouseApi from 'clubhouse_api';

let apiInstance = new ClubhouseApi.DefaultApi();
apiInstance.getWelcomeChannelGet((error, data, response) => {
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
- **Accept**: application/json


## inviteFromWaitlistPost

> inviteFromWaitlistPost(opts)

wave to another user on the waitlist to give them access

### Example

```javascript
import ClubhouseApi from 'clubhouse_api';

let apiInstance = new ClubhouseApi.DefaultApi();
let opts = {
  'body': {"user_id":1234} // Object | 
};
apiInstance.inviteFromWaitlistPost(opts, (error, data, response) => {
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
 **body** | **Object**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## inviteToAppPost

> inviteToAppPost(opts)

invite a user to the app, using one of your invites

### Example

```javascript
import ClubhouseApi from 'clubhouse_api';

let apiInstance = new ClubhouseApi.DefaultApi();
let opts = {
  'body': {"message":null,"name":"John Smith","phone_number":"+11234567890"} // Object | 
};
apiInstance.inviteToAppPost(opts, (error, data, response) => {
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
 **body** | **Object**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## joinChannelPost

> joinChannelPost(opts)

join a channel.

### Example

```javascript
import ClubhouseApi from 'clubhouse_api';

let apiInstance = new ClubhouseApi.DefaultApi();
let opts = {
  'body': {"attribution_details":"eyJpc19leHBsb3JlIjpmYWxzZSwicmFuayI6MX0=","attribution_source":"feed","channel":"abcdefgh"} // Object | 
};
apiInstance.joinChannelPost(opts, (error, data, response) => {
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
 **body** | **Object**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## leaveChannelPost

> leaveChannelPost(opts)

leave a channel.

### Example

```javascript
import ClubhouseApi from 'clubhouse_api';

let apiInstance = new ClubhouseApi.DefaultApi();
let opts = {
  'body': {"channel":"abcdefgh"} // Object | 
};
apiInstance.leaveChannelPost(opts, (error, data, response) => {
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
 **body** | **Object**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## mePost

> mePost(opts)

gets user

### Example

```javascript
import ClubhouseApi from 'clubhouse_api';

let apiInstance = new ClubhouseApi.DefaultApi();
let opts = {
  'body': {"return_blocked_ids":true,"return_following_ids":true,"timezone_identifier":"America/Los_Angeles"} // Object | 
};
apiInstance.mePost(opts, (error, data, response) => {
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
 **body** | **Object**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## recordActionTrailsPost

> recordActionTrailsPost(opts)

analytics

### Example

```javascript
import ClubhouseApi from 'clubhouse_api';

let apiInstance = new ClubhouseApi.DefaultApi();
let opts = {
  'body': {"action_trails":[{"blob_data":{},"client_time_created":1612971962,"trail_type":"app_opened"}]} // Object | 
};
apiInstance.recordActionTrailsPost(opts, (error, data, response) => {
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
 **body** | **Object**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## refreshTokenPost

> refreshTokenPost(opts)

gets an access_token from a refresh_token.

### Example

```javascript
import ClubhouseApi from 'clubhouse_api';

let apiInstance = new ClubhouseApi.DefaultApi();
let opts = {
  'body': {"refresh":"<refresh_token>"} // Object | 
};
apiInstance.refreshTokenPost(opts, (error, data, response) => {
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
 **body** | **Object**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## resendPhoneNumberAuthPost

> resendPhoneNumberAuthPost(opts)

Resend phone number auth.

### Example

```javascript
import ClubhouseApi from 'clubhouse_api';

let apiInstance = new ClubhouseApi.DefaultApi();
let opts = {
  'body': {} // Object | 
};
apiInstance.resendPhoneNumberAuthPost(opts, (error, data, response) => {
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
 **body** | **Object**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## searchClubsPost

> searchClubsPost(opts)

search clubs.

### Example

```javascript
import ClubhouseApi from 'clubhouse_api';

let apiInstance = new ClubhouseApi.DefaultApi();
let opts = {
  'body': {"cofollows_only":false,"followers_only":false,"following_only":false,"query":"rohan"} // Object | 
};
apiInstance.searchClubsPost(opts, (error, data, response) => {
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
 **body** | **Object**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## searchUsersPost

> searchUsersPost(opts)

search for users

### Example

```javascript
import ClubhouseApi from 'clubhouse_api';

let apiInstance = new ClubhouseApi.DefaultApi();
let opts = {
  'body': {"cofollows_only":false,"followers_only":false,"following_only":false,"query":"johnsmith"} // Object | 
};
apiInstance.searchUsersPost(opts, (error, data, response) => {
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
 **body** | **Object**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startPhoneNumberAuthPost

> startPhoneNumberAuthPost(opts)

Starts phone number auth.

### Example

```javascript
import ClubhouseApi from 'clubhouse_api';

let apiInstance = new ClubhouseApi.DefaultApi();
let opts = {
  'body': {"phone_number":"+11234567890"} // Object | 
};
apiInstance.startPhoneNumberAuthPost(opts, (error, data, response) => {
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
 **body** | **Object**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNotificationsPost

> updateNotificationsPost(opts)

updates notification during signup.

### Example

```javascript
import ClubhouseApi from 'clubhouse_api';

let apiInstance = new ClubhouseApi.DefaultApi();
let opts = {
  'body': {"apn_token":null,"enable_trending":-1,"frequency":-1,"is_sandbox":false,"pause_till":-1,"system_enabled":2} // Object | 
};
apiInstance.updateNotificationsPost(opts, (error, data, response) => {
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
 **body** | **Object**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateUsernamePost

> updateUsernamePost(opts)

edits username.

### Example

```javascript
import ClubhouseApi from 'clubhouse_api';

let apiInstance = new ClubhouseApi.DefaultApi();
let opts = {
  'body': {"username":"hipsterhouse"} // Object | 
};
apiInstance.updateUsernamePost(opts, (error, data, response) => {
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
 **body** | **Object**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

