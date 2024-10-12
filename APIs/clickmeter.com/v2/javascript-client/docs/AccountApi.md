# ClickMeterApi.AccountApi

All URIs are relative to *http://apiv2.clickmeter.com:80*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountDeleteDomainWhitelist**](AccountApi.md#accountDeleteDomainWhitelist) | **DELETE** /account/domainwhitelist/{whitelistId} | Delete an domain entry
[**accountDeleteGuest**](AccountApi.md#accountDeleteGuest) | **DELETE** /account/guests/{guestId} | Delete a guest
[**accountDeleteIpBlacklist**](AccountApi.md#accountDeleteIpBlacklist) | **DELETE** /account/ipblacklist/{blacklistId} | Delete an ip blacklist entry
[**accountGet**](AccountApi.md#accountGet) | **GET** /account | Retrieve current account data
[**accountGetDomainWhitelist**](AccountApi.md#accountGetDomainWhitelist) | **GET** /account/domainwhitelist | Retrieve list of a domains allowed to redirect in DDU mode
[**accountGetGuest**](AccountApi.md#accountGetGuest) | **GET** /account/guests/{guestId} | Retrieve a guest
[**accountGetGuests**](AccountApi.md#accountGetGuests) | **GET** /account/guests | Retrieve list of a guest
[**accountGetGuestsCount**](AccountApi.md#accountGetGuestsCount) | **GET** /account/guests/count | Retrieve count of guests
[**accountGetIpBlacklist**](AccountApi.md#accountGetIpBlacklist) | **GET** /account/ipblacklist | Retrieve list of a ip to exclude from event tracking
[**accountGetPermissions**](AccountApi.md#accountGetPermissions) | **GET** /account/guests/{guestId}/permissions | Retrieve permissions for a guest
[**accountGetPermissionsCount**](AccountApi.md#accountGetPermissionsCount) | **GET** /account/guests/{guestId}/permissions/count | Retrieve count of the permissions for a guest
[**accountGetPlan**](AccountApi.md#accountGetPlan) | **GET** /account/plan | Retrieve current account plan
[**accountGuestsGuestIdTypePermissionsPatchPost**](AccountApi.md#accountGuestsGuestIdTypePermissionsPatchPost) | **POST** /account/guests/{guestId}/{type}/permissions/patch | Change the permission on a shared object
[**accountPatchPermissions**](AccountApi.md#accountPatchPermissions) | **PUT** /account/guests/{guestId}/{type}/permissions/patch | Change the permission on a shared object
[**accountPost**](AccountApi.md#accountPost) | **POST** /account | Update current account data
[**accountPostGuest**](AccountApi.md#accountPostGuest) | **POST** /account/guests/{guestId} | Update a guest
[**accountPutDomainWhitelist**](AccountApi.md#accountPutDomainWhitelist) | **POST** /account/domainwhitelist | Create an domain entry
[**accountPutGuest**](AccountApi.md#accountPutGuest) | **POST** /account/guests | Create a guest
[**accountPutIpBlacklist**](AccountApi.md#accountPutIpBlacklist) | **POST** /account/ipblacklist | Create an ip blacklist entry



## accountDeleteDomainWhitelist

> ApiCoreDtoAccountingDomainWhitelistEntry accountDeleteDomainWhitelist(whitelistId)

Delete an domain entry

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.AccountApi();
let whitelistId = "whitelistId_example"; // String | The id of the domain to delete
apiInstance.accountDeleteDomainWhitelist(whitelistId, (error, data, response) => {
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
 **whitelistId** | **String**| The id of the domain to delete | 

### Return type

[**ApiCoreDtoAccountingDomainWhitelistEntry**](ApiCoreDtoAccountingDomainWhitelistEntry.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## accountDeleteGuest

> ApiCoreResponsesEntityUriSystemInt64 accountDeleteGuest(guestId)

Delete a guest

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.AccountApi();
let guestId = 789; // Number | Id of the guest
apiInstance.accountDeleteGuest(guestId, (error, data, response) => {
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
 **guestId** | **Number**| Id of the guest | 

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## accountDeleteIpBlacklist

> ApiCoreDtoAccountingIpBlacklistEntry accountDeleteIpBlacklist(blacklistId)

Delete an ip blacklist entry

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.AccountApi();
let blacklistId = "blacklistId_example"; // String | The id of the ip to delete
apiInstance.accountDeleteIpBlacklist(blacklistId, (error, data, response) => {
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
 **blacklistId** | **String**| The id of the ip to delete | 

### Return type

[**ApiCoreDtoAccountingIpBlacklistEntry**](ApiCoreDtoAccountingIpBlacklistEntry.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## accountGet

> ApiCoreDtoAccountingUser accountGet()

Retrieve current account data

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.AccountApi();
apiInstance.accountGet((error, data, response) => {
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

[**ApiCoreDtoAccountingUser**](ApiCoreDtoAccountingUser.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## accountGetDomainWhitelist

> ApiCoreResponsesEntitiesResponseApiCoreDtoAccountingDomainWhitelistEntry accountGetDomainWhitelist(opts)

Retrieve list of a domains allowed to redirect in DDU mode

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.AccountApi();
let opts = {
  'offset': 56, // Number | Offset where to start from
  'limit': 56 // Number | Limit results to this number
};
apiInstance.accountGetDomainWhitelist(opts, (error, data, response) => {
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
 **offset** | **Number**| Offset where to start from | [optional] 
 **limit** | **Number**| Limit results to this number | [optional] 

### Return type

[**ApiCoreResponsesEntitiesResponseApiCoreDtoAccountingDomainWhitelistEntry**](ApiCoreResponsesEntitiesResponseApiCoreDtoAccountingDomainWhitelistEntry.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## accountGetGuest

> ApiCoreDtoAccountingGuest accountGetGuest(guestId)

Retrieve a guest

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.AccountApi();
let guestId = 789; // Number | Id of the guest
apiInstance.accountGetGuest(guestId, (error, data, response) => {
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
 **guestId** | **Number**| Id of the guest | 

### Return type

[**ApiCoreDtoAccountingGuest**](ApiCoreDtoAccountingGuest.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## accountGetGuests

> ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64 accountGetGuests(opts)

Retrieve list of a guest

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.AccountApi();
let opts = {
  'offset': 56, // Number | Offset where to start from
  'limit': 56, // Number | Limit results to this number
  'sortBy': "sortBy_example", // String | Field to sort by
  'sortDirection': "sortDirection_example", // String | Direction of sort \"asc\" or \"desc\"
  'textSearch': "textSearch_example" // String | Filter fields by this pattern
};
apiInstance.accountGetGuests(opts, (error, data, response) => {
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
 **offset** | **Number**| Offset where to start from | [optional] 
 **limit** | **Number**| Limit results to this number | [optional] 
 **sortBy** | **String**| Field to sort by | [optional] 
 **sortDirection** | **String**| Direction of sort \&quot;asc\&quot; or \&quot;desc\&quot; | [optional] 
 **textSearch** | **String**| Filter fields by this pattern | [optional] 

### Return type

[**ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## accountGetGuestsCount

> ApiCoreResponsesCountResponce accountGetGuestsCount(opts)

Retrieve count of guests

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.AccountApi();
let opts = {
  'textSearch': "textSearch_example" // String | Filter fields by this pattern
};
apiInstance.accountGetGuestsCount(opts, (error, data, response) => {
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
 **textSearch** | **String**| Filter fields by this pattern | [optional] 

### Return type

[**ApiCoreResponsesCountResponce**](ApiCoreResponsesCountResponce.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## accountGetIpBlacklist

> ApiCoreResponsesEntitiesResponseApiCoreDtoAccountingIpBlacklistEntry accountGetIpBlacklist(opts)

Retrieve list of a ip to exclude from event tracking

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.AccountApi();
let opts = {
  'offset': 56, // Number | Offset where to start from
  'limit': 56 // Number | Limit results to this number
};
apiInstance.accountGetIpBlacklist(opts, (error, data, response) => {
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
 **offset** | **Number**| Offset where to start from | [optional] 
 **limit** | **Number**| Limit results to this number | [optional] 

### Return type

[**ApiCoreResponsesEntitiesResponseApiCoreDtoAccountingIpBlacklistEntry**](ApiCoreResponsesEntitiesResponseApiCoreDtoAccountingIpBlacklistEntry.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## accountGetPermissions

> ApiCoreResponsesEntitiesResponseApiCoreDtoGrantsGrant accountGetPermissions(guestId, opts)

Retrieve permissions for a guest

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.AccountApi();
let guestId = 789; // Number | Id of the guest
let opts = {
  'entityType': "entityType_example", // String | Can be \"datapoint\" or \"group\"
  'offset': 56, // Number | Offset where to start from
  'limit': 56, // Number | Limit results to this number
  'type': "type_example", // String | Can be \"w\" or \"r\"
  'entityId': 789 // Number | Optional id of the datapoint/group entity to filter by
};
apiInstance.accountGetPermissions(guestId, opts, (error, data, response) => {
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
 **guestId** | **Number**| Id of the guest | 
 **entityType** | **String**| Can be \&quot;datapoint\&quot; or \&quot;group\&quot; | [optional] 
 **offset** | **Number**| Offset where to start from | [optional] 
 **limit** | **Number**| Limit results to this number | [optional] 
 **type** | **String**| Can be \&quot;w\&quot; or \&quot;r\&quot; | [optional] 
 **entityId** | **Number**| Optional id of the datapoint/group entity to filter by | [optional] 

### Return type

[**ApiCoreResponsesEntitiesResponseApiCoreDtoGrantsGrant**](ApiCoreResponsesEntitiesResponseApiCoreDtoGrantsGrant.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## accountGetPermissionsCount

> ApiCoreResponsesCountResponce accountGetPermissionsCount(guestId, opts)

Retrieve count of the permissions for a guest

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.AccountApi();
let guestId = 789; // Number | Id of the guest
let opts = {
  'entityType': "entityType_example", // String | Can be \"datapoint\" or \"group\"
  'type': "type_example", // String | Can be \"w\" or \"r\"
  'entityId': 789 // Number | Optional id of the datapoint/group entity to filter by
};
apiInstance.accountGetPermissionsCount(guestId, opts, (error, data, response) => {
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
 **guestId** | **Number**| Id of the guest | 
 **entityType** | **String**| Can be \&quot;datapoint\&quot; or \&quot;group\&quot; | [optional] 
 **type** | **String**| Can be \&quot;w\&quot; or \&quot;r\&quot; | [optional] 
 **entityId** | **Number**| Optional id of the datapoint/group entity to filter by | [optional] 

### Return type

[**ApiCoreResponsesCountResponce**](ApiCoreResponsesCountResponce.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## accountGetPlan

> ApiCoreDtoAccountingPlan accountGetPlan()

Retrieve current account plan

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.AccountApi();
apiInstance.accountGetPlan((error, data, response) => {
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

[**ApiCoreDtoAccountingPlan**](ApiCoreDtoAccountingPlan.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## accountGuestsGuestIdTypePermissionsPatchPost

> ApiCoreResponsesEntityUriSystemInt64 accountGuestsGuestIdTypePermissionsPatchPost(guestId, type, apiCoreRequestsPermissionPatchRequest)

Change the permission on a shared object

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.AccountApi();
let guestId = 789; // Number | Id of the guest
let type = "type_example"; // String | Can be \"datapoint\" or \"group\"
let apiCoreRequestsPermissionPatchRequest = new ClickMeterApi.ApiCoreRequestsPermissionPatchRequest(); // ApiCoreRequestsPermissionPatchRequest | The patch permission request
apiInstance.accountGuestsGuestIdTypePermissionsPatchPost(guestId, type, apiCoreRequestsPermissionPatchRequest, (error, data, response) => {
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
 **guestId** | **Number**| Id of the guest | 
 **type** | **String**| Can be \&quot;datapoint\&quot; or \&quot;group\&quot; | 
 **apiCoreRequestsPermissionPatchRequest** | [**ApiCoreRequestsPermissionPatchRequest**](ApiCoreRequestsPermissionPatchRequest.md)| The patch permission request | 

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## accountPatchPermissions

> ApiCoreResponsesEntityUriSystemInt64 accountPatchPermissions(guestId, type, apiCoreRequestsPermissionPatchRequest)

Change the permission on a shared object

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.AccountApi();
let guestId = 789; // Number | Id of the guest
let type = "type_example"; // String | Can be \"datapoint\" or \"group\"
let apiCoreRequestsPermissionPatchRequest = new ClickMeterApi.ApiCoreRequestsPermissionPatchRequest(); // ApiCoreRequestsPermissionPatchRequest | The patch permission request
apiInstance.accountPatchPermissions(guestId, type, apiCoreRequestsPermissionPatchRequest, (error, data, response) => {
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
 **guestId** | **Number**| Id of the guest | 
 **type** | **String**| Can be \&quot;datapoint\&quot; or \&quot;group\&quot; | 
 **apiCoreRequestsPermissionPatchRequest** | [**ApiCoreRequestsPermissionPatchRequest**](ApiCoreRequestsPermissionPatchRequest.md)| The patch permission request | 

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## accountPost

> ApiCoreDtoAccountingUser accountPost(apiCoreDtoAccountingUser)

Update current account data

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.AccountApi();
let apiCoreDtoAccountingUser = new ClickMeterApi.ApiCoreDtoAccountingUser(); // ApiCoreDtoAccountingUser | 
apiInstance.accountPost(apiCoreDtoAccountingUser, (error, data, response) => {
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
 **apiCoreDtoAccountingUser** | [**ApiCoreDtoAccountingUser**](ApiCoreDtoAccountingUser.md)|  | 

### Return type

[**ApiCoreDtoAccountingUser**](ApiCoreDtoAccountingUser.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## accountPostGuest

> ApiCoreDtoAccountingGuest accountPostGuest(guestId, apiCoreDtoAccountingGuest)

Update a guest

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.AccountApi();
let guestId = 789; // Number | Id of the guest
let apiCoreDtoAccountingGuest = new ClickMeterApi.ApiCoreDtoAccountingGuest(); // ApiCoreDtoAccountingGuest | Guest object with field updated
apiInstance.accountPostGuest(guestId, apiCoreDtoAccountingGuest, (error, data, response) => {
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
 **guestId** | **Number**| Id of the guest | 
 **apiCoreDtoAccountingGuest** | [**ApiCoreDtoAccountingGuest**](ApiCoreDtoAccountingGuest.md)| Guest object with field updated | 

### Return type

[**ApiCoreDtoAccountingGuest**](ApiCoreDtoAccountingGuest.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## accountPutDomainWhitelist

> ApiCoreDtoAccountingDomainWhitelistEntry accountPutDomainWhitelist(apiCoreDtoAccountingDomainWhitelistEntry)

Create an domain entry

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.AccountApi();
let apiCoreDtoAccountingDomainWhitelistEntry = new ClickMeterApi.ApiCoreDtoAccountingDomainWhitelistEntry(); // ApiCoreDtoAccountingDomainWhitelistEntry | The entry to add
apiInstance.accountPutDomainWhitelist(apiCoreDtoAccountingDomainWhitelistEntry, (error, data, response) => {
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
 **apiCoreDtoAccountingDomainWhitelistEntry** | [**ApiCoreDtoAccountingDomainWhitelistEntry**](ApiCoreDtoAccountingDomainWhitelistEntry.md)| The entry to add | 

### Return type

[**ApiCoreDtoAccountingDomainWhitelistEntry**](ApiCoreDtoAccountingDomainWhitelistEntry.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## accountPutGuest

> ApiCoreDtoAccountingGuest accountPutGuest(apiCoreDtoAccountingGuest)

Create a guest

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.AccountApi();
let apiCoreDtoAccountingGuest = new ClickMeterApi.ApiCoreDtoAccountingGuest(); // ApiCoreDtoAccountingGuest | Guest object to create
apiInstance.accountPutGuest(apiCoreDtoAccountingGuest, (error, data, response) => {
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
 **apiCoreDtoAccountingGuest** | [**ApiCoreDtoAccountingGuest**](ApiCoreDtoAccountingGuest.md)| Guest object to create | 

### Return type

[**ApiCoreDtoAccountingGuest**](ApiCoreDtoAccountingGuest.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## accountPutIpBlacklist

> ApiCoreDtoAccountingIpBlacklistEntry accountPutIpBlacklist(apiCoreDtoAccountingIpBlacklistEntry)

Create an ip blacklist entry

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.AccountApi();
let apiCoreDtoAccountingIpBlacklistEntry = new ClickMeterApi.ApiCoreDtoAccountingIpBlacklistEntry(); // ApiCoreDtoAccountingIpBlacklistEntry | The entry to add
apiInstance.accountPutIpBlacklist(apiCoreDtoAccountingIpBlacklistEntry, (error, data, response) => {
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
 **apiCoreDtoAccountingIpBlacklistEntry** | [**ApiCoreDtoAccountingIpBlacklistEntry**](ApiCoreDtoAccountingIpBlacklistEntry.md)| The entry to add | 

### Return type

[**ApiCoreDtoAccountingIpBlacklistEntry**](ApiCoreDtoAccountingIpBlacklistEntry.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml

