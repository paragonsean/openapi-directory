# TwitterApiV2.UsersApi

All URIs are relative to *https://api.twitter.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**findMyUser**](UsersApi.md#findMyUser) | **GET** /2/users/me | User lookup me
[**findUserById**](UsersApi.md#findUserById) | **GET** /2/users/{id} | User lookup by ID
[**findUserByUsername**](UsersApi.md#findUserByUsername) | **GET** /2/users/by/username/{username} | User lookup by username
[**findUsersById**](UsersApi.md#findUsersById) | **GET** /2/users | User lookup by IDs
[**findUsersByUsername**](UsersApi.md#findUsersByUsername) | **GET** /2/users/by | User lookup by usernames
[**listGetFollowers**](UsersApi.md#listGetFollowers) | **GET** /2/lists/{id}/followers | Returns User objects that follow a List by the provided List ID
[**listGetMembers**](UsersApi.md#listGetMembers) | **GET** /2/lists/{id}/members | Returns User objects that are members of a List by the provided List ID.
[**tweetsIdLikingUsers**](UsersApi.md#tweetsIdLikingUsers) | **GET** /2/tweets/{id}/liking_users | Returns User objects that have liked the provided Tweet ID
[**tweetsIdRetweetingUsers**](UsersApi.md#tweetsIdRetweetingUsers) | **GET** /2/tweets/{id}/retweeted_by | Returns User objects that have retweeted the provided Tweet ID
[**usersIdBlock**](UsersApi.md#usersIdBlock) | **POST** /2/users/{id}/blocking | Block User by User ID
[**usersIdBlocking**](UsersApi.md#usersIdBlocking) | **GET** /2/users/{id}/blocking | Returns User objects that are blocked by provided User ID
[**usersIdFollow**](UsersApi.md#usersIdFollow) | **POST** /2/users/{id}/following | Follow User
[**usersIdFollowers**](UsersApi.md#usersIdFollowers) | **GET** /2/users/{id}/followers | Followers by User ID
[**usersIdFollowing**](UsersApi.md#usersIdFollowing) | **GET** /2/users/{id}/following | Following by User ID
[**usersIdMute**](UsersApi.md#usersIdMute) | **POST** /2/users/{id}/muting | Mute User by User ID.
[**usersIdMuting**](UsersApi.md#usersIdMuting) | **GET** /2/users/{id}/muting | Returns User objects that are muted by the provided User ID
[**usersIdUnblock**](UsersApi.md#usersIdUnblock) | **DELETE** /2/users/{source_user_id}/blocking/{target_user_id} | Unblock User by User ID
[**usersIdUnfollow**](UsersApi.md#usersIdUnfollow) | **DELETE** /2/users/{source_user_id}/following/{target_user_id} | Unfollow User
[**usersIdUnmute**](UsersApi.md#usersIdUnmute) | **DELETE** /2/users/{source_user_id}/muting/{target_user_id} | Unmute User by User ID



## findMyUser

> Get2UsersMeResponse findMyUser(opts)

User lookup me

This endpoint returns information about the requesting User.

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TwitterApiV2.UsersApi();
let opts = {
  'userFields': ["null"], // [String] | A comma separated list of User fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'tweetFields': ["null"] // [String] | A comma separated list of Tweet fields to display.
};
apiInstance.findMyUser(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userFields** | [**[String]**](String.md)| A comma separated list of User fields to display. | [optional] 
 **expansions** | [**[String]**](String.md)| A comma separated list of fields to expand. | [optional] 
 **tweetFields** | [**[String]**](String.md)| A comma separated list of Tweet fields to display. | [optional] 

### Return type

[**Get2UsersMeResponse**](Get2UsersMeResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## findUserById

> Get2UsersIdResponse findUserById(id, opts)

User lookup by ID

This endpoint returns information about a User. Specify User by ID.

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TwitterApiV2.UsersApi();
let id = "2244994945"; // String | The ID of the User to lookup.
let opts = {
  'userFields': ["null"], // [String] | A comma separated list of User fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'tweetFields': ["null"] // [String] | A comma separated list of Tweet fields to display.
};
apiInstance.findUserById(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The ID of the User to lookup. | 
 **userFields** | [**[String]**](String.md)| A comma separated list of User fields to display. | [optional] 
 **expansions** | [**[String]**](String.md)| A comma separated list of fields to expand. | [optional] 
 **tweetFields** | [**[String]**](String.md)| A comma separated list of Tweet fields to display. | [optional] 

### Return type

[**Get2UsersIdResponse**](Get2UsersIdResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [BearerToken](../README.md#BearerToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## findUserByUsername

> Get2UsersByUsernameUsernameResponse findUserByUsername(username, opts)

User lookup by username

This endpoint returns information about a User. Specify User by username.

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TwitterApiV2.UsersApi();
let username = "TwitterDev"; // String | A username.
let opts = {
  'userFields': ["null"], // [String] | A comma separated list of User fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'tweetFields': ["null"] // [String] | A comma separated list of Tweet fields to display.
};
apiInstance.findUserByUsername(username, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| A username. | 
 **userFields** | [**[String]**](String.md)| A comma separated list of User fields to display. | [optional] 
 **expansions** | [**[String]**](String.md)| A comma separated list of fields to expand. | [optional] 
 **tweetFields** | [**[String]**](String.md)| A comma separated list of Tweet fields to display. | [optional] 

### Return type

[**Get2UsersByUsernameUsernameResponse**](Get2UsersByUsernameUsernameResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [BearerToken](../README.md#BearerToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## findUsersById

> Get2UsersResponse findUsersById(ids, opts)

User lookup by IDs

This endpoint returns information about Users. Specify Users by their ID.

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TwitterApiV2.UsersApi();
let ids = ["2244994945"]; // [String] | A list of User IDs, comma-separated. You can specify up to 100 IDs.
let opts = {
  'userFields': ["null"], // [String] | A comma separated list of User fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'tweetFields': ["null"] // [String] | A comma separated list of Tweet fields to display.
};
apiInstance.findUsersById(ids, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**[String]**](String.md)| A list of User IDs, comma-separated. You can specify up to 100 IDs. | 
 **userFields** | [**[String]**](String.md)| A comma separated list of User fields to display. | [optional] 
 **expansions** | [**[String]**](String.md)| A comma separated list of fields to expand. | [optional] 
 **tweetFields** | [**[String]**](String.md)| A comma separated list of Tweet fields to display. | [optional] 

### Return type

[**Get2UsersResponse**](Get2UsersResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [BearerToken](../README.md#BearerToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## findUsersByUsername

> Get2UsersByResponse findUsersByUsername(usernames, opts)

User lookup by usernames

This endpoint returns information about Users. Specify Users by their username.

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TwitterApiV2.UsersApi();
let usernames = ["null"]; // [String] | A list of usernames, comma-separated.
let opts = {
  'userFields': ["null"], // [String] | A comma separated list of User fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'tweetFields': ["null"] // [String] | A comma separated list of Tweet fields to display.
};
apiInstance.findUsersByUsername(usernames, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usernames** | [**[String]**](String.md)| A list of usernames, comma-separated. | 
 **userFields** | [**[String]**](String.md)| A comma separated list of User fields to display. | [optional] 
 **expansions** | [**[String]**](String.md)| A comma separated list of fields to expand. | [optional] 
 **tweetFields** | [**[String]**](String.md)| A comma separated list of Tweet fields to display. | [optional] 

### Return type

[**Get2UsersByResponse**](Get2UsersByResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [BearerToken](../README.md#BearerToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## listGetFollowers

> Get2ListsIdFollowersResponse listGetFollowers(id, opts)

Returns User objects that follow a List by the provided List ID

Returns a list of Users that follow a List by the provided List ID

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TwitterApiV2.UsersApi();
let id = "id_example"; // String | The ID of the List.
let opts = {
  'maxResults': 100, // Number | The maximum number of results.
  'paginationToken': "paginationToken_example", // String | This parameter is used to get a specified 'page' of results.
  'userFields': ["null"], // [String] | A comma separated list of User fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'tweetFields': ["null"] // [String] | A comma separated list of Tweet fields to display.
};
apiInstance.listGetFollowers(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The ID of the List. | 
 **maxResults** | **Number**| The maximum number of results. | [optional] [default to 100]
 **paginationToken** | **String**| This parameter is used to get a specified &#39;page&#39; of results. | [optional] 
 **userFields** | [**[String]**](String.md)| A comma separated list of User fields to display. | [optional] 
 **expansions** | [**[String]**](String.md)| A comma separated list of fields to expand. | [optional] 
 **tweetFields** | [**[String]**](String.md)| A comma separated list of Tweet fields to display. | [optional] 

### Return type

[**Get2ListsIdFollowersResponse**](Get2ListsIdFollowersResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [BearerToken](../README.md#BearerToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## listGetMembers

> Get2ListsIdMembersResponse listGetMembers(id, opts)

Returns User objects that are members of a List by the provided List ID.

Returns a list of Users that are members of a List by the provided List ID.

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TwitterApiV2.UsersApi();
let id = "id_example"; // String | The ID of the List.
let opts = {
  'maxResults': 100, // Number | The maximum number of results.
  'paginationToken': "paginationToken_example", // String | This parameter is used to get a specified 'page' of results.
  'userFields': ["null"], // [String] | A comma separated list of User fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'tweetFields': ["null"] // [String] | A comma separated list of Tweet fields to display.
};
apiInstance.listGetMembers(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The ID of the List. | 
 **maxResults** | **Number**| The maximum number of results. | [optional] [default to 100]
 **paginationToken** | **String**| This parameter is used to get a specified &#39;page&#39; of results. | [optional] 
 **userFields** | [**[String]**](String.md)| A comma separated list of User fields to display. | [optional] 
 **expansions** | [**[String]**](String.md)| A comma separated list of fields to expand. | [optional] 
 **tweetFields** | [**[String]**](String.md)| A comma separated list of Tweet fields to display. | [optional] 

### Return type

[**Get2ListsIdMembersResponse**](Get2ListsIdMembersResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [BearerToken](../README.md#BearerToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## tweetsIdLikingUsers

> Get2TweetsIdLikingUsersResponse tweetsIdLikingUsers(id, opts)

Returns User objects that have liked the provided Tweet ID

Returns a list of Users that have liked the provided Tweet ID

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TwitterApiV2.UsersApi();
let id = "id_example"; // String | A single Tweet ID.
let opts = {
  'maxResults': 100, // Number | The maximum number of results.
  'paginationToken': "paginationToken_example", // String | This parameter is used to get the next 'page' of results.
  'userFields': ["null"], // [String] | A comma separated list of User fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'tweetFields': ["null"] // [String] | A comma separated list of Tweet fields to display.
};
apiInstance.tweetsIdLikingUsers(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| A single Tweet ID. | 
 **maxResults** | **Number**| The maximum number of results. | [optional] [default to 100]
 **paginationToken** | **String**| This parameter is used to get the next &#39;page&#39; of results. | [optional] 
 **userFields** | [**[String]**](String.md)| A comma separated list of User fields to display. | [optional] 
 **expansions** | [**[String]**](String.md)| A comma separated list of fields to expand. | [optional] 
 **tweetFields** | [**[String]**](String.md)| A comma separated list of Tweet fields to display. | [optional] 

### Return type

[**Get2TweetsIdLikingUsersResponse**](Get2TweetsIdLikingUsersResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [BearerToken](../README.md#BearerToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## tweetsIdRetweetingUsers

> Get2TweetsIdRetweetedByResponse tweetsIdRetweetingUsers(id, opts)

Returns User objects that have retweeted the provided Tweet ID

Returns a list of Users that have retweeted the provided Tweet ID

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TwitterApiV2.UsersApi();
let id = "id_example"; // String | A single Tweet ID.
let opts = {
  'maxResults': 100, // Number | The maximum number of results.
  'paginationToken': "paginationToken_example", // String | This parameter is used to get the next 'page' of results.
  'userFields': ["null"], // [String] | A comma separated list of User fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'tweetFields': ["null"] // [String] | A comma separated list of Tweet fields to display.
};
apiInstance.tweetsIdRetweetingUsers(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| A single Tweet ID. | 
 **maxResults** | **Number**| The maximum number of results. | [optional] [default to 100]
 **paginationToken** | **String**| This parameter is used to get the next &#39;page&#39; of results. | [optional] 
 **userFields** | [**[String]**](String.md)| A comma separated list of User fields to display. | [optional] 
 **expansions** | [**[String]**](String.md)| A comma separated list of fields to expand. | [optional] 
 **tweetFields** | [**[String]**](String.md)| A comma separated list of Tweet fields to display. | [optional] 

### Return type

[**Get2TweetsIdRetweetedByResponse**](Get2TweetsIdRetweetedByResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [BearerToken](../README.md#BearerToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## usersIdBlock

> BlockUserMutationResponse usersIdBlock(id, blockUserRequest)

Block User by User ID

Causes the User (in the path) to block the target User. The User (in the path) must match the User context authorizing the request

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TwitterApiV2.UsersApi();
let id = "id_example"; // String | The ID of the authenticated source User that is requesting to block the target User.
let blockUserRequest = new TwitterApiV2.BlockUserRequest(); // BlockUserRequest | 
apiInstance.usersIdBlock(id, blockUserRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The ID of the authenticated source User that is requesting to block the target User. | 
 **blockUserRequest** | [**BlockUserRequest**](BlockUserRequest.md)|  | 

### Return type

[**BlockUserMutationResponse**](BlockUserMutationResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/problem+json


## usersIdBlocking

> Get2UsersIdBlockingResponse usersIdBlocking(id, opts)

Returns User objects that are blocked by provided User ID

Returns a list of Users that are blocked by the provided User ID

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TwitterApiV2.UsersApi();
let id = "id_example"; // String | The ID of the authenticated source User for whom to return results.
let opts = {
  'maxResults': 56, // Number | The maximum number of results.
  'paginationToken': "paginationToken_example", // String | This parameter is used to get a specified 'page' of results.
  'userFields': ["null"], // [String] | A comma separated list of User fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'tweetFields': ["null"] // [String] | A comma separated list of Tweet fields to display.
};
apiInstance.usersIdBlocking(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The ID of the authenticated source User for whom to return results. | 
 **maxResults** | **Number**| The maximum number of results. | [optional] 
 **paginationToken** | **String**| This parameter is used to get a specified &#39;page&#39; of results. | [optional] 
 **userFields** | [**[String]**](String.md)| A comma separated list of User fields to display. | [optional] 
 **expansions** | [**[String]**](String.md)| A comma separated list of fields to expand. | [optional] 
 **tweetFields** | [**[String]**](String.md)| A comma separated list of Tweet fields to display. | [optional] 

### Return type

[**Get2UsersIdBlockingResponse**](Get2UsersIdBlockingResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## usersIdFollow

> UsersFollowingCreateResponse usersIdFollow(id, opts)

Follow User

Causes the User(in the path) to follow, or “request to follow” for protected Users, the target User. The User(in the path) must match the User context authorizing the request

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TwitterApiV2.UsersApi();
let id = "id_example"; // String | The ID of the authenticated source User that is requesting to follow the target User.
let opts = {
  'usersFollowingCreateRequest': new TwitterApiV2.UsersFollowingCreateRequest() // UsersFollowingCreateRequest | 
};
apiInstance.usersIdFollow(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The ID of the authenticated source User that is requesting to follow the target User. | 
 **usersFollowingCreateRequest** | [**UsersFollowingCreateRequest**](UsersFollowingCreateRequest.md)|  | [optional] 

### Return type

[**UsersFollowingCreateResponse**](UsersFollowingCreateResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/problem+json


## usersIdFollowers

> Get2UsersIdFollowersResponse usersIdFollowers(id, opts)

Followers by User ID

Returns a list of Users who are followers of the specified User ID.

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TwitterApiV2.UsersApi();
let id = "2244994945"; // String | The ID of the User to lookup.
let opts = {
  'maxResults': 56, // Number | The maximum number of results.
  'paginationToken': "paginationToken_example", // String | This parameter is used to get a specified 'page' of results.
  'userFields': ["null"], // [String] | A comma separated list of User fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'tweetFields': ["null"] // [String] | A comma separated list of Tweet fields to display.
};
apiInstance.usersIdFollowers(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The ID of the User to lookup. | 
 **maxResults** | **Number**| The maximum number of results. | [optional] 
 **paginationToken** | **String**| This parameter is used to get a specified &#39;page&#39; of results. | [optional] 
 **userFields** | [**[String]**](String.md)| A comma separated list of User fields to display. | [optional] 
 **expansions** | [**[String]**](String.md)| A comma separated list of fields to expand. | [optional] 
 **tweetFields** | [**[String]**](String.md)| A comma separated list of Tweet fields to display. | [optional] 

### Return type

[**Get2UsersIdFollowersResponse**](Get2UsersIdFollowersResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [BearerToken](../README.md#BearerToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## usersIdFollowing

> Get2UsersIdFollowingResponse usersIdFollowing(id, opts)

Following by User ID

Returns a list of Users that are being followed by the provided User ID

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TwitterApiV2.UsersApi();
let id = "2244994945"; // String | The ID of the User to lookup.
let opts = {
  'maxResults': 56, // Number | The maximum number of results.
  'paginationToken': "paginationToken_example", // String | This parameter is used to get a specified 'page' of results.
  'userFields': ["null"], // [String] | A comma separated list of User fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'tweetFields': ["null"] // [String] | A comma separated list of Tweet fields to display.
};
apiInstance.usersIdFollowing(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The ID of the User to lookup. | 
 **maxResults** | **Number**| The maximum number of results. | [optional] 
 **paginationToken** | **String**| This parameter is used to get a specified &#39;page&#39; of results. | [optional] 
 **userFields** | [**[String]**](String.md)| A comma separated list of User fields to display. | [optional] 
 **expansions** | [**[String]**](String.md)| A comma separated list of fields to expand. | [optional] 
 **tweetFields** | [**[String]**](String.md)| A comma separated list of Tweet fields to display. | [optional] 

### Return type

[**Get2UsersIdFollowingResponse**](Get2UsersIdFollowingResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [BearerToken](../README.md#BearerToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## usersIdMute

> MuteUserMutationResponse usersIdMute(id, opts)

Mute User by User ID.

Causes the User (in the path) to mute the target User. The User (in the path) must match the User context authorizing the request.

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TwitterApiV2.UsersApi();
let id = "id_example"; // String | The ID of the authenticated source User that is requesting to mute the target User.
let opts = {
  'muteUserRequest': new TwitterApiV2.MuteUserRequest() // MuteUserRequest | 
};
apiInstance.usersIdMute(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The ID of the authenticated source User that is requesting to mute the target User. | 
 **muteUserRequest** | [**MuteUserRequest**](MuteUserRequest.md)|  | [optional] 

### Return type

[**MuteUserMutationResponse**](MuteUserMutationResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/problem+json


## usersIdMuting

> Get2UsersIdMutingResponse usersIdMuting(id, opts)

Returns User objects that are muted by the provided User ID

Returns a list of Users that are muted by the provided User ID

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TwitterApiV2.UsersApi();
let id = "id_example"; // String | The ID of the authenticated source User for whom to return results.
let opts = {
  'maxResults': 100, // Number | The maximum number of results.
  'paginationToken': "paginationToken_example", // String | This parameter is used to get the next 'page' of results.
  'userFields': ["null"], // [String] | A comma separated list of User fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'tweetFields': ["null"] // [String] | A comma separated list of Tweet fields to display.
};
apiInstance.usersIdMuting(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The ID of the authenticated source User for whom to return results. | 
 **maxResults** | **Number**| The maximum number of results. | [optional] [default to 100]
 **paginationToken** | **String**| This parameter is used to get the next &#39;page&#39; of results. | [optional] 
 **userFields** | [**[String]**](String.md)| A comma separated list of User fields to display. | [optional] 
 **expansions** | [**[String]**](String.md)| A comma separated list of fields to expand. | [optional] 
 **tweetFields** | [**[String]**](String.md)| A comma separated list of Tweet fields to display. | [optional] 

### Return type

[**Get2UsersIdMutingResponse**](Get2UsersIdMutingResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## usersIdUnblock

> BlockUserMutationResponse usersIdUnblock(sourceUserId, targetUserId)

Unblock User by User ID

Causes the source User to unblock the target User. The source User must match the User context authorizing the request

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TwitterApiV2.UsersApi();
let sourceUserId = "sourceUserId_example"; // String | The ID of the authenticated source User that is requesting to unblock the target User.
let targetUserId = "targetUserId_example"; // String | The ID of the User that the source User is requesting to unblock.
apiInstance.usersIdUnblock(sourceUserId, targetUserId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sourceUserId** | **String**| The ID of the authenticated source User that is requesting to unblock the target User. | 
 **targetUserId** | **String**| The ID of the User that the source User is requesting to unblock. | 

### Return type

[**BlockUserMutationResponse**](BlockUserMutationResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## usersIdUnfollow

> UsersFollowingDeleteResponse usersIdUnfollow(sourceUserId, targetUserId)

Unfollow User

Causes the source User to unfollow the target User. The source User must match the User context authorizing the request

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TwitterApiV2.UsersApi();
let sourceUserId = "sourceUserId_example"; // String | The ID of the authenticated source User that is requesting to unfollow the target User.
let targetUserId = "targetUserId_example"; // String | The ID of the User that the source User is requesting to unfollow.
apiInstance.usersIdUnfollow(sourceUserId, targetUserId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sourceUserId** | **String**| The ID of the authenticated source User that is requesting to unfollow the target User. | 
 **targetUserId** | **String**| The ID of the User that the source User is requesting to unfollow. | 

### Return type

[**UsersFollowingDeleteResponse**](UsersFollowingDeleteResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## usersIdUnmute

> MuteUserMutationResponse usersIdUnmute(sourceUserId, targetUserId)

Unmute User by User ID

Causes the source User to unmute the target User. The source User must match the User context authorizing the request

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TwitterApiV2.UsersApi();
let sourceUserId = "sourceUserId_example"; // String | The ID of the authenticated source User that is requesting to unmute the target User.
let targetUserId = "targetUserId_example"; // String | The ID of the User that the source User is requesting to unmute.
apiInstance.usersIdUnmute(sourceUserId, targetUserId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sourceUserId** | **String**| The ID of the authenticated source User that is requesting to unmute the target User. | 
 **targetUserId** | **String**| The ID of the User that the source User is requesting to unmute. | 

### Return type

[**MuteUserMutationResponse**](MuteUserMutationResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json

