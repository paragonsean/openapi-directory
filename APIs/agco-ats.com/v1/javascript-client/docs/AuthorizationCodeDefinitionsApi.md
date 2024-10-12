# AgcoApi.AuthorizationCodeDefinitionsApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV2AuthorizationCodeDefinitionsIdGet**](AuthorizationCodeDefinitionsApi.md#apiV2AuthorizationCodeDefinitionsIdGet) | **GET** /api/v2/AuthorizationCodeDefinitions/{id} | Get an authorization code definition by its ID
[**authorizationCodeDefinitionsAddCategoryToDefinition**](AuthorizationCodeDefinitionsApi.md#authorizationCodeDefinitionsAddCategoryToDefinition) | **POST** /api/v2/AuthorizationCodeDefinitions/{ID}/Categories/{categoryID} | Add a category to an authorizationCodeDefintion.
[**authorizationCodeDefinitionsDeleteAuthorizationCodeDefinition**](AuthorizationCodeDefinitionsApi.md#authorizationCodeDefinitionsDeleteAuthorizationCodeDefinition) | **DELETE** /api/v2/AuthorizationCodeDefinitions/{id} | Disable an authorization code definition
[**authorizationCodeDefinitionsGetAuthorizationCodeDefinition**](AuthorizationCodeDefinitionsApi.md#authorizationCodeDefinitionsGetAuthorizationCodeDefinition) | **GET** /api/v2/AuthorizationCodeDefinitions | Get authorization code definitions.
[**authorizationCodeDefinitionsPostAuthorizationCodeDefinition**](AuthorizationCodeDefinitionsApi.md#authorizationCodeDefinitionsPostAuthorizationCodeDefinition) | **POST** /api/v2/AuthorizationCodeDefinitions | Add an authorization code definition.
[**authorizationCodeDefinitionsPutAuthorizationCodeDefinition**](AuthorizationCodeDefinitionsApi.md#authorizationCodeDefinitionsPutAuthorizationCodeDefinition) | **PUT** /api/v2/AuthorizationCodeDefinitions/{id} | Update an authorization code definition
[**authorizationCodeDefinitionsRemoveCategoryFromDefinition**](AuthorizationCodeDefinitionsApi.md#authorizationCodeDefinitionsRemoveCategoryFromDefinition) | **DELETE** /api/v2/AuthorizationCodeDefinitions/{ID}/Categories/{categoryID} | Deletes the category from the authorization code definition.



## apiV2AuthorizationCodeDefinitionsIdGet

> AuthorizationCodesSharedModelsAuthorizationCodeDefinition apiV2AuthorizationCodeDefinitionsIdGet(id)

Get an authorization code definition by its ID

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AuthorizationCodeDefinitionsApi();
let id = "id_example"; // String | The ID of the authorization code definition.
apiInstance.apiV2AuthorizationCodeDefinitionsIdGet(id, (error, data, response) => {
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
 **id** | **String**| The ID of the authorization code definition. | 

### Return type

[**AuthorizationCodesSharedModelsAuthorizationCodeDefinition**](AuthorizationCodesSharedModelsAuthorizationCodeDefinition.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## authorizationCodeDefinitionsAddCategoryToDefinition

> authorizationCodeDefinitionsAddCategoryToDefinition(ID, categoryID)

Add a category to an authorizationCodeDefintion.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AuthorizationCodeDefinitionsApi();
let ID = "ID_example"; // String | 
let categoryID = "categoryID_example"; // String | A category ID, as a GUID.
apiInstance.authorizationCodeDefinitionsAddCategoryToDefinition(ID, categoryID, (error, data, response) => {
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
 **ID** | **String**|  | 
 **categoryID** | **String**| A category ID, as a GUID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## authorizationCodeDefinitionsDeleteAuthorizationCodeDefinition

> authorizationCodeDefinitionsDeleteAuthorizationCodeDefinition(id)

Disable an authorization code definition

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AuthorizationCodeDefinitionsApi();
let id = "id_example"; // String | The ID of the authorization code definition.
apiInstance.authorizationCodeDefinitionsDeleteAuthorizationCodeDefinition(id, (error, data, response) => {
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
 **id** | **String**| The ID of the authorization code definition. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## authorizationCodeDefinitionsGetAuthorizationCodeDefinition

> APIIPagedResponseAuthorizationCodesSharedModelsAuthorizationCodeDefinition authorizationCodeDefinitionsGetAuthorizationCodeDefinition(opts)

Get authorization code definitions.

Additional searches: validationFields[Name]&#x3D;true and dataFields[Name]&#x3D;true. These can be used to search for authorization code definitions that have the specified data or validation fields.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AuthorizationCodeDefinitionsApi();
let opts = {
  'limit': 56, // Number | Optional. The page limit.  If not specified, the default page limit is 10.
  'offset': 56, // Number | Optional. The page offset.  If not specified, the default page offset is 0.
  'name': "name_example", // String | Optional. If specified, filters definitions by name. Starting and ending wildcards (*) supported.
  'createdByUserID': 56, // Number | Optional. If specified, filters definitions to those created by the given User ID.
  'deletedByUserID': 56, // Number | Optional. If specified, filters definitions to those deleted by the given User ID.
  'includeDeleted': true, // Boolean | Optional. Whether to include deleted definitions. 'False' by default.
  'categoryID': "categoryID_example" // String | Optional. If specified, filters definitions with the designated categoryID.
};
apiInstance.authorizationCodeDefinitionsGetAuthorizationCodeDefinition(opts, (error, data, response) => {
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
 **limit** | **Number**| Optional. The page limit.  If not specified, the default page limit is 10. | [optional] 
 **offset** | **Number**| Optional. The page offset.  If not specified, the default page offset is 0. | [optional] 
 **name** | **String**| Optional. If specified, filters definitions by name. Starting and ending wildcards (*) supported. | [optional] 
 **createdByUserID** | **Number**| Optional. If specified, filters definitions to those created by the given User ID. | [optional] 
 **deletedByUserID** | **Number**| Optional. If specified, filters definitions to those deleted by the given User ID. | [optional] 
 **includeDeleted** | **Boolean**| Optional. Whether to include deleted definitions. &#39;False&#39; by default. | [optional] 
 **categoryID** | **String**| Optional. If specified, filters definitions with the designated categoryID. | [optional] 

### Return type

[**APIIPagedResponseAuthorizationCodesSharedModelsAuthorizationCodeDefinition**](APIIPagedResponseAuthorizationCodesSharedModelsAuthorizationCodeDefinition.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## authorizationCodeDefinitionsPostAuthorizationCodeDefinition

> String authorizationCodeDefinitionsPostAuthorizationCodeDefinition(authorizationCodesSharedModelsAuthorizationCodeDefinition)

Add an authorization code definition.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AuthorizationCodeDefinitionsApi();
let authorizationCodesSharedModelsAuthorizationCodeDefinition = new AgcoApi.AuthorizationCodesSharedModelsAuthorizationCodeDefinition(); // AuthorizationCodesSharedModelsAuthorizationCodeDefinition | An authorization code definition.
apiInstance.authorizationCodeDefinitionsPostAuthorizationCodeDefinition(authorizationCodesSharedModelsAuthorizationCodeDefinition, (error, data, response) => {
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
 **authorizationCodesSharedModelsAuthorizationCodeDefinition** | [**AuthorizationCodesSharedModelsAuthorizationCodeDefinition**](AuthorizationCodesSharedModelsAuthorizationCodeDefinition.md)| An authorization code definition. | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## authorizationCodeDefinitionsPutAuthorizationCodeDefinition

> authorizationCodeDefinitionsPutAuthorizationCodeDefinition(id, authorizationCodesSharedModelsAuthorizationCodeDefinition)

Update an authorization code definition

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AuthorizationCodeDefinitionsApi();
let id = "id_example"; // String | The ID of the authorization code definition.
let authorizationCodesSharedModelsAuthorizationCodeDefinition = new AgcoApi.AuthorizationCodesSharedModelsAuthorizationCodeDefinition(); // AuthorizationCodesSharedModelsAuthorizationCodeDefinition | An authorization code definition.
apiInstance.authorizationCodeDefinitionsPutAuthorizationCodeDefinition(id, authorizationCodesSharedModelsAuthorizationCodeDefinition, (error, data, response) => {
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
 **id** | **String**| The ID of the authorization code definition. | 
 **authorizationCodesSharedModelsAuthorizationCodeDefinition** | [**AuthorizationCodesSharedModelsAuthorizationCodeDefinition**](AuthorizationCodesSharedModelsAuthorizationCodeDefinition.md)| An authorization code definition. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*


## authorizationCodeDefinitionsRemoveCategoryFromDefinition

> authorizationCodeDefinitionsRemoveCategoryFromDefinition(ID, categoryID)

Deletes the category from the authorization code definition.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AuthorizationCodeDefinitionsApi();
let ID = "ID_example"; // String | 
let categoryID = "categoryID_example"; // String | A category ID, as a GUID.
apiInstance.authorizationCodeDefinitionsRemoveCategoryFromDefinition(ID, categoryID, (error, data, response) => {
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
 **ID** | **String**|  | 
 **categoryID** | **String**| A category ID, as a GUID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

