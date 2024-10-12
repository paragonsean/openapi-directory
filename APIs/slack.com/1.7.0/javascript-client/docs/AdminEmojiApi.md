# SlackWebApi.AdminEmojiApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adminEmojiAdd**](AdminEmojiApi.md#adminEmojiAdd) | **POST** /admin.emoji.add | 
[**adminEmojiAddAlias**](AdminEmojiApi.md#adminEmojiAddAlias) | **POST** /admin.emoji.addAlias | 
[**adminEmojiList**](AdminEmojiApi.md#adminEmojiList) | **GET** /admin.emoji.list | 
[**adminEmojiRemove**](AdminEmojiApi.md#adminEmojiRemove) | **POST** /admin.emoji.remove | 
[**adminEmojiRename**](AdminEmojiApi.md#adminEmojiRename) | **POST** /admin.emoji.rename | 



## adminEmojiAdd

> DefaultSuccessTemplate adminEmojiAdd(name, token, url)



Add an emoji.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminEmojiApi();
let name = "name_example"; // String | The name of the emoji to be removed. Colons (`:myemoji:`) around the value are not required, although they may be included.
let token = "token_example"; // String | Authentication token. Requires scope: `admin.teams:write`
let url = "url_example"; // String | The URL of a file to use as an image for the emoji. Square images under 128KB and with transparent backgrounds work best.
apiInstance.adminEmojiAdd(name, token, url, (error, data, response) => {
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
 **name** | **String**| The name of the emoji to be removed. Colons (&#x60;:myemoji:&#x60;) around the value are not required, although they may be included. | 
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.teams:write&#x60; | 
 **url** | **String**| The URL of a file to use as an image for the emoji. Square images under 128KB and with transparent backgrounds work best. | 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## adminEmojiAddAlias

> DefaultSuccessTemplate adminEmojiAddAlias(aliasFor, name, token)



Add an emoji alias.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminEmojiApi();
let aliasFor = "aliasFor_example"; // String | The alias of the emoji.
let name = "name_example"; // String | The name of the emoji to be aliased. Colons (`:myemoji:`) around the value are not required, although they may be included.
let token = "token_example"; // String | Authentication token. Requires scope: `admin.teams:write`
apiInstance.adminEmojiAddAlias(aliasFor, name, token, (error, data, response) => {
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
 **aliasFor** | **String**| The alias of the emoji. | 
 **name** | **String**| The name of the emoji to be aliased. Colons (&#x60;:myemoji:&#x60;) around the value are not required, although they may be included. | 
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.teams:write&#x60; | 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## adminEmojiList

> DefaultSuccessTemplate adminEmojiList(token, opts)



List emoji for an Enterprise Grid organization.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminEmojiApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.teams:read`
let opts = {
  'cursor': "cursor_example", // String | Set `cursor` to `next_cursor` returned by the previous call to list items in the next page
  'limit': 56 // Number | The maximum number of items to return. Must be between 1 - 1000 both inclusive.
};
apiInstance.adminEmojiList(token, opts, (error, data, response) => {
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
 **cursor** | **String**| Set &#x60;cursor&#x60; to &#x60;next_cursor&#x60; returned by the previous call to list items in the next page | [optional] 
 **limit** | **Number**| The maximum number of items to return. Must be between 1 - 1000 both inclusive. | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## adminEmojiRemove

> DefaultSuccessTemplate adminEmojiRemove(name, token)



Remove an emoji across an Enterprise Grid organization

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminEmojiApi();
let name = "name_example"; // String | The name of the emoji to be removed. Colons (`:myemoji:`) around the value are not required, although they may be included.
let token = "token_example"; // String | Authentication token. Requires scope: `admin.teams:write`
apiInstance.adminEmojiRemove(name, token, (error, data, response) => {
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
 **name** | **String**| The name of the emoji to be removed. Colons (&#x60;:myemoji:&#x60;) around the value are not required, although they may be included. | 
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.teams:write&#x60; | 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## adminEmojiRename

> DefaultSuccessTemplate adminEmojiRename(name, newName, token)



Rename an emoji.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminEmojiApi();
let name = "name_example"; // String | The name of the emoji to be renamed. Colons (`:myemoji:`) around the value are not required, although they may be included.
let newName = "newName_example"; // String | The new name of the emoji.
let token = "token_example"; // String | Authentication token. Requires scope: `admin.teams:write`
apiInstance.adminEmojiRename(name, newName, token, (error, data, response) => {
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
 **name** | **String**| The name of the emoji to be renamed. Colons (&#x60;:myemoji:&#x60;) around the value are not required, although they may be included. | 
 **newName** | **String**| The new name of the emoji. | 
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.teams:write&#x60; | 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

