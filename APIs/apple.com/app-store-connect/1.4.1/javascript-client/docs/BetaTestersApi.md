# AppStoreConnectApi.BetaTestersApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**betaTestersAppsDeleteToManyRelationship**](BetaTestersApi.md#betaTestersAppsDeleteToManyRelationship) | **DELETE** /v1/betaTesters/{id}/relationships/apps | 
[**betaTestersAppsGetToManyRelated**](BetaTestersApi.md#betaTestersAppsGetToManyRelated) | **GET** /v1/betaTesters/{id}/apps | 
[**betaTestersAppsGetToManyRelationship**](BetaTestersApi.md#betaTestersAppsGetToManyRelationship) | **GET** /v1/betaTesters/{id}/relationships/apps | 
[**betaTestersBetaGroupsCreateToManyRelationship**](BetaTestersApi.md#betaTestersBetaGroupsCreateToManyRelationship) | **POST** /v1/betaTesters/{id}/relationships/betaGroups | 
[**betaTestersBetaGroupsDeleteToManyRelationship**](BetaTestersApi.md#betaTestersBetaGroupsDeleteToManyRelationship) | **DELETE** /v1/betaTesters/{id}/relationships/betaGroups | 
[**betaTestersBetaGroupsGetToManyRelated**](BetaTestersApi.md#betaTestersBetaGroupsGetToManyRelated) | **GET** /v1/betaTesters/{id}/betaGroups | 
[**betaTestersBetaGroupsGetToManyRelationship**](BetaTestersApi.md#betaTestersBetaGroupsGetToManyRelationship) | **GET** /v1/betaTesters/{id}/relationships/betaGroups | 
[**betaTestersBuildsCreateToManyRelationship**](BetaTestersApi.md#betaTestersBuildsCreateToManyRelationship) | **POST** /v1/betaTesters/{id}/relationships/builds | 
[**betaTestersBuildsDeleteToManyRelationship**](BetaTestersApi.md#betaTestersBuildsDeleteToManyRelationship) | **DELETE** /v1/betaTesters/{id}/relationships/builds | 
[**betaTestersBuildsGetToManyRelated**](BetaTestersApi.md#betaTestersBuildsGetToManyRelated) | **GET** /v1/betaTesters/{id}/builds | 
[**betaTestersBuildsGetToManyRelationship**](BetaTestersApi.md#betaTestersBuildsGetToManyRelationship) | **GET** /v1/betaTesters/{id}/relationships/builds | 
[**betaTestersCreateInstance**](BetaTestersApi.md#betaTestersCreateInstance) | **POST** /v1/betaTesters | 
[**betaTestersDeleteInstance**](BetaTestersApi.md#betaTestersDeleteInstance) | **DELETE** /v1/betaTesters/{id} | 
[**betaTestersGetCollection**](BetaTestersApi.md#betaTestersGetCollection) | **GET** /v1/betaTesters | 
[**betaTestersGetInstance**](BetaTestersApi.md#betaTestersGetInstance) | **GET** /v1/betaTesters/{id} | 



## betaTestersAppsDeleteToManyRelationship

> betaTestersAppsDeleteToManyRelationship(id, betaTesterAppsLinkagesRequest)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BetaTestersApi();
let id = "id_example"; // String | the id of the requested resource
let betaTesterAppsLinkagesRequest = new AppStoreConnectApi.BetaTesterAppsLinkagesRequest(); // BetaTesterAppsLinkagesRequest | List of related linkages
apiInstance.betaTestersAppsDeleteToManyRelationship(id, betaTesterAppsLinkagesRequest, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **betaTesterAppsLinkagesRequest** | [**BetaTesterAppsLinkagesRequest**](BetaTesterAppsLinkagesRequest.md)| List of related linkages | 

### Return type

null (empty response body)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## betaTestersAppsGetToManyRelated

> AppsResponse betaTestersAppsGetToManyRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BetaTestersApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsApps': ["null"], // [String] | the fields to include for returned resources of type apps
  'limit': 56 // Number | maximum resources per page
};
apiInstance.betaTestersAppsGetToManyRelated(id, opts, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **fieldsApps** | [**[String]**](String.md)| the fields to include for returned resources of type apps | [optional] 
 **limit** | **Number**| maximum resources per page | [optional] 

### Return type

[**AppsResponse**](AppsResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## betaTestersAppsGetToManyRelationship

> BetaTesterAppsLinkagesResponse betaTestersAppsGetToManyRelationship(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BetaTestersApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'limit': 56 // Number | maximum resources per page
};
apiInstance.betaTestersAppsGetToManyRelationship(id, opts, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **limit** | **Number**| maximum resources per page | [optional] 

### Return type

[**BetaTesterAppsLinkagesResponse**](BetaTesterAppsLinkagesResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## betaTestersBetaGroupsCreateToManyRelationship

> betaTestersBetaGroupsCreateToManyRelationship(id, betaTesterBetaGroupsLinkagesRequest)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BetaTestersApi();
let id = "id_example"; // String | the id of the requested resource
let betaTesterBetaGroupsLinkagesRequest = new AppStoreConnectApi.BetaTesterBetaGroupsLinkagesRequest(); // BetaTesterBetaGroupsLinkagesRequest | List of related linkages
apiInstance.betaTestersBetaGroupsCreateToManyRelationship(id, betaTesterBetaGroupsLinkagesRequest, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **betaTesterBetaGroupsLinkagesRequest** | [**BetaTesterBetaGroupsLinkagesRequest**](BetaTesterBetaGroupsLinkagesRequest.md)| List of related linkages | 

### Return type

null (empty response body)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## betaTestersBetaGroupsDeleteToManyRelationship

> betaTestersBetaGroupsDeleteToManyRelationship(id, betaTesterBetaGroupsLinkagesRequest)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BetaTestersApi();
let id = "id_example"; // String | the id of the requested resource
let betaTesterBetaGroupsLinkagesRequest = new AppStoreConnectApi.BetaTesterBetaGroupsLinkagesRequest(); // BetaTesterBetaGroupsLinkagesRequest | List of related linkages
apiInstance.betaTestersBetaGroupsDeleteToManyRelationship(id, betaTesterBetaGroupsLinkagesRequest, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **betaTesterBetaGroupsLinkagesRequest** | [**BetaTesterBetaGroupsLinkagesRequest**](BetaTesterBetaGroupsLinkagesRequest.md)| List of related linkages | 

### Return type

null (empty response body)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## betaTestersBetaGroupsGetToManyRelated

> BetaGroupsResponse betaTestersBetaGroupsGetToManyRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BetaTestersApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsBetaGroups': ["null"], // [String] | the fields to include for returned resources of type betaGroups
  'limit': 56 // Number | maximum resources per page
};
apiInstance.betaTestersBetaGroupsGetToManyRelated(id, opts, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **fieldsBetaGroups** | [**[String]**](String.md)| the fields to include for returned resources of type betaGroups | [optional] 
 **limit** | **Number**| maximum resources per page | [optional] 

### Return type

[**BetaGroupsResponse**](BetaGroupsResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## betaTestersBetaGroupsGetToManyRelationship

> BetaTesterBetaGroupsLinkagesResponse betaTestersBetaGroupsGetToManyRelationship(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BetaTestersApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'limit': 56 // Number | maximum resources per page
};
apiInstance.betaTestersBetaGroupsGetToManyRelationship(id, opts, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **limit** | **Number**| maximum resources per page | [optional] 

### Return type

[**BetaTesterBetaGroupsLinkagesResponse**](BetaTesterBetaGroupsLinkagesResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## betaTestersBuildsCreateToManyRelationship

> betaTestersBuildsCreateToManyRelationship(id, betaTesterBuildsLinkagesRequest)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BetaTestersApi();
let id = "id_example"; // String | the id of the requested resource
let betaTesterBuildsLinkagesRequest = new AppStoreConnectApi.BetaTesterBuildsLinkagesRequest(); // BetaTesterBuildsLinkagesRequest | List of related linkages
apiInstance.betaTestersBuildsCreateToManyRelationship(id, betaTesterBuildsLinkagesRequest, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **betaTesterBuildsLinkagesRequest** | [**BetaTesterBuildsLinkagesRequest**](BetaTesterBuildsLinkagesRequest.md)| List of related linkages | 

### Return type

null (empty response body)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## betaTestersBuildsDeleteToManyRelationship

> betaTestersBuildsDeleteToManyRelationship(id, betaTesterBuildsLinkagesRequest)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BetaTestersApi();
let id = "id_example"; // String | the id of the requested resource
let betaTesterBuildsLinkagesRequest = new AppStoreConnectApi.BetaTesterBuildsLinkagesRequest(); // BetaTesterBuildsLinkagesRequest | List of related linkages
apiInstance.betaTestersBuildsDeleteToManyRelationship(id, betaTesterBuildsLinkagesRequest, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **betaTesterBuildsLinkagesRequest** | [**BetaTesterBuildsLinkagesRequest**](BetaTesterBuildsLinkagesRequest.md)| List of related linkages | 

### Return type

null (empty response body)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## betaTestersBuildsGetToManyRelated

> BuildsResponse betaTestersBuildsGetToManyRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BetaTestersApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsBuilds': ["null"], // [String] | the fields to include for returned resources of type builds
  'limit': 56 // Number | maximum resources per page
};
apiInstance.betaTestersBuildsGetToManyRelated(id, opts, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **fieldsBuilds** | [**[String]**](String.md)| the fields to include for returned resources of type builds | [optional] 
 **limit** | **Number**| maximum resources per page | [optional] 

### Return type

[**BuildsResponse**](BuildsResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## betaTestersBuildsGetToManyRelationship

> BetaTesterBuildsLinkagesResponse betaTestersBuildsGetToManyRelationship(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BetaTestersApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'limit': 56 // Number | maximum resources per page
};
apiInstance.betaTestersBuildsGetToManyRelationship(id, opts, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **limit** | **Number**| maximum resources per page | [optional] 

### Return type

[**BetaTesterBuildsLinkagesResponse**](BetaTesterBuildsLinkagesResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## betaTestersCreateInstance

> BetaTesterResponse betaTestersCreateInstance(betaTesterCreateRequest)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BetaTestersApi();
let betaTesterCreateRequest = new AppStoreConnectApi.BetaTesterCreateRequest(); // BetaTesterCreateRequest | BetaTester representation
apiInstance.betaTestersCreateInstance(betaTesterCreateRequest, (error, data, response) => {
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
 **betaTesterCreateRequest** | [**BetaTesterCreateRequest**](BetaTesterCreateRequest.md)| BetaTester representation | 

### Return type

[**BetaTesterResponse**](BetaTesterResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## betaTestersDeleteInstance

> betaTestersDeleteInstance(id)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BetaTestersApi();
let id = "id_example"; // String | the id of the requested resource
apiInstance.betaTestersDeleteInstance(id, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 

### Return type

null (empty response body)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## betaTestersGetCollection

> BetaTestersResponse betaTestersGetCollection(opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BetaTestersApi();
let opts = {
  'filterEmail': ["null"], // [String] | filter by attribute 'email'
  'filterFirstName': ["null"], // [String] | filter by attribute 'firstName'
  'filterInviteType': ["null"], // [String] | filter by attribute 'inviteType'
  'filterLastName': ["null"], // [String] | filter by attribute 'lastName'
  'filterApps': ["null"], // [String] | filter by id(s) of related 'apps'
  'filterBetaGroups': ["null"], // [String] | filter by id(s) of related 'betaGroups'
  'filterBuilds': ["null"], // [String] | filter by id(s) of related 'builds'
  'sort': ["null"], // [String] | comma-separated list of sort expressions; resources will be sorted as specified
  'fieldsBetaTesters': ["null"], // [String] | the fields to include for returned resources of type betaTesters
  'limit': 56, // Number | maximum resources per page
  'include': ["null"], // [String] | comma-separated list of relationships to include
  'fieldsBetaGroups': ["null"], // [String] | the fields to include for returned resources of type betaGroups
  'fieldsBuilds': ["null"], // [String] | the fields to include for returned resources of type builds
  'fieldsApps': ["null"], // [String] | the fields to include for returned resources of type apps
  'limitApps': 56, // Number | maximum number of related apps returned (when they are included)
  'limitBetaGroups': 56, // Number | maximum number of related betaGroups returned (when they are included)
  'limitBuilds': 56 // Number | maximum number of related builds returned (when they are included)
};
apiInstance.betaTestersGetCollection(opts, (error, data, response) => {
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
 **filterEmail** | [**[String]**](String.md)| filter by attribute &#39;email&#39; | [optional] 
 **filterFirstName** | [**[String]**](String.md)| filter by attribute &#39;firstName&#39; | [optional] 
 **filterInviteType** | [**[String]**](String.md)| filter by attribute &#39;inviteType&#39; | [optional] 
 **filterLastName** | [**[String]**](String.md)| filter by attribute &#39;lastName&#39; | [optional] 
 **filterApps** | [**[String]**](String.md)| filter by id(s) of related &#39;apps&#39; | [optional] 
 **filterBetaGroups** | [**[String]**](String.md)| filter by id(s) of related &#39;betaGroups&#39; | [optional] 
 **filterBuilds** | [**[String]**](String.md)| filter by id(s) of related &#39;builds&#39; | [optional] 
 **sort** | [**[String]**](String.md)| comma-separated list of sort expressions; resources will be sorted as specified | [optional] 
 **fieldsBetaTesters** | [**[String]**](String.md)| the fields to include for returned resources of type betaTesters | [optional] 
 **limit** | **Number**| maximum resources per page | [optional] 
 **include** | [**[String]**](String.md)| comma-separated list of relationships to include | [optional] 
 **fieldsBetaGroups** | [**[String]**](String.md)| the fields to include for returned resources of type betaGroups | [optional] 
 **fieldsBuilds** | [**[String]**](String.md)| the fields to include for returned resources of type builds | [optional] 
 **fieldsApps** | [**[String]**](String.md)| the fields to include for returned resources of type apps | [optional] 
 **limitApps** | **Number**| maximum number of related apps returned (when they are included) | [optional] 
 **limitBetaGroups** | **Number**| maximum number of related betaGroups returned (when they are included) | [optional] 
 **limitBuilds** | **Number**| maximum number of related builds returned (when they are included) | [optional] 

### Return type

[**BetaTestersResponse**](BetaTestersResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## betaTestersGetInstance

> BetaTesterResponse betaTestersGetInstance(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BetaTestersApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsBetaTesters': ["null"], // [String] | the fields to include for returned resources of type betaTesters
  'include': ["null"], // [String] | comma-separated list of relationships to include
  'fieldsBetaGroups': ["null"], // [String] | the fields to include for returned resources of type betaGroups
  'fieldsBuilds': ["null"], // [String] | the fields to include for returned resources of type builds
  'fieldsApps': ["null"], // [String] | the fields to include for returned resources of type apps
  'limitApps': 56, // Number | maximum number of related apps returned (when they are included)
  'limitBetaGroups': 56, // Number | maximum number of related betaGroups returned (when they are included)
  'limitBuilds': 56 // Number | maximum number of related builds returned (when they are included)
};
apiInstance.betaTestersGetInstance(id, opts, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **fieldsBetaTesters** | [**[String]**](String.md)| the fields to include for returned resources of type betaTesters | [optional] 
 **include** | [**[String]**](String.md)| comma-separated list of relationships to include | [optional] 
 **fieldsBetaGroups** | [**[String]**](String.md)| the fields to include for returned resources of type betaGroups | [optional] 
 **fieldsBuilds** | [**[String]**](String.md)| the fields to include for returned resources of type builds | [optional] 
 **fieldsApps** | [**[String]**](String.md)| the fields to include for returned resources of type apps | [optional] 
 **limitApps** | **Number**| maximum number of related apps returned (when they are included) | [optional] 
 **limitBetaGroups** | **Number**| maximum number of related betaGroups returned (when they are included) | [optional] 
 **limitBuilds** | **Number**| maximum number of related builds returned (when they are included) | [optional] 

### Return type

[**BetaTesterResponse**](BetaTesterResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

