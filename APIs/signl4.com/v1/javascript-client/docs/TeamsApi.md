# Signl4Api.TeamsApi

All URIs are relative to *https://connect.signl4.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscriptionsSubscriptionIdTeamsGet**](TeamsApi.md#subscriptionsSubscriptionIdTeamsGet) | **GET** /subscriptions/{subscriptionId}/teams | Get infos for all teams of the subscription.
[**teamsGet**](TeamsApi.md#teamsGet) | **GET** /teams | Get infos of all teams.
[**teamsTeamIdAlertReportsFileNameGet**](TeamsApi.md#teamsTeamIdAlertReportsFileNameGet) | **GET** /teams/{teamId}/alertReports/{fileName} | Returns Alert Report
[**teamsTeamIdAlertReportsGet**](TeamsApi.md#teamsTeamIdAlertReportsGet) | **GET** /teams/{teamId}/alertReports | Get information about downloadable alert reports
[**teamsTeamIdAlertSettingsGet**](TeamsApi.md#teamsTeamIdAlertSettingsGet) | **GET** /teams/{teamId}/alertSettings | Gets alert settings of a specific team.
[**teamsTeamIdAlertSettingsPost**](TeamsApi.md#teamsTeamIdAlertSettingsPost) | **POST** /teams/{teamId}/alertSettings | Sets alert settings of a specific team.
[**teamsTeamIdEventSourcesGet**](TeamsApi.md#teamsTeamIdEventSourcesGet) | **GET** /teams/{teamId}/eventSources | Gets event sources of a specific team.
[**teamsTeamIdGet**](TeamsApi.md#teamsTeamIdGet) | **GET** /teams/{teamId} | Gets infos of a specific team.
[**teamsTeamIdProfilePut**](TeamsApi.md#teamsTeamIdProfilePut) | **PUT** /teams/{teamId}/profile | Updates team profile of a team
[**teamsTeamIdSetupProgressGet**](TeamsApi.md#teamsTeamIdSetupProgressGet) | **GET** /teams/{teamId}/setupProgress | Gets setup progress of a specific team.



## subscriptionsSubscriptionIdTeamsGet

> [TeamInfo] subscriptionsSubscriptionIdTeamsGet(subscriptionId)

Get infos for all teams of the subscription.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.TeamsApi();
let subscriptionId = "subscriptionId_example"; // String | 
apiInstance.subscriptionsSubscriptionIdTeamsGet(subscriptionId, (error, data, response) => {
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
 **subscriptionId** | **String**|  | 

### Return type

[**[TeamInfo]**](TeamInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## teamsGet

> [TeamInfo] teamsGet()

Get infos of all teams.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.TeamsApi();
apiInstance.teamsGet((error, data, response) => {
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

[**[TeamInfo]**](TeamInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## teamsTeamIdAlertReportsFileNameGet

> File teamsTeamIdAlertReportsFileNameGet(teamId, fileName)

Returns Alert Report

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.TeamsApi();
let teamId = "teamId_example"; // String | ID of team you want to get the duty report file infos for.
let fileName = "fileName_example"; // String | File name of file you want to download.
apiInstance.teamsTeamIdAlertReportsFileNameGet(teamId, fileName, (error, data, response) => {
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
 **teamId** | **String**| ID of team you want to get the duty report file infos for. | 
 **fileName** | **String**| File name of file you want to download. | 

### Return type

**File**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## teamsTeamIdAlertReportsGet

> [Object] teamsTeamIdAlertReportsGet(teamId)

Get information about downloadable alert reports

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.TeamsApi();
let teamId = "teamId_example"; // String | ID of team you want to download reports from.
apiInstance.teamsTeamIdAlertReportsGet(teamId, (error, data, response) => {
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
 **teamId** | **String**| ID of team you want to download reports from. | 

### Return type

**[Object]**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## teamsTeamIdAlertSettingsGet

> AlertSettings teamsTeamIdAlertSettingsGet(teamId)

Gets alert settings of a specific team.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.TeamsApi();
let teamId = "teamId_example"; // String | ID of the team the settings should be retrieved for.
apiInstance.teamsTeamIdAlertSettingsGet(teamId, (error, data, response) => {
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
 **teamId** | **String**| ID of the team the settings should be retrieved for. | 

### Return type

[**AlertSettings**](AlertSettings.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## teamsTeamIdAlertSettingsPost

> AlertSettings teamsTeamIdAlertSettingsPost(teamId, opts)

Sets alert settings of a specific team.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.TeamsApi();
let teamId = "teamId_example"; // String | ID of the team the settings should be set for.
let opts = {
  'alertSettings': new Signl4Api.AlertSettings() // AlertSettings | Alert settings to be set
};
apiInstance.teamsTeamIdAlertSettingsPost(teamId, opts, (error, data, response) => {
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
 **teamId** | **String**| ID of the team the settings should be set for. | 
 **alertSettings** | [**AlertSettings**](AlertSettings.md)| Alert settings to be set | [optional] 

### Return type

[**AlertSettings**](AlertSettings.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## teamsTeamIdEventSourcesGet

> [EventSourceEndpointInfo] teamsTeamIdEventSourcesGet(teamId)

Gets event sources of a specific team.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.TeamsApi();
let teamId = "teamId_example"; // String | ID of the team the sources should be retrieved for.
apiInstance.teamsTeamIdEventSourcesGet(teamId, (error, data, response) => {
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
 **teamId** | **String**| ID of the team the sources should be retrieved for. | 

### Return type

[**[EventSourceEndpointInfo]**](EventSourceEndpointInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## teamsTeamIdGet

> TeamInfo teamsTeamIdGet(teamId)

Gets infos of a specific team.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.TeamsApi();
let teamId = "teamId_example"; // String | ID of the team that should be retrieved.
apiInstance.teamsTeamIdGet(teamId, (error, data, response) => {
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
 **teamId** | **String**| ID of the team that should be retrieved. | 

### Return type

[**TeamInfo**](TeamInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## teamsTeamIdProfilePut

> TeamInfo teamsTeamIdProfilePut(teamId, opts)

Updates team profile of a team

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.TeamsApi();
let teamId = "teamId_example"; // String | Team ID of team which should be updated.
let opts = {
  'teamProfile': new Signl4Api.TeamProfile() // TeamProfile | 
};
apiInstance.teamsTeamIdProfilePut(teamId, opts, (error, data, response) => {
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
 **teamId** | **String**| Team ID of team which should be updated. | 
 **teamProfile** | [**TeamProfile**](TeamProfile.md)|  | [optional] 

### Return type

[**TeamInfo**](TeamInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## teamsTeamIdSetupProgressGet

> TeamSetupProgress teamsTeamIdSetupProgressGet(teamId)

Gets setup progress of a specific team.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.TeamsApi();
let teamId = "teamId_example"; // String | ID of the team the progress should be retrieved for.
apiInstance.teamsTeamIdSetupProgressGet(teamId, (error, data, response) => {
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
 **teamId** | **String**| ID of the team the progress should be retrieved for. | 

### Return type

[**TeamSetupProgress**](TeamSetupProgress.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

