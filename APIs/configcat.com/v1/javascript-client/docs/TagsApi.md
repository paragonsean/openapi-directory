# ConfigCatPublicManagementApi.TagsApi

All URIs are relative to *https://api.configcat.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createTag**](TagsApi.md#createTag) | **POST** /v1/products/{productId}/tags | Create Tag
[**deleteTag**](TagsApi.md#deleteTag) | **DELETE** /v1/tags/{tagId} | Delete Tag
[**getSettingsByTag**](TagsApi.md#getSettingsByTag) | **GET** /v1/tags/{tagId}/settings | List Settings by Tag
[**getTag**](TagsApi.md#getTag) | **GET** /v1/tags/{tagId} | Get Tag
[**getTags**](TagsApi.md#getTags) | **GET** /v1/products/{productId}/tags | List Tags
[**updateTag**](TagsApi.md#updateTag) | **PUT** /v1/tags/{tagId} | Update Tag



## createTag

> TagModelHaljson createTag(productId, createTagModel)

Create Tag

This endpoint creates a new Tag in a specified Product  identified by the &#x60;productId&#x60; parameter, which can be obtained from the [List Products](#operation/get-products) endpoint.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.TagsApi();
let productId = "productId_example"; // String | The identifier of the Organization.
let createTagModel = new ConfigCatPublicManagementApi.CreateTagModel(); // CreateTagModel | 
apiInstance.createTag(productId, createTagModel, (error, data, response) => {
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
 **productId** | **String**| The identifier of the Organization. | 
 **createTagModel** | [**CreateTagModel**](CreateTagModel.md)|  | 

### Return type

[**TagModelHaljson**](TagModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/hal+json, application/json


## deleteTag

> deleteTag(tagId)

Delete Tag

This endpoint deletes a Tag identified by the &#x60;tagId&#x60; parameter. To remove a Tag from a Feature Flag or Setting use the [Update Flag](#operation/update-setting) endpoint.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.TagsApi();
let tagId = 789; // Number | The identifier of the Tag.
apiInstance.deleteTag(tagId, (error, data, response) => {
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
 **tagId** | **Number**| The identifier of the Tag. | 

### Return type

null (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getSettingsByTag

> [SettingModelHaljson] getSettingsByTag(tagId)

List Settings by Tag

This endpoint returns the list of the Settings that  has the specified Tag, identified by the &#x60;tagId&#x60; parameter.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.TagsApi();
let tagId = 789; // Number | The identifier of the Tag.
apiInstance.getSettingsByTag(tagId, (error, data, response) => {
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
 **tagId** | **Number**| The identifier of the Tag. | 

### Return type

[**[SettingModelHaljson]**](SettingModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json, application/json


## getTag

> TagModelHaljson getTag(tagId)

Get Tag

This endpoint returns the metadata of a Tag  identified by the &#x60;tagId&#x60;.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.TagsApi();
let tagId = 789; // Number | The identifier of the Tag.
apiInstance.getTag(tagId, (error, data, response) => {
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
 **tagId** | **Number**| The identifier of the Tag. | 

### Return type

[**TagModelHaljson**](TagModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json, application/json


## getTags

> [TagModelHaljson] getTags(productId)

List Tags

This endpoint returns the list of the Tags in a  specified Product, identified by the &#x60;productId&#x60; parameter.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.TagsApi();
let productId = "productId_example"; // String | The identifier of the Product.
apiInstance.getTags(productId, (error, data, response) => {
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
 **productId** | **String**| The identifier of the Product. | 

### Return type

[**[TagModelHaljson]**](TagModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json, application/json


## updateTag

> TagModelHaljson updateTag(tagId, updateTagModel)

Update Tag

This endpoint updates a Tag identified by the &#x60;tagId&#x60; parameter.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.TagsApi();
let tagId = 789; // Number | The identifier of the Tag.
let updateTagModel = new ConfigCatPublicManagementApi.UpdateTagModel(); // UpdateTagModel | 
apiInstance.updateTag(tagId, updateTagModel, (error, data, response) => {
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
 **tagId** | **Number**| The identifier of the Tag. | 
 **updateTagModel** | [**UpdateTagModel**](UpdateTagModel.md)|  | 

### Return type

[**TagModelHaljson**](TagModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/hal+json, application/json

