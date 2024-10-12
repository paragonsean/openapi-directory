# Trello.NotificationApi

All URIs are relative to *https://trello.com/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addNotificationsAllRead**](NotificationApi.md#addNotificationsAllRead) | **POST** /notifications/all/read | addNotificationsAllRead()
[**getNotificationsBoardByIdNotification**](NotificationApi.md#getNotificationsBoardByIdNotification) | **GET** /notifications/{idNotification}/board | getNotificationsBoardByIdNotification()
[**getNotificationsBoardByIdNotificationByField**](NotificationApi.md#getNotificationsBoardByIdNotificationByField) | **GET** /notifications/{idNotification}/board/{field} | getNotificationsBoardByIdNotificationByField()
[**getNotificationsByIdNotification**](NotificationApi.md#getNotificationsByIdNotification) | **GET** /notifications/{idNotification} | getNotificationsByIdNotification()
[**getNotificationsByIdNotificationByField**](NotificationApi.md#getNotificationsByIdNotificationByField) | **GET** /notifications/{idNotification}/{field} | getNotificationsByIdNotificationByField()
[**getNotificationsCardByIdNotification**](NotificationApi.md#getNotificationsCardByIdNotification) | **GET** /notifications/{idNotification}/card | getNotificationsCardByIdNotification()
[**getNotificationsCardByIdNotificationByField**](NotificationApi.md#getNotificationsCardByIdNotificationByField) | **GET** /notifications/{idNotification}/card/{field} | getNotificationsCardByIdNotificationByField()
[**getNotificationsDisplayByIdNotification**](NotificationApi.md#getNotificationsDisplayByIdNotification) | **GET** /notifications/{idNotification}/display | getNotificationsDisplayByIdNotification()
[**getNotificationsEntitiesByIdNotification**](NotificationApi.md#getNotificationsEntitiesByIdNotification) | **GET** /notifications/{idNotification}/entities | getNotificationsEntitiesByIdNotification()
[**getNotificationsListByIdNotification**](NotificationApi.md#getNotificationsListByIdNotification) | **GET** /notifications/{idNotification}/list | getNotificationsListByIdNotification()
[**getNotificationsListByIdNotificationByField**](NotificationApi.md#getNotificationsListByIdNotificationByField) | **GET** /notifications/{idNotification}/list/{field} | getNotificationsListByIdNotificationByField()
[**getNotificationsMemberByIdNotification**](NotificationApi.md#getNotificationsMemberByIdNotification) | **GET** /notifications/{idNotification}/member | getNotificationsMemberByIdNotification()
[**getNotificationsMemberByIdNotificationByField**](NotificationApi.md#getNotificationsMemberByIdNotificationByField) | **GET** /notifications/{idNotification}/member/{field} | getNotificationsMemberByIdNotificationByField()
[**getNotificationsMemberCreatorByIdNotification**](NotificationApi.md#getNotificationsMemberCreatorByIdNotification) | **GET** /notifications/{idNotification}/memberCreator | getNotificationsMemberCreatorByIdNotification()
[**getNotificationsMemberCreatorByIdNotificationByField**](NotificationApi.md#getNotificationsMemberCreatorByIdNotificationByField) | **GET** /notifications/{idNotification}/memberCreator/{field} | getNotificationsMemberCreatorByIdNotificationByField()
[**getNotificationsOrganizationByIdNotification**](NotificationApi.md#getNotificationsOrganizationByIdNotification) | **GET** /notifications/{idNotification}/organization | getNotificationsOrganizationByIdNotification()
[**getNotificationsOrganizationByIdNotificationByField**](NotificationApi.md#getNotificationsOrganizationByIdNotificationByField) | **GET** /notifications/{idNotification}/organization/{field} | getNotificationsOrganizationByIdNotificationByField()
[**updateNotificationsByIdNotification**](NotificationApi.md#updateNotificationsByIdNotification) | **PUT** /notifications/{idNotification} | updateNotificationsByIdNotification()
[**updateNotificationsUnreadByIdNotification**](NotificationApi.md#updateNotificationsUnreadByIdNotification) | **PUT** /notifications/{idNotification}/unread | updateNotificationsUnreadByIdNotification()



## addNotificationsAllRead

> addNotificationsAllRead(key, token)

addNotificationsAllRead()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.NotificationApi();
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.addNotificationsAllRead(key, token, (error, data, response) => {
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
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNotificationsBoardByIdNotification

> getNotificationsBoardByIdNotification(idNotification, key, token, opts)

getNotificationsBoardByIdNotification()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.NotificationApi();
let idNotification = "idNotification_example"; // String | idNotification
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'fields': "'all'" // String | all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url
};
apiInstance.getNotificationsBoardByIdNotification(idNotification, key, token, opts, (error, data, response) => {
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
 **idNotification** | **String**| idNotification | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **fields** | **String**| all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url | [optional] [default to &#39;all&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNotificationsBoardByIdNotificationByField

> getNotificationsBoardByIdNotificationByField(idNotification, field, key, token)

getNotificationsBoardByIdNotificationByField()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.NotificationApi();
let idNotification = "idNotification_example"; // String | idNotification
let field = "field_example"; // String | field
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.getNotificationsBoardByIdNotificationByField(idNotification, field, key, token, (error, data, response) => {
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
 **idNotification** | **String**| idNotification | 
 **field** | **String**| field | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNotificationsByIdNotification

> getNotificationsByIdNotification(idNotification, key, token, opts)

getNotificationsByIdNotification()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.NotificationApi();
let idNotification = "idNotification_example"; // String | idNotification
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'display': "display_example", // String |  true or false
  'entities': "entities_example", // String |  true or false
  'fields': "'all'", // String | all or a comma-separated list of: data, date, idMemberCreator, type or unread
  'memberCreator': "memberCreator_example", // String |  true or false
  'memberCreatorFields': "'avatarHash, fullName, initials and username'", // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
  'board': "board_example", // String |  true or false
  'boardFields': "'name'", // String | all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url
  'list': "list_example", // String |  true or false
  'card': "card_example", // String |  true or false
  'cardFields': "'name'", // String | all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url
  'organization': "organization_example", // String |  true or false
  'organizationFields': "'displayName'", // String | all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website
  'member': "member_example", // String |  true or false
  'memberFields': "'avatarHash, fullName, initials and username'" // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
};
apiInstance.getNotificationsByIdNotification(idNotification, key, token, opts, (error, data, response) => {
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
 **idNotification** | **String**| idNotification | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **display** | **String**|  true or false | [optional] 
 **entities** | **String**|  true or false | [optional] 
 **fields** | **String**| all or a comma-separated list of: data, date, idMemberCreator, type or unread | [optional] [default to &#39;all&#39;]
 **memberCreator** | **String**|  true or false | [optional] 
 **memberCreatorFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to &#39;avatarHash, fullName, initials and username&#39;]
 **board** | **String**|  true or false | [optional] 
 **boardFields** | **String**| all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url | [optional] [default to &#39;name&#39;]
 **list** | **String**|  true or false | [optional] 
 **card** | **String**|  true or false | [optional] 
 **cardFields** | **String**| all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url | [optional] [default to &#39;name&#39;]
 **organization** | **String**|  true or false | [optional] 
 **organizationFields** | **String**| all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website | [optional] [default to &#39;displayName&#39;]
 **member** | **String**|  true or false | [optional] 
 **memberFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to &#39;avatarHash, fullName, initials and username&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNotificationsByIdNotificationByField

> getNotificationsByIdNotificationByField(idNotification, field, key, token)

getNotificationsByIdNotificationByField()

### Example

```javascript
import Trello from 'trello';

let apiInstance = new Trello.NotificationApi();
let idNotification = "idNotification_example"; // String | idNotification
let field = "field_example"; // String | field
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.getNotificationsByIdNotificationByField(idNotification, field, key, token, (error, data, response) => {
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
 **idNotification** | **String**| idNotification | 
 **field** | **String**| field | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNotificationsCardByIdNotification

> getNotificationsCardByIdNotification(idNotification, key, token, opts)

getNotificationsCardByIdNotification()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.NotificationApi();
let idNotification = "idNotification_example"; // String | idNotification
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'fields': "'all'" // String | all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url
};
apiInstance.getNotificationsCardByIdNotification(idNotification, key, token, opts, (error, data, response) => {
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
 **idNotification** | **String**| idNotification | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **fields** | **String**| all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url | [optional] [default to &#39;all&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNotificationsCardByIdNotificationByField

> getNotificationsCardByIdNotificationByField(idNotification, field, key, token)

getNotificationsCardByIdNotificationByField()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.NotificationApi();
let idNotification = "idNotification_example"; // String | idNotification
let field = "field_example"; // String | field
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.getNotificationsCardByIdNotificationByField(idNotification, field, key, token, (error, data, response) => {
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
 **idNotification** | **String**| idNotification | 
 **field** | **String**| field | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNotificationsDisplayByIdNotification

> getNotificationsDisplayByIdNotification(idNotification, key, token)

getNotificationsDisplayByIdNotification()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.NotificationApi();
let idNotification = "idNotification_example"; // String | idNotification
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.getNotificationsDisplayByIdNotification(idNotification, key, token, (error, data, response) => {
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
 **idNotification** | **String**| idNotification | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNotificationsEntitiesByIdNotification

> getNotificationsEntitiesByIdNotification(idNotification, key, token)

getNotificationsEntitiesByIdNotification()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.NotificationApi();
let idNotification = "idNotification_example"; // String | idNotification
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.getNotificationsEntitiesByIdNotification(idNotification, key, token, (error, data, response) => {
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
 **idNotification** | **String**| idNotification | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNotificationsListByIdNotification

> getNotificationsListByIdNotification(idNotification, key, token, opts)

getNotificationsListByIdNotification()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.NotificationApi();
let idNotification = "idNotification_example"; // String | idNotification
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'fields': "'all'" // String | all or a comma-separated list of: closed, idBoard, name, pos or subscribed
};
apiInstance.getNotificationsListByIdNotification(idNotification, key, token, opts, (error, data, response) => {
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
 **idNotification** | **String**| idNotification | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **fields** | **String**| all or a comma-separated list of: closed, idBoard, name, pos or subscribed | [optional] [default to &#39;all&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNotificationsListByIdNotificationByField

> getNotificationsListByIdNotificationByField(idNotification, field, key, token)

getNotificationsListByIdNotificationByField()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.NotificationApi();
let idNotification = "idNotification_example"; // String | idNotification
let field = "field_example"; // String | field
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.getNotificationsListByIdNotificationByField(idNotification, field, key, token, (error, data, response) => {
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
 **idNotification** | **String**| idNotification | 
 **field** | **String**| field | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNotificationsMemberByIdNotification

> getNotificationsMemberByIdNotification(idNotification, key, token, opts)

getNotificationsMemberByIdNotification()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.NotificationApi();
let idNotification = "idNotification_example"; // String | idNotification
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'fields': "'all'" // String | all or a comma-separated list of: avatarHash, avatarSource, bio, bioData, confirmed, email, fullName, gravatarHash, idBoards, idBoardsPinned, idOrganizations, idPremOrgsAdmin, initials, loginTypes, memberType, oneTimeMessagesDismissed, prefs, premiumFeatures, products, status, status, trophies, uploadedAvatarHash, url or username
};
apiInstance.getNotificationsMemberByIdNotification(idNotification, key, token, opts, (error, data, response) => {
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
 **idNotification** | **String**| idNotification | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **fields** | **String**| all or a comma-separated list of: avatarHash, avatarSource, bio, bioData, confirmed, email, fullName, gravatarHash, idBoards, idBoardsPinned, idOrganizations, idPremOrgsAdmin, initials, loginTypes, memberType, oneTimeMessagesDismissed, prefs, premiumFeatures, products, status, status, trophies, uploadedAvatarHash, url or username | [optional] [default to &#39;all&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNotificationsMemberByIdNotificationByField

> getNotificationsMemberByIdNotificationByField(idNotification, field, key, token)

getNotificationsMemberByIdNotificationByField()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.NotificationApi();
let idNotification = "idNotification_example"; // String | idNotification
let field = "field_example"; // String | field
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.getNotificationsMemberByIdNotificationByField(idNotification, field, key, token, (error, data, response) => {
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
 **idNotification** | **String**| idNotification | 
 **field** | **String**| field | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNotificationsMemberCreatorByIdNotification

> getNotificationsMemberCreatorByIdNotification(idNotification, key, token, opts)

getNotificationsMemberCreatorByIdNotification()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.NotificationApi();
let idNotification = "idNotification_example"; // String | idNotification
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'fields': "'all'" // String | all or a comma-separated list of: avatarHash, avatarSource, bio, bioData, confirmed, email, fullName, gravatarHash, idBoards, idBoardsPinned, idOrganizations, idPremOrgsAdmin, initials, loginTypes, memberType, oneTimeMessagesDismissed, prefs, premiumFeatures, products, status, status, trophies, uploadedAvatarHash, url or username
};
apiInstance.getNotificationsMemberCreatorByIdNotification(idNotification, key, token, opts, (error, data, response) => {
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
 **idNotification** | **String**| idNotification | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **fields** | **String**| all or a comma-separated list of: avatarHash, avatarSource, bio, bioData, confirmed, email, fullName, gravatarHash, idBoards, idBoardsPinned, idOrganizations, idPremOrgsAdmin, initials, loginTypes, memberType, oneTimeMessagesDismissed, prefs, premiumFeatures, products, status, status, trophies, uploadedAvatarHash, url or username | [optional] [default to &#39;all&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNotificationsMemberCreatorByIdNotificationByField

> getNotificationsMemberCreatorByIdNotificationByField(idNotification, field, key, token)

getNotificationsMemberCreatorByIdNotificationByField()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.NotificationApi();
let idNotification = "idNotification_example"; // String | idNotification
let field = "field_example"; // String | field
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.getNotificationsMemberCreatorByIdNotificationByField(idNotification, field, key, token, (error, data, response) => {
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
 **idNotification** | **String**| idNotification | 
 **field** | **String**| field | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNotificationsOrganizationByIdNotification

> getNotificationsOrganizationByIdNotification(idNotification, key, token, opts)

getNotificationsOrganizationByIdNotification()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.NotificationApi();
let idNotification = "idNotification_example"; // String | idNotification
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'fields': "'all'" // String | all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website
};
apiInstance.getNotificationsOrganizationByIdNotification(idNotification, key, token, opts, (error, data, response) => {
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
 **idNotification** | **String**| idNotification | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **fields** | **String**| all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website | [optional] [default to &#39;all&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNotificationsOrganizationByIdNotificationByField

> getNotificationsOrganizationByIdNotificationByField(idNotification, field, key, token)

getNotificationsOrganizationByIdNotificationByField()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.NotificationApi();
let idNotification = "idNotification_example"; // String | idNotification
let field = "field_example"; // String | field
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.getNotificationsOrganizationByIdNotificationByField(idNotification, field, key, token, (error, data, response) => {
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
 **idNotification** | **String**| idNotification | 
 **field** | **String**| field | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateNotificationsByIdNotification

> updateNotificationsByIdNotification(idNotification, key, token, notifications)

updateNotificationsByIdNotification()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.NotificationApi();
let idNotification = "idNotification_example"; // String | idNotification
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let notifications = new Trello.Notifications(); // Notifications | Attributes of \"Notifications\" to be updated.
apiInstance.updateNotificationsByIdNotification(idNotification, key, token, notifications, (error, data, response) => {
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
 **idNotification** | **String**| idNotification | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **notifications** | [**Notifications**](Notifications.md)| Attributes of \&quot;Notifications\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateNotificationsUnreadByIdNotification

> updateNotificationsUnreadByIdNotification(idNotification, key, token, notificationsUnread)

updateNotificationsUnreadByIdNotification()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.NotificationApi();
let idNotification = "idNotification_example"; // String | idNotification
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let notificationsUnread = new Trello.NotificationsUnread(); // NotificationsUnread | Attributes of \"Notifications Unread\" to be updated.
apiInstance.updateNotificationsUnreadByIdNotification(idNotification, key, token, notificationsUnread, (error, data, response) => {
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
 **idNotification** | **String**| idNotification | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **notificationsUnread** | [**NotificationsUnread**](NotificationsUnread.md)| Attributes of \&quot;Notifications Unread\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

