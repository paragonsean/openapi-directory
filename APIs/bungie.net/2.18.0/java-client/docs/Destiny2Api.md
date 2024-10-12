# Destiny2Api

All URIs are relative to *https://www.bungie.net/Platform*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**destiny2AwaGetActionToken**](Destiny2Api.md#destiny2AwaGetActionToken) | **GET** /Destiny2/Awa/GetActionToken/{correlationId}/ |  |
| [**destiny2AwaInitializeRequest**](Destiny2Api.md#destiny2AwaInitializeRequest) | **POST** /Destiny2/Awa/Initialize/ |  |
| [**destiny2AwaProvideAuthorizationResult**](Destiny2Api.md#destiny2AwaProvideAuthorizationResult) | **POST** /Destiny2/Awa/AwaProvideAuthorizationResult/ |  |
| [**destiny2ClearLoadout**](Destiny2Api.md#destiny2ClearLoadout) | **POST** /Destiny2/Actions/Loadouts/ClearLoadout/ |  |
| [**destiny2EquipItem**](Destiny2Api.md#destiny2EquipItem) | **POST** /Destiny2/Actions/Items/EquipItem/ |  |
| [**destiny2EquipItems**](Destiny2Api.md#destiny2EquipItems) | **POST** /Destiny2/Actions/Items/EquipItems/ |  |
| [**destiny2EquipLoadout**](Destiny2Api.md#destiny2EquipLoadout) | **POST** /Destiny2/Actions/Loadouts/EquipLoadout/ |  |
| [**destiny2GetActivityHistory**](Destiny2Api.md#destiny2GetActivityHistory) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/Activities/ |  |
| [**destiny2GetCharacter**](Destiny2Api.md#destiny2GetCharacter) | **GET** /Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/ |  |
| [**destiny2GetClanAggregateStats**](Destiny2Api.md#destiny2GetClanAggregateStats) | **GET** /Destiny2/Stats/AggregateClanStats/{groupId}/ |  |
| [**destiny2GetClanBannerSource**](Destiny2Api.md#destiny2GetClanBannerSource) | **GET** /Destiny2/Clan/ClanBannerDictionary/ |  |
| [**destiny2GetClanLeaderboards**](Destiny2Api.md#destiny2GetClanLeaderboards) | **GET** /Destiny2/Stats/Leaderboards/Clans/{groupId}/ |  |
| [**destiny2GetClanWeeklyRewardState**](Destiny2Api.md#destiny2GetClanWeeklyRewardState) | **GET** /Destiny2/Clan/{groupId}/WeeklyRewardState/ |  |
| [**destiny2GetCollectibleNodeDetails**](Destiny2Api.md#destiny2GetCollectibleNodeDetails) | **GET** /Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/Collectibles/{collectiblePresentationNodeHash}/ |  |
| [**destiny2GetDestinyAggregateActivityStats**](Destiny2Api.md#destiny2GetDestinyAggregateActivityStats) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/AggregateActivityStats/ |  |
| [**destiny2GetDestinyEntityDefinition**](Destiny2Api.md#destiny2GetDestinyEntityDefinition) | **GET** /Destiny2/Manifest/{entityType}/{hashIdentifier}/ |  |
| [**destiny2GetDestinyManifest**](Destiny2Api.md#destiny2GetDestinyManifest) | **GET** /Destiny2/Manifest/ |  |
| [**destiny2GetHistoricalStats**](Destiny2Api.md#destiny2GetHistoricalStats) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/ |  |
| [**destiny2GetHistoricalStatsDefinition**](Destiny2Api.md#destiny2GetHistoricalStatsDefinition) | **GET** /Destiny2/Stats/Definition/ |  |
| [**destiny2GetHistoricalStatsForAccount**](Destiny2Api.md#destiny2GetHistoricalStatsForAccount) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Stats/ |  |
| [**destiny2GetItem**](Destiny2Api.md#destiny2GetItem) | **GET** /Destiny2/{membershipType}/Profile/{destinyMembershipId}/Item/{itemInstanceId}/ |  |
| [**destiny2GetLeaderboards**](Destiny2Api.md#destiny2GetLeaderboards) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Stats/Leaderboards/ |  |
| [**destiny2GetLeaderboardsForCharacter**](Destiny2Api.md#destiny2GetLeaderboardsForCharacter) | **GET** /Destiny2/Stats/Leaderboards/{membershipType}/{destinyMembershipId}/{characterId}/ |  |
| [**destiny2GetLinkedProfiles**](Destiny2Api.md#destiny2GetLinkedProfiles) | **GET** /Destiny2/{membershipType}/Profile/{membershipId}/LinkedProfiles/ |  |
| [**destiny2GetPostGameCarnageReport**](Destiny2Api.md#destiny2GetPostGameCarnageReport) | **GET** /Destiny2/Stats/PostGameCarnageReport/{activityId}/ |  |
| [**destiny2GetProfile**](Destiny2Api.md#destiny2GetProfile) | **GET** /Destiny2/{membershipType}/Profile/{destinyMembershipId}/ |  |
| [**destiny2GetPublicMilestoneContent**](Destiny2Api.md#destiny2GetPublicMilestoneContent) | **GET** /Destiny2/Milestones/{milestoneHash}/Content/ |  |
| [**destiny2GetPublicMilestones**](Destiny2Api.md#destiny2GetPublicMilestones) | **GET** /Destiny2/Milestones/ |  |
| [**destiny2GetPublicVendors**](Destiny2Api.md#destiny2GetPublicVendors) | **GET** /Destiny2/Vendors/ |  |
| [**destiny2GetUniqueWeaponHistory**](Destiny2Api.md#destiny2GetUniqueWeaponHistory) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/UniqueWeapons/ |  |
| [**destiny2GetVendor**](Destiny2Api.md#destiny2GetVendor) | **GET** /Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/Vendors/{vendorHash}/ |  |
| [**destiny2GetVendors**](Destiny2Api.md#destiny2GetVendors) | **GET** /Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/Vendors/ |  |
| [**destiny2InsertSocketPlug**](Destiny2Api.md#destiny2InsertSocketPlug) | **POST** /Destiny2/Actions/Items/InsertSocketPlug/ |  |
| [**destiny2InsertSocketPlugFree**](Destiny2Api.md#destiny2InsertSocketPlugFree) | **POST** /Destiny2/Actions/Items/InsertSocketPlugFree/ |  |
| [**destiny2PullFromPostmaster**](Destiny2Api.md#destiny2PullFromPostmaster) | **POST** /Destiny2/Actions/Items/PullFromPostmaster/ |  |
| [**destiny2ReportOffensivePostGameCarnageReportPlayer**](Destiny2Api.md#destiny2ReportOffensivePostGameCarnageReportPlayer) | **POST** /Destiny2/Stats/PostGameCarnageReport/{activityId}/Report/ |  |
| [**destiny2SearchDestinyEntities**](Destiny2Api.md#destiny2SearchDestinyEntities) | **GET** /Destiny2/Armory/Search/{type}/{searchTerm}/ |  |
| [**destiny2SearchDestinyPlayerByBungieName**](Destiny2Api.md#destiny2SearchDestinyPlayerByBungieName) | **POST** /Destiny2/SearchDestinyPlayerByBungieName/{membershipType}/ |  |
| [**destiny2SetItemLockState**](Destiny2Api.md#destiny2SetItemLockState) | **POST** /Destiny2/Actions/Items/SetLockState/ |  |
| [**destiny2SetQuestTrackedState**](Destiny2Api.md#destiny2SetQuestTrackedState) | **POST** /Destiny2/Actions/Items/SetTrackedState/ |  |
| [**destiny2SnapshotLoadout**](Destiny2Api.md#destiny2SnapshotLoadout) | **POST** /Destiny2/Actions/Loadouts/SnapshotLoadout/ |  |
| [**destiny2TransferItem**](Destiny2Api.md#destiny2TransferItem) | **POST** /Destiny2/Actions/Items/TransferItem/ |  |
| [**destiny2UpdateLoadoutIdentifiers**](Destiny2Api.md#destiny2UpdateLoadoutIdentifiers) | **POST** /Destiny2/Actions/Loadouts/UpdateLoadoutIdentifiers/ |  |


<a id="destiny2AwaGetActionToken"></a>
# **destiny2AwaGetActionToken**
> Destiny2AwaGetActionToken200Response destiny2AwaGetActionToken(correlationId)



Returns the action token if user approves the request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    String correlationId = "correlationId_example"; // String | The identifier for the advanced write action request.
    try {
      Destiny2AwaGetActionToken200Response result = apiInstance.destiny2AwaGetActionToken(correlationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2AwaGetActionToken");
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
| **correlationId** | **String**| The identifier for the advanced write action request. | |

### Return type

[**Destiny2AwaGetActionToken200Response**](Destiny2AwaGetActionToken200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="destiny2AwaInitializeRequest"></a>
# **destiny2AwaInitializeRequest**
> Destiny2AwaInitializeRequest200Response destiny2AwaInitializeRequest()



Initialize a request to perform an advanced write action.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    try {
      Destiny2AwaInitializeRequest200Response result = apiInstance.destiny2AwaInitializeRequest();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2AwaInitializeRequest");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Destiny2AwaInitializeRequest200Response**](Destiny2AwaInitializeRequest200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="destiny2AwaProvideAuthorizationResult"></a>
# **destiny2AwaProvideAuthorizationResult**
> Destiny2EquipItem200Response destiny2AwaProvideAuthorizationResult()



Provide the result of the user interaction. Called by the Bungie Destiny App to approve or reject a request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    try {
      Destiny2EquipItem200Response result = apiInstance.destiny2AwaProvideAuthorizationResult();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2AwaProvideAuthorizationResult");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Destiny2EquipItem200Response**](Destiny2EquipItem200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="destiny2ClearLoadout"></a>
# **destiny2ClearLoadout**
> Destiny2EquipItem200Response destiny2ClearLoadout()



Clear the identifiers and items of a loadout.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    try {
      Destiny2EquipItem200Response result = apiInstance.destiny2ClearLoadout();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2ClearLoadout");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Destiny2EquipItem200Response**](Destiny2EquipItem200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="destiny2EquipItem"></a>
# **destiny2EquipItem**
> Destiny2EquipItem200Response destiny2EquipItem()



Equip an item. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    try {
      Destiny2EquipItem200Response result = apiInstance.destiny2EquipItem();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2EquipItem");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Destiny2EquipItem200Response**](Destiny2EquipItem200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="destiny2EquipItems"></a>
# **destiny2EquipItems**
> Destiny2EquipItems200Response destiny2EquipItems()



Equip a list of items by itemInstanceIds. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline. Any items not found on your character will be ignored.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    try {
      Destiny2EquipItems200Response result = apiInstance.destiny2EquipItems();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2EquipItems");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Destiny2EquipItems200Response**](Destiny2EquipItems200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The results of a bulk Equipping operation performed through the Destiny API. |  -  |

<a id="destiny2EquipLoadout"></a>
# **destiny2EquipLoadout**
> Destiny2EquipItem200Response destiny2EquipLoadout()



Equip a loadout. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    try {
      Destiny2EquipItem200Response result = apiInstance.destiny2EquipLoadout();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2EquipLoadout");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Destiny2EquipItem200Response**](Destiny2EquipItem200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="destiny2GetActivityHistory"></a>
# **destiny2GetActivityHistory**
> Destiny2GetActivityHistory200Response destiny2GetActivityHistory(characterId, destinyMembershipId, membershipType, count, mode, page)



Gets activity history stats for indicated character.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    Long characterId = 56L; // Long | The id of the character to retrieve.
    Long destinyMembershipId = 56L; // Long | The Destiny membershipId of the user to retrieve.
    Integer membershipType = 56; // Integer | A valid non-BungieNet membership type.
    Integer count = 56; // Integer | Number of rows to return
    Integer mode = 56; // Integer | A filter for the activity mode to be returned. None returns all activities. See the documentation for DestinyActivityModeType for valid values, and pass in string representation.
    Integer page = 56; // Integer | Page number to return, starting with 0.
    try {
      Destiny2GetActivityHistory200Response result = apiInstance.destiny2GetActivityHistory(characterId, destinyMembershipId, membershipType, count, mode, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2GetActivityHistory");
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
| **characterId** | **Long**| The id of the character to retrieve. | |
| **destinyMembershipId** | **Long**| The Destiny membershipId of the user to retrieve. | |
| **membershipType** | **Integer**| A valid non-BungieNet membership type. | |
| **count** | **Integer**| Number of rows to return | [optional] |
| **mode** | **Integer**| A filter for the activity mode to be returned. None returns all activities. See the documentation for DestinyActivityModeType for valid values, and pass in string representation. | [optional] |
| **page** | **Integer**| Page number to return, starting with 0. | [optional] |

### Return type

[**Destiny2GetActivityHistory200Response**](Destiny2GetActivityHistory200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="destiny2GetCharacter"></a>
# **destiny2GetCharacter**
> Destiny2GetCharacter200Response destiny2GetCharacter(characterId, destinyMembershipId, membershipType, components)



Returns character information for the supplied character.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    Long characterId = 56L; // Long | ID of the character.
    Long destinyMembershipId = 56L; // Long | Destiny membership ID.
    Integer membershipType = 56; // Integer | A valid non-BungieNet membership type.
    List<Integer> components = Arrays.asList(); // List<Integer> | A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
    try {
      Destiny2GetCharacter200Response result = apiInstance.destiny2GetCharacter(characterId, destinyMembershipId, membershipType, components);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2GetCharacter");
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
| **characterId** | **Long**| ID of the character. | |
| **destinyMembershipId** | **Long**| Destiny membership ID. | |
| **membershipType** | **Integer**| A valid non-BungieNet membership type. | |
| **components** | [**List&lt;Integer&gt;**](Integer.md)| A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results. | [optional] |

### Return type

[**Destiny2GetCharacter200Response**](Destiny2GetCharacter200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response contract for GetDestinyCharacter, with components that can be returned for character and item-level data. |  -  |

<a id="destiny2GetClanAggregateStats"></a>
# **destiny2GetClanAggregateStats**
> Destiny2GetClanAggregateStats200Response destiny2GetClanAggregateStats(groupId, modes)



Gets aggregated stats for a clan using the same categories as the clan leaderboards. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is in final form, but there may be bugs that prevent desirable operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    Long groupId = 56L; // Long | Group ID of the clan whose leaderboards you wish to fetch.
    String modes = "modes_example"; // String | List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
    try {
      Destiny2GetClanAggregateStats200Response result = apiInstance.destiny2GetClanAggregateStats(groupId, modes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2GetClanAggregateStats");
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
| **groupId** | **Long**| Group ID of the clan whose leaderboards you wish to fetch. | |
| **modes** | **String**| List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. | [optional] |

### Return type

[**Destiny2GetClanAggregateStats200Response**](Destiny2GetClanAggregateStats200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="destiny2GetClanBannerSource"></a>
# **destiny2GetClanBannerSource**
> Destiny2GetClanBannerSource200Response destiny2GetClanBannerSource()



Returns the dictionary of values for the Clan Banner

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    try {
      Destiny2GetClanBannerSource200Response result = apiInstance.destiny2GetClanBannerSource();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2GetClanBannerSource");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Destiny2GetClanBannerSource200Response**](Destiny2GetClanBannerSource200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="destiny2GetClanLeaderboards"></a>
# **destiny2GetClanLeaderboards**
> Destiny2GetClanLeaderboards200Response destiny2GetClanLeaderboards(groupId, maxtop, modes, statid)



Gets leaderboards with the signed in user&#39;s friends and the supplied destinyMembershipId as the focus. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is in final form, but there may be bugs that prevent desirable operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    Long groupId = 56L; // Long | Group ID of the clan whose leaderboards you wish to fetch.
    Integer maxtop = 56; // Integer | Maximum number of top players to return. Use a large number to get entire leaderboard.
    String modes = "modes_example"; // String | List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
    String statid = "statid_example"; // String | ID of stat to return rather than returning all Leaderboard stats.
    try {
      Destiny2GetClanLeaderboards200Response result = apiInstance.destiny2GetClanLeaderboards(groupId, maxtop, modes, statid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2GetClanLeaderboards");
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
| **groupId** | **Long**| Group ID of the clan whose leaderboards you wish to fetch. | |
| **maxtop** | **Integer**| Maximum number of top players to return. Use a large number to get entire leaderboard. | [optional] |
| **modes** | **String**| List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. | [optional] |
| **statid** | **String**| ID of stat to return rather than returning all Leaderboard stats. | [optional] |

### Return type

[**Destiny2GetClanLeaderboards200Response**](Destiny2GetClanLeaderboards200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="destiny2GetClanWeeklyRewardState"></a>
# **destiny2GetClanWeeklyRewardState**
> Destiny2GetClanWeeklyRewardState200Response destiny2GetClanWeeklyRewardState(groupId)



Returns information on the weekly clan rewards and if the clan has earned them or not. Note that this will always report rewards as not redeemed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    Long groupId = 56L; // Long | A valid group id of clan.
    try {
      Destiny2GetClanWeeklyRewardState200Response result = apiInstance.destiny2GetClanWeeklyRewardState(groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2GetClanWeeklyRewardState");
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
| **groupId** | **Long**| A valid group id of clan. | |

### Return type

[**Destiny2GetClanWeeklyRewardState200Response**](Destiny2GetClanWeeklyRewardState200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Represents a runtime instance of a user&#39;s milestone status. Live Milestone data should be combined with DestinyMilestoneDefinition data to show the user a picture of what is available for them to do in the game, and their status in regards to said \&quot;things to do.\&quot; Consider it a big, wonky to-do list, or Advisors 3.0 for those who remember the Destiny 1 API. |  -  |

<a id="destiny2GetCollectibleNodeDetails"></a>
# **destiny2GetCollectibleNodeDetails**
> Destiny2GetCollectibleNodeDetails200Response destiny2GetCollectibleNodeDetails(characterId, collectiblePresentationNodeHash, destinyMembershipId, membershipType, components)



Given a Presentation Node that has Collectibles as direct descendants, this will return item details about those descendants in the context of the requesting character.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    Long characterId = 56L; // Long | The Destiny Character ID of the character for whom we're getting collectible detail info.
    Integer collectiblePresentationNodeHash = 56; // Integer | The hash identifier of the Presentation Node for whom we should return collectible details. Details will only be returned for collectibles that are direct descendants of this node.
    Long destinyMembershipId = 56L; // Long | Destiny membership ID of another user. You may be denied.
    Integer membershipType = 56; // Integer | A valid non-BungieNet membership type.
    List<Integer> components = Arrays.asList(); // List<Integer> | A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
    try {
      Destiny2GetCollectibleNodeDetails200Response result = apiInstance.destiny2GetCollectibleNodeDetails(characterId, collectiblePresentationNodeHash, destinyMembershipId, membershipType, components);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2GetCollectibleNodeDetails");
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
| **characterId** | **Long**| The Destiny Character ID of the character for whom we&#39;re getting collectible detail info. | |
| **collectiblePresentationNodeHash** | **Integer**| The hash identifier of the Presentation Node for whom we should return collectible details. Details will only be returned for collectibles that are direct descendants of this node. | |
| **destinyMembershipId** | **Long**| Destiny membership ID of another user. You may be denied. | |
| **membershipType** | **Integer**| A valid non-BungieNet membership type. | |
| **components** | [**List&lt;Integer&gt;**](Integer.md)| A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results. | [optional] |

### Return type

[**Destiny2GetCollectibleNodeDetails200Response**](Destiny2GetCollectibleNodeDetails200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the detailed information about a Collectible Presentation Node and any Collectibles that are direct descendants. |  -  |

<a id="destiny2GetDestinyAggregateActivityStats"></a>
# **destiny2GetDestinyAggregateActivityStats**
> Destiny2GetDestinyAggregateActivityStats200Response destiny2GetDestinyAggregateActivityStats(characterId, destinyMembershipId, membershipType)



Gets all activities the character has participated in together with aggregate statistics for those activities.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    Long characterId = 56L; // Long | The specific character whose activities should be returned.
    Long destinyMembershipId = 56L; // Long | The Destiny membershipId of the user to retrieve.
    Integer membershipType = 56; // Integer | A valid non-BungieNet membership type.
    try {
      Destiny2GetDestinyAggregateActivityStats200Response result = apiInstance.destiny2GetDestinyAggregateActivityStats(characterId, destinyMembershipId, membershipType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2GetDestinyAggregateActivityStats");
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
| **characterId** | **Long**| The specific character whose activities should be returned. | |
| **destinyMembershipId** | **Long**| The Destiny membershipId of the user to retrieve. | |
| **membershipType** | **Integer**| A valid non-BungieNet membership type. | |

### Return type

[**Destiny2GetDestinyAggregateActivityStats200Response**](Destiny2GetDestinyAggregateActivityStats200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="destiny2GetDestinyEntityDefinition"></a>
# **destiny2GetDestinyEntityDefinition**
> Destiny2GetDestinyEntityDefinition200Response destiny2GetDestinyEntityDefinition(entityType, hashIdentifier)



Returns the static definition of an entity of the given Type and hash identifier. Examine the API Documentation for the Type Names of entities that have their own definitions. Note that the return type will always *inherit from* DestinyDefinition, but the specific type returned will be the requested entity type if it can be found. Please don&#39;t use this as a chatty alternative to the Manifest database if you require large sets of data, but for simple and one-off accesses this should be handy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    String entityType = "entityType_example"; // String | The type of entity for whom you would like results. These correspond to the entity's definition contract name. For instance, if you are looking for items, this property should be 'DestinyInventoryItemDefinition'. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is tentatively in final form, but there may be bugs that prevent desirable operation.
    Integer hashIdentifier = 56; // Integer | The hash identifier for the specific Entity you want returned.
    try {
      Destiny2GetDestinyEntityDefinition200Response result = apiInstance.destiny2GetDestinyEntityDefinition(entityType, hashIdentifier);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2GetDestinyEntityDefinition");
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
| **entityType** | **String**| The type of entity for whom you would like results. These correspond to the entity&#39;s definition contract name. For instance, if you are looking for items, this property should be &#39;DestinyInventoryItemDefinition&#39;. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is tentatively in final form, but there may be bugs that prevent desirable operation. | |
| **hashIdentifier** | **Integer**| The hash identifier for the specific Entity you want returned. | |

### Return type

[**Destiny2GetDestinyEntityDefinition200Response**](Destiny2GetDestinyEntityDefinition200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Provides common properties for destiny definitions. |  -  |

<a id="destiny2GetDestinyManifest"></a>
# **destiny2GetDestinyManifest**
> Destiny2GetDestinyManifest200Response destiny2GetDestinyManifest()



Returns the current version of the manifest as a json object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    try {
      Destiny2GetDestinyManifest200Response result = apiInstance.destiny2GetDestinyManifest();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2GetDestinyManifest");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Destiny2GetDestinyManifest200Response**](Destiny2GetDestinyManifest200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | DestinyManifest is the external-facing contract for just the properties needed by those calling the Destiny Platform. |  -  |

<a id="destiny2GetHistoricalStats"></a>
# **destiny2GetHistoricalStats**
> Destiny2GetHistoricalStats200Response destiny2GetHistoricalStats(characterId, destinyMembershipId, membershipType, dayend, daystart, groups, modes, periodType)



Gets historical stats for indicated character.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    Long characterId = 56L; // Long | The id of the character to retrieve. You can omit this character ID or set it to 0 to get aggregate stats across all characters.
    Long destinyMembershipId = 56L; // Long | The Destiny membershipId of the user to retrieve.
    Integer membershipType = 56; // Integer | A valid non-BungieNet membership type.
    OffsetDateTime dayend = OffsetDateTime.now(); // OffsetDateTime | Last day to return when daily stats are requested. Use the format YYYY-MM-DD. Currently, we cannot allow more than 31 days of daily data to be requested in a single request.
    OffsetDateTime daystart = OffsetDateTime.now(); // OffsetDateTime | First day to return when daily stats are requested. Use the format YYYY-MM-DD. Currently, we cannot allow more than 31 days of daily data to be requested in a single request.
    List<Integer> groups = Arrays.asList(); // List<Integer> | Group of stats to include, otherwise only general stats are returned. Comma separated list is allowed. Values: General, Weapons, Medals
    List<Integer> modes = Arrays.asList(); // List<Integer> | Game modes to return. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
    Integer periodType = 56; // Integer | Indicates a specific period type to return. Optional. May be: Daily, AllTime, or Activity
    try {
      Destiny2GetHistoricalStats200Response result = apiInstance.destiny2GetHistoricalStats(characterId, destinyMembershipId, membershipType, dayend, daystart, groups, modes, periodType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2GetHistoricalStats");
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
| **characterId** | **Long**| The id of the character to retrieve. You can omit this character ID or set it to 0 to get aggregate stats across all characters. | |
| **destinyMembershipId** | **Long**| The Destiny membershipId of the user to retrieve. | |
| **membershipType** | **Integer**| A valid non-BungieNet membership type. | |
| **dayend** | **OffsetDateTime**| Last day to return when daily stats are requested. Use the format YYYY-MM-DD. Currently, we cannot allow more than 31 days of daily data to be requested in a single request. | [optional] |
| **daystart** | **OffsetDateTime**| First day to return when daily stats are requested. Use the format YYYY-MM-DD. Currently, we cannot allow more than 31 days of daily data to be requested in a single request. | [optional] |
| **groups** | [**List&lt;Integer&gt;**](Integer.md)| Group of stats to include, otherwise only general stats are returned. Comma separated list is allowed. Values: General, Weapons, Medals | [optional] |
| **modes** | [**List&lt;Integer&gt;**](Integer.md)| Game modes to return. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. | [optional] |
| **periodType** | **Integer**| Indicates a specific period type to return. Optional. May be: Daily, AllTime, or Activity | [optional] |

### Return type

[**Destiny2GetHistoricalStats200Response**](Destiny2GetHistoricalStats200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="destiny2GetHistoricalStatsDefinition"></a>
# **destiny2GetHistoricalStatsDefinition**
> Destiny2GetHistoricalStatsDefinition200Response destiny2GetHistoricalStatsDefinition()



Gets historical stats definitions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    try {
      Destiny2GetHistoricalStatsDefinition200Response result = apiInstance.destiny2GetHistoricalStatsDefinition();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2GetHistoricalStatsDefinition");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Destiny2GetHistoricalStatsDefinition200Response**](Destiny2GetHistoricalStatsDefinition200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="destiny2GetHistoricalStatsForAccount"></a>
# **destiny2GetHistoricalStatsForAccount**
> Destiny2GetHistoricalStatsForAccount200Response destiny2GetHistoricalStatsForAccount(destinyMembershipId, membershipType, groups)



Gets aggregate historical stats organized around each character for a given account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    Long destinyMembershipId = 56L; // Long | The Destiny membershipId of the user to retrieve.
    Integer membershipType = 56; // Integer | A valid non-BungieNet membership type.
    List<Integer> groups = Arrays.asList(); // List<Integer> | Groups of stats to include, otherwise only general stats are returned. Comma separated list is allowed. Values: General, Weapons, Medals.
    try {
      Destiny2GetHistoricalStatsForAccount200Response result = apiInstance.destiny2GetHistoricalStatsForAccount(destinyMembershipId, membershipType, groups);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2GetHistoricalStatsForAccount");
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
| **destinyMembershipId** | **Long**| The Destiny membershipId of the user to retrieve. | |
| **membershipType** | **Integer**| A valid non-BungieNet membership type. | |
| **groups** | [**List&lt;Integer&gt;**](Integer.md)| Groups of stats to include, otherwise only general stats are returned. Comma separated list is allowed. Values: General, Weapons, Medals. | [optional] |

### Return type

[**Destiny2GetHistoricalStatsForAccount200Response**](Destiny2GetHistoricalStatsForAccount200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="destiny2GetItem"></a>
# **destiny2GetItem**
> Destiny2GetItem200Response destiny2GetItem(destinyMembershipId, itemInstanceId, membershipType, components)



Retrieve the details of an instanced Destiny Item. An instanced Destiny item is one with an ItemInstanceId. Non-instanced items, such as materials, have no useful instance-specific details and thus are not queryable here.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    Long destinyMembershipId = 56L; // Long | The membership ID of the destiny profile.
    Long itemInstanceId = 56L; // Long | The Instance ID of the destiny item.
    Integer membershipType = 56; // Integer | A valid non-BungieNet membership type.
    List<Integer> components = Arrays.asList(); // List<Integer> | A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
    try {
      Destiny2GetItem200Response result = apiInstance.destiny2GetItem(destinyMembershipId, itemInstanceId, membershipType, components);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2GetItem");
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
| **destinyMembershipId** | **Long**| The membership ID of the destiny profile. | |
| **itemInstanceId** | **Long**| The Instance ID of the destiny item. | |
| **membershipType** | **Integer**| A valid non-BungieNet membership type. | |
| **components** | [**List&lt;Integer&gt;**](Integer.md)| A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results. | [optional] |

### Return type

[**Destiny2GetItem200Response**](Destiny2GetItem200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response object for retrieving an individual instanced item. None of these components are relevant for an item that doesn&#39;t have an \&quot;itemInstanceId\&quot;: for those, get your information from the DestinyInventoryDefinition. |  -  |

<a id="destiny2GetLeaderboards"></a>
# **destiny2GetLeaderboards**
> Destiny2GetClanLeaderboards200Response destiny2GetLeaderboards(destinyMembershipId, membershipType, maxtop, modes, statid)



Gets leaderboards with the signed in user&#39;s friends and the supplied destinyMembershipId as the focus. PREVIEW: This endpoint has not yet been implemented. It is being returned for a preview of future functionality, and for public comment/suggestion/preparation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    Long destinyMembershipId = 56L; // Long | The Destiny membershipId of the user to retrieve.
    Integer membershipType = 56; // Integer | A valid non-BungieNet membership type.
    Integer maxtop = 56; // Integer | Maximum number of top players to return. Use a large number to get entire leaderboard.
    String modes = "modes_example"; // String | List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
    String statid = "statid_example"; // String | ID of stat to return rather than returning all Leaderboard stats.
    try {
      Destiny2GetClanLeaderboards200Response result = apiInstance.destiny2GetLeaderboards(destinyMembershipId, membershipType, maxtop, modes, statid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2GetLeaderboards");
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
| **destinyMembershipId** | **Long**| The Destiny membershipId of the user to retrieve. | |
| **membershipType** | **Integer**| A valid non-BungieNet membership type. | |
| **maxtop** | **Integer**| Maximum number of top players to return. Use a large number to get entire leaderboard. | [optional] |
| **modes** | **String**| List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. | [optional] |
| **statid** | **String**| ID of stat to return rather than returning all Leaderboard stats. | [optional] |

### Return type

[**Destiny2GetClanLeaderboards200Response**](Destiny2GetClanLeaderboards200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="destiny2GetLeaderboardsForCharacter"></a>
# **destiny2GetLeaderboardsForCharacter**
> Destiny2GetClanLeaderboards200Response destiny2GetLeaderboardsForCharacter(characterId, destinyMembershipId, membershipType, maxtop, modes, statid)



Gets leaderboards with the signed in user&#39;s friends and the supplied destinyMembershipId as the focus. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is in final form, but there may be bugs that prevent desirable operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    Long characterId = 56L; // Long | The specific character to build the leaderboard around for the provided Destiny Membership.
    Long destinyMembershipId = 56L; // Long | The Destiny membershipId of the user to retrieve.
    Integer membershipType = 56; // Integer | A valid non-BungieNet membership type.
    Integer maxtop = 56; // Integer | Maximum number of top players to return. Use a large number to get entire leaderboard.
    String modes = "modes_example"; // String | List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
    String statid = "statid_example"; // String | ID of stat to return rather than returning all Leaderboard stats.
    try {
      Destiny2GetClanLeaderboards200Response result = apiInstance.destiny2GetLeaderboardsForCharacter(characterId, destinyMembershipId, membershipType, maxtop, modes, statid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2GetLeaderboardsForCharacter");
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
| **characterId** | **Long**| The specific character to build the leaderboard around for the provided Destiny Membership. | |
| **destinyMembershipId** | **Long**| The Destiny membershipId of the user to retrieve. | |
| **membershipType** | **Integer**| A valid non-BungieNet membership type. | |
| **maxtop** | **Integer**| Maximum number of top players to return. Use a large number to get entire leaderboard. | [optional] |
| **modes** | **String**| List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. | [optional] |
| **statid** | **String**| ID of stat to return rather than returning all Leaderboard stats. | [optional] |

### Return type

[**Destiny2GetClanLeaderboards200Response**](Destiny2GetClanLeaderboards200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="destiny2GetLinkedProfiles"></a>
# **destiny2GetLinkedProfiles**
> Destiny2GetLinkedProfiles200Response destiny2GetLinkedProfiles(membershipId, membershipType, getAllMemberships)



Returns a summary information about all profiles linked to the requesting membership type/membership ID that have valid Destiny information. The passed-in Membership Type/Membership ID may be a Bungie.Net membership or a Destiny membership. It only returns the minimal amount of data to begin making more substantive requests, but will hopefully serve as a useful alternative to UserServices for people who just care about Destiny data. Note that it will only return linked accounts whose linkages you are allowed to view.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    Long membershipId = 56L; // Long | The ID of the membership whose linked Destiny accounts you want returned. Make sure your membership ID matches its Membership Type: don't pass us a PSN membership ID and the XBox membership type, it's not going to work!
    Integer membershipType = 56; // Integer | The type for the membership whose linked Destiny accounts you want returned.
    Boolean getAllMemberships = true; // Boolean | (optional) if set to 'true', all memberships regardless of whether they're obscured by overrides will be returned. Normal privacy restrictions on account linking will still apply no matter what.
    try {
      Destiny2GetLinkedProfiles200Response result = apiInstance.destiny2GetLinkedProfiles(membershipId, membershipType, getAllMemberships);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2GetLinkedProfiles");
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
| **membershipId** | **Long**| The ID of the membership whose linked Destiny accounts you want returned. Make sure your membership ID matches its Membership Type: don&#39;t pass us a PSN membership ID and the XBox membership type, it&#39;s not going to work! | |
| **membershipType** | **Integer**| The type for the membership whose linked Destiny accounts you want returned. | |
| **getAllMemberships** | **Boolean**| (optional) if set to &#39;true&#39;, all memberships regardless of whether they&#39;re obscured by overrides will be returned. Normal privacy restrictions on account linking will still apply no matter what. | [optional] |

### Return type

[**Destiny2GetLinkedProfiles200Response**](Destiny2GetLinkedProfiles200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | I know what you seek. You seek linked accounts. Found them, you have.  This contract returns a minimal amount of data about Destiny Accounts that are linked through your Bungie.Net account. We will not return accounts in this response whose |  -  |

<a id="destiny2GetPostGameCarnageReport"></a>
# **destiny2GetPostGameCarnageReport**
> Destiny2GetPostGameCarnageReport200Response destiny2GetPostGameCarnageReport(activityId)



Gets the available post game carnage report for the activity ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    Long activityId = 56L; // Long | The ID of the activity whose PGCR is requested.
    try {
      Destiny2GetPostGameCarnageReport200Response result = apiInstance.destiny2GetPostGameCarnageReport(activityId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2GetPostGameCarnageReport");
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
| **activityId** | **Long**| The ID of the activity whose PGCR is requested. | |

### Return type

[**Destiny2GetPostGameCarnageReport200Response**](Destiny2GetPostGameCarnageReport200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="destiny2GetProfile"></a>
# **destiny2GetProfile**
> Destiny2GetProfile200Response destiny2GetProfile(destinyMembershipId, membershipType, components)



Returns Destiny Profile information for the supplied membership.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    Long destinyMembershipId = 56L; // Long | Destiny membership ID.
    Integer membershipType = 56; // Integer | A valid non-BungieNet membership type.
    List<Integer> components = Arrays.asList(); // List<Integer> | A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
    try {
      Destiny2GetProfile200Response result = apiInstance.destiny2GetProfile(destinyMembershipId, membershipType, components);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2GetProfile");
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
| **destinyMembershipId** | **Long**| Destiny membership ID. | |
| **membershipType** | **Integer**| A valid non-BungieNet membership type. | |
| **components** | [**List&lt;Integer&gt;**](Integer.md)| A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results. | [optional] |

### Return type

[**Destiny2GetProfile200Response**](Destiny2GetProfile200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response for GetDestinyProfile, with components for character and item-level data. |  -  |

<a id="destiny2GetPublicMilestoneContent"></a>
# **destiny2GetPublicMilestoneContent**
> Destiny2GetPublicMilestoneContent200Response destiny2GetPublicMilestoneContent(milestoneHash)



Gets custom localized content for the milestone of the given hash, if it exists.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    Integer milestoneHash = 56; // Integer | The identifier for the milestone to be returned.
    try {
      Destiny2GetPublicMilestoneContent200Response result = apiInstance.destiny2GetPublicMilestoneContent(milestoneHash);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2GetPublicMilestoneContent");
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
| **milestoneHash** | **Integer**| The identifier for the milestone to be returned. | |

### Return type

[**Destiny2GetPublicMilestoneContent200Response**](Destiny2GetPublicMilestoneContent200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Represents localized, extended content related to Milestones. This is intentionally returned by a separate endpoint and not with Character-level Milestone data because we do not put localized data into standard Destiny responses, both for brevity of response and for caching purposes. If you really need this data, hit the Milestone Content endpoint. |  -  |

<a id="destiny2GetPublicMilestones"></a>
# **destiny2GetPublicMilestones**
> Destiny2GetPublicMilestones200Response destiny2GetPublicMilestones()



Gets public information about currently available Milestones.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    try {
      Destiny2GetPublicMilestones200Response result = apiInstance.destiny2GetPublicMilestones();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2GetPublicMilestones");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Destiny2GetPublicMilestones200Response**](Destiny2GetPublicMilestones200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="destiny2GetPublicVendors"></a>
# **destiny2GetPublicVendors**
> Destiny2GetPublicVendors200Response destiny2GetPublicVendors(components)



Get items available from vendors where the vendors have items for sale that are common for everyone. If any portion of the Vendor&#39;s available inventory is character or account specific, we will be unable to return their data from this endpoint due to the way that available inventory is computed. As I am often guilty of saying: &#39;It&#39;s a long story...&#39;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    List<Integer> components = Arrays.asList(); // List<Integer> | A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
    try {
      Destiny2GetPublicVendors200Response result = apiInstance.destiny2GetPublicVendors(components);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2GetPublicVendors");
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
| **components** | [**List&lt;Integer&gt;**](Integer.md)| A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results. | [optional] |

### Return type

[**Destiny2GetPublicVendors200Response**](Destiny2GetPublicVendors200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A response containing all valid components for the public Vendors endpoint.   It is a decisively smaller subset of data compared to what we can get when we know the specific user making the request.   If you want any of the other data - item details, whether or not you can buy it, etc... you&#39;ll have to call in the context of a character. I know, sad but true. |  -  |

<a id="destiny2GetUniqueWeaponHistory"></a>
# **destiny2GetUniqueWeaponHistory**
> Destiny2GetUniqueWeaponHistory200Response destiny2GetUniqueWeaponHistory(characterId, destinyMembershipId, membershipType)



Gets details about unique weapon usage, including all exotic weapons.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    Long characterId = 56L; // Long | The id of the character to retrieve.
    Long destinyMembershipId = 56L; // Long | The Destiny membershipId of the user to retrieve.
    Integer membershipType = 56; // Integer | A valid non-BungieNet membership type.
    try {
      Destiny2GetUniqueWeaponHistory200Response result = apiInstance.destiny2GetUniqueWeaponHistory(characterId, destinyMembershipId, membershipType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2GetUniqueWeaponHistory");
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
| **characterId** | **Long**| The id of the character to retrieve. | |
| **destinyMembershipId** | **Long**| The Destiny membershipId of the user to retrieve. | |
| **membershipType** | **Integer**| A valid non-BungieNet membership type. | |

### Return type

[**Destiny2GetUniqueWeaponHistory200Response**](Destiny2GetUniqueWeaponHistory200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="destiny2GetVendor"></a>
# **destiny2GetVendor**
> Destiny2GetVendor200Response destiny2GetVendor(characterId, destinyMembershipId, membershipType, vendorHash, components)



Get the details of a specific Vendor.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    Long characterId = 56L; // Long | The Destiny Character ID of the character for whom we're getting vendor info.
    Long destinyMembershipId = 56L; // Long | Destiny membership ID of another user. You may be denied.
    Integer membershipType = 56; // Integer | A valid non-BungieNet membership type.
    Integer vendorHash = 56; // Integer | The Hash identifier of the Vendor to be returned.
    List<Integer> components = Arrays.asList(); // List<Integer> | A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
    try {
      Destiny2GetVendor200Response result = apiInstance.destiny2GetVendor(characterId, destinyMembershipId, membershipType, vendorHash, components);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2GetVendor");
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
| **characterId** | **Long**| The Destiny Character ID of the character for whom we&#39;re getting vendor info. | |
| **destinyMembershipId** | **Long**| Destiny membership ID of another user. You may be denied. | |
| **membershipType** | **Integer**| A valid non-BungieNet membership type. | |
| **vendorHash** | **Integer**| The Hash identifier of the Vendor to be returned. | |
| **components** | [**List&lt;Integer&gt;**](Integer.md)| A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results. | [optional] |

### Return type

[**Destiny2GetVendor200Response**](Destiny2GetVendor200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A response containing all of the components for a vendor. |  -  |

<a id="destiny2GetVendors"></a>
# **destiny2GetVendors**
> Destiny2GetVendors200Response destiny2GetVendors(characterId, destinyMembershipId, membershipType, components, filter)



Get currently available vendors from the list of vendors that can possibly have rotating inventory. Note that this does not include things like preview vendors and vendors-as-kiosks, neither of whom have rotating/dynamic inventories. Use their definitions as-is for those.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    Long characterId = 56L; // Long | The Destiny Character ID of the character for whom we're getting vendor info.
    Long destinyMembershipId = 56L; // Long | Destiny membership ID of another user. You may be denied.
    Integer membershipType = 56; // Integer | A valid non-BungieNet membership type.
    List<Integer> components = Arrays.asList(); // List<Integer> | A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
    Integer filter = 56; // Integer | The filter of what vendors and items to return, if any.
    try {
      Destiny2GetVendors200Response result = apiInstance.destiny2GetVendors(characterId, destinyMembershipId, membershipType, components, filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2GetVendors");
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
| **characterId** | **Long**| The Destiny Character ID of the character for whom we&#39;re getting vendor info. | |
| **destinyMembershipId** | **Long**| Destiny membership ID of another user. You may be denied. | |
| **membershipType** | **Integer**| A valid non-BungieNet membership type. | |
| **components** | [**List&lt;Integer&gt;**](Integer.md)| A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results. | [optional] |
| **filter** | **Integer**| The filter of what vendors and items to return, if any. | [optional] |

### Return type

[**Destiny2GetVendors200Response**](Destiny2GetVendors200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A response containing all of the components for all requested vendors. |  -  |

<a id="destiny2InsertSocketPlug"></a>
# **destiny2InsertSocketPlug**
> Destiny2InsertSocketPlug200Response destiny2InsertSocketPlug()



Insert a plug into a socketed item. I know how it sounds, but I assure you it&#39;s much more G-rated than you might be guessing. We haven&#39;t decided yet whether this will be able to insert plugs that have side effects, but if we do it will require special scope permission for an application attempting to do so. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline. Request must include proof of permission for &#39;InsertPlugs&#39; from the account owner.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    try {
      Destiny2InsertSocketPlug200Response result = apiInstance.destiny2InsertSocketPlug();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2InsertSocketPlug");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Destiny2InsertSocketPlug200Response**](Destiny2InsertSocketPlug200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="destiny2InsertSocketPlugFree"></a>
# **destiny2InsertSocketPlugFree**
> Destiny2InsertSocketPlug200Response destiny2InsertSocketPlugFree()



Insert a &#39;free&#39; plug into an item&#39;s socket. This does not require &#39;Advanced Write Action&#39; authorization and is available to 3rd-party apps, but will only work on &#39;free and reversible&#39; socket actions (Perks, Armor Mods, Shaders, Ornaments, etc.). You must have a valid Destiny Account, and the character must either be in a social space, in orbit, or offline.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    try {
      Destiny2InsertSocketPlug200Response result = apiInstance.destiny2InsertSocketPlugFree();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2InsertSocketPlugFree");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Destiny2InsertSocketPlug200Response**](Destiny2InsertSocketPlug200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="destiny2PullFromPostmaster"></a>
# **destiny2PullFromPostmaster**
> Destiny2EquipItem200Response destiny2PullFromPostmaster()



Extract an item from the Postmaster, with whatever implications that may entail. You must have a valid Destiny account. You must also pass BOTH a reference AND an instance ID if it&#39;s an instanced item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    try {
      Destiny2EquipItem200Response result = apiInstance.destiny2PullFromPostmaster();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2PullFromPostmaster");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Destiny2EquipItem200Response**](Destiny2EquipItem200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="destiny2ReportOffensivePostGameCarnageReportPlayer"></a>
# **destiny2ReportOffensivePostGameCarnageReportPlayer**
> Destiny2EquipItem200Response destiny2ReportOffensivePostGameCarnageReportPlayer(activityId)



Report a player that you met in an activity that was engaging in ToS-violating activities. Both you and the offending player must have played in the activityId passed in. Please use this judiciously and only when you have strong suspicions of violation, pretty please.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    Long activityId = 56L; // Long | The ID of the activity where you ran into the brigand that you're reporting.
    try {
      Destiny2EquipItem200Response result = apiInstance.destiny2ReportOffensivePostGameCarnageReportPlayer(activityId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2ReportOffensivePostGameCarnageReportPlayer");
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
| **activityId** | **Long**| The ID of the activity where you ran into the brigand that you&#39;re reporting. | |

### Return type

[**Destiny2EquipItem200Response**](Destiny2EquipItem200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="destiny2SearchDestinyEntities"></a>
# **destiny2SearchDestinyEntities**
> Destiny2SearchDestinyEntities200Response destiny2SearchDestinyEntities(searchTerm, type, page)



Gets a page list of Destiny items.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    String searchTerm = "searchTerm_example"; // String | The string to use when searching for Destiny entities.
    String type = "type_example"; // String | The type of entity for whom you would like results. These correspond to the entity's definition contract name. For instance, if you are looking for items, this property should be 'DestinyInventoryItemDefinition'.
    Integer page = 56; // Integer | Page number to return, starting with 0.
    try {
      Destiny2SearchDestinyEntities200Response result = apiInstance.destiny2SearchDestinyEntities(searchTerm, type, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2SearchDestinyEntities");
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
| **searchTerm** | **String**| The string to use when searching for Destiny entities. | |
| **type** | **String**| The type of entity for whom you would like results. These correspond to the entity&#39;s definition contract name. For instance, if you are looking for items, this property should be &#39;DestinyInventoryItemDefinition&#39;. | |
| **page** | **Integer**| Page number to return, starting with 0. | [optional] |

### Return type

[**Destiny2SearchDestinyEntities200Response**](Destiny2SearchDestinyEntities200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The results of a search for Destiny content. This will be improved on over time, I&#39;ve been doing some experimenting to see what might be useful. |  -  |

<a id="destiny2SearchDestinyPlayerByBungieName"></a>
# **destiny2SearchDestinyPlayerByBungieName**
> Destiny2SearchDestinyPlayerByBungieName200Response destiny2SearchDestinyPlayerByBungieName(membershipType)



Returns a list of Destiny memberships given a global Bungie Display Name. This method will hide overridden memberships due to cross save.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    Integer membershipType = 56; // Integer | A valid non-BungieNet membership type, or All. Indicates which memberships to return. You probably want this set to All.
    try {
      Destiny2SearchDestinyPlayerByBungieName200Response result = apiInstance.destiny2SearchDestinyPlayerByBungieName(membershipType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2SearchDestinyPlayerByBungieName");
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
| **membershipType** | **Integer**| A valid non-BungieNet membership type, or All. Indicates which memberships to return. You probably want this set to All. | |

### Return type

[**Destiny2SearchDestinyPlayerByBungieName200Response**](Destiny2SearchDestinyPlayerByBungieName200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="destiny2SetItemLockState"></a>
# **destiny2SetItemLockState**
> Destiny2EquipItem200Response destiny2SetItemLockState()



Set the Lock State for an instanced item. You must have a valid Destiny Account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    try {
      Destiny2EquipItem200Response result = apiInstance.destiny2SetItemLockState();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2SetItemLockState");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Destiny2EquipItem200Response**](Destiny2EquipItem200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="destiny2SetQuestTrackedState"></a>
# **destiny2SetQuestTrackedState**
> Destiny2EquipItem200Response destiny2SetQuestTrackedState()



Set the Tracking State for an instanced item, if that item is a Quest or Bounty. You must have a valid Destiny Account. Yeah, it&#39;s an item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    try {
      Destiny2EquipItem200Response result = apiInstance.destiny2SetQuestTrackedState();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2SetQuestTrackedState");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Destiny2EquipItem200Response**](Destiny2EquipItem200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="destiny2SnapshotLoadout"></a>
# **destiny2SnapshotLoadout**
> Destiny2EquipItem200Response destiny2SnapshotLoadout()



Snapshot a loadout with the currently equipped items.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    try {
      Destiny2EquipItem200Response result = apiInstance.destiny2SnapshotLoadout();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2SnapshotLoadout");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Destiny2EquipItem200Response**](Destiny2EquipItem200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="destiny2TransferItem"></a>
# **destiny2TransferItem**
> Destiny2EquipItem200Response destiny2TransferItem()



Transfer an item to/from your vault. You must have a valid Destiny account. You must also pass BOTH a reference AND an instance ID if it&#39;s an instanced item. itshappening.gif

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    try {
      Destiny2EquipItem200Response result = apiInstance.destiny2TransferItem();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2TransferItem");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Destiny2EquipItem200Response**](Destiny2EquipItem200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="destiny2UpdateLoadoutIdentifiers"></a>
# **destiny2UpdateLoadoutIdentifiers**
> Destiny2EquipItem200Response destiny2UpdateLoadoutIdentifiers()



Update the color, icon, and name of a loadout.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Destiny2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    Destiny2Api apiInstance = new Destiny2Api(defaultClient);
    try {
      Destiny2EquipItem200Response result = apiInstance.destiny2UpdateLoadoutIdentifiers();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Destiny2Api#destiny2UpdateLoadoutIdentifiers");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Destiny2EquipItem200Response**](Destiny2EquipItem200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

