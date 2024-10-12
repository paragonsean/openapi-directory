# BungieNetApi.TokensApi

All URIs are relative to *https://www.bungie.net/Platform*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tokensApplyMissingPartnerOffersWithoutClaim**](TokensApi.md#tokensApplyMissingPartnerOffersWithoutClaim) | **POST** /Tokens/Partner/ApplyMissingOffers/{partnerApplicationId}/{targetBnetMembershipId}/ | 
[**tokensClaimPartnerOffer**](TokensApi.md#tokensClaimPartnerOffer) | **POST** /Tokens/Partner/ClaimOffer/ | 
[**tokensForceDropsRepair**](TokensApi.md#tokensForceDropsRepair) | **POST** /Tokens/Partner/ForceDropsRepair/ | 
[**tokensGetBungieRewardsForPlatformUser**](TokensApi.md#tokensGetBungieRewardsForPlatformUser) | **GET** /Tokens/Rewards/GetRewardsForPlatformUser/{membershipId}/{membershipType}/ | 
[**tokensGetBungieRewardsForUser**](TokensApi.md#tokensGetBungieRewardsForUser) | **GET** /Tokens/Rewards/GetRewardsForUser/{membershipId}/ | 
[**tokensGetBungieRewardsList**](TokensApi.md#tokensGetBungieRewardsList) | **GET** /Tokens/Rewards/BungieRewards/ | 
[**tokensGetPartnerOfferSkuHistory**](TokensApi.md#tokensGetPartnerOfferSkuHistory) | **GET** /Tokens/Partner/History/{partnerApplicationId}/{targetBnetMembershipId}/ | 
[**tokensGetPartnerRewardHistory**](TokensApi.md#tokensGetPartnerRewardHistory) | **GET** /Tokens/Partner/History/{targetBnetMembershipId}/Application/{partnerApplicationId}/ | 



## tokensApplyMissingPartnerOffersWithoutClaim

> GroupV2GetUserClanInviteSetting200Response tokensApplyMissingPartnerOffersWithoutClaim(partnerApplicationId, targetBnetMembershipId)



Apply a partner offer to the targeted user. This endpoint does not claim a new offer, but any already claimed offers will be applied to the game if not already.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.TokensApi();
let partnerApplicationId = 56; // Number | The partner application identifier.
let targetBnetMembershipId = 789; // Number | The bungie.net user to apply missing offers to. If not self, elevated permissions are required.
apiInstance.tokensApplyMissingPartnerOffersWithoutClaim(partnerApplicationId, targetBnetMembershipId, (error, data, response) => {
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
 **partnerApplicationId** | **Number**| The partner application identifier. | 
 **targetBnetMembershipId** | **Number**| The bungie.net user to apply missing offers to. If not self, elevated permissions are required. | 

### Return type

[**GroupV2GetUserClanInviteSetting200Response**](GroupV2GetUserClanInviteSetting200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## tokensClaimPartnerOffer

> GroupV2GetUserClanInviteSetting200Response tokensClaimPartnerOffer()



Claim a partner offer as the authenticated user.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.TokensApi();
apiInstance.tokensClaimPartnerOffer((error, data, response) => {
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

[**GroupV2GetUserClanInviteSetting200Response**](GroupV2GetUserClanInviteSetting200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## tokensForceDropsRepair

> GroupV2GetUserClanInviteSetting200Response tokensForceDropsRepair()



Twitch Drops self-repair function - scans twitch for drops not marked as fulfilled and resyncs them.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.TokensApi();
apiInstance.tokensForceDropsRepair((error, data, response) => {
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

[**GroupV2GetUserClanInviteSetting200Response**](GroupV2GetUserClanInviteSetting200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## tokensGetBungieRewardsForPlatformUser

> TokensGetBungieRewardsList200Response tokensGetBungieRewardsForPlatformUser(membershipId, membershipType)



Returns the bungie rewards for the targeted user when a platform membership Id and Type are used.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.TokensApi();
let membershipId = 789; // Number | users platform membershipId for requested user rewards. If not self, elevated permissions are required.
let membershipType = 56; // Number | The target Destiny 2 membership type.
apiInstance.tokensGetBungieRewardsForPlatformUser(membershipId, membershipType, (error, data, response) => {
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
 **membershipId** | **Number**| users platform membershipId for requested user rewards. If not self, elevated permissions are required. | 
 **membershipType** | **Number**| The target Destiny 2 membership type. | 

### Return type

[**TokensGetBungieRewardsList200Response**](TokensGetBungieRewardsList200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## tokensGetBungieRewardsForUser

> TokensGetBungieRewardsList200Response tokensGetBungieRewardsForUser(membershipId)



Returns the bungie rewards for the targeted user.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.TokensApi();
let membershipId = 789; // Number | bungie.net user membershipId for requested user rewards. If not self, elevated permissions are required.
apiInstance.tokensGetBungieRewardsForUser(membershipId, (error, data, response) => {
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
 **membershipId** | **Number**| bungie.net user membershipId for requested user rewards. If not self, elevated permissions are required. | 

### Return type

[**TokensGetBungieRewardsList200Response**](TokensGetBungieRewardsList200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## tokensGetBungieRewardsList

> TokensGetBungieRewardsList200Response tokensGetBungieRewardsList()



Returns a list of the current bungie rewards

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.TokensApi();
apiInstance.tokensGetBungieRewardsList((error, data, response) => {
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

[**TokensGetBungieRewardsList200Response**](TokensGetBungieRewardsList200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## tokensGetPartnerOfferSkuHistory

> TokensGetPartnerOfferSkuHistory200Response tokensGetPartnerOfferSkuHistory(partnerApplicationId, targetBnetMembershipId)



Returns the partner sku and offer history of the targeted user. Elevated permissions are required to see users that are not yourself.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.TokensApi();
let partnerApplicationId = 56; // Number | The partner application identifier.
let targetBnetMembershipId = 789; // Number | The bungie.net user to apply missing offers to. If not self, elevated permissions are required.
apiInstance.tokensGetPartnerOfferSkuHistory(partnerApplicationId, targetBnetMembershipId, (error, data, response) => {
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
 **partnerApplicationId** | **Number**| The partner application identifier. | 
 **targetBnetMembershipId** | **Number**| The bungie.net user to apply missing offers to. If not self, elevated permissions are required. | 

### Return type

[**TokensGetPartnerOfferSkuHistory200Response**](TokensGetPartnerOfferSkuHistory200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## tokensGetPartnerRewardHistory

> TokensGetPartnerRewardHistory200Response tokensGetPartnerRewardHistory(partnerApplicationId, targetBnetMembershipId)



Returns the partner rewards history of the targeted user, both partner offers and Twitch drops.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.TokensApi();
let partnerApplicationId = 56; // Number | The partner application identifier.
let targetBnetMembershipId = 789; // Number | The bungie.net user to return reward history for.
apiInstance.tokensGetPartnerRewardHistory(partnerApplicationId, targetBnetMembershipId, (error, data, response) => {
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
 **partnerApplicationId** | **Number**| The partner application identifier. | 
 **targetBnetMembershipId** | **Number**| The bungie.net user to return reward history for. | 

### Return type

[**TokensGetPartnerRewardHistory200Response**](TokensGetPartnerRewardHistory200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

