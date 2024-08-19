# MemberApi

All URIs are relative to *https://trello.com/1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addMembersAvatarByIdMember**](MemberApi.md#addMembersAvatarByIdMember) | **POST** /members/{idMember}/avatar | addMembersAvatarByIdMember() |
| [**addMembersBoardBackgroundsByIdMember**](MemberApi.md#addMembersBoardBackgroundsByIdMember) | **POST** /members/{idMember}/boardBackgrounds | addMembersBoardBackgroundsByIdMember() |
| [**addMembersBoardStarsByIdMember**](MemberApi.md#addMembersBoardStarsByIdMember) | **POST** /members/{idMember}/boardStars | addMembersBoardStarsByIdMember() |
| [**addMembersCustomBoardBackgroundsByIdMember**](MemberApi.md#addMembersCustomBoardBackgroundsByIdMember) | **POST** /members/{idMember}/customBoardBackgrounds | addMembersCustomBoardBackgroundsByIdMember() |
| [**addMembersCustomEmojiByIdMember**](MemberApi.md#addMembersCustomEmojiByIdMember) | **POST** /members/{idMember}/customEmoji | addMembersCustomEmojiByIdMember() |
| [**addMembersCustomStickersByIdMember**](MemberApi.md#addMembersCustomStickersByIdMember) | **POST** /members/{idMember}/customStickers | addMembersCustomStickersByIdMember() |
| [**addMembersOneTimeMessagesDismissedByIdMember**](MemberApi.md#addMembersOneTimeMessagesDismissedByIdMember) | **POST** /members/{idMember}/oneTimeMessagesDismissed | addMembersOneTimeMessagesDismissedByIdMember() |
| [**addMembersSavedSearchesByIdMember**](MemberApi.md#addMembersSavedSearchesByIdMember) | **POST** /members/{idMember}/savedSearches | addMembersSavedSearchesByIdMember() |
| [**deleteMembersBoardBackgroundsByIdMemberByIdBoardBackground**](MemberApi.md#deleteMembersBoardBackgroundsByIdMemberByIdBoardBackground) | **DELETE** /members/{idMember}/boardBackgrounds/{idBoardBackground} | deleteMembersBoardBackgroundsByIdMemberByIdBoardBackground() |
| [**deleteMembersBoardStarsByIdMemberByIdBoardStar**](MemberApi.md#deleteMembersBoardStarsByIdMemberByIdBoardStar) | **DELETE** /members/{idMember}/boardStars/{idBoardStar} | deleteMembersBoardStarsByIdMemberByIdBoardStar() |
| [**deleteMembersCustomBoardBackgroundsByIdMemberByIdBoardBackground**](MemberApi.md#deleteMembersCustomBoardBackgroundsByIdMemberByIdBoardBackground) | **DELETE** /members/{idMember}/customBoardBackgrounds/{idBoardBackground} | deleteMembersCustomBoardBackgroundsByIdMemberByIdBoardBackground() |
| [**deleteMembersCustomStickersByIdMemberByIdCustomSticker**](MemberApi.md#deleteMembersCustomStickersByIdMemberByIdCustomSticker) | **DELETE** /members/{idMember}/customStickers/{idCustomSticker} | deleteMembersCustomStickersByIdMemberByIdCustomSticker() |
| [**deleteMembersSavedSearchesByIdMemberByIdSavedSearch**](MemberApi.md#deleteMembersSavedSearchesByIdMemberByIdSavedSearch) | **DELETE** /members/{idMember}/savedSearches/{idSavedSearch} | deleteMembersSavedSearchesByIdMemberByIdSavedSearch() |
| [**getMembersActionsByIdMember**](MemberApi.md#getMembersActionsByIdMember) | **GET** /members/{idMember}/actions | getMembersActionsByIdMember() |
| [**getMembersBoardBackgroundsByIdMember**](MemberApi.md#getMembersBoardBackgroundsByIdMember) | **GET** /members/{idMember}/boardBackgrounds | getMembersBoardBackgroundsByIdMember() |
| [**getMembersBoardBackgroundsByIdMemberByIdBoardBackground**](MemberApi.md#getMembersBoardBackgroundsByIdMemberByIdBoardBackground) | **GET** /members/{idMember}/boardBackgrounds/{idBoardBackground} | getMembersBoardBackgroundsByIdMemberByIdBoardBackground() |
| [**getMembersBoardStarsByIdMember**](MemberApi.md#getMembersBoardStarsByIdMember) | **GET** /members/{idMember}/boardStars | getMembersBoardStarsByIdMember() |
| [**getMembersBoardStarsByIdMemberByIdBoardStar**](MemberApi.md#getMembersBoardStarsByIdMemberByIdBoardStar) | **GET** /members/{idMember}/boardStars/{idBoardStar} | getMembersBoardStarsByIdMemberByIdBoardStar() |
| [**getMembersBoardsByIdMember**](MemberApi.md#getMembersBoardsByIdMember) | **GET** /members/{idMember}/boards | getMembersBoardsByIdMember() |
| [**getMembersBoardsByIdMemberByFilter**](MemberApi.md#getMembersBoardsByIdMemberByFilter) | **GET** /members/{idMember}/boards/{filter} | getMembersBoardsByIdMemberByFilter() |
| [**getMembersBoardsInvitedByIdMember**](MemberApi.md#getMembersBoardsInvitedByIdMember) | **GET** /members/{idMember}/boardsInvited | getMembersBoardsInvitedByIdMember() |
| [**getMembersBoardsInvitedByIdMemberByField**](MemberApi.md#getMembersBoardsInvitedByIdMemberByField) | **GET** /members/{idMember}/boardsInvited/{field} | getMembersBoardsInvitedByIdMemberByField() |
| [**getMembersByIdMember**](MemberApi.md#getMembersByIdMember) | **GET** /members/{idMember} | getMembersByIdMember() |
| [**getMembersByIdMemberByField**](MemberApi.md#getMembersByIdMemberByField) | **GET** /members/{idMember}/{field} | getMembersByIdMemberByField() |
| [**getMembersCardsByIdMember**](MemberApi.md#getMembersCardsByIdMember) | **GET** /members/{idMember}/cards | getMembersCardsByIdMember() |
| [**getMembersCardsByIdMemberByFilter**](MemberApi.md#getMembersCardsByIdMemberByFilter) | **GET** /members/{idMember}/cards/{filter} | getMembersCardsByIdMemberByFilter() |
| [**getMembersCustomBoardBackgroundsByIdMember**](MemberApi.md#getMembersCustomBoardBackgroundsByIdMember) | **GET** /members/{idMember}/customBoardBackgrounds | getMembersCustomBoardBackgroundsByIdMember() |
| [**getMembersCustomBoardBackgroundsByIdMemberByIdBoardBackground**](MemberApi.md#getMembersCustomBoardBackgroundsByIdMemberByIdBoardBackground) | **GET** /members/{idMember}/customBoardBackgrounds/{idBoardBackground} | getMembersCustomBoardBackgroundsByIdMemberByIdBoardBackground() |
| [**getMembersCustomEmojiByIdMember**](MemberApi.md#getMembersCustomEmojiByIdMember) | **GET** /members/{idMember}/customEmoji | getMembersCustomEmojiByIdMember() |
| [**getMembersCustomEmojiByIdMemberByIdCustomEmoji**](MemberApi.md#getMembersCustomEmojiByIdMemberByIdCustomEmoji) | **GET** /members/{idMember}/customEmoji/{idCustomEmoji} | getMembersCustomEmojiByIdMemberByIdCustomEmoji() |
| [**getMembersCustomStickersByIdMember**](MemberApi.md#getMembersCustomStickersByIdMember) | **GET** /members/{idMember}/customStickers | getMembersCustomStickersByIdMember() |
| [**getMembersCustomStickersByIdMemberByIdCustomSticker**](MemberApi.md#getMembersCustomStickersByIdMemberByIdCustomSticker) | **GET** /members/{idMember}/customStickers/{idCustomSticker} | getMembersCustomStickersByIdMemberByIdCustomSticker() |
| [**getMembersDeltasByIdMember**](MemberApi.md#getMembersDeltasByIdMember) | **GET** /members/{idMember}/deltas | getMembersDeltasByIdMember() |
| [**getMembersNotificationsByIdMember**](MemberApi.md#getMembersNotificationsByIdMember) | **GET** /members/{idMember}/notifications | getMembersNotificationsByIdMember() |
| [**getMembersNotificationsByIdMemberByFilter**](MemberApi.md#getMembersNotificationsByIdMemberByFilter) | **GET** /members/{idMember}/notifications/{filter} | getMembersNotificationsByIdMemberByFilter() |
| [**getMembersOrganizationsByIdMember**](MemberApi.md#getMembersOrganizationsByIdMember) | **GET** /members/{idMember}/organizations | getMembersOrganizationsByIdMember() |
| [**getMembersOrganizationsByIdMemberByFilter**](MemberApi.md#getMembersOrganizationsByIdMemberByFilter) | **GET** /members/{idMember}/organizations/{filter} | getMembersOrganizationsByIdMemberByFilter() |
| [**getMembersOrganizationsInvitedByIdMember**](MemberApi.md#getMembersOrganizationsInvitedByIdMember) | **GET** /members/{idMember}/organizationsInvited | getMembersOrganizationsInvitedByIdMember() |
| [**getMembersOrganizationsInvitedByIdMemberByField**](MemberApi.md#getMembersOrganizationsInvitedByIdMemberByField) | **GET** /members/{idMember}/organizationsInvited/{field} | getMembersOrganizationsInvitedByIdMemberByField() |
| [**getMembersSavedSearchesByIdMember**](MemberApi.md#getMembersSavedSearchesByIdMember) | **GET** /members/{idMember}/savedSearches | getMembersSavedSearchesByIdMember() |
| [**getMembersSavedSearchesByIdMemberByIdSavedSearch**](MemberApi.md#getMembersSavedSearchesByIdMemberByIdSavedSearch) | **GET** /members/{idMember}/savedSearches/{idSavedSearch} | getMembersSavedSearchesByIdMemberByIdSavedSearch() |
| [**getMembersTokensByIdMember**](MemberApi.md#getMembersTokensByIdMember) | **GET** /members/{idMember}/tokens | getMembersTokensByIdMember() |
| [**updateMembersAvatarSourceByIdMember**](MemberApi.md#updateMembersAvatarSourceByIdMember) | **PUT** /members/{idMember}/avatarSource | updateMembersAvatarSourceByIdMember() |
| [**updateMembersBioByIdMember**](MemberApi.md#updateMembersBioByIdMember) | **PUT** /members/{idMember}/bio | updateMembersBioByIdMember() |
| [**updateMembersBoardBackgroundsByIdMemberByIdBoardBackground**](MemberApi.md#updateMembersBoardBackgroundsByIdMemberByIdBoardBackground) | **PUT** /members/{idMember}/boardBackgrounds/{idBoardBackground} | updateMembersBoardBackgroundsByIdMemberByIdBoardBackground() |
| [**updateMembersBoardStarsByIdMemberByIdBoardStar**](MemberApi.md#updateMembersBoardStarsByIdMemberByIdBoardStar) | **PUT** /members/{idMember}/boardStars/{idBoardStar} | updateMembersBoardStarsByIdMemberByIdBoardStar() |
| [**updateMembersBoardStarsIdBoardByIdMemberByIdBoardStar**](MemberApi.md#updateMembersBoardStarsIdBoardByIdMemberByIdBoardStar) | **PUT** /members/{idMember}/boardStars/{idBoardStar}/idBoard | updateMembersBoardStarsIdBoardByIdMemberByIdBoardStar() |
| [**updateMembersBoardStarsPosByIdMemberByIdBoardStar**](MemberApi.md#updateMembersBoardStarsPosByIdMemberByIdBoardStar) | **PUT** /members/{idMember}/boardStars/{idBoardStar}/pos | updateMembersBoardStarsPosByIdMemberByIdBoardStar() |
| [**updateMembersByIdMember**](MemberApi.md#updateMembersByIdMember) | **PUT** /members/{idMember} | updateMembersByIdMember() |
| [**updateMembersCustomBoardBackgroundsByIdMemberByIdBoardBackground**](MemberApi.md#updateMembersCustomBoardBackgroundsByIdMemberByIdBoardBackground) | **PUT** /members/{idMember}/customBoardBackgrounds/{idBoardBackground} | updateMembersCustomBoardBackgroundsByIdMemberByIdBoardBackground() |
| [**updateMembersFullNameByIdMember**](MemberApi.md#updateMembersFullNameByIdMember) | **PUT** /members/{idMember}/fullName | updateMembersFullNameByIdMember() |
| [**updateMembersInitialsByIdMember**](MemberApi.md#updateMembersInitialsByIdMember) | **PUT** /members/{idMember}/initials | updateMembersInitialsByIdMember() |
| [**updateMembersPrefsColorBlindByIdMember**](MemberApi.md#updateMembersPrefsColorBlindByIdMember) | **PUT** /members/{idMember}/prefs/colorBlind | updateMembersPrefsColorBlindByIdMember() |
| [**updateMembersPrefsLocaleByIdMember**](MemberApi.md#updateMembersPrefsLocaleByIdMember) | **PUT** /members/{idMember}/prefs/locale | updateMembersPrefsLocaleByIdMember() |
| [**updateMembersPrefsMinutesBetweenSummariesByIdMember**](MemberApi.md#updateMembersPrefsMinutesBetweenSummariesByIdMember) | **PUT** /members/{idMember}/prefs/minutesBetweenSummaries | updateMembersPrefsMinutesBetweenSummariesByIdMember() |
| [**updateMembersSavedSearchesByIdMemberByIdSavedSearch**](MemberApi.md#updateMembersSavedSearchesByIdMemberByIdSavedSearch) | **PUT** /members/{idMember}/savedSearches/{idSavedSearch} | updateMembersSavedSearchesByIdMemberByIdSavedSearch() |
| [**updateMembersSavedSearchesNameByIdMemberByIdSavedSearch**](MemberApi.md#updateMembersSavedSearchesNameByIdMemberByIdSavedSearch) | **PUT** /members/{idMember}/savedSearches/{idSavedSearch}/name | updateMembersSavedSearchesNameByIdMemberByIdSavedSearch() |
| [**updateMembersSavedSearchesPosByIdMemberByIdSavedSearch**](MemberApi.md#updateMembersSavedSearchesPosByIdMemberByIdSavedSearch) | **PUT** /members/{idMember}/savedSearches/{idSavedSearch}/pos | updateMembersSavedSearchesPosByIdMemberByIdSavedSearch() |
| [**updateMembersSavedSearchesQueryByIdMemberByIdSavedSearch**](MemberApi.md#updateMembersSavedSearchesQueryByIdMemberByIdSavedSearch) | **PUT** /members/{idMember}/savedSearches/{idSavedSearch}/query | updateMembersSavedSearchesQueryByIdMemberByIdSavedSearch() |
| [**updateMembersUsernameByIdMember**](MemberApi.md#updateMembersUsernameByIdMember) | **PUT** /members/{idMember}/username | updateMembersUsernameByIdMember() |


<a id="addMembersAvatarByIdMember"></a>
# **addMembersAvatarByIdMember**
> addMembersAvatarByIdMember(idMember, key, token, membersAvatar)

addMembersAvatarByIdMember()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    MembersAvatar membersAvatar = new MembersAvatar(); // MembersAvatar | Attributes of \"Members Avatar\" to be added.
    try {
      apiInstance.addMembersAvatarByIdMember(idMember, key, token, membersAvatar);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#addMembersAvatarByIdMember");
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
| **idMember** | **String**| idMember or username | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **membersAvatar** | [**MembersAvatar**](MembersAvatar.md)| Attributes of \&quot;Members Avatar\&quot; to be added. | |

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

<a id="addMembersBoardBackgroundsByIdMember"></a>
# **addMembersBoardBackgroundsByIdMember**
> addMembersBoardBackgroundsByIdMember(idMember, key, token, membersBoardBackgrounds)

addMembersBoardBackgroundsByIdMember()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    MembersBoardBackgrounds membersBoardBackgrounds = new MembersBoardBackgrounds(); // MembersBoardBackgrounds | Attributes of \"Members Board Backgrounds\" to be added.
    try {
      apiInstance.addMembersBoardBackgroundsByIdMember(idMember, key, token, membersBoardBackgrounds);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#addMembersBoardBackgroundsByIdMember");
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
| **idMember** | **String**| idMember or username | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **membersBoardBackgrounds** | [**MembersBoardBackgrounds**](MembersBoardBackgrounds.md)| Attributes of \&quot;Members Board Backgrounds\&quot; to be added. | |

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

<a id="addMembersBoardStarsByIdMember"></a>
# **addMembersBoardStarsByIdMember**
> addMembersBoardStarsByIdMember(idMember, key, token, membersBoardStars)

addMembersBoardStarsByIdMember()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    MembersBoardStars membersBoardStars = new MembersBoardStars(); // MembersBoardStars | Attributes of \"Members Board Stars\" to be added.
    try {
      apiInstance.addMembersBoardStarsByIdMember(idMember, key, token, membersBoardStars);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#addMembersBoardStarsByIdMember");
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
| **idMember** | **String**| idMember or username | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **membersBoardStars** | [**MembersBoardStars**](MembersBoardStars.md)| Attributes of \&quot;Members Board Stars\&quot; to be added. | |

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

<a id="addMembersCustomBoardBackgroundsByIdMember"></a>
# **addMembersCustomBoardBackgroundsByIdMember**
> addMembersCustomBoardBackgroundsByIdMember(idMember, key, token, membersCustomBoardBackgrounds)

addMembersCustomBoardBackgroundsByIdMember()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    MembersCustomBoardBackgrounds membersCustomBoardBackgrounds = new MembersCustomBoardBackgrounds(); // MembersCustomBoardBackgrounds | Attributes of \"Members Custom Board Backgrounds\" to be added.
    try {
      apiInstance.addMembersCustomBoardBackgroundsByIdMember(idMember, key, token, membersCustomBoardBackgrounds);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#addMembersCustomBoardBackgroundsByIdMember");
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
| **idMember** | **String**| idMember or username | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **membersCustomBoardBackgrounds** | [**MembersCustomBoardBackgrounds**](MembersCustomBoardBackgrounds.md)| Attributes of \&quot;Members Custom Board Backgrounds\&quot; to be added. | |

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

<a id="addMembersCustomEmojiByIdMember"></a>
# **addMembersCustomEmojiByIdMember**
> addMembersCustomEmojiByIdMember(idMember, key, token, membersCustomEmoji)

addMembersCustomEmojiByIdMember()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    MembersCustomEmoji membersCustomEmoji = new MembersCustomEmoji(); // MembersCustomEmoji | Attributes of \"Members Custom Emoji\" to be added.
    try {
      apiInstance.addMembersCustomEmojiByIdMember(idMember, key, token, membersCustomEmoji);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#addMembersCustomEmojiByIdMember");
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
| **idMember** | **String**| idMember or username | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **membersCustomEmoji** | [**MembersCustomEmoji**](MembersCustomEmoji.md)| Attributes of \&quot;Members Custom Emoji\&quot; to be added. | |

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

<a id="addMembersCustomStickersByIdMember"></a>
# **addMembersCustomStickersByIdMember**
> addMembersCustomStickersByIdMember(idMember, key, token, membersCustomStickers)

addMembersCustomStickersByIdMember()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    MembersCustomStickers membersCustomStickers = new MembersCustomStickers(); // MembersCustomStickers | Attributes of \"Members Custom Stickers\" to be added.
    try {
      apiInstance.addMembersCustomStickersByIdMember(idMember, key, token, membersCustomStickers);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#addMembersCustomStickersByIdMember");
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
| **idMember** | **String**| idMember or username | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **membersCustomStickers** | [**MembersCustomStickers**](MembersCustomStickers.md)| Attributes of \&quot;Members Custom Stickers\&quot; to be added. | |

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

<a id="addMembersOneTimeMessagesDismissedByIdMember"></a>
# **addMembersOneTimeMessagesDismissedByIdMember**
> addMembersOneTimeMessagesDismissedByIdMember(idMember, key, token, membersOneTimeMessagesDismissed)

addMembersOneTimeMessagesDismissedByIdMember()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    MembersOneTimeMessagesDismissed membersOneTimeMessagesDismissed = new MembersOneTimeMessagesDismissed(); // MembersOneTimeMessagesDismissed | Attributes of \"Members One Time Messages Dismissed\" to be added.
    try {
      apiInstance.addMembersOneTimeMessagesDismissedByIdMember(idMember, key, token, membersOneTimeMessagesDismissed);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#addMembersOneTimeMessagesDismissedByIdMember");
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
| **idMember** | **String**| idMember or username | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **membersOneTimeMessagesDismissed** | [**MembersOneTimeMessagesDismissed**](MembersOneTimeMessagesDismissed.md)| Attributes of \&quot;Members One Time Messages Dismissed\&quot; to be added. | |

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

<a id="addMembersSavedSearchesByIdMember"></a>
# **addMembersSavedSearchesByIdMember**
> addMembersSavedSearchesByIdMember(idMember, key, token, membersSavedSearches)

addMembersSavedSearchesByIdMember()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    MembersSavedSearches membersSavedSearches = new MembersSavedSearches(); // MembersSavedSearches | Attributes of \"Members Saved Searches\" to be added.
    try {
      apiInstance.addMembersSavedSearchesByIdMember(idMember, key, token, membersSavedSearches);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#addMembersSavedSearchesByIdMember");
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
| **idMember** | **String**| idMember or username | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **membersSavedSearches** | [**MembersSavedSearches**](MembersSavedSearches.md)| Attributes of \&quot;Members Saved Searches\&quot; to be added. | |

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

<a id="deleteMembersBoardBackgroundsByIdMemberByIdBoardBackground"></a>
# **deleteMembersBoardBackgroundsByIdMemberByIdBoardBackground**
> deleteMembersBoardBackgroundsByIdMemberByIdBoardBackground(idMember, idBoardBackground, key, token)

deleteMembersBoardBackgroundsByIdMemberByIdBoardBackground()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String idBoardBackground = "idBoardBackground_example"; // String | idBoardBackground
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    try {
      apiInstance.deleteMembersBoardBackgroundsByIdMemberByIdBoardBackground(idMember, idBoardBackground, key, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#deleteMembersBoardBackgroundsByIdMemberByIdBoardBackground");
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
| **idMember** | **String**| idMember or username | |
| **idBoardBackground** | **String**| idBoardBackground | |
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

<a id="deleteMembersBoardStarsByIdMemberByIdBoardStar"></a>
# **deleteMembersBoardStarsByIdMemberByIdBoardStar**
> deleteMembersBoardStarsByIdMemberByIdBoardStar(idMember, idBoardStar, key, token)

deleteMembersBoardStarsByIdMemberByIdBoardStar()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String idBoardStar = "idBoardStar_example"; // String | idBoardStar
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    try {
      apiInstance.deleteMembersBoardStarsByIdMemberByIdBoardStar(idMember, idBoardStar, key, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#deleteMembersBoardStarsByIdMemberByIdBoardStar");
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
| **idMember** | **String**| idMember or username | |
| **idBoardStar** | **String**| idBoardStar | |
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

<a id="deleteMembersCustomBoardBackgroundsByIdMemberByIdBoardBackground"></a>
# **deleteMembersCustomBoardBackgroundsByIdMemberByIdBoardBackground**
> deleteMembersCustomBoardBackgroundsByIdMemberByIdBoardBackground(idMember, idBoardBackground, key, token)

deleteMembersCustomBoardBackgroundsByIdMemberByIdBoardBackground()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String idBoardBackground = "idBoardBackground_example"; // String | idBoardBackground
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    try {
      apiInstance.deleteMembersCustomBoardBackgroundsByIdMemberByIdBoardBackground(idMember, idBoardBackground, key, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#deleteMembersCustomBoardBackgroundsByIdMemberByIdBoardBackground");
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
| **idMember** | **String**| idMember or username | |
| **idBoardBackground** | **String**| idBoardBackground | |
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

<a id="deleteMembersCustomStickersByIdMemberByIdCustomSticker"></a>
# **deleteMembersCustomStickersByIdMemberByIdCustomSticker**
> deleteMembersCustomStickersByIdMemberByIdCustomSticker(idMember, idCustomSticker, key, token)

deleteMembersCustomStickersByIdMemberByIdCustomSticker()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String idCustomSticker = "idCustomSticker_example"; // String | idCustomSticker
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    try {
      apiInstance.deleteMembersCustomStickersByIdMemberByIdCustomSticker(idMember, idCustomSticker, key, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#deleteMembersCustomStickersByIdMemberByIdCustomSticker");
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
| **idMember** | **String**| idMember or username | |
| **idCustomSticker** | **String**| idCustomSticker | |
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

<a id="deleteMembersSavedSearchesByIdMemberByIdSavedSearch"></a>
# **deleteMembersSavedSearchesByIdMemberByIdSavedSearch**
> deleteMembersSavedSearchesByIdMemberByIdSavedSearch(idMember, idSavedSearch, key, token)

deleteMembersSavedSearchesByIdMemberByIdSavedSearch()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String idSavedSearch = "idSavedSearch_example"; // String | idSavedSearch
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    try {
      apiInstance.deleteMembersSavedSearchesByIdMemberByIdSavedSearch(idMember, idSavedSearch, key, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#deleteMembersSavedSearchesByIdMemberByIdSavedSearch");
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
| **idMember** | **String**| idMember or username | |
| **idSavedSearch** | **String**| idSavedSearch | |
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

<a id="getMembersActionsByIdMember"></a>
# **getMembersActionsByIdMember**
> getMembersActionsByIdMember(idMember, key, token, entities, display, filter, fields, limit, format, since, before, page, idModels, member, memberFields, memberCreator, memberCreatorFields)

getMembersActionsByIdMember()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
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
      apiInstance.getMembersActionsByIdMember(idMember, key, token, entities, display, filter, fields, limit, format, since, before, page, idModels, member, memberFields, memberCreator, memberCreatorFields);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#getMembersActionsByIdMember");
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
| **idMember** | **String**| idMember or username | |
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

<a id="getMembersBoardBackgroundsByIdMember"></a>
# **getMembersBoardBackgroundsByIdMember**
> getMembersBoardBackgroundsByIdMember(idMember, key, token, filter)

getMembersBoardBackgroundsByIdMember()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    String filter = "all"; // String | One of: all, custom, default, none or premium
    try {
      apiInstance.getMembersBoardBackgroundsByIdMember(idMember, key, token, filter);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#getMembersBoardBackgroundsByIdMember");
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
| **idMember** | **String**| idMember or username | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **filter** | **String**| One of: all, custom, default, none or premium | [optional] [default to all] |

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

<a id="getMembersBoardBackgroundsByIdMemberByIdBoardBackground"></a>
# **getMembersBoardBackgroundsByIdMemberByIdBoardBackground**
> getMembersBoardBackgroundsByIdMemberByIdBoardBackground(idMember, idBoardBackground, key, token, fields)

getMembersBoardBackgroundsByIdMemberByIdBoardBackground()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String idBoardBackground = "idBoardBackground_example"; // String | idBoardBackground
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    String fields = "all"; // String | all or a comma-separated list of: brightness, fullSizeUrl, scaled or tile
    try {
      apiInstance.getMembersBoardBackgroundsByIdMemberByIdBoardBackground(idMember, idBoardBackground, key, token, fields);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#getMembersBoardBackgroundsByIdMemberByIdBoardBackground");
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
| **idMember** | **String**| idMember or username | |
| **idBoardBackground** | **String**| idBoardBackground | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **fields** | **String**| all or a comma-separated list of: brightness, fullSizeUrl, scaled or tile | [optional] [default to all] |

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

<a id="getMembersBoardStarsByIdMember"></a>
# **getMembersBoardStarsByIdMember**
> getMembersBoardStarsByIdMember(idMember, key, token)

getMembersBoardStarsByIdMember()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    try {
      apiInstance.getMembersBoardStarsByIdMember(idMember, key, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#getMembersBoardStarsByIdMember");
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
| **idMember** | **String**| idMember or username | |
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

<a id="getMembersBoardStarsByIdMemberByIdBoardStar"></a>
# **getMembersBoardStarsByIdMemberByIdBoardStar**
> getMembersBoardStarsByIdMemberByIdBoardStar(idMember, idBoardStar, key, token)

getMembersBoardStarsByIdMemberByIdBoardStar()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String idBoardStar = "idBoardStar_example"; // String | idBoardStar
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    try {
      apiInstance.getMembersBoardStarsByIdMemberByIdBoardStar(idMember, idBoardStar, key, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#getMembersBoardStarsByIdMemberByIdBoardStar");
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
| **idMember** | **String**| idMember or username | |
| **idBoardStar** | **String**| idBoardStar | |
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

<a id="getMembersBoardsByIdMember"></a>
# **getMembersBoardsByIdMember**
> getMembersBoardsByIdMember(idMember, key, token, filter, fields, actions, actionsEntities, actionsLimit, actionsFormat, actionsSince, actionFields, memberships, organization, organizationFields, lists)

getMembersBoardsByIdMember()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    String filter = "all"; // String | all or a comma-separated list of: closed, members, open, organization, pinned, public, starred or unpinned
    String fields = "all"; // String | all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url
    String actions = "actions_example"; // String | all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization
    String actionsEntities = "actionsEntities_example"; // String |  true or false
    String actionsLimit = "50"; // String | a number from 0 to 1000
    String actionsFormat = "list"; // String | One of: count, list or minimal
    String actionsSince = "actionsSince_example"; // String | A date, null or lastView
    String actionFields = "all"; // String | all or a comma-separated list of: data, date, idMemberCreator or type
    String memberships = "none"; // String | all or a comma-separated list of: active, admin, deactivated, me or normal
    String organization = "organization_example"; // String |  true or false
    String organizationFields = "name and displayName"; // String | all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website
    String lists = "none"; // String | One of: all, closed, none or open
    try {
      apiInstance.getMembersBoardsByIdMember(idMember, key, token, filter, fields, actions, actionsEntities, actionsLimit, actionsFormat, actionsSince, actionFields, memberships, organization, organizationFields, lists);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#getMembersBoardsByIdMember");
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
| **idMember** | **String**| idMember or username | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **filter** | **String**| all or a comma-separated list of: closed, members, open, organization, pinned, public, starred or unpinned | [optional] [default to all] |
| **fields** | **String**| all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url | [optional] [default to all] |
| **actions** | **String**| all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization | [optional] |
| **actionsEntities** | **String**|  true or false | [optional] |
| **actionsLimit** | **String**| a number from 0 to 1000 | [optional] [default to 50] |
| **actionsFormat** | **String**| One of: count, list or minimal | [optional] [default to list] |
| **actionsSince** | **String**| A date, null or lastView | [optional] |
| **actionFields** | **String**| all or a comma-separated list of: data, date, idMemberCreator or type | [optional] [default to all] |
| **memberships** | **String**| all or a comma-separated list of: active, admin, deactivated, me or normal | [optional] [default to none] |
| **organization** | **String**|  true or false | [optional] |
| **organizationFields** | **String**| all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website | [optional] [default to name and displayName] |
| **lists** | **String**| One of: all, closed, none or open | [optional] [default to none] |

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

<a id="getMembersBoardsByIdMemberByFilter"></a>
# **getMembersBoardsByIdMemberByFilter**
> getMembersBoardsByIdMemberByFilter(idMember, filter, key, token)

getMembersBoardsByIdMemberByFilter()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String filter = "filter_example"; // String | filter
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    try {
      apiInstance.getMembersBoardsByIdMemberByFilter(idMember, filter, key, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#getMembersBoardsByIdMemberByFilter");
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
| **idMember** | **String**| idMember or username | |
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

<a id="getMembersBoardsInvitedByIdMember"></a>
# **getMembersBoardsInvitedByIdMember**
> getMembersBoardsInvitedByIdMember(idMember, key, token, fields)

getMembersBoardsInvitedByIdMember()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    String fields = "all"; // String | all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url
    try {
      apiInstance.getMembersBoardsInvitedByIdMember(idMember, key, token, fields);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#getMembersBoardsInvitedByIdMember");
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
| **idMember** | **String**| idMember or username | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **fields** | **String**| all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url | [optional] [default to all] |

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

<a id="getMembersBoardsInvitedByIdMemberByField"></a>
# **getMembersBoardsInvitedByIdMemberByField**
> getMembersBoardsInvitedByIdMemberByField(idMember, field, key, token)

getMembersBoardsInvitedByIdMemberByField()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String field = "field_example"; // String | field
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    try {
      apiInstance.getMembersBoardsInvitedByIdMemberByField(idMember, field, key, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#getMembersBoardsInvitedByIdMemberByField");
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
| **idMember** | **String**| idMember or username | |
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

<a id="getMembersByIdMember"></a>
# **getMembersByIdMember**
> getMembersByIdMember(idMember, key, token, actions, actionsEntities, actionsDisplay, actionsLimit, actionFields, actionSince, actionBefore, cards, cardFields, cardMembers, cardMemberFields, cardAttachments, cardAttachmentFields, cardStickers, boards, boardFields, boardActions, boardActionsEntities, boardActionsDisplay, boardActionsFormat, boardActionsSince, boardActionsLimit, boardActionFields, boardLists, boardMemberships, boardOrganization, boardOrganizationFields, boardsInvited, boardsInvitedFields, boardStars, savedSearches, organizations, organizationFields, organizationPaidAccount, organizationsInvited, organizationsInvitedFields, notifications, notificationsEntities, notificationsDisplay, notificationsLimit, notificationFields, notificationMemberCreator, notificationMemberCreatorFields, notificationBefore, notificationSince, tokens, paidAccount, boardBackgrounds, customBoardBackgrounds, customStickers, customEmoji, fields)

getMembersByIdMember()

If you specify &#39;me&#39; as the username, this call will respond as if you had supplied the username associated with the supplied token

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    String actions = "actions_example"; // String | all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization
    String actionsEntities = "actionsEntities_example"; // String |  true or false
    String actionsDisplay = "actionsDisplay_example"; // String |  true or false
    String actionsLimit = "50"; // String | a number from 0 to 1000
    String actionFields = "all"; // String | all or a comma-separated list of: data, date, idMemberCreator or type
    String actionSince = "actionSince_example"; // String | A date, null or lastView
    String actionBefore = "actionBefore_example"; // String | A date, or null
    String cards = "none"; // String | One of: all, closed, none, open or visible
    String cardFields = "all"; // String | all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url
    String cardMembers = "cardMembers_example"; // String |  true or false
    String cardMemberFields = "avatarHash, fullName, initials and username"; // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
    String cardAttachments = "cardAttachments_example"; // String | A boolean value or &quot;cover&quot; for only card cover attachments
    String cardAttachmentFields = "url and previews"; // String | all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url
    String cardStickers = "cardStickers_example"; // String |  true or false
    String boards = "boards_example"; // String | all or a comma-separated list of: closed, members, open, organization, pinned, public, starred or unpinned
    String boardFields = "name, closed, idOrganization and pinned"; // String | all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url
    String boardActions = "boardActions_example"; // String | all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization
    String boardActionsEntities = "boardActionsEntities_example"; // String |  true or false
    String boardActionsDisplay = "boardActionsDisplay_example"; // String |  true or false
    String boardActionsFormat = "list"; // String | One of: count, list or minimal
    String boardActionsSince = "boardActionsSince_example"; // String | A date, null or lastView
    String boardActionsLimit = "50"; // String | a number from 0 to 1000
    String boardActionFields = "all"; // String | all or a comma-separated list of: data, date, idMemberCreator or type
    String boardLists = "none"; // String | One of: all, closed, none or open
    String boardMemberships = "none"; // String | all or a comma-separated list of: active, admin, deactivated, me or normal
    String boardOrganization = "boardOrganization_example"; // String |  true or false
    String boardOrganizationFields = "name and displayName"; // String | all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website
    String boardsInvited = "boardsInvited_example"; // String | all or a comma-separated list of: closed, members, open, organization, pinned, public, starred or unpinned
    String boardsInvitedFields = "name, closed, idOrganization and pinned"; // String | all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url
    String boardStars = "boardStars_example"; // String |  true or false
    String savedSearches = "savedSearches_example"; // String |  true or false
    String organizations = "none"; // String | One of: all, members, none or public
    String organizationFields = "all"; // String | all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website
    String organizationPaidAccount = "organizationPaidAccount_example"; // String |  true or false
    String organizationsInvited = "none"; // String | One of: all, members, none or public
    String organizationsInvitedFields = "all"; // String | all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website
    String notifications = "notifications_example"; // String | all or a comma-separated list of: addAdminToBoard, addAdminToOrganization, addedAttachmentToCard, addedMemberToCard, addedToBoard, addedToCard, addedToOrganization, cardDueSoon, changeCard, closeBoard, commentCard, createdCard, declinedInvitationToBoard, declinedInvitationToOrganization, invitedToBoard, invitedToOrganization, makeAdminOfBoard, makeAdminOfOrganization, memberJoinedTrello, mentionedOnCard, removedFromBoard, removedFromCard, removedFromOrganization, removedMemberFromCard, unconfirmedInvitedToBoard, unconfirmedInvitedToOrganization or updateCheckItemStateOnCard
    String notificationsEntities = "notificationsEntities_example"; // String |  true or false
    String notificationsDisplay = "notificationsDisplay_example"; // String |  true or false
    String notificationsLimit = "50"; // String | a number from 1 to 1000
    String notificationFields = "all"; // String | all or a comma-separated list of: data, date, idMemberCreator, type or unread
    String notificationMemberCreator = "notificationMemberCreator_example"; // String |  true or false
    String notificationMemberCreatorFields = "avatarHash, fullName, initials and username"; // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
    String notificationBefore = "notificationBefore_example"; // String | An id, or null
    String notificationSince = "notificationSince_example"; // String | An id, or null
    String tokens = "none"; // String | One of: all or none
    String paidAccount = "paidAccount_example"; // String |  true or false
    String boardBackgrounds = "none"; // String | One of: all, custom, default, none or premium
    String customBoardBackgrounds = "none"; // String | One of: all or none
    String customStickers = "none"; // String | One of: all or none
    String customEmoji = "none"; // String | One of: all or none
    String fields = "all"; // String | all or a comma-separated list of: avatarHash, avatarSource, bio, bioData, confirmed, email, fullName, gravatarHash, idBoards, idBoardsPinned, idOrganizations, idPremOrgsAdmin, initials, loginTypes, memberType, oneTimeMessagesDismissed, prefs, premiumFeatures, products, status, status, trophies, uploadedAvatarHash, url or username
    try {
      apiInstance.getMembersByIdMember(idMember, key, token, actions, actionsEntities, actionsDisplay, actionsLimit, actionFields, actionSince, actionBefore, cards, cardFields, cardMembers, cardMemberFields, cardAttachments, cardAttachmentFields, cardStickers, boards, boardFields, boardActions, boardActionsEntities, boardActionsDisplay, boardActionsFormat, boardActionsSince, boardActionsLimit, boardActionFields, boardLists, boardMemberships, boardOrganization, boardOrganizationFields, boardsInvited, boardsInvitedFields, boardStars, savedSearches, organizations, organizationFields, organizationPaidAccount, organizationsInvited, organizationsInvitedFields, notifications, notificationsEntities, notificationsDisplay, notificationsLimit, notificationFields, notificationMemberCreator, notificationMemberCreatorFields, notificationBefore, notificationSince, tokens, paidAccount, boardBackgrounds, customBoardBackgrounds, customStickers, customEmoji, fields);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#getMembersByIdMember");
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
| **idMember** | **String**| idMember or username | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **actions** | **String**| all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization | [optional] |
| **actionsEntities** | **String**|  true or false | [optional] |
| **actionsDisplay** | **String**|  true or false | [optional] |
| **actionsLimit** | **String**| a number from 0 to 1000 | [optional] [default to 50] |
| **actionFields** | **String**| all or a comma-separated list of: data, date, idMemberCreator or type | [optional] [default to all] |
| **actionSince** | **String**| A date, null or lastView | [optional] |
| **actionBefore** | **String**| A date, or null | [optional] |
| **cards** | **String**| One of: all, closed, none, open or visible | [optional] [default to none] |
| **cardFields** | **String**| all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url | [optional] [default to all] |
| **cardMembers** | **String**|  true or false | [optional] |
| **cardMemberFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to avatarHash, fullName, initials and username] |
| **cardAttachments** | **String**| A boolean value or &amp;quot;cover&amp;quot; for only card cover attachments | [optional] |
| **cardAttachmentFields** | **String**| all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url | [optional] [default to url and previews] |
| **cardStickers** | **String**|  true or false | [optional] |
| **boards** | **String**| all or a comma-separated list of: closed, members, open, organization, pinned, public, starred or unpinned | [optional] |
| **boardFields** | **String**| all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url | [optional] [default to name, closed, idOrganization and pinned] |
| **boardActions** | **String**| all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization | [optional] |
| **boardActionsEntities** | **String**|  true or false | [optional] |
| **boardActionsDisplay** | **String**|  true or false | [optional] |
| **boardActionsFormat** | **String**| One of: count, list or minimal | [optional] [default to list] |
| **boardActionsSince** | **String**| A date, null or lastView | [optional] |
| **boardActionsLimit** | **String**| a number from 0 to 1000 | [optional] [default to 50] |
| **boardActionFields** | **String**| all or a comma-separated list of: data, date, idMemberCreator or type | [optional] [default to all] |
| **boardLists** | **String**| One of: all, closed, none or open | [optional] [default to none] |
| **boardMemberships** | **String**| all or a comma-separated list of: active, admin, deactivated, me or normal | [optional] [default to none] |
| **boardOrganization** | **String**|  true or false | [optional] |
| **boardOrganizationFields** | **String**| all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website | [optional] [default to name and displayName] |
| **boardsInvited** | **String**| all or a comma-separated list of: closed, members, open, organization, pinned, public, starred or unpinned | [optional] |
| **boardsInvitedFields** | **String**| all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url | [optional] [default to name, closed, idOrganization and pinned] |
| **boardStars** | **String**|  true or false | [optional] |
| **savedSearches** | **String**|  true or false | [optional] |
| **organizations** | **String**| One of: all, members, none or public | [optional] [default to none] |
| **organizationFields** | **String**| all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website | [optional] [default to all] |
| **organizationPaidAccount** | **String**|  true or false | [optional] |
| **organizationsInvited** | **String**| One of: all, members, none or public | [optional] [default to none] |
| **organizationsInvitedFields** | **String**| all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website | [optional] [default to all] |
| **notifications** | **String**| all or a comma-separated list of: addAdminToBoard, addAdminToOrganization, addedAttachmentToCard, addedMemberToCard, addedToBoard, addedToCard, addedToOrganization, cardDueSoon, changeCard, closeBoard, commentCard, createdCard, declinedInvitationToBoard, declinedInvitationToOrganization, invitedToBoard, invitedToOrganization, makeAdminOfBoard, makeAdminOfOrganization, memberJoinedTrello, mentionedOnCard, removedFromBoard, removedFromCard, removedFromOrganization, removedMemberFromCard, unconfirmedInvitedToBoard, unconfirmedInvitedToOrganization or updateCheckItemStateOnCard | [optional] |
| **notificationsEntities** | **String**|  true or false | [optional] |
| **notificationsDisplay** | **String**|  true or false | [optional] |
| **notificationsLimit** | **String**| a number from 1 to 1000 | [optional] [default to 50] |
| **notificationFields** | **String**| all or a comma-separated list of: data, date, idMemberCreator, type or unread | [optional] [default to all] |
| **notificationMemberCreator** | **String**|  true or false | [optional] |
| **notificationMemberCreatorFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to avatarHash, fullName, initials and username] |
| **notificationBefore** | **String**| An id, or null | [optional] |
| **notificationSince** | **String**| An id, or null | [optional] |
| **tokens** | **String**| One of: all or none | [optional] [default to none] |
| **paidAccount** | **String**|  true or false | [optional] |
| **boardBackgrounds** | **String**| One of: all, custom, default, none or premium | [optional] [default to none] |
| **customBoardBackgrounds** | **String**| One of: all or none | [optional] [default to none] |
| **customStickers** | **String**| One of: all or none | [optional] [default to none] |
| **customEmoji** | **String**| One of: all or none | [optional] [default to none] |
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

<a id="getMembersByIdMemberByField"></a>
# **getMembersByIdMemberByField**
> getMembersByIdMemberByField(idMember, field, key, token)

getMembersByIdMemberByField()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String field = "field_example"; // String | field
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    try {
      apiInstance.getMembersByIdMemberByField(idMember, field, key, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#getMembersByIdMemberByField");
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
| **idMember** | **String**| idMember or username | |
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

<a id="getMembersCardsByIdMember"></a>
# **getMembersCardsByIdMember**
> getMembersCardsByIdMember(idMember, key, token, actions, attachments, attachmentFields, stickers, members, memberFields, checkItemStates, checklists, limit, since, before, filter, fields)

getMembersCardsByIdMember()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
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
      apiInstance.getMembersCardsByIdMember(idMember, key, token, actions, attachments, attachmentFields, stickers, members, memberFields, checkItemStates, checklists, limit, since, before, filter, fields);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#getMembersCardsByIdMember");
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
| **idMember** | **String**| idMember or username | |
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

<a id="getMembersCardsByIdMemberByFilter"></a>
# **getMembersCardsByIdMemberByFilter**
> getMembersCardsByIdMemberByFilter(idMember, filter, key, token)

getMembersCardsByIdMemberByFilter()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String filter = "filter_example"; // String | filter
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    try {
      apiInstance.getMembersCardsByIdMemberByFilter(idMember, filter, key, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#getMembersCardsByIdMemberByFilter");
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
| **idMember** | **String**| idMember or username | |
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

<a id="getMembersCustomBoardBackgroundsByIdMember"></a>
# **getMembersCustomBoardBackgroundsByIdMember**
> getMembersCustomBoardBackgroundsByIdMember(idMember, key, token, filter)

getMembersCustomBoardBackgroundsByIdMember()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    String filter = "all"; // String | One of: all or none
    try {
      apiInstance.getMembersCustomBoardBackgroundsByIdMember(idMember, key, token, filter);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#getMembersCustomBoardBackgroundsByIdMember");
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
| **idMember** | **String**| idMember or username | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **filter** | **String**| One of: all or none | [optional] [default to all] |

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

<a id="getMembersCustomBoardBackgroundsByIdMemberByIdBoardBackground"></a>
# **getMembersCustomBoardBackgroundsByIdMemberByIdBoardBackground**
> getMembersCustomBoardBackgroundsByIdMemberByIdBoardBackground(idMember, idBoardBackground, key, token, fields)

getMembersCustomBoardBackgroundsByIdMemberByIdBoardBackground()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String idBoardBackground = "idBoardBackground_example"; // String | idBoardBackground
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    String fields = "all"; // String | all or a comma-separated list of: brightness, fullSizeUrl, scaled or tile
    try {
      apiInstance.getMembersCustomBoardBackgroundsByIdMemberByIdBoardBackground(idMember, idBoardBackground, key, token, fields);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#getMembersCustomBoardBackgroundsByIdMemberByIdBoardBackground");
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
| **idMember** | **String**| idMember or username | |
| **idBoardBackground** | **String**| idBoardBackground | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **fields** | **String**| all or a comma-separated list of: brightness, fullSizeUrl, scaled or tile | [optional] [default to all] |

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

<a id="getMembersCustomEmojiByIdMember"></a>
# **getMembersCustomEmojiByIdMember**
> getMembersCustomEmojiByIdMember(idMember, key, token, filter)

getMembersCustomEmojiByIdMember()

This gets the list of all of the user’s uploaded emoji

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    String filter = "all"; // String | One of: all or none
    try {
      apiInstance.getMembersCustomEmojiByIdMember(idMember, key, token, filter);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#getMembersCustomEmojiByIdMember");
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
| **idMember** | **String**| idMember or username | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **filter** | **String**| One of: all or none | [optional] [default to all] |

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

<a id="getMembersCustomEmojiByIdMemberByIdCustomEmoji"></a>
# **getMembersCustomEmojiByIdMemberByIdCustomEmoji**
> getMembersCustomEmojiByIdMemberByIdCustomEmoji(idMember, idCustomEmoji, key, token, fields)

getMembersCustomEmojiByIdMemberByIdCustomEmoji()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String idCustomEmoji = "idCustomEmoji_example"; // String | idCustomEmoji
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    String fields = "all"; // String | all or a comma-separated list of: name or url
    try {
      apiInstance.getMembersCustomEmojiByIdMemberByIdCustomEmoji(idMember, idCustomEmoji, key, token, fields);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#getMembersCustomEmojiByIdMemberByIdCustomEmoji");
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
| **idMember** | **String**| idMember or username | |
| **idCustomEmoji** | **String**| idCustomEmoji | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **fields** | **String**| all or a comma-separated list of: name or url | [optional] [default to all] |

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

<a id="getMembersCustomStickersByIdMember"></a>
# **getMembersCustomStickersByIdMember**
> getMembersCustomStickersByIdMember(idMember, key, token, filter)

getMembersCustomStickersByIdMember()

This gets a list of all of the user’s uploaded stickers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    String filter = "all"; // String | One of: all or none
    try {
      apiInstance.getMembersCustomStickersByIdMember(idMember, key, token, filter);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#getMembersCustomStickersByIdMember");
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
| **idMember** | **String**| idMember or username | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **filter** | **String**| One of: all or none | [optional] [default to all] |

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

<a id="getMembersCustomStickersByIdMemberByIdCustomSticker"></a>
# **getMembersCustomStickersByIdMemberByIdCustomSticker**
> getMembersCustomStickersByIdMemberByIdCustomSticker(idMember, idCustomSticker, key, token, fields)

getMembersCustomStickersByIdMemberByIdCustomSticker()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String idCustomSticker = "idCustomSticker_example"; // String | idCustomSticker
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    String fields = "all"; // String | all or a comma-separated list of: scaled or url
    try {
      apiInstance.getMembersCustomStickersByIdMemberByIdCustomSticker(idMember, idCustomSticker, key, token, fields);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#getMembersCustomStickersByIdMemberByIdCustomSticker");
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
| **idMember** | **String**| idMember or username | |
| **idCustomSticker** | **String**| idCustomSticker | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **fields** | **String**| all or a comma-separated list of: scaled or url | [optional] [default to all] |

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

<a id="getMembersDeltasByIdMember"></a>
# **getMembersDeltasByIdMember**
> getMembersDeltasByIdMember(idMember, tags, ixLastUpdate, key, token)

getMembersDeltasByIdMember()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String tags = "tags_example"; // String | A valid tag for subscribing
    String ixLastUpdate = "ixLastUpdate_example"; // String | a number from -1 to Infinity
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    try {
      apiInstance.getMembersDeltasByIdMember(idMember, tags, ixLastUpdate, key, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#getMembersDeltasByIdMember");
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
| **idMember** | **String**| idMember or username | |
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

<a id="getMembersNotificationsByIdMember"></a>
# **getMembersNotificationsByIdMember**
> getMembersNotificationsByIdMember(idMember, key, token, entities, display, filter, readFilter, fields, limit, page, before, since, memberCreator, memberCreatorFields)

getMembersNotificationsByIdMember()

You can only read the notifications for the member associated with the supplied token

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    String entities = "entities_example"; // String |  true or false
    String display = "display_example"; // String |  true or false
    String filter = "all"; // String | all or a comma-separated list of: addAdminToBoard, addAdminToOrganization, addedAttachmentToCard, addedMemberToCard, addedToBoard, addedToCard, addedToOrganization, cardDueSoon, changeCard, closeBoard, commentCard, createdCard, declinedInvitationToBoard, declinedInvitationToOrganization, invitedToBoard, invitedToOrganization, makeAdminOfBoard, makeAdminOfOrganization, memberJoinedTrello, mentionedOnCard, removedFromBoard, removedFromCard, removedFromOrganization, removedMemberFromCard, unconfirmedInvitedToBoard, unconfirmedInvitedToOrganization or updateCheckItemStateOnCard
    String readFilter = "all"; // String | One of: all, read or unread
    String fields = "all"; // String | all or a comma-separated list of: data, date, idMemberCreator, type or unread
    String limit = "50"; // String | a number from 1 to 1000
    String page = "0"; // String | a number from 0 to 100
    String before = "before_example"; // String | An id, or null
    String since = "since_example"; // String | An id, or null
    String memberCreator = "memberCreator_example"; // String |  true or false
    String memberCreatorFields = "avatarHash, fullName, initials and username"; // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
    try {
      apiInstance.getMembersNotificationsByIdMember(idMember, key, token, entities, display, filter, readFilter, fields, limit, page, before, since, memberCreator, memberCreatorFields);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#getMembersNotificationsByIdMember");
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
| **idMember** | **String**| idMember or username | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **entities** | **String**|  true or false | [optional] |
| **display** | **String**|  true or false | [optional] |
| **filter** | **String**| all or a comma-separated list of: addAdminToBoard, addAdminToOrganization, addedAttachmentToCard, addedMemberToCard, addedToBoard, addedToCard, addedToOrganization, cardDueSoon, changeCard, closeBoard, commentCard, createdCard, declinedInvitationToBoard, declinedInvitationToOrganization, invitedToBoard, invitedToOrganization, makeAdminOfBoard, makeAdminOfOrganization, memberJoinedTrello, mentionedOnCard, removedFromBoard, removedFromCard, removedFromOrganization, removedMemberFromCard, unconfirmedInvitedToBoard, unconfirmedInvitedToOrganization or updateCheckItemStateOnCard | [optional] [default to all] |
| **readFilter** | **String**| One of: all, read or unread | [optional] [default to all] |
| **fields** | **String**| all or a comma-separated list of: data, date, idMemberCreator, type or unread | [optional] [default to all] |
| **limit** | **String**| a number from 1 to 1000 | [optional] [default to 50] |
| **page** | **String**| a number from 0 to 100 | [optional] [default to 0] |
| **before** | **String**| An id, or null | [optional] |
| **since** | **String**| An id, or null | [optional] |
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

<a id="getMembersNotificationsByIdMemberByFilter"></a>
# **getMembersNotificationsByIdMemberByFilter**
> getMembersNotificationsByIdMemberByFilter(idMember, filter, key, token)

getMembersNotificationsByIdMemberByFilter()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String filter = "filter_example"; // String | filter
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    try {
      apiInstance.getMembersNotificationsByIdMemberByFilter(idMember, filter, key, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#getMembersNotificationsByIdMemberByFilter");
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
| **idMember** | **String**| idMember or username | |
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

<a id="getMembersOrganizationsByIdMember"></a>
# **getMembersOrganizationsByIdMember**
> getMembersOrganizationsByIdMember(idMember, key, token, filter, fields, paidAccount)

getMembersOrganizationsByIdMember()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    String filter = "all"; // String | One of: all, members, none or public
    String fields = "all"; // String | all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website
    String paidAccount = "paidAccount_example"; // String |  true or false
    try {
      apiInstance.getMembersOrganizationsByIdMember(idMember, key, token, filter, fields, paidAccount);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#getMembersOrganizationsByIdMember");
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
| **idMember** | **String**| idMember or username | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **filter** | **String**| One of: all, members, none or public | [optional] [default to all] |
| **fields** | **String**| all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website | [optional] [default to all] |
| **paidAccount** | **String**|  true or false | [optional] |

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

<a id="getMembersOrganizationsByIdMemberByFilter"></a>
# **getMembersOrganizationsByIdMemberByFilter**
> getMembersOrganizationsByIdMemberByFilter(idMember, filter, key, token)

getMembersOrganizationsByIdMemberByFilter()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trello.com/1");

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String filter = "filter_example"; // String | filter
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    try {
      apiInstance.getMembersOrganizationsByIdMemberByFilter(idMember, filter, key, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#getMembersOrganizationsByIdMemberByFilter");
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
| **idMember** | **String**| idMember or username | |
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

<a id="getMembersOrganizationsInvitedByIdMember"></a>
# **getMembersOrganizationsInvitedByIdMember**
> getMembersOrganizationsInvitedByIdMember(idMember, key, token, fields)

getMembersOrganizationsInvitedByIdMember()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    String fields = "all"; // String | all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website
    try {
      apiInstance.getMembersOrganizationsInvitedByIdMember(idMember, key, token, fields);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#getMembersOrganizationsInvitedByIdMember");
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
| **idMember** | **String**| idMember or username | |
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

<a id="getMembersOrganizationsInvitedByIdMemberByField"></a>
# **getMembersOrganizationsInvitedByIdMemberByField**
> getMembersOrganizationsInvitedByIdMemberByField(idMember, field, key, token)

getMembersOrganizationsInvitedByIdMemberByField()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String field = "field_example"; // String | field
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    try {
      apiInstance.getMembersOrganizationsInvitedByIdMemberByField(idMember, field, key, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#getMembersOrganizationsInvitedByIdMemberByField");
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
| **idMember** | **String**| idMember or username | |
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

<a id="getMembersSavedSearchesByIdMember"></a>
# **getMembersSavedSearchesByIdMember**
> getMembersSavedSearchesByIdMember(idMember, key, token)

getMembersSavedSearchesByIdMember()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    try {
      apiInstance.getMembersSavedSearchesByIdMember(idMember, key, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#getMembersSavedSearchesByIdMember");
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
| **idMember** | **String**| idMember or username | |
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

<a id="getMembersSavedSearchesByIdMemberByIdSavedSearch"></a>
# **getMembersSavedSearchesByIdMemberByIdSavedSearch**
> getMembersSavedSearchesByIdMemberByIdSavedSearch(idMember, idSavedSearch, key, token)

getMembersSavedSearchesByIdMemberByIdSavedSearch()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String idSavedSearch = "idSavedSearch_example"; // String | idSavedSearch
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    try {
      apiInstance.getMembersSavedSearchesByIdMemberByIdSavedSearch(idMember, idSavedSearch, key, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#getMembersSavedSearchesByIdMemberByIdSavedSearch");
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
| **idMember** | **String**| idMember or username | |
| **idSavedSearch** | **String**| idSavedSearch | |
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

<a id="getMembersTokensByIdMember"></a>
# **getMembersTokensByIdMember**
> getMembersTokensByIdMember(idMember, key, token, filter)

getMembersTokensByIdMember()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    String filter = "all"; // String | One of: all or none
    try {
      apiInstance.getMembersTokensByIdMember(idMember, key, token, filter);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#getMembersTokensByIdMember");
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
| **idMember** | **String**| idMember or username | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **filter** | **String**| One of: all or none | [optional] [default to all] |

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

<a id="updateMembersAvatarSourceByIdMember"></a>
# **updateMembersAvatarSourceByIdMember**
> updateMembersAvatarSourceByIdMember(idMember, key, token, membersAvatarSource)

updateMembersAvatarSourceByIdMember()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    MembersAvatarSource membersAvatarSource = new MembersAvatarSource(); // MembersAvatarSource | Attributes of \"Members Avatar Source\" to be updated.
    try {
      apiInstance.updateMembersAvatarSourceByIdMember(idMember, key, token, membersAvatarSource);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#updateMembersAvatarSourceByIdMember");
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
| **idMember** | **String**| idMember or username | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **membersAvatarSource** | [**MembersAvatarSource**](MembersAvatarSource.md)| Attributes of \&quot;Members Avatar Source\&quot; to be updated. | |

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

<a id="updateMembersBioByIdMember"></a>
# **updateMembersBioByIdMember**
> updateMembersBioByIdMember(idMember, key, token, membersBio)

updateMembersBioByIdMember()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    MembersBio membersBio = new MembersBio(); // MembersBio | Attributes of \"Members Bio\" to be updated.
    try {
      apiInstance.updateMembersBioByIdMember(idMember, key, token, membersBio);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#updateMembersBioByIdMember");
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
| **idMember** | **String**| idMember or username | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **membersBio** | [**MembersBio**](MembersBio.md)| Attributes of \&quot;Members Bio\&quot; to be updated. | |

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

<a id="updateMembersBoardBackgroundsByIdMemberByIdBoardBackground"></a>
# **updateMembersBoardBackgroundsByIdMemberByIdBoardBackground**
> updateMembersBoardBackgroundsByIdMemberByIdBoardBackground(idMember, idBoardBackground, key, token, membersBoardBackgrounds)

updateMembersBoardBackgroundsByIdMemberByIdBoardBackground()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String idBoardBackground = "idBoardBackground_example"; // String | idBoardBackground
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    MembersBoardBackgrounds membersBoardBackgrounds = new MembersBoardBackgrounds(); // MembersBoardBackgrounds | Attributes of \"Members Board Backgrounds\" to be updated.
    try {
      apiInstance.updateMembersBoardBackgroundsByIdMemberByIdBoardBackground(idMember, idBoardBackground, key, token, membersBoardBackgrounds);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#updateMembersBoardBackgroundsByIdMemberByIdBoardBackground");
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
| **idMember** | **String**| idMember or username | |
| **idBoardBackground** | **String**| idBoardBackground | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **membersBoardBackgrounds** | [**MembersBoardBackgrounds**](MembersBoardBackgrounds.md)| Attributes of \&quot;Members Board Backgrounds\&quot; to be updated. | |

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

<a id="updateMembersBoardStarsByIdMemberByIdBoardStar"></a>
# **updateMembersBoardStarsByIdMemberByIdBoardStar**
> updateMembersBoardStarsByIdMemberByIdBoardStar(idMember, idBoardStar, key, token, membersBoardStars)

updateMembersBoardStarsByIdMemberByIdBoardStar()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String idBoardStar = "idBoardStar_example"; // String | idBoardStar
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    MembersBoardStars membersBoardStars = new MembersBoardStars(); // MembersBoardStars | Attributes of \"Members Board Stars\" to be updated.
    try {
      apiInstance.updateMembersBoardStarsByIdMemberByIdBoardStar(idMember, idBoardStar, key, token, membersBoardStars);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#updateMembersBoardStarsByIdMemberByIdBoardStar");
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
| **idMember** | **String**| idMember or username | |
| **idBoardStar** | **String**| idBoardStar | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **membersBoardStars** | [**MembersBoardStars**](MembersBoardStars.md)| Attributes of \&quot;Members Board Stars\&quot; to be updated. | |

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

<a id="updateMembersBoardStarsIdBoardByIdMemberByIdBoardStar"></a>
# **updateMembersBoardStarsIdBoardByIdMemberByIdBoardStar**
> updateMembersBoardStarsIdBoardByIdMemberByIdBoardStar(idMember, idBoardStar, key, token, membersBoardStarsIdBoard)

updateMembersBoardStarsIdBoardByIdMemberByIdBoardStar()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String idBoardStar = "idBoardStar_example"; // String | idBoardStar
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    MembersBoardStarsIdBoard membersBoardStarsIdBoard = new MembersBoardStarsIdBoard(); // MembersBoardStarsIdBoard | Attributes of \"Members Board Stars Id Board\" to be updated.
    try {
      apiInstance.updateMembersBoardStarsIdBoardByIdMemberByIdBoardStar(idMember, idBoardStar, key, token, membersBoardStarsIdBoard);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#updateMembersBoardStarsIdBoardByIdMemberByIdBoardStar");
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
| **idMember** | **String**| idMember or username | |
| **idBoardStar** | **String**| idBoardStar | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **membersBoardStarsIdBoard** | [**MembersBoardStarsIdBoard**](MembersBoardStarsIdBoard.md)| Attributes of \&quot;Members Board Stars Id Board\&quot; to be updated. | |

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

<a id="updateMembersBoardStarsPosByIdMemberByIdBoardStar"></a>
# **updateMembersBoardStarsPosByIdMemberByIdBoardStar**
> updateMembersBoardStarsPosByIdMemberByIdBoardStar(idMember, idBoardStar, key, token, membersBoardStarsPos)

updateMembersBoardStarsPosByIdMemberByIdBoardStar()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String idBoardStar = "idBoardStar_example"; // String | idBoardStar
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    MembersBoardStarsPos membersBoardStarsPos = new MembersBoardStarsPos(); // MembersBoardStarsPos | Attributes of \"Members Board Stars Pos\" to be updated.
    try {
      apiInstance.updateMembersBoardStarsPosByIdMemberByIdBoardStar(idMember, idBoardStar, key, token, membersBoardStarsPos);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#updateMembersBoardStarsPosByIdMemberByIdBoardStar");
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
| **idMember** | **String**| idMember or username | |
| **idBoardStar** | **String**| idBoardStar | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **membersBoardStarsPos** | [**MembersBoardStarsPos**](MembersBoardStarsPos.md)| Attributes of \&quot;Members Board Stars Pos\&quot; to be updated. | |

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

<a id="updateMembersByIdMember"></a>
# **updateMembersByIdMember**
> updateMembersByIdMember(idMember, key, token, members)

updateMembersByIdMember()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    Members members = new Members(); // Members | Attributes of \"Members\" to be updated.
    try {
      apiInstance.updateMembersByIdMember(idMember, key, token, members);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#updateMembersByIdMember");
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
| **idMember** | **String**| idMember or username | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **members** | [**Members**](Members.md)| Attributes of \&quot;Members\&quot; to be updated. | |

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

<a id="updateMembersCustomBoardBackgroundsByIdMemberByIdBoardBackground"></a>
# **updateMembersCustomBoardBackgroundsByIdMemberByIdBoardBackground**
> updateMembersCustomBoardBackgroundsByIdMemberByIdBoardBackground(idMember, idBoardBackground, key, token, membersCustomBoardBackgrounds)

updateMembersCustomBoardBackgroundsByIdMemberByIdBoardBackground()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String idBoardBackground = "idBoardBackground_example"; // String | idBoardBackground
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    MembersCustomBoardBackgrounds membersCustomBoardBackgrounds = new MembersCustomBoardBackgrounds(); // MembersCustomBoardBackgrounds | Attributes of \"Members Custom Board Backgrounds\" to be updated.
    try {
      apiInstance.updateMembersCustomBoardBackgroundsByIdMemberByIdBoardBackground(idMember, idBoardBackground, key, token, membersCustomBoardBackgrounds);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#updateMembersCustomBoardBackgroundsByIdMemberByIdBoardBackground");
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
| **idMember** | **String**| idMember or username | |
| **idBoardBackground** | **String**| idBoardBackground | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **membersCustomBoardBackgrounds** | [**MembersCustomBoardBackgrounds**](MembersCustomBoardBackgrounds.md)| Attributes of \&quot;Members Custom Board Backgrounds\&quot; to be updated. | |

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

<a id="updateMembersFullNameByIdMember"></a>
# **updateMembersFullNameByIdMember**
> updateMembersFullNameByIdMember(idMember, key, token, membersFullName)

updateMembersFullNameByIdMember()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    MembersFullName membersFullName = new MembersFullName(); // MembersFullName | Attributes of \"Members Full Name\" to be updated.
    try {
      apiInstance.updateMembersFullNameByIdMember(idMember, key, token, membersFullName);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#updateMembersFullNameByIdMember");
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
| **idMember** | **String**| idMember or username | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **membersFullName** | [**MembersFullName**](MembersFullName.md)| Attributes of \&quot;Members Full Name\&quot; to be updated. | |

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

<a id="updateMembersInitialsByIdMember"></a>
# **updateMembersInitialsByIdMember**
> updateMembersInitialsByIdMember(idMember, key, token, membersInitials)

updateMembersInitialsByIdMember()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    MembersInitials membersInitials = new MembersInitials(); // MembersInitials | Attributes of \"Members Initials\" to be updated.
    try {
      apiInstance.updateMembersInitialsByIdMember(idMember, key, token, membersInitials);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#updateMembersInitialsByIdMember");
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
| **idMember** | **String**| idMember or username | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **membersInitials** | [**MembersInitials**](MembersInitials.md)| Attributes of \&quot;Members Initials\&quot; to be updated. | |

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

<a id="updateMembersPrefsColorBlindByIdMember"></a>
# **updateMembersPrefsColorBlindByIdMember**
> updateMembersPrefsColorBlindByIdMember(idMember, key, token, prefsColorBlind)

updateMembersPrefsColorBlindByIdMember()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    PrefsColorBlind prefsColorBlind = new PrefsColorBlind(); // PrefsColorBlind | Attributes of \"Prefs Color Blind\" to be updated.
    try {
      apiInstance.updateMembersPrefsColorBlindByIdMember(idMember, key, token, prefsColorBlind);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#updateMembersPrefsColorBlindByIdMember");
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
| **idMember** | **String**| idMember or username | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **prefsColorBlind** | [**PrefsColorBlind**](PrefsColorBlind.md)| Attributes of \&quot;Prefs Color Blind\&quot; to be updated. | |

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

<a id="updateMembersPrefsLocaleByIdMember"></a>
# **updateMembersPrefsLocaleByIdMember**
> updateMembersPrefsLocaleByIdMember(idMember, key, token, prefsLocale)

updateMembersPrefsLocaleByIdMember()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    PrefsLocale prefsLocale = new PrefsLocale(); // PrefsLocale | Attributes of \"Prefs Locale\" to be updated.
    try {
      apiInstance.updateMembersPrefsLocaleByIdMember(idMember, key, token, prefsLocale);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#updateMembersPrefsLocaleByIdMember");
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
| **idMember** | **String**| idMember or username | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **prefsLocale** | [**PrefsLocale**](PrefsLocale.md)| Attributes of \&quot;Prefs Locale\&quot; to be updated. | |

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

<a id="updateMembersPrefsMinutesBetweenSummariesByIdMember"></a>
# **updateMembersPrefsMinutesBetweenSummariesByIdMember**
> updateMembersPrefsMinutesBetweenSummariesByIdMember(idMember, key, token, prefsMinutesBetweenSummaries)

updateMembersPrefsMinutesBetweenSummariesByIdMember()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    PrefsMinutesBetweenSummaries prefsMinutesBetweenSummaries = new PrefsMinutesBetweenSummaries(); // PrefsMinutesBetweenSummaries | Attributes of \"Prefs Minutes Between Summaries\" to be updated.
    try {
      apiInstance.updateMembersPrefsMinutesBetweenSummariesByIdMember(idMember, key, token, prefsMinutesBetweenSummaries);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#updateMembersPrefsMinutesBetweenSummariesByIdMember");
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
| **idMember** | **String**| idMember or username | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **prefsMinutesBetweenSummaries** | [**PrefsMinutesBetweenSummaries**](PrefsMinutesBetweenSummaries.md)| Attributes of \&quot;Prefs Minutes Between Summaries\&quot; to be updated. | |

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

<a id="updateMembersSavedSearchesByIdMemberByIdSavedSearch"></a>
# **updateMembersSavedSearchesByIdMemberByIdSavedSearch**
> updateMembersSavedSearchesByIdMemberByIdSavedSearch(idMember, idSavedSearch, key, token, membersSavedSearches)

updateMembersSavedSearchesByIdMemberByIdSavedSearch()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String idSavedSearch = "idSavedSearch_example"; // String | idSavedSearch
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    MembersSavedSearches membersSavedSearches = new MembersSavedSearches(); // MembersSavedSearches | Attributes of \"Members Saved Searches\" to be updated.
    try {
      apiInstance.updateMembersSavedSearchesByIdMemberByIdSavedSearch(idMember, idSavedSearch, key, token, membersSavedSearches);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#updateMembersSavedSearchesByIdMemberByIdSavedSearch");
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
| **idMember** | **String**| idMember or username | |
| **idSavedSearch** | **String**| idSavedSearch | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **membersSavedSearches** | [**MembersSavedSearches**](MembersSavedSearches.md)| Attributes of \&quot;Members Saved Searches\&quot; to be updated. | |

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

<a id="updateMembersSavedSearchesNameByIdMemberByIdSavedSearch"></a>
# **updateMembersSavedSearchesNameByIdMemberByIdSavedSearch**
> updateMembersSavedSearchesNameByIdMemberByIdSavedSearch(idMember, idSavedSearch, key, token, membersSavedSearchesName)

updateMembersSavedSearchesNameByIdMemberByIdSavedSearch()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String idSavedSearch = "idSavedSearch_example"; // String | idSavedSearch
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    MembersSavedSearchesName membersSavedSearchesName = new MembersSavedSearchesName(); // MembersSavedSearchesName | Attributes of \"Members Saved Searches Name\" to be updated.
    try {
      apiInstance.updateMembersSavedSearchesNameByIdMemberByIdSavedSearch(idMember, idSavedSearch, key, token, membersSavedSearchesName);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#updateMembersSavedSearchesNameByIdMemberByIdSavedSearch");
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
| **idMember** | **String**| idMember or username | |
| **idSavedSearch** | **String**| idSavedSearch | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **membersSavedSearchesName** | [**MembersSavedSearchesName**](MembersSavedSearchesName.md)| Attributes of \&quot;Members Saved Searches Name\&quot; to be updated. | |

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

<a id="updateMembersSavedSearchesPosByIdMemberByIdSavedSearch"></a>
# **updateMembersSavedSearchesPosByIdMemberByIdSavedSearch**
> updateMembersSavedSearchesPosByIdMemberByIdSavedSearch(idMember, idSavedSearch, key, token, membersSavedSearchesPos)

updateMembersSavedSearchesPosByIdMemberByIdSavedSearch()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String idSavedSearch = "idSavedSearch_example"; // String | idSavedSearch
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    MembersSavedSearchesPos membersSavedSearchesPos = new MembersSavedSearchesPos(); // MembersSavedSearchesPos | Attributes of \"Members Saved Searches Pos\" to be updated.
    try {
      apiInstance.updateMembersSavedSearchesPosByIdMemberByIdSavedSearch(idMember, idSavedSearch, key, token, membersSavedSearchesPos);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#updateMembersSavedSearchesPosByIdMemberByIdSavedSearch");
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
| **idMember** | **String**| idMember or username | |
| **idSavedSearch** | **String**| idSavedSearch | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **membersSavedSearchesPos** | [**MembersSavedSearchesPos**](MembersSavedSearchesPos.md)| Attributes of \&quot;Members Saved Searches Pos\&quot; to be updated. | |

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

<a id="updateMembersSavedSearchesQueryByIdMemberByIdSavedSearch"></a>
# **updateMembersSavedSearchesQueryByIdMemberByIdSavedSearch**
> updateMembersSavedSearchesQueryByIdMemberByIdSavedSearch(idMember, idSavedSearch, key, token, membersSavedSearchesQuery)

updateMembersSavedSearchesQueryByIdMemberByIdSavedSearch()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String idSavedSearch = "idSavedSearch_example"; // String | idSavedSearch
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    MembersSavedSearchesQuery membersSavedSearchesQuery = new MembersSavedSearchesQuery(); // MembersSavedSearchesQuery | Attributes of \"Members Saved Searches Query\" to be updated.
    try {
      apiInstance.updateMembersSavedSearchesQueryByIdMemberByIdSavedSearch(idMember, idSavedSearch, key, token, membersSavedSearchesQuery);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#updateMembersSavedSearchesQueryByIdMemberByIdSavedSearch");
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
| **idMember** | **String**| idMember or username | |
| **idSavedSearch** | **String**| idSavedSearch | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **membersSavedSearchesQuery** | [**MembersSavedSearchesQuery**](MembersSavedSearchesQuery.md)| Attributes of \&quot;Members Saved Searches Query\&quot; to be updated. | |

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

<a id="updateMembersUsernameByIdMember"></a>
# **updateMembersUsernameByIdMember**
> updateMembersUsernameByIdMember(idMember, key, token, membersUsername)

updateMembersUsernameByIdMember()

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

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

    MemberApi apiInstance = new MemberApi(defaultClient);
    String idMember = "idMember_example"; // String | idMember or username
    String key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
    String token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
    MembersUsername membersUsername = new MembersUsername(); // MembersUsername | Attributes of \"Members Username\" to be updated.
    try {
      apiInstance.updateMembersUsernameByIdMember(idMember, key, token, membersUsername);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#updateMembersUsernameByIdMember");
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
| **idMember** | **String**| idMember or username | |
| **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | |
| **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | |
| **membersUsername** | [**MembersUsername**](MembersUsername.md)| Attributes of \&quot;Members Username\&quot; to be updated. | |

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

