# Appwrite.TeamsApi

All URIs are relative to *https://appwrite.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**teamsCreate**](TeamsApi.md#teamsCreate) | **POST** /teams | Create Team
[**teamsCreateMembership**](TeamsApi.md#teamsCreateMembership) | **POST** /teams/{teamId}/memberships | Create Team Membership
[**teamsDelete**](TeamsApi.md#teamsDelete) | **DELETE** /teams/{teamId} | Delete Team
[**teamsDeleteMembership**](TeamsApi.md#teamsDeleteMembership) | **DELETE** /teams/{teamId}/memberships/{membershipId} | Delete Team Membership
[**teamsGet**](TeamsApi.md#teamsGet) | **GET** /teams/{teamId} | Get Team
[**teamsGetMemberships**](TeamsApi.md#teamsGetMemberships) | **GET** /teams/{teamId}/memberships | Get Team Memberships
[**teamsList**](TeamsApi.md#teamsList) | **GET** /teams | List Teams
[**teamsUpdate**](TeamsApi.md#teamsUpdate) | **PUT** /teams/{teamId} | Update Team
[**teamsUpdateMembershipRoles**](TeamsApi.md#teamsUpdateMembershipRoles) | **PATCH** /teams/{teamId}/memberships/{membershipId} | Update Membership Roles
[**teamsUpdateMembershipStatus**](TeamsApi.md#teamsUpdateMembershipStatus) | **PATCH** /teams/{teamId}/memberships/{membershipId}/status | Update Team Membership Status



## teamsCreate

> Team teamsCreate(opts)

Create Team

Create a new team. The user who creates the team will automatically be assigned as the owner of the team. The team owner can invite new members, who will be able add new owners and update or delete the team from your project.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.TeamsApi();
let opts = {
  'teamsCreateRequest': new Appwrite.TeamsCreateRequest() // TeamsCreateRequest | 
};
apiInstance.teamsCreate(opts, (error, data, response) => {
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
 **teamsCreateRequest** | [**TeamsCreateRequest**](TeamsCreateRequest.md)|  | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## teamsCreateMembership

> Membership teamsCreateMembership(teamId, opts)

Create Team Membership

Use this endpoint to invite a new member to join your team. If initiated from Client SDK, an email with a link to join the team will be sent to the new member&#39;s email address if the member doesn&#39;t exist in the project it will be created automatically. If initiated from server side SDKs, new member will automatically be added to the team.  Use the &#39;URL&#39; parameter to redirect the user from the invitation email back to your app. When the user is redirected, use the [Update Team Membership Status](/docs/client/teams#teamsUpdateMembershipStatus) endpoint to allow the user to accept the invitation to the team.  While calling from side SDKs the redirect url can be empty string.  Please note that in order to avoid a [Redirect Attacks](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.md) the only valid redirect URL&#39;s are the once from domains you have set when added your platforms in the console interface.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.TeamsApi();
let teamId = "teamId_example"; // String | Team unique ID.
let opts = {
  'teamsCreateMembershipRequest': new Appwrite.TeamsCreateMembershipRequest() // TeamsCreateMembershipRequest | 
};
apiInstance.teamsCreateMembership(teamId, opts, (error, data, response) => {
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
 **teamId** | **String**| Team unique ID. | 
 **teamsCreateMembershipRequest** | [**TeamsCreateMembershipRequest**](TeamsCreateMembershipRequest.md)|  | [optional] 

### Return type

[**Membership**](Membership.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## teamsDelete

> teamsDelete(teamId)

Delete Team

Delete a team by its unique ID. Only team owners have write access for this resource.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.TeamsApi();
let teamId = "teamId_example"; // String | Team unique ID.
apiInstance.teamsDelete(teamId, (error, data, response) => {
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
 **teamId** | **String**| Team unique ID. | 

### Return type

null (empty response body)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## teamsDeleteMembership

> teamsDeleteMembership(teamId, membershipId)

Delete Team Membership

This endpoint allows a user to leave a team or for a team owner to delete the membership of any other team member. You can also use this endpoint to delete a user membership even if it is not accepted.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.TeamsApi();
let teamId = "teamId_example"; // String | Team unique ID.
let membershipId = "membershipId_example"; // String | Membership ID.
apiInstance.teamsDeleteMembership(teamId, membershipId, (error, data, response) => {
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
 **teamId** | **String**| Team unique ID. | 
 **membershipId** | **String**| Membership ID. | 

### Return type

null (empty response body)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## teamsGet

> Team teamsGet(teamId)

Get Team

Get a team by its unique ID. All team members have read access for this resource.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.TeamsApi();
let teamId = "teamId_example"; // String | Team unique ID.
apiInstance.teamsGet(teamId, (error, data, response) => {
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
 **teamId** | **String**| Team unique ID. | 

### Return type

[**Team**](Team.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsGetMemberships

> MembershipList teamsGetMemberships(teamId, opts)

Get Team Memberships

Get a team members by the team unique ID. All team members have read access for this list of resources.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.TeamsApi();
let teamId = "teamId_example"; // String | Team unique ID.
let opts = {
  'search': "''", // String | Search term to filter your list results. Max length: 256 chars.
  'limit': 25, // Number | Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.
  'offset': 0, // Number | Results offset. The default value is 0. Use this param to manage pagination.
  'orderType': "'ASC'" // String | Order result by ASC or DESC order.
};
apiInstance.teamsGetMemberships(teamId, opts, (error, data, response) => {
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
 **teamId** | **String**| Team unique ID. | 
 **search** | **String**| Search term to filter your list results. Max length: 256 chars. | [optional] [default to &#39;&#39;]
 **limit** | **Number**| Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request. | [optional] [default to 25]
 **offset** | **Number**| Results offset. The default value is 0. Use this param to manage pagination. | [optional] [default to 0]
 **orderType** | **String**| Order result by ASC or DESC order. | [optional] [default to &#39;ASC&#39;]

### Return type

[**MembershipList**](MembershipList.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsList

> TeamList teamsList(opts)

List Teams

Get a list of all the current user teams. You can use the query params to filter your results. On admin mode, this endpoint will return a list of all of the project&#39;s teams. [Learn more about different API modes](/docs/admin).

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.TeamsApi();
let opts = {
  'search': "''", // String | Search term to filter your list results. Max length: 256 chars.
  'limit': 25, // Number | Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.
  'offset': 0, // Number | Results offset. The default value is 0. Use this param to manage pagination.
  'orderType': "'ASC'" // String | Order result by ASC or DESC order.
};
apiInstance.teamsList(opts, (error, data, response) => {
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
 **search** | **String**| Search term to filter your list results. Max length: 256 chars. | [optional] [default to &#39;&#39;]
 **limit** | **Number**| Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request. | [optional] [default to 25]
 **offset** | **Number**| Results offset. The default value is 0. Use this param to manage pagination. | [optional] [default to 0]
 **orderType** | **String**| Order result by ASC or DESC order. | [optional] [default to &#39;ASC&#39;]

### Return type

[**TeamList**](TeamList.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsUpdate

> Team teamsUpdate(teamId, opts)

Update Team

Update a team by its unique ID. Only team owners have write access for this resource.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.TeamsApi();
let teamId = "teamId_example"; // String | Team unique ID.
let opts = {
  'teamsUpdateRequest': new Appwrite.TeamsUpdateRequest() // TeamsUpdateRequest | 
};
apiInstance.teamsUpdate(teamId, opts, (error, data, response) => {
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
 **teamId** | **String**| Team unique ID. | 
 **teamsUpdateRequest** | [**TeamsUpdateRequest**](TeamsUpdateRequest.md)|  | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## teamsUpdateMembershipRoles

> Membership teamsUpdateMembershipRoles(teamId, membershipId, opts)

Update Membership Roles



### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.TeamsApi();
let teamId = "teamId_example"; // String | Team unique ID.
let membershipId = "membershipId_example"; // String | Membership ID.
let opts = {
  'teamsUpdateMembershipRolesRequest': new Appwrite.TeamsUpdateMembershipRolesRequest() // TeamsUpdateMembershipRolesRequest | 
};
apiInstance.teamsUpdateMembershipRoles(teamId, membershipId, opts, (error, data, response) => {
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
 **teamId** | **String**| Team unique ID. | 
 **membershipId** | **String**| Membership ID. | 
 **teamsUpdateMembershipRolesRequest** | [**TeamsUpdateMembershipRolesRequest**](TeamsUpdateMembershipRolesRequest.md)|  | [optional] 

### Return type

[**Membership**](Membership.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## teamsUpdateMembershipStatus

> Membership teamsUpdateMembershipStatus(teamId, membershipId, opts)

Update Team Membership Status

Use this endpoint to allow a user to accept an invitation to join a team after being redirected back to your app from the invitation email recieved by the user.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.TeamsApi();
let teamId = "teamId_example"; // String | Team unique ID.
let membershipId = "membershipId_example"; // String | Membership ID.
let opts = {
  'teamsUpdateMembershipStatusRequest': new Appwrite.TeamsUpdateMembershipStatusRequest() // TeamsUpdateMembershipStatusRequest | 
};
apiInstance.teamsUpdateMembershipStatus(teamId, membershipId, opts, (error, data, response) => {
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
 **teamId** | **String**| Team unique ID. | 
 **membershipId** | **String**| Membership ID. | 
 **teamsUpdateMembershipStatusRequest** | [**TeamsUpdateMembershipStatusRequest**](TeamsUpdateMembershipStatusRequest.md)|  | [optional] 

### Return type

[**Membership**](Membership.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

