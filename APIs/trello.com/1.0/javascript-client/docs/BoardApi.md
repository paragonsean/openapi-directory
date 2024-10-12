# Trello.BoardApi

All URIs are relative to *https://trello.com/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addBoards**](BoardApi.md#addBoards) | **POST** /boards | addBoards()
[**addBoardsCalendarKeyGenerateByIdBoard**](BoardApi.md#addBoardsCalendarKeyGenerateByIdBoard) | **POST** /boards/{idBoard}/calendarKey/generate | addBoardsCalendarKeyGenerateByIdBoard()
[**addBoardsChecklistsByIdBoard**](BoardApi.md#addBoardsChecklistsByIdBoard) | **POST** /boards/{idBoard}/checklists | addBoardsChecklistsByIdBoard()
[**addBoardsEmailKeyGenerateByIdBoard**](BoardApi.md#addBoardsEmailKeyGenerateByIdBoard) | **POST** /boards/{idBoard}/emailKey/generate | addBoardsEmailKeyGenerateByIdBoard()
[**addBoardsLabelsByIdBoard**](BoardApi.md#addBoardsLabelsByIdBoard) | **POST** /boards/{idBoard}/labels | addBoardsLabelsByIdBoard()
[**addBoardsListsByIdBoard**](BoardApi.md#addBoardsListsByIdBoard) | **POST** /boards/{idBoard}/lists | addBoardsListsByIdBoard()
[**addBoardsMarkAsViewedByIdBoard**](BoardApi.md#addBoardsMarkAsViewedByIdBoard) | **POST** /boards/{idBoard}/markAsViewed | addBoardsMarkAsViewedByIdBoard()
[**addBoardsPowerUpsByIdBoard**](BoardApi.md#addBoardsPowerUpsByIdBoard) | **POST** /boards/{idBoard}/powerUps | addBoardsPowerUpsByIdBoard()
[**deleteBoardsMembersByIdBoardByIdMember**](BoardApi.md#deleteBoardsMembersByIdBoardByIdMember) | **DELETE** /boards/{idBoard}/members/{idMember} | deleteBoardsMembersByIdBoardByIdMember()
[**deleteBoardsPowerUpsByIdBoardByPowerUp**](BoardApi.md#deleteBoardsPowerUpsByIdBoardByPowerUp) | **DELETE** /boards/{idBoard}/powerUps/{powerUp} | deleteBoardsPowerUpsByIdBoardByPowerUp()
[**getBoardsActionsByIdBoard**](BoardApi.md#getBoardsActionsByIdBoard) | **GET** /boards/{idBoard}/actions | getBoardsActionsByIdBoard()
[**getBoardsBoardStarsByIdBoard**](BoardApi.md#getBoardsBoardStarsByIdBoard) | **GET** /boards/{idBoard}/boardStars | getBoardsBoardStarsByIdBoard()
[**getBoardsByIdBoard**](BoardApi.md#getBoardsByIdBoard) | **GET** /boards/{idBoard} | getBoardsByIdBoard()
[**getBoardsByIdBoardByField**](BoardApi.md#getBoardsByIdBoardByField) | **GET** /boards/{idBoard}/{field} | getBoardsByIdBoardByField()
[**getBoardsCardsByIdBoard**](BoardApi.md#getBoardsCardsByIdBoard) | **GET** /boards/{idBoard}/cards | getBoardsCardsByIdBoard()
[**getBoardsCardsByIdBoardByFilter**](BoardApi.md#getBoardsCardsByIdBoardByFilter) | **GET** /boards/{idBoard}/cards/{filter} | getBoardsCardsByIdBoardByFilter()
[**getBoardsCardsByIdBoardByIdCard**](BoardApi.md#getBoardsCardsByIdBoardByIdCard) | **GET** /boards/{idBoard}/cards/{idCard} | getBoardsCardsByIdBoardByIdCard()
[**getBoardsChecklistsByIdBoard**](BoardApi.md#getBoardsChecklistsByIdBoard) | **GET** /boards/{idBoard}/checklists | getBoardsChecklistsByIdBoard()
[**getBoardsDeltasByIdBoard**](BoardApi.md#getBoardsDeltasByIdBoard) | **GET** /boards/{idBoard}/deltas | getBoardsDeltasByIdBoard()
[**getBoardsLabelsByIdBoard**](BoardApi.md#getBoardsLabelsByIdBoard) | **GET** /boards/{idBoard}/labels | getBoardsLabelsByIdBoard()
[**getBoardsLabelsByIdBoardByIdLabel**](BoardApi.md#getBoardsLabelsByIdBoardByIdLabel) | **GET** /boards/{idBoard}/labels/{idLabel} | getBoardsLabelsByIdBoardByIdLabel()
[**getBoardsListsByIdBoard**](BoardApi.md#getBoardsListsByIdBoard) | **GET** /boards/{idBoard}/lists | getBoardsListsByIdBoard()
[**getBoardsListsByIdBoardByFilter**](BoardApi.md#getBoardsListsByIdBoardByFilter) | **GET** /boards/{idBoard}/lists/{filter} | getBoardsListsByIdBoardByFilter()
[**getBoardsMembersByIdBoard**](BoardApi.md#getBoardsMembersByIdBoard) | **GET** /boards/{idBoard}/members | getBoardsMembersByIdBoard()
[**getBoardsMembersByIdBoardByFilter**](BoardApi.md#getBoardsMembersByIdBoardByFilter) | **GET** /boards/{idBoard}/members/{filter} | getBoardsMembersByIdBoardByFilter()
[**getBoardsMembersCardsByIdBoardByIdMember**](BoardApi.md#getBoardsMembersCardsByIdBoardByIdMember) | **GET** /boards/{idBoard}/members/{idMember}/cards | getBoardsMembersCardsByIdBoardByIdMember()
[**getBoardsMembersInvitedByIdBoard**](BoardApi.md#getBoardsMembersInvitedByIdBoard) | **GET** /boards/{idBoard}/membersInvited | getBoardsMembersInvitedByIdBoard()
[**getBoardsMembersInvitedByIdBoardByField**](BoardApi.md#getBoardsMembersInvitedByIdBoardByField) | **GET** /boards/{idBoard}/membersInvited/{field} | getBoardsMembersInvitedByIdBoardByField()
[**getBoardsMembershipsByIdBoard**](BoardApi.md#getBoardsMembershipsByIdBoard) | **GET** /boards/{idBoard}/memberships | getBoardsMembershipsByIdBoard()
[**getBoardsMembershipsByIdBoardByIdMembership**](BoardApi.md#getBoardsMembershipsByIdBoardByIdMembership) | **GET** /boards/{idBoard}/memberships/{idMembership} | getBoardsMembershipsByIdBoardByIdMembership()
[**getBoardsMyPrefsByIdBoard**](BoardApi.md#getBoardsMyPrefsByIdBoard) | **GET** /boards/{idBoard}/myPrefs | getBoardsMyPrefsByIdBoard()
[**getBoardsOrganizationByIdBoard**](BoardApi.md#getBoardsOrganizationByIdBoard) | **GET** /boards/{idBoard}/organization | getBoardsOrganizationByIdBoard()
[**getBoardsOrganizationByIdBoardByField**](BoardApi.md#getBoardsOrganizationByIdBoardByField) | **GET** /boards/{idBoard}/organization/{field} | getBoardsOrganizationByIdBoardByField()
[**updateBoardsByIdBoard**](BoardApi.md#updateBoardsByIdBoard) | **PUT** /boards/{idBoard} | updateBoardsByIdBoard()
[**updateBoardsClosedByIdBoard**](BoardApi.md#updateBoardsClosedByIdBoard) | **PUT** /boards/{idBoard}/closed | updateBoardsClosedByIdBoard()
[**updateBoardsDescByIdBoard**](BoardApi.md#updateBoardsDescByIdBoard) | **PUT** /boards/{idBoard}/desc | updateBoardsDescByIdBoard()
[**updateBoardsIdOrganizationByIdBoard**](BoardApi.md#updateBoardsIdOrganizationByIdBoard) | **PUT** /boards/{idBoard}/idOrganization | updateBoardsIdOrganizationByIdBoard()
[**updateBoardsLabelNamesBlueByIdBoard**](BoardApi.md#updateBoardsLabelNamesBlueByIdBoard) | **PUT** /boards/{idBoard}/labelNames/blue | updateBoardsLabelNamesBlueByIdBoard()
[**updateBoardsLabelNamesGreenByIdBoard**](BoardApi.md#updateBoardsLabelNamesGreenByIdBoard) | **PUT** /boards/{idBoard}/labelNames/green | updateBoardsLabelNamesGreenByIdBoard()
[**updateBoardsLabelNamesOrangeByIdBoard**](BoardApi.md#updateBoardsLabelNamesOrangeByIdBoard) | **PUT** /boards/{idBoard}/labelNames/orange | updateBoardsLabelNamesOrangeByIdBoard()
[**updateBoardsLabelNamesPurpleByIdBoard**](BoardApi.md#updateBoardsLabelNamesPurpleByIdBoard) | **PUT** /boards/{idBoard}/labelNames/purple | updateBoardsLabelNamesPurpleByIdBoard()
[**updateBoardsLabelNamesRedByIdBoard**](BoardApi.md#updateBoardsLabelNamesRedByIdBoard) | **PUT** /boards/{idBoard}/labelNames/red | updateBoardsLabelNamesRedByIdBoard()
[**updateBoardsLabelNamesYellowByIdBoard**](BoardApi.md#updateBoardsLabelNamesYellowByIdBoard) | **PUT** /boards/{idBoard}/labelNames/yellow | updateBoardsLabelNamesYellowByIdBoard()
[**updateBoardsMembersByIdBoard**](BoardApi.md#updateBoardsMembersByIdBoard) | **PUT** /boards/{idBoard}/members | updateBoardsMembersByIdBoard()
[**updateBoardsMembersByIdBoardByIdMember**](BoardApi.md#updateBoardsMembersByIdBoardByIdMember) | **PUT** /boards/{idBoard}/members/{idMember} | updateBoardsMembersByIdBoardByIdMember()
[**updateBoardsMembershipsByIdBoardByIdMembership**](BoardApi.md#updateBoardsMembershipsByIdBoardByIdMembership) | **PUT** /boards/{idBoard}/memberships/{idMembership} | updateBoardsMembershipsByIdBoardByIdMembership()
[**updateBoardsMyPrefsEmailPositionByIdBoard**](BoardApi.md#updateBoardsMyPrefsEmailPositionByIdBoard) | **PUT** /boards/{idBoard}/myPrefs/emailPosition | updateBoardsMyPrefsEmailPositionByIdBoard()
[**updateBoardsMyPrefsIdEmailListByIdBoard**](BoardApi.md#updateBoardsMyPrefsIdEmailListByIdBoard) | **PUT** /boards/{idBoard}/myPrefs/idEmailList | updateBoardsMyPrefsIdEmailListByIdBoard()
[**updateBoardsMyPrefsShowListGuideByIdBoard**](BoardApi.md#updateBoardsMyPrefsShowListGuideByIdBoard) | **PUT** /boards/{idBoard}/myPrefs/showListGuide | updateBoardsMyPrefsShowListGuideByIdBoard()
[**updateBoardsMyPrefsShowSidebarActivityByIdBoard**](BoardApi.md#updateBoardsMyPrefsShowSidebarActivityByIdBoard) | **PUT** /boards/{idBoard}/myPrefs/showSidebarActivity | updateBoardsMyPrefsShowSidebarActivityByIdBoard()
[**updateBoardsMyPrefsShowSidebarBoardActionsByIdBoard**](BoardApi.md#updateBoardsMyPrefsShowSidebarBoardActionsByIdBoard) | **PUT** /boards/{idBoard}/myPrefs/showSidebarBoardActions | updateBoardsMyPrefsShowSidebarBoardActionsByIdBoard()
[**updateBoardsMyPrefsShowSidebarByIdBoard**](BoardApi.md#updateBoardsMyPrefsShowSidebarByIdBoard) | **PUT** /boards/{idBoard}/myPrefs/showSidebar | updateBoardsMyPrefsShowSidebarByIdBoard()
[**updateBoardsMyPrefsShowSidebarMembersByIdBoard**](BoardApi.md#updateBoardsMyPrefsShowSidebarMembersByIdBoard) | **PUT** /boards/{idBoard}/myPrefs/showSidebarMembers | updateBoardsMyPrefsShowSidebarMembersByIdBoard()
[**updateBoardsNameByIdBoard**](BoardApi.md#updateBoardsNameByIdBoard) | **PUT** /boards/{idBoard}/name | updateBoardsNameByIdBoard()
[**updateBoardsPrefsBackgroundByIdBoard**](BoardApi.md#updateBoardsPrefsBackgroundByIdBoard) | **PUT** /boards/{idBoard}/prefs/background | updateBoardsPrefsBackgroundByIdBoard()
[**updateBoardsPrefsCalendarFeedEnabledByIdBoard**](BoardApi.md#updateBoardsPrefsCalendarFeedEnabledByIdBoard) | **PUT** /boards/{idBoard}/prefs/calendarFeedEnabled | updateBoardsPrefsCalendarFeedEnabledByIdBoard()
[**updateBoardsPrefsCardAgingByIdBoard**](BoardApi.md#updateBoardsPrefsCardAgingByIdBoard) | **PUT** /boards/{idBoard}/prefs/cardAging | updateBoardsPrefsCardAgingByIdBoard()
[**updateBoardsPrefsCardCoversByIdBoard**](BoardApi.md#updateBoardsPrefsCardCoversByIdBoard) | **PUT** /boards/{idBoard}/prefs/cardCovers | updateBoardsPrefsCardCoversByIdBoard()
[**updateBoardsPrefsCommentsByIdBoard**](BoardApi.md#updateBoardsPrefsCommentsByIdBoard) | **PUT** /boards/{idBoard}/prefs/comments | updateBoardsPrefsCommentsByIdBoard()
[**updateBoardsPrefsInvitationsByIdBoard**](BoardApi.md#updateBoardsPrefsInvitationsByIdBoard) | **PUT** /boards/{idBoard}/prefs/invitations | updateBoardsPrefsInvitationsByIdBoard()
[**updateBoardsPrefsPermissionLevelByIdBoard**](BoardApi.md#updateBoardsPrefsPermissionLevelByIdBoard) | **PUT** /boards/{idBoard}/prefs/permissionLevel | updateBoardsPrefsPermissionLevelByIdBoard()
[**updateBoardsPrefsSelfJoinByIdBoard**](BoardApi.md#updateBoardsPrefsSelfJoinByIdBoard) | **PUT** /boards/{idBoard}/prefs/selfJoin | updateBoardsPrefsSelfJoinByIdBoard()
[**updateBoardsPrefsVotingByIdBoard**](BoardApi.md#updateBoardsPrefsVotingByIdBoard) | **PUT** /boards/{idBoard}/prefs/voting | updateBoardsPrefsVotingByIdBoard()
[**updateBoardsSubscribedByIdBoard**](BoardApi.md#updateBoardsSubscribedByIdBoard) | **PUT** /boards/{idBoard}/subscribed | updateBoardsSubscribedByIdBoard()



## addBoards

> addBoards(key, token, boards)

addBoards()

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

let apiInstance = new Trello.BoardApi();
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let boards = new Trello.Boards(); // Boards | Attributes of \"Boards\" to be added.
apiInstance.addBoards(key, token, boards, (error, data, response) => {
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
 **boards** | [**Boards**](Boards.md)| Attributes of \&quot;Boards\&quot; to be added. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## addBoardsCalendarKeyGenerateByIdBoard

> addBoardsCalendarKeyGenerateByIdBoard(idBoard, key, token)

addBoardsCalendarKeyGenerateByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.addBoardsCalendarKeyGenerateByIdBoard(idBoard, key, token, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addBoardsChecklistsByIdBoard

> addBoardsChecklistsByIdBoard(idBoard, key, token, boardsChecklists)

addBoardsChecklistsByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let boardsChecklists = new Trello.BoardsChecklists(); // BoardsChecklists | Attributes of \"Boards Checklists\" to be added.
apiInstance.addBoardsChecklistsByIdBoard(idBoard, key, token, boardsChecklists, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **boardsChecklists** | [**BoardsChecklists**](BoardsChecklists.md)| Attributes of \&quot;Boards Checklists\&quot; to be added. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## addBoardsEmailKeyGenerateByIdBoard

> addBoardsEmailKeyGenerateByIdBoard(idBoard, key, token)

addBoardsEmailKeyGenerateByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.addBoardsEmailKeyGenerateByIdBoard(idBoard, key, token, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addBoardsLabelsByIdBoard

> addBoardsLabelsByIdBoard(idBoard, key, token, boardsLabels)

addBoardsLabelsByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let boardsLabels = new Trello.BoardsLabels(); // BoardsLabels | Attributes of \"Boards Labels\" to be added.
apiInstance.addBoardsLabelsByIdBoard(idBoard, key, token, boardsLabels, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **boardsLabels** | [**BoardsLabels**](BoardsLabels.md)| Attributes of \&quot;Boards Labels\&quot; to be added. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## addBoardsListsByIdBoard

> addBoardsListsByIdBoard(idBoard, key, token, boardsLists)

addBoardsListsByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let boardsLists = new Trello.BoardsLists(); // BoardsLists | Attributes of \"Boards Lists\" to be added.
apiInstance.addBoardsListsByIdBoard(idBoard, key, token, boardsLists, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **boardsLists** | [**BoardsLists**](BoardsLists.md)| Attributes of \&quot;Boards Lists\&quot; to be added. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## addBoardsMarkAsViewedByIdBoard

> addBoardsMarkAsViewedByIdBoard(idBoard, key, token)

addBoardsMarkAsViewedByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.addBoardsMarkAsViewedByIdBoard(idBoard, key, token, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addBoardsPowerUpsByIdBoard

> addBoardsPowerUpsByIdBoard(idBoard, key, token, boardsPowerUps)

addBoardsPowerUpsByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let boardsPowerUps = new Trello.BoardsPowerUps(); // BoardsPowerUps | Attributes of \"Boards Power Ups\" to be added.
apiInstance.addBoardsPowerUpsByIdBoard(idBoard, key, token, boardsPowerUps, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **boardsPowerUps** | [**BoardsPowerUps**](BoardsPowerUps.md)| Attributes of \&quot;Boards Power Ups\&quot; to be added. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## deleteBoardsMembersByIdBoardByIdMember

> deleteBoardsMembersByIdBoardByIdMember(idBoard, idMember, key, token)

deleteBoardsMembersByIdBoardByIdMember()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let idMember = "idMember_example"; // String | idMember
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.deleteBoardsMembersByIdBoardByIdMember(idBoard, idMember, key, token, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **idMember** | **String**| idMember | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteBoardsPowerUpsByIdBoardByPowerUp

> deleteBoardsPowerUpsByIdBoardByPowerUp(idBoard, powerUp, key, token)

deleteBoardsPowerUpsByIdBoardByPowerUp()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let powerUp = "powerUp_example"; // String | powerUp
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.deleteBoardsPowerUpsByIdBoardByPowerUp(idBoard, powerUp, key, token, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **powerUp** | **String**| powerUp | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getBoardsActionsByIdBoard

> getBoardsActionsByIdBoard(idBoard, key, token, opts)

getBoardsActionsByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
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
apiInstance.getBoardsActionsByIdBoard(idBoard, key, token, opts, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
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


## getBoardsBoardStarsByIdBoard

> getBoardsBoardStarsByIdBoard(idBoard, key, token, opts)

getBoardsBoardStarsByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'filter': "'mine'" // String | One of: mine or none
};
apiInstance.getBoardsBoardStarsByIdBoard(idBoard, key, token, opts, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **filter** | **String**| One of: mine or none | [optional] [default to &#39;mine&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getBoardsByIdBoard

> getBoardsByIdBoard(idBoard, key, token, opts)

getBoardsByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'actions': "actions_example", // String | all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization
  'actionsEntities': "actionsEntities_example", // String |  true or false
  'actionsDisplay': "actionsDisplay_example", // String |  true or false
  'actionsFormat': "'list'", // String | One of: count, list or minimal
  'actionsSince': "actionsSince_example", // String | A date, null or lastView
  'actionsLimit': "'50'", // String | a number from 0 to 1000
  'actionFields': "'all'", // String | all or a comma-separated list of: data, date, idMemberCreator or type
  'actionMember': "actionMember_example", // String |  true or false
  'actionMemberFields': "'avatarHash, fullName, initials and username'", // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
  'actionMemberCreator': "actionMemberCreator_example", // String |  true or false
  'actionMemberCreatorFields': "'avatarHash, fullName, initials and username'", // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
  'cards': "'none'", // String | One of: all, closed, none, open or visible
  'cardFields': "'all'", // String | all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url
  'cardAttachments': "cardAttachments_example", // String | A boolean value or &quot;cover&quot; for only card cover attachments
  'cardAttachmentFields': "'all'", // String | all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url
  'cardChecklists': "'none'", // String | One of: all or none
  'cardStickers': "cardStickers_example", // String |  true or false
  'boardStars': "'none'", // String | One of: mine or none
  'labels': "'none'", // String | One of: all or none
  'labelFields': "'all'", // String | all or a comma-separated list of: color, idBoard, name or uses
  'labelsLimit': "'50'", // String | a number from 0 to 1000
  'lists': "'none'", // String | One of: all, closed, none or open
  'listFields': "'all'", // String | all or a comma-separated list of: closed, idBoard, name, pos or subscribed
  'memberships': "'none'", // String | all or a comma-separated list of: active, admin, deactivated, me or normal
  'membershipsMember': "membershipsMember_example", // String |  true or false
  'membershipsMemberFields': "'fullName and username'", // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
  'members': "'none'", // String | One of: admins, all, none, normal or owners
  'memberFields': "'avatarHash, initials, fullName, username and confirmed'", // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
  'membersInvited': "'none'", // String | One of: admins, all, none, normal or owners
  'membersInvitedFields': "'avatarHash, initials, fullName and username'", // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
  'checklists': "'none'", // String | One of: all or none
  'checklistFields': "'all'", // String | all or a comma-separated list of: idBoard, idCard, name or pos
  'organization': "organization_example", // String |  true or false
  'organizationFields': "'name and displayName'", // String | all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website
  'organizationMemberships': "'none'", // String | all or a comma-separated list of: active, admin, deactivated, me or normal
  'myPrefs': "myPrefs_example", // String |  true or false
  'fields': "'name, desc, descData, closed, idOrganization, pinned, url, shortUrl, prefs and labelNames'" // String | all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url
};
apiInstance.getBoardsByIdBoard(idBoard, key, token, opts, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **actions** | **String**| all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization | [optional] 
 **actionsEntities** | **String**|  true or false | [optional] 
 **actionsDisplay** | **String**|  true or false | [optional] 
 **actionsFormat** | **String**| One of: count, list or minimal | [optional] [default to &#39;list&#39;]
 **actionsSince** | **String**| A date, null or lastView | [optional] 
 **actionsLimit** | **String**| a number from 0 to 1000 | [optional] [default to &#39;50&#39;]
 **actionFields** | **String**| all or a comma-separated list of: data, date, idMemberCreator or type | [optional] [default to &#39;all&#39;]
 **actionMember** | **String**|  true or false | [optional] 
 **actionMemberFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to &#39;avatarHash, fullName, initials and username&#39;]
 **actionMemberCreator** | **String**|  true or false | [optional] 
 **actionMemberCreatorFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to &#39;avatarHash, fullName, initials and username&#39;]
 **cards** | **String**| One of: all, closed, none, open or visible | [optional] [default to &#39;none&#39;]
 **cardFields** | **String**| all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url | [optional] [default to &#39;all&#39;]
 **cardAttachments** | **String**| A boolean value or &amp;quot;cover&amp;quot; for only card cover attachments | [optional] 
 **cardAttachmentFields** | **String**| all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url | [optional] [default to &#39;all&#39;]
 **cardChecklists** | **String**| One of: all or none | [optional] [default to &#39;none&#39;]
 **cardStickers** | **String**|  true or false | [optional] 
 **boardStars** | **String**| One of: mine or none | [optional] [default to &#39;none&#39;]
 **labels** | **String**| One of: all or none | [optional] [default to &#39;none&#39;]
 **labelFields** | **String**| all or a comma-separated list of: color, idBoard, name or uses | [optional] [default to &#39;all&#39;]
 **labelsLimit** | **String**| a number from 0 to 1000 | [optional] [default to &#39;50&#39;]
 **lists** | **String**| One of: all, closed, none or open | [optional] [default to &#39;none&#39;]
 **listFields** | **String**| all or a comma-separated list of: closed, idBoard, name, pos or subscribed | [optional] [default to &#39;all&#39;]
 **memberships** | **String**| all or a comma-separated list of: active, admin, deactivated, me or normal | [optional] [default to &#39;none&#39;]
 **membershipsMember** | **String**|  true or false | [optional] 
 **membershipsMemberFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to &#39;fullName and username&#39;]
 **members** | **String**| One of: admins, all, none, normal or owners | [optional] [default to &#39;none&#39;]
 **memberFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to &#39;avatarHash, initials, fullName, username and confirmed&#39;]
 **membersInvited** | **String**| One of: admins, all, none, normal or owners | [optional] [default to &#39;none&#39;]
 **membersInvitedFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to &#39;avatarHash, initials, fullName and username&#39;]
 **checklists** | **String**| One of: all or none | [optional] [default to &#39;none&#39;]
 **checklistFields** | **String**| all or a comma-separated list of: idBoard, idCard, name or pos | [optional] [default to &#39;all&#39;]
 **organization** | **String**|  true or false | [optional] 
 **organizationFields** | **String**| all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website | [optional] [default to &#39;name and displayName&#39;]
 **organizationMemberships** | **String**| all or a comma-separated list of: active, admin, deactivated, me or normal | [optional] [default to &#39;none&#39;]
 **myPrefs** | **String**|  true or false | [optional] 
 **fields** | **String**| all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url | [optional] [default to &#39;name, desc, descData, closed, idOrganization, pinned, url, shortUrl, prefs and labelNames&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getBoardsByIdBoardByField

> getBoardsByIdBoardByField(idBoard, field, key, token)

getBoardsByIdBoardByField()

### Example

```javascript
import Trello from 'trello';

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let field = "field_example"; // String | field
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.getBoardsByIdBoardByField(idBoard, field, key, token, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
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


## getBoardsCardsByIdBoard

> getBoardsCardsByIdBoard(idBoard, key, token, opts)

getBoardsCardsByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
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
  'filter': "'visible'", // String | One of: all, closed, none, open or visible
  'fields': "'all'" // String | all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url
};
apiInstance.getBoardsCardsByIdBoard(idBoard, key, token, opts, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
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
 **filter** | **String**| One of: all, closed, none, open or visible | [optional] [default to &#39;visible&#39;]
 **fields** | **String**| all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url | [optional] [default to &#39;all&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getBoardsCardsByIdBoardByFilter

> getBoardsCardsByIdBoardByFilter(idBoard, filter, key, token)

getBoardsCardsByIdBoardByFilter()

### Example

```javascript
import Trello from 'trello';

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let filter = "filter_example"; // String | filter
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.getBoardsCardsByIdBoardByFilter(idBoard, filter, key, token, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
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


## getBoardsCardsByIdBoardByIdCard

> getBoardsCardsByIdBoardByIdCard(idBoard, idCard, key, token, opts)

getBoardsCardsByIdBoardByIdCard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let idCard = "idCard_example"; // String | idCard
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'attachments': "attachments_example", // String | A boolean value or &quot;cover&quot; for only card cover attachments
  'attachmentFields': "'all'", // String | all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url
  'actions': "actions_example", // String | all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization
  'actionsEntities': "actionsEntities_example", // String |  true or false
  'actionsDisplay': "actionsDisplay_example", // String |  true or false
  'actionsLimit': "'50'", // String | a number from 0 to 1000
  'actionFields': "'all'", // String | all or a comma-separated list of: data, date, idMemberCreator or type
  'actionMemberCreatorFields': "'avatarHash, fullName, initials and username'", // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
  'members': "members_example", // String |  true or false
  'memberFields': "'avatarHash, initials, fullName and username'", // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
  'checkItemStates': "checkItemStates_example", // String |  true or false
  'checkItemStateFields': "'all'", // String | all or a comma-separated list of: idCheckItem or state
  'labels': "labels_example", // String |  true or false
  'checklists': "'none'", // String | One of: all or none
  'checklistFields': "'all'", // String | all or a comma-separated list of: idBoard, idCard, name or pos
  'fields': "'all'" // String | all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url
};
apiInstance.getBoardsCardsByIdBoardByIdCard(idBoard, idCard, key, token, opts, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **idCard** | **String**| idCard | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **attachments** | **String**| A boolean value or &amp;quot;cover&amp;quot; for only card cover attachments | [optional] 
 **attachmentFields** | **String**| all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url | [optional] [default to &#39;all&#39;]
 **actions** | **String**| all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization | [optional] 
 **actionsEntities** | **String**|  true or false | [optional] 
 **actionsDisplay** | **String**|  true or false | [optional] 
 **actionsLimit** | **String**| a number from 0 to 1000 | [optional] [default to &#39;50&#39;]
 **actionFields** | **String**| all or a comma-separated list of: data, date, idMemberCreator or type | [optional] [default to &#39;all&#39;]
 **actionMemberCreatorFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to &#39;avatarHash, fullName, initials and username&#39;]
 **members** | **String**|  true or false | [optional] 
 **memberFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to &#39;avatarHash, initials, fullName and username&#39;]
 **checkItemStates** | **String**|  true or false | [optional] 
 **checkItemStateFields** | **String**| all or a comma-separated list of: idCheckItem or state | [optional] [default to &#39;all&#39;]
 **labels** | **String**|  true or false | [optional] 
 **checklists** | **String**| One of: all or none | [optional] [default to &#39;none&#39;]
 **checklistFields** | **String**| all or a comma-separated list of: idBoard, idCard, name or pos | [optional] [default to &#39;all&#39;]
 **fields** | **String**| all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url | [optional] [default to &#39;all&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getBoardsChecklistsByIdBoard

> getBoardsChecklistsByIdBoard(idBoard, key, token, opts)

getBoardsChecklistsByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'cards': "'none'", // String | One of: all, closed, none, open or visible
  'cardFields': "'all'", // String | all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url
  'checkItems': "'all'", // String | One of: all or none
  'checkItemFields': "'name, nameData, pos and state'", // String | all or a comma-separated list of: name, nameData, pos, state or type
  'filter': "'all'", // String | One of: all or none
  'fields': "'all'" // String | all or a comma-separated list of: idBoard, idCard, name or pos
};
apiInstance.getBoardsChecklistsByIdBoard(idBoard, key, token, opts, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **cards** | **String**| One of: all, closed, none, open or visible | [optional] [default to &#39;none&#39;]
 **cardFields** | **String**| all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url | [optional] [default to &#39;all&#39;]
 **checkItems** | **String**| One of: all or none | [optional] [default to &#39;all&#39;]
 **checkItemFields** | **String**| all or a comma-separated list of: name, nameData, pos, state or type | [optional] [default to &#39;name, nameData, pos and state&#39;]
 **filter** | **String**| One of: all or none | [optional] [default to &#39;all&#39;]
 **fields** | **String**| all or a comma-separated list of: idBoard, idCard, name or pos | [optional] [default to &#39;all&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getBoardsDeltasByIdBoard

> getBoardsDeltasByIdBoard(idBoard, tags, ixLastUpdate, key, token)

getBoardsDeltasByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let tags = "tags_example"; // String | A valid tag for subscribing
let ixLastUpdate = "ixLastUpdate_example"; // String | a number from -1 to Infinity
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.getBoardsDeltasByIdBoard(idBoard, tags, ixLastUpdate, key, token, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **tags** | **String**| A valid tag for subscribing | 
 **ixLastUpdate** | **String**| a number from -1 to Infinity | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getBoardsLabelsByIdBoard

> getBoardsLabelsByIdBoard(idBoard, key, token, opts)

getBoardsLabelsByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'fields': "'all'", // String | all or a comma-separated list of: color, idBoard, name or uses
  'limit': "'50'" // String | a number from 0 to 1000
};
apiInstance.getBoardsLabelsByIdBoard(idBoard, key, token, opts, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **fields** | **String**| all or a comma-separated list of: color, idBoard, name or uses | [optional] [default to &#39;all&#39;]
 **limit** | **String**| a number from 0 to 1000 | [optional] [default to &#39;50&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getBoardsLabelsByIdBoardByIdLabel

> getBoardsLabelsByIdBoardByIdLabel(idBoard, idLabel, key, token, opts)

getBoardsLabelsByIdBoardByIdLabel()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let idLabel = "idLabel_example"; // String | idLabel
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'fields': "'all'" // String | all or a comma-separated list of: color, idBoard, name or uses
};
apiInstance.getBoardsLabelsByIdBoardByIdLabel(idBoard, idLabel, key, token, opts, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **idLabel** | **String**| idLabel | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **fields** | **String**| all or a comma-separated list of: color, idBoard, name or uses | [optional] [default to &#39;all&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getBoardsListsByIdBoard

> getBoardsListsByIdBoard(idBoard, key, token, opts)

getBoardsListsByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'cards': "'none'", // String | One of: all, closed, none, open or visible
  'cardFields': "'all'", // String | all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url
  'filter': "'open'", // String | One of: all, closed, none or open
  'fields': "'all'" // String | all or a comma-separated list of: closed, idBoard, name, pos or subscribed
};
apiInstance.getBoardsListsByIdBoard(idBoard, key, token, opts, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **cards** | **String**| One of: all, closed, none, open or visible | [optional] [default to &#39;none&#39;]
 **cardFields** | **String**| all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url | [optional] [default to &#39;all&#39;]
 **filter** | **String**| One of: all, closed, none or open | [optional] [default to &#39;open&#39;]
 **fields** | **String**| all or a comma-separated list of: closed, idBoard, name, pos or subscribed | [optional] [default to &#39;all&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getBoardsListsByIdBoardByFilter

> getBoardsListsByIdBoardByFilter(idBoard, filter, key, token)

getBoardsListsByIdBoardByFilter()

### Example

```javascript
import Trello from 'trello';

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let filter = "filter_example"; // String | filter
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.getBoardsListsByIdBoardByFilter(idBoard, filter, key, token, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
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


## getBoardsMembersByIdBoard

> getBoardsMembersByIdBoard(idBoard, key, token, opts)

getBoardsMembersByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'filter': "'all'", // String | One of: admins, all, none, normal or owners
  'fields': "'fullName and username'", // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
  'activity': "activity_example" // String | true or false ; works for premium organizations only.
};
apiInstance.getBoardsMembersByIdBoard(idBoard, key, token, opts, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **filter** | **String**| One of: admins, all, none, normal or owners | [optional] [default to &#39;all&#39;]
 **fields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to &#39;fullName and username&#39;]
 **activity** | **String**| true or false ; works for premium organizations only. | [optional] 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getBoardsMembersByIdBoardByFilter

> getBoardsMembersByIdBoardByFilter(idBoard, filter, key, token)

getBoardsMembersByIdBoardByFilter()

### Example

```javascript
import Trello from 'trello';

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let filter = "filter_example"; // String | filter
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.getBoardsMembersByIdBoardByFilter(idBoard, filter, key, token, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
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


## getBoardsMembersCardsByIdBoardByIdMember

> getBoardsMembersCardsByIdBoardByIdMember(idBoard, idMember, key, token, opts)

getBoardsMembersCardsByIdBoardByIdMember()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let idMember = "idMember_example"; // String | idMember
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'actions': "actions_example", // String | all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization
  'attachments': "attachments_example", // String | A boolean value or &quot;cover&quot; for only card cover attachments
  'attachmentFields': "'all'", // String | all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url
  'members': "members_example", // String |  true or false
  'memberFields': "'avatarHash, fullName, initials and username'", // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
  'checkItemStates': "checkItemStates_example", // String |  true or false
  'checklists': "'none'", // String | One of: all or none
  'board': "board_example", // String |  true or false
  'boardFields': "'name, desc, closed, idOrganization, pinned, url and prefs'", // String | all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url
  'list': "list_example", // String |  true or false
  'listFields': "'all'", // String | all or a comma-separated list of: closed, idBoard, name, pos or subscribed
  'filter': "'visible'", // String | One of: all, closed, none, open or visible
  'fields': "'all'" // String | all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url
};
apiInstance.getBoardsMembersCardsByIdBoardByIdMember(idBoard, idMember, key, token, opts, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **idMember** | **String**| idMember | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **actions** | **String**| all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization | [optional] 
 **attachments** | **String**| A boolean value or &amp;quot;cover&amp;quot; for only card cover attachments | [optional] 
 **attachmentFields** | **String**| all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url | [optional] [default to &#39;all&#39;]
 **members** | **String**|  true or false | [optional] 
 **memberFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to &#39;avatarHash, fullName, initials and username&#39;]
 **checkItemStates** | **String**|  true or false | [optional] 
 **checklists** | **String**| One of: all or none | [optional] [default to &#39;none&#39;]
 **board** | **String**|  true or false | [optional] 
 **boardFields** | **String**| all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url | [optional] [default to &#39;name, desc, closed, idOrganization, pinned, url and prefs&#39;]
 **list** | **String**|  true or false | [optional] 
 **listFields** | **String**| all or a comma-separated list of: closed, idBoard, name, pos or subscribed | [optional] [default to &#39;all&#39;]
 **filter** | **String**| One of: all, closed, none, open or visible | [optional] [default to &#39;visible&#39;]
 **fields** | **String**| all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url | [optional] [default to &#39;all&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getBoardsMembersInvitedByIdBoard

> getBoardsMembersInvitedByIdBoard(idBoard, key, token, opts)

getBoardsMembersInvitedByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'fields': "'all'" // String | all or a comma-separated list of: avatarHash, avatarSource, bio, bioData, confirmed, email, fullName, gravatarHash, idBoards, idBoardsPinned, idOrganizations, idPremOrgsAdmin, initials, loginTypes, memberType, oneTimeMessagesDismissed, prefs, premiumFeatures, products, status, status, trophies, uploadedAvatarHash, url or username
};
apiInstance.getBoardsMembersInvitedByIdBoard(idBoard, key, token, opts, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
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


## getBoardsMembersInvitedByIdBoardByField

> getBoardsMembersInvitedByIdBoardByField(idBoard, field, key, token)

getBoardsMembersInvitedByIdBoardByField()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let field = "field_example"; // String | field
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.getBoardsMembersInvitedByIdBoardByField(idBoard, field, key, token, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
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


## getBoardsMembershipsByIdBoard

> getBoardsMembershipsByIdBoard(idBoard, key, token, opts)

getBoardsMembershipsByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'filter': "'all'", // String | all or a comma-separated list of: active, admin, deactivated, me or normal
  'member': "member_example", // String |  true or false
  'memberFields': "'fullName and username'" // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
};
apiInstance.getBoardsMembershipsByIdBoard(idBoard, key, token, opts, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **filter** | **String**| all or a comma-separated list of: active, admin, deactivated, me or normal | [optional] [default to &#39;all&#39;]
 **member** | **String**|  true or false | [optional] 
 **memberFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to &#39;fullName and username&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getBoardsMembershipsByIdBoardByIdMembership

> getBoardsMembershipsByIdBoardByIdMembership(idBoard, idMembership, key, token, opts)

getBoardsMembershipsByIdBoardByIdMembership()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let idMembership = "idMembership_example"; // String | idMembership
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'member': "member_example", // String |  true or false
  'memberFields': "'fullName and username'" // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
};
apiInstance.getBoardsMembershipsByIdBoardByIdMembership(idBoard, idMembership, key, token, opts, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **idMembership** | **String**| idMembership | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **member** | **String**|  true or false | [optional] 
 **memberFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to &#39;fullName and username&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getBoardsMyPrefsByIdBoard

> getBoardsMyPrefsByIdBoard(idBoard, key, token)

getBoardsMyPrefsByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.getBoardsMyPrefsByIdBoard(idBoard, key, token, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getBoardsOrganizationByIdBoard

> getBoardsOrganizationByIdBoard(idBoard, key, token, opts)

getBoardsOrganizationByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'fields': "'all'" // String | all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website
};
apiInstance.getBoardsOrganizationByIdBoard(idBoard, key, token, opts, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
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


## getBoardsOrganizationByIdBoardByField

> getBoardsOrganizationByIdBoardByField(idBoard, field, key, token)

getBoardsOrganizationByIdBoardByField()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let field = "field_example"; // String | field
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.getBoardsOrganizationByIdBoardByField(idBoard, field, key, token, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
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


## updateBoardsByIdBoard

> updateBoardsByIdBoard(idBoard, key, token, boards)

updateBoardsByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let boards = new Trello.Boards(); // Boards | Attributes of \"Boards\" to be updated.
apiInstance.updateBoardsByIdBoard(idBoard, key, token, boards, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **boards** | [**Boards**](Boards.md)| Attributes of \&quot;Boards\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateBoardsClosedByIdBoard

> updateBoardsClosedByIdBoard(idBoard, key, token, boardsClosed)

updateBoardsClosedByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let boardsClosed = new Trello.BoardsClosed(); // BoardsClosed | Attributes of \"Boards Closed\" to be updated.
apiInstance.updateBoardsClosedByIdBoard(idBoard, key, token, boardsClosed, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **boardsClosed** | [**BoardsClosed**](BoardsClosed.md)| Attributes of \&quot;Boards Closed\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateBoardsDescByIdBoard

> updateBoardsDescByIdBoard(idBoard, key, token, boardsDesc)

updateBoardsDescByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let boardsDesc = new Trello.BoardsDesc(); // BoardsDesc | Attributes of \"Boards Desc\" to be updated.
apiInstance.updateBoardsDescByIdBoard(idBoard, key, token, boardsDesc, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **boardsDesc** | [**BoardsDesc**](BoardsDesc.md)| Attributes of \&quot;Boards Desc\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateBoardsIdOrganizationByIdBoard

> updateBoardsIdOrganizationByIdBoard(idBoard, key, token, boardsIdOrganization)

updateBoardsIdOrganizationByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let boardsIdOrganization = new Trello.BoardsIdOrganization(); // BoardsIdOrganization | Attributes of \"Boards Id Organization\" to be updated.
apiInstance.updateBoardsIdOrganizationByIdBoard(idBoard, key, token, boardsIdOrganization, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **boardsIdOrganization** | [**BoardsIdOrganization**](BoardsIdOrganization.md)| Attributes of \&quot;Boards Id Organization\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateBoardsLabelNamesBlueByIdBoard

> updateBoardsLabelNamesBlueByIdBoard(idBoard, key, token, labelNamesBlue)

updateBoardsLabelNamesBlueByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let labelNamesBlue = new Trello.LabelNamesBlue(); // LabelNamesBlue | Attributes of \"Label Names Blue\" to be updated.
apiInstance.updateBoardsLabelNamesBlueByIdBoard(idBoard, key, token, labelNamesBlue, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **labelNamesBlue** | [**LabelNamesBlue**](LabelNamesBlue.md)| Attributes of \&quot;Label Names Blue\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateBoardsLabelNamesGreenByIdBoard

> updateBoardsLabelNamesGreenByIdBoard(idBoard, key, token, labelNamesGreen)

updateBoardsLabelNamesGreenByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let labelNamesGreen = new Trello.LabelNamesGreen(); // LabelNamesGreen | Attributes of \"Label Names Green\" to be updated.
apiInstance.updateBoardsLabelNamesGreenByIdBoard(idBoard, key, token, labelNamesGreen, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **labelNamesGreen** | [**LabelNamesGreen**](LabelNamesGreen.md)| Attributes of \&quot;Label Names Green\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateBoardsLabelNamesOrangeByIdBoard

> updateBoardsLabelNamesOrangeByIdBoard(idBoard, key, token, labelNamesOrange)

updateBoardsLabelNamesOrangeByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let labelNamesOrange = new Trello.LabelNamesOrange(); // LabelNamesOrange | Attributes of \"Label Names Orange\" to be updated.
apiInstance.updateBoardsLabelNamesOrangeByIdBoard(idBoard, key, token, labelNamesOrange, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **labelNamesOrange** | [**LabelNamesOrange**](LabelNamesOrange.md)| Attributes of \&quot;Label Names Orange\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateBoardsLabelNamesPurpleByIdBoard

> updateBoardsLabelNamesPurpleByIdBoard(idBoard, key, token, labelNamesPurple)

updateBoardsLabelNamesPurpleByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let labelNamesPurple = new Trello.LabelNamesPurple(); // LabelNamesPurple | Attributes of \"Label Names Purple\" to be updated.
apiInstance.updateBoardsLabelNamesPurpleByIdBoard(idBoard, key, token, labelNamesPurple, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **labelNamesPurple** | [**LabelNamesPurple**](LabelNamesPurple.md)| Attributes of \&quot;Label Names Purple\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateBoardsLabelNamesRedByIdBoard

> updateBoardsLabelNamesRedByIdBoard(idBoard, key, token, labelNamesRed)

updateBoardsLabelNamesRedByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let labelNamesRed = new Trello.LabelNamesRed(); // LabelNamesRed | Attributes of \"Label Names Red\" to be updated.
apiInstance.updateBoardsLabelNamesRedByIdBoard(idBoard, key, token, labelNamesRed, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **labelNamesRed** | [**LabelNamesRed**](LabelNamesRed.md)| Attributes of \&quot;Label Names Red\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateBoardsLabelNamesYellowByIdBoard

> updateBoardsLabelNamesYellowByIdBoard(idBoard, key, token, labelNamesYellow)

updateBoardsLabelNamesYellowByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let labelNamesYellow = new Trello.LabelNamesYellow(); // LabelNamesYellow | Attributes of \"Label Names Yellow\" to be updated.
apiInstance.updateBoardsLabelNamesYellowByIdBoard(idBoard, key, token, labelNamesYellow, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **labelNamesYellow** | [**LabelNamesYellow**](LabelNamesYellow.md)| Attributes of \&quot;Label Names Yellow\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateBoardsMembersByIdBoard

> updateBoardsMembersByIdBoard(idBoard, key, token, boardsMembers)

updateBoardsMembersByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let boardsMembers = new Trello.BoardsMembers(); // BoardsMembers | Attributes of \"Boards Members\" to be updated.
apiInstance.updateBoardsMembersByIdBoard(idBoard, key, token, boardsMembers, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **boardsMembers** | [**BoardsMembers**](BoardsMembers.md)| Attributes of \&quot;Boards Members\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateBoardsMembersByIdBoardByIdMember

> updateBoardsMembersByIdBoardByIdMember(idBoard, idMember, key, token, boardsMembers)

updateBoardsMembersByIdBoardByIdMember()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let idMember = "idMember_example"; // String | idMember
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let boardsMembers = new Trello.BoardsMembers(); // BoardsMembers | Attributes of \"Boards Members\" to be updated.
apiInstance.updateBoardsMembersByIdBoardByIdMember(idBoard, idMember, key, token, boardsMembers, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **idMember** | **String**| idMember | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **boardsMembers** | [**BoardsMembers**](BoardsMembers.md)| Attributes of \&quot;Boards Members\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateBoardsMembershipsByIdBoardByIdMembership

> updateBoardsMembershipsByIdBoardByIdMembership(idBoard, idMembership, key, token, boardsMemberships)

updateBoardsMembershipsByIdBoardByIdMembership()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let idMembership = "idMembership_example"; // String | idMembership
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let boardsMemberships = new Trello.BoardsMemberships(); // BoardsMemberships | Attributes of \"Boards Memberships\" to be updated.
apiInstance.updateBoardsMembershipsByIdBoardByIdMembership(idBoard, idMembership, key, token, boardsMemberships, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **idMembership** | **String**| idMembership | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **boardsMemberships** | [**BoardsMemberships**](BoardsMemberships.md)| Attributes of \&quot;Boards Memberships\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateBoardsMyPrefsEmailPositionByIdBoard

> updateBoardsMyPrefsEmailPositionByIdBoard(idBoard, key, token, myPrefsEmailPosition)

updateBoardsMyPrefsEmailPositionByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let myPrefsEmailPosition = new Trello.MyPrefsEmailPosition(); // MyPrefsEmailPosition | Attributes of \"My Prefs Email Position\" to be updated.
apiInstance.updateBoardsMyPrefsEmailPositionByIdBoard(idBoard, key, token, myPrefsEmailPosition, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **myPrefsEmailPosition** | [**MyPrefsEmailPosition**](MyPrefsEmailPosition.md)| Attributes of \&quot;My Prefs Email Position\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateBoardsMyPrefsIdEmailListByIdBoard

> updateBoardsMyPrefsIdEmailListByIdBoard(idBoard, key, token, myPrefsIdEmailList)

updateBoardsMyPrefsIdEmailListByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let myPrefsIdEmailList = new Trello.MyPrefsIdEmailList(); // MyPrefsIdEmailList | Attributes of \"My Prefs Id Email List\" to be updated.
apiInstance.updateBoardsMyPrefsIdEmailListByIdBoard(idBoard, key, token, myPrefsIdEmailList, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **myPrefsIdEmailList** | [**MyPrefsIdEmailList**](MyPrefsIdEmailList.md)| Attributes of \&quot;My Prefs Id Email List\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateBoardsMyPrefsShowListGuideByIdBoard

> updateBoardsMyPrefsShowListGuideByIdBoard(idBoard, key, token, myPrefsShowListGuide)

updateBoardsMyPrefsShowListGuideByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let myPrefsShowListGuide = new Trello.MyPrefsShowListGuide(); // MyPrefsShowListGuide | Attributes of \"My Prefs Show List Guide\" to be updated.
apiInstance.updateBoardsMyPrefsShowListGuideByIdBoard(idBoard, key, token, myPrefsShowListGuide, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **myPrefsShowListGuide** | [**MyPrefsShowListGuide**](MyPrefsShowListGuide.md)| Attributes of \&quot;My Prefs Show List Guide\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateBoardsMyPrefsShowSidebarActivityByIdBoard

> updateBoardsMyPrefsShowSidebarActivityByIdBoard(idBoard, key, token, myPrefsShowSidebarActivity)

updateBoardsMyPrefsShowSidebarActivityByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let myPrefsShowSidebarActivity = new Trello.MyPrefsShowSidebarActivity(); // MyPrefsShowSidebarActivity | Attributes of \"My Prefs Show Sidebar Activity\" to be updated.
apiInstance.updateBoardsMyPrefsShowSidebarActivityByIdBoard(idBoard, key, token, myPrefsShowSidebarActivity, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **myPrefsShowSidebarActivity** | [**MyPrefsShowSidebarActivity**](MyPrefsShowSidebarActivity.md)| Attributes of \&quot;My Prefs Show Sidebar Activity\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateBoardsMyPrefsShowSidebarBoardActionsByIdBoard

> updateBoardsMyPrefsShowSidebarBoardActionsByIdBoard(idBoard, key, token, myPrefsShowSidebarBoardActions)

updateBoardsMyPrefsShowSidebarBoardActionsByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let myPrefsShowSidebarBoardActions = new Trello.MyPrefsShowSidebarBoardActions(); // MyPrefsShowSidebarBoardActions | Attributes of \"My Prefs Show Sidebar Board Actions\" to be updated.
apiInstance.updateBoardsMyPrefsShowSidebarBoardActionsByIdBoard(idBoard, key, token, myPrefsShowSidebarBoardActions, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **myPrefsShowSidebarBoardActions** | [**MyPrefsShowSidebarBoardActions**](MyPrefsShowSidebarBoardActions.md)| Attributes of \&quot;My Prefs Show Sidebar Board Actions\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateBoardsMyPrefsShowSidebarByIdBoard

> updateBoardsMyPrefsShowSidebarByIdBoard(idBoard, key, token, myPrefsShowSidebar)

updateBoardsMyPrefsShowSidebarByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let myPrefsShowSidebar = new Trello.MyPrefsShowSidebar(); // MyPrefsShowSidebar | Attributes of \"My Prefs Show Sidebar\" to be updated.
apiInstance.updateBoardsMyPrefsShowSidebarByIdBoard(idBoard, key, token, myPrefsShowSidebar, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **myPrefsShowSidebar** | [**MyPrefsShowSidebar**](MyPrefsShowSidebar.md)| Attributes of \&quot;My Prefs Show Sidebar\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateBoardsMyPrefsShowSidebarMembersByIdBoard

> updateBoardsMyPrefsShowSidebarMembersByIdBoard(idBoard, key, token, myPrefsShowSidebarMembers)

updateBoardsMyPrefsShowSidebarMembersByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let myPrefsShowSidebarMembers = new Trello.MyPrefsShowSidebarMembers(); // MyPrefsShowSidebarMembers | Attributes of \"My Prefs Show Sidebar Members\" to be updated.
apiInstance.updateBoardsMyPrefsShowSidebarMembersByIdBoard(idBoard, key, token, myPrefsShowSidebarMembers, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **myPrefsShowSidebarMembers** | [**MyPrefsShowSidebarMembers**](MyPrefsShowSidebarMembers.md)| Attributes of \&quot;My Prefs Show Sidebar Members\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateBoardsNameByIdBoard

> updateBoardsNameByIdBoard(idBoard, key, token, boardsName)

updateBoardsNameByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let boardsName = new Trello.BoardsName(); // BoardsName | Attributes of \"Boards Name\" to be updated.
apiInstance.updateBoardsNameByIdBoard(idBoard, key, token, boardsName, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **boardsName** | [**BoardsName**](BoardsName.md)| Attributes of \&quot;Boards Name\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateBoardsPrefsBackgroundByIdBoard

> updateBoardsPrefsBackgroundByIdBoard(idBoard, key, token, prefsBackground)

updateBoardsPrefsBackgroundByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let prefsBackground = new Trello.PrefsBackground(); // PrefsBackground | Attributes of \"Prefs Background\" to be updated.
apiInstance.updateBoardsPrefsBackgroundByIdBoard(idBoard, key, token, prefsBackground, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **prefsBackground** | [**PrefsBackground**](PrefsBackground.md)| Attributes of \&quot;Prefs Background\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateBoardsPrefsCalendarFeedEnabledByIdBoard

> updateBoardsPrefsCalendarFeedEnabledByIdBoard(idBoard, key, token, prefsCalendarFeedEnabled)

updateBoardsPrefsCalendarFeedEnabledByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let prefsCalendarFeedEnabled = new Trello.PrefsCalendarFeedEnabled(); // PrefsCalendarFeedEnabled | Attributes of \"Prefs Calendar Feed Enabled\" to be updated.
apiInstance.updateBoardsPrefsCalendarFeedEnabledByIdBoard(idBoard, key, token, prefsCalendarFeedEnabled, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **prefsCalendarFeedEnabled** | [**PrefsCalendarFeedEnabled**](PrefsCalendarFeedEnabled.md)| Attributes of \&quot;Prefs Calendar Feed Enabled\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateBoardsPrefsCardAgingByIdBoard

> updateBoardsPrefsCardAgingByIdBoard(idBoard, key, token, prefsCardAging)

updateBoardsPrefsCardAgingByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let prefsCardAging = new Trello.PrefsCardAging(); // PrefsCardAging | Attributes of \"Prefs Card Aging\" to be updated.
apiInstance.updateBoardsPrefsCardAgingByIdBoard(idBoard, key, token, prefsCardAging, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **prefsCardAging** | [**PrefsCardAging**](PrefsCardAging.md)| Attributes of \&quot;Prefs Card Aging\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateBoardsPrefsCardCoversByIdBoard

> updateBoardsPrefsCardCoversByIdBoard(idBoard, key, token, prefsCardCovers)

updateBoardsPrefsCardCoversByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let prefsCardCovers = new Trello.PrefsCardCovers(); // PrefsCardCovers | Attributes of \"Prefs Card Covers\" to be updated.
apiInstance.updateBoardsPrefsCardCoversByIdBoard(idBoard, key, token, prefsCardCovers, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **prefsCardCovers** | [**PrefsCardCovers**](PrefsCardCovers.md)| Attributes of \&quot;Prefs Card Covers\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateBoardsPrefsCommentsByIdBoard

> updateBoardsPrefsCommentsByIdBoard(idBoard, key, token, prefsComments)

updateBoardsPrefsCommentsByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let prefsComments = new Trello.PrefsComments(); // PrefsComments | Attributes of \"Prefs Comments\" to be updated.
apiInstance.updateBoardsPrefsCommentsByIdBoard(idBoard, key, token, prefsComments, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **prefsComments** | [**PrefsComments**](PrefsComments.md)| Attributes of \&quot;Prefs Comments\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateBoardsPrefsInvitationsByIdBoard

> updateBoardsPrefsInvitationsByIdBoard(idBoard, key, token, prefsInvitations)

updateBoardsPrefsInvitationsByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let prefsInvitations = new Trello.PrefsInvitations(); // PrefsInvitations | Attributes of \"Prefs Invitations\" to be updated.
apiInstance.updateBoardsPrefsInvitationsByIdBoard(idBoard, key, token, prefsInvitations, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **prefsInvitations** | [**PrefsInvitations**](PrefsInvitations.md)| Attributes of \&quot;Prefs Invitations\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateBoardsPrefsPermissionLevelByIdBoard

> updateBoardsPrefsPermissionLevelByIdBoard(idBoard, key, token, prefsPermissionLevel)

updateBoardsPrefsPermissionLevelByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let prefsPermissionLevel = new Trello.PrefsPermissionLevel(); // PrefsPermissionLevel | Attributes of \"Prefs Permission Level\" to be updated.
apiInstance.updateBoardsPrefsPermissionLevelByIdBoard(idBoard, key, token, prefsPermissionLevel, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **prefsPermissionLevel** | [**PrefsPermissionLevel**](PrefsPermissionLevel.md)| Attributes of \&quot;Prefs Permission Level\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateBoardsPrefsSelfJoinByIdBoard

> updateBoardsPrefsSelfJoinByIdBoard(idBoard, key, token, prefsSelfJoin)

updateBoardsPrefsSelfJoinByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let prefsSelfJoin = new Trello.PrefsSelfJoin(); // PrefsSelfJoin | Attributes of \"Prefs Self Join\" to be updated.
apiInstance.updateBoardsPrefsSelfJoinByIdBoard(idBoard, key, token, prefsSelfJoin, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **prefsSelfJoin** | [**PrefsSelfJoin**](PrefsSelfJoin.md)| Attributes of \&quot;Prefs Self Join\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateBoardsPrefsVotingByIdBoard

> updateBoardsPrefsVotingByIdBoard(idBoard, key, token, prefsVoting)

updateBoardsPrefsVotingByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let prefsVoting = new Trello.PrefsVoting(); // PrefsVoting | Attributes of \"Prefs Voting\" to be updated.
apiInstance.updateBoardsPrefsVotingByIdBoard(idBoard, key, token, prefsVoting, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **prefsVoting** | [**PrefsVoting**](PrefsVoting.md)| Attributes of \&quot;Prefs Voting\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateBoardsSubscribedByIdBoard

> updateBoardsSubscribedByIdBoard(idBoard, key, token, boardsSubscribed)

updateBoardsSubscribedByIdBoard()

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

let apiInstance = new Trello.BoardApi();
let idBoard = "idBoard_example"; // String | board_id
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let boardsSubscribed = new Trello.BoardsSubscribed(); // BoardsSubscribed | Attributes of \"Boards Subscribed\" to be updated.
apiInstance.updateBoardsSubscribedByIdBoard(idBoard, key, token, boardsSubscribed, (error, data, response) => {
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
 **idBoard** | **String**| board_id | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **boardsSubscribed** | [**BoardsSubscribed**](BoardsSubscribed.md)| Attributes of \&quot;Boards Subscribed\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

