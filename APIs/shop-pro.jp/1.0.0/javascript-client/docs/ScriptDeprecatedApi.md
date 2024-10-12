# Api.ScriptDeprecatedApi

All URIs are relative to *https://api.shop-pro.jp*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createScriptTag**](ScriptDeprecatedApi.md#createScriptTag) | **POST** /v1/script_tags.json | スクリプトタグの作成
[**getScriptTag**](ScriptDeprecatedApi.md#getScriptTag) | **GET** /v1/script_tags/{scriptTagId}.json | スクリプトタグの取得
[**getScriptTags**](ScriptDeprecatedApi.md#getScriptTags) | **GET** /v1/script_tags.json | スクリプトタグの取得
[**updateScriptTag**](ScriptDeprecatedApi.md#updateScriptTag) | **PUT** /v1/script_tags/{scriptTagId}.json | スクリプトタグの更新
[**v1ScriptTagsScriptTagIdJsonDelete**](ScriptDeprecatedApi.md#v1ScriptTagsScriptTagIdJsonDelete) | **DELETE** /v1/script_tags/{scriptTagId}.json | スクリプトタグの削除



## createScriptTag

> CreateScriptTag200Response createScriptTag(opts)

スクリプトタグの作成



### Example

```javascript
import Api from '_api';
let defaultClient = Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Api.ScriptDeprecatedApi();
let opts = {
  'createScriptTagRequest': new Api.CreateScriptTagRequest() // CreateScriptTagRequest | 作成するスクリプトタグの情報
};
apiInstance.createScriptTag(opts, (error, data, response) => {
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
 **createScriptTagRequest** | [**CreateScriptTagRequest**](CreateScriptTagRequest.md)| 作成するスクリプトタグの情報 | [optional] 

### Return type

[**CreateScriptTag200Response**](CreateScriptTag200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getScriptTag

> CreateScriptTag200Response getScriptTag(scriptTagId)

スクリプトタグの取得



### Example

```javascript
import Api from '_api';
let defaultClient = Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Api.ScriptDeprecatedApi();
let scriptTagId = 56; // Number | スクリプトタグID
apiInstance.getScriptTag(scriptTagId, (error, data, response) => {
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
 **scriptTagId** | **Number**| スクリプトタグID | 

### Return type

[**CreateScriptTag200Response**](CreateScriptTag200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getScriptTags

> GetScriptTags200Response getScriptTags()

スクリプトタグの取得



### Example

```javascript
import Api from '_api';
let defaultClient = Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Api.ScriptDeprecatedApi();
apiInstance.getScriptTags((error, data, response) => {
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

[**GetScriptTags200Response**](GetScriptTags200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateScriptTag

> CreateScriptTag200Response updateScriptTag(scriptTagId, opts)

スクリプトタグの更新



### Example

```javascript
import Api from '_api';
let defaultClient = Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Api.ScriptDeprecatedApi();
let scriptTagId = 56; // Number | スクリプトタグID
let opts = {
  'createScriptTagRequest': new Api.CreateScriptTagRequest() // CreateScriptTagRequest | 作成するスクリプトタグの情報
};
apiInstance.updateScriptTag(scriptTagId, opts, (error, data, response) => {
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
 **scriptTagId** | **Number**| スクリプトタグID | 
 **createScriptTagRequest** | [**CreateScriptTagRequest**](CreateScriptTagRequest.md)| 作成するスクリプトタグの情報 | [optional] 

### Return type

[**CreateScriptTag200Response**](CreateScriptTag200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## v1ScriptTagsScriptTagIdJsonDelete

> v1ScriptTagsScriptTagIdJsonDelete(scriptTagId)

スクリプトタグの削除



### Example

```javascript
import Api from '_api';
let defaultClient = Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Api.ScriptDeprecatedApi();
let scriptTagId = 56; // Number | スクリプトタグID
apiInstance.v1ScriptTagsScriptTagIdJsonDelete(scriptTagId, (error, data, response) => {
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
 **scriptTagId** | **Number**| スクリプトタグID | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

