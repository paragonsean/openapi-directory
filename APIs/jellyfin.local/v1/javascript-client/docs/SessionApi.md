# JellyfinApi.SessionApi

All URIs are relative to *http://jellyfin.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addUserToSession**](SessionApi.md#addUserToSession) | **POST** /Sessions/{sessionId}/User/{userId} | Adds an additional user to a session.
[**displayContent**](SessionApi.md#displayContent) | **POST** /Sessions/{sessionId}/Viewing | Instructs a session to browse to an item or view.
[**getAuthProviders**](SessionApi.md#getAuthProviders) | **GET** /Auth/Providers | Get all auth providers.
[**getPasswordResetProviders**](SessionApi.md#getPasswordResetProviders) | **GET** /Auth/PasswordResetProviders | Get all password reset providers.
[**getSessions**](SessionApi.md#getSessions) | **GET** /Sessions | Gets a list of sessions.
[**play**](SessionApi.md#play) | **POST** /Sessions/{sessionId}/Playing | Instructs a session to play an item.
[**postCapabilities**](SessionApi.md#postCapabilities) | **POST** /Sessions/Capabilities | Updates capabilities for a device.
[**postFullCapabilities**](SessionApi.md#postFullCapabilities) | **POST** /Sessions/Capabilities/Full | Updates capabilities for a device.
[**removeUserFromSession**](SessionApi.md#removeUserFromSession) | **DELETE** /Sessions/{sessionId}/User/{userId} | Removes an additional user from a session.
[**reportSessionEnded**](SessionApi.md#reportSessionEnded) | **POST** /Sessions/Logout | Reports that a session has ended.
[**reportViewing**](SessionApi.md#reportViewing) | **POST** /Sessions/Viewing | Reports that a session is viewing an item.
[**sendFullGeneralCommand**](SessionApi.md#sendFullGeneralCommand) | **POST** /Sessions/{sessionId}/Command | Issues a full general command to a client.
[**sendGeneralCommand**](SessionApi.md#sendGeneralCommand) | **POST** /Sessions/{sessionId}/Command/{command} | Issues a general command to a client.
[**sendMessageCommand**](SessionApi.md#sendMessageCommand) | **POST** /Sessions/{sessionId}/Message | Issues a command to a client to display a message to the user.
[**sendPlaystateCommand**](SessionApi.md#sendPlaystateCommand) | **POST** /Sessions/{sessionId}/Playing/{command} | Issues a playstate command to a client.
[**sendSystemCommand**](SessionApi.md#sendSystemCommand) | **POST** /Sessions/{sessionId}/System/{command} | Issues a system command to a client.



## addUserToSession

> addUserToSession(sessionId, userId)

Adds an additional user to a session.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.SessionApi();
let sessionId = "sessionId_example"; // String | The session id.
let userId = "userId_example"; // String | The user id.
apiInstance.addUserToSession(sessionId, userId, (error, data, response) => {
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
 **sessionId** | **String**| The session id. | 
 **userId** | **String**| The user id. | 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## displayContent

> displayContent(sessionId, itemType, itemId, itemName)

Instructs a session to browse to an item or view.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.SessionApi();
let sessionId = "sessionId_example"; // String | The session Id.
let itemType = "itemType_example"; // String | The type of item to browse to.
let itemId = "itemId_example"; // String | The Id of the item.
let itemName = "itemName_example"; // String | The name of the item.
apiInstance.displayContent(sessionId, itemType, itemId, itemName, (error, data, response) => {
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
 **sessionId** | **String**| The session Id. | 
 **itemType** | **String**| The type of item to browse to. | 
 **itemId** | **String**| The Id of the item. | 
 **itemName** | **String**| The name of the item. | 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAuthProviders

> [NameIdPair] getAuthProviders()

Get all auth providers.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.SessionApi();
apiInstance.getAuthProviders((error, data, response) => {
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

[**[NameIdPair]**](NameIdPair.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getPasswordResetProviders

> [NameIdPair] getPasswordResetProviders()

Get all password reset providers.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.SessionApi();
apiInstance.getPasswordResetProviders((error, data, response) => {
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

[**[NameIdPair]**](NameIdPair.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getSessions

> [SessionInfo] getSessions(opts)

Gets a list of sessions.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.SessionApi();
let opts = {
  'controllableByUserId': "controllableByUserId_example", // String | Filter by sessions that a given user is allowed to remote control.
  'deviceId': "deviceId_example", // String | Filter by device Id.
  'activeWithinSeconds': 56 // Number | Optional. Filter by sessions that were active in the last n seconds.
};
apiInstance.getSessions(opts, (error, data, response) => {
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
 **controllableByUserId** | **String**| Filter by sessions that a given user is allowed to remote control. | [optional] 
 **deviceId** | **String**| Filter by device Id. | [optional] 
 **activeWithinSeconds** | **Number**| Optional. Filter by sessions that were active in the last n seconds. | [optional] 

### Return type

[**[SessionInfo]**](SessionInfo.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## play

> play(sessionId, playCommand, itemIds, opts)

Instructs a session to play an item.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.SessionApi();
let sessionId = "sessionId_example"; // String | The session id.
let playCommand = new JellyfinApi.PlayCommand(); // PlayCommand | The type of play command to issue (PlayNow, PlayNext, PlayLast). Clients who have not yet implemented play next and play last may play now.
let itemIds = ["null"]; // [String] | The ids of the items to play, comma delimited.
let opts = {
  'startPositionTicks': 789 // Number | The starting position of the first item.
};
apiInstance.play(sessionId, playCommand, itemIds, opts, (error, data, response) => {
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
 **sessionId** | **String**| The session id. | 
 **playCommand** | [**PlayCommand**](.md)| The type of play command to issue (PlayNow, PlayNext, PlayLast). Clients who have not yet implemented play next and play last may play now. | 
 **itemIds** | [**[String]**](String.md)| The ids of the items to play, comma delimited. | 
 **startPositionTicks** | **Number**| The starting position of the first item. | [optional] 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postCapabilities

> postCapabilities(opts)

Updates capabilities for a device.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.SessionApi();
let opts = {
  'id': "id_example", // String | The session id.
  'playableMediaTypes': ["null"], // [String] | A list of playable media types, comma delimited. Audio, Video, Book, Photo.
  'supportedCommands': [new JellyfinApi.GeneralCommandType()], // [GeneralCommandType] | A list of supported remote control commands, comma delimited.
  'supportsMediaControl': false, // Boolean | Determines whether media can be played remotely..
  'supportsSync': false, // Boolean | Determines whether sync is supported.
  'supportsPersistentIdentifier': true // Boolean | Determines whether the device supports a unique identifier.
};
apiInstance.postCapabilities(opts, (error, data, response) => {
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
 **id** | **String**| The session id. | [optional] 
 **playableMediaTypes** | [**[String]**](String.md)| A list of playable media types, comma delimited. Audio, Video, Book, Photo. | [optional] 
 **supportedCommands** | [**[GeneralCommandType]**](GeneralCommandType.md)| A list of supported remote control commands, comma delimited. | [optional] 
 **supportsMediaControl** | **Boolean**| Determines whether media can be played remotely.. | [optional] [default to false]
 **supportsSync** | **Boolean**| Determines whether sync is supported. | [optional] [default to false]
 **supportsPersistentIdentifier** | **Boolean**| Determines whether the device supports a unique identifier. | [optional] [default to true]

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postFullCapabilities

> postFullCapabilities(clientCapabilitiesDto, opts)

Updates capabilities for a device.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.SessionApi();
let clientCapabilitiesDto = new JellyfinApi.ClientCapabilitiesDto(); // ClientCapabilitiesDto | The MediaBrowser.Model.Session.ClientCapabilities.
let opts = {
  'id': "id_example" // String | The session id.
};
apiInstance.postFullCapabilities(clientCapabilitiesDto, opts, (error, data, response) => {
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
 **clientCapabilitiesDto** | [**ClientCapabilitiesDto**](ClientCapabilitiesDto.md)| The MediaBrowser.Model.Session.ClientCapabilities. | 
 **id** | **String**| The session id. | [optional] 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: Not defined


## removeUserFromSession

> removeUserFromSession(sessionId, userId)

Removes an additional user from a session.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.SessionApi();
let sessionId = "sessionId_example"; // String | The session id.
let userId = "userId_example"; // String | The user id.
apiInstance.removeUserFromSession(sessionId, userId, (error, data, response) => {
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
 **sessionId** | **String**| The session id. | 
 **userId** | **String**| The user id. | 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## reportSessionEnded

> reportSessionEnded()

Reports that a session has ended.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.SessionApi();
apiInstance.reportSessionEnded((error, data, response) => {
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

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## reportViewing

> reportViewing(itemId, opts)

Reports that a session is viewing an item.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.SessionApi();
let itemId = "itemId_example"; // String | The item id.
let opts = {
  'sessionId': "sessionId_example" // String | The session id.
};
apiInstance.reportViewing(itemId, opts, (error, data, response) => {
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
 **itemId** | **String**| The item id. | 
 **sessionId** | **String**| The session id. | [optional] 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## sendFullGeneralCommand

> sendFullGeneralCommand(sessionId, generalCommand)

Issues a full general command to a client.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.SessionApi();
let sessionId = "sessionId_example"; // String | The session id.
let generalCommand = new JellyfinApi.GeneralCommand(); // GeneralCommand | The MediaBrowser.Model.Session.GeneralCommand.
apiInstance.sendFullGeneralCommand(sessionId, generalCommand, (error, data, response) => {
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
 **sessionId** | **String**| The session id. | 
 **generalCommand** | [**GeneralCommand**](GeneralCommand.md)| The MediaBrowser.Model.Session.GeneralCommand. | 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: Not defined


## sendGeneralCommand

> sendGeneralCommand(sessionId, command)

Issues a general command to a client.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.SessionApi();
let sessionId = "sessionId_example"; // String | The session id.
let command = new JellyfinApi.GeneralCommandType(); // GeneralCommandType | The command to send.
apiInstance.sendGeneralCommand(sessionId, command, (error, data, response) => {
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
 **sessionId** | **String**| The session id. | 
 **command** | [**GeneralCommandType**](.md)| The command to send. | 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## sendMessageCommand

> sendMessageCommand(sessionId, text, opts)

Issues a command to a client to display a message to the user.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.SessionApi();
let sessionId = "sessionId_example"; // String | The session id.
let text = "text_example"; // String | The message test.
let opts = {
  'header': "header_example", // String | The message header.
  'timeoutMs': 789 // Number | The message timeout. If omitted the user will have to confirm viewing the message.
};
apiInstance.sendMessageCommand(sessionId, text, opts, (error, data, response) => {
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
 **sessionId** | **String**| The session id. | 
 **text** | **String**| The message test. | 
 **header** | **String**| The message header. | [optional] 
 **timeoutMs** | **Number**| The message timeout. If omitted the user will have to confirm viewing the message. | [optional] 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## sendPlaystateCommand

> sendPlaystateCommand(sessionId, command, opts)

Issues a playstate command to a client.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.SessionApi();
let sessionId = "sessionId_example"; // String | The session id.
let command = new JellyfinApi.PlaystateCommand(); // PlaystateCommand | The MediaBrowser.Model.Session.PlaystateCommand.
let opts = {
  'seekPositionTicks': 789, // Number | The optional position ticks.
  'controllingUserId': "controllingUserId_example" // String | The optional controlling user id.
};
apiInstance.sendPlaystateCommand(sessionId, command, opts, (error, data, response) => {
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
 **sessionId** | **String**| The session id. | 
 **command** | [**PlaystateCommand**](.md)| The MediaBrowser.Model.Session.PlaystateCommand. | 
 **seekPositionTicks** | **Number**| The optional position ticks. | [optional] 
 **controllingUserId** | **String**| The optional controlling user id. | [optional] 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## sendSystemCommand

> sendSystemCommand(sessionId, command)

Issues a system command to a client.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.SessionApi();
let sessionId = "sessionId_example"; // String | The session id.
let command = new JellyfinApi.GeneralCommandType(); // GeneralCommandType | The command to send.
apiInstance.sendSystemCommand(sessionId, command, (error, data, response) => {
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
 **sessionId** | **String**| The session id. | 
 **command** | [**GeneralCommandType**](.md)| The command to send. | 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

