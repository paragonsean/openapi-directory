# Trello.ListApi

All URIs are relative to *https://trello.com/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addLists**](ListApi.md#addLists) | **POST** /lists | addLists()
[**addListsArchiveAllCardsByIdList**](ListApi.md#addListsArchiveAllCardsByIdList) | **POST** /lists/{idList}/archiveAllCards | addListsArchiveAllCardsByIdList()
[**addListsCardsByIdList**](ListApi.md#addListsCardsByIdList) | **POST** /lists/{idList}/cards | addListsCardsByIdList()
[**addListsMoveAllCardsByIdList**](ListApi.md#addListsMoveAllCardsByIdList) | **POST** /lists/{idList}/moveAllCards | addListsMoveAllCardsByIdList()
[**getListsActionsByIdList**](ListApi.md#getListsActionsByIdList) | **GET** /lists/{idList}/actions | getListsActionsByIdList()
[**getListsBoardByIdList**](ListApi.md#getListsBoardByIdList) | **GET** /lists/{idList}/board | getListsBoardByIdList()
[**getListsBoardByIdListByField**](ListApi.md#getListsBoardByIdListByField) | **GET** /lists/{idList}/board/{field} | getListsBoardByIdListByField()
[**getListsByIdList**](ListApi.md#getListsByIdList) | **GET** /lists/{idList} | getListsByIdList()
[**getListsByIdListByField**](ListApi.md#getListsByIdListByField) | **GET** /lists/{idList}/{field} | getListsByIdListByField()
[**getListsCardsByIdList**](ListApi.md#getListsCardsByIdList) | **GET** /lists/{idList}/cards | getListsCardsByIdList()
[**getListsCardsByIdListByFilter**](ListApi.md#getListsCardsByIdListByFilter) | **GET** /lists/{idList}/cards/{filter} | getListsCardsByIdListByFilter()
[**updateListsByIdList**](ListApi.md#updateListsByIdList) | **PUT** /lists/{idList} | updateListsByIdList()
[**updateListsClosedByIdList**](ListApi.md#updateListsClosedByIdList) | **PUT** /lists/{idList}/closed | updateListsClosedByIdList()
[**updateListsIdBoardByIdList**](ListApi.md#updateListsIdBoardByIdList) | **PUT** /lists/{idList}/idBoard | updateListsIdBoardByIdList()
[**updateListsNameByIdList**](ListApi.md#updateListsNameByIdList) | **PUT** /lists/{idList}/name | updateListsNameByIdList()
[**updateListsPosByIdList**](ListApi.md#updateListsPosByIdList) | **PUT** /lists/{idList}/pos | updateListsPosByIdList()
[**updateListsSubscribedByIdList**](ListApi.md#updateListsSubscribedByIdList) | **PUT** /lists/{idList}/subscribed | updateListsSubscribedByIdList()



## addLists

> addLists(key, token, lists)

addLists()

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

let apiInstance = new Trello.ListApi();
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let lists = new Trello.Lists(); // Lists | Attributes of \"Lists\" to be added.
apiInstance.addLists(key, token, lists, (error, data, response) => {
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
 **lists** | [**Lists**](Lists.md)| Attributes of \&quot;Lists\&quot; to be added. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## addListsArchiveAllCardsByIdList

> addListsArchiveAllCardsByIdList(idList, key, token)

addListsArchiveAllCardsByIdList()

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

let apiInstance = new Trello.ListApi();
let idList = "idList_example"; // String | idList
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.addListsArchiveAllCardsByIdList(idList, key, token, (error, data, response) => {
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
 **idList** | **String**| idList | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addListsCardsByIdList

> addListsCardsByIdList(idList, key, token, listsCards)

addListsCardsByIdList()

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

let apiInstance = new Trello.ListApi();
let idList = "idList_example"; // String | idList
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let listsCards = new Trello.ListsCards(); // ListsCards | Attributes of \"Lists Cards\" to be added.
apiInstance.addListsCardsByIdList(idList, key, token, listsCards, (error, data, response) => {
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
 **idList** | **String**| idList | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **listsCards** | [**ListsCards**](ListsCards.md)| Attributes of \&quot;Lists Cards\&quot; to be added. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## addListsMoveAllCardsByIdList

> addListsMoveAllCardsByIdList(idList, key, token, listsMoveAllCards)

addListsMoveAllCardsByIdList()

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

let apiInstance = new Trello.ListApi();
let idList = "idList_example"; // String | idList
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let listsMoveAllCards = new Trello.ListsMoveAllCards(); // ListsMoveAllCards | Attributes of \"Lists Move All Cards\" to be added.
apiInstance.addListsMoveAllCardsByIdList(idList, key, token, listsMoveAllCards, (error, data, response) => {
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
 **idList** | **String**| idList | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **listsMoveAllCards** | [**ListsMoveAllCards**](ListsMoveAllCards.md)| Attributes of \&quot;Lists Move All Cards\&quot; to be added. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## getListsActionsByIdList

> getListsActionsByIdList(idList, key, token, opts)

getListsActionsByIdList()

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

let apiInstance = new Trello.ListApi();
let idList = "idList_example"; // String | idList
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'entities': "entities_example", // String |  true or false
  'display': "display_example", // String |  true or false
  'filter': "'all'", // String | all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization
  'fields': "'all'", // String | all or a comma-separated list of: data, date, idMemberCreator or type
  'limit': "'50'", // String | a number from 0 to 1000
  'format': "'list'", // String | One of: count, list or minimal
  'since': "since_example", // String | A date, null or lastView
  'before': "before_example", // String | A date, or null
  'page': "'0'", // String | Page * limit must be less than 1000
  'idModels': "idModels_example", // String | Only return actions related to these model ids
  'member': "member_example", // String |  true or false
  'memberFields': "'avatarHash, fullName, initials and username'", // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
  'memberCreator': "memberCreator_example", // String |  true or false
  'memberCreatorFields': "'avatarHash, fullName, initials and username'" // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
};
apiInstance.getListsActionsByIdList(idList, key, token, opts, (error, data, response) => {
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
 **idList** | **String**| idList | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **entities** | **String**|  true or false | [optional] 
 **display** | **String**|  true or false | [optional] 
 **filter** | **String**| all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization | [optional] [default to &#39;all&#39;]
 **fields** | **String**| all or a comma-separated list of: data, date, idMemberCreator or type | [optional] [default to &#39;all&#39;]
 **limit** | **String**| a number from 0 to 1000 | [optional] [default to &#39;50&#39;]
 **format** | **String**| One of: count, list or minimal | [optional] [default to &#39;list&#39;]
 **since** | **String**| A date, null or lastView | [optional] 
 **before** | **String**| A date, or null | [optional] 
 **page** | **String**| Page * limit must be less than 1000 | [optional] [default to &#39;0&#39;]
 **idModels** | **String**| Only return actions related to these model ids | [optional] 
 **member** | **String**|  true or false | [optional] 
 **memberFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to &#39;avatarHash, fullName, initials and username&#39;]
 **memberCreator** | **String**|  true or false | [optional] 
 **memberCreatorFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to &#39;avatarHash, fullName, initials and username&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getListsBoardByIdList

> getListsBoardByIdList(idList, key, token, opts)

getListsBoardByIdList()

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

let apiInstance = new Trello.ListApi();
let idList = "idList_example"; // String | idList
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'fields': "'all'" // String | all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url
};
apiInstance.getListsBoardByIdList(idList, key, token, opts, (error, data, response) => {
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
 **idList** | **String**| idList | 
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


## getListsBoardByIdListByField

> getListsBoardByIdListByField(idList, field, key, token)

getListsBoardByIdListByField()

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

let apiInstance = new Trello.ListApi();
let idList = "idList_example"; // String | idList
let field = "field_example"; // String | field
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.getListsBoardByIdListByField(idList, field, key, token, (error, data, response) => {
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
 **idList** | **String**| idList | 
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


## getListsByIdList

> getListsByIdList(idList, key, token, opts)

getListsByIdList()

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

let apiInstance = new Trello.ListApi();
let idList = "idList_example"; // String | idList
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'cards': "'none'", // String | One of: all, closed, none or open
  'cardFields': "'all'", // String | all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url
  'board': "board_example", // String |  true or false
  'boardFields': "'name, desc, descData, closed, idOrganization, pinned, url and prefs'", // String | all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url
  'fields': "'name, closed, idBoard and pos'" // String | all or a comma-separated list of: closed, idBoard, name, pos or subscribed
};
apiInstance.getListsByIdList(idList, key, token, opts, (error, data, response) => {
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
 **idList** | **String**| idList | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **cards** | **String**| One of: all, closed, none or open | [optional] [default to &#39;none&#39;]
 **cardFields** | **String**| all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url | [optional] [default to &#39;all&#39;]
 **board** | **String**|  true or false | [optional] 
 **boardFields** | **String**| all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url | [optional] [default to &#39;name, desc, descData, closed, idOrganization, pinned, url and prefs&#39;]
 **fields** | **String**| all or a comma-separated list of: closed, idBoard, name, pos or subscribed | [optional] [default to &#39;name, closed, idBoard and pos&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getListsByIdListByField

> getListsByIdListByField(idList, field, key, token)

getListsByIdListByField()

### Example

```javascript
import Trello from 'trello';

let apiInstance = new Trello.ListApi();
let idList = "idList_example"; // String | idList
let field = "field_example"; // String | field
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.getListsByIdListByField(idList, field, key, token, (error, data, response) => {
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
 **idList** | **String**| idList | 
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


## getListsCardsByIdList

> getListsCardsByIdList(idList, key, token, opts)

getListsCardsByIdList()

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

let apiInstance = new Trello.ListApi();
let idList = "idList_example"; // String | idList
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'actions': "actions_example", // String | all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization
  'attachments': "attachments_example", // String | A boolean value or &quot;cover&quot; for only card cover attachments
  'attachmentFields': "'all'", // String | all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url
  'stickers': "stickers_example", // String |  true or false
  'members': "members_example", // String |  true or false
  'memberFields': "'avatarHash, fullName, initials and username'", // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
  'checkItemStates': "checkItemStates_example", // String |  true or false
  'checklists': "'none'", // String | One of: all or none
  'limit': "limit_example", // String | a number from 1 to 1000
  'since': "since_example", // String | A date, or null
  'before': "before_example", // String | A date, or null
  'filter': "'open'", // String | One of: all, closed, none or open
  'fields': "'all'" // String | all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url
};
apiInstance.getListsCardsByIdList(idList, key, token, opts, (error, data, response) => {
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
 **idList** | **String**| idList | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **actions** | **String**| all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization | [optional] 
 **attachments** | **String**| A boolean value or &amp;quot;cover&amp;quot; for only card cover attachments | [optional] 
 **attachmentFields** | **String**| all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url | [optional] [default to &#39;all&#39;]
 **stickers** | **String**|  true or false | [optional] 
 **members** | **String**|  true or false | [optional] 
 **memberFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to &#39;avatarHash, fullName, initials and username&#39;]
 **checkItemStates** | **String**|  true or false | [optional] 
 **checklists** | **String**| One of: all or none | [optional] [default to &#39;none&#39;]
 **limit** | **String**| a number from 1 to 1000 | [optional] 
 **since** | **String**| A date, or null | [optional] 
 **before** | **String**| A date, or null | [optional] 
 **filter** | **String**| One of: all, closed, none or open | [optional] [default to &#39;open&#39;]
 **fields** | **String**| all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url | [optional] [default to &#39;all&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getListsCardsByIdListByFilter

> getListsCardsByIdListByFilter(idList, filter, key, token)

getListsCardsByIdListByFilter()

### Example

```javascript
import Trello from 'trello';

let apiInstance = new Trello.ListApi();
let idList = "idList_example"; // String | idList
let filter = "filter_example"; // String | filter
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.getListsCardsByIdListByFilter(idList, filter, key, token, (error, data, response) => {
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
 **idList** | **String**| idList | 
 **filter** | **String**| filter | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateListsByIdList

> updateListsByIdList(idList, key, token, lists)

updateListsByIdList()

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

let apiInstance = new Trello.ListApi();
let idList = "idList_example"; // String | idList
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let lists = new Trello.Lists(); // Lists | Attributes of \"Lists\" to be updated.
apiInstance.updateListsByIdList(idList, key, token, lists, (error, data, response) => {
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
 **idList** | **String**| idList | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **lists** | [**Lists**](Lists.md)| Attributes of \&quot;Lists\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateListsClosedByIdList

> updateListsClosedByIdList(idList, key, token, listsClosed)

updateListsClosedByIdList()

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

let apiInstance = new Trello.ListApi();
let idList = "idList_example"; // String | idList
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let listsClosed = new Trello.ListsClosed(); // ListsClosed | Attributes of \"Lists Closed\" to be updated.
apiInstance.updateListsClosedByIdList(idList, key, token, listsClosed, (error, data, response) => {
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
 **idList** | **String**| idList | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **listsClosed** | [**ListsClosed**](ListsClosed.md)| Attributes of \&quot;Lists Closed\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateListsIdBoardByIdList

> updateListsIdBoardByIdList(idList, key, token, listsIdBoard)

updateListsIdBoardByIdList()

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

let apiInstance = new Trello.ListApi();
let idList = "idList_example"; // String | idList
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let listsIdBoard = new Trello.ListsIdBoard(); // ListsIdBoard | Attributes of \"Lists Id Board\" to be updated.
apiInstance.updateListsIdBoardByIdList(idList, key, token, listsIdBoard, (error, data, response) => {
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
 **idList** | **String**| idList | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **listsIdBoard** | [**ListsIdBoard**](ListsIdBoard.md)| Attributes of \&quot;Lists Id Board\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateListsNameByIdList

> updateListsNameByIdList(idList, key, token, listsName)

updateListsNameByIdList()

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

let apiInstance = new Trello.ListApi();
let idList = "idList_example"; // String | idList
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let listsName = new Trello.ListsName(); // ListsName | Attributes of \"Lists Name\" to be updated.
apiInstance.updateListsNameByIdList(idList, key, token, listsName, (error, data, response) => {
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
 **idList** | **String**| idList | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **listsName** | [**ListsName**](ListsName.md)| Attributes of \&quot;Lists Name\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateListsPosByIdList

> updateListsPosByIdList(idList, key, token, listsPos)

updateListsPosByIdList()

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

let apiInstance = new Trello.ListApi();
let idList = "idList_example"; // String | idList
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let listsPos = new Trello.ListsPos(); // ListsPos | Attributes of \"Lists Pos\" to be updated.
apiInstance.updateListsPosByIdList(idList, key, token, listsPos, (error, data, response) => {
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
 **idList** | **String**| idList | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **listsPos** | [**ListsPos**](ListsPos.md)| Attributes of \&quot;Lists Pos\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateListsSubscribedByIdList

> updateListsSubscribedByIdList(idList, key, token, listsSubscribed)

updateListsSubscribedByIdList()

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

let apiInstance = new Trello.ListApi();
let idList = "idList_example"; // String | idList
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let listsSubscribed = new Trello.ListsSubscribed(); // ListsSubscribed | Attributes of \"Lists Subscribed\" to be updated.
apiInstance.updateListsSubscribedByIdList(idList, key, token, listsSubscribed, (error, data, response) => {
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
 **idList** | **String**| idList | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **listsSubscribed** | [**ListsSubscribed**](ListsSubscribed.md)| Attributes of \&quot;Lists Subscribed\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

