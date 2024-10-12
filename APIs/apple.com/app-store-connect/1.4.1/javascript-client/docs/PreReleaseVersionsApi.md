# AppStoreConnectApi.PreReleaseVersionsApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**preReleaseVersionsAppGetToOneRelated**](PreReleaseVersionsApi.md#preReleaseVersionsAppGetToOneRelated) | **GET** /v1/preReleaseVersions/{id}/app | 
[**preReleaseVersionsBuildsGetToManyRelated**](PreReleaseVersionsApi.md#preReleaseVersionsBuildsGetToManyRelated) | **GET** /v1/preReleaseVersions/{id}/builds | 
[**preReleaseVersionsGetCollection**](PreReleaseVersionsApi.md#preReleaseVersionsGetCollection) | **GET** /v1/preReleaseVersions | 
[**preReleaseVersionsGetInstance**](PreReleaseVersionsApi.md#preReleaseVersionsGetInstance) | **GET** /v1/preReleaseVersions/{id} | 



## preReleaseVersionsAppGetToOneRelated

> AppResponse preReleaseVersionsAppGetToOneRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.PreReleaseVersionsApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsApps': ["null"] // [String] | the fields to include for returned resources of type apps
};
apiInstance.preReleaseVersionsAppGetToOneRelated(id, opts, (error, data, response) => {
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

### Return type

[**AppResponse**](AppResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## preReleaseVersionsBuildsGetToManyRelated

> BuildsResponse preReleaseVersionsBuildsGetToManyRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.PreReleaseVersionsApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsBuilds': ["null"], // [String] | the fields to include for returned resources of type builds
  'limit': 56 // Number | maximum resources per page
};
apiInstance.preReleaseVersionsBuildsGetToManyRelated(id, opts, (error, data, response) => {
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


## preReleaseVersionsGetCollection

> PreReleaseVersionsResponse preReleaseVersionsGetCollection(opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.PreReleaseVersionsApi();
let opts = {
  'filterBuildsExpired': ["null"], // [String] | filter by attribute 'builds.expired'
  'filterBuildsProcessingState': ["null"], // [String] | filter by attribute 'builds.processingState'
  'filterPlatform': ["null"], // [String] | filter by attribute 'platform'
  'filterVersion': ["null"], // [String] | filter by attribute 'version'
  'filterApp': ["null"], // [String] | filter by id(s) of related 'app'
  'filterBuilds': ["null"], // [String] | filter by id(s) of related 'builds'
  'sort': ["null"], // [String] | comma-separated list of sort expressions; resources will be sorted as specified
  'fieldsPreReleaseVersions': ["null"], // [String] | the fields to include for returned resources of type preReleaseVersions
  'limit': 56, // Number | maximum resources per page
  'include': ["null"], // [String] | comma-separated list of relationships to include
  'fieldsBuilds': ["null"], // [String] | the fields to include for returned resources of type builds
  'fieldsApps': ["null"], // [String] | the fields to include for returned resources of type apps
  'limitBuilds': 56 // Number | maximum number of related builds returned (when they are included)
};
apiInstance.preReleaseVersionsGetCollection(opts, (error, data, response) => {
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
 **filterBuildsExpired** | [**[String]**](String.md)| filter by attribute &#39;builds.expired&#39; | [optional] 
 **filterBuildsProcessingState** | [**[String]**](String.md)| filter by attribute &#39;builds.processingState&#39; | [optional] 
 **filterPlatform** | [**[String]**](String.md)| filter by attribute &#39;platform&#39; | [optional] 
 **filterVersion** | [**[String]**](String.md)| filter by attribute &#39;version&#39; | [optional] 
 **filterApp** | [**[String]**](String.md)| filter by id(s) of related &#39;app&#39; | [optional] 
 **filterBuilds** | [**[String]**](String.md)| filter by id(s) of related &#39;builds&#39; | [optional] 
 **sort** | [**[String]**](String.md)| comma-separated list of sort expressions; resources will be sorted as specified | [optional] 
 **fieldsPreReleaseVersions** | [**[String]**](String.md)| the fields to include for returned resources of type preReleaseVersions | [optional] 
 **limit** | **Number**| maximum resources per page | [optional] 
 **include** | [**[String]**](String.md)| comma-separated list of relationships to include | [optional] 
 **fieldsBuilds** | [**[String]**](String.md)| the fields to include for returned resources of type builds | [optional] 
 **fieldsApps** | [**[String]**](String.md)| the fields to include for returned resources of type apps | [optional] 
 **limitBuilds** | **Number**| maximum number of related builds returned (when they are included) | [optional] 

### Return type

[**PreReleaseVersionsResponse**](PreReleaseVersionsResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## preReleaseVersionsGetInstance

> PrereleaseVersionResponse preReleaseVersionsGetInstance(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.PreReleaseVersionsApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsPreReleaseVersions': ["null"], // [String] | the fields to include for returned resources of type preReleaseVersions
  'include': ["null"], // [String] | comma-separated list of relationships to include
  'fieldsBuilds': ["null"], // [String] | the fields to include for returned resources of type builds
  'fieldsApps': ["null"], // [String] | the fields to include for returned resources of type apps
  'limitBuilds': 56 // Number | maximum number of related builds returned (when they are included)
};
apiInstance.preReleaseVersionsGetInstance(id, opts, (error, data, response) => {
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
 **fieldsPreReleaseVersions** | [**[String]**](String.md)| the fields to include for returned resources of type preReleaseVersions | [optional] 
 **include** | [**[String]**](String.md)| comma-separated list of relationships to include | [optional] 
 **fieldsBuilds** | [**[String]**](String.md)| the fields to include for returned resources of type builds | [optional] 
 **fieldsApps** | [**[String]**](String.md)| the fields to include for returned resources of type apps | [optional] 
 **limitBuilds** | **Number**| maximum number of related builds returned (when they are included) | [optional] 

### Return type

[**PrereleaseVersionResponse**](PrereleaseVersionResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

