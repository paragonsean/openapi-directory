# VictorOps.TeamsApi

All URIs are relative to *https://api.victorops.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiPublicV1TeamGet**](TeamsApi.md#apiPublicV1TeamGet) | **GET** /api-public/v1/team | List teams
[**apiPublicV1TeamPost**](TeamsApi.md#apiPublicV1TeamPost) | **POST** /api-public/v1/team | Add a team
[**apiPublicV1TeamTeamAdminsGet**](TeamsApi.md#apiPublicV1TeamTeamAdminsGet) | **GET** /api-public/v1/team/{team}/admins | Retrieve a list of team admins for a team
[**apiPublicV1TeamTeamDelete**](TeamsApi.md#apiPublicV1TeamTeamDelete) | **DELETE** /api-public/v1/team/{team} | Remove a team
[**apiPublicV1TeamTeamGet**](TeamsApi.md#apiPublicV1TeamTeamGet) | **GET** /api-public/v1/team/{team} | Retrieve information for a team
[**apiPublicV1TeamTeamMembersGet**](TeamsApi.md#apiPublicV1TeamTeamMembersGet) | **GET** /api-public/v1/team/{team}/members | Retrieve a list of members for a team
[**apiPublicV1TeamTeamMembersPost**](TeamsApi.md#apiPublicV1TeamTeamMembersPost) | **POST** /api-public/v1/team/{team}/members | Add a team member
[**apiPublicV1TeamTeamMembersUserDelete**](TeamsApi.md#apiPublicV1TeamTeamMembersUserDelete) | **DELETE** /api-public/v1/team/{team}/members/{user} | Remove a team member
[**apiPublicV1TeamTeamPoliciesGet_0**](TeamsApi.md#apiPublicV1TeamTeamPoliciesGet_0) | **GET** /api-public/v1/team/{team}/policies | Retrieve a list of escalation policies for a team
[**apiPublicV1TeamTeamPut**](TeamsApi.md#apiPublicV1TeamTeamPut) | **PUT** /api-public/v1/team/{team} | Update a team



## apiPublicV1TeamGet

> [TeamDetail] apiPublicV1TeamGet(xVOApiId, xVOApiKey)

List teams

Get a list of teams for your organization.  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.TeamsApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
apiInstance.apiPublicV1TeamGet(xVOApiId, xVOApiKey, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 

### Return type

[**[TeamDetail]**](TeamDetail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1TeamPost

> TeamDetail apiPublicV1TeamPost(xVOApiId, xVOApiKey, body)

Add a team

Add a team to your organization.  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.TeamsApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let body = new VictorOps.AddTeamPayload(); // AddTeamPayload | The team information
apiInstance.apiPublicV1TeamPost(xVOApiId, xVOApiKey, body, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **body** | [**AddTeamPayload**](AddTeamPayload.md)| The team information | 

### Return type

[**TeamDetail**](TeamDetail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1TeamTeamAdminsGet

> TeamAdminsResponse apiPublicV1TeamTeamAdminsGet(xVOApiId, xVOApiKey, team)

Retrieve a list of team admins for a team

Get the team admins for the specified team.  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.TeamsApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let team = "team_example"; // String | The VictorOps team
apiInstance.apiPublicV1TeamTeamAdminsGet(xVOApiId, xVOApiKey, team, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **team** | **String**| The VictorOps team | 

### Return type

[**TeamAdminsResponse**](TeamAdminsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1TeamTeamDelete

> apiPublicV1TeamTeamDelete(xVOApiId, xVOApiKey, team)

Remove a team

Remove a team from your organization.  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.TeamsApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let team = "team_example"; // String | The VictorOps team to be deleted
apiInstance.apiPublicV1TeamTeamDelete(xVOApiId, xVOApiKey, team, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **team** | **String**| The VictorOps team to be deleted | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiPublicV1TeamTeamGet

> TeamDetail apiPublicV1TeamTeamGet(xVOApiId, xVOApiKey, team)

Retrieve information for a team

Get the information for the specified team.  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.TeamsApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let team = "team_example"; // String | The VictorOps team to fetch
apiInstance.apiPublicV1TeamTeamGet(xVOApiId, xVOApiKey, team, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **team** | **String**| The VictorOps team to fetch | 

### Return type

[**TeamDetail**](TeamDetail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1TeamTeamMembersGet

> ListTeamMembersResponse apiPublicV1TeamTeamMembersGet(xVOApiId, xVOApiKey, team)

Retrieve a list of members for a team

Get the members for the specified team.  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.TeamsApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let team = "team_example"; // String | The VictorOps team to fetch
apiInstance.apiPublicV1TeamTeamMembersGet(xVOApiId, xVOApiKey, team, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **team** | **String**| The VictorOps team to fetch | 

### Return type

[**ListTeamMembersResponse**](ListTeamMembersResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1TeamTeamMembersPost

> ListTeamMembersResponse apiPublicV1TeamTeamMembersPost(xVOApiId, xVOApiKey, team, body)

Add a team member

Add a team member to your team.  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.TeamsApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let team = "team_example"; // String | The VictorOps team to fetch
let body = new VictorOps.AddTeamMemberPayload(); // AddTeamMemberPayload | 
apiInstance.apiPublicV1TeamTeamMembersPost(xVOApiId, xVOApiKey, team, body, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **team** | **String**| The VictorOps team to fetch | 
 **body** | [**AddTeamMemberPayload**](AddTeamMemberPayload.md)|  | 

### Return type

[**ListTeamMembersResponse**](ListTeamMembersResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1TeamTeamMembersUserDelete

> apiPublicV1TeamTeamMembersUserDelete(xVOApiId, xVOApiKey, team, user, body)

Remove a team member

Remove a team from your organization.  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.TeamsApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let team = "team_example"; // String | The VictorOps team to be deleted
let user = "user_example"; // String | The team member username
let body = new VictorOps.RemoveTeamMemberPayload(); // RemoveTeamMemberPayload | The user information
apiInstance.apiPublicV1TeamTeamMembersUserDelete(xVOApiId, xVOApiKey, team, user, body, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **team** | **String**| The VictorOps team to be deleted | 
 **user** | **String**| The team member username | 
 **body** | [**RemoveTeamMemberPayload**](RemoveTeamMemberPayload.md)| The user information | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiPublicV1TeamTeamPoliciesGet_0

> EscalationPolicyList apiPublicV1TeamTeamPoliciesGet_0(xVOApiId, xVOApiKey, team)

Retrieve a list of escalation policies for a team

Get the escalation policies for the specified team.  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.TeamsApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let team = "team_example"; // String | The VictorOps team to fetch
apiInstance.apiPublicV1TeamTeamPoliciesGet_0(xVOApiId, xVOApiKey, team, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **team** | **String**| The VictorOps team to fetch | 

### Return type

[**EscalationPolicyList**](EscalationPolicyList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1TeamTeamPut

> TeamDetail apiPublicV1TeamTeamPut(xVOApiId, xVOApiKey, team, body)

Update a team

Update the designated team  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.TeamsApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let team = "team_example"; // String | The VictorOps team to be updated
let body = new VictorOps.AddTeamPayload(); // AddTeamPayload | The team information
apiInstance.apiPublicV1TeamTeamPut(xVOApiId, xVOApiKey, team, body, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **team** | **String**| The VictorOps team to be updated | 
 **body** | [**AddTeamPayload**](AddTeamPayload.md)| The team information | 

### Return type

[**TeamDetail**](TeamDetail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

