# AppStoreConnectApi.BuildBetaDetailsApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**buildBetaDetailsBuildGetToOneRelated**](BuildBetaDetailsApi.md#buildBetaDetailsBuildGetToOneRelated) | **GET** /v1/buildBetaDetails/{id}/build | 
[**buildBetaDetailsGetCollection**](BuildBetaDetailsApi.md#buildBetaDetailsGetCollection) | **GET** /v1/buildBetaDetails | 
[**buildBetaDetailsGetInstance**](BuildBetaDetailsApi.md#buildBetaDetailsGetInstance) | **GET** /v1/buildBetaDetails/{id} | 
[**buildBetaDetailsUpdateInstance**](BuildBetaDetailsApi.md#buildBetaDetailsUpdateInstance) | **PATCH** /v1/buildBetaDetails/{id} | 



## buildBetaDetailsBuildGetToOneRelated

> BuildResponse buildBetaDetailsBuildGetToOneRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BuildBetaDetailsApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsBuilds': ["null"] // [String] | the fields to include for returned resources of type builds
};
apiInstance.buildBetaDetailsBuildGetToOneRelated(id, opts, (error, data, response) => {
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

### Return type

[**BuildResponse**](BuildResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## buildBetaDetailsGetCollection

> BuildBetaDetailsResponse buildBetaDetailsGetCollection(opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BuildBetaDetailsApi();
let opts = {
  'filterBuild': ["null"], // [String] | filter by id(s) of related 'build'
  'filterId': ["null"], // [String] | filter by id(s)
  'fieldsBuildBetaDetails': ["null"], // [String] | the fields to include for returned resources of type buildBetaDetails
  'limit': 56, // Number | maximum resources per page
  'include': ["null"], // [String] | comma-separated list of relationships to include
  'fieldsBuilds': ["null"] // [String] | the fields to include for returned resources of type builds
};
apiInstance.buildBetaDetailsGetCollection(opts, (error, data, response) => {
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
 **filterBuild** | [**[String]**](String.md)| filter by id(s) of related &#39;build&#39; | [optional] 
 **filterId** | [**[String]**](String.md)| filter by id(s) | [optional] 
 **fieldsBuildBetaDetails** | [**[String]**](String.md)| the fields to include for returned resources of type buildBetaDetails | [optional] 
 **limit** | **Number**| maximum resources per page | [optional] 
 **include** | [**[String]**](String.md)| comma-separated list of relationships to include | [optional] 
 **fieldsBuilds** | [**[String]**](String.md)| the fields to include for returned resources of type builds | [optional] 

### Return type

[**BuildBetaDetailsResponse**](BuildBetaDetailsResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## buildBetaDetailsGetInstance

> BuildBetaDetailResponse buildBetaDetailsGetInstance(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BuildBetaDetailsApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsBuildBetaDetails': ["null"], // [String] | the fields to include for returned resources of type buildBetaDetails
  'include': ["null"], // [String] | comma-separated list of relationships to include
  'fieldsBuilds': ["null"] // [String] | the fields to include for returned resources of type builds
};
apiInstance.buildBetaDetailsGetInstance(id, opts, (error, data, response) => {
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
 **fieldsBuildBetaDetails** | [**[String]**](String.md)| the fields to include for returned resources of type buildBetaDetails | [optional] 
 **include** | [**[String]**](String.md)| comma-separated list of relationships to include | [optional] 
 **fieldsBuilds** | [**[String]**](String.md)| the fields to include for returned resources of type builds | [optional] 

### Return type

[**BuildBetaDetailResponse**](BuildBetaDetailResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## buildBetaDetailsUpdateInstance

> BuildBetaDetailResponse buildBetaDetailsUpdateInstance(id, buildBetaDetailUpdateRequest)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BuildBetaDetailsApi();
let id = "id_example"; // String | the id of the requested resource
let buildBetaDetailUpdateRequest = new AppStoreConnectApi.BuildBetaDetailUpdateRequest(); // BuildBetaDetailUpdateRequest | BuildBetaDetail representation
apiInstance.buildBetaDetailsUpdateInstance(id, buildBetaDetailUpdateRequest, (error, data, response) => {
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
 **buildBetaDetailUpdateRequest** | [**BuildBetaDetailUpdateRequest**](BuildBetaDetailUpdateRequest.md)| BuildBetaDetail representation | 

### Return type

[**BuildBetaDetailResponse**](BuildBetaDetailResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

