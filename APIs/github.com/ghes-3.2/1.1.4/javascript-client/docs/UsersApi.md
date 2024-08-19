# GitHubV3RestApi.UsersApi

All URIs are relative to *https://github.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usersAddEmailForAuthenticatedUser**](UsersApi.md#usersAddEmailForAuthenticatedUser) | **POST** /user/emails | Add an email address for the authenticated user
[**usersCheckFollowingForUser**](UsersApi.md#usersCheckFollowingForUser) | **GET** /users/{username}/following/{target_user} | Check if a user follows another user
[**usersCheckPersonIsFollowedByAuthenticated**](UsersApi.md#usersCheckPersonIsFollowedByAuthenticated) | **GET** /user/following/{username} | Check if a person is followed by the authenticated user
[**usersCreateGpgKeyForAuthenticatedUser**](UsersApi.md#usersCreateGpgKeyForAuthenticatedUser) | **POST** /user/gpg_keys | Create a GPG key for the authenticated user
[**usersCreatePublicSshKeyForAuthenticatedUser**](UsersApi.md#usersCreatePublicSshKeyForAuthenticatedUser) | **POST** /user/keys | Create a public SSH key for the authenticated user
[**usersDeleteEmailForAuthenticatedUser**](UsersApi.md#usersDeleteEmailForAuthenticatedUser) | **DELETE** /user/emails | Delete an email address for the authenticated user
[**usersDeleteGpgKeyForAuthenticatedUser**](UsersApi.md#usersDeleteGpgKeyForAuthenticatedUser) | **DELETE** /user/gpg_keys/{gpg_key_id} | Delete a GPG key for the authenticated user
[**usersDeletePublicSshKeyForAuthenticatedUser**](UsersApi.md#usersDeletePublicSshKeyForAuthenticatedUser) | **DELETE** /user/keys/{key_id} | Delete a public SSH key for the authenticated user
[**usersFollow**](UsersApi.md#usersFollow) | **PUT** /user/following/{username} | Follow a user
[**usersGetAuthenticated**](UsersApi.md#usersGetAuthenticated) | **GET** /user | Get the authenticated user
[**usersGetByUsername**](UsersApi.md#usersGetByUsername) | **GET** /users/{username} | Get a user
[**usersGetContextForUser**](UsersApi.md#usersGetContextForUser) | **GET** /users/{username}/hovercard | Get contextual information for a user
[**usersGetGpgKeyForAuthenticatedUser**](UsersApi.md#usersGetGpgKeyForAuthenticatedUser) | **GET** /user/gpg_keys/{gpg_key_id} | Get a GPG key for the authenticated user
[**usersGetPublicSshKeyForAuthenticatedUser**](UsersApi.md#usersGetPublicSshKeyForAuthenticatedUser) | **GET** /user/keys/{key_id} | Get a public SSH key for the authenticated user
[**usersList**](UsersApi.md#usersList) | **GET** /users | List users
[**usersListEmailsForAuthenticatedUser**](UsersApi.md#usersListEmailsForAuthenticatedUser) | **GET** /user/emails | List email addresses for the authenticated user
[**usersListFollowedByAuthenticatedUser**](UsersApi.md#usersListFollowedByAuthenticatedUser) | **GET** /user/following | List the people the authenticated user follows
[**usersListFollowersForAuthenticatedUser**](UsersApi.md#usersListFollowersForAuthenticatedUser) | **GET** /user/followers | List followers of the authenticated user
[**usersListFollowersForUser**](UsersApi.md#usersListFollowersForUser) | **GET** /users/{username}/followers | List followers of a user
[**usersListFollowingForUser**](UsersApi.md#usersListFollowingForUser) | **GET** /users/{username}/following | List the people a user follows
[**usersListGpgKeysForAuthenticatedUser**](UsersApi.md#usersListGpgKeysForAuthenticatedUser) | **GET** /user/gpg_keys | List GPG keys for the authenticated user
[**usersListGpgKeysForUser**](UsersApi.md#usersListGpgKeysForUser) | **GET** /users/{username}/gpg_keys | List GPG keys for a user
[**usersListPublicEmailsForAuthenticatedUser**](UsersApi.md#usersListPublicEmailsForAuthenticatedUser) | **GET** /user/public_emails | List public email addresses for the authenticated user
[**usersListPublicKeysForUser**](UsersApi.md#usersListPublicKeysForUser) | **GET** /users/{username}/keys | List public keys for a user
[**usersListPublicSshKeysForAuthenticatedUser**](UsersApi.md#usersListPublicSshKeysForAuthenticatedUser) | **GET** /user/keys | List public SSH keys for the authenticated user
[**usersUnfollow**](UsersApi.md#usersUnfollow) | **DELETE** /user/following/{username} | Unfollow a user
[**usersUpdateAuthenticated**](UsersApi.md#usersUpdateAuthenticated) | **PATCH** /user | Update the authenticated user



## usersAddEmailForAuthenticatedUser

> [Email] usersAddEmailForAuthenticatedUser(opts)

Add an email address for the authenticated user

This endpoint is accessible with the &#x60;user&#x60; scope.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.UsersApi();
let opts = {
  'usersAddEmailForAuthenticatedUserRequest': {"emails":["octocat@github.com","mona@github.com","octocat@octocat.org"]} // UsersAddEmailForAuthenticatedUserRequest | 
};
apiInstance.usersAddEmailForAuthenticatedUser(opts, (error, data, response) => {
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
 **usersAddEmailForAuthenticatedUserRequest** | [**UsersAddEmailForAuthenticatedUserRequest**](UsersAddEmailForAuthenticatedUserRequest.md)|  | [optional] 

### Return type

[**[Email]**](Email.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersCheckFollowingForUser

> usersCheckFollowingForUser(username, targetUser)

Check if a user follows another user



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.UsersApi();
let username = "username_example"; // String | The handle for the GitHub user account.
let targetUser = "targetUser_example"; // String | 
apiInstance.usersCheckFollowingForUser(username, targetUser, (error, data, response) => {
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
 **username** | **String**| The handle for the GitHub user account. | 
 **targetUser** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## usersCheckPersonIsFollowedByAuthenticated

> usersCheckPersonIsFollowedByAuthenticated(username)

Check if a person is followed by the authenticated user



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.UsersApi();
let username = "username_example"; // String | The handle for the GitHub user account.
apiInstance.usersCheckPersonIsFollowedByAuthenticated(username, (error, data, response) => {
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
 **username** | **String**| The handle for the GitHub user account. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersCreateGpgKeyForAuthenticatedUser

> GpgKey usersCreateGpgKeyForAuthenticatedUser(usersCreateGpgKeyForAuthenticatedUserRequest)

Create a GPG key for the authenticated user

Adds a GPG key to the authenticated user&#39;s GitHub account. Requires that you are authenticated via Basic Auth, or OAuth with at least &#x60;write:gpg_key&#x60; [scope](https://docs.github.com/enterprise-server@3.2/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.UsersApi();
let usersCreateGpgKeyForAuthenticatedUserRequest = new GitHubV3RestApi.UsersCreateGpgKeyForAuthenticatedUserRequest(); // UsersCreateGpgKeyForAuthenticatedUserRequest | 
apiInstance.usersCreateGpgKeyForAuthenticatedUser(usersCreateGpgKeyForAuthenticatedUserRequest, (error, data, response) => {
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
 **usersCreateGpgKeyForAuthenticatedUserRequest** | [**UsersCreateGpgKeyForAuthenticatedUserRequest**](UsersCreateGpgKeyForAuthenticatedUserRequest.md)|  | 

### Return type

[**GpgKey**](GpgKey.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersCreatePublicSshKeyForAuthenticatedUser

> Key usersCreatePublicSshKeyForAuthenticatedUser(usersCreatePublicSshKeyForAuthenticatedUserRequest)

Create a public SSH key for the authenticated user

Adds a public SSH key to the authenticated user&#39;s GitHub account. Requires that you are authenticated via Basic Auth, or OAuth with at least &#x60;write:public_key&#x60; [scope](https://docs.github.com/enterprise-server@3.2/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.UsersApi();
let usersCreatePublicSshKeyForAuthenticatedUserRequest = new GitHubV3RestApi.UsersCreatePublicSshKeyForAuthenticatedUserRequest(); // UsersCreatePublicSshKeyForAuthenticatedUserRequest | 
apiInstance.usersCreatePublicSshKeyForAuthenticatedUser(usersCreatePublicSshKeyForAuthenticatedUserRequest, (error, data, response) => {
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
 **usersCreatePublicSshKeyForAuthenticatedUserRequest** | [**UsersCreatePublicSshKeyForAuthenticatedUserRequest**](UsersCreatePublicSshKeyForAuthenticatedUserRequest.md)|  | 

### Return type

[**Key**](Key.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersDeleteEmailForAuthenticatedUser

> usersDeleteEmailForAuthenticatedUser(opts)

Delete an email address for the authenticated user

This endpoint is accessible with the &#x60;user&#x60; scope.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.UsersApi();
let opts = {
  'usersDeleteEmailForAuthenticatedUserRequest': {"emails":["octocat@github.com","mona@github.com"]} // UsersDeleteEmailForAuthenticatedUserRequest | 
};
apiInstance.usersDeleteEmailForAuthenticatedUser(opts, (error, data, response) => {
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
 **usersDeleteEmailForAuthenticatedUserRequest** | [**UsersDeleteEmailForAuthenticatedUserRequest**](UsersDeleteEmailForAuthenticatedUserRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersDeleteGpgKeyForAuthenticatedUser

> usersDeleteGpgKeyForAuthenticatedUser(gpgKeyId)

Delete a GPG key for the authenticated user

Removes a GPG key from the authenticated user&#39;s GitHub account. Requires that you are authenticated via Basic Auth or via OAuth with at least &#x60;admin:gpg_key&#x60; [scope](https://docs.github.com/enterprise-server@3.2/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.UsersApi();
let gpgKeyId = 56; // Number | The unique identifier of the GPG key.
apiInstance.usersDeleteGpgKeyForAuthenticatedUser(gpgKeyId, (error, data, response) => {
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
 **gpgKeyId** | **Number**| The unique identifier of the GPG key. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersDeletePublicSshKeyForAuthenticatedUser

> usersDeletePublicSshKeyForAuthenticatedUser(keyId)

Delete a public SSH key for the authenticated user

Removes a public SSH key from the authenticated user&#39;s GitHub account. Requires that you are authenticated via Basic Auth or via OAuth with at least &#x60;admin:public_key&#x60; [scope](https://docs.github.com/enterprise-server@3.2/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.UsersApi();
let keyId = 56; // Number | The unique identifier of the key.
apiInstance.usersDeletePublicSshKeyForAuthenticatedUser(keyId, (error, data, response) => {
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
 **keyId** | **Number**| The unique identifier of the key. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersFollow

> usersFollow(username)

Follow a user

Note that you&#39;ll need to set &#x60;Content-Length&#x60; to zero when calling out to this endpoint. For more information, see \&quot;[HTTP verbs](https://docs.github.com/enterprise-server@3.2/rest/overview/resources-in-the-rest-api#http-verbs).\&quot;  Following a user requires the user to be logged in and authenticated with basic auth or OAuth with the &#x60;user:follow&#x60; scope.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.UsersApi();
let username = "username_example"; // String | The handle for the GitHub user account.
apiInstance.usersFollow(username, (error, data, response) => {
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
 **username** | **String**| The handle for the GitHub user account. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersGetAuthenticated

> UsersGetAuthenticated200Response usersGetAuthenticated()

Get the authenticated user

If the authenticated user is authenticated through basic authentication or OAuth with the &#x60;user&#x60; scope, then the response lists public and private profile information.  If the authenticated user is authenticated through OAuth without the &#x60;user&#x60; scope, then the response lists only public profile information.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.UsersApi();
apiInstance.usersGetAuthenticated((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**UsersGetAuthenticated200Response**](UsersGetAuthenticated200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersGetByUsername

> UsersGetAuthenticated200Response usersGetByUsername(username)

Get a user

Provides publicly available information about someone with a GitHub account.  GitHub Apps with the &#x60;Plan&#x60; user permission can use this endpoint to retrieve information about a user&#39;s GitHub Enterprise Server plan. The GitHub App must be authenticated as a user. See \&quot;[Identifying and authorizing users for GitHub Apps](https://docs.github.com/enterprise-server@3.2/apps/building-github-apps/identifying-and-authorizing-users-for-github-apps/)\&quot; for details about authentication. For an example response, see &#39;Response with GitHub Enterprise Server plan information&#39; below\&quot;  The &#x60;email&#x60; key in the following response is the publicly visible email address from your GitHub Enterprise Server [profile page](https://github.com/settings/profile). When setting up your profile, you can select a primary email address to be “public” which provides an email entry for this endpoint. If you do not set a public email address for &#x60;email&#x60;, then it will have a value of &#x60;null&#x60;. You only see publicly visible email addresses when authenticated with GitHub Enterprise Server. For more information, see [Authentication](https://docs.github.com/enterprise-server@3.2/rest/overview/resources-in-the-rest-api#authentication).  The Emails API enables you to list all of your email addresses, and toggle a primary email to be visible publicly. For more information, see \&quot;[Emails API](https://docs.github.com/enterprise-server@3.2/rest/reference/users#emails)\&quot;.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.UsersApi();
let username = "username_example"; // String | The handle for the GitHub user account.
apiInstance.usersGetByUsername(username, (error, data, response) => {
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
 **username** | **String**| The handle for the GitHub user account. | 

### Return type

[**UsersGetAuthenticated200Response**](UsersGetAuthenticated200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersGetContextForUser

> Hovercard usersGetContextForUser(username, opts)

Get contextual information for a user

Provides hovercard information when authenticated through basic auth or OAuth with the &#x60;repo&#x60; scope. You can find out more about someone in relation to their pull requests, issues, repositories, and organizations.  The &#x60;subject_type&#x60; and &#x60;subject_id&#x60; parameters provide context for the person&#39;s hovercard, which returns more information than without the parameters. For example, if you wanted to find out more about &#x60;octocat&#x60; who owns the &#x60;Spoon-Knife&#x60; repository via cURL, it would look like this:  &#x60;&#x60;&#x60;shell  curl -u username:token   https://api.github.com/users/octocat/hovercard?subject_type&#x3D;repository&amp;subject_id&#x3D;1300192 &#x60;&#x60;&#x60;

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.UsersApi();
let username = "username_example"; // String | The handle for the GitHub user account.
let opts = {
  'subjectType': "subjectType_example", // String | Identifies which additional information you'd like to receive about the person's hovercard. Can be `organization`, `repository`, `issue`, `pull_request`. **Required** when using `subject_id`.
  'subjectId': "subjectId_example" // String | Uses the ID for the `subject_type` you specified. **Required** when using `subject_type`.
};
apiInstance.usersGetContextForUser(username, opts, (error, data, response) => {
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
 **username** | **String**| The handle for the GitHub user account. | 
 **subjectType** | **String**| Identifies which additional information you&#39;d like to receive about the person&#39;s hovercard. Can be &#x60;organization&#x60;, &#x60;repository&#x60;, &#x60;issue&#x60;, &#x60;pull_request&#x60;. **Required** when using &#x60;subject_id&#x60;. | [optional] 
 **subjectId** | **String**| Uses the ID for the &#x60;subject_type&#x60; you specified. **Required** when using &#x60;subject_type&#x60;. | [optional] 

### Return type

[**Hovercard**](Hovercard.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersGetGpgKeyForAuthenticatedUser

> GpgKey usersGetGpgKeyForAuthenticatedUser(gpgKeyId)

Get a GPG key for the authenticated user

View extended details for a single GPG key. Requires that you are authenticated via Basic Auth or via OAuth with at least &#x60;read:gpg_key&#x60; [scope](https://docs.github.com/enterprise-server@3.2/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.UsersApi();
let gpgKeyId = 56; // Number | The unique identifier of the GPG key.
apiInstance.usersGetGpgKeyForAuthenticatedUser(gpgKeyId, (error, data, response) => {
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
 **gpgKeyId** | **Number**| The unique identifier of the GPG key. | 

### Return type

[**GpgKey**](GpgKey.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersGetPublicSshKeyForAuthenticatedUser

> Key usersGetPublicSshKeyForAuthenticatedUser(keyId)

Get a public SSH key for the authenticated user

View extended details for a single public SSH key. Requires that you are authenticated via Basic Auth or via OAuth with at least &#x60;read:public_key&#x60; [scope](https://docs.github.com/enterprise-server@3.2/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.UsersApi();
let keyId = 56; // Number | The unique identifier of the key.
apiInstance.usersGetPublicSshKeyForAuthenticatedUser(keyId, (error, data, response) => {
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
 **keyId** | **Number**| The unique identifier of the key. | 

### Return type

[**Key**](Key.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersList

> [SimpleUser] usersList(opts)

List users

Lists all users, in the order that they signed up on GitHub Enterprise Server. This list includes personal user accounts and organization accounts.  Note: Pagination is powered exclusively by the &#x60;since&#x60; parameter. Use the [Link header](https://docs.github.com/enterprise-server@3.2/rest/overview/resources-in-the-rest-api#link-header) to get the URL for the next page of users.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.UsersApi();
let opts = {
  'since': 56, // Number | A user ID. Only return users with an ID greater than this ID.
  'perPage': 30 // Number | The number of results per page (max 100).
};
apiInstance.usersList(opts, (error, data, response) => {
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
 **since** | **Number**| A user ID. Only return users with an ID greater than this ID. | [optional] 
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]

### Return type

[**[SimpleUser]**](SimpleUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersListEmailsForAuthenticatedUser

> [Email] usersListEmailsForAuthenticatedUser(opts)

List email addresses for the authenticated user

Lists all of your email addresses, and specifies which one is visible to the public. This endpoint is accessible with the &#x60;user:email&#x60; scope.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.UsersApi();
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.usersListEmailsForAuthenticatedUser(opts, (error, data, response) => {
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
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[Email]**](Email.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersListFollowedByAuthenticatedUser

> [SimpleUser] usersListFollowedByAuthenticatedUser(opts)

List the people the authenticated user follows

Lists the people who the authenticated user follows.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.UsersApi();
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.usersListFollowedByAuthenticatedUser(opts, (error, data, response) => {
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
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[SimpleUser]**](SimpleUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersListFollowersForAuthenticatedUser

> [SimpleUser] usersListFollowersForAuthenticatedUser(opts)

List followers of the authenticated user

Lists the people following the authenticated user.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.UsersApi();
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.usersListFollowersForAuthenticatedUser(opts, (error, data, response) => {
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
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[SimpleUser]**](SimpleUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersListFollowersForUser

> [SimpleUser] usersListFollowersForUser(username, opts)

List followers of a user

Lists the people following the specified user.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.UsersApi();
let username = "username_example"; // String | The handle for the GitHub user account.
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.usersListFollowersForUser(username, opts, (error, data, response) => {
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
 **username** | **String**| The handle for the GitHub user account. | 
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[SimpleUser]**](SimpleUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersListFollowingForUser

> [SimpleUser] usersListFollowingForUser(username, opts)

List the people a user follows

Lists the people who the specified user follows.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.UsersApi();
let username = "username_example"; // String | The handle for the GitHub user account.
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.usersListFollowingForUser(username, opts, (error, data, response) => {
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
 **username** | **String**| The handle for the GitHub user account. | 
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[SimpleUser]**](SimpleUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersListGpgKeysForAuthenticatedUser

> [GpgKey] usersListGpgKeysForAuthenticatedUser(opts)

List GPG keys for the authenticated user

Lists the current user&#39;s GPG keys. Requires that you are authenticated via Basic Auth or via OAuth with at least &#x60;read:gpg_key&#x60; [scope](https://docs.github.com/enterprise-server@3.2/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.UsersApi();
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.usersListGpgKeysForAuthenticatedUser(opts, (error, data, response) => {
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
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[GpgKey]**](GpgKey.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersListGpgKeysForUser

> [GpgKey] usersListGpgKeysForUser(username, opts)

List GPG keys for a user

Lists the GPG keys for a user. This information is accessible by anyone.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.UsersApi();
let username = "username_example"; // String | The handle for the GitHub user account.
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.usersListGpgKeysForUser(username, opts, (error, data, response) => {
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
 **username** | **String**| The handle for the GitHub user account. | 
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[GpgKey]**](GpgKey.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersListPublicEmailsForAuthenticatedUser

> [Email] usersListPublicEmailsForAuthenticatedUser(opts)

List public email addresses for the authenticated user

Lists your publicly visible email address, which you can set with the [Set primary email visibility for the authenticated user](https://docs.github.com/enterprise-server@3.2/rest/reference/users#set-primary-email-visibility-for-the-authenticated-user) endpoint. This endpoint is accessible with the &#x60;user:email&#x60; scope.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.UsersApi();
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.usersListPublicEmailsForAuthenticatedUser(opts, (error, data, response) => {
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
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[Email]**](Email.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersListPublicKeysForUser

> [KeySimple] usersListPublicKeysForUser(username, opts)

List public keys for a user

Lists the _verified_ public SSH keys for a user. This is accessible by anyone.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.UsersApi();
let username = "username_example"; // String | The handle for the GitHub user account.
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.usersListPublicKeysForUser(username, opts, (error, data, response) => {
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
 **username** | **String**| The handle for the GitHub user account. | 
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[KeySimple]**](KeySimple.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersListPublicSshKeysForAuthenticatedUser

> [Key] usersListPublicSshKeysForAuthenticatedUser(opts)

List public SSH keys for the authenticated user

Lists the public SSH keys for the authenticated user&#39;s GitHub account. Requires that you are authenticated via Basic Auth or via OAuth with at least &#x60;read:public_key&#x60; [scope](https://docs.github.com/enterprise-server@3.2/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.UsersApi();
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.usersListPublicSshKeysForAuthenticatedUser(opts, (error, data, response) => {
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
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[Key]**](Key.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersUnfollow

> usersUnfollow(username)

Unfollow a user

Unfollowing a user requires the user to be logged in and authenticated with basic auth or OAuth with the &#x60;user:follow&#x60; scope.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.UsersApi();
let username = "username_example"; // String | The handle for the GitHub user account.
apiInstance.usersUnfollow(username, (error, data, response) => {
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
 **username** | **String**| The handle for the GitHub user account. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersUpdateAuthenticated

> PrivateUser usersUpdateAuthenticated(opts)

Update the authenticated user

**Note:** If your email is set to private and you send an &#x60;email&#x60; parameter as part of this request to update your profile, your privacy settings are still enforced: the email address will not be displayed on your public profile or via the API.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.UsersApi();
let opts = {
  'usersUpdateAuthenticatedRequest': {"blog":"https://github.com/blog","name":"monalisa octocat"} // UsersUpdateAuthenticatedRequest | 
};
apiInstance.usersUpdateAuthenticated(opts, (error, data, response) => {
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
 **usersUpdateAuthenticatedRequest** | [**UsersUpdateAuthenticatedRequest**](UsersUpdateAuthenticatedRequest.md)|  | [optional] 

### Return type

[**PrivateUser**](PrivateUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

