# AppStoreConnectApi.ProfilesApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**profilesBundleIdGetToOneRelated**](ProfilesApi.md#profilesBundleIdGetToOneRelated) | **GET** /v1/profiles/{id}/bundleId | 
[**profilesCertificatesGetToManyRelated**](ProfilesApi.md#profilesCertificatesGetToManyRelated) | **GET** /v1/profiles/{id}/certificates | 
[**profilesCreateInstance**](ProfilesApi.md#profilesCreateInstance) | **POST** /v1/profiles | 
[**profilesDeleteInstance**](ProfilesApi.md#profilesDeleteInstance) | **DELETE** /v1/profiles/{id} | 
[**profilesDevicesGetToManyRelated**](ProfilesApi.md#profilesDevicesGetToManyRelated) | **GET** /v1/profiles/{id}/devices | 
[**profilesGetCollection**](ProfilesApi.md#profilesGetCollection) | **GET** /v1/profiles | 
[**profilesGetInstance**](ProfilesApi.md#profilesGetInstance) | **GET** /v1/profiles/{id} | 



## profilesBundleIdGetToOneRelated

> BundleIdResponse profilesBundleIdGetToOneRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.ProfilesApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsBundleIds': ["null"] // [String] | the fields to include for returned resources of type bundleIds
};
apiInstance.profilesBundleIdGetToOneRelated(id, opts, (error, data, response) => {
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

### Return type

[**BundleIdResponse**](BundleIdResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## profilesCertificatesGetToManyRelated

> CertificatesResponse profilesCertificatesGetToManyRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.ProfilesApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsCertificates': ["null"], // [String] | the fields to include for returned resources of type certificates
  'limit': 56 // Number | maximum resources per page
};
apiInstance.profilesCertificatesGetToManyRelated(id, opts, (error, data, response) => {
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
 **fieldsCertificates** | [**[String]**](String.md)| the fields to include for returned resources of type certificates | [optional] 
 **limit** | **Number**| maximum resources per page | [optional] 

### Return type

[**CertificatesResponse**](CertificatesResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## profilesCreateInstance

> ProfileResponse profilesCreateInstance(profileCreateRequest)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.ProfilesApi();
let profileCreateRequest = new AppStoreConnectApi.ProfileCreateRequest(); // ProfileCreateRequest | Profile representation
apiInstance.profilesCreateInstance(profileCreateRequest, (error, data, response) => {
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
 **profileCreateRequest** | [**ProfileCreateRequest**](ProfileCreateRequest.md)| Profile representation | 

### Return type

[**ProfileResponse**](ProfileResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## profilesDeleteInstance

> profilesDeleteInstance(id)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.ProfilesApi();
let id = "id_example"; // String | the id of the requested resource
apiInstance.profilesDeleteInstance(id, (error, data, response) => {
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


## profilesDevicesGetToManyRelated

> DevicesResponse profilesDevicesGetToManyRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.ProfilesApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsDevices': ["null"], // [String] | the fields to include for returned resources of type devices
  'limit': 56 // Number | maximum resources per page
};
apiInstance.profilesDevicesGetToManyRelated(id, opts, (error, data, response) => {
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
 **fieldsDevices** | [**[String]**](String.md)| the fields to include for returned resources of type devices | [optional] 
 **limit** | **Number**| maximum resources per page | [optional] 

### Return type

[**DevicesResponse**](DevicesResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## profilesGetCollection

> ProfilesResponse profilesGetCollection(opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.ProfilesApi();
let opts = {
  'filterName': ["null"], // [String] | filter by attribute 'name'
  'filterProfileState': ["null"], // [String] | filter by attribute 'profileState'
  'filterProfileType': ["null"], // [String] | filter by attribute 'profileType'
  'filterId': ["null"], // [String] | filter by id(s)
  'sort': ["null"], // [String] | comma-separated list of sort expressions; resources will be sorted as specified
  'fieldsProfiles': ["null"], // [String] | the fields to include for returned resources of type profiles
  'limit': 56, // Number | maximum resources per page
  'include': ["null"], // [String] | comma-separated list of relationships to include
  'fieldsCertificates': ["null"], // [String] | the fields to include for returned resources of type certificates
  'fieldsDevices': ["null"], // [String] | the fields to include for returned resources of type devices
  'fieldsBundleIds': ["null"], // [String] | the fields to include for returned resources of type bundleIds
  'limitCertificates': 56, // Number | maximum number of related certificates returned (when they are included)
  'limitDevices': 56 // Number | maximum number of related devices returned (when they are included)
};
apiInstance.profilesGetCollection(opts, (error, data, response) => {
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
 **filterName** | [**[String]**](String.md)| filter by attribute &#39;name&#39; | [optional] 
 **filterProfileState** | [**[String]**](String.md)| filter by attribute &#39;profileState&#39; | [optional] 
 **filterProfileType** | [**[String]**](String.md)| filter by attribute &#39;profileType&#39; | [optional] 
 **filterId** | [**[String]**](String.md)| filter by id(s) | [optional] 
 **sort** | [**[String]**](String.md)| comma-separated list of sort expressions; resources will be sorted as specified | [optional] 
 **fieldsProfiles** | [**[String]**](String.md)| the fields to include for returned resources of type profiles | [optional] 
 **limit** | **Number**| maximum resources per page | [optional] 
 **include** | [**[String]**](String.md)| comma-separated list of relationships to include | [optional] 
 **fieldsCertificates** | [**[String]**](String.md)| the fields to include for returned resources of type certificates | [optional] 
 **fieldsDevices** | [**[String]**](String.md)| the fields to include for returned resources of type devices | [optional] 
 **fieldsBundleIds** | [**[String]**](String.md)| the fields to include for returned resources of type bundleIds | [optional] 
 **limitCertificates** | **Number**| maximum number of related certificates returned (when they are included) | [optional] 
 **limitDevices** | **Number**| maximum number of related devices returned (when they are included) | [optional] 

### Return type

[**ProfilesResponse**](ProfilesResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## profilesGetInstance

> ProfileResponse profilesGetInstance(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.ProfilesApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsProfiles': ["null"], // [String] | the fields to include for returned resources of type profiles
  'include': ["null"], // [String] | comma-separated list of relationships to include
  'fieldsCertificates': ["null"], // [String] | the fields to include for returned resources of type certificates
  'fieldsDevices': ["null"], // [String] | the fields to include for returned resources of type devices
  'fieldsBundleIds': ["null"], // [String] | the fields to include for returned resources of type bundleIds
  'limitCertificates': 56, // Number | maximum number of related certificates returned (when they are included)
  'limitDevices': 56 // Number | maximum number of related devices returned (when they are included)
};
apiInstance.profilesGetInstance(id, opts, (error, data, response) => {
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
 **include** | [**[String]**](String.md)| comma-separated list of relationships to include | [optional] 
 **fieldsCertificates** | [**[String]**](String.md)| the fields to include for returned resources of type certificates | [optional] 
 **fieldsDevices** | [**[String]**](String.md)| the fields to include for returned resources of type devices | [optional] 
 **fieldsBundleIds** | [**[String]**](String.md)| the fields to include for returned resources of type bundleIds | [optional] 
 **limitCertificates** | **Number**| maximum number of related certificates returned (when they are included) | [optional] 
 **limitDevices** | **Number**| maximum number of related devices returned (when they are included) | [optional] 

### Return type

[**ProfileResponse**](ProfileResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

