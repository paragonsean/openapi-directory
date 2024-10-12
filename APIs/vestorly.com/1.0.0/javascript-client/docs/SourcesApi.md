# VestorlyApi.SourcesApi

All URIs are relative to *https://staging.vestorly.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSource**](SourcesApi.md#createSource) | **POST** /sources | 
[**findSources**](SourcesApi.md#findSources) | **GET** /sources | 
[**getSourceByID**](SourcesApi.md#getSourceByID) | **GET** /sources/{id} | 
[**updateSourceByID**](SourcesApi.md#updateSourceByID) | **PUT** /sources/{id} | 



## createSource

> Sourceresponse createSource(vestorlyAuth, source, opts)



Create source

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.SourcesApi();
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let source = new VestorlyApi.SourceInput(); // SourceInput | Source
let opts = {
  'accessToken': "accessToken_example" // String | OAuth Token
};
apiInstance.createSource(vestorlyAuth, source, opts, (error, data, response) => {
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
 **vestorlyAuth** | **String**| Vestorly Auth Token | 
 **source** | [**SourceInput**](SourceInput.md)| Source | 
 **accessToken** | **String**| OAuth Token | [optional] 

### Return type

[**Sourceresponse**](Sourceresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## findSources

> Sources findSources(vestorlyAuth, opts)



Returns all sources

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.SourcesApi();
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let opts = {
  'accessToken': "accessToken_example" // String | OAuth Token
};
apiInstance.findSources(vestorlyAuth, opts, (error, data, response) => {
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
 **vestorlyAuth** | **String**| Vestorly Auth Token | 
 **accessToken** | **String**| OAuth Token | [optional] 

### Return type

[**Sources**](Sources.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getSourceByID

> Sourceresponse getSourceByID(vestorlyAuth, id, opts)



Get Source By ID

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.SourcesApi();
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let id = "id_example"; // String | ID of source to fetch
let opts = {
  'accessToken': "accessToken_example" // String | OAuth Token
};
apiInstance.getSourceByID(vestorlyAuth, id, opts, (error, data, response) => {
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
 **vestorlyAuth** | **String**| Vestorly Auth Token | 
 **id** | **String**| ID of source to fetch | 
 **accessToken** | **String**| OAuth Token | [optional] 

### Return type

[**Sourceresponse**](Sourceresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## updateSourceByID

> Sourceresponse updateSourceByID(vestorlyAuth, id, source, opts)



Update Source By ID

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.SourcesApi();
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let id = "id_example"; // String | ID of source to fetch
let source = new VestorlyApi.SourceInput(); // SourceInput | Source
let opts = {
  'accessToken': "accessToken_example" // String | OAuth Token
};
apiInstance.updateSourceByID(vestorlyAuth, id, source, opts, (error, data, response) => {
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
 **vestorlyAuth** | **String**| Vestorly Auth Token | 
 **id** | **String**| ID of source to fetch | 
 **source** | [**SourceInput**](SourceInput.md)| Source | 
 **accessToken** | **String**| OAuth Token | [optional] 

### Return type

[**Sourceresponse**](Sourceresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

