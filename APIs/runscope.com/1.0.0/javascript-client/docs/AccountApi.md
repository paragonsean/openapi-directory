# RunscopeApi.AccountApi

All URIs are relative to *https://api.runscope.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountGet**](AccountApi.md#accountGet) | **GET** /account | Account Resource
[**teamsTeamIdAgentsGet**](AccountApi.md#teamsTeamIdAgentsGet) | **GET** /teams/{teamId}/agents | Team agents list
[**teamsTeamIdIntegrationsGet**](AccountApi.md#teamsTeamIdIntegrationsGet) | **GET** /teams/{teamId}/integrations | Team integrations list
[**teamsTeamIdPeopleGet**](AccountApi.md#teamsTeamIdPeopleGet) | **GET** /teams/{teamId}/people | Teams Resource



## accountGet

> AccountGet200Response accountGet()

Account Resource

Information about the authorized account.

### Example

```javascript
import RunscopeApi from 'runscope_api';
let defaultClient = RunscopeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: runscope_auth
let runscope_auth = defaultClient.authentications['runscope_auth'];
runscope_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RunscopeApi.AccountApi();
apiInstance.accountGet((error, data, response) => {
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

[**AccountGet200Response**](AccountGet200Response.md)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsTeamIdAgentsGet

> [Agent] teamsTeamIdAgentsGet(teamId)

Team agents list

List currently connected agents associated with a given team.

### Example

```javascript
import RunscopeApi from 'runscope_api';
let defaultClient = RunscopeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: runscope_auth
let runscope_auth = defaultClient.authentications['runscope_auth'];
runscope_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RunscopeApi.AccountApi();
let teamId = "teamId_example"; // String | Unique identifier for team
apiInstance.teamsTeamIdAgentsGet(teamId, (error, data, response) => {
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
 **teamId** | **String**| Unique identifier for team | 

### Return type

[**[Agent]**](Agent.md)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsTeamIdIntegrationsGet

> TeamsTeamIdIntegrationsGet200Response teamsTeamIdIntegrationsGet(teamId)

Team integrations list

Returns a list of integrations configured for the team.

### Example

```javascript
import RunscopeApi from 'runscope_api';
let defaultClient = RunscopeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: runscope_auth
let runscope_auth = defaultClient.authentications['runscope_auth'];
runscope_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RunscopeApi.AccountApi();
let teamId = "teamId_example"; // String | Unique identifier for team
apiInstance.teamsTeamIdIntegrationsGet(teamId, (error, data, response) => {
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
 **teamId** | **String**| Unique identifier for team | 

### Return type

[**TeamsTeamIdIntegrationsGet200Response**](TeamsTeamIdIntegrationsGet200Response.md)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsTeamIdPeopleGet

> [Account] teamsTeamIdPeopleGet(teamId)

Teams Resource

List people and integrations associated with a given team.

### Example

```javascript
import RunscopeApi from 'runscope_api';
let defaultClient = RunscopeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: runscope_auth
let runscope_auth = defaultClient.authentications['runscope_auth'];
runscope_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RunscopeApi.AccountApi();
let teamId = "teamId_example"; // String | Unique identifier for team
apiInstance.teamsTeamIdPeopleGet(teamId, (error, data, response) => {
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
 **teamId** | **String**| Unique identifier for team | 

### Return type

[**[Account]**](Account.md)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

