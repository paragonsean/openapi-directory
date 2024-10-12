# OpenChannelMarketApi.AppsFindAndModifyAppsApi

All URIs are relative to *https://market.openchannel.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appsAppIdDelete**](AppsFindAndModifyAppsApi.md#appsAppIdDelete) | **DELETE** /apps/{appId} | Removes app and all versions
[**appsAppIdGet**](AppsFindAndModifyAppsApi.md#appsAppIdGet) | **GET** /apps/{appId} | Returns a single APPROVED or SUSPENDED app
[**appsAppIdLivePost**](AppsFindAndModifyAppsApi.md#appsAppIdLivePost) | **POST** /apps/{appId}/live | Change the live app to another, previously approved version
[**appsAppIdPublishPost**](AppsFindAndModifyAppsApi.md#appsAppIdPublishPost) | **POST** /apps/{appId}/publish | Publishes the current working version of the app to the marketplace
[**appsAppIdVersionsVersionDelete**](AppsFindAndModifyAppsApi.md#appsAppIdVersionsVersionDelete) | **DELETE** /apps/{appId}/versions/{version} | Removes AppVersion
[**appsAppIdVersionsVersionGet**](AppsFindAndModifyAppsApi.md#appsAppIdVersionsVersionGet) | **GET** /apps/{appId}/versions/{version} | Returns a single AppVersion
[**appsAppIdVersionsVersionPatch**](AppsFindAndModifyAppsApi.md#appsAppIdVersionsVersionPatch) | **PATCH** /apps/{appId}/versions/{version} | Updates the app fields or creates a new version
[**appsAppIdVersionsVersionPost**](AppsFindAndModifyAppsApi.md#appsAppIdVersionsVersionPost) | **POST** /apps/{appId}/versions/{version} | Updates the app or creates a new version
[**appsAppIdVersionsVersionStatusPost**](AppsFindAndModifyAppsApi.md#appsAppIdVersionsVersionStatusPost) | **POST** /apps/{appId}/versions/{version}/status | Allows a developer or administrator to change the status of apps
[**appsBySafeNameSafeNameGet**](AppsFindAndModifyAppsApi.md#appsBySafeNameSafeNameGet) | **GET** /apps/bySafeName/{safeName} | Returns a single APPROVED or SUSPENDED app
[**appsGet**](AppsFindAndModifyAppsApi.md#appsGet) | **GET** /apps | Returns a paginated list of APPROVED or SUSPENDED apps
[**appsPost**](AppsFindAndModifyAppsApi.md#appsPost) | **POST** /apps | Adds a new app for this developer
[**appsTextSearchGet**](AppsFindAndModifyAppsApi.md#appsTextSearchGet) | **GET** /apps/textSearch | Searches through the text of fields to find APPROVED or SUSPENDED apps
[**appsVersionsGet**](AppsFindAndModifyAppsApi.md#appsVersionsGet) | **GET** /apps/versions | Returns a paginated list of AppVersions



## appsAppIdDelete

> appsAppIdDelete(appId, developerId)

Removes app and all versions

- This method is called on behalf of a developer. 

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.AppsFindAndModifyAppsApi();
let appId = "appId_example"; // String | The id of the App to be removed
let developerId = "developerId_example"; // String | The unique id of the developer that is removing this app
apiInstance.appsAppIdDelete(appId, developerId, (error, data, response) => {
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
 **appId** | **String**| The id of the App to be removed | 
 **developerId** | **String**| The unique id of the developer that is removing this app | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## appsAppIdGet

> App appsAppIdGet(appId, opts)

Returns a single APPROVED or SUSPENDED app

- A &#39;view&#39; event is recorded when trackViews is set to true 

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.AppsFindAndModifyAppsApi();
let appId = "appId_example"; // String | The id of the App to be located
let opts = {
  'userId': "userId_example", // String | The unique id of the user that is requesting this resource
  'trackViews': true // Boolean | Whether this call should be tracked as a 'view' for this app. Default is false.
};
apiInstance.appsAppIdGet(appId, opts, (error, data, response) => {
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
 **appId** | **String**| The id of the App to be located | 
 **userId** | **String**| The unique id of the user that is requesting this resource | [optional] 
 **trackViews** | **Boolean**| Whether this call should be tracked as a &#39;view&#39; for this app. Default is false. | [optional] 

### Return type

[**App**](App.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## appsAppIdLivePost

> appsAppIdLivePost(appId, developerId, version)

Change the live app to another, previously approved version

- This method is called on behalf of a developer. 

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.AppsFindAndModifyAppsApi();
let appId = "appId_example"; // String | The id of the App to be changed
let developerId = "developerId_example"; // String | The unique id of the developer that is changing this AppVersion
let version = "version_example"; // String | The new version of the live App
apiInstance.appsAppIdLivePost(appId, developerId, version, (error, data, response) => {
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
 **appId** | **String**| The id of the App to be changed | 
 **developerId** | **String**| The unique id of the developer that is changing this AppVersion | 
 **version** | **String**| The new version of the live App | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## appsAppIdPublishPost

> appsAppIdPublishPost(appId, developerId, version, opts)

Publishes the current working version of the app to the marketplace

- This method is called on behalf of a developer.  - Only effects the current working version of the app. 

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.AppsFindAndModifyAppsApi();
let appId = "appId_example"; // String | The id of the app to be published
let developerId = "developerId_example"; // String | The unique id of the developer that is modifying this app
let version = 56; // Number | The version of the app to be published
let opts = {
  'autoApprove': true // Boolean | If true, this AppVersion is automatically approved and becomes immediately available to end users
};
apiInstance.appsAppIdPublishPost(appId, developerId, version, opts, (error, data, response) => {
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
 **appId** | **String**| The id of the app to be published | 
 **developerId** | **String**| The unique id of the developer that is modifying this app | 
 **version** | **Number**| The version of the app to be published | 
 **autoApprove** | **Boolean**| If true, this AppVersion is automatically approved and becomes immediately available to end users | [optional] 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## appsAppIdVersionsVersionDelete

> appsAppIdVersionsVersionDelete(appId, version, developerId)

Removes AppVersion

- This method is called on behalf of a developer. 

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.AppsFindAndModifyAppsApi();
let appId = "appId_example"; // String | The id of the App to be removed
let version = "version_example"; // String | The version of the App to be removed
let developerId = "developerId_example"; // String | The unique id of the developer that is removing this app
apiInstance.appsAppIdVersionsVersionDelete(appId, version, developerId, (error, data, response) => {
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
 **appId** | **String**| The id of the App to be removed | 
 **version** | **String**| The version of the App to be removed | 
 **developerId** | **String**| The unique id of the developer that is removing this app | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## appsAppIdVersionsVersionGet

> AppVersion appsAppIdVersionsVersionGet(appId, version, opts)

Returns a single AppVersion

- Only returns AppVersions owned by this developer 

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.AppsFindAndModifyAppsApi();
let appId = "appId_example"; // String | The id of the App to be located
let version = 56; // Number | The version number of the app
let opts = {
  'developerId': "developerId_example" // String | The unique id of the developer that is requesting this resource
};
apiInstance.appsAppIdVersionsVersionGet(appId, version, opts, (error, data, response) => {
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
 **appId** | **String**| The id of the App to be located | 
 **version** | **Number**| The version number of the app | 
 **developerId** | **String**| The unique id of the developer that is requesting this resource | [optional] 

### Return type

[**AppVersion**](AppVersion.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## appsAppIdVersionsVersionPatch

> AppVersion appsAppIdVersionsVersionPatch(appId, version, developerId, opts)

Updates the app fields or creates a new version

- This method is called on behalf of a developer. - Price and is required if the model is &#39;single&#39; or &#39;recurring&#39; - Returns the newly updated app - This endpoint updates only the fields provided in the request (relative update). In contrast, the POST version of this method replaces the entire object to match the request (absolute update).  

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.AppsFindAndModifyAppsApi();
let appId = "appId_example"; // String | The id of the App to be updated
let version = "version_example"; // String | The version of the App to be updated
let developerId = "developerId_example"; // String | The unique id of the developer that is updating this app
let opts = {
  'name': "name_example", // String | The name of the app
  'type': "type_example", // String | The type for this app
  'model': "model_example", // String | A JSON object representing the pricing model type for this app
  'customData': "customData_example", // String | A custom JSON object that you can create and attach to this record
  'attributes': "attributes_example", // String | A custom set of app attributes defined by the administrator and attached to this app
  'restrict': "restrict_example", // String | JSON object to restrict users from purchasing or viewing this app. Example: {'view':{'country':['Canada','Mexico']},'purchase':{'country':['Canada','Mexico']}} restricts users from canada and mexico from viewing or purchasing this app
  'allow': "allow_example", // String | JSON object to allow users to purchase or view this app. Example: {'purchase':{'country':['Canada','Mexico']}} allows only users from canada and mexico to purchase this app
  'access': "access_example", // String | JSON array of data access requirements
  'approvalRequired': "approvalRequired_example" // String | False if updates should skip the approval process and be available immediately. Default is True
};
apiInstance.appsAppIdVersionsVersionPatch(appId, version, developerId, opts, (error, data, response) => {
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
 **appId** | **String**| The id of the App to be updated | 
 **version** | **String**| The version of the App to be updated | 
 **developerId** | **String**| The unique id of the developer that is updating this app | 
 **name** | **String**| The name of the app | [optional] 
 **type** | **String**| The type for this app | [optional] 
 **model** | **String**| A JSON object representing the pricing model type for this app | [optional] 
 **customData** | **String**| A custom JSON object that you can create and attach to this record | [optional] 
 **attributes** | **String**| A custom set of app attributes defined by the administrator and attached to this app | [optional] 
 **restrict** | **String**| JSON object to restrict users from purchasing or viewing this app. Example: {&#39;view&#39;:{&#39;country&#39;:[&#39;Canada&#39;,&#39;Mexico&#39;]},&#39;purchase&#39;:{&#39;country&#39;:[&#39;Canada&#39;,&#39;Mexico&#39;]}} restricts users from canada and mexico from viewing or purchasing this app | [optional] 
 **allow** | **String**| JSON object to allow users to purchase or view this app. Example: {&#39;purchase&#39;:{&#39;country&#39;:[&#39;Canada&#39;,&#39;Mexico&#39;]}} allows only users from canada and mexico to purchase this app | [optional] 
 **access** | **String**| JSON array of data access requirements | [optional] 
 **approvalRequired** | **String**| False if updates should skip the approval process and be available immediately. Default is True | [optional] 

### Return type

[**AppVersion**](AppVersion.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## appsAppIdVersionsVersionPost

> AppVersion appsAppIdVersionsVersionPost(appId, version, developerId, opts)

Updates the app or creates a new version

- This method is called on behalf of a developer. - Price and is required if the model is &#39;single&#39; or &#39;recurring&#39; - Returns the newly updated app - This endpoint replaces the entire object to match the request (absolute update). In contrast, the PATCH version of this endpoint updates only the fields provided in the request (relative update). 

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.AppsFindAndModifyAppsApi();
let appId = "appId_example"; // String | The id of the App to be updated
let version = "version_example"; // String | The version of the App to be updated
let developerId = "developerId_example"; // String | The unique id of the developer that is updating this app
let opts = {
  'name': "name_example", // String | The name of the app
  'type': "type_example", // String | The type for this app
  'model': "model_example", // String | A JSON object representing the pricing model type for this app
  'customData': "customData_example", // String | A custom JSON object that you can create and attach to this record
  'attributes': "attributes_example", // String | A custom set of app attributes defined by the administrator and attached to this app
  'restrict': "restrict_example", // String | JSON object to restrict users from purchasing or viewing this app. Example: {'view':{'country':['Canada','Mexico']},'purchase':{'country':['Canada','Mexico']}} restricts users from canada and mexico from viewing or purchasing this app
  'allow': "allow_example", // String | JSON object to allow users to purchase or view this app. Example: {'purchase':{'country':['Canada','Mexico']}} allows only users from canada and mexico to purchase this app
  'access': "access_example", // String | JSON array of data access requirements
  'approvalRequired': "approvalRequired_example" // String | False if updates should skip the approval process and be available immediately. Default is True
};
apiInstance.appsAppIdVersionsVersionPost(appId, version, developerId, opts, (error, data, response) => {
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
 **appId** | **String**| The id of the App to be updated | 
 **version** | **String**| The version of the App to be updated | 
 **developerId** | **String**| The unique id of the developer that is updating this app | 
 **name** | **String**| The name of the app | [optional] 
 **type** | **String**| The type for this app | [optional] 
 **model** | **String**| A JSON object representing the pricing model type for this app | [optional] 
 **customData** | **String**| A custom JSON object that you can create and attach to this record | [optional] 
 **attributes** | **String**| A custom set of app attributes defined by the administrator and attached to this app | [optional] 
 **restrict** | **String**| JSON object to restrict users from purchasing or viewing this app. Example: {&#39;view&#39;:{&#39;country&#39;:[&#39;Canada&#39;,&#39;Mexico&#39;]},&#39;purchase&#39;:{&#39;country&#39;:[&#39;Canada&#39;,&#39;Mexico&#39;]}} restricts users from canada and mexico from viewing or purchasing this app | [optional] 
 **allow** | **String**| JSON object to allow users to purchase or view this app. Example: {&#39;purchase&#39;:{&#39;country&#39;:[&#39;Canada&#39;,&#39;Mexico&#39;]}} allows only users from canada and mexico to purchase this app | [optional] 
 **access** | **String**| JSON array of data access requirements | [optional] 
 **approvalRequired** | **String**| False if updates should skip the approval process and be available immediately. Default is True | [optional] 

### Return type

[**AppVersion**](AppVersion.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## appsAppIdVersionsVersionStatusPost

> appsAppIdVersionsVersionStatusPost(appId, version, opts)

Allows a developer or administrator to change the status of apps

Only certain status changes are allowed. For instance, a developer is only able to suspend and unsuspend their app (which must already be approved). See here for a state change diagram of allowed status changes for administrators: https://support.openchannel.io/documentation/api/#415-apps-status-change 

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.AppsFindAndModifyAppsApi();
let appId = "appId_example"; // String | The id of the App to be updated
let version = 56; // Number | The version of the App to be updated
let opts = {
  'developerId': "developerId_example", // String | The unique id of the developer that is modifying this app
  'status': "status_example", // String | The new status for this app. Can be either 'inReview', 'approved', 'suspended' or 'rejected'
  'modifiedBy': "'administrator'", // String | The role initiating this status change. Can be either 'developer' or 'administrator' (default)
  'reason': "reason_example" // String | The reason for this status change
};
apiInstance.appsAppIdVersionsVersionStatusPost(appId, version, opts, (error, data, response) => {
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
 **appId** | **String**| The id of the App to be updated | 
 **version** | **Number**| The version of the App to be updated | 
 **developerId** | **String**| The unique id of the developer that is modifying this app | [optional] 
 **status** | **String**| The new status for this app. Can be either &#39;inReview&#39;, &#39;approved&#39;, &#39;suspended&#39; or &#39;rejected&#39; | [optional] 
 **modifiedBy** | **String**| The role initiating this status change. Can be either &#39;developer&#39; or &#39;administrator&#39; (default) | [optional] [default to &#39;administrator&#39;]
 **reason** | **String**| The reason for this status change | [optional] 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## appsBySafeNameSafeNameGet

> App appsBySafeNameSafeNameGet(safeName, opts)

Returns a single APPROVED or SUSPENDED app

- A &#39;view&#39; event is recorded when trackViews is set to true 

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.AppsFindAndModifyAppsApi();
let safeName = "safeName_example"; // String | The safeName of the App to be located
let opts = {
  'userId': "userId_example", // String | The unique id of the user that is requesting this resource
  'trackViews': true // Boolean | Whether this call should be tracked as a 'view' for this app. Default is false.
};
apiInstance.appsBySafeNameSafeNameGet(safeName, opts, (error, data, response) => {
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
 **safeName** | **String**| The safeName of the App to be located | 
 **userId** | **String**| The unique id of the user that is requesting this resource | [optional] 
 **trackViews** | **Boolean**| Whether this call should be tracked as a &#39;view&#39; for this app. Default is false. | [optional] 

### Return type

[**App**](App.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## appsGet

> AppPages appsGet(opts)

Returns a paginated list of APPROVED or SUSPENDED apps

- Results are paginated and the default is value is 1000 if no limit is provided - If no query is specified, returns all APPROVED or SUSPENDED apps within the marketplace 

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.AppsFindAndModifyAppsApi();
let opts = {
  'query': "query_example", // String | A query document. Example: {'name':'MyApp'} matches all the apps that have the name 'MyApp'
  'sort': "sort_example", // String | A sort document. Example: {'name':1} sorts the results by name in ascending order
  'pageNumber': 56, // Number | The result set page number to be returned
  'limit': 56, // Number | The maximum number of results to return per page
  'userId': "userId_example", // String | The unique id of the user requesting this resource
  'isOwner': true // Boolean | Whether this result should only contain apps that are owned by this user
};
apiInstance.appsGet(opts, (error, data, response) => {
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
 **query** | **String**| A query document. Example: {&#39;name&#39;:&#39;MyApp&#39;} matches all the apps that have the name &#39;MyApp&#39; | [optional] 
 **sort** | **String**| A sort document. Example: {&#39;name&#39;:1} sorts the results by name in ascending order | [optional] 
 **pageNumber** | **Number**| The result set page number to be returned | [optional] 
 **limit** | **Number**| The maximum number of results to return per page | [optional] 
 **userId** | **String**| The unique id of the user requesting this resource | [optional] 
 **isOwner** | **Boolean**| Whether this result should only contain apps that are owned by this user | [optional] 

### Return type

[**AppPages**](AppPages.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## appsPost

> AppVersion appsPost(developerId, name, opts)

Adds a new app for this developer

- This method is called on behalf of a developer. - Price is required if the model is &#39;single&#39; or &#39;recurring&#39; - Returns the newly created app 

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.AppsFindAndModifyAppsApi();
let developerId = "developerId_example"; // String | The unique id of the developer that is adding this app
let name = "name_example"; // String | The name of the app
let opts = {
  'type': "type_example", // String | The type for this app
  'model': "model_example", // String | A JSON object representing the pricing model type for this app
  'customData': "customData_example", // String | A custom JSON object that you can create and attach to this record
  'attributes': "attributes_example", // String | A custom set of app attributes defined by the administrator and attached to this app
  'restrict': "restrict_example", // String | JSON object to restrict users from owning or viewing this app. Example: {'view':{'country':['Canada','Mexico']},'own':{'country':['Canada','Mexico']}} restricts users from canada and mexico from viewing or owning this app
  'allow': "allow_example", // String | JSON object to restrict users from owning or viewing this app. Example: {'view':{'country':['Canada','Mexico']},'own':{'country':['Canada','Mexico']}} restricts users from canada and mexico from viewing or owning this app
  'access': "access_example" // String | JSON array of data access requirements
};
apiInstance.appsPost(developerId, name, opts, (error, data, response) => {
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
 **developerId** | **String**| The unique id of the developer that is adding this app | 
 **name** | **String**| The name of the app | 
 **type** | **String**| The type for this app | [optional] 
 **model** | **String**| A JSON object representing the pricing model type for this app | [optional] 
 **customData** | **String**| A custom JSON object that you can create and attach to this record | [optional] 
 **attributes** | **String**| A custom set of app attributes defined by the administrator and attached to this app | [optional] 
 **restrict** | **String**| JSON object to restrict users from owning or viewing this app. Example: {&#39;view&#39;:{&#39;country&#39;:[&#39;Canada&#39;,&#39;Mexico&#39;]},&#39;own&#39;:{&#39;country&#39;:[&#39;Canada&#39;,&#39;Mexico&#39;]}} restricts users from canada and mexico from viewing or owning this app | [optional] 
 **allow** | **String**| JSON object to restrict users from owning or viewing this app. Example: {&#39;view&#39;:{&#39;country&#39;:[&#39;Canada&#39;,&#39;Mexico&#39;]},&#39;own&#39;:{&#39;country&#39;:[&#39;Canada&#39;,&#39;Mexico&#39;]}} restricts users from canada and mexico from viewing or owning this app | [optional] 
 **access** | **String**| JSON array of data access requirements | [optional] 

### Return type

[**AppVersion**](AppVersion.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## appsTextSearchGet

> SearchPages appsTextSearchGet(text, fields, opts)

Searches through the text of fields to find APPROVED or SUSPENDED apps

- Results are returned for the market provided within the basic authentication credentials 

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.AppsFindAndModifyAppsApi();
let text = "text_example"; // String | The text to search for.
let fields = "fields_example"; // String | A JSON array containing all the fields to be searched through. Example: ['name', 'customData.description']
let opts = {
  'query': "query_example", // String | A query document. Example: {'name':'MyApp'} matches all the documents that have the name 'MyApp'
  'pageNumber': 56, // Number | The result set page number to be returned
  'limit': 56, // Number | The maximum number of results to return per page
  'userId': "userId_example", // String | The unique id of the user requesting this resource
  'isOwned': true // Boolean | Whether this result should only contain apps that are owned by this user
};
apiInstance.appsTextSearchGet(text, fields, opts, (error, data, response) => {
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
 **text** | **String**| The text to search for. | 
 **fields** | **String**| A JSON array containing all the fields to be searched through. Example: [&#39;name&#39;, &#39;customData.description&#39;] | 
 **query** | **String**| A query document. Example: {&#39;name&#39;:&#39;MyApp&#39;} matches all the documents that have the name &#39;MyApp&#39; | [optional] 
 **pageNumber** | **Number**| The result set page number to be returned | [optional] 
 **limit** | **Number**| The maximum number of results to return per page | [optional] 
 **userId** | **String**| The unique id of the user requesting this resource | [optional] 
 **isOwned** | **Boolean**| Whether this result should only contain apps that are owned by this user | [optional] 

### Return type

[**SearchPages**](SearchPages.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## appsVersionsGet

> VersionPages appsVersionsGet(opts)

Returns a paginated list of AppVersions

- Results are paginated when limit is set, otherwise all results are returned - If no query is specified, returns all AppVersions within the marketplace - Only returns AppVersions owned by this developer 

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.AppsFindAndModifyAppsApi();
let opts = {
  'query': "query_example", // String | A query document. Example: {'name':'MyApp'} matches all the apps that have the name 'MyApp'
  'sort': "sort_example", // String | A sort document. Example: {'name':1} sorts the results by name in ascending order
  'pageNumber': 56, // Number | The result set page number to be returned
  'limit': 56, // Number | The maximum number of results to return per page
  'developerId': "developerId_example" // String | The unique id of the developer requesting this resource
};
apiInstance.appsVersionsGet(opts, (error, data, response) => {
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
 **query** | **String**| A query document. Example: {&#39;name&#39;:&#39;MyApp&#39;} matches all the apps that have the name &#39;MyApp&#39; | [optional] 
 **sort** | **String**| A sort document. Example: {&#39;name&#39;:1} sorts the results by name in ascending order | [optional] 
 **pageNumber** | **Number**| The result set page number to be returned | [optional] 
 **limit** | **Number**| The maximum number of results to return per page | [optional] 
 **developerId** | **String**| The unique id of the developer requesting this resource | [optional] 

### Return type

[**VersionPages**](VersionPages.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

