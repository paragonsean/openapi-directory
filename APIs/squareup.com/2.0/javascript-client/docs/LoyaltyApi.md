# SquareConnectApi.LoyaltyApi

All URIs are relative to *https://connect.squareup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accumulateLoyaltyPoints**](LoyaltyApi.md#accumulateLoyaltyPoints) | **POST** /v2/loyalty/accounts/{account_id}/accumulate | AccumulateLoyaltyPoints
[**adjustLoyaltyPoints**](LoyaltyApi.md#adjustLoyaltyPoints) | **POST** /v2/loyalty/accounts/{account_id}/adjust | AdjustLoyaltyPoints
[**calculateLoyaltyPoints**](LoyaltyApi.md#calculateLoyaltyPoints) | **POST** /v2/loyalty/programs/{program_id}/calculate | CalculateLoyaltyPoints
[**createLoyaltyAccount**](LoyaltyApi.md#createLoyaltyAccount) | **POST** /v2/loyalty/accounts | CreateLoyaltyAccount
[**createLoyaltyReward**](LoyaltyApi.md#createLoyaltyReward) | **POST** /v2/loyalty/rewards | CreateLoyaltyReward
[**deleteLoyaltyReward**](LoyaltyApi.md#deleteLoyaltyReward) | **DELETE** /v2/loyalty/rewards/{reward_id} | DeleteLoyaltyReward
[**listLoyaltyPrograms**](LoyaltyApi.md#listLoyaltyPrograms) | **GET** /v2/loyalty/programs | ListLoyaltyPrograms
[**redeemLoyaltyReward**](LoyaltyApi.md#redeemLoyaltyReward) | **POST** /v2/loyalty/rewards/{reward_id}/redeem | RedeemLoyaltyReward
[**retrieveLoyaltyAccount**](LoyaltyApi.md#retrieveLoyaltyAccount) | **GET** /v2/loyalty/accounts/{account_id} | RetrieveLoyaltyAccount
[**retrieveLoyaltyProgram**](LoyaltyApi.md#retrieveLoyaltyProgram) | **GET** /v2/loyalty/programs/{program_id} | RetrieveLoyaltyProgram
[**retrieveLoyaltyReward**](LoyaltyApi.md#retrieveLoyaltyReward) | **GET** /v2/loyalty/rewards/{reward_id} | RetrieveLoyaltyReward
[**searchLoyaltyAccounts**](LoyaltyApi.md#searchLoyaltyAccounts) | **POST** /v2/loyalty/accounts/search | SearchLoyaltyAccounts
[**searchLoyaltyEvents**](LoyaltyApi.md#searchLoyaltyEvents) | **POST** /v2/loyalty/events/search | SearchLoyaltyEvents
[**searchLoyaltyRewards**](LoyaltyApi.md#searchLoyaltyRewards) | **POST** /v2/loyalty/rewards/search | SearchLoyaltyRewards



## accumulateLoyaltyPoints

> AccumulateLoyaltyPointsResponse accumulateLoyaltyPoints(accountId, accumulateLoyaltyPointsRequest)

AccumulateLoyaltyPoints

Adds points to a loyalty account.  - If you are using the Orders API to manage orders, you only provide the &#x60;order_id&#x60;.  The endpoint reads the order to compute points to add to the buyer&#39;s account. - If you are not using the Orders API to manage orders,  you first perform a client-side computation to compute the points.   For spend-based and visit-based programs, you can first call  [CalculateLoyaltyPoints](https://developer.squareup.com/reference/square_2021-08-18/loyalty-api/calculate-loyalty-points) to compute the points   that you provide to this endpoint.   __Note:__ The country of the seller&#39;s Square account determines whether tax is included in the purchase amount when accruing points for spend-based and visit-based programs.  For more information, see [Availability of Square Loyalty](https://developer.squareup.com/docs/loyalty-api/overview#loyalty-market-availability).

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.LoyaltyApi();
let accountId = "accountId_example"; // String | The [loyalty account](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyAccount) ID to which to add the points.
let accumulateLoyaltyPointsRequest = new SquareConnectApi.AccumulateLoyaltyPointsRequest(); // AccumulateLoyaltyPointsRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.accumulateLoyaltyPoints(accountId, accumulateLoyaltyPointsRequest, (error, data, response) => {
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
 **accountId** | **String**| The [loyalty account](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyAccount) ID to which to add the points. | 
 **accumulateLoyaltyPointsRequest** | [**AccumulateLoyaltyPointsRequest**](AccumulateLoyaltyPointsRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**AccumulateLoyaltyPointsResponse**](AccumulateLoyaltyPointsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## adjustLoyaltyPoints

> AdjustLoyaltyPointsResponse adjustLoyaltyPoints(accountId, adjustLoyaltyPointsRequest)

AdjustLoyaltyPoints

Adds points to or subtracts points from a buyer&#39;s account.   Use this endpoint only when you need to manually adjust points. Otherwise, in your application flow, you call  [AccumulateLoyaltyPoints](https://developer.squareup.com/reference/square_2021-08-18/loyalty-api/accumulate-loyalty-points)  to add points when a buyer pays for the purchase.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.LoyaltyApi();
let accountId = "accountId_example"; // String | The ID of the [loyalty account](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyAccount) in which to adjust the points.
let adjustLoyaltyPointsRequest = new SquareConnectApi.AdjustLoyaltyPointsRequest(); // AdjustLoyaltyPointsRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.adjustLoyaltyPoints(accountId, adjustLoyaltyPointsRequest, (error, data, response) => {
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
 **accountId** | **String**| The ID of the [loyalty account](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyAccount) in which to adjust the points. | 
 **adjustLoyaltyPointsRequest** | [**AdjustLoyaltyPointsRequest**](AdjustLoyaltyPointsRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**AdjustLoyaltyPointsResponse**](AdjustLoyaltyPointsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## calculateLoyaltyPoints

> CalculateLoyaltyPointsResponse calculateLoyaltyPoints(programId, calculateLoyaltyPointsRequest)

CalculateLoyaltyPoints

Calculates the points a purchase earns.  - If you are using the Orders API to manage orders, you provide &#x60;order_id&#x60; in the request. The  endpoint calculates the points by reading the order. - If you are not using the Orders API to manage orders, you provide the purchase amount in  the request for the endpoint to calculate the points.  An application might call this endpoint to show the points that a buyer can earn with the  specific purchase.  __Note:__ The country of the seller&#39;s Square account determines whether tax is included in the purchase amount when accruing points for spend-based and visit-based programs.  For more information, see [Availability of Square Loyalty](https://developer.squareup.com/docs/loyalty-api/overview#loyalty-market-availability).

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.LoyaltyApi();
let programId = "programId_example"; // String | The [loyalty program](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyProgram) ID, which defines the rules for accruing points.
let calculateLoyaltyPointsRequest = new SquareConnectApi.CalculateLoyaltyPointsRequest(); // CalculateLoyaltyPointsRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.calculateLoyaltyPoints(programId, calculateLoyaltyPointsRequest, (error, data, response) => {
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
 **programId** | **String**| The [loyalty program](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyProgram) ID, which defines the rules for accruing points. | 
 **calculateLoyaltyPointsRequest** | [**CalculateLoyaltyPointsRequest**](CalculateLoyaltyPointsRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**CalculateLoyaltyPointsResponse**](CalculateLoyaltyPointsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createLoyaltyAccount

> CreateLoyaltyAccountResponse createLoyaltyAccount(createLoyaltyAccountRequest)

CreateLoyaltyAccount

Creates a loyalty account. To create a loyalty account, you must provide the &#x60;program_id&#x60; and a &#x60;mapping&#x60; with the &#x60;phone_number&#x60; of the buyer.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.LoyaltyApi();
let createLoyaltyAccountRequest = new SquareConnectApi.CreateLoyaltyAccountRequest(); // CreateLoyaltyAccountRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.createLoyaltyAccount(createLoyaltyAccountRequest, (error, data, response) => {
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
 **createLoyaltyAccountRequest** | [**CreateLoyaltyAccountRequest**](CreateLoyaltyAccountRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**CreateLoyaltyAccountResponse**](CreateLoyaltyAccountResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createLoyaltyReward

> CreateLoyaltyRewardResponse createLoyaltyReward(createLoyaltyRewardRequest)

CreateLoyaltyReward

Creates a loyalty reward. In the process, the endpoint does following:  - Uses the &#x60;reward_tier_id&#x60; in the request to determine the number of points  to lock for this reward.  - If the request includes &#x60;order_id&#x60;, it adds the reward and related discount to the order.   After a reward is created, the points are locked and  not available for the buyer to redeem another reward.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.LoyaltyApi();
let createLoyaltyRewardRequest = new SquareConnectApi.CreateLoyaltyRewardRequest(); // CreateLoyaltyRewardRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.createLoyaltyReward(createLoyaltyRewardRequest, (error, data, response) => {
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
 **createLoyaltyRewardRequest** | [**CreateLoyaltyRewardRequest**](CreateLoyaltyRewardRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**CreateLoyaltyRewardResponse**](CreateLoyaltyRewardResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteLoyaltyReward

> DeleteLoyaltyRewardResponse deleteLoyaltyReward(rewardId)

DeleteLoyaltyReward

Deletes a loyalty reward by doing the following:  - Returns the loyalty points back to the loyalty account. - If an order ID was specified when the reward was created  (see [CreateLoyaltyReward](https://developer.squareup.com/reference/square_2021-08-18/loyalty-api/create-loyalty-reward)),  it updates the order by removing the reward and related  discounts.  You cannot delete a reward that has reached the terminal state (REDEEMED).

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.LoyaltyApi();
let rewardId = "rewardId_example"; // String | The ID of the [loyalty reward](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyReward) to delete.
apiInstance.deleteLoyaltyReward(rewardId, (error, data, response) => {
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
 **rewardId** | **String**| The ID of the [loyalty reward](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyReward) to delete. | 

### Return type

[**DeleteLoyaltyRewardResponse**](DeleteLoyaltyRewardResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listLoyaltyPrograms

> ListLoyaltyProgramsResponse listLoyaltyPrograms()

ListLoyaltyPrograms

Returns a list of loyalty programs in the seller&#39;s account. Loyalty programs define how buyers can earn points and redeem points for rewards. Square sellers can have only one loyalty program, which is created and managed from the Seller Dashboard. For more information, see [Loyalty Program Overview](https://developer.squareup.com/docs/loyalty/overview).   Replaced with [RetrieveLoyaltyProgram](https://developer.squareup.com/reference/square_2021-08-18/loyalty-api/retrieve-loyalty-program) when used with the keyword &#x60;main&#x60;.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.LoyaltyApi();
apiInstance.listLoyaltyPrograms((error, data, response) => {
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

[**ListLoyaltyProgramsResponse**](ListLoyaltyProgramsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## redeemLoyaltyReward

> RedeemLoyaltyRewardResponse redeemLoyaltyReward(rewardId, redeemLoyaltyRewardRequest)

RedeemLoyaltyReward

Redeems a loyalty reward.  The endpoint sets the reward to the &#x60;REDEEMED&#x60; terminal state.   If you are using your own order processing system (not using the  Orders API), you call this endpoint after the buyer paid for the  purchase.  After the reward reaches the terminal state, it cannot be deleted.  In other words, points used for the reward cannot be returned  to the account.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.LoyaltyApi();
let rewardId = "rewardId_example"; // String | The ID of the [loyalty reward](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyReward) to redeem.
let redeemLoyaltyRewardRequest = new SquareConnectApi.RedeemLoyaltyRewardRequest(); // RedeemLoyaltyRewardRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.redeemLoyaltyReward(rewardId, redeemLoyaltyRewardRequest, (error, data, response) => {
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
 **rewardId** | **String**| The ID of the [loyalty reward](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyReward) to redeem. | 
 **redeemLoyaltyRewardRequest** | [**RedeemLoyaltyRewardRequest**](RedeemLoyaltyRewardRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**RedeemLoyaltyRewardResponse**](RedeemLoyaltyRewardResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## retrieveLoyaltyAccount

> RetrieveLoyaltyAccountResponse retrieveLoyaltyAccount(accountId)

RetrieveLoyaltyAccount

Retrieves a loyalty account.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.LoyaltyApi();
let accountId = "accountId_example"; // String | The ID of the [loyalty account](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyAccount) to retrieve.
apiInstance.retrieveLoyaltyAccount(accountId, (error, data, response) => {
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
 **accountId** | **String**| The ID of the [loyalty account](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyAccount) to retrieve. | 

### Return type

[**RetrieveLoyaltyAccountResponse**](RetrieveLoyaltyAccountResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveLoyaltyProgram

> RetrieveLoyaltyProgramResponse retrieveLoyaltyProgram(programId)

RetrieveLoyaltyProgram

Retrieves the loyalty program in a seller&#39;s account, specified by the program ID or the keyword &#x60;main&#x60;.   Loyalty programs define how buyers can earn points and redeem points for rewards. Square sellers can have only one loyalty program, which is created and managed from the Seller Dashboard. For more information, see [Loyalty Program Overview](https://developer.squareup.com/docs/loyalty/overview).

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.LoyaltyApi();
let programId = "programId_example"; // String | The ID of the loyalty program or the keyword `main`. Either value can be used to retrieve the single loyalty program that belongs to the seller.
apiInstance.retrieveLoyaltyProgram(programId, (error, data, response) => {
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
 **programId** | **String**| The ID of the loyalty program or the keyword &#x60;main&#x60;. Either value can be used to retrieve the single loyalty program that belongs to the seller. | 

### Return type

[**RetrieveLoyaltyProgramResponse**](RetrieveLoyaltyProgramResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveLoyaltyReward

> RetrieveLoyaltyRewardResponse retrieveLoyaltyReward(rewardId)

RetrieveLoyaltyReward

Retrieves a loyalty reward.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.LoyaltyApi();
let rewardId = "rewardId_example"; // String | The ID of the [loyalty reward](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyReward) to retrieve.
apiInstance.retrieveLoyaltyReward(rewardId, (error, data, response) => {
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
 **rewardId** | **String**| The ID of the [loyalty reward](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyReward) to retrieve. | 

### Return type

[**RetrieveLoyaltyRewardResponse**](RetrieveLoyaltyRewardResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchLoyaltyAccounts

> SearchLoyaltyAccountsResponse searchLoyaltyAccounts(searchLoyaltyAccountsRequest)

SearchLoyaltyAccounts

Searches for loyalty accounts in a loyalty program.    You can search for a loyalty account using the phone number or customer ID associated with the account. To return all loyalty accounts, specify an empty &#x60;query&#x60; object or omit it entirely.    Search results are sorted by &#x60;created_at&#x60; in ascending order.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.LoyaltyApi();
let searchLoyaltyAccountsRequest = new SquareConnectApi.SearchLoyaltyAccountsRequest(); // SearchLoyaltyAccountsRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.searchLoyaltyAccounts(searchLoyaltyAccountsRequest, (error, data, response) => {
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
 **searchLoyaltyAccountsRequest** | [**SearchLoyaltyAccountsRequest**](SearchLoyaltyAccountsRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**SearchLoyaltyAccountsResponse**](SearchLoyaltyAccountsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## searchLoyaltyEvents

> SearchLoyaltyEventsResponse searchLoyaltyEvents(searchLoyaltyEventsRequest)

SearchLoyaltyEvents

Searches for loyalty events.  A Square loyalty program maintains a ledger of events that occur during the lifetime of a  buyer&#39;s loyalty account. Each change in the point balance  (for example, points earned, points redeemed, and points expired) is  recorded in the ledger. Using this endpoint, you can search the ledger for events.  Search results are sorted by &#x60;created_at&#x60; in descending order.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.LoyaltyApi();
let searchLoyaltyEventsRequest = new SquareConnectApi.SearchLoyaltyEventsRequest(); // SearchLoyaltyEventsRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.searchLoyaltyEvents(searchLoyaltyEventsRequest, (error, data, response) => {
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
 **searchLoyaltyEventsRequest** | [**SearchLoyaltyEventsRequest**](SearchLoyaltyEventsRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**SearchLoyaltyEventsResponse**](SearchLoyaltyEventsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## searchLoyaltyRewards

> SearchLoyaltyRewardsResponse searchLoyaltyRewards(searchLoyaltyRewardsRequest)

SearchLoyaltyRewards

Searches for loyalty rewards in a loyalty account.   In the current implementation, the endpoint supports search by the reward &#x60;status&#x60;.  If you know a reward ID, use the  [RetrieveLoyaltyReward](https://developer.squareup.com/reference/square_2021-08-18/loyalty-api/retrieve-loyalty-reward) endpoint.  Search results are sorted by &#x60;updated_at&#x60; in descending order.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.LoyaltyApi();
let searchLoyaltyRewardsRequest = new SquareConnectApi.SearchLoyaltyRewardsRequest(); // SearchLoyaltyRewardsRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.searchLoyaltyRewards(searchLoyaltyRewardsRequest, (error, data, response) => {
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
 **searchLoyaltyRewardsRequest** | [**SearchLoyaltyRewardsRequest**](SearchLoyaltyRewardsRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**SearchLoyaltyRewardsResponse**](SearchLoyaltyRewardsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

