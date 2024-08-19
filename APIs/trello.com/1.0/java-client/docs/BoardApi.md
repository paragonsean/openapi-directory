# BoardApi

All URIs are relative to *https://trello.com/1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addBoards**](BoardApi.md#addBoards) | **POST** /boards | addBoards() |
| [**addBoardsCalendarKeyGenerateByIdBoard**](BoardApi.md#addBoardsCalendarKeyGenerateByIdBoard) | **POST** /boards/{idBoard}/calendarKey/generate | addBoardsCalendarKeyGenerateByIdBoard() |
| [**addBoardsChecklistsByIdBoard**](BoardApi.md#addBoardsChecklistsByIdBoard) | **POST** /boards/{idBoard}/checklists | addBoardsChecklistsByIdBoard() |
| [**addBoardsEmailKeyGenerateByIdBoard**](BoardApi.md#addBoardsEmailKeyGenerateByIdBoard) | **POST** /boards/{idBoard}/emailKey/generate | addBoardsEmailKeyGenerateByIdBoard() |
| [**addBoardsLabelsByIdBoard**](BoardApi.md#addBoardsLabelsByIdBoard) | **POST** /boards/{idBoard}/labels | addBoardsLabelsByIdBoard() |
| [**addBoardsListsByIdBoard**](BoardApi.md#addBoardsListsByIdBoard) | **POST** /boards/{idBoard}/lists | addBoardsListsByIdBoard() |
| [**addBoardsMarkAsViewedByIdBoard**](BoardApi.md#addBoardsMarkAsViewedByIdBoard) | **POST** /boards/{idBoard}/markAsViewed | addBoardsMarkAsViewedByIdBoard() |
| [**addBoardsPowerUpsByIdBoard**](BoardApi.md#addBoardsPowerUpsByIdBoard) | **POST** /boards/{idBoard}/powerUps | addBoardsPowerUpsByIdBoard() |
| [**deleteBoardsMembersByIdBoardByIdMember**](BoardApi.md#deleteBoardsMembersByIdBoardByIdMember) | **DELETE** /boards/{idBoard}/members/{idMember} | deleteBoardsMembersByIdBoardByIdMember() |
| [**deleteBoardsPowerUpsByIdBoardByPowerUp**](BoardApi.md#deleteBoardsPowerUpsByIdBoardByPowerUp) | **DELETE** /boards/{idBoard}/powerUps/{powerUp} | deleteBoardsPowerUpsByIdBoardByPowerUp() |
| [**getBoardsActionsByIdBoard**](BoardApi.md#getBoardsActionsByIdBoard) | **GET** /boards/{idBoard}/actions | getBoardsActionsByIdBoard() |
| [**getBoardsBoardStarsByIdBoard**](BoardApi.md#getBoardsBoardStarsByIdBoard) | **GET** /boards/{idBoard}/boardStars | getBoardsBoardStarsByIdBoard() |
| [**getBoardsByIdBoard**](BoardApi.md#getBoardsByIdBoard) | **GET** /boards/{idBoard} | getBoardsByIdBoard() |
| [**getBoardsByIdBoardByField**](BoardApi.md#getBoardsByIdBoardByField) | **GET** /boards/{idBoard}/{field} | getBoardsByIdBoardByField() |
| [**getBoardsCardsByIdBoard**](BoardApi.md#getBoardsCardsByIdBoard) | **GET** /boards/{idBoard}/cards | getBoardsCardsByIdBoard() |
| [**getBoardsCardsByIdBoardByFilter**](BoardApi.md#getBoardsCardsByIdBoardByFilter) | **GET** /boards/{idBoard}/cards/{filter} | getBoardsCardsByIdBoardByFilter() |
| [**getBoardsCardsByIdBoardByIdCard**](BoardApi.md#getBoardsCardsByIdBoardByIdCard) | **GET** /boards/{idBoard}/cards/{idCard} | getBoardsCardsByIdBoardByIdCard() |
| [**getBoardsChecklistsByIdBoard**](BoardApi.md#getBoardsChecklistsByIdBoard) | **GET** /boards/{idBoard}/checklists | getBoardsChecklistsByIdBoard() |
| [**getBoardsDeltasByIdBoard**](BoardApi.md#getBoardsDeltasByIdBoard) | **GET** /boards/{idBoard}/deltas | getBoardsDeltasByIdBoard() |
| [**getBoardsLabelsByIdBoard**](BoardApi.md#getBoardsLabelsByIdBoard) | **GET** /boards/{idBoard}/labels | getBoardsLabelsByIdBoard() |
| [**getBoardsLabelsByIdBoardByIdLabel**](BoardApi.md#getBoardsLabelsByIdBoardByIdLabel) | **GET** /boards/{idBoard}/labels/{idLabel} | getBoardsLabelsByIdBoardByIdLabel() |
| [**getBoardsListsByIdBoard**](BoardApi.md#getBoardsListsByIdBoard) | **GET** /boards/{idBoard}/lists | getBoardsListsByIdBoard() |
| [**getBoardsListsByIdBoardByFilter**](BoardApi.md#getBoardsListsByIdBoardByFilter) | **GET** /boards/{idBoard}/lists/{filter} | getBoardsListsByIdBoardByFilter() |
| [**getBoardsMembersByIdBoard**](BoardApi.md#getBoardsMembersByIdBoard) | **GET** /boards/{idBoard}/members | getBoardsMembersByIdBoard() |
| [**getBoardsMembersByIdBoardByFilter**](BoardApi.md#getBoardsMembersByIdBoardByFilter) | **GET** /boards/{idBoard}/members/{filter} | getBoardsMembersByIdBoardByFilter() |
| [**getBoardsMembersCardsByIdBoardByIdMember**](BoardApi.md#getBoardsMembersCardsByIdBoardByIdMember) | **GET** /boards/{idBoard}/members/{idMember}/cards | getBoardsMembersCardsByIdBoardByIdMember() |
| [**getBoardsMembersInvitedByIdBoard**](BoardApi.md#getBoardsMembersInvitedByIdBoard) | **GET** /boards/{idBoard}/membersInvited | getBoardsMembersInvitedByIdBoard() |
| [**getBoardsMembersInvitedByIdBoardByField**](BoardApi.md#getBoardsMembersInvitedByIdBoardByField) | **GET** /boards/{idBoard}/membersInvited/{field} | getBoardsMembersInvitedByIdBoardByField() |
| [**getBoardsMembershipsByIdBoard**](BoardApi.md#getBoardsMembershipsByIdBoard) | **GET** /boards/{idBoard}/memberships | getBoardsMembershipsByIdBoard() |
| [**getBoardsMembershipsByIdBoardByIdMembership**](BoardApi.md#getBoardsMembershipsByIdBoardByIdMembership) | **GET** /boards/{idBoard}/memberships/{idMembership} | getBoardsMembershipsByIdBoardByIdMembership() |
| [**getBoardsMyPrefsByIdBoard**](BoardApi.md#getBoardsMyPrefsByIdBoard) | **GET** /boards/{idBoard}/myPrefs | getBoardsMyPrefsByIdBoard() |
| [**getBoardsOrganizationByIdBoard**](BoardApi.md#getBoardsOrganizationByIdBoard) | **GET** /boards/{idBoard}/organization | getBoardsOrganizationByIdBoard() |
| [**getBoardsOrganizationByIdBoardByField**](BoardApi.md#getBoardsOrganizationByIdBoardByField) | **GET** /boards/{idBoard}/organization/{field} | getBoardsOrganizationByIdBoardByField() |
| [**updateBoardsByIdBoard**](BoardApi.md#updateBoardsByIdBoard) | **PUT** /boards/{idBoard} | updateBoardsByIdBoard() |
| [**updateBoardsClosedByIdBoard**](BoardApi.md#updateBoardsClosedByIdBoard) | **PUT** /boards/{idBoard}/closed | updateBoardsClosedByIdBoard() |
| [**updateBoardsDescByIdBoard**](BoardApi.md#updateBoardsDescByIdBoard) | **PUT** /boards/{idBoard}/desc | updateBoardsDescByIdBoard() |
| [**updateBoardsIdOrganizationByIdBoard**](BoardApi.md#updateBoardsIdOrganizationByIdBoard) | **PUT** /boards/{idBoard}/idOrganization | updateBoardsIdOrganizationByIdBoard() |
| [**updateBoardsLabelNamesBlueByIdBoard**](BoardApi.md#updateBoardsLabelNamesBlueByIdBoard) | **PUT** /boards/{idBoard}/labelNames/blue | updateBoardsLabelNamesBlueByIdBoard() |
| [**updateBoardsLabelNamesGreenByIdBoard**](BoardApi.md#updateBoardsLabelNamesGreenByIdBoard) | **PUT** /boards/{idBoard}/labelNames/green | updateBoardsLabelNamesGreenByIdBoard() |
| [**updateBoardsLabelNamesOrangeByIdBoard**](BoardApi.md#updateBoardsLabelNamesOrangeByIdBoard) | **PUT** /boards/{idBoard}/labelNames/orange | updateBoardsLabelNamesOrangeByIdBoard() |
| [**updateBoardsLabelNamesPurpleByIdBoard**](BoardApi.md#updateBoardsLabelNamesPurpleByIdBoard) | **PUT** /boards/{idBoard}/labelNames/purple | updateBoardsLabelNamesPurpleByIdBoard() |
| [**updateBoardsLabelNamesRedByIdBoard**](BoardApi.md#updateBoardsLabelNamesRedByIdBoard) | **PUT** /boards/{idBoard}/labelNames/red | updateBoardsLabelNamesRedByIdBoard() |
| [**updateBoardsLabelNamesYellowByIdBoard**](BoardApi.md#updateBoardsLabelNamesYellowByIdBoard) | **PUT** /boards/{idBoard}/labelNames/yellow | updateBoardsLabelNamesYellowByIdBoard() |
| [**updateBoardsMembersByIdBoard**](BoardApi.md#updateBoardsMembersByIdBoard) | **PUT** /boards/{idBoard}/members | updateBoardsMembersByIdBoard() |
| [**updateBoardsMembersByIdBoardByIdMember**](BoardApi.md#updateBoardsMembersByIdBoardByIdMember) | **PUT** /boards/{idBoard}/members/{idMember} | updateBoardsMembersByIdBoardByIdMember() |
| [**updateBoardsMembershipsByIdBoardByIdMembership**](BoardApi.md#updateBoardsMembershipsByIdBoardByIdMembership) | **PUT** /boards/{idBoard}/memberships/{idMembership} | updateBoardsMembershipsByIdBoardByIdMembership() |
| [**updateBoardsMyPrefsEmailPositionByIdBoard**](BoardApi.md#updateBoardsMyPrefsEmailPositionByIdBoard) | **PUT** /boards/{idBoard}/myPrefs/emailPosition | updateBoardsMyPrefsEmailPositionByIdBoard() |
| [**updateBoardsMyPrefsIdEmailListByIdBoard**](BoardApi.md#updateBoardsMyPrefsIdEmailListByIdBoard) | **PUT** /boards/{idBoard}/myPrefs/idEmailList | updateBoardsMyPrefsIdEmailListByIdBoard() |
| [**updateBoardsMyPrefsShowListGuideByIdBoard**](BoardApi.md#updateBoardsMyPrefsShowListGuideByIdBoard) | **PUT** /boards/{idBoard}/myPrefs/showListGuide | updateBoardsMyPrefsShowListGuideByIdBoard() |
| [**updateBoardsMyPrefsShowSidebarActivityByIdBoard**](BoardApi.md#updateBoardsMyPrefsShowSidebarActivityByIdBoard) | **PUT** /boards/{idBoard}/myPrefs/showSidebarActivity | updateBoardsMyPrefsShowSidebarActivityByIdBoard() |
| [**updateBoardsMyPrefsShowSidebarBoardActionsByIdBoard**](BoardApi.md#updateBoardsMyPrefsShowSidebarBoardActionsByIdBoard) | **PUT** /boards/{idBoard}/myPrefs/showSidebarBoardActions | updateBoardsMyPrefsShowSidebarBoardActionsByIdBoard() |
| [**updateBoardsMyPrefsShowSidebarByIdBoard**](BoardApi.md#updateBoardsMyPrefsShowSidebarByIdBoard) | **PUT** /boards/{idBoard}/myPrefs/showSidebar | updateBoardsMyPrefsShowSidebarByIdBoard() |
| [**updateBoardsMyPrefsShowSidebarMembersByIdBoard**](BoardApi.md#updateBoardsMyPrefsShowSidebarMembersByIdBoard) | **PUT** /boards/{idBoard}/myPrefs/showSidebarMembers | updateBoardsMyPrefsShowSidebarMembersByIdBoard() |
| [**updateBoardsNameByIdBoard**](BoardApi.md#updateBoardsNameByIdBoard) | **PUT** /boards/{idBoard}/name | updateBoardsNameByIdBoard() |
| [**updateBoardsPrefsBackgroundByIdBoard**](BoardApi.md#updateBoardsPrefsBackgroundByIdBoard) | **PUT** /boards/{idBoard}/prefs/background | updateBoardsPrefsBackgroundByIdBoard() |
| [**updateBoardsPrefsCalendarFeedEnabledByIdBoard**](BoardApi.md#updateBoardsPrefsCalendarFeedEnabledByIdBoard) | **PUT** /boards/{idBoard}/prefs/calendarFeedEnabled | updateBoardsPrefsCalendarFeedEnabledByIdBoard() |
| [**updateBoardsPrefsCardAgingByIdBoard**](BoardApi.md#updateBoardsPrefsCardAgingByIdBoard) | **PUT** /boards/{idBoard}/prefs/cardAging | updateBoardsPrefsCardAgingByIdBoard() |
| [**updateBoardsPrefsCardCoversByIdBoard**](BoardApi.md#updateBoardsPrefsCardCoversByIdBoard) | **PUT** /boards/{idBoard}/prefs/cardCovers | updateBoardsPrefsCardCoversByIdBoard() |
| [**updateBoardsPrefsCommentsByIdBoard**](BoardApi.md#updateBoardsPrefsCommentsByIdBoard) | **PUT** /boards/{idBoard}/prefs/comments | updateBoardsPrefsCommentsByIdBoard() |
| [**updateBoardsPrefsInvitationsByIdBoard**](BoardApi.md#updateBoardsPrefsInvitationsByIdBoard) | **PUT** /boards/{idBoard}/prefs/invitations | updateBoardsPrefsInvitationsByIdBoard() |
| [**updateBoardsPrefsPermissionLevelByIdBoard**](BoardApi.md#updateBoardsPrefsPermissionLevelByIdBoard) | **PUT** /boards/{idBoard}/prefs/permissionLevel | updateBoardsPrefsPermissionLevelByIdBoard() |
| [**updateBoardsPrefsSelfJoinByIdBoard**](BoardApi.md#updateBoardsPrefsSelfJoinByIdBoard) | **PUT** /boards/{idBoard}/prefs/selfJoin | updateBoardsPrefsSelfJoinByIdBoard() |
| [**updateBoardsPrefsVotingByIdBoard**](BoardApi.md#updateBoardsPrefsVotingByIdBoard) | **PUT** /boards/{idBoard}/prefs/voting | updateBoardsPrefsVotingByIdBoard() |
| [**updateBoardsSubscribedByIdBoard**](BoardApi.md#updateBoardsSubscribedByIdBoard) | **PUT** /boards/{idBoard}/subscribed | updateBoardsSubscribedByIdBoard() |


<a id="addBoards"></a>
# **addBoards**
> addBoards(key, token, boards)

addBoards()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    Boards boards = new Boards(); // Boards | Attributes of \"Boards\" to be added.
    try {
      apiInstance.addBoards(key, token, boards);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#addBoards");
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
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **boards** | [**Boards**](Boards.md)| Attributes of \&quot;Boards\&quot; to be added. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="addBoardsCalendarKeyGenerateByIdBoard"></a>
# **addBoardsCalendarKeyGenerateByIdBoard**
> addBoardsCalendarKeyGenerateByIdBoard(idBoard, key, token)

addBoardsCalendarKeyGenerateByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    try {
      apiInstance.addBoardsCalendarKeyGenerateByIdBoard(idBoard, key, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#addBoardsCalendarKeyGenerateByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="addBoardsChecklistsByIdBoard"></a>
# **addBoardsChecklistsByIdBoard**
> addBoardsChecklistsByIdBoard(idBoard, key, token, boardsChecklists)

addBoardsChecklistsByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    BoardsChecklists boardsChecklists = new BoardsChecklists(); // BoardsChecklists | Attributes of \"Boards Checklists\" to be added.
    try {
      apiInstance.addBoardsChecklistsByIdBoard(idBoard, key, token, boardsChecklists);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#addBoardsChecklistsByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **boardsChecklists** | [**BoardsChecklists**](BoardsChecklists.md)| Attributes of \&quot;Boards Checklists\&quot; to be added. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="addBoardsEmailKeyGenerateByIdBoard"></a>
# **addBoardsEmailKeyGenerateByIdBoard**
> addBoardsEmailKeyGenerateByIdBoard(idBoard, key, token)

addBoardsEmailKeyGenerateByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    try {
      apiInstance.addBoardsEmailKeyGenerateByIdBoard(idBoard, key, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#addBoardsEmailKeyGenerateByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="addBoardsLabelsByIdBoard"></a>
# **addBoardsLabelsByIdBoard**
> addBoardsLabelsByIdBoard(idBoard, key, token, boardsLabels)

addBoardsLabelsByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    BoardsLabels boardsLabels = new BoardsLabels(); // BoardsLabels | Attributes of \"Boards Labels\" to be added.
    try {
      apiInstance.addBoardsLabelsByIdBoard(idBoard, key, token, boardsLabels);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#addBoardsLabelsByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **boardsLabels** | [**BoardsLabels**](BoardsLabels.md)| Attributes of \&quot;Boards Labels\&quot; to be added. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="addBoardsListsByIdBoard"></a>
# **addBoardsListsByIdBoard**
> addBoardsListsByIdBoard(idBoard, key, token, boardsLists)

addBoardsListsByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    BoardsLists boardsLists = new BoardsLists(); // BoardsLists | Attributes of \"Boards Lists\" to be added.
    try {
      apiInstance.addBoardsListsByIdBoard(idBoard, key, token, boardsLists);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#addBoardsListsByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **boardsLists** | [**BoardsLists**](BoardsLists.md)| Attributes of \&quot;Boards Lists\&quot; to be added. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="addBoardsMarkAsViewedByIdBoard"></a>
# **addBoardsMarkAsViewedByIdBoard**
> addBoardsMarkAsViewedByIdBoard(idBoard, key, token)

addBoardsMarkAsViewedByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    try {
      apiInstance.addBoardsMarkAsViewedByIdBoard(idBoard, key, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#addBoardsMarkAsViewedByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="addBoardsPowerUpsByIdBoard"></a>
# **addBoardsPowerUpsByIdBoard**
> addBoardsPowerUpsByIdBoard(idBoard, key, token, boardsPowerUps)

addBoardsPowerUpsByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    BoardsPowerUps boardsPowerUps = new BoardsPowerUps(); // BoardsPowerUps | Attributes of \"Boards Power Ups\" to be added.
    try {
      apiInstance.addBoardsPowerUpsByIdBoard(idBoard, key, token, boardsPowerUps);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#addBoardsPowerUpsByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **boardsPowerUps** | [**BoardsPowerUps**](BoardsPowerUps.md)| Attributes of \&quot;Boards Power Ups\&quot; to be added. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="deleteBoardsMembersByIdBoardByIdMember"></a>
# **deleteBoardsMembersByIdBoardByIdMember**
> deleteBoardsMembersByIdBoardByIdMember(idBoard, idMember, key, token)

deleteBoardsMembersByIdBoardByIdMember()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String idMember = "idMember_example"; // String | idMember
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    try {
      apiInstance.deleteBoardsMembersByIdBoardByIdMember(idBoard, idMember, key, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#deleteBoardsMembersByIdBoardByIdMember");
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
| **idBoard** | **String**| board_id | |
| **idMember** | **String**| idMember | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="deleteBoardsPowerUpsByIdBoardByPowerUp"></a>
# **deleteBoardsPowerUpsByIdBoardByPowerUp**
> deleteBoardsPowerUpsByIdBoardByPowerUp(idBoard, powerUp, key, token)

deleteBoardsPowerUpsByIdBoardByPowerUp()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String powerUp = "powerUp_example"; // String | powerUp
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    try {
      apiInstance.deleteBoardsPowerUpsByIdBoardByPowerUp(idBoard, powerUp, key, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#deleteBoardsPowerUpsByIdBoardByPowerUp");
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
| **idBoard** | **String**| board_id | |
| **powerUp** | **String**| powerUp | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="getBoardsActionsByIdBoard"></a>
# **getBoardsActionsByIdBoard**
> getBoardsActionsByIdBoard(idBoard, key, token, entities, display, filter, fields, limit, format, since, before, page, idModels, member, memberFields, memberCreator, memberCreatorFields)

getBoardsActionsByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    String entities = "entities_example"; // String |  true or false
    String display = "display_example"; // String |  true or false
    String filter = "all"; // String | all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization
    String fields = "all"; // String | all or a comma-separated list of: data, date, idMemberCreator or type
    String limit = "50"; // String | a number from 0 to 1000
    String format = "list"; // String | One of: count, list or minimal
    String since = "since_example"; // String | A date, null or lastView
    String before = "before_example"; // String | A date, or null
    String page = "0"; // String | Page * limit must be less than 1000
    String idModels = "idModels_example"; // String | Only return actions related to these model ids
    String member = "member_example"; // String |  true or false
    String memberFields = "avatarHash, fullName, initials and username"; // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
    String memberCreator = "memberCreator_example"; // String |  true or false
    String memberCreatorFields = "avatarHash, fullName, initials and username"; // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
    try {
      apiInstance.getBoardsActionsByIdBoard(idBoard, key, token, entities, display, filter, fields, limit, format, since, before, page, idModels, member, memberFields, memberCreator, memberCreatorFields);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#getBoardsActionsByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **entities** | **String**|  true or false | [optional] |
| **display** | **String**|  true or false | [optional] |
| **filter** | **String**| all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization | [optional] [default to all] |
| **fields** | **String**| all or a comma-separated list of: data, date, idMemberCreator or type | [optional] [default to all] |
| **limit** | **String**| a number from 0 to 1000 | [optional] [default to 50] |
| **format** | **String**| One of: count, list or minimal | [optional] [default to list] |
| **since** | **String**| A date, null or lastView | [optional] |
| **before** | **String**| A date, or null | [optional] |
| **page** | **String**| Page * limit must be less than 1000 | [optional] [default to 0] |
| **idModels** | **String**| Only return actions related to these model ids | [optional] |
| **member** | **String**|  true or false | [optional] |
| **memberFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to avatarHash, fullName, initials and username] |
| **memberCreator** | **String**|  true or false | [optional] |
| **memberCreatorFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to avatarHash, fullName, initials and username] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="getBoardsBoardStarsByIdBoard"></a>
# **getBoardsBoardStarsByIdBoard**
> getBoardsBoardStarsByIdBoard(idBoard, key, token, filter)

getBoardsBoardStarsByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    String filter = "mine"; // String | One of: mine or none
    try {
      apiInstance.getBoardsBoardStarsByIdBoard(idBoard, key, token, filter);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#getBoardsBoardStarsByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **filter** | **String**| One of: mine or none | [optional] [default to mine] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="getBoardsByIdBoard"></a>
# **getBoardsByIdBoard**
> getBoardsByIdBoard(idBoard, key, token, actions, actionsEntities, actionsDisplay, actionsFormat, actionsSince, actionsLimit, actionFields, actionMember, actionMemberFields, actionMemberCreator, actionMemberCreatorFields, cards, cardFields, cardAttachments, cardAttachmentFields, cardChecklists, cardStickers, boardStars, labels, labelFields, labelsLimit, lists, listFields, memberships, membershipsMember, membershipsMemberFields, members, memberFields, membersInvited, membersInvitedFields, checklists, checklistFields, organization, organizationFields, organizationMemberships, myPrefs, fields)

getBoardsByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    String actions = "actions_example"; // String | all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization
    String actionsEntities = "actionsEntities_example"; // String |  true or false
    String actionsDisplay = "actionsDisplay_example"; // String |  true or false
    String actionsFormat = "list"; // String | One of: count, list or minimal
    String actionsSince = "actionsSince_example"; // String | A date, null or lastView
    String actionsLimit = "50"; // String | a number from 0 to 1000
    String actionFields = "all"; // String | all or a comma-separated list of: data, date, idMemberCreator or type
    String actionMember = "actionMember_example"; // String |  true or false
    String actionMemberFields = "avatarHash, fullName, initials and username"; // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
    String actionMemberCreator = "actionMemberCreator_example"; // String |  true or false
    String actionMemberCreatorFields = "avatarHash, fullName, initials and username"; // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
    String cards = "none"; // String | One of: all, closed, none, open or visible
    String cardFields = "all"; // String | all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url
    String cardAttachments = "cardAttachments_example"; // String | A boolean value or &quot;cover&quot; for only card cover attachments
    String cardAttachmentFields = "all"; // String | all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url
    String cardChecklists = "none"; // String | One of: all or none
    String cardStickers = "cardStickers_example"; // String |  true or false
    String boardStars = "none"; // String | One of: mine or none
    String labels = "none"; // String | One of: all or none
    String labelFields = "all"; // String | all or a comma-separated list of: color, idBoard, name or uses
    String labelsLimit = "50"; // String | a number from 0 to 1000
    String lists = "none"; // String | One of: all, closed, none or open
    String listFields = "all"; // String | all or a comma-separated list of: closed, idBoard, name, pos or subscribed
    String memberships = "none"; // String | all or a comma-separated list of: active, admin, deactivated, me or normal
    String membershipsMember = "membershipsMember_example"; // String |  true or false
    String membershipsMemberFields = "fullName and username"; // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
    String members = "none"; // String | One of: admins, all, none, normal or owners
    String memberFields = "avatarHash, initials, fullName, username and confirmed"; // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
    String membersInvited = "none"; // String | One of: admins, all, none, normal or owners
    String membersInvitedFields = "avatarHash, initials, fullName and username"; // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
    String checklists = "none"; // String | One of: all or none
    String checklistFields = "all"; // String | all or a comma-separated list of: idBoard, idCard, name or pos
    String organization = "organization_example"; // String |  true or false
    String organizationFields = "name and displayName"; // String | all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website
    String organizationMemberships = "none"; // String | all or a comma-separated list of: active, admin, deactivated, me or normal
    String myPrefs = "myPrefs_example"; // String |  true or false
    String fields = "name, desc, descData, closed, idOrganization, pinned, url, shortUrl, prefs and labelNames"; // String | all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url
    try {
      apiInstance.getBoardsByIdBoard(idBoard, key, token, actions, actionsEntities, actionsDisplay, actionsFormat, actionsSince, actionsLimit, actionFields, actionMember, actionMemberFields, actionMemberCreator, actionMemberCreatorFields, cards, cardFields, cardAttachments, cardAttachmentFields, cardChecklists, cardStickers, boardStars, labels, labelFields, labelsLimit, lists, listFields, memberships, membershipsMember, membershipsMemberFields, members, memberFields, membersInvited, membersInvitedFields, checklists, checklistFields, organization, organizationFields, organizationMemberships, myPrefs, fields);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#getBoardsByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **actions** | **String**| all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization | [optional] |
| **actionsEntities** | **String**|  true or false | [optional] |
| **actionsDisplay** | **String**|  true or false | [optional] |
| **actionsFormat** | **String**| One of: count, list or minimal | [optional] [default to list] |
| **actionsSince** | **String**| A date, null or lastView | [optional] |
| **actionsLimit** | **String**| a number from 0 to 1000 | [optional] [default to 50] |
| **actionFields** | **String**| all or a comma-separated list of: data, date, idMemberCreator or type | [optional] [default to all] |
| **actionMember** | **String**|  true or false | [optional] |
| **actionMemberFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to avatarHash, fullName, initials and username] |
| **actionMemberCreator** | **String**|  true or false | [optional] |
| **actionMemberCreatorFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to avatarHash, fullName, initials and username] |
| **cards** | **String**| One of: all, closed, none, open or visible | [optional] [default to none] |
| **cardFields** | **String**| all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url | [optional] [default to all] |
| **cardAttachments** | **String**| A boolean value or &amp;quot;cover&amp;quot; for only card cover attachments | [optional] |
| **cardAttachmentFields** | **String**| all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url | [optional] [default to all] |
| **cardChecklists** | **String**| One of: all or none | [optional] [default to none] |
| **cardStickers** | **String**|  true or false | [optional] |
| **boardStars** | **String**| One of: mine or none | [optional] [default to none] |
| **labels** | **String**| One of: all or none | [optional] [default to none] |
| **labelFields** | **String**| all or a comma-separated list of: color, idBoard, name or uses | [optional] [default to all] |
| **labelsLimit** | **String**| a number from 0 to 1000 | [optional] [default to 50] |
| **lists** | **String**| One of: all, closed, none or open | [optional] [default to none] |
| **listFields** | **String**| all or a comma-separated list of: closed, idBoard, name, pos or subscribed | [optional] [default to all] |
| **memberships** | **String**| all or a comma-separated list of: active, admin, deactivated, me or normal | [optional] [default to none] |
| **membershipsMember** | **String**|  true or false | [optional] |
| **membershipsMemberFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to fullName and username] |
| **members** | **String**| One of: admins, all, none, normal or owners | [optional] [default to none] |
| **memberFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to avatarHash, initials, fullName, username and confirmed] |
| **membersInvited** | **String**| One of: admins, all, none, normal or owners | [optional] [default to none] |
| **membersInvitedFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to avatarHash, initials, fullName and username] |
| **checklists** | **String**| One of: all or none | [optional] [default to none] |
| **checklistFields** | **String**| all or a comma-separated list of: idBoard, idCard, name or pos | [optional] [default to all] |
| **organization** | **String**|  true or false | [optional] |
| **organizationFields** | **String**| all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website | [optional] [default to name and displayName] |
| **organizationMemberships** | **String**| all or a comma-separated list of: active, admin, deactivated, me or normal | [optional] [default to none] |
| **myPrefs** | **String**|  true or false | [optional] |
| **fields** | **String**| all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url | [optional] [default to name, desc, descData, closed, idOrganization, pinned, url, shortUrl, prefs and labelNames] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="getBoardsByIdBoardByField"></a>
# **getBoardsByIdBoardByField**
> getBoardsByIdBoardByField(idBoard, field, key, token)

getBoardsByIdBoardByField()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String field = "field_example"; // String | field
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    try {
      apiInstance.getBoardsByIdBoardByField(idBoard, field, key, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#getBoardsByIdBoardByField");
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
| **idBoard** | **String**| board_id | |
| **field** | **String**| field | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |

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

<a id="getBoardsCardsByIdBoard"></a>
# **getBoardsCardsByIdBoard**
> getBoardsCardsByIdBoard(idBoard, key, token, actions, attachments, attachmentFields, stickers, members, memberFields, checkItemStates, checklists, limit, since, before, filter, fields)

getBoardsCardsByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    String actions = "actions_example"; // String | all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization
    String attachments = "attachments_example"; // String | A boolean value or &quot;cover&quot; for only card cover attachments
    String attachmentFields = "all"; // String | all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url
    String stickers = "stickers_example"; // String |  true or false
    String members = "members_example"; // String |  true or false
    String memberFields = "avatarHash, fullName, initials and username"; // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
    String checkItemStates = "checkItemStates_example"; // String |  true or false
    String checklists = "none"; // String | One of: all or none
    String limit = "limit_example"; // String | a number from 1 to 1000
    String since = "since_example"; // String | A date, or null
    String before = "before_example"; // String | A date, or null
    String filter = "visible"; // String | One of: all, closed, none, open or visible
    String fields = "all"; // String | all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url
    try {
      apiInstance.getBoardsCardsByIdBoard(idBoard, key, token, actions, attachments, attachmentFields, stickers, members, memberFields, checkItemStates, checklists, limit, since, before, filter, fields);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#getBoardsCardsByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **actions** | **String**| all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization | [optional] |
| **attachments** | **String**| A boolean value or &amp;quot;cover&amp;quot; for only card cover attachments | [optional] |
| **attachmentFields** | **String**| all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url | [optional] [default to all] |
| **stickers** | **String**|  true or false | [optional] |
| **members** | **String**|  true or false | [optional] |
| **memberFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to avatarHash, fullName, initials and username] |
| **checkItemStates** | **String**|  true or false | [optional] |
| **checklists** | **String**| One of: all or none | [optional] [default to none] |
| **limit** | **String**| a number from 1 to 1000 | [optional] |
| **since** | **String**| A date, or null | [optional] |
| **before** | **String**| A date, or null | [optional] |
| **filter** | **String**| One of: all, closed, none, open or visible | [optional] [default to visible] |
| **fields** | **String**| all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url | [optional] [default to all] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="getBoardsCardsByIdBoardByFilter"></a>
# **getBoardsCardsByIdBoardByFilter**
> getBoardsCardsByIdBoardByFilter(idBoard, filter, key, token)

getBoardsCardsByIdBoardByFilter()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String filter = "filter_example"; // String | filter
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    try {
      apiInstance.getBoardsCardsByIdBoardByFilter(idBoard, filter, key, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#getBoardsCardsByIdBoardByFilter");
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
| **idBoard** | **String**| board_id | |
| **filter** | **String**| filter | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |

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

<a id="getBoardsCardsByIdBoardByIdCard"></a>
# **getBoardsCardsByIdBoardByIdCard**
> getBoardsCardsByIdBoardByIdCard(idBoard, idCard, key, token, attachments, attachmentFields, actions, actionsEntities, actionsDisplay, actionsLimit, actionFields, actionMemberCreatorFields, members, memberFields, checkItemStates, checkItemStateFields, labels, checklists, checklistFields, fields)

getBoardsCardsByIdBoardByIdCard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String idCard = "idCard_example"; // String | idCard
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    String attachments = "attachments_example"; // String | A boolean value or &quot;cover&quot; for only card cover attachments
    String attachmentFields = "all"; // String | all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url
    String actions = "actions_example"; // String | all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization
    String actionsEntities = "actionsEntities_example"; // String |  true or false
    String actionsDisplay = "actionsDisplay_example"; // String |  true or false
    String actionsLimit = "50"; // String | a number from 0 to 1000
    String actionFields = "all"; // String | all or a comma-separated list of: data, date, idMemberCreator or type
    String actionMemberCreatorFields = "avatarHash, fullName, initials and username"; // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
    String members = "members_example"; // String |  true or false
    String memberFields = "avatarHash, initials, fullName and username"; // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
    String checkItemStates = "checkItemStates_example"; // String |  true or false
    String checkItemStateFields = "all"; // String | all or a comma-separated list of: idCheckItem or state
    String labels = "labels_example"; // String |  true or false
    String checklists = "none"; // String | One of: all or none
    String checklistFields = "all"; // String | all or a comma-separated list of: idBoard, idCard, name or pos
    String fields = "all"; // String | all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url
    try {
      apiInstance.getBoardsCardsByIdBoardByIdCard(idBoard, idCard, key, token, attachments, attachmentFields, actions, actionsEntities, actionsDisplay, actionsLimit, actionFields, actionMemberCreatorFields, members, memberFields, checkItemStates, checkItemStateFields, labels, checklists, checklistFields, fields);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#getBoardsCardsByIdBoardByIdCard");
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
| **idBoard** | **String**| board_id | |
| **idCard** | **String**| idCard | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **attachments** | **String**| A boolean value or &amp;quot;cover&amp;quot; for only card cover attachments | [optional] |
| **attachmentFields** | **String**| all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url | [optional] [default to all] |
| **actions** | **String**| all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization | [optional] |
| **actionsEntities** | **String**|  true or false | [optional] |
| **actionsDisplay** | **String**|  true or false | [optional] |
| **actionsLimit** | **String**| a number from 0 to 1000 | [optional] [default to 50] |
| **actionFields** | **String**| all or a comma-separated list of: data, date, idMemberCreator or type | [optional] [default to all] |
| **actionMemberCreatorFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to avatarHash, fullName, initials and username] |
| **members** | **String**|  true or false | [optional] |
| **memberFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to avatarHash, initials, fullName and username] |
| **checkItemStates** | **String**|  true or false | [optional] |
| **checkItemStateFields** | **String**| all or a comma-separated list of: idCheckItem or state | [optional] [default to all] |
| **labels** | **String**|  true or false | [optional] |
| **checklists** | **String**| One of: all or none | [optional] [default to none] |
| **checklistFields** | **String**| all or a comma-separated list of: idBoard, idCard, name or pos | [optional] [default to all] |
| **fields** | **String**| all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url | [optional] [default to all] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="getBoardsChecklistsByIdBoard"></a>
# **getBoardsChecklistsByIdBoard**
> getBoardsChecklistsByIdBoard(idBoard, key, token, cards, cardFields, checkItems, checkItemFields, filter, fields)

getBoardsChecklistsByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    String cards = "none"; // String | One of: all, closed, none, open or visible
    String cardFields = "all"; // String | all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url
    String checkItems = "all"; // String | One of: all or none
    String checkItemFields = "name, nameData, pos and state"; // String | all or a comma-separated list of: name, nameData, pos, state or type
    String filter = "all"; // String | One of: all or none
    String fields = "all"; // String | all or a comma-separated list of: idBoard, idCard, name or pos
    try {
      apiInstance.getBoardsChecklistsByIdBoard(idBoard, key, token, cards, cardFields, checkItems, checkItemFields, filter, fields);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#getBoardsChecklistsByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **cards** | **String**| One of: all, closed, none, open or visible | [optional] [default to none] |
| **cardFields** | **String**| all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url | [optional] [default to all] |
| **checkItems** | **String**| One of: all or none | [optional] [default to all] |
| **checkItemFields** | **String**| all or a comma-separated list of: name, nameData, pos, state or type | [optional] [default to name, nameData, pos and state] |
| **filter** | **String**| One of: all or none | [optional] [default to all] |
| **fields** | **String**| all or a comma-separated list of: idBoard, idCard, name or pos | [optional] [default to all] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="getBoardsDeltasByIdBoard"></a>
# **getBoardsDeltasByIdBoard**
> getBoardsDeltasByIdBoard(idBoard, tags, ixLastUpdate, key, token)

getBoardsDeltasByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String tags = "tags_example"; // String | A valid tag for subscribing
    String ixLastUpdate = "ixLastUpdate_example"; // String | a number from -1 to Infinity
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    try {
      apiInstance.getBoardsDeltasByIdBoard(idBoard, tags, ixLastUpdate, key, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#getBoardsDeltasByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **tags** | **String**| A valid tag for subscribing | |
| **ixLastUpdate** | **String**| a number from -1 to Infinity | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="getBoardsLabelsByIdBoard"></a>
# **getBoardsLabelsByIdBoard**
> getBoardsLabelsByIdBoard(idBoard, key, token, fields, limit)

getBoardsLabelsByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    String fields = "all"; // String | all or a comma-separated list of: color, idBoard, name or uses
    String limit = "50"; // String | a number from 0 to 1000
    try {
      apiInstance.getBoardsLabelsByIdBoard(idBoard, key, token, fields, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#getBoardsLabelsByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **fields** | **String**| all or a comma-separated list of: color, idBoard, name or uses | [optional] [default to all] |
| **limit** | **String**| a number from 0 to 1000 | [optional] [default to 50] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="getBoardsLabelsByIdBoardByIdLabel"></a>
# **getBoardsLabelsByIdBoardByIdLabel**
> getBoardsLabelsByIdBoardByIdLabel(idBoard, idLabel, key, token, fields)

getBoardsLabelsByIdBoardByIdLabel()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String idLabel = "idLabel_example"; // String | idLabel
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    String fields = "all"; // String | all or a comma-separated list of: color, idBoard, name or uses
    try {
      apiInstance.getBoardsLabelsByIdBoardByIdLabel(idBoard, idLabel, key, token, fields);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#getBoardsLabelsByIdBoardByIdLabel");
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
| **idBoard** | **String**| board_id | |
| **idLabel** | **String**| idLabel | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **fields** | **String**| all or a comma-separated list of: color, idBoard, name or uses | [optional] [default to all] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="getBoardsListsByIdBoard"></a>
# **getBoardsListsByIdBoard**
> getBoardsListsByIdBoard(idBoard, key, token, cards, cardFields, filter, fields)

getBoardsListsByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    String cards = "none"; // String | One of: all, closed, none, open or visible
    String cardFields = "all"; // String | all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url
    String filter = "open"; // String | One of: all, closed, none or open
    String fields = "all"; // String | all or a comma-separated list of: closed, idBoard, name, pos or subscribed
    try {
      apiInstance.getBoardsListsByIdBoard(idBoard, key, token, cards, cardFields, filter, fields);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#getBoardsListsByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **cards** | **String**| One of: all, closed, none, open or visible | [optional] [default to none] |
| **cardFields** | **String**| all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url | [optional] [default to all] |
| **filter** | **String**| One of: all, closed, none or open | [optional] [default to open] |
| **fields** | **String**| all or a comma-separated list of: closed, idBoard, name, pos or subscribed | [optional] [default to all] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="getBoardsListsByIdBoardByFilter"></a>
# **getBoardsListsByIdBoardByFilter**
> getBoardsListsByIdBoardByFilter(idBoard, filter, key, token)

getBoardsListsByIdBoardByFilter()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String filter = "filter_example"; // String | filter
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    try {
      apiInstance.getBoardsListsByIdBoardByFilter(idBoard, filter, key, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#getBoardsListsByIdBoardByFilter");
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
| **idBoard** | **String**| board_id | |
| **filter** | **String**| filter | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |

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

<a id="getBoardsMembersByIdBoard"></a>
# **getBoardsMembersByIdBoard**
> getBoardsMembersByIdBoard(idBoard, key, token, filter, fields, activity)

getBoardsMembersByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    String filter = "all"; // String | One of: admins, all, none, normal or owners
    String fields = "fullName and username"; // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
    String activity = "activity_example"; // String | true or false ; works for premium organizations only.
    try {
      apiInstance.getBoardsMembersByIdBoard(idBoard, key, token, filter, fields, activity);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#getBoardsMembersByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **filter** | **String**| One of: admins, all, none, normal or owners | [optional] [default to all] |
| **fields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to fullName and username] |
| **activity** | **String**| true or false ; works for premium organizations only. | [optional] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="getBoardsMembersByIdBoardByFilter"></a>
# **getBoardsMembersByIdBoardByFilter**
> getBoardsMembersByIdBoardByFilter(idBoard, filter, key, token)

getBoardsMembersByIdBoardByFilter()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String filter = "filter_example"; // String | filter
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    try {
      apiInstance.getBoardsMembersByIdBoardByFilter(idBoard, filter, key, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#getBoardsMembersByIdBoardByFilter");
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
| **idBoard** | **String**| board_id | |
| **filter** | **String**| filter | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |

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

<a id="getBoardsMembersCardsByIdBoardByIdMember"></a>
# **getBoardsMembersCardsByIdBoardByIdMember**
> getBoardsMembersCardsByIdBoardByIdMember(idBoard, idMember, key, token, actions, attachments, attachmentFields, members, memberFields, checkItemStates, checklists, board, boardFields, _list, listFields, filter, fields)

getBoardsMembersCardsByIdBoardByIdMember()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String idMember = "idMember_example"; // String | idMember
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    String actions = "actions_example"; // String | all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization
    String attachments = "attachments_example"; // String | A boolean value or &quot;cover&quot; for only card cover attachments
    String attachmentFields = "all"; // String | all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url
    String members = "members_example"; // String |  true or false
    String memberFields = "avatarHash, fullName, initials and username"; // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
    String checkItemStates = "checkItemStates_example"; // String |  true or false
    String checklists = "none"; // String | One of: all or none
    String board = "board_example"; // String |  true or false
    String boardFields = "name, desc, closed, idOrganization, pinned, url and prefs"; // String | all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url
    String _list = "_list_example"; // String |  true or false
    String listFields = "all"; // String | all or a comma-separated list of: closed, idBoard, name, pos or subscribed
    String filter = "visible"; // String | One of: all, closed, none, open or visible
    String fields = "all"; // String | all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url
    try {
      apiInstance.getBoardsMembersCardsByIdBoardByIdMember(idBoard, idMember, key, token, actions, attachments, attachmentFields, members, memberFields, checkItemStates, checklists, board, boardFields, _list, listFields, filter, fields);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#getBoardsMembersCardsByIdBoardByIdMember");
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
| **idBoard** | **String**| board_id | |
| **idMember** | **String**| idMember | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **actions** | **String**| all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization | [optional] |
| **attachments** | **String**| A boolean value or &amp;quot;cover&amp;quot; for only card cover attachments | [optional] |
| **attachmentFields** | **String**| all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url | [optional] [default to all] |
| **members** | **String**|  true or false | [optional] |
| **memberFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to avatarHash, fullName, initials and username] |
| **checkItemStates** | **String**|  true or false | [optional] |
| **checklists** | **String**| One of: all or none | [optional] [default to none] |
| **board** | **String**|  true or false | [optional] |
| **boardFields** | **String**| all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url | [optional] [default to name, desc, closed, idOrganization, pinned, url and prefs] |
| **_list** | **String**|  true or false | [optional] |
| **listFields** | **String**| all or a comma-separated list of: closed, idBoard, name, pos or subscribed | [optional] [default to all] |
| **filter** | **String**| One of: all, closed, none, open or visible | [optional] [default to visible] |
| **fields** | **String**| all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url | [optional] [default to all] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="getBoardsMembersInvitedByIdBoard"></a>
# **getBoardsMembersInvitedByIdBoard**
> getBoardsMembersInvitedByIdBoard(idBoard, key, token, fields)

getBoardsMembersInvitedByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    String fields = "all"; // String | all or a comma-separated list of: avatarHash, avatarSource, bio, bioData, confirmed, email, fullName, gravatarHash, idBoards, idBoardsPinned, idOrganizations, idPremOrgsAdmin, initials, loginTypes, memberType, oneTimeMessagesDismissed, prefs, premiumFeatures, products, status, status, trophies, uploadedAvatarHash, url or username
    try {
      apiInstance.getBoardsMembersInvitedByIdBoard(idBoard, key, token, fields);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#getBoardsMembersInvitedByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **fields** | **String**| all or a comma-separated list of: avatarHash, avatarSource, bio, bioData, confirmed, email, fullName, gravatarHash, idBoards, idBoardsPinned, idOrganizations, idPremOrgsAdmin, initials, loginTypes, memberType, oneTimeMessagesDismissed, prefs, premiumFeatures, products, status, status, trophies, uploadedAvatarHash, url or username | [optional] [default to all] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="getBoardsMembersInvitedByIdBoardByField"></a>
# **getBoardsMembersInvitedByIdBoardByField**
> getBoardsMembersInvitedByIdBoardByField(idBoard, field, key, token)

getBoardsMembersInvitedByIdBoardByField()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String field = "field_example"; // String | field
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    try {
      apiInstance.getBoardsMembersInvitedByIdBoardByField(idBoard, field, key, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#getBoardsMembersInvitedByIdBoardByField");
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
| **idBoard** | **String**| board_id | |
| **field** | **String**| field | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="getBoardsMembershipsByIdBoard"></a>
# **getBoardsMembershipsByIdBoard**
> getBoardsMembershipsByIdBoard(idBoard, key, token, filter, member, memberFields)

getBoardsMembershipsByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    String filter = "all"; // String | all or a comma-separated list of: active, admin, deactivated, me or normal
    String member = "member_example"; // String |  true or false
    String memberFields = "fullName and username"; // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
    try {
      apiInstance.getBoardsMembershipsByIdBoard(idBoard, key, token, filter, member, memberFields);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#getBoardsMembershipsByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **filter** | **String**| all or a comma-separated list of: active, admin, deactivated, me or normal | [optional] [default to all] |
| **member** | **String**|  true or false | [optional] |
| **memberFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to fullName and username] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="getBoardsMembershipsByIdBoardByIdMembership"></a>
# **getBoardsMembershipsByIdBoardByIdMembership**
> getBoardsMembershipsByIdBoardByIdMembership(idBoard, idMembership, key, token, member, memberFields)

getBoardsMembershipsByIdBoardByIdMembership()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String idMembership = "idMembership_example"; // String | idMembership
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    String member = "member_example"; // String |  true or false
    String memberFields = "fullName and username"; // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
    try {
      apiInstance.getBoardsMembershipsByIdBoardByIdMembership(idBoard, idMembership, key, token, member, memberFields);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#getBoardsMembershipsByIdBoardByIdMembership");
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
| **idBoard** | **String**| board_id | |
| **idMembership** | **String**| idMembership | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **member** | **String**|  true or false | [optional] |
| **memberFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to fullName and username] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="getBoardsMyPrefsByIdBoard"></a>
# **getBoardsMyPrefsByIdBoard**
> getBoardsMyPrefsByIdBoard(idBoard, key, token)

getBoardsMyPrefsByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    try {
      apiInstance.getBoardsMyPrefsByIdBoard(idBoard, key, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#getBoardsMyPrefsByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="getBoardsOrganizationByIdBoard"></a>
# **getBoardsOrganizationByIdBoard**
> getBoardsOrganizationByIdBoard(idBoard, key, token, fields)

getBoardsOrganizationByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    String fields = "all"; // String | all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website
    try {
      apiInstance.getBoardsOrganizationByIdBoard(idBoard, key, token, fields);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#getBoardsOrganizationByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **fields** | **String**| all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website | [optional] [default to all] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="getBoardsOrganizationByIdBoardByField"></a>
# **getBoardsOrganizationByIdBoardByField**
> getBoardsOrganizationByIdBoardByField(idBoard, field, key, token)

getBoardsOrganizationByIdBoardByField()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String field = "field_example"; // String | field
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    try {
      apiInstance.getBoardsOrganizationByIdBoardByField(idBoard, field, key, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#getBoardsOrganizationByIdBoardByField");
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
| **idBoard** | **String**| board_id | |
| **field** | **String**| field | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="updateBoardsByIdBoard"></a>
# **updateBoardsByIdBoard**
> updateBoardsByIdBoard(idBoard, key, token, boards)

updateBoardsByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    Boards boards = new Boards(); // Boards | Attributes of \"Boards\" to be updated.
    try {
      apiInstance.updateBoardsByIdBoard(idBoard, key, token, boards);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#updateBoardsByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **boards** | [**Boards**](Boards.md)| Attributes of \&quot;Boards\&quot; to be updated. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="updateBoardsClosedByIdBoard"></a>
# **updateBoardsClosedByIdBoard**
> updateBoardsClosedByIdBoard(idBoard, key, token, boardsClosed)

updateBoardsClosedByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    BoardsClosed boardsClosed = new BoardsClosed(); // BoardsClosed | Attributes of \"Boards Closed\" to be updated.
    try {
      apiInstance.updateBoardsClosedByIdBoard(idBoard, key, token, boardsClosed);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#updateBoardsClosedByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **boardsClosed** | [**BoardsClosed**](BoardsClosed.md)| Attributes of \&quot;Boards Closed\&quot; to be updated. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="updateBoardsDescByIdBoard"></a>
# **updateBoardsDescByIdBoard**
> updateBoardsDescByIdBoard(idBoard, key, token, boardsDesc)

updateBoardsDescByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    BoardsDesc boardsDesc = new BoardsDesc(); // BoardsDesc | Attributes of \"Boards Desc\" to be updated.
    try {
      apiInstance.updateBoardsDescByIdBoard(idBoard, key, token, boardsDesc);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#updateBoardsDescByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **boardsDesc** | [**BoardsDesc**](BoardsDesc.md)| Attributes of \&quot;Boards Desc\&quot; to be updated. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="updateBoardsIdOrganizationByIdBoard"></a>
# **updateBoardsIdOrganizationByIdBoard**
> updateBoardsIdOrganizationByIdBoard(idBoard, key, token, boardsIdOrganization)

updateBoardsIdOrganizationByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    BoardsIdOrganization boardsIdOrganization = new BoardsIdOrganization(); // BoardsIdOrganization | Attributes of \"Boards Id Organization\" to be updated.
    try {
      apiInstance.updateBoardsIdOrganizationByIdBoard(idBoard, key, token, boardsIdOrganization);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#updateBoardsIdOrganizationByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **boardsIdOrganization** | [**BoardsIdOrganization**](BoardsIdOrganization.md)| Attributes of \&quot;Boards Id Organization\&quot; to be updated. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="updateBoardsLabelNamesBlueByIdBoard"></a>
# **updateBoardsLabelNamesBlueByIdBoard**
> updateBoardsLabelNamesBlueByIdBoard(idBoard, key, token, labelNamesBlue)

updateBoardsLabelNamesBlueByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    LabelNamesBlue labelNamesBlue = new LabelNamesBlue(); // LabelNamesBlue | Attributes of \"Label Names Blue\" to be updated.
    try {
      apiInstance.updateBoardsLabelNamesBlueByIdBoard(idBoard, key, token, labelNamesBlue);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#updateBoardsLabelNamesBlueByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **labelNamesBlue** | [**LabelNamesBlue**](LabelNamesBlue.md)| Attributes of \&quot;Label Names Blue\&quot; to be updated. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="updateBoardsLabelNamesGreenByIdBoard"></a>
# **updateBoardsLabelNamesGreenByIdBoard**
> updateBoardsLabelNamesGreenByIdBoard(idBoard, key, token, labelNamesGreen)

updateBoardsLabelNamesGreenByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    LabelNamesGreen labelNamesGreen = new LabelNamesGreen(); // LabelNamesGreen | Attributes of \"Label Names Green\" to be updated.
    try {
      apiInstance.updateBoardsLabelNamesGreenByIdBoard(idBoard, key, token, labelNamesGreen);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#updateBoardsLabelNamesGreenByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **labelNamesGreen** | [**LabelNamesGreen**](LabelNamesGreen.md)| Attributes of \&quot;Label Names Green\&quot; to be updated. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="updateBoardsLabelNamesOrangeByIdBoard"></a>
# **updateBoardsLabelNamesOrangeByIdBoard**
> updateBoardsLabelNamesOrangeByIdBoard(idBoard, key, token, labelNamesOrange)

updateBoardsLabelNamesOrangeByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    LabelNamesOrange labelNamesOrange = new LabelNamesOrange(); // LabelNamesOrange | Attributes of \"Label Names Orange\" to be updated.
    try {
      apiInstance.updateBoardsLabelNamesOrangeByIdBoard(idBoard, key, token, labelNamesOrange);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#updateBoardsLabelNamesOrangeByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **labelNamesOrange** | [**LabelNamesOrange**](LabelNamesOrange.md)| Attributes of \&quot;Label Names Orange\&quot; to be updated. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="updateBoardsLabelNamesPurpleByIdBoard"></a>
# **updateBoardsLabelNamesPurpleByIdBoard**
> updateBoardsLabelNamesPurpleByIdBoard(idBoard, key, token, labelNamesPurple)

updateBoardsLabelNamesPurpleByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    LabelNamesPurple labelNamesPurple = new LabelNamesPurple(); // LabelNamesPurple | Attributes of \"Label Names Purple\" to be updated.
    try {
      apiInstance.updateBoardsLabelNamesPurpleByIdBoard(idBoard, key, token, labelNamesPurple);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#updateBoardsLabelNamesPurpleByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **labelNamesPurple** | [**LabelNamesPurple**](LabelNamesPurple.md)| Attributes of \&quot;Label Names Purple\&quot; to be updated. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="updateBoardsLabelNamesRedByIdBoard"></a>
# **updateBoardsLabelNamesRedByIdBoard**
> updateBoardsLabelNamesRedByIdBoard(idBoard, key, token, labelNamesRed)

updateBoardsLabelNamesRedByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    LabelNamesRed labelNamesRed = new LabelNamesRed(); // LabelNamesRed | Attributes of \"Label Names Red\" to be updated.
    try {
      apiInstance.updateBoardsLabelNamesRedByIdBoard(idBoard, key, token, labelNamesRed);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#updateBoardsLabelNamesRedByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **labelNamesRed** | [**LabelNamesRed**](LabelNamesRed.md)| Attributes of \&quot;Label Names Red\&quot; to be updated. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="updateBoardsLabelNamesYellowByIdBoard"></a>
# **updateBoardsLabelNamesYellowByIdBoard**
> updateBoardsLabelNamesYellowByIdBoard(idBoard, key, token, labelNamesYellow)

updateBoardsLabelNamesYellowByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    LabelNamesYellow labelNamesYellow = new LabelNamesYellow(); // LabelNamesYellow | Attributes of \"Label Names Yellow\" to be updated.
    try {
      apiInstance.updateBoardsLabelNamesYellowByIdBoard(idBoard, key, token, labelNamesYellow);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#updateBoardsLabelNamesYellowByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **labelNamesYellow** | [**LabelNamesYellow**](LabelNamesYellow.md)| Attributes of \&quot;Label Names Yellow\&quot; to be updated. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="updateBoardsMembersByIdBoard"></a>
# **updateBoardsMembersByIdBoard**
> updateBoardsMembersByIdBoard(idBoard, key, token, boardsMembers)

updateBoardsMembersByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    BoardsMembers boardsMembers = new BoardsMembers(); // BoardsMembers | Attributes of \"Boards Members\" to be updated.
    try {
      apiInstance.updateBoardsMembersByIdBoard(idBoard, key, token, boardsMembers);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#updateBoardsMembersByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **boardsMembers** | [**BoardsMembers**](BoardsMembers.md)| Attributes of \&quot;Boards Members\&quot; to be updated. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="updateBoardsMembersByIdBoardByIdMember"></a>
# **updateBoardsMembersByIdBoardByIdMember**
> updateBoardsMembersByIdBoardByIdMember(idBoard, idMember, key, token, boardsMembers)

updateBoardsMembersByIdBoardByIdMember()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String idMember = "idMember_example"; // String | idMember
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    BoardsMembers boardsMembers = new BoardsMembers(); // BoardsMembers | Attributes of \"Boards Members\" to be updated.
    try {
      apiInstance.updateBoardsMembersByIdBoardByIdMember(idBoard, idMember, key, token, boardsMembers);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#updateBoardsMembersByIdBoardByIdMember");
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
| **idBoard** | **String**| board_id | |
| **idMember** | **String**| idMember | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **boardsMembers** | [**BoardsMembers**](BoardsMembers.md)| Attributes of \&quot;Boards Members\&quot; to be updated. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="updateBoardsMembershipsByIdBoardByIdMembership"></a>
# **updateBoardsMembershipsByIdBoardByIdMembership**
> updateBoardsMembershipsByIdBoardByIdMembership(idBoard, idMembership, key, token, boardsMemberships)

updateBoardsMembershipsByIdBoardByIdMembership()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String idMembership = "idMembership_example"; // String | idMembership
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    BoardsMemberships boardsMemberships = new BoardsMemberships(); // BoardsMemberships | Attributes of \"Boards Memberships\" to be updated.
    try {
      apiInstance.updateBoardsMembershipsByIdBoardByIdMembership(idBoard, idMembership, key, token, boardsMemberships);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#updateBoardsMembershipsByIdBoardByIdMembership");
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
| **idBoard** | **String**| board_id | |
| **idMembership** | **String**| idMembership | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **boardsMemberships** | [**BoardsMemberships**](BoardsMemberships.md)| Attributes of \&quot;Boards Memberships\&quot; to be updated. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="updateBoardsMyPrefsEmailPositionByIdBoard"></a>
# **updateBoardsMyPrefsEmailPositionByIdBoard**
> updateBoardsMyPrefsEmailPositionByIdBoard(idBoard, key, token, myPrefsEmailPosition)

updateBoardsMyPrefsEmailPositionByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    MyPrefsEmailPosition myPrefsEmailPosition = new MyPrefsEmailPosition(); // MyPrefsEmailPosition | Attributes of \"My Prefs Email Position\" to be updated.
    try {
      apiInstance.updateBoardsMyPrefsEmailPositionByIdBoard(idBoard, key, token, myPrefsEmailPosition);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#updateBoardsMyPrefsEmailPositionByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **myPrefsEmailPosition** | [**MyPrefsEmailPosition**](MyPrefsEmailPosition.md)| Attributes of \&quot;My Prefs Email Position\&quot; to be updated. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="updateBoardsMyPrefsIdEmailListByIdBoard"></a>
# **updateBoardsMyPrefsIdEmailListByIdBoard**
> updateBoardsMyPrefsIdEmailListByIdBoard(idBoard, key, token, myPrefsIdEmailList)

updateBoardsMyPrefsIdEmailListByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    MyPrefsIdEmailList myPrefsIdEmailList = new MyPrefsIdEmailList(); // MyPrefsIdEmailList | Attributes of \"My Prefs Id Email List\" to be updated.
    try {
      apiInstance.updateBoardsMyPrefsIdEmailListByIdBoard(idBoard, key, token, myPrefsIdEmailList);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#updateBoardsMyPrefsIdEmailListByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **myPrefsIdEmailList** | [**MyPrefsIdEmailList**](MyPrefsIdEmailList.md)| Attributes of \&quot;My Prefs Id Email List\&quot; to be updated. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="updateBoardsMyPrefsShowListGuideByIdBoard"></a>
# **updateBoardsMyPrefsShowListGuideByIdBoard**
> updateBoardsMyPrefsShowListGuideByIdBoard(idBoard, key, token, myPrefsShowListGuide)

updateBoardsMyPrefsShowListGuideByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    MyPrefsShowListGuide myPrefsShowListGuide = new MyPrefsShowListGuide(); // MyPrefsShowListGuide | Attributes of \"My Prefs Show List Guide\" to be updated.
    try {
      apiInstance.updateBoardsMyPrefsShowListGuideByIdBoard(idBoard, key, token, myPrefsShowListGuide);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#updateBoardsMyPrefsShowListGuideByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **myPrefsShowListGuide** | [**MyPrefsShowListGuide**](MyPrefsShowListGuide.md)| Attributes of \&quot;My Prefs Show List Guide\&quot; to be updated. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="updateBoardsMyPrefsShowSidebarActivityByIdBoard"></a>
# **updateBoardsMyPrefsShowSidebarActivityByIdBoard**
> updateBoardsMyPrefsShowSidebarActivityByIdBoard(idBoard, key, token, myPrefsShowSidebarActivity)

updateBoardsMyPrefsShowSidebarActivityByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    MyPrefsShowSidebarActivity myPrefsShowSidebarActivity = new MyPrefsShowSidebarActivity(); // MyPrefsShowSidebarActivity | Attributes of \"My Prefs Show Sidebar Activity\" to be updated.
    try {
      apiInstance.updateBoardsMyPrefsShowSidebarActivityByIdBoard(idBoard, key, token, myPrefsShowSidebarActivity);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#updateBoardsMyPrefsShowSidebarActivityByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **myPrefsShowSidebarActivity** | [**MyPrefsShowSidebarActivity**](MyPrefsShowSidebarActivity.md)| Attributes of \&quot;My Prefs Show Sidebar Activity\&quot; to be updated. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="updateBoardsMyPrefsShowSidebarBoardActionsByIdBoard"></a>
# **updateBoardsMyPrefsShowSidebarBoardActionsByIdBoard**
> updateBoardsMyPrefsShowSidebarBoardActionsByIdBoard(idBoard, key, token, myPrefsShowSidebarBoardActions)

updateBoardsMyPrefsShowSidebarBoardActionsByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    MyPrefsShowSidebarBoardActions myPrefsShowSidebarBoardActions = new MyPrefsShowSidebarBoardActions(); // MyPrefsShowSidebarBoardActions | Attributes of \"My Prefs Show Sidebar Board Actions\" to be updated.
    try {
      apiInstance.updateBoardsMyPrefsShowSidebarBoardActionsByIdBoard(idBoard, key, token, myPrefsShowSidebarBoardActions);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#updateBoardsMyPrefsShowSidebarBoardActionsByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **myPrefsShowSidebarBoardActions** | [**MyPrefsShowSidebarBoardActions**](MyPrefsShowSidebarBoardActions.md)| Attributes of \&quot;My Prefs Show Sidebar Board Actions\&quot; to be updated. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="updateBoardsMyPrefsShowSidebarByIdBoard"></a>
# **updateBoardsMyPrefsShowSidebarByIdBoard**
> updateBoardsMyPrefsShowSidebarByIdBoard(idBoard, key, token, myPrefsShowSidebar)

updateBoardsMyPrefsShowSidebarByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    MyPrefsShowSidebar myPrefsShowSidebar = new MyPrefsShowSidebar(); // MyPrefsShowSidebar | Attributes of \"My Prefs Show Sidebar\" to be updated.
    try {
      apiInstance.updateBoardsMyPrefsShowSidebarByIdBoard(idBoard, key, token, myPrefsShowSidebar);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#updateBoardsMyPrefsShowSidebarByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **myPrefsShowSidebar** | [**MyPrefsShowSidebar**](MyPrefsShowSidebar.md)| Attributes of \&quot;My Prefs Show Sidebar\&quot; to be updated. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="updateBoardsMyPrefsShowSidebarMembersByIdBoard"></a>
# **updateBoardsMyPrefsShowSidebarMembersByIdBoard**
> updateBoardsMyPrefsShowSidebarMembersByIdBoard(idBoard, key, token, myPrefsShowSidebarMembers)

updateBoardsMyPrefsShowSidebarMembersByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    MyPrefsShowSidebarMembers myPrefsShowSidebarMembers = new MyPrefsShowSidebarMembers(); // MyPrefsShowSidebarMembers | Attributes of \"My Prefs Show Sidebar Members\" to be updated.
    try {
      apiInstance.updateBoardsMyPrefsShowSidebarMembersByIdBoard(idBoard, key, token, myPrefsShowSidebarMembers);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#updateBoardsMyPrefsShowSidebarMembersByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **myPrefsShowSidebarMembers** | [**MyPrefsShowSidebarMembers**](MyPrefsShowSidebarMembers.md)| Attributes of \&quot;My Prefs Show Sidebar Members\&quot; to be updated. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="updateBoardsNameByIdBoard"></a>
# **updateBoardsNameByIdBoard**
> updateBoardsNameByIdBoard(idBoard, key, token, boardsName)

updateBoardsNameByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    BoardsName boardsName = new BoardsName(); // BoardsName | Attributes of \"Boards Name\" to be updated.
    try {
      apiInstance.updateBoardsNameByIdBoard(idBoard, key, token, boardsName);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#updateBoardsNameByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **boardsName** | [**BoardsName**](BoardsName.md)| Attributes of \&quot;Boards Name\&quot; to be updated. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="updateBoardsPrefsBackgroundByIdBoard"></a>
# **updateBoardsPrefsBackgroundByIdBoard**
> updateBoardsPrefsBackgroundByIdBoard(idBoard, key, token, prefsBackground)

updateBoardsPrefsBackgroundByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    PrefsBackground prefsBackground = new PrefsBackground(); // PrefsBackground | Attributes of \"Prefs Background\" to be updated.
    try {
      apiInstance.updateBoardsPrefsBackgroundByIdBoard(idBoard, key, token, prefsBackground);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#updateBoardsPrefsBackgroundByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **prefsBackground** | [**PrefsBackground**](PrefsBackground.md)| Attributes of \&quot;Prefs Background\&quot; to be updated. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="updateBoardsPrefsCalendarFeedEnabledByIdBoard"></a>
# **updateBoardsPrefsCalendarFeedEnabledByIdBoard**
> updateBoardsPrefsCalendarFeedEnabledByIdBoard(idBoard, key, token, prefsCalendarFeedEnabled)

updateBoardsPrefsCalendarFeedEnabledByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    PrefsCalendarFeedEnabled prefsCalendarFeedEnabled = new PrefsCalendarFeedEnabled(); // PrefsCalendarFeedEnabled | Attributes of \"Prefs Calendar Feed Enabled\" to be updated.
    try {
      apiInstance.updateBoardsPrefsCalendarFeedEnabledByIdBoard(idBoard, key, token, prefsCalendarFeedEnabled);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#updateBoardsPrefsCalendarFeedEnabledByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **prefsCalendarFeedEnabled** | [**PrefsCalendarFeedEnabled**](PrefsCalendarFeedEnabled.md)| Attributes of \&quot;Prefs Calendar Feed Enabled\&quot; to be updated. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="updateBoardsPrefsCardAgingByIdBoard"></a>
# **updateBoardsPrefsCardAgingByIdBoard**
> updateBoardsPrefsCardAgingByIdBoard(idBoard, key, token, prefsCardAging)

updateBoardsPrefsCardAgingByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    PrefsCardAging prefsCardAging = new PrefsCardAging(); // PrefsCardAging | Attributes of \"Prefs Card Aging\" to be updated.
    try {
      apiInstance.updateBoardsPrefsCardAgingByIdBoard(idBoard, key, token, prefsCardAging);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#updateBoardsPrefsCardAgingByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **prefsCardAging** | [**PrefsCardAging**](PrefsCardAging.md)| Attributes of \&quot;Prefs Card Aging\&quot; to be updated. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="updateBoardsPrefsCardCoversByIdBoard"></a>
# **updateBoardsPrefsCardCoversByIdBoard**
> updateBoardsPrefsCardCoversByIdBoard(idBoard, key, token, prefsCardCovers)

updateBoardsPrefsCardCoversByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    PrefsCardCovers prefsCardCovers = new PrefsCardCovers(); // PrefsCardCovers | Attributes of \"Prefs Card Covers\" to be updated.
    try {
      apiInstance.updateBoardsPrefsCardCoversByIdBoard(idBoard, key, token, prefsCardCovers);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#updateBoardsPrefsCardCoversByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **prefsCardCovers** | [**PrefsCardCovers**](PrefsCardCovers.md)| Attributes of \&quot;Prefs Card Covers\&quot; to be updated. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="updateBoardsPrefsCommentsByIdBoard"></a>
# **updateBoardsPrefsCommentsByIdBoard**
> updateBoardsPrefsCommentsByIdBoard(idBoard, key, token, prefsComments)

updateBoardsPrefsCommentsByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    PrefsComments prefsComments = new PrefsComments(); // PrefsComments | Attributes of \"Prefs Comments\" to be updated.
    try {
      apiInstance.updateBoardsPrefsCommentsByIdBoard(idBoard, key, token, prefsComments);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#updateBoardsPrefsCommentsByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **prefsComments** | [**PrefsComments**](PrefsComments.md)| Attributes of \&quot;Prefs Comments\&quot; to be updated. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="updateBoardsPrefsInvitationsByIdBoard"></a>
# **updateBoardsPrefsInvitationsByIdBoard**
> updateBoardsPrefsInvitationsByIdBoard(idBoard, key, token, prefsInvitations)

updateBoardsPrefsInvitationsByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    PrefsInvitations prefsInvitations = new PrefsInvitations(); // PrefsInvitations | Attributes of \"Prefs Invitations\" to be updated.
    try {
      apiInstance.updateBoardsPrefsInvitationsByIdBoard(idBoard, key, token, prefsInvitations);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#updateBoardsPrefsInvitationsByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **prefsInvitations** | [**PrefsInvitations**](PrefsInvitations.md)| Attributes of \&quot;Prefs Invitations\&quot; to be updated. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="updateBoardsPrefsPermissionLevelByIdBoard"></a>
# **updateBoardsPrefsPermissionLevelByIdBoard**
> updateBoardsPrefsPermissionLevelByIdBoard(idBoard, key, token, prefsPermissionLevel)

updateBoardsPrefsPermissionLevelByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    PrefsPermissionLevel prefsPermissionLevel = new PrefsPermissionLevel(); // PrefsPermissionLevel | Attributes of \"Prefs Permission Level\" to be updated.
    try {
      apiInstance.updateBoardsPrefsPermissionLevelByIdBoard(idBoard, key, token, prefsPermissionLevel);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#updateBoardsPrefsPermissionLevelByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **prefsPermissionLevel** | [**PrefsPermissionLevel**](PrefsPermissionLevel.md)| Attributes of \&quot;Prefs Permission Level\&quot; to be updated. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="updateBoardsPrefsSelfJoinByIdBoard"></a>
# **updateBoardsPrefsSelfJoinByIdBoard**
> updateBoardsPrefsSelfJoinByIdBoard(idBoard, key, token, prefsSelfJoin)

updateBoardsPrefsSelfJoinByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    PrefsSelfJoin prefsSelfJoin = new PrefsSelfJoin(); // PrefsSelfJoin | Attributes of \"Prefs Self Join\" to be updated.
    try {
      apiInstance.updateBoardsPrefsSelfJoinByIdBoard(idBoard, key, token, prefsSelfJoin);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#updateBoardsPrefsSelfJoinByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **prefsSelfJoin** | [**PrefsSelfJoin**](PrefsSelfJoin.md)| Attributes of \&quot;Prefs Self Join\&quot; to be updated. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="updateBoardsPrefsVotingByIdBoard"></a>
# **updateBoardsPrefsVotingByIdBoard**
> updateBoardsPrefsVotingByIdBoard(idBoard, key, token, prefsVoting)

updateBoardsPrefsVotingByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    PrefsVoting prefsVoting = new PrefsVoting(); // PrefsVoting | Attributes of \"Prefs Voting\" to be updated.
    try {
      apiInstance.updateBoardsPrefsVotingByIdBoard(idBoard, key, token, prefsVoting);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#updateBoardsPrefsVotingByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **prefsVoting** | [**PrefsVoting**](PrefsVoting.md)| Attributes of \&quot;Prefs Voting\&quot; to be updated. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

<a id="updateBoardsSubscribedByIdBoard"></a>
# **updateBoardsSubscribedByIdBoard**
> updateBoardsSubscribedByIdBoard(idBoard, key, token, boardsSubscribed)

updateBoardsSubscribedByIdBoard()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: api_token
    ApiKeyAuth api_token = (ApiKeyAuth) defaultClient.getAuthentication("api_token");
    api_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_token.setApiKeyPrefix("Token");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String idBoard = "idBoard_example"; // String | board_id
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    BoardsSubscribed boardsSubscribed = new BoardsSubscribed(); // BoardsSubscribed | Attributes of \"Boards Subscribed\" to be updated.
    try {
      apiInstance.updateBoardsSubscribedByIdBoard(idBoard, key, token, boardsSubscribed);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#updateBoardsSubscribedByIdBoard");
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
| **idBoard** | **String**| board_id | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **boardsSubscribed** | [**BoardsSubscribed**](BoardsSubscribed.md)| Attributes of \&quot;Boards Subscribed\&quot; to be updated. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Server rejection |  -  |

