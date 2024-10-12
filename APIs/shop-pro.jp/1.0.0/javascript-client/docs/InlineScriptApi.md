# Api.InlineScriptApi

All URIs are relative to *https://api.shop-pro.jp*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createInlineScriptTag**](InlineScriptApi.md#createInlineScriptTag) | **POST** /v1/inline_script_tags.json | インラインスクリプトタグの登録
[**deleteInlineScriptTag**](InlineScriptApi.md#deleteInlineScriptTag) | **DELETE** /v1/inline_script_tags/{inlineScriptTagId}.json | インラインスクリプトタグの削除
[**getInlineScriptTag**](InlineScriptApi.md#getInlineScriptTag) | **GET** /v1/inline_script_tags/{inlineScriptTagId}.json | インラインスクリプトタグの取得
[**getInlineScriptTags**](InlineScriptApi.md#getInlineScriptTags) | **GET** /v1/inline_script_tags.json | インラインスクリプトタグの取得
[**updateInlineScriptTag**](InlineScriptApi.md#updateInlineScriptTag) | **PUT** /v1/inline_script_tags/{inlineScriptTagId}.json | インラインスクリプトタグの更新



## createInlineScriptTag

> CreateInlineScriptTag201Response createInlineScriptTag(opts)

インラインスクリプトタグの登録



### Example

```javascript
import Api from '_api';
let defaultClient = Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Api.InlineScriptApi();
let opts = {
  'createInlineScriptTagRequest': new Api.CreateInlineScriptTagRequest() // CreateInlineScriptTagRequest | 作成するインラインスクリプトタグの情報
};
apiInstance.createInlineScriptTag(opts, (error, data, response) => {
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
 **createInlineScriptTagRequest** | [**CreateInlineScriptTagRequest**](CreateInlineScriptTagRequest.md)| 作成するインラインスクリプトタグの情報 | [optional] 

### Return type

[**CreateInlineScriptTag201Response**](CreateInlineScriptTag201Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteInlineScriptTag

> deleteInlineScriptTag(inlineScriptTagId)

インラインスクリプトタグの削除



### Example

```javascript
import Api from '_api';
let defaultClient = Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Api.InlineScriptApi();
let inlineScriptTagId = 56; // Number | インラインスクリプトタグID
apiInstance.deleteInlineScriptTag(inlineScriptTagId, (error, data, response) => {
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
 **inlineScriptTagId** | **Number**| インラインスクリプトタグID | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getInlineScriptTag

> CreateInlineScriptTag201Response getInlineScriptTag(inlineScriptTagId)

インラインスクリプトタグの取得



### Example

```javascript
import Api from '_api';
let defaultClient = Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Api.InlineScriptApi();
let inlineScriptTagId = 56; // Number | インラインスクリプトタグID
apiInstance.getInlineScriptTag(inlineScriptTagId, (error, data, response) => {
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
 **inlineScriptTagId** | **Number**| インラインスクリプトタグID | 

### Return type

[**CreateInlineScriptTag201Response**](CreateInlineScriptTag201Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getInlineScriptTags

> GetInlineScriptTags200Response getInlineScriptTags()

インラインスクリプトタグの取得



### Example

```javascript
import Api from '_api';
let defaultClient = Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Api.InlineScriptApi();
apiInstance.getInlineScriptTags((error, data, response) => {
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

[**GetInlineScriptTags200Response**](GetInlineScriptTags200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateInlineScriptTag

> CreateInlineScriptTag201Response updateInlineScriptTag(inlineScriptTagId, opts)

インラインスクリプトタグの更新



### Example

```javascript
import Api from '_api';
let defaultClient = Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Api.InlineScriptApi();
let inlineScriptTagId = 56; // Number | インラインスクリプトタグID
let opts = {
  'createInlineScriptTagRequest': new Api.CreateInlineScriptTagRequest() // CreateInlineScriptTagRequest | 更新するスクリプトタグの情報
};
apiInstance.updateInlineScriptTag(inlineScriptTagId, opts, (error, data, response) => {
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
 **inlineScriptTagId** | **Number**| インラインスクリプトタグID | 
 **createInlineScriptTagRequest** | [**CreateInlineScriptTagRequest**](CreateInlineScriptTagRequest.md)| 更新するスクリプトタグの情報 | [optional] 

### Return type

[**CreateInlineScriptTag201Response**](CreateInlineScriptTag201Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

