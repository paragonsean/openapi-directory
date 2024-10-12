# SlackWebApi.CallsApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**callsAdd**](CallsApi.md#callsAdd) | **POST** /calls.add | 
[**callsEnd**](CallsApi.md#callsEnd) | **POST** /calls.end | 
[**callsInfo**](CallsApi.md#callsInfo) | **GET** /calls.info | 
[**callsParticipantsAdd_0**](CallsApi.md#callsParticipantsAdd_0) | **POST** /calls.participants.add | 
[**callsParticipantsRemove_0**](CallsApi.md#callsParticipantsRemove_0) | **POST** /calls.participants.remove | 
[**callsUpdate**](CallsApi.md#callsUpdate) | **POST** /calls.update | 



## callsAdd

> DefaultSuccessTemplate callsAdd(token, externalUniqueId, joinUrl, opts)



Registers a new Call.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.CallsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `calls:write`
let externalUniqueId = "externalUniqueId_example"; // String | An ID supplied by the 3rd-party Call provider. It must be unique across all Calls from that service.
let joinUrl = "joinUrl_example"; // String | The URL required for a client to join the Call.
let opts = {
  'createdBy': "createdBy_example", // String | The valid Slack user ID of the user who created this Call. When this method is called with a user token, the `created_by` field is optional and defaults to the authed user of the token. Otherwise, the field is required.
  'dateStart': 56, // Number | Call start time in UTC UNIX timestamp format
  'desktopAppJoinUrl': "desktopAppJoinUrl_example", // String | When supplied, available Slack clients will attempt to directly launch the 3rd-party Call with this URL.
  'externalDisplayId': "externalDisplayId_example", // String | An optional, human-readable ID supplied by the 3rd-party Call provider. If supplied, this ID will be displayed in the Call object.
  'title': "title_example", // String | The name of the Call.
  'users': "users_example" // String | The list of users to register as participants in the Call. [Read more on how to specify users here](/apis/calls#users).
};
apiInstance.callsAdd(token, externalUniqueId, joinUrl, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;calls:write&#x60; | 
 **externalUniqueId** | **String**| An ID supplied by the 3rd-party Call provider. It must be unique across all Calls from that service. | 
 **joinUrl** | **String**| The URL required for a client to join the Call. | 
 **createdBy** | **String**| The valid Slack user ID of the user who created this Call. When this method is called with a user token, the &#x60;created_by&#x60; field is optional and defaults to the authed user of the token. Otherwise, the field is required. | [optional] 
 **dateStart** | **Number**| Call start time in UTC UNIX timestamp format | [optional] 
 **desktopAppJoinUrl** | **String**| When supplied, available Slack clients will attempt to directly launch the 3rd-party Call with this URL. | [optional] 
 **externalDisplayId** | **String**| An optional, human-readable ID supplied by the 3rd-party Call provider. If supplied, this ID will be displayed in the Call object. | [optional] 
 **title** | **String**| The name of the Call. | [optional] 
 **users** | **String**| The list of users to register as participants in the Call. [Read more on how to specify users here](/apis/calls#users). | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## callsEnd

> DefaultSuccessTemplate callsEnd(token, id, opts)



Ends a Call.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.CallsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `calls:write`
let id = "id_example"; // String | `id` returned when registering the call using the [`calls.add`](/methods/calls.add) method.
let opts = {
  'duration': 56 // Number | Call duration in seconds
};
apiInstance.callsEnd(token, id, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;calls:write&#x60; | 
 **id** | **String**| &#x60;id&#x60; returned when registering the call using the [&#x60;calls.add&#x60;](/methods/calls.add) method. | 
 **duration** | **Number**| Call duration in seconds | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## callsInfo

> DefaultSuccessTemplate callsInfo(token, id)



Returns information about a Call.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.CallsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `calls:read`
let id = "id_example"; // String | `id` of the Call returned by the [`calls.add`](/methods/calls.add) method.
apiInstance.callsInfo(token, id, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;calls:read&#x60; | 
 **id** | **String**| &#x60;id&#x60; of the Call returned by the [&#x60;calls.add&#x60;](/methods/calls.add) method. | 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## callsParticipantsAdd_0

> DefaultSuccessTemplate callsParticipantsAdd_0(token, id, users)



Registers new participants added to a Call.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.CallsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `calls:write`
let id = "id_example"; // String | `id` returned by the [`calls.add`](/methods/calls.add) method.
let users = "users_example"; // String | The list of users to add as participants in the Call. [Read more on how to specify users here](/apis/calls#users).
apiInstance.callsParticipantsAdd_0(token, id, users, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;calls:write&#x60; | 
 **id** | **String**| &#x60;id&#x60; returned by the [&#x60;calls.add&#x60;](/methods/calls.add) method. | 
 **users** | **String**| The list of users to add as participants in the Call. [Read more on how to specify users here](/apis/calls#users). | 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## callsParticipantsRemove_0

> DefaultSuccessTemplate callsParticipantsRemove_0(token, id, users)



Registers participants removed from a Call.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.CallsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `calls:write`
let id = "id_example"; // String | `id` returned by the [`calls.add`](/methods/calls.add) method.
let users = "users_example"; // String | The list of users to remove as participants in the Call. [Read more on how to specify users here](/apis/calls#users).
apiInstance.callsParticipantsRemove_0(token, id, users, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;calls:write&#x60; | 
 **id** | **String**| &#x60;id&#x60; returned by the [&#x60;calls.add&#x60;](/methods/calls.add) method. | 
 **users** | **String**| The list of users to remove as participants in the Call. [Read more on how to specify users here](/apis/calls#users). | 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## callsUpdate

> DefaultSuccessTemplate callsUpdate(token, id, opts)



Updates information about a Call.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.CallsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `calls:write`
let id = "id_example"; // String | `id` returned by the [`calls.add`](/methods/calls.add) method.
let opts = {
  'desktopAppJoinUrl': "desktopAppJoinUrl_example", // String | When supplied, available Slack clients will attempt to directly launch the 3rd-party Call with this URL.
  'joinUrl': "joinUrl_example", // String | The URL required for a client to join the Call.
  'title': "title_example" // String | The name of the Call.
};
apiInstance.callsUpdate(token, id, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;calls:write&#x60; | 
 **id** | **String**| &#x60;id&#x60; returned by the [&#x60;calls.add&#x60;](/methods/calls.add) method. | 
 **desktopAppJoinUrl** | **String**| When supplied, available Slack clients will attempt to directly launch the 3rd-party Call with this URL. | [optional] 
 **joinUrl** | **String**| The URL required for a client to join the Call. | [optional] 
 **title** | **String**| The name of the Call. | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

