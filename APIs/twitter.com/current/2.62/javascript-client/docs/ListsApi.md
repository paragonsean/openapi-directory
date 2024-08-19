# TwitterApiV2.ListsApi

All URIs are relative to *https://api.twitter.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getUserListMemberships**](ListsApi.md#getUserListMemberships) | **GET** /2/users/{id}/list_memberships | Get a User&#39;s List Memberships
[**listAddMember**](ListsApi.md#listAddMember) | **POST** /2/lists/{id}/members | Add a List member
[**listIdCreate**](ListsApi.md#listIdCreate) | **POST** /2/lists | Create List
[**listIdDelete**](ListsApi.md#listIdDelete) | **DELETE** /2/lists/{id} | Delete List
[**listIdGet**](ListsApi.md#listIdGet) | **GET** /2/lists/{id} | List lookup by List ID.
[**listIdUpdate**](ListsApi.md#listIdUpdate) | **PUT** /2/lists/{id} | Update List.
[**listRemoveMember**](ListsApi.md#listRemoveMember) | **DELETE** /2/lists/{id}/members/{user_id} | Remove a List member
[**listUserFollow**](ListsApi.md#listUserFollow) | **POST** /2/users/{id}/followed_lists | Follow a List
[**listUserOwnedLists**](ListsApi.md#listUserOwnedLists) | **GET** /2/users/{id}/owned_lists | Get a User&#39;s Owned Lists.
[**listUserPin**](ListsApi.md#listUserPin) | **POST** /2/users/{id}/pinned_lists | Pin a List
[**listUserPinnedLists**](ListsApi.md#listUserPinnedLists) | **GET** /2/users/{id}/pinned_lists | Get a User&#39;s Pinned Lists
[**listUserUnfollow**](ListsApi.md#listUserUnfollow) | **DELETE** /2/users/{id}/followed_lists/{list_id} | Unfollow a List
[**listUserUnpin**](ListsApi.md#listUserUnpin) | **DELETE** /2/users/{id}/pinned_lists/{list_id} | Unpin a List
[**userFollowedLists**](ListsApi.md#userFollowedLists) | **GET** /2/users/{id}/followed_lists | Get User&#39;s Followed Lists



## getUserListMemberships

> Get2UsersIdListMembershipsResponse getUserListMemberships(id, opts)

Get a User&#39;s List Memberships

Get a User&#39;s List Memberships.

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

let apiInstance = new TwitterApiV2.ListsApi();
let id = "2244994945"; // String | The ID of the User to lookup.
let opts = {
  'maxResults': 100, // Number | The maximum number of results.
  'paginationToken': "paginationToken_example", // String | This parameter is used to get a specified 'page' of results.
  'listFields': ["null"], // [String] | A comma separated list of List fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'userFields': ["null"] // [String] | A comma separated list of User fields to display.
};
apiInstance.getUserListMemberships(id, opts, (error, data, response) => {
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
 **maxResults** | **Number**| The maximum number of results. | [optional] [default to 100]
 **paginationToken** | **String**| This parameter is used to get a specified &#39;page&#39; of results. | [optional] 
 **listFields** | [**[String]**](String.md)| A comma separated list of List fields to display. | [optional] 
 **expansions** | [**[String]**](String.md)| A comma separated list of fields to expand. | [optional] 
 **userFields** | [**[String]**](String.md)| A comma separated list of User fields to display. | [optional] 

### Return type

[**Get2UsersIdListMembershipsResponse**](Get2UsersIdListMembershipsResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [BearerToken](../README.md#BearerToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## listAddMember

> ListMutateResponse listAddMember(id, opts)

Add a List member

Causes a User to become a member of a List.

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TwitterApiV2.ListsApi();
let id = "id_example"; // String | The ID of the List for which to add a member.
let opts = {
  'listAddUserRequest': new TwitterApiV2.ListAddUserRequest() // ListAddUserRequest | 
};
apiInstance.listAddMember(id, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the List for which to add a member. | 
 **listAddUserRequest** | [**ListAddUserRequest**](ListAddUserRequest.md)|  | [optional] 

### Return type

[**ListMutateResponse**](ListMutateResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/problem+json


## listIdCreate

> ListCreateResponse listIdCreate(opts)

Create List

Creates a new List.

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TwitterApiV2.ListsApi();
let opts = {
  'listCreateRequest': new TwitterApiV2.ListCreateRequest() // ListCreateRequest | 
};
apiInstance.listIdCreate(opts, (error, data, response) => {
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
 **listCreateRequest** | [**ListCreateRequest**](ListCreateRequest.md)|  | [optional] 

### Return type

[**ListCreateResponse**](ListCreateResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/problem+json


## listIdDelete

> ListDeleteResponse listIdDelete(id)

Delete List

Delete a List that you own.

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TwitterApiV2.ListsApi();
let id = "id_example"; // String | The ID of the List to delete.
apiInstance.listIdDelete(id, (error, data, response) => {
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
 **id** | **String**| The ID of the List to delete. | 

### Return type

[**ListDeleteResponse**](ListDeleteResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## listIdGet

> Get2ListsIdResponse listIdGet(id, opts)

List lookup by List ID.

Returns a List.

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

let apiInstance = new TwitterApiV2.ListsApi();
let id = "id_example"; // String | The ID of the List.
let opts = {
  'listFields': ["null"], // [String] | A comma separated list of List fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'userFields': ["null"] // [String] | A comma separated list of User fields to display.
};
apiInstance.listIdGet(id, opts, (error, data, response) => {
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
 **listFields** | [**[String]**](String.md)| A comma separated list of List fields to display. | [optional] 
 **expansions** | [**[String]**](String.md)| A comma separated list of fields to expand. | [optional] 
 **userFields** | [**[String]**](String.md)| A comma separated list of User fields to display. | [optional] 

### Return type

[**Get2ListsIdResponse**](Get2ListsIdResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [BearerToken](../README.md#BearerToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## listIdUpdate

> ListUpdateResponse listIdUpdate(id, opts)

Update List.

Update a List that you own.

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TwitterApiV2.ListsApi();
let id = "id_example"; // String | The ID of the List to modify.
let opts = {
  'listUpdateRequest': new TwitterApiV2.ListUpdateRequest() // ListUpdateRequest | 
};
apiInstance.listIdUpdate(id, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the List to modify. | 
 **listUpdateRequest** | [**ListUpdateRequest**](ListUpdateRequest.md)|  | [optional] 

### Return type

[**ListUpdateResponse**](ListUpdateResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/problem+json


## listRemoveMember

> ListMutateResponse listRemoveMember(id, userId)

Remove a List member

Causes a User to be removed from the members of a List.

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TwitterApiV2.ListsApi();
let id = "id_example"; // String | The ID of the List to remove a member.
let userId = "userId_example"; // String | The ID of User that will be removed from the List.
apiInstance.listRemoveMember(id, userId, (error, data, response) => {
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
 **id** | **String**| The ID of the List to remove a member. | 
 **userId** | **String**| The ID of User that will be removed from the List. | 

### Return type

[**ListMutateResponse**](ListMutateResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## listUserFollow

> ListFollowedResponse listUserFollow(id, opts)

Follow a List

Causes a User to follow a List.

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TwitterApiV2.ListsApi();
let id = "id_example"; // String | The ID of the authenticated source User that will follow the List.
let opts = {
  'listFollowedRequest': new TwitterApiV2.ListFollowedRequest() // ListFollowedRequest | 
};
apiInstance.listUserFollow(id, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the authenticated source User that will follow the List. | 
 **listFollowedRequest** | [**ListFollowedRequest**](ListFollowedRequest.md)|  | [optional] 

### Return type

[**ListFollowedResponse**](ListFollowedResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/problem+json


## listUserOwnedLists

> Get2UsersIdOwnedListsResponse listUserOwnedLists(id, opts)

Get a User&#39;s Owned Lists.

Get a User&#39;s Owned Lists.

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

let apiInstance = new TwitterApiV2.ListsApi();
let id = "2244994945"; // String | The ID of the User to lookup.
let opts = {
  'maxResults': 100, // Number | The maximum number of results.
  'paginationToken': "paginationToken_example", // String | This parameter is used to get a specified 'page' of results.
  'listFields': ["null"], // [String] | A comma separated list of List fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'userFields': ["null"] // [String] | A comma separated list of User fields to display.
};
apiInstance.listUserOwnedLists(id, opts, (error, data, response) => {
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
 **maxResults** | **Number**| The maximum number of results. | [optional] [default to 100]
 **paginationToken** | **String**| This parameter is used to get a specified &#39;page&#39; of results. | [optional] 
 **listFields** | [**[String]**](String.md)| A comma separated list of List fields to display. | [optional] 
 **expansions** | [**[String]**](String.md)| A comma separated list of fields to expand. | [optional] 
 **userFields** | [**[String]**](String.md)| A comma separated list of User fields to display. | [optional] 

### Return type

[**Get2UsersIdOwnedListsResponse**](Get2UsersIdOwnedListsResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [BearerToken](../README.md#BearerToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## listUserPin

> ListPinnedResponse listUserPin(id, listPinnedRequest)

Pin a List

Causes a User to pin a List.

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TwitterApiV2.ListsApi();
let id = "id_example"; // String | The ID of the authenticated source User that will pin the List.
let listPinnedRequest = new TwitterApiV2.ListPinnedRequest(); // ListPinnedRequest | 
apiInstance.listUserPin(id, listPinnedRequest, (error, data, response) => {
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
 **id** | **String**| The ID of the authenticated source User that will pin the List. | 
 **listPinnedRequest** | [**ListPinnedRequest**](ListPinnedRequest.md)|  | 

### Return type

[**ListPinnedResponse**](ListPinnedResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/problem+json


## listUserPinnedLists

> Get2UsersIdPinnedListsResponse listUserPinnedLists(id, opts)

Get a User&#39;s Pinned Lists

Get a User&#39;s Pinned Lists.

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TwitterApiV2.ListsApi();
let id = "id_example"; // String | The ID of the authenticated source User for whom to return results.
let opts = {
  'listFields': ["null"], // [String] | A comma separated list of List fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'userFields': ["null"] // [String] | A comma separated list of User fields to display.
};
apiInstance.listUserPinnedLists(id, opts, (error, data, response) => {
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
 **listFields** | [**[String]**](String.md)| A comma separated list of List fields to display. | [optional] 
 **expansions** | [**[String]**](String.md)| A comma separated list of fields to expand. | [optional] 
 **userFields** | [**[String]**](String.md)| A comma separated list of User fields to display. | [optional] 

### Return type

[**Get2UsersIdPinnedListsResponse**](Get2UsersIdPinnedListsResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## listUserUnfollow

> ListFollowedResponse listUserUnfollow(id, listId)

Unfollow a List

Causes a User to unfollow a List.

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TwitterApiV2.ListsApi();
let id = "id_example"; // String | The ID of the authenticated source User that will unfollow the List.
let listId = "listId_example"; // String | The ID of the List to unfollow.
apiInstance.listUserUnfollow(id, listId, (error, data, response) => {
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
 **id** | **String**| The ID of the authenticated source User that will unfollow the List. | 
 **listId** | **String**| The ID of the List to unfollow. | 

### Return type

[**ListFollowedResponse**](ListFollowedResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## listUserUnpin

> ListUnpinResponse listUserUnpin(id, listId)

Unpin a List

Causes a User to remove a pinned List.

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TwitterApiV2.ListsApi();
let id = "id_example"; // String | The ID of the authenticated source User for whom to return results.
let listId = "listId_example"; // String | The ID of the List to unpin.
apiInstance.listUserUnpin(id, listId, (error, data, response) => {
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
 **listId** | **String**| The ID of the List to unpin. | 

### Return type

[**ListUnpinResponse**](ListUnpinResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## userFollowedLists

> Get2UsersIdFollowedListsResponse userFollowedLists(id, opts)

Get User&#39;s Followed Lists

Returns a User&#39;s followed Lists.

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

let apiInstance = new TwitterApiV2.ListsApi();
let id = "2244994945"; // String | The ID of the User to lookup.
let opts = {
  'maxResults': 100, // Number | The maximum number of results.
  'paginationToken': "paginationToken_example", // String | This parameter is used to get a specified 'page' of results.
  'listFields': ["null"], // [String] | A comma separated list of List fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'userFields': ["null"] // [String] | A comma separated list of User fields to display.
};
apiInstance.userFollowedLists(id, opts, (error, data, response) => {
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
 **maxResults** | **Number**| The maximum number of results. | [optional] [default to 100]
 **paginationToken** | **String**| This parameter is used to get a specified &#39;page&#39; of results. | [optional] 
 **listFields** | [**[String]**](String.md)| A comma separated list of List fields to display. | [optional] 
 **expansions** | [**[String]**](String.md)| A comma separated list of fields to expand. | [optional] 
 **userFields** | [**[String]**](String.md)| A comma separated list of User fields to display. | [optional] 

### Return type

[**Get2UsersIdFollowedListsResponse**](Get2UsersIdFollowedListsResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [BearerToken](../README.md#BearerToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json

