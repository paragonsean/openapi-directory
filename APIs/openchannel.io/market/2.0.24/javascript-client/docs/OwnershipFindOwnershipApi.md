# OpenChannelMarketApi.OwnershipFindOwnershipApi

All URIs are relative to *https://market.openchannel.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ownershipGet**](OwnershipFindOwnershipApi.md#ownershipGet) | **GET** /ownership | Returns a paginated list of app licenses
[**ownershipInstallPost**](OwnershipFindOwnershipApi.md#ownershipInstallPost) | **POST** /ownership/install | Aquires an app license for a user (installs app)
[**ownershipOwnershipIdGet**](OwnershipFindOwnershipApi.md#ownershipOwnershipIdGet) | **GET** /ownership/{ownershipId} | Returns an ownership record
[**ownershipOwnershipIdPatch**](OwnershipFindOwnershipApi.md#ownershipOwnershipIdPatch) | **PATCH** /ownership/{ownershipId} | Updates ownership fields
[**ownershipOwnershipIdPost**](OwnershipFindOwnershipApi.md#ownershipOwnershipIdPost) | **POST** /ownership/{ownershipId} | Updates an ownership record
[**ownershipUninstallOwnershipIdPost**](OwnershipFindOwnershipApi.md#ownershipUninstallOwnershipIdPost) | **POST** /ownership/uninstall/{ownershipId} | Uninstalls a license for a particular user and app (uninstalls app)



## ownershipGet

> OwnershipPages ownershipGet(opts)

Returns a paginated list of app licenses

 - Results are returned for the market provided within the basic authentication credentials 

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.OwnershipFindOwnershipApi();
let opts = {
  'query': "query_example", // String | A query document. Example: {'userId':'12'} matches all the ownership records that have the userId '12'.
  'sort': "sort_example", // String | A sort document. Example: {'date':1} sorts the results by date in ascending order
  'pageNumber': 56, // Number | The result set page number to be returned
  'limit': 56 // Number | The maximum number of results to return per page
};
apiInstance.ownershipGet(opts, (error, data, response) => {
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
 **query** | **String**| A query document. Example: {&#39;userId&#39;:&#39;12&#39;} matches all the ownership records that have the userId &#39;12&#39;. | [optional] 
 **sort** | **String**| A sort document. Example: {&#39;date&#39;:1} sorts the results by date in ascending order | [optional] 
 **pageNumber** | **Number**| The result set page number to be returned | [optional] 
 **limit** | **Number**| The maximum number of results to return per page | [optional] 

### Return type

[**OwnershipPages**](OwnershipPages.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## ownershipInstallPost

> Ownership ownershipInstallPost(appId, userId, opts)

Aquires an app license for a user (installs app)

 - This method is called on behalf of a user - This method requires either a modelId from the app or a custom model - User data and statistics are recorded when this method is called 

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.OwnershipFindOwnershipApi();
let appId = "appId_example"; // String | The id of the App being owned
let userId = "userId_example"; // String | The id of the User requesting to own the App
let opts = {
  'modelId': "modelId_example", // String | The id of the model associated with this ownership request
  'model': "model_example", // String | A custom model that will override the app's default model for this install
  'customData': "customData_example" // String | A custom JSON object to attach to this ownership record
};
apiInstance.ownershipInstallPost(appId, userId, opts, (error, data, response) => {
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
 **appId** | **String**| The id of the App being owned | 
 **userId** | **String**| The id of the User requesting to own the App | 
 **modelId** | **String**| The id of the model associated with this ownership request | [optional] 
 **model** | **String**| A custom model that will override the app&#39;s default model for this install | [optional] 
 **customData** | **String**| A custom JSON object to attach to this ownership record | [optional] 

### Return type

[**Ownership**](Ownership.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## ownershipOwnershipIdGet

> Ownership ownershipOwnershipIdGet(ownershipId)

Returns an ownership record

 - Results are returned for the market provided within the basic authentication credentials 

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.OwnershipFindOwnershipApi();
let ownershipId = "ownershipId_example"; // String | The id belonging to the ownership record
apiInstance.ownershipOwnershipIdGet(ownershipId, (error, data, response) => {
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
 **ownershipId** | **String**| The id belonging to the ownership record | 

### Return type

[**Ownership**](Ownership.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## ownershipOwnershipIdPatch

> Ownership ownershipOwnershipIdPatch(ownershipId, opts)

Updates ownership fields

 - Results are returned for the market provided within the basic authentication credentials 

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.OwnershipFindOwnershipApi();
let ownershipId = "ownershipId_example"; // String | The id of the ownership to be updated
let opts = {
  'customData': "customData_example", // String | Custom JSON object that will be attached to this ownership record
  'expires': 789 // Number | The date (in millis) of when this app ownership expires
};
apiInstance.ownershipOwnershipIdPatch(ownershipId, opts, (error, data, response) => {
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
 **ownershipId** | **String**| The id of the ownership to be updated | 
 **customData** | **String**| Custom JSON object that will be attached to this ownership record | [optional] 
 **expires** | **Number**| The date (in millis) of when this app ownership expires | [optional] 

### Return type

[**Ownership**](Ownership.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## ownershipOwnershipIdPost

> Ownership ownershipOwnershipIdPost(ownershipId, opts)

Updates an ownership record

 - Results are returned for the market provided within the basic authentication credentials 

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.OwnershipFindOwnershipApi();
let ownershipId = "ownershipId_example"; // String | The id of the ownership to be updated
let opts = {
  'customData': "customData_example", // String | Custom JSON object that will be attached to this ownership record
  'expires': 789 // Number | The date (in millis) of when this app ownership expires
};
apiInstance.ownershipOwnershipIdPost(ownershipId, opts, (error, data, response) => {
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
 **ownershipId** | **String**| The id of the ownership to be updated | 
 **customData** | **String**| Custom JSON object that will be attached to this ownership record | [optional] 
 **expires** | **Number**| The date (in millis) of when this app ownership expires | [optional] 

### Return type

[**Ownership**](Ownership.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## ownershipUninstallOwnershipIdPost

> Ownership ownershipUninstallOwnershipIdPost(ownershipId, userId, opts)

Uninstalls a license for a particular user and app (uninstalls app)

 - This method is called on behalf of a user - User data and statistics are recorded when this method is called 

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.OwnershipFindOwnershipApi();
let ownershipId = "ownershipId_example"; // String | The id of the ownership to be unintalled
let userId = "userId_example"; // String | The id of the User requesting to uninstall the App
let opts = {
  'cancelOwnership': true, // Boolean | True if this app will require payment to be re-installed. Default is false
  'customData': "customData_example" // String | A custom JSON object to attach to this ownership record
};
apiInstance.ownershipUninstallOwnershipIdPost(ownershipId, userId, opts, (error, data, response) => {
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
 **ownershipId** | **String**| The id of the ownership to be unintalled | 
 **userId** | **String**| The id of the User requesting to uninstall the App | 
 **cancelOwnership** | **Boolean**| True if this app will require payment to be re-installed. Default is false | [optional] 
 **customData** | **String**| A custom JSON object to attach to this ownership record | [optional] 

### Return type

[**Ownership**](Ownership.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

