# Trello.SearchApi

All URIs are relative to *https://trello.com/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSearch**](SearchApi.md#getSearch) | **GET** /search | getSearch()
[**getSearchMembers**](SearchApi.md#getSearchMembers) | **GET** /search/members | getSearchMembers()



## getSearch

> getSearch(query, idOrganizations, key, token, opts)

getSearch()

### Example

```javascript
import Trello from 'trello';

let apiInstance = new Trello.SearchApi();
let query = "query_example"; // String | a string with a length from 1 to 16384
let idOrganizations = "idOrganizations_example"; // String | A comma-separated list of objectIds, 24-character hex strings
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'idBoards': "'mine'", // String | A comma-separated list of objectIds, 24-character hex strings
  'idCards': "idCards_example", // String | A comma-separated list of objectIds, 24-character hex strings
  'modelTypes': "'all'", // String | all or a comma-separated list of: actions, boards, cards, members or organizations
  'boardFields': "'name and idOrganization'", // String | all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url
  'boardsLimit': "'10'", // String | a number from 1 to 1000
  'cardFields': "'all'", // String | all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url
  'cardsLimit': "'10'", // String | a number from 1 to 1000
  'cardsPage': "'0'", // String | a number from 0 to 100
  'cardBoard': "cardBoard_example", // String |  true or false
  'cardList': "cardList_example", // String |  true or false
  'cardMembers': "cardMembers_example", // String |  true or false
  'cardStickers': "cardStickers_example", // String |  true or false
  'cardAttachments': "cardAttachments_example", // String | A boolean value or &quot;cover&quot; for only card cover attachments
  'organizationFields': "'name and displayName'", // String | all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website
  'organizationsLimit': "'10'", // String | a number from 1 to 1000
  'memberFields': "'avatarHash, fullName, initials, username and confirmed'", // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
  'membersLimit': "'10'", // String | a number from 1 to 1000
  'partial': "partial_example" // String |  true or false
};
apiInstance.getSearch(query, idOrganizations, key, token, opts, (error, data, response) => {
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
 **query** | **String**| a string with a length from 1 to 16384 | 
 **idOrganizations** | **String**| A comma-separated list of objectIds, 24-character hex strings | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **idBoards** | **String**| A comma-separated list of objectIds, 24-character hex strings | [optional] [default to &#39;mine&#39;]
 **idCards** | **String**| A comma-separated list of objectIds, 24-character hex strings | [optional] 
 **modelTypes** | **String**| all or a comma-separated list of: actions, boards, cards, members or organizations | [optional] [default to &#39;all&#39;]
 **boardFields** | **String**| all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url | [optional] [default to &#39;name and idOrganization&#39;]
 **boardsLimit** | **String**| a number from 1 to 1000 | [optional] [default to &#39;10&#39;]
 **cardFields** | **String**| all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url | [optional] [default to &#39;all&#39;]
 **cardsLimit** | **String**| a number from 1 to 1000 | [optional] [default to &#39;10&#39;]
 **cardsPage** | **String**| a number from 0 to 100 | [optional] [default to &#39;0&#39;]
 **cardBoard** | **String**|  true or false | [optional] 
 **cardList** | **String**|  true or false | [optional] 
 **cardMembers** | **String**|  true or false | [optional] 
 **cardStickers** | **String**|  true or false | [optional] 
 **cardAttachments** | **String**| A boolean value or &amp;quot;cover&amp;quot; for only card cover attachments | [optional] 
 **organizationFields** | **String**| all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website | [optional] [default to &#39;name and displayName&#39;]
 **organizationsLimit** | **String**| a number from 1 to 1000 | [optional] [default to &#39;10&#39;]
 **memberFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to &#39;avatarHash, fullName, initials, username and confirmed&#39;]
 **membersLimit** | **String**| a number from 1 to 1000 | [optional] [default to &#39;10&#39;]
 **partial** | **String**|  true or false | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getSearchMembers

> getSearchMembers(query, key, token, opts)

getSearchMembers()

### Example

```javascript
import Trello from 'trello';

let apiInstance = new Trello.SearchApi();
let query = "query_example"; // String | a string with a length from 1 to 16384
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'limit': "'8'", // String | a number from 1 to 20
  'idBoard': "idBoard_example", // String | An id, or null
  'idOrganization': "idOrganization_example", // String | An id, or null
  'onlyOrgMembers': "onlyOrgMembers_example" // String | A boolean
};
apiInstance.getSearchMembers(query, key, token, opts, (error, data, response) => {
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
 **query** | **String**| a string with a length from 1 to 16384 | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **limit** | **String**| a number from 1 to 20 | [optional] [default to &#39;8&#39;]
 **idBoard** | **String**| An id, or null | [optional] 
 **idOrganization** | **String**| An id, or null | [optional] 
 **onlyOrgMembers** | **String**| A boolean | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

