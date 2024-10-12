# Api.ScriptApi

All URIs are relative to *https://api.shop-pro.jp*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createShopScriptTag**](ScriptApi.md#createShopScriptTag) | **POST** /appstore/v1/script_tags.json | スクリプトタグの作成
[**deleteScriptTag**](ScriptApi.md#deleteScriptTag) | **DELETE** /appstore/v1/script_tags/{scriptTagId}.json | スクリプトタグの削除
[**getShopScriptTag**](ScriptApi.md#getShopScriptTag) | **GET** /appstore/v1/script_tags/{scriptTagId}.json | スクリプトタグの取得
[**getShopScriptTags**](ScriptApi.md#getShopScriptTags) | **GET** /appstore/v1/script_tags.json | スクリプトタグの取得
[**updateShopScriptTag**](ScriptApi.md#updateShopScriptTag) | **PUT** /appstore/v1/script_tags/{scriptTagId}.json | スクリプトタグの更新



## createShopScriptTag

> CreateShopScriptTag200Response createShopScriptTag(opts)

スクリプトタグの作成



### Example

```javascript
import Api from '_api';
let defaultClient = Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Api.ScriptApi();
let opts = {
  'createShopScriptTagRequest': new Api.CreateShopScriptTagRequest() // CreateShopScriptTagRequest | 作成するスクリプトタグの情報
};
apiInstance.createShopScriptTag(opts, (error, data, response) => {
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
 **createShopScriptTagRequest** | [**CreateShopScriptTagRequest**](CreateShopScriptTagRequest.md)| 作成するスクリプトタグの情報 | [optional] 

### Return type

[**CreateShopScriptTag200Response**](CreateShopScriptTag200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteScriptTag

> deleteScriptTag(scriptTagId)

スクリプトタグの削除



### Example

```javascript
import Api from '_api';
let defaultClient = Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Api.ScriptApi();
let scriptTagId = 56; // Number | スクリプトタグID
apiInstance.deleteScriptTag(scriptTagId, (error, data, response) => {
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


## getShopScriptTag

> CreateShopScriptTag200Response getShopScriptTag(scriptTagId)

スクリプトタグの取得



### Example

```javascript
import Api from '_api';
let defaultClient = Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Api.ScriptApi();
let scriptTagId = 56; // Number | スクリプトタグID
apiInstance.getShopScriptTag(scriptTagId, (error, data, response) => {
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

[**CreateShopScriptTag200Response**](CreateShopScriptTag200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getShopScriptTags

> GetShopScriptTags200Response getShopScriptTags()

スクリプトタグの取得



### Example

```javascript
import Api from '_api';
let defaultClient = Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Api.ScriptApi();
apiInstance.getShopScriptTags((error, data, response) => {
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

[**GetShopScriptTags200Response**](GetShopScriptTags200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateShopScriptTag

> CreateShopScriptTag200Response updateShopScriptTag(scriptTagId, opts)

スクリプトタグの更新



### Example

```javascript
import Api from '_api';
let defaultClient = Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Api.ScriptApi();
let scriptTagId = 56; // Number | スクリプトタグID
let opts = {
  'createShopScriptTagRequest': new Api.CreateShopScriptTagRequest() // CreateShopScriptTagRequest | 作成するスクリプトタグの情報
};
apiInstance.updateShopScriptTag(scriptTagId, opts, (error, data, response) => {
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
 **createShopScriptTagRequest** | [**CreateShopScriptTagRequest**](CreateShopScriptTagRequest.md)| 作成するスクリプトタグの情報 | [optional] 

### Return type

[**CreateShopScriptTag200Response**](CreateShopScriptTag200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

