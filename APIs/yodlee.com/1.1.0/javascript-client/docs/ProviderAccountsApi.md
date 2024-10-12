# YodleeCoreApis.ProviderAccountsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteProviderAccount**](ProviderAccountsApi.md#deleteProviderAccount) | **DELETE** /providerAccounts/{providerAccountId} | Delete Provider Account
[**editCredentialsOrRefreshProviderAccount**](ProviderAccountsApi.md#editCredentialsOrRefreshProviderAccount) | **PUT** /providerAccounts | Update Account
[**getAllProviderAccounts**](ProviderAccountsApi.md#getAllProviderAccounts) | **GET** /providerAccounts | Get Provider Accounts
[**getProviderAccount**](ProviderAccountsApi.md#getProviderAccount) | **GET** /providerAccounts/{providerAccountId} | Get Provider Account Details
[**getProviderAccountProfiles**](ProviderAccountsApi.md#getProviderAccountProfiles) | **GET** /providerAccounts/profile | Get User Profile Details
[**updatePreferences**](ProviderAccountsApi.md#updatePreferences) | **PUT** /providerAccounts/{providerAccountId}/preferences | Update Preferences



## deleteProviderAccount

> deleteProviderAccount(providerAccountId)

Delete Provider Account

The delete provider account service is used to delete a provider account from the Yodlee system. This service also deletes the accounts that are created in the Yodlee system for that provider account. &lt;br&gt;This service does not return a response. The HTTP response code is 204 (Success with no content).&lt;br&gt;

### Example

```javascript
import YodleeCoreApis from 'yodlee_core_apis';

let apiInstance = new YodleeCoreApis.ProviderAccountsApi();
let providerAccountId = 789; // Number | providerAccountId
apiInstance.deleteProviderAccount(providerAccountId, (error, data, response) => {
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
 **providerAccountId** | **Number**| providerAccountId | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## editCredentialsOrRefreshProviderAccount

> UpdatedProviderAccountResponse editCredentialsOrRefreshProviderAccount(providerAccountIds, opts)

Update Account

The update account API is used to:&lt;br&gt; &lt;ul&gt;&lt;li&gt;Retrieve the latest information for accounts that belong to one providerAccount from the provider site. You must allow at least 15 min between requests.&lt;li&gt;Retrieve the latest information of all the eligible accounts that belong to the user.&lt;li&gt;Data to be retrieved from the provider site can be overridden using datasetName or dataset. If you do pass datasetName, all the datasets that are implicitly configured for the dataset will be retrieved. This action is allowed for single provider account refresh flows only.&lt;li&gt;Check the status of the providerAccount before invoking this API. Do not call this API to trigger any action on a providerAccount when an action is already in progress for the providerAccount.&lt;li&gt;If the customer has subscribed to the REFRESH event notification and invoked this API, relevant notifications will be sent to the customer.&lt;li&gt;A dataset may depend on another dataset for retrieval, so the response will include the requested and dependent datasets.&lt;li&gt;Check all the dataset additional statuses returned in the response because the provider account status is drawn from the dataset additional statuses.&lt;li&gt;Updating preferences using this API will trigger refreshes.&lt;li&gt; The content type has to be passed as application/json for the body parameter.&lt;/ul&gt;&lt;br&gt;-----------------------------------------------------------------------------------------------------------------------------------------&lt;br&gt;&lt;br&gt;&lt;b&gt;Update All Eligible Accounts - Notes:&lt;/b&gt;&lt;br&gt;&lt;ul&gt;&lt;li&gt;This API will trigger a refresh for all the eligible provider accounts(both OB and credential-based accounts).&lt;li&gt;This API will not refresh closed, inactive, or UAR accounts, or accounts with refreshes in-progress or recently refreshed non-OB accounts.&lt;li&gt;No parameters should be passed to this API to trigger this action.&lt;li&gt;Do not call this API often. Our recommendation is to call this only at the time the user logs in to your app because it can hamper other API calls performance.&lt;li&gt;The response only contains information for accounts that were refreshed. If no accounts are eligible for refresh, no response is returned.&lt;/ul&gt;

### Example

```javascript
import YodleeCoreApis from 'yodlee_core_apis';

let apiInstance = new YodleeCoreApis.ProviderAccountsApi();
let providerAccountIds = "providerAccountIds_example"; // String | comma separated providerAccountIds
let opts = {
  'providerAccountRequest': new YodleeCoreApis.ProviderAccountRequest() // ProviderAccountRequest | loginForm or field entity
};
apiInstance.editCredentialsOrRefreshProviderAccount(providerAccountIds, opts, (error, data, response) => {
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
 **providerAccountIds** | **String**| comma separated providerAccountIds | 
 **providerAccountRequest** | [**ProviderAccountRequest**](ProviderAccountRequest.md)| loginForm or field entity | [optional] 

### Return type

[**UpdatedProviderAccountResponse**](UpdatedProviderAccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json;charset=UTF-8


## getAllProviderAccounts

> ProviderAccountResponse getAllProviderAccounts(opts)

Get Provider Accounts

The get provider accounts service is used to return all the provider accounts added by the user. &lt;br&gt;This includes the failed and successfully added provider accounts.&lt;br&gt;

### Example

```javascript
import YodleeCoreApis from 'yodlee_core_apis';

let apiInstance = new YodleeCoreApis.ProviderAccountsApi();
let opts = {
  'include': "include_example", // String | include
  'providerIds': "providerIds_example" // String | Comma separated providerIds.
};
apiInstance.getAllProviderAccounts(opts, (error, data, response) => {
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
 **include** | **String**| include | [optional] 
 **providerIds** | **String**| Comma separated providerIds. | [optional] 

### Return type

[**ProviderAccountResponse**](ProviderAccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getProviderAccount

> ProviderAccountDetailResponse getProviderAccount(providerAccountId, opts)

Get Provider Account Details

The get provider account details service is used to learn the status of adding accounts and updating accounts.&lt;br&gt;This service has to be called continuously to know the progress level of the triggered process. This service also provides the MFA information requested by the provider site.&lt;br&gt;When &lt;i&gt;include &#x3D; credentials&lt;/i&gt;, questions is passed as input, the service returns the credentials (non-password values) and questions stored in the Yodlee system for that provider account. &lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt; &lt;li&gt;The password and answer fields are not returned in the response.&lt;/li&gt;

### Example

```javascript
import YodleeCoreApis from 'yodlee_core_apis';

let apiInstance = new YodleeCoreApis.ProviderAccountsApi();
let providerAccountId = 789; // Number | providerAccountId
let opts = {
  'include': "include_example", // String | include credentials,questions
  'requestId': "requestId_example" // String | The unique identifier for the request that returns contextual data
};
apiInstance.getProviderAccount(providerAccountId, opts, (error, data, response) => {
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
 **providerAccountId** | **Number**| providerAccountId | 
 **include** | **String**| include credentials,questions | [optional] 
 **requestId** | **String**| The unique identifier for the request that returns contextual data | [optional] 

### Return type

[**ProviderAccountDetailResponse**](ProviderAccountDetailResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getProviderAccountProfiles

> ProviderAccountUserProfileResponse getProviderAccountProfiles(opts)

Get User Profile Details

The get provider accounts profile service is used to return the user profile details that are associated to the provider account. &lt;br&gt;

### Example

```javascript
import YodleeCoreApis from 'yodlee_core_apis';

let apiInstance = new YodleeCoreApis.ProviderAccountsApi();
let opts = {
  'providerAccountId': "providerAccountId_example" // String | Comma separated providerAccountIds.
};
apiInstance.getProviderAccountProfiles(opts, (error, data, response) => {
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
 **providerAccountId** | **String**| Comma separated providerAccountIds. | [optional] 

### Return type

[**ProviderAccountUserProfileResponse**](ProviderAccountUserProfileResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## updatePreferences

> updatePreferences(providerAccountId, providerAccountPreferencesRequest)

Update Preferences

This endpoint is used to update preferences like data extracts and auto refreshes without triggering refresh for the providerAccount.&lt;br&gt;Setting isDataExtractsEnabled to false will not trigger data extracts notification and dataExtracts/events will not reflect any data change that is happening for the providerAccount.&lt;br&gt;Modified data will not be provided in the dataExtracts/userData endpoint.&lt;br&gt;Setting isAutoRefreshEnabled to false will not trigger auto refreshes for the provider account.&lt;br&gt;

### Example

```javascript
import YodleeCoreApis from 'yodlee_core_apis';

let apiInstance = new YodleeCoreApis.ProviderAccountsApi();
let providerAccountId = 789; // Number | providerAccountId
let providerAccountPreferencesRequest = new YodleeCoreApis.ProviderAccountPreferencesRequest(); // ProviderAccountPreferencesRequest | preferences
apiInstance.updatePreferences(providerAccountId, providerAccountPreferencesRequest, (error, data, response) => {
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
 **providerAccountId** | **Number**| providerAccountId | 
 **providerAccountPreferencesRequest** | [**ProviderAccountPreferencesRequest**](ProviderAccountPreferencesRequest.md)| preferences | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json;charset=UTF-8

