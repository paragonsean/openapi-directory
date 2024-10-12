# AppStoreConnectApi.BundleIdsApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bundleIdsAppGetToOneRelated**](BundleIdsApi.md#bundleIdsAppGetToOneRelated) | **GET** /v1/bundleIds/{id}/app | 
[**bundleIdsBundleIdCapabilitiesGetToManyRelated**](BundleIdsApi.md#bundleIdsBundleIdCapabilitiesGetToManyRelated) | **GET** /v1/bundleIds/{id}/bundleIdCapabilities | 
[**bundleIdsCreateInstance**](BundleIdsApi.md#bundleIdsCreateInstance) | **POST** /v1/bundleIds | 
[**bundleIdsDeleteInstance**](BundleIdsApi.md#bundleIdsDeleteInstance) | **DELETE** /v1/bundleIds/{id} | 
[**bundleIdsGetCollection**](BundleIdsApi.md#bundleIdsGetCollection) | **GET** /v1/bundleIds | 
[**bundleIdsGetInstance**](BundleIdsApi.md#bundleIdsGetInstance) | **GET** /v1/bundleIds/{id} | 
[**bundleIdsProfilesGetToManyRelated**](BundleIdsApi.md#bundleIdsProfilesGetToManyRelated) | **GET** /v1/bundleIds/{id}/profiles | 
[**bundleIdsUpdateInstance**](BundleIdsApi.md#bundleIdsUpdateInstance) | **PATCH** /v1/bundleIds/{id} | 



## bundleIdsAppGetToOneRelated

> AppResponse bundleIdsAppGetToOneRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BundleIdsApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsApps': ["null"] // [String] | the fields to include for returned resources of type apps
};
apiInstance.bundleIdsAppGetToOneRelated(id, opts, (error, data, response) => {
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


## bundleIdsBundleIdCapabilitiesGetToManyRelated

> BundleIdCapabilitiesResponse bundleIdsBundleIdCapabilitiesGetToManyRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BundleIdsApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsBundleIdCapabilities': ["null"], // [String] | the fields to include for returned resources of type bundleIdCapabilities
  'limit': 56 // Number | maximum resources per page
};
apiInstance.bundleIdsBundleIdCapabilitiesGetToManyRelated(id, opts, (error, data, response) => {
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
 **fieldsBundleIdCapabilities** | [**[String]**](String.md)| the fields to include for returned resources of type bundleIdCapabilities | [optional] 
 **limit** | **Number**| maximum resources per page | [optional] 

### Return type

[**BundleIdCapabilitiesResponse**](BundleIdCapabilitiesResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## bundleIdsCreateInstance

> BundleIdResponse bundleIdsCreateInstance(bundleIdCreateRequest)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BundleIdsApi();
let bundleIdCreateRequest = new AppStoreConnectApi.BundleIdCreateRequest(); // BundleIdCreateRequest | BundleId representation
apiInstance.bundleIdsCreateInstance(bundleIdCreateRequest, (error, data, response) => {
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
 **bundleIdCreateRequest** | [**BundleIdCreateRequest**](BundleIdCreateRequest.md)| BundleId representation | 

### Return type

[**BundleIdResponse**](BundleIdResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bundleIdsDeleteInstance

> bundleIdsDeleteInstance(id)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BundleIdsApi();
let id = "id_example"; // String | the id of the requested resource
apiInstance.bundleIdsDeleteInstance(id, (error, data, response) => {
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


## bundleIdsGetCollection

> BundleIdsResponse bundleIdsGetCollection(opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BundleIdsApi();
let opts = {
  'filterIdentifier': ["null"], // [String] | filter by attribute 'identifier'
  'filterName': ["null"], // [String] | filter by attribute 'name'
  'filterPlatform': ["null"], // [String] | filter by attribute 'platform'
  'filterSeedId': ["null"], // [String] | filter by attribute 'seedId'
  'filterId': ["null"], // [String] | filter by id(s)
  'sort': ["null"], // [String] | comma-separated list of sort expressions; resources will be sorted as specified
  'fieldsBundleIds': ["null"], // [String] | the fields to include for returned resources of type bundleIds
  'limit': 56, // Number | maximum resources per page
  'include': ["null"], // [String] | comma-separated list of relationships to include
  'fieldsBundleIdCapabilities': ["null"], // [String] | the fields to include for returned resources of type bundleIdCapabilities
  'fieldsProfiles': ["null"], // [String] | the fields to include for returned resources of type profiles
  'fieldsApps': ["null"], // [String] | the fields to include for returned resources of type apps
  'limitBundleIdCapabilities': 56, // Number | maximum number of related bundleIdCapabilities returned (when they are included)
  'limitProfiles': 56 // Number | maximum number of related profiles returned (when they are included)
};
apiInstance.bundleIdsGetCollection(opts, (error, data, response) => {
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
 **filterIdentifier** | [**[String]**](String.md)| filter by attribute &#39;identifier&#39; | [optional] 
 **filterName** | [**[String]**](String.md)| filter by attribute &#39;name&#39; | [optional] 
 **filterPlatform** | [**[String]**](String.md)| filter by attribute &#39;platform&#39; | [optional] 
 **filterSeedId** | [**[String]**](String.md)| filter by attribute &#39;seedId&#39; | [optional] 
 **filterId** | [**[String]**](String.md)| filter by id(s) | [optional] 
 **sort** | [**[String]**](String.md)| comma-separated list of sort expressions; resources will be sorted as specified | [optional] 
 **fieldsBundleIds** | [**[String]**](String.md)| the fields to include for returned resources of type bundleIds | [optional] 
 **limit** | **Number**| maximum resources per page | [optional] 
 **include** | [**[String]**](String.md)| comma-separated list of relationships to include | [optional] 
 **fieldsBundleIdCapabilities** | [**[String]**](String.md)| the fields to include for returned resources of type bundleIdCapabilities | [optional] 
 **fieldsProfiles** | [**[String]**](String.md)| the fields to include for returned resources of type profiles | [optional] 
 **fieldsApps** | [**[String]**](String.md)| the fields to include for returned resources of type apps | [optional] 
 **limitBundleIdCapabilities** | **Number**| maximum number of related bundleIdCapabilities returned (when they are included) | [optional] 
 **limitProfiles** | **Number**| maximum number of related profiles returned (when they are included) | [optional] 

### Return type

[**BundleIdsResponse**](BundleIdsResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## bundleIdsGetInstance

> BundleIdResponse bundleIdsGetInstance(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BundleIdsApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsBundleIds': ["null"], // [String] | the fields to include for returned resources of type bundleIds
  'include': ["null"], // [String] | comma-separated list of relationships to include
  'fieldsBundleIdCapabilities': ["null"], // [String] | the fields to include for returned resources of type bundleIdCapabilities
  'fieldsProfiles': ["null"], // [String] | the fields to include for returned resources of type profiles
  'fieldsApps': ["null"], // [String] | the fields to include for returned resources of type apps
  'limitBundleIdCapabilities': 56, // Number | maximum number of related bundleIdCapabilities returned (when they are included)
  'limitProfiles': 56 // Number | maximum number of related profiles returned (when they are included)
};
apiInstance.bundleIdsGetInstance(id, opts, (error, data, response) => {
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
 **fieldsBundleIds** | [**[String]**](String.md)| the fields to include for returned resources of type bundleIds | [optional] 
 **include** | [**[String]**](String.md)| comma-separated list of relationships to include | [optional] 
 **fieldsBundleIdCapabilities** | [**[String]**](String.md)| the fields to include for returned resources of type bundleIdCapabilities | [optional] 
 **fieldsProfiles** | [**[String]**](String.md)| the fields to include for returned resources of type profiles | [optional] 
 **fieldsApps** | [**[String]**](String.md)| the fields to include for returned resources of type apps | [optional] 
 **limitBundleIdCapabilities** | **Number**| maximum number of related bundleIdCapabilities returned (when they are included) | [optional] 
 **limitProfiles** | **Number**| maximum number of related profiles returned (when they are included) | [optional] 

### Return type

[**BundleIdResponse**](BundleIdResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## bundleIdsProfilesGetToManyRelated

> ProfilesResponse bundleIdsProfilesGetToManyRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BundleIdsApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsProfiles': ["null"], // [String] | the fields to include for returned resources of type profiles
  'limit': 56 // Number | maximum resources per page
};
apiInstance.bundleIdsProfilesGetToManyRelated(id, opts, (error, data, response) => {
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
 **fieldsProfiles** | [**[String]**](String.md)| the fields to include for returned resources of type profiles | [optional] 
 **limit** | **Number**| maximum resources per page | [optional] 

### Return type

[**ProfilesResponse**](ProfilesResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## bundleIdsUpdateInstance

> BundleIdResponse bundleIdsUpdateInstance(id, bundleIdUpdateRequest)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BundleIdsApi();
let id = "id_example"; // String | the id of the requested resource
let bundleIdUpdateRequest = new AppStoreConnectApi.BundleIdUpdateRequest(); // BundleIdUpdateRequest | BundleId representation
apiInstance.bundleIdsUpdateInstance(id, bundleIdUpdateRequest, (error, data, response) => {
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
 **bundleIdUpdateRequest** | [**BundleIdUpdateRequest**](BundleIdUpdateRequest.md)| BundleId representation | 

### Return type

[**BundleIdResponse**](BundleIdResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

