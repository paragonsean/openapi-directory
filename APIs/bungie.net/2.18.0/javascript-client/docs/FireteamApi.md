# BungieNetApi.FireteamApi

All URIs are relative to *https://www.bungie.net/Platform*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fireteamGetActivePrivateClanFireteamCount**](FireteamApi.md#fireteamGetActivePrivateClanFireteamCount) | **GET** /Fireteam/Clan/{groupId}/ActiveCount/ | 
[**fireteamGetAvailableClanFireteams**](FireteamApi.md#fireteamGetAvailableClanFireteams) | **GET** /Fireteam/Clan/{groupId}/Available/{platform}/{activityType}/{dateRange}/{slotFilter}/{publicOnly}/{page}/ | 
[**fireteamGetClanFireteam**](FireteamApi.md#fireteamGetClanFireteam) | **GET** /Fireteam/Clan/{groupId}/Summary/{fireteamId}/ | 
[**fireteamGetMyClanFireteams**](FireteamApi.md#fireteamGetMyClanFireteams) | **GET** /Fireteam/Clan/{groupId}/My/{platform}/{includeClosed}/{page}/ | 
[**fireteamSearchPublicAvailableClanFireteams**](FireteamApi.md#fireteamSearchPublicAvailableClanFireteams) | **GET** /Fireteam/Search/Available/{platform}/{activityType}/{dateRange}/{slotFilter}/{page}/ | 



## fireteamGetActivePrivateClanFireteamCount

> Destiny2EquipItem200Response fireteamGetActivePrivateClanFireteamCount(groupId)



Gets a count of all active non-public fireteams for the specified clan. Maximum value returned is 25.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.FireteamApi();
let groupId = 789; // Number | The group id of the clan.
apiInstance.fireteamGetActivePrivateClanFireteamCount(groupId, (error, data, response) => {
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
 **groupId** | **Number**| The group id of the clan. | 

### Return type

[**Destiny2EquipItem200Response**](Destiny2EquipItem200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## fireteamGetAvailableClanFireteams

> FireteamGetAvailableClanFireteams200Response fireteamGetAvailableClanFireteams(activityType, dateRange, groupId, page, platform, publicOnly, slotFilter, opts)



Gets a listing of all of this clan&#39;s fireteams that are have available slots. Caller is not checked for join criteria so caching is maximized.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.FireteamApi();
let activityType = 56; // Number | The activity type to filter by.
let dateRange = 56; // Number | The date range to grab available fireteams.
let groupId = 789; // Number | The group id of the clan.
let page = 56; // Number | Zero based page
let platform = 56; // Number | The platform filter.
let publicOnly = 56; // Number | Determines public/private filtering.
let slotFilter = 56; // Number | Filters based on available slots
let opts = {
  'excludeImmediate': true, // Boolean | If you wish the result to exclude immediate fireteams, set this to true. Immediate-only can be forced using the dateRange enum.
  'langFilter': "langFilter_example" // String | An optional language filter.
};
apiInstance.fireteamGetAvailableClanFireteams(activityType, dateRange, groupId, page, platform, publicOnly, slotFilter, opts, (error, data, response) => {
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
 **activityType** | **Number**| The activity type to filter by. | 
 **dateRange** | **Number**| The date range to grab available fireteams. | 
 **groupId** | **Number**| The group id of the clan. | 
 **page** | **Number**| Zero based page | 
 **platform** | **Number**| The platform filter. | 
 **publicOnly** | **Number**| Determines public/private filtering. | 
 **slotFilter** | **Number**| Filters based on available slots | 
 **excludeImmediate** | **Boolean**| If you wish the result to exclude immediate fireteams, set this to true. Immediate-only can be forced using the dateRange enum. | [optional] 
 **langFilter** | **String**| An optional language filter. | [optional] 

### Return type

[**FireteamGetAvailableClanFireteams200Response**](FireteamGetAvailableClanFireteams200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## fireteamGetClanFireteam

> FireteamGetClanFireteam200Response fireteamGetClanFireteam(fireteamId, groupId)



Gets a specific fireteam.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.FireteamApi();
let fireteamId = 789; // Number | The unique id of the fireteam.
let groupId = 789; // Number | The group id of the clan.
apiInstance.fireteamGetClanFireteam(fireteamId, groupId, (error, data, response) => {
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
 **fireteamId** | **Number**| The unique id of the fireteam. | 
 **groupId** | **Number**| The group id of the clan. | 

### Return type

[**FireteamGetClanFireteam200Response**](FireteamGetClanFireteam200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## fireteamGetMyClanFireteams

> FireteamGetMyClanFireteams200Response fireteamGetMyClanFireteams(groupId, includeClosed, page, platform, opts)



Gets a listing of all fireteams that caller is an applicant, a member, or an alternate of.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.FireteamApi();
let groupId = 789; // Number | The group id of the clan. (This parameter is ignored unless the optional query parameter groupFilter is true).
let includeClosed = true; // Boolean | If true, return fireteams that have been closed.
let page = 56; // Number | Deprecated parameter, ignored.
let platform = 56; // Number | The platform filter.
let opts = {
  'groupFilter': true, // Boolean | If true, filter by clan. Otherwise, ignore the clan and show all of the user's fireteams.
  'langFilter': "langFilter_example" // String | An optional language filter.
};
apiInstance.fireteamGetMyClanFireteams(groupId, includeClosed, page, platform, opts, (error, data, response) => {
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
 **groupId** | **Number**| The group id of the clan. (This parameter is ignored unless the optional query parameter groupFilter is true). | 
 **includeClosed** | **Boolean**| If true, return fireteams that have been closed. | 
 **page** | **Number**| Deprecated parameter, ignored. | 
 **platform** | **Number**| The platform filter. | 
 **groupFilter** | **Boolean**| If true, filter by clan. Otherwise, ignore the clan and show all of the user&#39;s fireteams. | [optional] 
 **langFilter** | **String**| An optional language filter. | [optional] 

### Return type

[**FireteamGetMyClanFireteams200Response**](FireteamGetMyClanFireteams200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## fireteamSearchPublicAvailableClanFireteams

> FireteamGetAvailableClanFireteams200Response fireteamSearchPublicAvailableClanFireteams(activityType, dateRange, page, platform, slotFilter, opts)



Gets a listing of all public fireteams starting now with open slots. Caller is not checked for join criteria so caching is maximized.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.FireteamApi();
let activityType = 56; // Number | The activity type to filter by.
let dateRange = 56; // Number | The date range to grab available fireteams.
let page = 56; // Number | Zero based page
let platform = 56; // Number | The platform filter.
let slotFilter = 56; // Number | Filters based on available slots
let opts = {
  'excludeImmediate': true, // Boolean | If you wish the result to exclude immediate fireteams, set this to true. Immediate-only can be forced using the dateRange enum.
  'langFilter': "langFilter_example" // String | An optional language filter.
};
apiInstance.fireteamSearchPublicAvailableClanFireteams(activityType, dateRange, page, platform, slotFilter, opts, (error, data, response) => {
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
 **activityType** | **Number**| The activity type to filter by. | 
 **dateRange** | **Number**| The date range to grab available fireteams. | 
 **page** | **Number**| Zero based page | 
 **platform** | **Number**| The platform filter. | 
 **slotFilter** | **Number**| Filters based on available slots | 
 **excludeImmediate** | **Boolean**| If you wish the result to exclude immediate fireteams, set this to true. Immediate-only can be forced using the dateRange enum. | [optional] 
 **langFilter** | **String**| An optional language filter. | [optional] 

### Return type

[**FireteamGetAvailableClanFireteams200Response**](FireteamGetAvailableClanFireteams200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

