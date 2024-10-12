# AdSenseHostApi.AccountsApi

All URIs are relative to *https://www.googleapis.com/adsensehost/v4.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adsensehostAccountsAdclientsGet**](AccountsApi.md#adsensehostAccountsAdclientsGet) | **GET** /accounts/{accountId}/adclients/{adClientId} | 
[**adsensehostAccountsAdclientsList**](AccountsApi.md#adsensehostAccountsAdclientsList) | **GET** /accounts/{accountId}/adclients | 
[**adsensehostAccountsAdunitsDelete**](AccountsApi.md#adsensehostAccountsAdunitsDelete) | **DELETE** /accounts/{accountId}/adclients/{adClientId}/adunits/{adUnitId} | 
[**adsensehostAccountsAdunitsGet**](AccountsApi.md#adsensehostAccountsAdunitsGet) | **GET** /accounts/{accountId}/adclients/{adClientId}/adunits/{adUnitId} | 
[**adsensehostAccountsAdunitsGetAdCode**](AccountsApi.md#adsensehostAccountsAdunitsGetAdCode) | **GET** /accounts/{accountId}/adclients/{adClientId}/adunits/{adUnitId}/adcode | 
[**adsensehostAccountsAdunitsInsert**](AccountsApi.md#adsensehostAccountsAdunitsInsert) | **POST** /accounts/{accountId}/adclients/{adClientId}/adunits | 
[**adsensehostAccountsAdunitsList**](AccountsApi.md#adsensehostAccountsAdunitsList) | **GET** /accounts/{accountId}/adclients/{adClientId}/adunits | 
[**adsensehostAccountsAdunitsPatch**](AccountsApi.md#adsensehostAccountsAdunitsPatch) | **PATCH** /accounts/{accountId}/adclients/{adClientId}/adunits | 
[**adsensehostAccountsAdunitsUpdate**](AccountsApi.md#adsensehostAccountsAdunitsUpdate) | **PUT** /accounts/{accountId}/adclients/{adClientId}/adunits | 
[**adsensehostAccountsGet**](AccountsApi.md#adsensehostAccountsGet) | **GET** /accounts/{accountId} | 
[**adsensehostAccountsList**](AccountsApi.md#adsensehostAccountsList) | **GET** /accounts | 
[**adsensehostAccountsReportsGenerate**](AccountsApi.md#adsensehostAccountsReportsGenerate) | **GET** /accounts/{accountId}/reports | 



## adsensehostAccountsAdclientsGet

> AdClient adsensehostAccountsAdclientsGet(accountId, adClientId, opts)



Get information about one of the ad clients in the specified publisher&#39;s AdSense account.

### Example

```javascript
import AdSenseHostApi from 'ad_sense_host_api';
let defaultClient = AdSenseHostApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdSenseHostApi.AccountsApi();
let accountId = "accountId_example"; // String | Account which contains the ad client.
let adClientId = "adClientId_example"; // String | Ad client to get.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.adsensehostAccountsAdclientsGet(accountId, adClientId, opts, (error, data, response) => {
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
 **accountId** | **String**| Account which contains the ad client. | 
 **adClientId** | **String**| Ad client to get. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

[**AdClient**](AdClient.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## adsensehostAccountsAdclientsList

> AdClients adsensehostAccountsAdclientsList(accountId, opts)



List all hosted ad clients in the specified hosted account.

### Example

```javascript
import AdSenseHostApi from 'ad_sense_host_api';
let defaultClient = AdSenseHostApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdSenseHostApi.AccountsApi();
let accountId = "accountId_example"; // String | Account for which to list ad clients.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'maxResults': 56, // Number | The maximum number of ad clients to include in the response, used for paging.
  'pageToken': "pageToken_example" // String | A continuation token, used to page through ad clients. To retrieve the next page, set this parameter to the value of \"nextPageToken\" from the previous response.
};
apiInstance.adsensehostAccountsAdclientsList(accountId, opts, (error, data, response) => {
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
 **accountId** | **String**| Account for which to list ad clients. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **maxResults** | **Number**| The maximum number of ad clients to include in the response, used for paging. | [optional] 
 **pageToken** | **String**| A continuation token, used to page through ad clients. To retrieve the next page, set this parameter to the value of \&quot;nextPageToken\&quot; from the previous response. | [optional] 

### Return type

[**AdClients**](AdClients.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## adsensehostAccountsAdunitsDelete

> AdUnit adsensehostAccountsAdunitsDelete(accountId, adClientId, adUnitId, opts)



Delete the specified ad unit from the specified publisher AdSense account.

### Example

```javascript
import AdSenseHostApi from 'ad_sense_host_api';
let defaultClient = AdSenseHostApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdSenseHostApi.AccountsApi();
let accountId = "accountId_example"; // String | Account which contains the ad unit.
let adClientId = "adClientId_example"; // String | Ad client for which to get ad unit.
let adUnitId = "adUnitId_example"; // String | Ad unit to delete.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.adsensehostAccountsAdunitsDelete(accountId, adClientId, adUnitId, opts, (error, data, response) => {
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
 **accountId** | **String**| Account which contains the ad unit. | 
 **adClientId** | **String**| Ad client for which to get ad unit. | 
 **adUnitId** | **String**| Ad unit to delete. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

[**AdUnit**](AdUnit.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## adsensehostAccountsAdunitsGet

> AdUnit adsensehostAccountsAdunitsGet(accountId, adClientId, adUnitId, opts)



Get the specified host ad unit in this AdSense account.

### Example

```javascript
import AdSenseHostApi from 'ad_sense_host_api';
let defaultClient = AdSenseHostApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdSenseHostApi.AccountsApi();
let accountId = "accountId_example"; // String | Account which contains the ad unit.
let adClientId = "adClientId_example"; // String | Ad client for which to get ad unit.
let adUnitId = "adUnitId_example"; // String | Ad unit to get.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.adsensehostAccountsAdunitsGet(accountId, adClientId, adUnitId, opts, (error, data, response) => {
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
 **accountId** | **String**| Account which contains the ad unit. | 
 **adClientId** | **String**| Ad client for which to get ad unit. | 
 **adUnitId** | **String**| Ad unit to get. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

[**AdUnit**](AdUnit.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## adsensehostAccountsAdunitsGetAdCode

> AdCode adsensehostAccountsAdunitsGetAdCode(accountId, adClientId, adUnitId, opts)



Get ad code for the specified ad unit, attaching the specified host custom channels.

### Example

```javascript
import AdSenseHostApi from 'ad_sense_host_api';
let defaultClient = AdSenseHostApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdSenseHostApi.AccountsApi();
let accountId = "accountId_example"; // String | Account which contains the ad client.
let adClientId = "adClientId_example"; // String | Ad client with contains the ad unit.
let adUnitId = "adUnitId_example"; // String | Ad unit to get the code for.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'hostCustomChannelId': ["null"] // [String] | Host custom channel to attach to the ad code.
};
apiInstance.adsensehostAccountsAdunitsGetAdCode(accountId, adClientId, adUnitId, opts, (error, data, response) => {
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
 **accountId** | **String**| Account which contains the ad client. | 
 **adClientId** | **String**| Ad client with contains the ad unit. | 
 **adUnitId** | **String**| Ad unit to get the code for. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **hostCustomChannelId** | [**[String]**](String.md)| Host custom channel to attach to the ad code. | [optional] 

### Return type

[**AdCode**](AdCode.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## adsensehostAccountsAdunitsInsert

> AdUnit adsensehostAccountsAdunitsInsert(accountId, adClientId, opts)



Insert the supplied ad unit into the specified publisher AdSense account.

### Example

```javascript
import AdSenseHostApi from 'ad_sense_host_api';
let defaultClient = AdSenseHostApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdSenseHostApi.AccountsApi();
let accountId = "accountId_example"; // String | Account which will contain the ad unit.
let adClientId = "adClientId_example"; // String | Ad client into which to insert the ad unit.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'adUnit': new AdSenseHostApi.AdUnit() // AdUnit | 
};
apiInstance.adsensehostAccountsAdunitsInsert(accountId, adClientId, opts, (error, data, response) => {
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
 **accountId** | **String**| Account which will contain the ad unit. | 
 **adClientId** | **String**| Ad client into which to insert the ad unit. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **adUnit** | [**AdUnit**](AdUnit.md)|  | [optional] 

### Return type

[**AdUnit**](AdUnit.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## adsensehostAccountsAdunitsList

> AdUnits adsensehostAccountsAdunitsList(accountId, adClientId, opts)



List all ad units in the specified publisher&#39;s AdSense account.

### Example

```javascript
import AdSenseHostApi from 'ad_sense_host_api';
let defaultClient = AdSenseHostApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdSenseHostApi.AccountsApi();
let accountId = "accountId_example"; // String | Account which contains the ad client.
let adClientId = "adClientId_example"; // String | Ad client for which to list ad units.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'includeInactive': true, // Boolean | Whether to include inactive ad units. Default: true.
  'maxResults': 56, // Number | The maximum number of ad units to include in the response, used for paging.
  'pageToken': "pageToken_example" // String | A continuation token, used to page through ad units. To retrieve the next page, set this parameter to the value of \"nextPageToken\" from the previous response.
};
apiInstance.adsensehostAccountsAdunitsList(accountId, adClientId, opts, (error, data, response) => {
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
 **accountId** | **String**| Account which contains the ad client. | 
 **adClientId** | **String**| Ad client for which to list ad units. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **includeInactive** | **Boolean**| Whether to include inactive ad units. Default: true. | [optional] 
 **maxResults** | **Number**| The maximum number of ad units to include in the response, used for paging. | [optional] 
 **pageToken** | **String**| A continuation token, used to page through ad units. To retrieve the next page, set this parameter to the value of \&quot;nextPageToken\&quot; from the previous response. | [optional] 

### Return type

[**AdUnits**](AdUnits.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## adsensehostAccountsAdunitsPatch

> AdUnit adsensehostAccountsAdunitsPatch(accountId, adClientId, adUnitId, opts)



Update the supplied ad unit in the specified publisher AdSense account. This method supports patch semantics.

### Example

```javascript
import AdSenseHostApi from 'ad_sense_host_api';
let defaultClient = AdSenseHostApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdSenseHostApi.AccountsApi();
let accountId = "accountId_example"; // String | Account which contains the ad client.
let adClientId = "adClientId_example"; // String | Ad client which contains the ad unit.
let adUnitId = "adUnitId_example"; // String | Ad unit to get.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'adUnit': new AdSenseHostApi.AdUnit() // AdUnit | 
};
apiInstance.adsensehostAccountsAdunitsPatch(accountId, adClientId, adUnitId, opts, (error, data, response) => {
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
 **accountId** | **String**| Account which contains the ad client. | 
 **adClientId** | **String**| Ad client which contains the ad unit. | 
 **adUnitId** | **String**| Ad unit to get. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **adUnit** | [**AdUnit**](AdUnit.md)|  | [optional] 

### Return type

[**AdUnit**](AdUnit.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## adsensehostAccountsAdunitsUpdate

> AdUnit adsensehostAccountsAdunitsUpdate(accountId, adClientId, opts)



Update the supplied ad unit in the specified publisher AdSense account.

### Example

```javascript
import AdSenseHostApi from 'ad_sense_host_api';
let defaultClient = AdSenseHostApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdSenseHostApi.AccountsApi();
let accountId = "accountId_example"; // String | Account which contains the ad client.
let adClientId = "adClientId_example"; // String | Ad client which contains the ad unit.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'adUnit': new AdSenseHostApi.AdUnit() // AdUnit | 
};
apiInstance.adsensehostAccountsAdunitsUpdate(accountId, adClientId, opts, (error, data, response) => {
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
 **accountId** | **String**| Account which contains the ad client. | 
 **adClientId** | **String**| Ad client which contains the ad unit. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **adUnit** | [**AdUnit**](AdUnit.md)|  | [optional] 

### Return type

[**AdUnit**](AdUnit.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## adsensehostAccountsGet

> Account adsensehostAccountsGet(accountId, opts)



Get information about the selected associated AdSense account.

### Example

```javascript
import AdSenseHostApi from 'ad_sense_host_api';
let defaultClient = AdSenseHostApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdSenseHostApi.AccountsApi();
let accountId = "accountId_example"; // String | Account to get information about.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.adsensehostAccountsGet(accountId, opts, (error, data, response) => {
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
 **accountId** | **String**| Account to get information about. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

[**Account**](Account.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## adsensehostAccountsList

> Accounts adsensehostAccountsList(filterAdClientId, opts)



List hosted accounts associated with this AdSense account by ad client id.

### Example

```javascript
import AdSenseHostApi from 'ad_sense_host_api';
let defaultClient = AdSenseHostApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdSenseHostApi.AccountsApi();
let filterAdClientId = ["null"]; // [String] | Ad clients to list accounts for.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.adsensehostAccountsList(filterAdClientId, opts, (error, data, response) => {
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
 **filterAdClientId** | [**[String]**](String.md)| Ad clients to list accounts for. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

[**Accounts**](Accounts.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## adsensehostAccountsReportsGenerate

> Report adsensehostAccountsReportsGenerate(accountId, startDate, endDate, opts)



Generate an AdSense report based on the report request sent in the query parameters. Returns the result as JSON; to retrieve output in CSV format specify \&quot;alt&#x3D;csv\&quot; as a query parameter.

### Example

```javascript
import AdSenseHostApi from 'ad_sense_host_api';
let defaultClient = AdSenseHostApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdSenseHostApi.AccountsApi();
let accountId = "accountId_example"; // String | Hosted account upon which to report.
let startDate = "startDate_example"; // String | Start of the date range to report on in \"YYYY-MM-DD\" format, inclusive.
let endDate = "endDate_example"; // String | End of the date range to report on in \"YYYY-MM-DD\" format, inclusive.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'dimension': ["null"], // [String] | Dimensions to base the report on.
  'filter': ["null"], // [String] | Filters to be run on the report.
  'locale': "locale_example", // String | Optional locale to use for translating report output to a local language. Defaults to \"en_US\" if not specified.
  'maxResults': 56, // Number | The maximum number of rows of report data to return.
  'metric': ["null"], // [String] | Numeric columns to include in the report.
  'sort': ["null"], // [String] | The name of a dimension or metric to sort the resulting report on, optionally prefixed with \"+\" to sort ascending or \"-\" to sort descending. If no prefix is specified, the column is sorted ascending.
  'startIndex': 56 // Number | Index of the first row of report data to return.
};
apiInstance.adsensehostAccountsReportsGenerate(accountId, startDate, endDate, opts, (error, data, response) => {
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
 **accountId** | **String**| Hosted account upon which to report. | 
 **startDate** | **String**| Start of the date range to report on in \&quot;YYYY-MM-DD\&quot; format, inclusive. | 
 **endDate** | **String**| End of the date range to report on in \&quot;YYYY-MM-DD\&quot; format, inclusive. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **dimension** | [**[String]**](String.md)| Dimensions to base the report on. | [optional] 
 **filter** | [**[String]**](String.md)| Filters to be run on the report. | [optional] 
 **locale** | **String**| Optional locale to use for translating report output to a local language. Defaults to \&quot;en_US\&quot; if not specified. | [optional] 
 **maxResults** | **Number**| The maximum number of rows of report data to return. | [optional] 
 **metric** | [**[String]**](String.md)| Numeric columns to include in the report. | [optional] 
 **sort** | [**[String]**](String.md)| The name of a dimension or metric to sort the resulting report on, optionally prefixed with \&quot;+\&quot; to sort ascending or \&quot;-\&quot; to sort descending. If no prefix is specified, the column is sorted ascending. | [optional] 
 **startIndex** | **Number**| Index of the first row of report data to return. | [optional] 

### Return type

[**Report**](Report.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

