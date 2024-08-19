# Trello.CardApi

All URIs are relative to *https://trello.com/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addCards**](CardApi.md#addCards) | **POST** /cards | addCards()
[**addCardsActionsCommentsByIdCard**](CardApi.md#addCardsActionsCommentsByIdCard) | **POST** /cards/{idCard}/actions/comments | addCardsActionsCommentsByIdCard()
[**addCardsAttachmentsByIdCard**](CardApi.md#addCardsAttachmentsByIdCard) | **POST** /cards/{idCard}/attachments | addCardsAttachmentsByIdCard()
[**addCardsChecklistCheckItemByIdCardByIdChecklist**](CardApi.md#addCardsChecklistCheckItemByIdCardByIdChecklist) | **POST** /cards/{idCard}/checklist/{idChecklist}/checkItem | addCardsChecklistCheckItemByIdCardByIdChecklist()
[**addCardsChecklistCheckItemConvertToCardByIdCardByIdChecklistByIdCheckItem**](CardApi.md#addCardsChecklistCheckItemConvertToCardByIdCardByIdChecklistByIdCheckItem) | **POST** /cards/{idCard}/checklist/{idChecklist}/checkItem/{idCheckItem}/convertToCard | addCardsChecklistCheckItemConvertToCardByIdCardByIdChecklistByIdCheckItem()
[**addCardsChecklistsByIdCard**](CardApi.md#addCardsChecklistsByIdCard) | **POST** /cards/{idCard}/checklists | addCardsChecklistsByIdCard()
[**addCardsIdLabelsByIdCard**](CardApi.md#addCardsIdLabelsByIdCard) | **POST** /cards/{idCard}/idLabels | addCardsIdLabelsByIdCard()
[**addCardsIdMembersByIdCard**](CardApi.md#addCardsIdMembersByIdCard) | **POST** /cards/{idCard}/idMembers | addCardsIdMembersByIdCard()
[**addCardsLabelsByIdCard**](CardApi.md#addCardsLabelsByIdCard) | **POST** /cards/{idCard}/labels | addCardsLabelsByIdCard()
[**addCardsMarkAssociatedNotificationsReadByIdCard**](CardApi.md#addCardsMarkAssociatedNotificationsReadByIdCard) | **POST** /cards/{idCard}/markAssociatedNotificationsRead | addCardsMarkAssociatedNotificationsReadByIdCard()
[**addCardsMembersVotedByIdCard**](CardApi.md#addCardsMembersVotedByIdCard) | **POST** /cards/{idCard}/membersVoted | addCardsMembersVotedByIdCard()
[**addCardsStickersByIdCard**](CardApi.md#addCardsStickersByIdCard) | **POST** /cards/{idCard}/stickers | addCardsStickersByIdCard()
[**deleteCardsActionsCommentsByIdCardByIdAction**](CardApi.md#deleteCardsActionsCommentsByIdCardByIdAction) | **DELETE** /cards/{idCard}/actions/{idAction}/comments | deleteCardsActionsCommentsByIdCardByIdAction()
[**deleteCardsAttachmentsByIdCardByIdAttachment**](CardApi.md#deleteCardsAttachmentsByIdCardByIdAttachment) | **DELETE** /cards/{idCard}/attachments/{idAttachment} | deleteCardsAttachmentsByIdCardByIdAttachment()
[**deleteCardsByIdCard**](CardApi.md#deleteCardsByIdCard) | **DELETE** /cards/{idCard} | deleteCardsByIdCard()
[**deleteCardsChecklistCheckItemByIdCardByIdChecklistByIdCheckItem**](CardApi.md#deleteCardsChecklistCheckItemByIdCardByIdChecklistByIdCheckItem) | **DELETE** /cards/{idCard}/checklist/{idChecklist}/checkItem/{idCheckItem} | deleteCardsChecklistCheckItemByIdCardByIdChecklistByIdCheckItem()
[**deleteCardsChecklistsByIdCardByIdChecklist**](CardApi.md#deleteCardsChecklistsByIdCardByIdChecklist) | **DELETE** /cards/{idCard}/checklists/{idChecklist} | deleteCardsChecklistsByIdCardByIdChecklist()
[**deleteCardsIdLabelsByIdCardByIdLabel**](CardApi.md#deleteCardsIdLabelsByIdCardByIdLabel) | **DELETE** /cards/{idCard}/idLabels/{idLabel} | deleteCardsIdLabelsByIdCardByIdLabel()
[**deleteCardsIdMembersByIdCardByIdMember**](CardApi.md#deleteCardsIdMembersByIdCardByIdMember) | **DELETE** /cards/{idCard}/idMembers/{idMember} | deleteCardsIdMembersByIdCardByIdMember()
[**deleteCardsLabelsByIdCardByColor**](CardApi.md#deleteCardsLabelsByIdCardByColor) | **DELETE** /cards/{idCard}/labels/{color} | deleteCardsLabelsByIdCardByColor()
[**deleteCardsMembersVotedByIdCardByIdMember**](CardApi.md#deleteCardsMembersVotedByIdCardByIdMember) | **DELETE** /cards/{idCard}/membersVoted/{idMember} | deleteCardsMembersVotedByIdCardByIdMember()
[**deleteCardsStickersByIdCardByIdSticker**](CardApi.md#deleteCardsStickersByIdCardByIdSticker) | **DELETE** /cards/{idCard}/stickers/{idSticker} | deleteCardsStickersByIdCardByIdSticker()
[**getCardsActionsByIdCard**](CardApi.md#getCardsActionsByIdCard) | **GET** /cards/{idCard}/actions | getCardsActionsByIdCard()
[**getCardsAttachmentsByIdCard**](CardApi.md#getCardsAttachmentsByIdCard) | **GET** /cards/{idCard}/attachments | getCardsAttachmentsByIdCard()
[**getCardsAttachmentsByIdCardByIdAttachment**](CardApi.md#getCardsAttachmentsByIdCardByIdAttachment) | **GET** /cards/{idCard}/attachments/{idAttachment} | getCardsAttachmentsByIdCardByIdAttachment()
[**getCardsBoardByIdCard**](CardApi.md#getCardsBoardByIdCard) | **GET** /cards/{idCard}/board | getCardsBoardByIdCard()
[**getCardsBoardByIdCardByField**](CardApi.md#getCardsBoardByIdCardByField) | **GET** /cards/{idCard}/board/{field} | getCardsBoardByIdCardByField()
[**getCardsByIdCard**](CardApi.md#getCardsByIdCard) | **GET** /cards/{idCard} | getCardsByIdCard()
[**getCardsByIdCardByField**](CardApi.md#getCardsByIdCardByField) | **GET** /cards/{idCard}/{field} | getCardsByIdCardByField()
[**getCardsCheckItemStatesByIdCard**](CardApi.md#getCardsCheckItemStatesByIdCard) | **GET** /cards/{idCard}/checkItemStates | getCardsCheckItemStatesByIdCard()
[**getCardsChecklistsByIdCard**](CardApi.md#getCardsChecklistsByIdCard) | **GET** /cards/{idCard}/checklists | getCardsChecklistsByIdCard()
[**getCardsListByIdCard**](CardApi.md#getCardsListByIdCard) | **GET** /cards/{idCard}/list | getCardsListByIdCard()
[**getCardsListByIdCardByField**](CardApi.md#getCardsListByIdCardByField) | **GET** /cards/{idCard}/list/{field} | getCardsListByIdCardByField()
[**getCardsMembersByIdCard**](CardApi.md#getCardsMembersByIdCard) | **GET** /cards/{idCard}/members | getCardsMembersByIdCard()
[**getCardsMembersVotedByIdCard**](CardApi.md#getCardsMembersVotedByIdCard) | **GET** /cards/{idCard}/membersVoted | getCardsMembersVotedByIdCard()
[**getCardsStickersByIdCard**](CardApi.md#getCardsStickersByIdCard) | **GET** /cards/{idCard}/stickers | getCardsStickersByIdCard()
[**getCardsStickersByIdCardByIdSticker**](CardApi.md#getCardsStickersByIdCardByIdSticker) | **GET** /cards/{idCard}/stickers/{idSticker} | getCardsStickersByIdCardByIdSticker()
[**updateCardsActionsCommentsByIdCardByIdAction**](CardApi.md#updateCardsActionsCommentsByIdCardByIdAction) | **PUT** /cards/{idCard}/actions/{idAction}/comments | updateCardsActionsCommentsByIdCardByIdAction()
[**updateCardsByIdCard**](CardApi.md#updateCardsByIdCard) | **PUT** /cards/{idCard} | updateCardsByIdCard()
[**updateCardsChecklistCheckItemByIdCardByIdChecklistCurrentByIdCheckItem**](CardApi.md#updateCardsChecklistCheckItemByIdCardByIdChecklistCurrentByIdCheckItem) | **PUT** /cards/{idCard}/checklist/{idChecklistCurrent}/checkItem/{idCheckItem} | updateCardsChecklistCheckItemByIdCardByIdChecklistCurrentByIdCheckItem()
[**updateCardsChecklistCheckItemNameByIdCardByIdChecklistByIdCheckItem**](CardApi.md#updateCardsChecklistCheckItemNameByIdCardByIdChecklistByIdCheckItem) | **PUT** /cards/{idCard}/checklist/{idChecklist}/checkItem/{idCheckItem}/name | updateCardsChecklistCheckItemNameByIdCardByIdChecklistByIdCheckItem()
[**updateCardsChecklistCheckItemPosByIdCardByIdChecklistByIdCheckItem**](CardApi.md#updateCardsChecklistCheckItemPosByIdCardByIdChecklistByIdCheckItem) | **PUT** /cards/{idCard}/checklist/{idChecklist}/checkItem/{idCheckItem}/pos | updateCardsChecklistCheckItemPosByIdCardByIdChecklistByIdCheckItem()
[**updateCardsChecklistCheckItemStateByIdCardByIdChecklistByIdCheckItem**](CardApi.md#updateCardsChecklistCheckItemStateByIdCardByIdChecklistByIdCheckItem) | **PUT** /cards/{idCard}/checklist/{idChecklist}/checkItem/{idCheckItem}/state | updateCardsChecklistCheckItemStateByIdCardByIdChecklistByIdCheckItem()
[**updateCardsClosedByIdCard**](CardApi.md#updateCardsClosedByIdCard) | **PUT** /cards/{idCard}/closed | updateCardsClosedByIdCard()
[**updateCardsDescByIdCard**](CardApi.md#updateCardsDescByIdCard) | **PUT** /cards/{idCard}/desc | updateCardsDescByIdCard()
[**updateCardsDueByIdCard**](CardApi.md#updateCardsDueByIdCard) | **PUT** /cards/{idCard}/due | updateCardsDueByIdCard()
[**updateCardsIdAttachmentCoverByIdCard**](CardApi.md#updateCardsIdAttachmentCoverByIdCard) | **PUT** /cards/{idCard}/idAttachmentCover | updateCardsIdAttachmentCoverByIdCard()
[**updateCardsIdBoardByIdCard**](CardApi.md#updateCardsIdBoardByIdCard) | **PUT** /cards/{idCard}/idBoard | updateCardsIdBoardByIdCard()
[**updateCardsIdListByIdCard**](CardApi.md#updateCardsIdListByIdCard) | **PUT** /cards/{idCard}/idList | updateCardsIdListByIdCard()
[**updateCardsIdMembersByIdCard**](CardApi.md#updateCardsIdMembersByIdCard) | **PUT** /cards/{idCard}/idMembers | updateCardsIdMembersByIdCard()
[**updateCardsLabelsByIdCard**](CardApi.md#updateCardsLabelsByIdCard) | **PUT** /cards/{idCard}/labels | updateCardsLabelsByIdCard()
[**updateCardsNameByIdCard**](CardApi.md#updateCardsNameByIdCard) | **PUT** /cards/{idCard}/name | updateCardsNameByIdCard()
[**updateCardsPosByIdCard**](CardApi.md#updateCardsPosByIdCard) | **PUT** /cards/{idCard}/pos | updateCardsPosByIdCard()
[**updateCardsStickersByIdCardByIdSticker**](CardApi.md#updateCardsStickersByIdCardByIdSticker) | **PUT** /cards/{idCard}/stickers/{idSticker} | updateCardsStickersByIdCardByIdSticker()
[**updateCardsSubscribedByIdCard**](CardApi.md#updateCardsSubscribedByIdCard) | **PUT** /cards/{idCard}/subscribed | updateCardsSubscribedByIdCard()



## addCards

> addCards(key, token, cards)

addCards()

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

let apiInstance = new Trello.CardApi();
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let cards = new Trello.Cards(); // Cards | Attributes of \"Cards\" to be added.
apiInstance.addCards(key, token, cards, (error, data, response) => {
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
 **cards** | [**Cards**](Cards.md)| Attributes of \&quot;Cards\&quot; to be added. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## addCardsActionsCommentsByIdCard

> addCardsActionsCommentsByIdCard(idCard, key, token, actionsComments)

addCardsActionsCommentsByIdCard()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let actionsComments = new Trello.ActionsComments(); // ActionsComments | Attributes of \"Actions Comments\" to be added.
apiInstance.addCardsActionsCommentsByIdCard(idCard, key, token, actionsComments, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **actionsComments** | [**ActionsComments**](ActionsComments.md)| Attributes of \&quot;Actions Comments\&quot; to be added. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## addCardsAttachmentsByIdCard

> addCardsAttachmentsByIdCard(idCard, key, token, cardsAttachments)

addCardsAttachmentsByIdCard()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let cardsAttachments = new Trello.CardsAttachments(); // CardsAttachments | Attributes of \"Cards Attachments\" to be added.
apiInstance.addCardsAttachmentsByIdCard(idCard, key, token, cardsAttachments, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **cardsAttachments** | [**CardsAttachments**](CardsAttachments.md)| Attributes of \&quot;Cards Attachments\&quot; to be added. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## addCardsChecklistCheckItemByIdCardByIdChecklist

> addCardsChecklistCheckItemByIdCardByIdChecklist(idCard, idChecklist, key, token, cardsChecklistCheckItem)

addCardsChecklistCheckItemByIdCardByIdChecklist()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let idChecklist = "idChecklist_example"; // String | idChecklist
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let cardsChecklistCheckItem = new Trello.CardsChecklistCheckItem(); // CardsChecklistCheckItem | Attributes of \"Cards Checklist Check Item\" to be added.
apiInstance.addCardsChecklistCheckItemByIdCardByIdChecklist(idCard, idChecklist, key, token, cardsChecklistCheckItem, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **idChecklist** | **String**| idChecklist | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **cardsChecklistCheckItem** | [**CardsChecklistCheckItem**](CardsChecklistCheckItem.md)| Attributes of \&quot;Cards Checklist Check Item\&quot; to be added. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## addCardsChecklistCheckItemConvertToCardByIdCardByIdChecklistByIdCheckItem

> addCardsChecklistCheckItemConvertToCardByIdCardByIdChecklistByIdCheckItem(idCard, idChecklist, idCheckItem, key, token)

addCardsChecklistCheckItemConvertToCardByIdCardByIdChecklistByIdCheckItem()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let idChecklist = "idChecklist_example"; // String | idChecklist
let idCheckItem = "idCheckItem_example"; // String | idCheckItem
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.addCardsChecklistCheckItemConvertToCardByIdCardByIdChecklistByIdCheckItem(idCard, idChecklist, idCheckItem, key, token, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **idChecklist** | **String**| idChecklist | 
 **idCheckItem** | **String**| idCheckItem | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addCardsChecklistsByIdCard

> addCardsChecklistsByIdCard(idCard, key, token, cardsChecklists)

addCardsChecklistsByIdCard()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let cardsChecklists = new Trello.CardsChecklists(); // CardsChecklists | Attributes of \"Cards Checklists\" to be added.
apiInstance.addCardsChecklistsByIdCard(idCard, key, token, cardsChecklists, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **cardsChecklists** | [**CardsChecklists**](CardsChecklists.md)| Attributes of \&quot;Cards Checklists\&quot; to be added. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## addCardsIdLabelsByIdCard

> addCardsIdLabelsByIdCard(idCard, key, token, cardsIdLabels)

addCardsIdLabelsByIdCard()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let cardsIdLabels = new Trello.CardsIdLabels(); // CardsIdLabels | Attributes of \"Cards Id Labels\" to be added.
apiInstance.addCardsIdLabelsByIdCard(idCard, key, token, cardsIdLabels, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **cardsIdLabels** | [**CardsIdLabels**](CardsIdLabels.md)| Attributes of \&quot;Cards Id Labels\&quot; to be added. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## addCardsIdMembersByIdCard

> addCardsIdMembersByIdCard(idCard, key, token, cardsIdMembers)

addCardsIdMembersByIdCard()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let cardsIdMembers = new Trello.CardsIdMembers(); // CardsIdMembers | Attributes of \"Cards Id Members\" to be added.
apiInstance.addCardsIdMembersByIdCard(idCard, key, token, cardsIdMembers, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **cardsIdMembers** | [**CardsIdMembers**](CardsIdMembers.md)| Attributes of \&quot;Cards Id Members\&quot; to be added. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## addCardsLabelsByIdCard

> addCardsLabelsByIdCard(idCard, key, token, cardsLabels)

addCardsLabelsByIdCard()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let cardsLabels = new Trello.CardsLabels(); // CardsLabels | Attributes of \"Cards Labels\" to be added.
apiInstance.addCardsLabelsByIdCard(idCard, key, token, cardsLabels, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **cardsLabels** | [**CardsLabels**](CardsLabels.md)| Attributes of \&quot;Cards Labels\&quot; to be added. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## addCardsMarkAssociatedNotificationsReadByIdCard

> addCardsMarkAssociatedNotificationsReadByIdCard(idCard, key, token)

addCardsMarkAssociatedNotificationsReadByIdCard()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.addCardsMarkAssociatedNotificationsReadByIdCard(idCard, key, token, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addCardsMembersVotedByIdCard

> addCardsMembersVotedByIdCard(idCard, key, token, cardsMembersVoted)

addCardsMembersVotedByIdCard()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let cardsMembersVoted = new Trello.CardsMembersVoted(); // CardsMembersVoted | Attributes of \"Cards Members Voted\" to be added.
apiInstance.addCardsMembersVotedByIdCard(idCard, key, token, cardsMembersVoted, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **cardsMembersVoted** | [**CardsMembersVoted**](CardsMembersVoted.md)| Attributes of \&quot;Cards Members Voted\&quot; to be added. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## addCardsStickersByIdCard

> addCardsStickersByIdCard(idCard, key, token, cardsStickers)

addCardsStickersByIdCard()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let cardsStickers = new Trello.CardsStickers(); // CardsStickers | Attributes of \"Cards Stickers\" to be added.
apiInstance.addCardsStickersByIdCard(idCard, key, token, cardsStickers, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **cardsStickers** | [**CardsStickers**](CardsStickers.md)| Attributes of \&quot;Cards Stickers\&quot; to be added. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## deleteCardsActionsCommentsByIdCardByIdAction

> deleteCardsActionsCommentsByIdCardByIdAction(idCard, idAction, key, token)

deleteCardsActionsCommentsByIdCardByIdAction()

This can only be done by the original author of the comment, or someone with higher permissions than the original author.

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let idAction = "idAction_example"; // String | idAction
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.deleteCardsActionsCommentsByIdCardByIdAction(idCard, idAction, key, token, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **idAction** | **String**| idAction | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteCardsAttachmentsByIdCardByIdAttachment

> deleteCardsAttachmentsByIdCardByIdAttachment(idCard, idAttachment, key, token)

deleteCardsAttachmentsByIdCardByIdAttachment()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let idAttachment = "idAttachment_example"; // String | idAttachment
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.deleteCardsAttachmentsByIdCardByIdAttachment(idCard, idAttachment, key, token, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **idAttachment** | **String**| idAttachment | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteCardsByIdCard

> deleteCardsByIdCard(idCard, key, token)

deleteCardsByIdCard()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.deleteCardsByIdCard(idCard, key, token, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteCardsChecklistCheckItemByIdCardByIdChecklistByIdCheckItem

> deleteCardsChecklistCheckItemByIdCardByIdChecklistByIdCheckItem(idCard, idChecklist, idCheckItem, key, token)

deleteCardsChecklistCheckItemByIdCardByIdChecklistByIdCheckItem()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let idChecklist = "idChecklist_example"; // String | idChecklist
let idCheckItem = "idCheckItem_example"; // String | idCheckItem
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.deleteCardsChecklistCheckItemByIdCardByIdChecklistByIdCheckItem(idCard, idChecklist, idCheckItem, key, token, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **idChecklist** | **String**| idChecklist | 
 **idCheckItem** | **String**| idCheckItem | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteCardsChecklistsByIdCardByIdChecklist

> deleteCardsChecklistsByIdCardByIdChecklist(idCard, idChecklist, key, token)

deleteCardsChecklistsByIdCardByIdChecklist()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let idChecklist = "idChecklist_example"; // String | idChecklist
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.deleteCardsChecklistsByIdCardByIdChecklist(idCard, idChecklist, key, token, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **idChecklist** | **String**| idChecklist | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteCardsIdLabelsByIdCardByIdLabel

> deleteCardsIdLabelsByIdCardByIdLabel(idCard, idLabel, key, token)

deleteCardsIdLabelsByIdCardByIdLabel()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let idLabel = "idLabel_example"; // String | idLabel
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.deleteCardsIdLabelsByIdCardByIdLabel(idCard, idLabel, key, token, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **idLabel** | **String**| idLabel | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteCardsIdMembersByIdCardByIdMember

> deleteCardsIdMembersByIdCardByIdMember(idCard, idMember, key, token)

deleteCardsIdMembersByIdCardByIdMember()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let idMember = "idMember_example"; // String | idMember
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.deleteCardsIdMembersByIdCardByIdMember(idCard, idMember, key, token, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
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


## deleteCardsLabelsByIdCardByColor

> deleteCardsLabelsByIdCardByColor(idCard, color, key, token)

deleteCardsLabelsByIdCardByColor()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let color = "color_example"; // String | color
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.deleteCardsLabelsByIdCardByColor(idCard, color, key, token, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **color** | **String**| color | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteCardsMembersVotedByIdCardByIdMember

> deleteCardsMembersVotedByIdCardByIdMember(idCard, idMember, key, token)

deleteCardsMembersVotedByIdCardByIdMember()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let idMember = "idMember_example"; // String | idMember
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.deleteCardsMembersVotedByIdCardByIdMember(idCard, idMember, key, token, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
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


## deleteCardsStickersByIdCardByIdSticker

> deleteCardsStickersByIdCardByIdSticker(idCard, idSticker, key, token)

deleteCardsStickersByIdCardByIdSticker()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let idSticker = "idSticker_example"; // String | idSticker
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.deleteCardsStickersByIdCardByIdSticker(idCard, idSticker, key, token, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **idSticker** | **String**| idSticker | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getCardsActionsByIdCard

> getCardsActionsByIdCard(idCard, key, token, opts)

getCardsActionsByIdCard()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'entities': "entities_example", // String |  true or false
  'display': "display_example", // String |  true or false
  'filter': "'commentCard and updateCard:idList'", // String | all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization
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
apiInstance.getCardsActionsByIdCard(idCard, key, token, opts, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **entities** | **String**|  true or false | [optional] 
 **display** | **String**|  true or false | [optional] 
 **filter** | **String**| all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization | [optional] [default to &#39;commentCard and updateCard:idList&#39;]
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


## getCardsAttachmentsByIdCard

> getCardsAttachmentsByIdCard(idCard, key, token, opts)

getCardsAttachmentsByIdCard()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'fields': "'all'", // String | all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url
  'filter': "filter_example" // String | A boolean value or &quot;cover&quot; for only card cover attachments
};
apiInstance.getCardsAttachmentsByIdCard(idCard, key, token, opts, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **fields** | **String**| all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url | [optional] [default to &#39;all&#39;]
 **filter** | **String**| A boolean value or &amp;quot;cover&amp;quot; for only card cover attachments | [optional] 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getCardsAttachmentsByIdCardByIdAttachment

> getCardsAttachmentsByIdCardByIdAttachment(idCard, idAttachment, key, token, opts)

getCardsAttachmentsByIdCardByIdAttachment()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let idAttachment = "idAttachment_example"; // String | idAttachment
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'fields': "'all'" // String | all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url
};
apiInstance.getCardsAttachmentsByIdCardByIdAttachment(idCard, idAttachment, key, token, opts, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **idAttachment** | **String**| idAttachment | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **fields** | **String**| all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url | [optional] [default to &#39;all&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getCardsBoardByIdCard

> getCardsBoardByIdCard(idCard, key, token, opts)

getCardsBoardByIdCard()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'fields': "'all'" // String | all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url
};
apiInstance.getCardsBoardByIdCard(idCard, key, token, opts, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
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


## getCardsBoardByIdCardByField

> getCardsBoardByIdCardByField(idCard, field, key, token)

getCardsBoardByIdCardByField()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let field = "field_example"; // String | field
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.getCardsBoardByIdCardByField(idCard, field, key, token, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
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


## getCardsByIdCard

> getCardsByIdCard(idCard, key, token, opts)

getCardsByIdCard()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'actions': "actions_example", // String | all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization
  'actionsEntities': "actionsEntities_example", // String |  true or false
  'actionsDisplay': "actionsDisplay_example", // String |  true or false
  'actionsLimit': "'50'", // String | a number from 0 to 1000
  'actionFields': "'all'", // String | all or a comma-separated list of: data, date, idMemberCreator or type
  'actionMemberCreatorFields': "'avatarHash, fullName, initials and username'", // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
  'attachments': "attachments_example", // String | A boolean value or &quot;cover&quot; for only card cover attachments
  'attachmentFields': "'all'", // String | all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url
  'members': "members_example", // String |  true or false
  'memberFields': "'avatarHash, fullName, initials and username'", // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
  'membersVoted': "membersVoted_example", // String |  true or false
  'memberVotedFields': "'avatarHash, fullName, initials and username'", // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
  'checkItemStates': "checkItemStates_example", // String |  true or false
  'checkItemStateFields': "'all'", // String | all or a comma-separated list of: idCheckItem or state
  'checklists': "'none'", // String | One of: all or none
  'checklistFields': "'all'", // String | all or a comma-separated list of: idBoard, idCard, name or pos
  'board': "board_example", // String |  true or false
  'boardFields': "'name, desc, descData, closed, idOrganization, pinned, url and prefs'", // String | all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url
  'list': "list_example", // String |  true or false
  'listFields': "'all'", // String | all or a comma-separated list of: closed, idBoard, name, pos or subscribed
  'stickers': "stickers_example", // String |  true or false
  'stickerFields': "'all'", // String | all or a comma-separated list of: image, imageScaled, imageUrl, left, rotate, top or zIndex
  'fields': "'badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idBoard, idChecklists, idLabels, idList, idMembers, idShort, idAttachmentCover, manualCoverAttachment, labels, name, pos, shortUrl and url'" // String | all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url
};
apiInstance.getCardsByIdCard(idCard, key, token, opts, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **actions** | **String**| all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization | [optional] 
 **actionsEntities** | **String**|  true or false | [optional] 
 **actionsDisplay** | **String**|  true or false | [optional] 
 **actionsLimit** | **String**| a number from 0 to 1000 | [optional] [default to &#39;50&#39;]
 **actionFields** | **String**| all or a comma-separated list of: data, date, idMemberCreator or type | [optional] [default to &#39;all&#39;]
 **actionMemberCreatorFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to &#39;avatarHash, fullName, initials and username&#39;]
 **attachments** | **String**| A boolean value or &amp;quot;cover&amp;quot; for only card cover attachments | [optional] 
 **attachmentFields** | **String**| all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url | [optional] [default to &#39;all&#39;]
 **members** | **String**|  true or false | [optional] 
 **memberFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to &#39;avatarHash, fullName, initials and username&#39;]
 **membersVoted** | **String**|  true or false | [optional] 
 **memberVotedFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to &#39;avatarHash, fullName, initials and username&#39;]
 **checkItemStates** | **String**|  true or false | [optional] 
 **checkItemStateFields** | **String**| all or a comma-separated list of: idCheckItem or state | [optional] [default to &#39;all&#39;]
 **checklists** | **String**| One of: all or none | [optional] [default to &#39;none&#39;]
 **checklistFields** | **String**| all or a comma-separated list of: idBoard, idCard, name or pos | [optional] [default to &#39;all&#39;]
 **board** | **String**|  true or false | [optional] 
 **boardFields** | **String**| all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url | [optional] [default to &#39;name, desc, descData, closed, idOrganization, pinned, url and prefs&#39;]
 **list** | **String**|  true or false | [optional] 
 **listFields** | **String**| all or a comma-separated list of: closed, idBoard, name, pos or subscribed | [optional] [default to &#39;all&#39;]
 **stickers** | **String**|  true or false | [optional] 
 **stickerFields** | **String**| all or a comma-separated list of: image, imageScaled, imageUrl, left, rotate, top or zIndex | [optional] [default to &#39;all&#39;]
 **fields** | **String**| all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url | [optional] [default to &#39;badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idBoard, idChecklists, idLabels, idList, idMembers, idShort, idAttachmentCover, manualCoverAttachment, labels, name, pos, shortUrl and url&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getCardsByIdCardByField

> getCardsByIdCardByField(idCard, field, key, token)

getCardsByIdCardByField()

### Example

```javascript
import Trello from 'trello';

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let field = "field_example"; // String | field
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.getCardsByIdCardByField(idCard, field, key, token, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
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


## getCardsCheckItemStatesByIdCard

> getCardsCheckItemStatesByIdCard(idCard, key, token, opts)

getCardsCheckItemStatesByIdCard()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'fields': "'all'" // String | all or a comma-separated list of: idCheckItem or state
};
apiInstance.getCardsCheckItemStatesByIdCard(idCard, key, token, opts, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **fields** | **String**| all or a comma-separated list of: idCheckItem or state | [optional] [default to &#39;all&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getCardsChecklistsByIdCard

> getCardsChecklistsByIdCard(idCard, key, token, opts)

getCardsChecklistsByIdCard()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
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
apiInstance.getCardsChecklistsByIdCard(idCard, key, token, opts, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
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


## getCardsListByIdCard

> getCardsListByIdCard(idCard, key, token, opts)

getCardsListByIdCard()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'fields': "'all'" // String | all or a comma-separated list of: closed, idBoard, name, pos or subscribed
};
apiInstance.getCardsListByIdCard(idCard, key, token, opts, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
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


## getCardsListByIdCardByField

> getCardsListByIdCardByField(idCard, field, key, token)

getCardsListByIdCardByField()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let field = "field_example"; // String | field
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.getCardsListByIdCardByField(idCard, field, key, token, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
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


## getCardsMembersByIdCard

> getCardsMembersByIdCard(idCard, key, token, opts)

getCardsMembersByIdCard()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'fields': "'avatarHash, fullName, initials and username'" // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
};
apiInstance.getCardsMembersByIdCard(idCard, key, token, opts, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **fields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to &#39;avatarHash, fullName, initials and username&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getCardsMembersVotedByIdCard

> getCardsMembersVotedByIdCard(idCard, key, token, opts)

getCardsMembersVotedByIdCard()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'fields': "'avatarHash, fullName, initials and username'" // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
};
apiInstance.getCardsMembersVotedByIdCard(idCard, key, token, opts, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **fields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to &#39;avatarHash, fullName, initials and username&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getCardsStickersByIdCard

> getCardsStickersByIdCard(idCard, key, token, opts)

getCardsStickersByIdCard()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'fields': "'all'" // String | all or a comma-separated list of: image, imageScaled, imageUrl, left, rotate, top or zIndex
};
apiInstance.getCardsStickersByIdCard(idCard, key, token, opts, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **fields** | **String**| all or a comma-separated list of: image, imageScaled, imageUrl, left, rotate, top or zIndex | [optional] [default to &#39;all&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getCardsStickersByIdCardByIdSticker

> getCardsStickersByIdCardByIdSticker(idCard, idSticker, key, token, opts)

getCardsStickersByIdCardByIdSticker()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let idSticker = "idSticker_example"; // String | idSticker
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'fields': "'all'" // String | all or a comma-separated list of: image, imageScaled, imageUrl, left, rotate, top or zIndex
};
apiInstance.getCardsStickersByIdCardByIdSticker(idCard, idSticker, key, token, opts, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **idSticker** | **String**| idSticker | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **fields** | **String**| all or a comma-separated list of: image, imageScaled, imageUrl, left, rotate, top or zIndex | [optional] [default to &#39;all&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateCardsActionsCommentsByIdCardByIdAction

> updateCardsActionsCommentsByIdCardByIdAction(idCard, idAction, key, token, cardsActionsComments)

updateCardsActionsCommentsByIdCardByIdAction()

This can only be done by the original author of the comment.

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let idAction = "idAction_example"; // String | idAction
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let cardsActionsComments = new Trello.CardsActionsComments(); // CardsActionsComments | Attributes of \"Cards Actions Comments\" to be updated.
apiInstance.updateCardsActionsCommentsByIdCardByIdAction(idCard, idAction, key, token, cardsActionsComments, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **idAction** | **String**| idAction | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **cardsActionsComments** | [**CardsActionsComments**](CardsActionsComments.md)| Attributes of \&quot;Cards Actions Comments\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateCardsByIdCard

> updateCardsByIdCard(idCard, key, token, cards)

updateCardsByIdCard()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let cards = new Trello.Cards(); // Cards | Attributes of \"Cards\" to be updated.
apiInstance.updateCardsByIdCard(idCard, key, token, cards, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **cards** | [**Cards**](Cards.md)| Attributes of \&quot;Cards\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateCardsChecklistCheckItemByIdCardByIdChecklistCurrentByIdCheckItem

> updateCardsChecklistCheckItemByIdCardByIdChecklistCurrentByIdCheckItem(idCard, idChecklistCurrent, idCheckItem, key, token, cardsChecklistIdChecklistCurrentCheckItem)

updateCardsChecklistCheckItemByIdCardByIdChecklistCurrentByIdCheckItem()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let idChecklistCurrent = "idChecklistCurrent_example"; // String | idChecklistCurrent
let idCheckItem = "idCheckItem_example"; // String | idCheckItem
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let cardsChecklistIdChecklistCurrentCheckItem = new Trello.CardsChecklistIdChecklistCurrentCheckItem(); // CardsChecklistIdChecklistCurrentCheckItem | Attributes of \"Cards Checklist Id Checklist Current Check Item\" to be updated.
apiInstance.updateCardsChecklistCheckItemByIdCardByIdChecklistCurrentByIdCheckItem(idCard, idChecklistCurrent, idCheckItem, key, token, cardsChecklistIdChecklistCurrentCheckItem, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **idChecklistCurrent** | **String**| idChecklistCurrent | 
 **idCheckItem** | **String**| idCheckItem | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **cardsChecklistIdChecklistCurrentCheckItem** | [**CardsChecklistIdChecklistCurrentCheckItem**](CardsChecklistIdChecklistCurrentCheckItem.md)| Attributes of \&quot;Cards Checklist Id Checklist Current Check Item\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateCardsChecklistCheckItemNameByIdCardByIdChecklistByIdCheckItem

> updateCardsChecklistCheckItemNameByIdCardByIdChecklistByIdCheckItem(idCard, idChecklist, idCheckItem, key, token, cardsChecklistCheckItemName)

updateCardsChecklistCheckItemNameByIdCardByIdChecklistByIdCheckItem()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let idChecklist = "idChecklist_example"; // String | idChecklist
let idCheckItem = "idCheckItem_example"; // String | idCheckItem
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let cardsChecklistCheckItemName = new Trello.CardsChecklistCheckItemName(); // CardsChecklistCheckItemName | Attributes of \"Cards Checklist Check Item Name\" to be updated.
apiInstance.updateCardsChecklistCheckItemNameByIdCardByIdChecklistByIdCheckItem(idCard, idChecklist, idCheckItem, key, token, cardsChecklistCheckItemName, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **idChecklist** | **String**| idChecklist | 
 **idCheckItem** | **String**| idCheckItem | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **cardsChecklistCheckItemName** | [**CardsChecklistCheckItemName**](CardsChecklistCheckItemName.md)| Attributes of \&quot;Cards Checklist Check Item Name\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateCardsChecklistCheckItemPosByIdCardByIdChecklistByIdCheckItem

> updateCardsChecklistCheckItemPosByIdCardByIdChecklistByIdCheckItem(idCard, idChecklist, idCheckItem, key, token, cardsChecklistCheckItemPos)

updateCardsChecklistCheckItemPosByIdCardByIdChecklistByIdCheckItem()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let idChecklist = "idChecklist_example"; // String | idChecklist
let idCheckItem = "idCheckItem_example"; // String | idCheckItem
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let cardsChecklistCheckItemPos = new Trello.CardsChecklistCheckItemPos(); // CardsChecklistCheckItemPos | Attributes of \"Cards Checklist Check Item Pos\" to be updated.
apiInstance.updateCardsChecklistCheckItemPosByIdCardByIdChecklistByIdCheckItem(idCard, idChecklist, idCheckItem, key, token, cardsChecklistCheckItemPos, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **idChecklist** | **String**| idChecklist | 
 **idCheckItem** | **String**| idCheckItem | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **cardsChecklistCheckItemPos** | [**CardsChecklistCheckItemPos**](CardsChecklistCheckItemPos.md)| Attributes of \&quot;Cards Checklist Check Item Pos\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateCardsChecklistCheckItemStateByIdCardByIdChecklistByIdCheckItem

> updateCardsChecklistCheckItemStateByIdCardByIdChecklistByIdCheckItem(idCard, idChecklist, idCheckItem, key, token, cardsChecklistCheckItemState)

updateCardsChecklistCheckItemStateByIdCardByIdChecklistByIdCheckItem()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let idChecklist = "idChecklist_example"; // String | idChecklist
let idCheckItem = "idCheckItem_example"; // String | idCheckItem
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let cardsChecklistCheckItemState = new Trello.CardsChecklistCheckItemState(); // CardsChecklistCheckItemState | Attributes of \"Cards Checklist Check Item State\" to be updated.
apiInstance.updateCardsChecklistCheckItemStateByIdCardByIdChecklistByIdCheckItem(idCard, idChecklist, idCheckItem, key, token, cardsChecklistCheckItemState, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **idChecklist** | **String**| idChecklist | 
 **idCheckItem** | **String**| idCheckItem | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **cardsChecklistCheckItemState** | [**CardsChecklistCheckItemState**](CardsChecklistCheckItemState.md)| Attributes of \&quot;Cards Checklist Check Item State\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateCardsClosedByIdCard

> updateCardsClosedByIdCard(idCard, key, token, cardsClosed)

updateCardsClosedByIdCard()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let cardsClosed = new Trello.CardsClosed(); // CardsClosed | Attributes of \"Cards Closed\" to be updated.
apiInstance.updateCardsClosedByIdCard(idCard, key, token, cardsClosed, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **cardsClosed** | [**CardsClosed**](CardsClosed.md)| Attributes of \&quot;Cards Closed\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateCardsDescByIdCard

> updateCardsDescByIdCard(idCard, key, token, cardsDesc)

updateCardsDescByIdCard()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let cardsDesc = new Trello.CardsDesc(); // CardsDesc | Attributes of \"Cards Desc\" to be updated.
apiInstance.updateCardsDescByIdCard(idCard, key, token, cardsDesc, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **cardsDesc** | [**CardsDesc**](CardsDesc.md)| Attributes of \&quot;Cards Desc\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateCardsDueByIdCard

> updateCardsDueByIdCard(idCard, key, token, cardsDue)

updateCardsDueByIdCard()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let cardsDue = new Trello.CardsDue(); // CardsDue | Attributes of \"Cards Due\" to be updated.
apiInstance.updateCardsDueByIdCard(idCard, key, token, cardsDue, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **cardsDue** | [**CardsDue**](CardsDue.md)| Attributes of \&quot;Cards Due\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateCardsIdAttachmentCoverByIdCard

> updateCardsIdAttachmentCoverByIdCard(idCard, key, token, cardsIdAttachmentCover)

updateCardsIdAttachmentCoverByIdCard()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let cardsIdAttachmentCover = new Trello.CardsIdAttachmentCover(); // CardsIdAttachmentCover | Attributes of \"Cards Id Attachment Cover\" to be updated.
apiInstance.updateCardsIdAttachmentCoverByIdCard(idCard, key, token, cardsIdAttachmentCover, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **cardsIdAttachmentCover** | [**CardsIdAttachmentCover**](CardsIdAttachmentCover.md)| Attributes of \&quot;Cards Id Attachment Cover\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateCardsIdBoardByIdCard

> updateCardsIdBoardByIdCard(idCard, key, token, cardsIdBoard)

updateCardsIdBoardByIdCard()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let cardsIdBoard = new Trello.CardsIdBoard(); // CardsIdBoard | Attributes of \"Cards Id Board\" to be updated.
apiInstance.updateCardsIdBoardByIdCard(idCard, key, token, cardsIdBoard, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **cardsIdBoard** | [**CardsIdBoard**](CardsIdBoard.md)| Attributes of \&quot;Cards Id Board\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateCardsIdListByIdCard

> updateCardsIdListByIdCard(idCard, key, token, cardsIdList)

updateCardsIdListByIdCard()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let cardsIdList = new Trello.CardsIdList(); // CardsIdList | Attributes of \"Cards Id List\" to be updated.
apiInstance.updateCardsIdListByIdCard(idCard, key, token, cardsIdList, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **cardsIdList** | [**CardsIdList**](CardsIdList.md)| Attributes of \&quot;Cards Id List\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateCardsIdMembersByIdCard

> updateCardsIdMembersByIdCard(idCard, key, token, cardsIdMembers)

updateCardsIdMembersByIdCard()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let cardsIdMembers = new Trello.CardsIdMembers(); // CardsIdMembers | Attributes of \"Cards Id Members\" to be updated.
apiInstance.updateCardsIdMembersByIdCard(idCard, key, token, cardsIdMembers, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **cardsIdMembers** | [**CardsIdMembers**](CardsIdMembers.md)| Attributes of \&quot;Cards Id Members\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateCardsLabelsByIdCard

> updateCardsLabelsByIdCard(idCard, key, token, cardsLabels)

updateCardsLabelsByIdCard()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let cardsLabels = new Trello.CardsLabels(); // CardsLabels | Attributes of \"Cards Labels\" to be updated.
apiInstance.updateCardsLabelsByIdCard(idCard, key, token, cardsLabels, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **cardsLabels** | [**CardsLabels**](CardsLabels.md)| Attributes of \&quot;Cards Labels\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateCardsNameByIdCard

> updateCardsNameByIdCard(idCard, key, token, cardsName)

updateCardsNameByIdCard()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let cardsName = new Trello.CardsName(); // CardsName | Attributes of \"Cards Name\" to be updated.
apiInstance.updateCardsNameByIdCard(idCard, key, token, cardsName, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **cardsName** | [**CardsName**](CardsName.md)| Attributes of \&quot;Cards Name\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateCardsPosByIdCard

> updateCardsPosByIdCard(idCard, key, token, cardsPos)

updateCardsPosByIdCard()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let cardsPos = new Trello.CardsPos(); // CardsPos | Attributes of \"Cards Pos\" to be updated.
apiInstance.updateCardsPosByIdCard(idCard, key, token, cardsPos, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **cardsPos** | [**CardsPos**](CardsPos.md)| Attributes of \&quot;Cards Pos\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateCardsStickersByIdCardByIdSticker

> updateCardsStickersByIdCardByIdSticker(idCard, idSticker, key, token, cardsStickers)

updateCardsStickersByIdCardByIdSticker()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let idSticker = "idSticker_example"; // String | idSticker
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let cardsStickers = new Trello.CardsStickers(); // CardsStickers | Attributes of \"Cards Stickers\" to be updated.
apiInstance.updateCardsStickersByIdCardByIdSticker(idCard, idSticker, key, token, cardsStickers, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **idSticker** | **String**| idSticker | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **cardsStickers** | [**CardsStickers**](CardsStickers.md)| Attributes of \&quot;Cards Stickers\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateCardsSubscribedByIdCard

> updateCardsSubscribedByIdCard(idCard, key, token, cardsSubscribed)

updateCardsSubscribedByIdCard()

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

let apiInstance = new Trello.CardApi();
let idCard = "idCard_example"; // String | card id or shortlink
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let cardsSubscribed = new Trello.CardsSubscribed(); // CardsSubscribed | Attributes of \"Cards Subscribed\" to be updated.
apiInstance.updateCardsSubscribedByIdCard(idCard, key, token, cardsSubscribed, (error, data, response) => {
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
 **idCard** | **String**| card id or shortlink | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **cardsSubscribed** | [**CardsSubscribed**](CardsSubscribed.md)| Attributes of \&quot;Cards Subscribed\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

