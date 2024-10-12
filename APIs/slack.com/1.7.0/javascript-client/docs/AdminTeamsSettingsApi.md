# SlackWebApi.AdminTeamsSettingsApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adminTeamsSettingsInfo**](AdminTeamsSettingsApi.md#adminTeamsSettingsInfo) | **GET** /admin.teams.settings.info | 
[**adminTeamsSettingsSetDefaultChannels**](AdminTeamsSettingsApi.md#adminTeamsSettingsSetDefaultChannels) | **POST** /admin.teams.settings.setDefaultChannels | 
[**adminTeamsSettingsSetDescription**](AdminTeamsSettingsApi.md#adminTeamsSettingsSetDescription) | **POST** /admin.teams.settings.setDescription | 
[**adminTeamsSettingsSetDiscoverability**](AdminTeamsSettingsApi.md#adminTeamsSettingsSetDiscoverability) | **POST** /admin.teams.settings.setDiscoverability | 
[**adminTeamsSettingsSetIcon**](AdminTeamsSettingsApi.md#adminTeamsSettingsSetIcon) | **POST** /admin.teams.settings.setIcon | 
[**adminTeamsSettingsSetName**](AdminTeamsSettingsApi.md#adminTeamsSettingsSetName) | **POST** /admin.teams.settings.setName | 



## adminTeamsSettingsInfo

> DefaultSuccessTemplate adminTeamsSettingsInfo(token, teamId)



Fetch information about settings in a workspace

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminTeamsSettingsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.teams:read`
let teamId = "teamId_example"; // String | 
apiInstance.adminTeamsSettingsInfo(token, teamId, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.teams:read&#x60; | 
 **teamId** | **String**|  | 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## adminTeamsSettingsSetDefaultChannels

> DefaultSuccessTemplate adminTeamsSettingsSetDefaultChannels(channelIds, teamId, token)



Set the default channels of a workspace.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminTeamsSettingsApi();
let channelIds = "channelIds_example"; // String | An array of channel IDs.
let teamId = "teamId_example"; // String | ID for the workspace to set the default channel for.
let token = "token_example"; // String | Authentication token. Requires scope: `admin.teams:write`
apiInstance.adminTeamsSettingsSetDefaultChannels(channelIds, teamId, token, (error, data, response) => {
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
 **channelIds** | **String**| An array of channel IDs. | 
 **teamId** | **String**| ID for the workspace to set the default channel for. | 
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.teams:write&#x60; | 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## adminTeamsSettingsSetDescription

> DefaultSuccessTemplate adminTeamsSettingsSetDescription(token, description, teamId)



Set the description of a given workspace.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminTeamsSettingsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.teams:write`
let description = "description_example"; // String | The new description for the workspace.
let teamId = "teamId_example"; // String | ID for the workspace to set the description for.
apiInstance.adminTeamsSettingsSetDescription(token, description, teamId, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.teams:write&#x60; | 
 **description** | **String**| The new description for the workspace. | 
 **teamId** | **String**| ID for the workspace to set the description for. | 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## adminTeamsSettingsSetDiscoverability

> DefaultSuccessTemplate adminTeamsSettingsSetDiscoverability(token, discoverability, teamId)



An API method that allows admins to set the discoverability of a given workspace

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminTeamsSettingsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.teams:write`
let discoverability = "discoverability_example"; // String | This workspace's discovery setting. It must be set to one of `open`, `invite_only`, `closed`, or `unlisted`.
let teamId = "teamId_example"; // String | The ID of the workspace to set discoverability on.
apiInstance.adminTeamsSettingsSetDiscoverability(token, discoverability, teamId, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.teams:write&#x60; | 
 **discoverability** | **String**| This workspace&#39;s discovery setting. It must be set to one of &#x60;open&#x60;, &#x60;invite_only&#x60;, &#x60;closed&#x60;, or &#x60;unlisted&#x60;. | 
 **teamId** | **String**| The ID of the workspace to set discoverability on. | 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## adminTeamsSettingsSetIcon

> DefaultSuccessTemplate adminTeamsSettingsSetIcon(imageUrl, teamId, token)



Sets the icon of a workspace.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminTeamsSettingsApi();
let imageUrl = "imageUrl_example"; // String | Image URL for the icon
let teamId = "teamId_example"; // String | ID for the workspace to set the icon for.
let token = "token_example"; // String | Authentication token. Requires scope: `admin.teams:write`
apiInstance.adminTeamsSettingsSetIcon(imageUrl, teamId, token, (error, data, response) => {
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
 **imageUrl** | **String**| Image URL for the icon | 
 **teamId** | **String**| ID for the workspace to set the icon for. | 
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.teams:write&#x60; | 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## adminTeamsSettingsSetName

> DefaultSuccessTemplate adminTeamsSettingsSetName(token, name, teamId)



Set the name of a given workspace.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminTeamsSettingsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.teams:write`
let name = "name_example"; // String | The new name of the workspace.
let teamId = "teamId_example"; // String | ID for the workspace to set the name for.
apiInstance.adminTeamsSettingsSetName(token, name, teamId, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.teams:write&#x60; | 
 **name** | **String**| The new name of the workspace. | 
 **teamId** | **String**| ID for the workspace to set the name for. | 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

