# BungieNetApi.PreviewApi

All URIs are relative to *https://www.bungie.net/Platform*

Method | HTTP request | Description
------------- | ------------- | -------------
[**destiny2GetClanAggregateStats_0**](PreviewApi.md#destiny2GetClanAggregateStats_0) | **GET** /Destiny2/Stats/AggregateClanStats/{groupId}/ | 
[**destiny2GetClanLeaderboards_0**](PreviewApi.md#destiny2GetClanLeaderboards_0) | **GET** /Destiny2/Stats/Leaderboards/Clans/{groupId}/ | 
[**destiny2GetLeaderboardsForCharacter_0**](PreviewApi.md#destiny2GetLeaderboardsForCharacter_0) | **GET** /Destiny2/Stats/Leaderboards/{membershipType}/{destinyMembershipId}/{characterId}/ | 
[**destiny2GetLeaderboards_0**](PreviewApi.md#destiny2GetLeaderboards_0) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Stats/Leaderboards/ | 
[**destiny2GetPublicVendors_0**](PreviewApi.md#destiny2GetPublicVendors_0) | **GET** /Destiny2/Vendors/ | 
[**destiny2InsertSocketPlugFree_0**](PreviewApi.md#destiny2InsertSocketPlugFree_0) | **POST** /Destiny2/Actions/Items/InsertSocketPlugFree/ | 
[**destiny2InsertSocketPlug_0**](PreviewApi.md#destiny2InsertSocketPlug_0) | **POST** /Destiny2/Actions/Items/InsertSocketPlug/ | 



## destiny2GetClanAggregateStats_0

> Destiny2GetClanAggregateStats200Response destiny2GetClanAggregateStats_0(groupId, opts)



Gets aggregated stats for a clan using the same categories as the clan leaderboards. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is in final form, but there may be bugs that prevent desirable operation.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.PreviewApi();
let groupId = 789; // Number | Group ID of the clan whose leaderboards you wish to fetch.
let opts = {
  'modes': "modes_example" // String | List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
};
apiInstance.destiny2GetClanAggregateStats_0(groupId, opts, (error, data, response) => {
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


## destiny2GetClanLeaderboards_0

> Destiny2GetClanLeaderboards200Response destiny2GetClanLeaderboards_0(groupId, opts)



Gets leaderboards with the signed in user&#39;s friends and the supplied destinyMembershipId as the focus. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is in final form, but there may be bugs that prevent desirable operation.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.PreviewApi();
let groupId = 789; // Number | Group ID of the clan whose leaderboards you wish to fetch.
let opts = {
  'maxtop': 56, // Number | Maximum number of top players to return. Use a large number to get entire leaderboard.
  'modes': "modes_example", // String | List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
  'statid': "statid_example" // String | ID of stat to return rather than returning all Leaderboard stats.
};
apiInstance.destiny2GetClanLeaderboards_0(groupId, opts, (error, data, response) => {
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


## destiny2GetLeaderboardsForCharacter_0

> Destiny2GetClanLeaderboards200Response destiny2GetLeaderboardsForCharacter_0(characterId, destinyMembershipId, membershipType, opts)



Gets leaderboards with the signed in user&#39;s friends and the supplied destinyMembershipId as the focus. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is in final form, but there may be bugs that prevent desirable operation.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.PreviewApi();
let characterId = 789; // Number | The specific character to build the leaderboard around for the provided Destiny Membership.
let destinyMembershipId = 789; // Number | The Destiny membershipId of the user to retrieve.
let membershipType = 56; // Number | A valid non-BungieNet membership type.
let opts = {
  'maxtop': 56, // Number | Maximum number of top players to return. Use a large number to get entire leaderboard.
  'modes': "modes_example", // String | List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
  'statid': "statid_example" // String | ID of stat to return rather than returning all Leaderboard stats.
};
apiInstance.destiny2GetLeaderboardsForCharacter_0(characterId, destinyMembershipId, membershipType, opts, (error, data, response) => {
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


## destiny2GetLeaderboards_0

> Destiny2GetClanLeaderboards200Response destiny2GetLeaderboards_0(destinyMembershipId, membershipType, opts)



Gets leaderboards with the signed in user&#39;s friends and the supplied destinyMembershipId as the focus. PREVIEW: This endpoint has not yet been implemented. It is being returned for a preview of future functionality, and for public comment/suggestion/preparation.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.PreviewApi();
let destinyMembershipId = 789; // Number | The Destiny membershipId of the user to retrieve.
let membershipType = 56; // Number | A valid non-BungieNet membership type.
let opts = {
  'maxtop': 56, // Number | Maximum number of top players to return. Use a large number to get entire leaderboard.
  'modes': "modes_example", // String | List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
  'statid': "statid_example" // String | ID of stat to return rather than returning all Leaderboard stats.
};
apiInstance.destiny2GetLeaderboards_0(destinyMembershipId, membershipType, opts, (error, data, response) => {
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


## destiny2GetPublicVendors_0

> Destiny2GetPublicVendors200Response destiny2GetPublicVendors_0(opts)



Get items available from vendors where the vendors have items for sale that are common for everyone. If any portion of the Vendor&#39;s available inventory is character or account specific, we will be unable to return their data from this endpoint due to the way that available inventory is computed. As I am often guilty of saying: &#39;It&#39;s a long story...&#39;

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.PreviewApi();
let opts = {
  'components': [null] // [Number] | A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
};
apiInstance.destiny2GetPublicVendors_0(opts, (error, data, response) => {
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


## destiny2InsertSocketPlugFree_0

> Destiny2InsertSocketPlug200Response destiny2InsertSocketPlugFree_0()



Insert a &#39;free&#39; plug into an item&#39;s socket. This does not require &#39;Advanced Write Action&#39; authorization and is available to 3rd-party apps, but will only work on &#39;free and reversible&#39; socket actions (Perks, Armor Mods, Shaders, Ornaments, etc.). You must have a valid Destiny Account, and the character must either be in a social space, in orbit, or offline.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.PreviewApi();
apiInstance.destiny2InsertSocketPlugFree_0((error, data, response) => {
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


## destiny2InsertSocketPlug_0

> Destiny2InsertSocketPlug200Response destiny2InsertSocketPlug_0()



Insert a plug into a socketed item. I know how it sounds, but I assure you it&#39;s much more G-rated than you might be guessing. We haven&#39;t decided yet whether this will be able to insert plugs that have side effects, but if we do it will require special scope permission for an application attempting to do so. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline. Request must include proof of permission for &#39;InsertPlugs&#39; from the account owner.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.PreviewApi();
apiInstance.destiny2InsertSocketPlug_0((error, data, response) => {
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

