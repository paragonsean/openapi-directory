# AgcoApi.AuthorizationCodesApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorizationCodesDeleteAuthorizationCode**](AuthorizationCodesApi.md#authorizationCodesDeleteAuthorizationCode) | **DELETE** /api/v2/AuthorizationCodes/{id} | Hide an authorization code.
[**authorizationCodesGetAuthorizationCode**](AuthorizationCodesApi.md#authorizationCodesGetAuthorizationCode) | **GET** /api/v2/AuthorizationCodes/{id} | Get an authorization code by its ID.
[**authorizationCodesGetAuthorizationCodes**](AuthorizationCodesApi.md#authorizationCodesGetAuthorizationCodes) | **GET** /api/v2/AuthorizationCodes | Get authorization codes.
[**authorizationCodesGetContactInformation**](AuthorizationCodesApi.md#authorizationCodesGetContactInformation) | **GET** /api/v2/AuthorizationCodes/{id}/ContactInformation | Get contact information for an authorization code.
[**authorizationCodesPostAuthorizationCode**](AuthorizationCodesApi.md#authorizationCodesPostAuthorizationCode) | **POST** /api/v2/AuthorizationCodes | Generates an authorization code using the provided definition and parameters.
[**authorizationCodesPutAuthorizationCode**](AuthorizationCodesApi.md#authorizationCodesPutAuthorizationCode) | **PUT** /api/v2/AuthorizationCodes/{id} | Update an authorization code.
[**authorizationCodesValidateAuthorizationCode**](AuthorizationCodesApi.md#authorizationCodesValidateAuthorizationCode) | **GET** /api/v2/AuthorizationCodes/{id}/Validate | No Documentation Found.



## authorizationCodesDeleteAuthorizationCode

> authorizationCodesDeleteAuthorizationCode(id)

Hide an authorization code.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AuthorizationCodesApi();
let id = 56; // Number | The id of the authorization code.
apiInstance.authorizationCodesDeleteAuthorizationCode(id, (error, data, response) => {
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
 **id** | **Number**| The id of the authorization code. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## authorizationCodesGetAuthorizationCode

> AuthorizationCodesSharedModelsAuthorizationCode authorizationCodesGetAuthorizationCode(id)

Get an authorization code by its ID.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AuthorizationCodesApi();
let id = 56; // Number | The id of the authorization code.
apiInstance.authorizationCodesGetAuthorizationCode(id, (error, data, response) => {
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
 **id** | **Number**| The id of the authorization code. | 

### Return type

[**AuthorizationCodesSharedModelsAuthorizationCode**](AuthorizationCodesSharedModelsAuthorizationCode.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## authorizationCodesGetAuthorizationCodes

> APIIPagedResponseAuthorizationCodesSharedModelsAuthorizationCode authorizationCodesGetAuthorizationCodes(opts)

Get authorization codes.

Additional searches: validationParameters[Name]&#x3D;Value and dataParameters[Name]&#x3D;Value. These can be used to search for authorization codes that have been generated using specified values for data or validation parameters.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AuthorizationCodesApi();
let opts = {
  'code': "code_example", // String | Optional. If provided, searches for entities with the provided authorization code.
  'limit': 56, // Number | Optional. The page limit.  If not specified, the default page limit is 10.
  'offset': 56, // Number | Optional. The page offset.  If not specified, the default page offset is 0.
  'definitionID': "definitionID_example", // String | Optional. If specified, filters codes by definition id.
  'createdByUserID': 56, // Number | Optional. If specified, filters codes to those created by the given User ID.
  'deletedByUserID': 56, // Number | Optional. If specified, filters codes to those deleted by the given User ID.
  'includeDeleted': true // Boolean | Optional. Whether to include deleted codes. 'False' by default.
};
apiInstance.authorizationCodesGetAuthorizationCodes(opts, (error, data, response) => {
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
 **code** | **String**| Optional. If provided, searches for entities with the provided authorization code. | [optional] 
 **limit** | **Number**| Optional. The page limit.  If not specified, the default page limit is 10. | [optional] 
 **offset** | **Number**| Optional. The page offset.  If not specified, the default page offset is 0. | [optional] 
 **definitionID** | **String**| Optional. If specified, filters codes by definition id. | [optional] 
 **createdByUserID** | **Number**| Optional. If specified, filters codes to those created by the given User ID. | [optional] 
 **deletedByUserID** | **Number**| Optional. If specified, filters codes to those deleted by the given User ID. | [optional] 
 **includeDeleted** | **Boolean**| Optional. Whether to include deleted codes. &#39;False&#39; by default. | [optional] 

### Return type

[**APIIPagedResponseAuthorizationCodesSharedModelsAuthorizationCode**](APIIPagedResponseAuthorizationCodesSharedModelsAuthorizationCode.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## authorizationCodesGetContactInformation

> AuthorizationCodesSharedModelsAuthorizationContactInformation authorizationCodesGetContactInformation(id)

Get contact information for an authorization code.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AuthorizationCodesApi();
let id = 56; // Number | The id of the authorization code.
apiInstance.authorizationCodesGetContactInformation(id, (error, data, response) => {
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
 **id** | **Number**| The id of the authorization code. | 

### Return type

[**AuthorizationCodesSharedModelsAuthorizationContactInformation**](AuthorizationCodesSharedModelsAuthorizationContactInformation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## authorizationCodesPostAuthorizationCode

> Number authorizationCodesPostAuthorizationCode(authorizationCodesSharedModelsAuthorizationCode)

Generates an authorization code using the provided definition and parameters.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AuthorizationCodesApi();
let authorizationCodesSharedModelsAuthorizationCode = new AgcoApi.AuthorizationCodesSharedModelsAuthorizationCode(); // AuthorizationCodesSharedModelsAuthorizationCode | The model from which to generate an authorization code.
apiInstance.authorizationCodesPostAuthorizationCode(authorizationCodesSharedModelsAuthorizationCode, (error, data, response) => {
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
 **authorizationCodesSharedModelsAuthorizationCode** | [**AuthorizationCodesSharedModelsAuthorizationCode**](AuthorizationCodesSharedModelsAuthorizationCode.md)| The model from which to generate an authorization code. | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## authorizationCodesPutAuthorizationCode

> authorizationCodesPutAuthorizationCode(id, authorizationCodesSharedModelsAuthorizationCode)

Update an authorization code.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AuthorizationCodesApi();
let id = 56; // Number | The id of the authorization code.
let authorizationCodesSharedModelsAuthorizationCode = new AgcoApi.AuthorizationCodesSharedModelsAuthorizationCode(); // AuthorizationCodesSharedModelsAuthorizationCode | The model from which to update an authorization code.
apiInstance.authorizationCodesPutAuthorizationCode(id, authorizationCodesSharedModelsAuthorizationCode, (error, data, response) => {
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
 **id** | **Number**| The id of the authorization code. | 
 **authorizationCodesSharedModelsAuthorizationCode** | [**AuthorizationCodesSharedModelsAuthorizationCode**](AuthorizationCodesSharedModelsAuthorizationCode.md)| The model from which to update an authorization code. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*


## authorizationCodesValidateAuthorizationCode

> AuthorizationCodesSharedModelsCodeValidationModel authorizationCodesValidateAuthorizationCode(id)

No Documentation Found.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AuthorizationCodesApi();
let id = 56; // Number | 
apiInstance.authorizationCodesValidateAuthorizationCode(id, (error, data, response) => {
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
 **id** | **Number**|  | 

### Return type

[**AuthorizationCodesSharedModelsCodeValidationModel**](AuthorizationCodesSharedModelsCodeValidationModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

