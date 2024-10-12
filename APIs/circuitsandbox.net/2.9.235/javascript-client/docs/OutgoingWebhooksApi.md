# RestApiVersion2.OutgoingWebhooksApi

All URIs are relative to *https://circuitsandbox.net/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addPresenceWebHook**](OutgoingWebhooksApi.md#addPresenceWebHook) | **POST** /webhooks/presence | Registers Presence WebHook registration
[**addWebHook**](OutgoingWebhooksApi.md#addWebHook) | **POST** /webhooks | Registers a WebHook
[**getWebHook**](OutgoingWebhooksApi.md#getWebHook) | **GET** /webhooks | Gets a list of webHooks
[**getWebHookById**](OutgoingWebhooksApi.md#getWebHookById) | **GET** /webhooks/{id} | Gets a webHook
[**removeWebHook**](OutgoingWebhooksApi.md#removeWebHook) | **DELETE** /webhooks/{id} | Removes a registered webHook
[**removeWebHooks**](OutgoingWebhooksApi.md#removeWebHooks) | **DELETE** /webhooks | Removes all webHooks
[**updatePresenceWebHook**](OutgoingWebhooksApi.md#updatePresenceWebHook) | **PUT** /webhooks/presence/{id} | Updates a Presence WebHook registration
[**updateWebHook**](OutgoingWebhooksApi.md#updateWebHook) | **PUT** /webhooks/{id} | Updates a WebHook registration



## addPresenceWebHook

> WebHook addPresenceWebHook(url, userIds)

Registers Presence WebHook registration

Registers a webHook that has a presence filter with the given URL and userIds. There is a maximum number of userIds allowed OauthScopes: READ_USER

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.OutgoingWebhooksApi();
let url = "url_example"; // String | WebHook callback URL
let userIds = ["null"]; // [String] | The IDs of the users to subscribe for their presence
apiInstance.addPresenceWebHook(url, userIds, (error, data, response) => {
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
 **url** | **String**| WebHook callback URL | 
 **userIds** | [**[String]**](String.md)| The IDs of the users to subscribe for their presence | 

### Return type

[**WebHook**](WebHook.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## addWebHook

> WebHook addWebHook(filter, url)

Registers a WebHook

Registers the webHook with the given filter and callback URL. OauthScopes: READ_CONVERSATIONS, READ_USER

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.OutgoingWebhooksApi();
let filter = ["null"]; // [String] | A filter for WebHooks that checks for a list of configured events. This filter will use a regular expression to determine if it is interested in the events or not. The event itself is converted into a string of format AREA.EVENT. Examples: CONVERSATION.CREATE / USER.UPDATE
let url = "url_example"; // String | WebHook callback URL
apiInstance.addWebHook(filter, url, (error, data, response) => {
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
 **filter** | [**[String]**](String.md)| A filter for WebHooks that checks for a list of configured events. This filter will use a regular expression to determine if it is interested in the events or not. The event itself is converted into a string of format AREA.EVENT. Examples: CONVERSATION.CREATE / USER.UPDATE | 
 **url** | **String**| WebHook callback URL | 

### Return type

[**WebHook**](WebHook.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## getWebHook

> [WebHook] getWebHook()

Gets a list of webHooks

Gets the list of webHooks registered for this user or API. OauthScopes: READ_CONVERSATIONS, READ_USER

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.OutgoingWebhooksApi();
apiInstance.getWebHook((error, data, response) => {
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

[**[WebHook]**](WebHook.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getWebHookById

> WebHook getWebHookById(id)

Gets a webHook

Gets the registered webHook with the given ID. OauthScopes: READ_CONVERSATIONS, READ_USER

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.OutgoingWebhooksApi();
let id = "id_example"; // String | The unique ID of the webHook to fetch
apiInstance.getWebHookById(id, (error, data, response) => {
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
 **id** | **String**| The unique ID of the webHook to fetch | 

### Return type

[**WebHook**](WebHook.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## removeWebHook

> removeWebHook(id)

Removes a registered webHook

Unregisters the webHook with the given ID. OauthScopes: READ_CONVERSATIONS, READ_USER

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.OutgoingWebhooksApi();
let id = "id_example"; // String | The unique ID of the webHook to remove
apiInstance.removeWebHook(id, (error, data, response) => {
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
 **id** | **String**| The unique ID of the webHook to remove | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## removeWebHooks

> removeWebHooks()

Removes all webHooks

Unregisters all webHooks of the authenticated user OauthScopes: READ_CONVERSATIONS, READ_USER

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.OutgoingWebhooksApi();
apiInstance.removeWebHooks((error, data, response) => {
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

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updatePresenceWebHook

> WebHook updatePresenceWebHook(id, opts)

Updates a Presence WebHook registration

Updates a registration of a webHook that has a presence filter. The update can be performed either on the URL and/or the userIds. The new userIds, if any, will override any existing userIds. OauthScopes: READ_USER

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.OutgoingWebhooksApi();
let id = "id_example"; // String | The unique ID of the webHook to update
let opts = {
  'url': "url_example", // String | WebHook callback URL
  'userIds': ["null"] // [String] | The IDs of the users to subscribe for their presence
};
apiInstance.updatePresenceWebHook(id, opts, (error, data, response) => {
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
 **id** | **String**| The unique ID of the webHook to update | 
 **url** | **String**| WebHook callback URL | [optional] 
 **userIds** | [**[String]**](String.md)| The IDs of the users to subscribe for their presence | [optional] 

### Return type

[**WebHook**](WebHook.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## updateWebHook

> WebHook updateWebHook(id, opts)

Updates a WebHook registration

Updates a webHook registration with the given filter and callback URL. OauthScopes: READ_CONVERSATIONS, READ_USER

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.OutgoingWebhooksApi();
let id = "id_example"; // String | The unique ID of the webHook to update
let opts = {
  'filter': ["null"], // [String] | A filter for WebHooks that checks for a list of configured events. This filter will use a regular expression to determine if it is interested in the events or not. The event itself is converted into a string of format AREA.EVENT. Examples: CONVERSATION.CREATE / USER.UPDATE
  'url': "url_example" // String | WebHook callback URL
};
apiInstance.updateWebHook(id, opts, (error, data, response) => {
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
 **id** | **String**| The unique ID of the webHook to update | 
 **filter** | [**[String]**](String.md)| A filter for WebHooks that checks for a list of configured events. This filter will use a regular expression to determine if it is interested in the events or not. The event itself is converted into a string of format AREA.EVENT. Examples: CONVERSATION.CREATE / USER.UPDATE | [optional] 
 **url** | **String**| WebHook callback URL | [optional] 

### Return type

[**WebHook**](WebHook.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml

