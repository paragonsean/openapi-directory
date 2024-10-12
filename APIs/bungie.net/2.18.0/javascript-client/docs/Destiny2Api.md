# BungieNetApi.Destiny2Api

All URIs are relative to *https://www.bungie.net/Platform*

Method | HTTP request | Description
------------- | ------------- | -------------
[**destiny2AwaGetActionToken**](Destiny2Api.md#destiny2AwaGetActionToken) | **GET** /Destiny2/Awa/GetActionToken/{correlationId}/ | 
[**destiny2AwaInitializeRequest**](Destiny2Api.md#destiny2AwaInitializeRequest) | **POST** /Destiny2/Awa/Initialize/ | 
[**destiny2AwaProvideAuthorizationResult**](Destiny2Api.md#destiny2AwaProvideAuthorizationResult) | **POST** /Destiny2/Awa/AwaProvideAuthorizationResult/ | 
[**destiny2ClearLoadout**](Destiny2Api.md#destiny2ClearLoadout) | **POST** /Destiny2/Actions/Loadouts/ClearLoadout/ | 
[**destiny2EquipItem**](Destiny2Api.md#destiny2EquipItem) | **POST** /Destiny2/Actions/Items/EquipItem/ | 
[**destiny2EquipItems**](Destiny2Api.md#destiny2EquipItems) | **POST** /Destiny2/Actions/Items/EquipItems/ | 
[**destiny2EquipLoadout**](Destiny2Api.md#destiny2EquipLoadout) | **POST** /Destiny2/Actions/Loadouts/EquipLoadout/ | 
[**destiny2GetActivityHistory**](Destiny2Api.md#destiny2GetActivityHistory) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/Activities/ | 
[**destiny2GetCharacter**](Destiny2Api.md#destiny2GetCharacter) | **GET** /Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/ | 
[**destiny2GetClanAggregateStats**](Destiny2Api.md#destiny2GetClanAggregateStats) | **GET** /Destiny2/Stats/AggregateClanStats/{groupId}/ | 
[**destiny2GetClanBannerSource**](Destiny2Api.md#destiny2GetClanBannerSource) | **GET** /Destiny2/Clan/ClanBannerDictionary/ | 
[**destiny2GetClanLeaderboards**](Destiny2Api.md#destiny2GetClanLeaderboards) | **GET** /Destiny2/Stats/Leaderboards/Clans/{groupId}/ | 
[**destiny2GetClanWeeklyRewardState**](Destiny2Api.md#destiny2GetClanWeeklyRewardState) | **GET** /Destiny2/Clan/{groupId}/WeeklyRewardState/ | 
[**destiny2GetCollectibleNodeDetails**](Destiny2Api.md#destiny2GetCollectibleNodeDetails) | **GET** /Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/Collectibles/{collectiblePresentationNodeHash}/ | 
[**destiny2GetDestinyAggregateActivityStats**](Destiny2Api.md#destiny2GetDestinyAggregateActivityStats) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/AggregateActivityStats/ | 
[**destiny2GetDestinyEntityDefinition**](Destiny2Api.md#destiny2GetDestinyEntityDefinition) | **GET** /Destiny2/Manifest/{entityType}/{hashIdentifier}/ | 
[**destiny2GetDestinyManifest**](Destiny2Api.md#destiny2GetDestinyManifest) | **GET** /Destiny2/Manifest/ | 
[**destiny2GetHistoricalStats**](Destiny2Api.md#destiny2GetHistoricalStats) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/ | 
[**destiny2GetHistoricalStatsDefinition**](Destiny2Api.md#destiny2GetHistoricalStatsDefinition) | **GET** /Destiny2/Stats/Definition/ | 
[**destiny2GetHistoricalStatsForAccount**](Destiny2Api.md#destiny2GetHistoricalStatsForAccount) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Stats/ | 
[**destiny2GetItem**](Destiny2Api.md#destiny2GetItem) | **GET** /Destiny2/{membershipType}/Profile/{destinyMembershipId}/Item/{itemInstanceId}/ | 
[**destiny2GetLeaderboards**](Destiny2Api.md#destiny2GetLeaderboards) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Stats/Leaderboards/ | 
[**destiny2GetLeaderboardsForCharacter**](Destiny2Api.md#destiny2GetLeaderboardsForCharacter) | **GET** /Destiny2/Stats/Leaderboards/{membershipType}/{destinyMembershipId}/{characterId}/ | 
[**destiny2GetLinkedProfiles**](Destiny2Api.md#destiny2GetLinkedProfiles) | **GET** /Destiny2/{membershipType}/Profile/{membershipId}/LinkedProfiles/ | 
[**destiny2GetPostGameCarnageReport**](Destiny2Api.md#destiny2GetPostGameCarnageReport) | **GET** /Destiny2/Stats/PostGameCarnageReport/{activityId}/ | 
[**destiny2GetProfile**](Destiny2Api.md#destiny2GetProfile) | **GET** /Destiny2/{membershipType}/Profile/{destinyMembershipId}/ | 
[**destiny2GetPublicMilestoneContent**](Destiny2Api.md#destiny2GetPublicMilestoneContent) | **GET** /Destiny2/Milestones/{milestoneHash}/Content/ | 
[**destiny2GetPublicMilestones**](Destiny2Api.md#destiny2GetPublicMilestones) | **GET** /Destiny2/Milestones/ | 
[**destiny2GetPublicVendors**](Destiny2Api.md#destiny2GetPublicVendors) | **GET** /Destiny2/Vendors/ | 
[**destiny2GetUniqueWeaponHistory**](Destiny2Api.md#destiny2GetUniqueWeaponHistory) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/UniqueWeapons/ | 
[**destiny2GetVendor**](Destiny2Api.md#destiny2GetVendor) | **GET** /Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/Vendors/{vendorHash}/ | 
[**destiny2GetVendors**](Destiny2Api.md#destiny2GetVendors) | **GET** /Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/Vendors/ | 
[**destiny2InsertSocketPlug**](Destiny2Api.md#destiny2InsertSocketPlug) | **POST** /Destiny2/Actions/Items/InsertSocketPlug/ | 
[**destiny2InsertSocketPlugFree**](Destiny2Api.md#destiny2InsertSocketPlugFree) | **POST** /Destiny2/Actions/Items/InsertSocketPlugFree/ | 
[**destiny2PullFromPostmaster**](Destiny2Api.md#destiny2PullFromPostmaster) | **POST** /Destiny2/Actions/Items/PullFromPostmaster/ | 
[**destiny2ReportOffensivePostGameCarnageReportPlayer**](Destiny2Api.md#destiny2ReportOffensivePostGameCarnageReportPlayer) | **POST** /Destiny2/Stats/PostGameCarnageReport/{activityId}/Report/ | 
[**destiny2SearchDestinyEntities**](Destiny2Api.md#destiny2SearchDestinyEntities) | **GET** /Destiny2/Armory/Search/{type}/{searchTerm}/ | 
[**destiny2SearchDestinyPlayerByBungieName**](Destiny2Api.md#destiny2SearchDestinyPlayerByBungieName) | **POST** /Destiny2/SearchDestinyPlayerByBungieName/{membershipType}/ | 
[**destiny2SetItemLockState**](Destiny2Api.md#destiny2SetItemLockState) | **POST** /Destiny2/Actions/Items/SetLockState/ | 
[**destiny2SetQuestTrackedState**](Destiny2Api.md#destiny2SetQuestTrackedState) | **POST** /Destiny2/Actions/Items/SetTrackedState/ | 
[**destiny2SnapshotLoadout**](Destiny2Api.md#destiny2SnapshotLoadout) | **POST** /Destiny2/Actions/Loadouts/SnapshotLoadout/ | 
[**destiny2TransferItem**](Destiny2Api.md#destiny2TransferItem) | **POST** /Destiny2/Actions/Items/TransferItem/ | 
[**destiny2UpdateLoadoutIdentifiers**](Destiny2Api.md#destiny2UpdateLoadoutIdentifiers) | **POST** /Destiny2/Actions/Loadouts/UpdateLoadoutIdentifiers/ | 



## destiny2AwaGetActionToken

> Destiny2AwaGetActionToken200Response destiny2AwaGetActionToken(correlationId)



Returns the action token if user approves the request.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.Destiny2Api();
let correlationId = "correlationId_example"; // String | The identifier for the advanced write action request.
apiInstance.destiny2AwaGetActionToken(correlationId, (error, data, response) => {
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
 **correlationId** | **String**| The identifier for the advanced write action request. | 

### Return type

[**Destiny2AwaGetActionToken200Response**](Destiny2AwaGetActionToken200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## destiny2AwaInitializeRequest

> Destiny2AwaInitializeRequest200Response destiny2AwaInitializeRequest()



Initialize a request to perform an advanced write action.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.Destiny2Api();
apiInstance.destiny2AwaInitializeRequest((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## destiny2AwaProvideAuthorizationResult

> Destiny2EquipItem200Response destiny2AwaProvideAuthorizationResult()



Provide the result of the user interaction. Called by the Bungie Destiny App to approve or reject a request.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.Destiny2Api();
apiInstance.destiny2AwaProvideAuthorizationResult((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## destiny2ClearLoadout

> Destiny2EquipItem200Response destiny2ClearLoadout()



Clear the identifiers and items of a loadout.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.Destiny2Api();
apiInstance.destiny2ClearLoadout((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## destiny2EquipItem

> Destiny2EquipItem200Response destiny2EquipItem()



Equip an item. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.Destiny2Api();
apiInstance.destiny2EquipItem((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## destiny2EquipItems

> Destiny2EquipItems200Response destiny2EquipItems()



Equip a list of items by itemInstanceIds. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline. Any items not found on your character will be ignored.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.Destiny2Api();
apiInstance.destiny2EquipItems((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## destiny2EquipLoadout

> Destiny2EquipItem200Response destiny2EquipLoadout()



Equip a loadout. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.Destiny2Api();
apiInstance.destiny2EquipLoadout((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## destiny2GetActivityHistory

> Destiny2GetActivityHistory200Response destiny2GetActivityHistory(characterId, destinyMembershipId, membershipType, opts)



Gets activity history stats for indicated character.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.Destiny2Api();
let characterId = 789; // Number | The id of the character to retrieve.
let destinyMembershipId = 789; // Number | The Destiny membershipId of the user to retrieve.
let membershipType = 56; // Number | A valid non-BungieNet membership type.
let opts = {
  'count': 56, // Number | Number of rows to return
  'mode': 56, // Number | A filter for the activity mode to be returned. None returns all activities. See the documentation for DestinyActivityModeType for valid values, and pass in string representation.
  'page': 56 // Number | Page number to return, starting with 0.
};
apiInstance.destiny2GetActivityHistory(characterId, destinyMembershipId, membershipType, opts, (error, data, response) => {
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
 **characterId** | **Number**| The id of the character to retrieve. | 
 **destinyMembershipId** | **Number**| The Destiny membershipId of the user to retrieve. | 
 **membershipType** | **Number**| A valid non-BungieNet membership type. | 
 **count** | **Number**| Number of rows to return | [optional] 
 **mode** | **Number**| A filter for the activity mode to be returned. None returns all activities. See the documentation for DestinyActivityModeType for valid values, and pass in string representation. | [optional] 
 **page** | **Number**| Page number to return, starting with 0. | [optional] 

### Return type

[**Destiny2GetActivityHistory200Response**](Destiny2GetActivityHistory200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## destiny2GetCharacter

> Destiny2GetCharacter200Response destiny2GetCharacter(characterId, destinyMembershipId, membershipType, opts)



Returns character information for the supplied character.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.Destiny2Api();
let characterId = 789; // Number | ID of the character.
let destinyMembershipId = 789; // Number | Destiny membership ID.
let membershipType = 56; // Number | A valid non-BungieNet membership type.
let opts = {
  'components': [null] // [Number] | A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
};
apiInstance.destiny2GetCharacter(characterId, destinyMembershipId, membershipType, opts, (error, data, response) => {
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
 **characterId** | **Number**| ID of the character. | 
 **destinyMembershipId** | **Number**| Destiny membership ID. | 
 **membershipType** | **Number**| A valid non-BungieNet membership type. | 
 **components** | [**[Number]**](Number.md)| A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results. | [optional] 

### Return type

[**Destiny2GetCharacter200Response**](Destiny2GetCharacter200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## destiny2GetClanAggregateStats

> Destiny2GetClanAggregateStats200Response destiny2GetClanAggregateStats(groupId, opts)



Gets aggregated stats for a clan using the same categories as the clan leaderboards. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is in final form, but there may be bugs that prevent desirable operation.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.Destiny2Api();
let groupId = 789; // Number | Group ID of the clan whose leaderboards you wish to fetch.
let opts = {
  'modes': "modes_example" // String | List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
};
apiInstance.destiny2GetClanAggregateStats(groupId, opts, (error, data, response) => {
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
 **groupId** | **Number**| Group ID of the clan whose leaderboards you wish to fetch. | 
 **modes** | **String**| List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. | [optional] 

### Return type

[**Destiny2GetClanAggregateStats200Response**](Destiny2GetClanAggregateStats200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## destiny2GetClanBannerSource

> Destiny2GetClanBannerSource200Response destiny2GetClanBannerSource()



Returns the dictionary of values for the Clan Banner

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.Destiny2Api();
apiInstance.destiny2GetClanBannerSource((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## destiny2GetClanLeaderboards

> Destiny2GetClanLeaderboards200Response destiny2GetClanLeaderboards(groupId, opts)



Gets leaderboards with the signed in user&#39;s friends and the supplied destinyMembershipId as the focus. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is in final form, but there may be bugs that prevent desirable operation.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.Destiny2Api();
let groupId = 789; // Number | Group ID of the clan whose leaderboards you wish to fetch.
let opts = {
  'maxtop': 56, // Number | Maximum number of top players to return. Use a large number to get entire leaderboard.
  'modes': "modes_example", // String | List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
  'statid': "statid_example" // String | ID of stat to return rather than returning all Leaderboard stats.
};
apiInstance.destiny2GetClanLeaderboards(groupId, opts, (error, data, response) => {
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
 **groupId** | **Number**| Group ID of the clan whose leaderboards you wish to fetch. | 
 **maxtop** | **Number**| Maximum number of top players to return. Use a large number to get entire leaderboard. | [optional] 
 **modes** | **String**| List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. | [optional] 
 **statid** | **String**| ID of stat to return rather than returning all Leaderboard stats. | [optional] 

### Return type

[**Destiny2GetClanLeaderboards200Response**](Destiny2GetClanLeaderboards200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## destiny2GetClanWeeklyRewardState

> Destiny2GetClanWeeklyRewardState200Response destiny2GetClanWeeklyRewardState(groupId)



Returns information on the weekly clan rewards and if the clan has earned them or not. Note that this will always report rewards as not redeemed.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.Destiny2Api();
let groupId = 789; // Number | A valid group id of clan.
apiInstance.destiny2GetClanWeeklyRewardState(groupId, (error, data, response) => {
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
 **groupId** | **Number**| A valid group id of clan. | 

### Return type

[**Destiny2GetClanWeeklyRewardState200Response**](Destiny2GetClanWeeklyRewardState200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## destiny2GetCollectibleNodeDetails

> Destiny2GetCollectibleNodeDetails200Response destiny2GetCollectibleNodeDetails(characterId, collectiblePresentationNodeHash, destinyMembershipId, membershipType, opts)



Given a Presentation Node that has Collectibles as direct descendants, this will return item details about those descendants in the context of the requesting character.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.Destiny2Api();
let characterId = 789; // Number | The Destiny Character ID of the character for whom we're getting collectible detail info.
let collectiblePresentationNodeHash = 56; // Number | The hash identifier of the Presentation Node for whom we should return collectible details. Details will only be returned for collectibles that are direct descendants of this node.
let destinyMembershipId = 789; // Number | Destiny membership ID of another user. You may be denied.
let membershipType = 56; // Number | A valid non-BungieNet membership type.
let opts = {
  'components': [null] // [Number] | A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
};
apiInstance.destiny2GetCollectibleNodeDetails(characterId, collectiblePresentationNodeHash, destinyMembershipId, membershipType, opts, (error, data, response) => {
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
 **characterId** | **Number**| The Destiny Character ID of the character for whom we&#39;re getting collectible detail info. | 
 **collectiblePresentationNodeHash** | **Number**| The hash identifier of the Presentation Node for whom we should return collectible details. Details will only be returned for collectibles that are direct descendants of this node. | 
 **destinyMembershipId** | **Number**| Destiny membership ID of another user. You may be denied. | 
 **membershipType** | **Number**| A valid non-BungieNet membership type. | 
 **components** | [**[Number]**](Number.md)| A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results. | [optional] 

### Return type

[**Destiny2GetCollectibleNodeDetails200Response**](Destiny2GetCollectibleNodeDetails200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## destiny2GetDestinyAggregateActivityStats

> Destiny2GetDestinyAggregateActivityStats200Response destiny2GetDestinyAggregateActivityStats(characterId, destinyMembershipId, membershipType)



Gets all activities the character has participated in together with aggregate statistics for those activities.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.Destiny2Api();
let characterId = 789; // Number | The specific character whose activities should be returned.
let destinyMembershipId = 789; // Number | The Destiny membershipId of the user to retrieve.
let membershipType = 56; // Number | A valid non-BungieNet membership type.
apiInstance.destiny2GetDestinyAggregateActivityStats(characterId, destinyMembershipId, membershipType, (error, data, response) => {
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
 **characterId** | **Number**| The specific character whose activities should be returned. | 
 **destinyMembershipId** | **Number**| The Destiny membershipId of the user to retrieve. | 
 **membershipType** | **Number**| A valid non-BungieNet membership type. | 

### Return type

[**Destiny2GetDestinyAggregateActivityStats200Response**](Destiny2GetDestinyAggregateActivityStats200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## destiny2GetDestinyEntityDefinition

> Destiny2GetDestinyEntityDefinition200Response destiny2GetDestinyEntityDefinition(entityType, hashIdentifier)



Returns the static definition of an entity of the given Type and hash identifier. Examine the API Documentation for the Type Names of entities that have their own definitions. Note that the return type will always *inherit from* DestinyDefinition, but the specific type returned will be the requested entity type if it can be found. Please don&#39;t use this as a chatty alternative to the Manifest database if you require large sets of data, but for simple and one-off accesses this should be handy.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.Destiny2Api();
let entityType = "entityType_example"; // String | The type of entity for whom you would like results. These correspond to the entity's definition contract name. For instance, if you are looking for items, this property should be 'DestinyInventoryItemDefinition'. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is tentatively in final form, but there may be bugs that prevent desirable operation.
let hashIdentifier = 56; // Number | The hash identifier for the specific Entity you want returned.
apiInstance.destiny2GetDestinyEntityDefinition(entityType, hashIdentifier, (error, data, response) => {
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
 **entityType** | **String**| The type of entity for whom you would like results. These correspond to the entity&#39;s definition contract name. For instance, if you are looking for items, this property should be &#39;DestinyInventoryItemDefinition&#39;. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is tentatively in final form, but there may be bugs that prevent desirable operation. | 
 **hashIdentifier** | **Number**| The hash identifier for the specific Entity you want returned. | 

### Return type

[**Destiny2GetDestinyEntityDefinition200Response**](Destiny2GetDestinyEntityDefinition200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## destiny2GetDestinyManifest

> Destiny2GetDestinyManifest200Response destiny2GetDestinyManifest()



Returns the current version of the manifest as a json object.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.Destiny2Api();
apiInstance.destiny2GetDestinyManifest((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## destiny2GetHistoricalStats

> Destiny2GetHistoricalStats200Response destiny2GetHistoricalStats(characterId, destinyMembershipId, membershipType, opts)



Gets historical stats for indicated character.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.Destiny2Api();
let characterId = 789; // Number | The id of the character to retrieve. You can omit this character ID or set it to 0 to get aggregate stats across all characters.
let destinyMembershipId = 789; // Number | The Destiny membershipId of the user to retrieve.
let membershipType = 56; // Number | A valid non-BungieNet membership type.
let opts = {
  'dayend': new Date("2013-10-20T19:20:30+01:00"), // Date | Last day to return when daily stats are requested. Use the format YYYY-MM-DD. Currently, we cannot allow more than 31 days of daily data to be requested in a single request.
  'daystart': new Date("2013-10-20T19:20:30+01:00"), // Date | First day to return when daily stats are requested. Use the format YYYY-MM-DD. Currently, we cannot allow more than 31 days of daily data to be requested in a single request.
  'groups': [null], // [Number] | Group of stats to include, otherwise only general stats are returned. Comma separated list is allowed. Values: General, Weapons, Medals
  'modes': [null], // [Number] | Game modes to return. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
  'periodType': 56 // Number | Indicates a specific period type to return. Optional. May be: Daily, AllTime, or Activity
};
apiInstance.destiny2GetHistoricalStats(characterId, destinyMembershipId, membershipType, opts, (error, data, response) => {
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
 **characterId** | **Number**| The id of the character to retrieve. You can omit this character ID or set it to 0 to get aggregate stats across all characters. | 
 **destinyMembershipId** | **Number**| The Destiny membershipId of the user to retrieve. | 
 **membershipType** | **Number**| A valid non-BungieNet membership type. | 
 **dayend** | **Date**| Last day to return when daily stats are requested. Use the format YYYY-MM-DD. Currently, we cannot allow more than 31 days of daily data to be requested in a single request. | [optional] 
 **daystart** | **Date**| First day to return when daily stats are requested. Use the format YYYY-MM-DD. Currently, we cannot allow more than 31 days of daily data to be requested in a single request. | [optional] 
 **groups** | [**[Number]**](Number.md)| Group of stats to include, otherwise only general stats are returned. Comma separated list is allowed. Values: General, Weapons, Medals | [optional] 
 **modes** | [**[Number]**](Number.md)| Game modes to return. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. | [optional] 
 **periodType** | **Number**| Indicates a specific period type to return. Optional. May be: Daily, AllTime, or Activity | [optional] 

### Return type

[**Destiny2GetHistoricalStats200Response**](Destiny2GetHistoricalStats200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## destiny2GetHistoricalStatsDefinition

> Destiny2GetHistoricalStatsDefinition200Response destiny2GetHistoricalStatsDefinition()



Gets historical stats definitions.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.Destiny2Api();
apiInstance.destiny2GetHistoricalStatsDefinition((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## destiny2GetHistoricalStatsForAccount

> Destiny2GetHistoricalStatsForAccount200Response destiny2GetHistoricalStatsForAccount(destinyMembershipId, membershipType, opts)



Gets aggregate historical stats organized around each character for a given account.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.Destiny2Api();
let destinyMembershipId = 789; // Number | The Destiny membershipId of the user to retrieve.
let membershipType = 56; // Number | A valid non-BungieNet membership type.
let opts = {
  'groups': [null] // [Number] | Groups of stats to include, otherwise only general stats are returned. Comma separated list is allowed. Values: General, Weapons, Medals.
};
apiInstance.destiny2GetHistoricalStatsForAccount(destinyMembershipId, membershipType, opts, (error, data, response) => {
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
 **destinyMembershipId** | **Number**| The Destiny membershipId of the user to retrieve. | 
 **membershipType** | **Number**| A valid non-BungieNet membership type. | 
 **groups** | [**[Number]**](Number.md)| Groups of stats to include, otherwise only general stats are returned. Comma separated list is allowed. Values: General, Weapons, Medals. | [optional] 

### Return type

[**Destiny2GetHistoricalStatsForAccount200Response**](Destiny2GetHistoricalStatsForAccount200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## destiny2GetItem

> Destiny2GetItem200Response destiny2GetItem(destinyMembershipId, itemInstanceId, membershipType, opts)



Retrieve the details of an instanced Destiny Item. An instanced Destiny item is one with an ItemInstanceId. Non-instanced items, such as materials, have no useful instance-specific details and thus are not queryable here.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.Destiny2Api();
let destinyMembershipId = 789; // Number | The membership ID of the destiny profile.
let itemInstanceId = 789; // Number | The Instance ID of the destiny item.
let membershipType = 56; // Number | A valid non-BungieNet membership type.
let opts = {
  'components': [null] // [Number] | A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
};
apiInstance.destiny2GetItem(destinyMembershipId, itemInstanceId, membershipType, opts, (error, data, response) => {
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
 **destinyMembershipId** | **Number**| The membership ID of the destiny profile. | 
 **itemInstanceId** | **Number**| The Instance ID of the destiny item. | 
 **membershipType** | **Number**| A valid non-BungieNet membership type. | 
 **components** | [**[Number]**](Number.md)| A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results. | [optional] 

### Return type

[**Destiny2GetItem200Response**](Destiny2GetItem200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## destiny2GetLeaderboards

> Destiny2GetClanLeaderboards200Response destiny2GetLeaderboards(destinyMembershipId, membershipType, opts)



Gets leaderboards with the signed in user&#39;s friends and the supplied destinyMembershipId as the focus. PREVIEW: This endpoint has not yet been implemented. It is being returned for a preview of future functionality, and for public comment/suggestion/preparation.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.Destiny2Api();
let destinyMembershipId = 789; // Number | The Destiny membershipId of the user to retrieve.
let membershipType = 56; // Number | A valid non-BungieNet membership type.
let opts = {
  'maxtop': 56, // Number | Maximum number of top players to return. Use a large number to get entire leaderboard.
  'modes': "modes_example", // String | List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
  'statid': "statid_example" // String | ID of stat to return rather than returning all Leaderboard stats.
};
apiInstance.destiny2GetLeaderboards(destinyMembershipId, membershipType, opts, (error, data, response) => {
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
 **destinyMembershipId** | **Number**| The Destiny membershipId of the user to retrieve. | 
 **membershipType** | **Number**| A valid non-BungieNet membership type. | 
 **maxtop** | **Number**| Maximum number of top players to return. Use a large number to get entire leaderboard. | [optional] 
 **modes** | **String**| List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. | [optional] 
 **statid** | **String**| ID of stat to return rather than returning all Leaderboard stats. | [optional] 

### Return type

[**Destiny2GetClanLeaderboards200Response**](Destiny2GetClanLeaderboards200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## destiny2GetLeaderboardsForCharacter

> Destiny2GetClanLeaderboards200Response destiny2GetLeaderboardsForCharacter(characterId, destinyMembershipId, membershipType, opts)



Gets leaderboards with the signed in user&#39;s friends and the supplied destinyMembershipId as the focus. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is in final form, but there may be bugs that prevent desirable operation.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.Destiny2Api();
let characterId = 789; // Number | The specific character to build the leaderboard around for the provided Destiny Membership.
let destinyMembershipId = 789; // Number | The Destiny membershipId of the user to retrieve.
let membershipType = 56; // Number | A valid non-BungieNet membership type.
let opts = {
  'maxtop': 56, // Number | Maximum number of top players to return. Use a large number to get entire leaderboard.
  'modes': "modes_example", // String | List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
  'statid': "statid_example" // String | ID of stat to return rather than returning all Leaderboard stats.
};
apiInstance.destiny2GetLeaderboardsForCharacter(characterId, destinyMembershipId, membershipType, opts, (error, data, response) => {
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
 **characterId** | **Number**| The specific character to build the leaderboard around for the provided Destiny Membership. | 
 **destinyMembershipId** | **Number**| The Destiny membershipId of the user to retrieve. | 
 **membershipType** | **Number**| A valid non-BungieNet membership type. | 
 **maxtop** | **Number**| Maximum number of top players to return. Use a large number to get entire leaderboard. | [optional] 
 **modes** | **String**| List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited. | [optional] 
 **statid** | **String**| ID of stat to return rather than returning all Leaderboard stats. | [optional] 

### Return type

[**Destiny2GetClanLeaderboards200Response**](Destiny2GetClanLeaderboards200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## destiny2GetLinkedProfiles

> Destiny2GetLinkedProfiles200Response destiny2GetLinkedProfiles(membershipId, membershipType, opts)



Returns a summary information about all profiles linked to the requesting membership type/membership ID that have valid Destiny information. The passed-in Membership Type/Membership ID may be a Bungie.Net membership or a Destiny membership. It only returns the minimal amount of data to begin making more substantive requests, but will hopefully serve as a useful alternative to UserServices for people who just care about Destiny data. Note that it will only return linked accounts whose linkages you are allowed to view.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.Destiny2Api();
let membershipId = 789; // Number | The ID of the membership whose linked Destiny accounts you want returned. Make sure your membership ID matches its Membership Type: don't pass us a PSN membership ID and the XBox membership type, it's not going to work!
let membershipType = 56; // Number | The type for the membership whose linked Destiny accounts you want returned.
let opts = {
  'getAllMemberships': true // Boolean | (optional) if set to 'true', all memberships regardless of whether they're obscured by overrides will be returned. Normal privacy restrictions on account linking will still apply no matter what.
};
apiInstance.destiny2GetLinkedProfiles(membershipId, membershipType, opts, (error, data, response) => {
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
 **membershipId** | **Number**| The ID of the membership whose linked Destiny accounts you want returned. Make sure your membership ID matches its Membership Type: don&#39;t pass us a PSN membership ID and the XBox membership type, it&#39;s not going to work! | 
 **membershipType** | **Number**| The type for the membership whose linked Destiny accounts you want returned. | 
 **getAllMemberships** | **Boolean**| (optional) if set to &#39;true&#39;, all memberships regardless of whether they&#39;re obscured by overrides will be returned. Normal privacy restrictions on account linking will still apply no matter what. | [optional] 

### Return type

[**Destiny2GetLinkedProfiles200Response**](Destiny2GetLinkedProfiles200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## destiny2GetPostGameCarnageReport

> Destiny2GetPostGameCarnageReport200Response destiny2GetPostGameCarnageReport(activityId)



Gets the available post game carnage report for the activity ID.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.Destiny2Api();
let activityId = 789; // Number | The ID of the activity whose PGCR is requested.
apiInstance.destiny2GetPostGameCarnageReport(activityId, (error, data, response) => {
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
 **activityId** | **Number**| The ID of the activity whose PGCR is requested. | 

### Return type

[**Destiny2GetPostGameCarnageReport200Response**](Destiny2GetPostGameCarnageReport200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## destiny2GetProfile

> Destiny2GetProfile200Response destiny2GetProfile(destinyMembershipId, membershipType, opts)



Returns Destiny Profile information for the supplied membership.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.Destiny2Api();
let destinyMembershipId = 789; // Number | Destiny membership ID.
let membershipType = 56; // Number | A valid non-BungieNet membership type.
let opts = {
  'components': [null] // [Number] | A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
};
apiInstance.destiny2GetProfile(destinyMembershipId, membershipType, opts, (error, data, response) => {
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
 **destinyMembershipId** | **Number**| Destiny membership ID. | 
 **membershipType** | **Number**| A valid non-BungieNet membership type. | 
 **components** | [**[Number]**](Number.md)| A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results. | [optional] 

### Return type

[**Destiny2GetProfile200Response**](Destiny2GetProfile200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## destiny2GetPublicMilestoneContent

> Destiny2GetPublicMilestoneContent200Response destiny2GetPublicMilestoneContent(milestoneHash)



Gets custom localized content for the milestone of the given hash, if it exists.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.Destiny2Api();
let milestoneHash = 56; // Number | The identifier for the milestone to be returned.
apiInstance.destiny2GetPublicMilestoneContent(milestoneHash, (error, data, response) => {
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
 **milestoneHash** | **Number**| The identifier for the milestone to be returned. | 

### Return type

[**Destiny2GetPublicMilestoneContent200Response**](Destiny2GetPublicMilestoneContent200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## destiny2GetPublicMilestones

> Destiny2GetPublicMilestones200Response destiny2GetPublicMilestones()



Gets public information about currently available Milestones.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.Destiny2Api();
apiInstance.destiny2GetPublicMilestones((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## destiny2GetPublicVendors

> Destiny2GetPublicVendors200Response destiny2GetPublicVendors(opts)



Get items available from vendors where the vendors have items for sale that are common for everyone. If any portion of the Vendor&#39;s available inventory is character or account specific, we will be unable to return their data from this endpoint due to the way that available inventory is computed. As I am often guilty of saying: &#39;It&#39;s a long story...&#39;

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.Destiny2Api();
let opts = {
  'components': [null] // [Number] | A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
};
apiInstance.destiny2GetPublicVendors(opts, (error, data, response) => {
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
 **components** | [**[Number]**](Number.md)| A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results. | [optional] 

### Return type

[**Destiny2GetPublicVendors200Response**](Destiny2GetPublicVendors200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## destiny2GetUniqueWeaponHistory

> Destiny2GetUniqueWeaponHistory200Response destiny2GetUniqueWeaponHistory(characterId, destinyMembershipId, membershipType)



Gets details about unique weapon usage, including all exotic weapons.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.Destiny2Api();
let characterId = 789; // Number | The id of the character to retrieve.
let destinyMembershipId = 789; // Number | The Destiny membershipId of the user to retrieve.
let membershipType = 56; // Number | A valid non-BungieNet membership type.
apiInstance.destiny2GetUniqueWeaponHistory(characterId, destinyMembershipId, membershipType, (error, data, response) => {
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
 **characterId** | **Number**| The id of the character to retrieve. | 
 **destinyMembershipId** | **Number**| The Destiny membershipId of the user to retrieve. | 
 **membershipType** | **Number**| A valid non-BungieNet membership type. | 

### Return type

[**Destiny2GetUniqueWeaponHistory200Response**](Destiny2GetUniqueWeaponHistory200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## destiny2GetVendor

> Destiny2GetVendor200Response destiny2GetVendor(characterId, destinyMembershipId, membershipType, vendorHash, opts)



Get the details of a specific Vendor.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.Destiny2Api();
let characterId = 789; // Number | The Destiny Character ID of the character for whom we're getting vendor info.
let destinyMembershipId = 789; // Number | Destiny membership ID of another user. You may be denied.
let membershipType = 56; // Number | A valid non-BungieNet membership type.
let vendorHash = 56; // Number | The Hash identifier of the Vendor to be returned.
let opts = {
  'components': [null] // [Number] | A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
};
apiInstance.destiny2GetVendor(characterId, destinyMembershipId, membershipType, vendorHash, opts, (error, data, response) => {
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
 **characterId** | **Number**| The Destiny Character ID of the character for whom we&#39;re getting vendor info. | 
 **destinyMembershipId** | **Number**| Destiny membership ID of another user. You may be denied. | 
 **membershipType** | **Number**| A valid non-BungieNet membership type. | 
 **vendorHash** | **Number**| The Hash identifier of the Vendor to be returned. | 
 **components** | [**[Number]**](Number.md)| A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results. | [optional] 

### Return type

[**Destiny2GetVendor200Response**](Destiny2GetVendor200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## destiny2GetVendors

> Destiny2GetVendors200Response destiny2GetVendors(characterId, destinyMembershipId, membershipType, opts)



Get currently available vendors from the list of vendors that can possibly have rotating inventory. Note that this does not include things like preview vendors and vendors-as-kiosks, neither of whom have rotating/dynamic inventories. Use their definitions as-is for those.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.Destiny2Api();
let characterId = 789; // Number | The Destiny Character ID of the character for whom we're getting vendor info.
let destinyMembershipId = 789; // Number | Destiny membership ID of another user. You may be denied.
let membershipType = 56; // Number | A valid non-BungieNet membership type.
let opts = {
  'components': [null], // [Number] | A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
  'filter': 56 // Number | The filter of what vendors and items to return, if any.
};
apiInstance.destiny2GetVendors(characterId, destinyMembershipId, membershipType, opts, (error, data, response) => {
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
 **characterId** | **Number**| The Destiny Character ID of the character for whom we&#39;re getting vendor info. | 
 **destinyMembershipId** | **Number**| Destiny membership ID of another user. You may be denied. | 
 **membershipType** | **Number**| A valid non-BungieNet membership type. | 
 **components** | [**[Number]**](Number.md)| A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results. | [optional] 
 **filter** | **Number**| The filter of what vendors and items to return, if any. | [optional] 

### Return type

[**Destiny2GetVendors200Response**](Destiny2GetVendors200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## destiny2InsertSocketPlug

> Destiny2InsertSocketPlug200Response destiny2InsertSocketPlug()



Insert a plug into a socketed item. I know how it sounds, but I assure you it&#39;s much more G-rated than you might be guessing. We haven&#39;t decided yet whether this will be able to insert plugs that have side effects, but if we do it will require special scope permission for an application attempting to do so. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline. Request must include proof of permission for &#39;InsertPlugs&#39; from the account owner.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.Destiny2Api();
apiInstance.destiny2InsertSocketPlug((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## destiny2InsertSocketPlugFree

> Destiny2InsertSocketPlug200Response destiny2InsertSocketPlugFree()



Insert a &#39;free&#39; plug into an item&#39;s socket. This does not require &#39;Advanced Write Action&#39; authorization and is available to 3rd-party apps, but will only work on &#39;free and reversible&#39; socket actions (Perks, Armor Mods, Shaders, Ornaments, etc.). You must have a valid Destiny Account, and the character must either be in a social space, in orbit, or offline.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.Destiny2Api();
apiInstance.destiny2InsertSocketPlugFree((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## destiny2PullFromPostmaster

> Destiny2EquipItem200Response destiny2PullFromPostmaster()



Extract an item from the Postmaster, with whatever implications that may entail. You must have a valid Destiny account. You must also pass BOTH a reference AND an instance ID if it&#39;s an instanced item.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.Destiny2Api();
apiInstance.destiny2PullFromPostmaster((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## destiny2ReportOffensivePostGameCarnageReportPlayer

> Destiny2EquipItem200Response destiny2ReportOffensivePostGameCarnageReportPlayer(activityId)



Report a player that you met in an activity that was engaging in ToS-violating activities. Both you and the offending player must have played in the activityId passed in. Please use this judiciously and only when you have strong suspicions of violation, pretty please.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.Destiny2Api();
let activityId = 789; // Number | The ID of the activity where you ran into the brigand that you're reporting.
apiInstance.destiny2ReportOffensivePostGameCarnageReportPlayer(activityId, (error, data, response) => {
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
 **activityId** | **Number**| The ID of the activity where you ran into the brigand that you&#39;re reporting. | 

### Return type

[**Destiny2EquipItem200Response**](Destiny2EquipItem200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## destiny2SearchDestinyEntities

> Destiny2SearchDestinyEntities200Response destiny2SearchDestinyEntities(searchTerm, type, opts)



Gets a page list of Destiny items.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.Destiny2Api();
let searchTerm = "searchTerm_example"; // String | The string to use when searching for Destiny entities.
let type = "type_example"; // String | The type of entity for whom you would like results. These correspond to the entity's definition contract name. For instance, if you are looking for items, this property should be 'DestinyInventoryItemDefinition'.
let opts = {
  'page': 56 // Number | Page number to return, starting with 0.
};
apiInstance.destiny2SearchDestinyEntities(searchTerm, type, opts, (error, data, response) => {
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
 **searchTerm** | **String**| The string to use when searching for Destiny entities. | 
 **type** | **String**| The type of entity for whom you would like results. These correspond to the entity&#39;s definition contract name. For instance, if you are looking for items, this property should be &#39;DestinyInventoryItemDefinition&#39;. | 
 **page** | **Number**| Page number to return, starting with 0. | [optional] 

### Return type

[**Destiny2SearchDestinyEntities200Response**](Destiny2SearchDestinyEntities200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## destiny2SearchDestinyPlayerByBungieName

> Destiny2SearchDestinyPlayerByBungieName200Response destiny2SearchDestinyPlayerByBungieName(membershipType)



Returns a list of Destiny memberships given a global Bungie Display Name. This method will hide overridden memberships due to cross save.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.Destiny2Api();
let membershipType = 56; // Number | A valid non-BungieNet membership type, or All. Indicates which memberships to return. You probably want this set to All.
apiInstance.destiny2SearchDestinyPlayerByBungieName(membershipType, (error, data, response) => {
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
 **membershipType** | **Number**| A valid non-BungieNet membership type, or All. Indicates which memberships to return. You probably want this set to All. | 

### Return type

[**Destiny2SearchDestinyPlayerByBungieName200Response**](Destiny2SearchDestinyPlayerByBungieName200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## destiny2SetItemLockState

> Destiny2EquipItem200Response destiny2SetItemLockState()



Set the Lock State for an instanced item. You must have a valid Destiny Account.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.Destiny2Api();
apiInstance.destiny2SetItemLockState((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## destiny2SetQuestTrackedState

> Destiny2EquipItem200Response destiny2SetQuestTrackedState()



Set the Tracking State for an instanced item, if that item is a Quest or Bounty. You must have a valid Destiny Account. Yeah, it&#39;s an item.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.Destiny2Api();
apiInstance.destiny2SetQuestTrackedState((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## destiny2SnapshotLoadout

> Destiny2EquipItem200Response destiny2SnapshotLoadout()



Snapshot a loadout with the currently equipped items.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.Destiny2Api();
apiInstance.destiny2SnapshotLoadout((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## destiny2TransferItem

> Destiny2EquipItem200Response destiny2TransferItem()



Transfer an item to/from your vault. You must have a valid Destiny account. You must also pass BOTH a reference AND an instance ID if it&#39;s an instanced item. itshappening.gif

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.Destiny2Api();
apiInstance.destiny2TransferItem((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## destiny2UpdateLoadoutIdentifiers

> Destiny2EquipItem200Response destiny2UpdateLoadoutIdentifiers()



Update the color, icon, and name of a loadout.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.Destiny2Api();
apiInstance.destiny2UpdateLoadoutIdentifiers((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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

