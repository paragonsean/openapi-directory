# SearchApi

All URIs are relative to *https://trello.com/1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSearch**](SearchApi.md#getSearch) | **GET** /search | getSearch() |
| [**getSearchMembers**](SearchApi.md#getSearchMembers) | **GET** /search/members | getSearchMembers() |


<a id="getSearch"></a>
# **getSearch**
> getSearch(query, idOrganizations, key, token, idBoards, idCards, modelTypes, boardFields, boardsLimit, cardFields, cardsLimit, cardsPage, cardBoard, cardList, cardMembers, cardStickers, cardAttachments, organizationFields, organizationsLimit, memberFields, membersLimit, partial)

getSearch()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String query = "query_example"; // String | a string with a length from 1 to 16384
    String idOrganizations = "idOrganizations_example"; // String | A comma-separated list of objectIds, 24-character hex strings
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    String idBoards = "mine"; // String | A comma-separated list of objectIds, 24-character hex strings
    String idCards = "idCards_example"; // String | A comma-separated list of objectIds, 24-character hex strings
    String modelTypes = "all"; // String | all or a comma-separated list of: actions, boards, cards, members or organizations
    String boardFields = "name and idOrganization"; // String | all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url
    String boardsLimit = "10"; // String | a number from 1 to 1000
    String cardFields = "all"; // String | all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url
    String cardsLimit = "10"; // String | a number from 1 to 1000
    String cardsPage = "0"; // String | a number from 0 to 100
    String cardBoard = "cardBoard_example"; // String |  true or false
    String cardList = "cardList_example"; // String |  true or false
    String cardMembers = "cardMembers_example"; // String |  true or false
    String cardStickers = "cardStickers_example"; // String |  true or false
    String cardAttachments = "cardAttachments_example"; // String | A boolean value or &quot;cover&quot; for only card cover attachments
    String organizationFields = "name and displayName"; // String | all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website
    String organizationsLimit = "10"; // String | a number from 1 to 1000
    String memberFields = "avatarHash, fullName, initials, username and confirmed"; // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
    String membersLimit = "10"; // String | a number from 1 to 1000
    String partial = "partial_example"; // String |  true or false
    try {
      apiInstance.getSearch(query, idOrganizations, key, token, idBoards, idCards, modelTypes, boardFields, boardsLimit, cardFields, cardsLimit, cardsPage, cardBoard, cardList, cardMembers, cardStickers, cardAttachments, organizationFields, organizationsLimit, memberFields, membersLimit, partial);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#getSearch");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **query** | **String**| a string with a length from 1 to 16384 | |
| **idOrganizations** | **String**| A comma-separated list of objectIds, 24-character hex strings | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **idBoards** | **String**| A comma-separated list of objectIds, 24-character hex strings | [optional] [default to mine] |
| **idCards** | **String**| A comma-separated list of objectIds, 24-character hex strings | [optional] |
| **modelTypes** | **String**| all or a comma-separated list of: actions, boards, cards, members or organizations | [optional] [default to all] |
| **boardFields** | **String**| all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url | [optional] [default to name and idOrganization] |
| **boardsLimit** | **String**| a number from 1 to 1000 | [optional] [default to 10] |
| **cardFields** | **String**| all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url | [optional] [default to all] |
| **cardsLimit** | **String**| a number from 1 to 1000 | [optional] [default to 10] |
| **cardsPage** | **String**| a number from 0 to 100 | [optional] [default to 0] |
| **cardBoard** | **String**|  true or false | [optional] |
| **cardList** | **String**|  true or false | [optional] |
| **cardMembers** | **String**|  true or false | [optional] |
| **cardStickers** | **String**|  true or false | [optional] |
| **cardAttachments** | **String**| A boolean value or &amp;quot;cover&amp;quot; for only card cover attachments | [optional] |
| **organizationFields** | **String**| all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website | [optional] [default to name and displayName] |
| **organizationsLimit** | **String**| a number from 1 to 1000 | [optional] [default to 10] |
| **memberFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to avatarHash, fullName, initials, username and confirmed] |
| **membersLimit** | **String**| a number from 1 to 1000 | [optional] [default to 10] |
| **partial** | **String**|  true or false | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="getSearchMembers"></a>
# **getSearchMembers**
> getSearchMembers(query, key, token, limit, idBoard, idOrganization, onlyOrgMembers)

getSearchMembers()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String query = "query_example"; // String | a string with a length from 1 to 16384
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    String limit = "8"; // String | a number from 1 to 20
    String idBoard = "idBoard_example"; // String | An id, or null
    String idOrganization = "idOrganization_example"; // String | An id, or null
    String onlyOrgMembers = "onlyOrgMembers_example"; // String | A boolean
    try {
      apiInstance.getSearchMembers(query, key, token, limit, idBoard, idOrganization, onlyOrgMembers);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#getSearchMembers");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **query** | **String**| a string with a length from 1 to 16384 | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **limit** | **String**| a number from 1 to 20 | [optional] [default to 8] |
| **idBoard** | **String**| An id, or null | [optional] |
| **idOrganization** | **String**| An id, or null | [optional] |
| **onlyOrgMembers** | **String**| A boolean | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

