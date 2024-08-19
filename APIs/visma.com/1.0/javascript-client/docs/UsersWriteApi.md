# SeveraPublicRestApiDocumentation.UsersWriteApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**flextimeAdjustmentsDeleteFlextimeAdjustment**](UsersWriteApi.md#flextimeAdjustmentsDeleteFlextimeAdjustment) | **DELETE** /v1/flextimeadjustments/{guid} | Delete an flextime adjustment.
[**flextimeAdjustmentsPatchFlextimeAdjustment**](UsersWriteApi.md#flextimeAdjustmentsPatchFlextimeAdjustment) | **PATCH** /v1/flextimeadjustments/{guid} | Update (Patch) an Flextime Adjustment or a part of it.
[**flextimeAdjustmentsPostFlextimeAdjustment**](UsersWriteApi.md#flextimeAdjustmentsPostFlextimeAdjustment) | **POST** /v1/flextimeadjustments | Insert a flextime adjustment.
[**keywordsLinkKeywordToUser**](UsersWriteApi.md#keywordsLinkKeywordToUser) | **POST** /v1/users/{userGuid}/keywords/{guid} | Link existing keyword to user
[**userCustomValuesPatchUserCustomValue**](UsersWriteApi.md#userCustomValuesPatchUserCustomValue) | **PATCH** /v1/users/customvalues/{guid} | Update (Patch) a user custom value or a part of it.
[**userCustomValuesPostUserCustomValue**](UsersWriteApi.md#userCustomValuesPostUserCustomValue) | **POST** /v1/users/customvalues | Insert a user custom value.
[**usersPatchUser**](UsersWriteApi.md#usersPatchUser) | **PATCH** /v1/users/{guid} | Update (Patch) an user or a part of it.
[**usersPostUser**](UsersWriteApi.md#usersPostUser) | **POST** /v1/users | Insert an user.
[**workContractsPatchWorkContract_0**](UsersWriteApi.md#workContractsPatchWorkContract_0) | **PATCH** /v1/workcontracts/{guid} | Update (Patch) a work contract or a part of it.
[**workContractsPostWorkContract_0**](UsersWriteApi.md#workContractsPostWorkContract_0) | **POST** /v1/workcontracts | Insert a work contract.
[**workdaysPatchWorkDay**](UsersWriteApi.md#workdaysPatchWorkDay) | **PATCH** /v1/users/{userGuid}/workdays/{date} | Update (Patch) a workday or a part of it



## flextimeAdjustmentsDeleteFlextimeAdjustment

> flextimeAdjustmentsDeleteFlextimeAdjustment(guid)

Delete an flextime adjustment.

Returns: No Content (204) if succeeded. Not found (404) if flextime adjustment can&#39;t be found.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.UsersWriteApi();
let guid = "guid_example"; // String | ID for the flextime adjustment to delete.
apiInstance.flextimeAdjustmentsDeleteFlextimeAdjustment(guid, (error, data, response) => {
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
 **guid** | **String**| ID for the flextime adjustment to delete. | 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## flextimeAdjustmentsPatchFlextimeAdjustment

> [FlextimeAdjustmentOutputModel] flextimeAdjustmentsPatchFlextimeAdjustment(guid, opts)

Update (Patch) an Flextime Adjustment or a part of it.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.UsersWriteApi();
let guid = "guid_example"; // String | ID of the Flextime Adjustment.
let opts = {
  'patchOperation': [new SeveraPublicRestApiDocumentation.PatchOperation()] // [PatchOperation] | JSON patch document of FlextimeAdjustmentInputModel.
};
apiInstance.flextimeAdjustmentsPatchFlextimeAdjustment(guid, opts, (error, data, response) => {
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
 **guid** | **String**| ID of the Flextime Adjustment. | 
 **patchOperation** | [**[PatchOperation]**](PatchOperation.md)| JSON patch document of FlextimeAdjustmentInputModel. | [optional] 

### Return type

[**[FlextimeAdjustmentOutputModel]**](FlextimeAdjustmentOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## flextimeAdjustmentsPostFlextimeAdjustment

> FlextimeAdjustmentOutputModel flextimeAdjustmentsPostFlextimeAdjustment(opts)

Insert a flextime adjustment.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.UsersWriteApi();
let opts = {
  'flextimeAdjustmentInputModel': new SeveraPublicRestApiDocumentation.FlextimeAdjustmentInputModel() // FlextimeAdjustmentInputModel | FlextimeAdjustmentInputModel.
};
apiInstance.flextimeAdjustmentsPostFlextimeAdjustment(opts, (error, data, response) => {
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
 **flextimeAdjustmentInputModel** | [**FlextimeAdjustmentInputModel**](FlextimeAdjustmentInputModel.md)| FlextimeAdjustmentInputModel. | [optional] 

### Return type

[**FlextimeAdjustmentOutputModel**](FlextimeAdjustmentOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## keywordsLinkKeywordToUser

> UserKeywordModel keywordsLinkKeywordToUser(userGuid, guid)

Link existing keyword to user

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.UsersWriteApi();
let userGuid = "userGuid_example"; // String | 
let guid = "guid_example"; // String | 
apiInstance.keywordsLinkKeywordToUser(userGuid, guid, (error, data, response) => {
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
 **userGuid** | **String**|  | 
 **guid** | **String**|  | 

### Return type

[**UserKeywordModel**](UserKeywordModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## userCustomValuesPatchUserCustomValue

> [UserCustomValueOutputModel] userCustomValuesPatchUserCustomValue(guid, opts)

Update (Patch) a user custom value or a part of it.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.UsersWriteApi();
let guid = "guid_example"; // String | ID of the user custom value Can also be comma separate list of IDs to patch multiple user custom values with one call. When multiple IDs are given, returns model which has list of succeeded user custom values and list of errors.
let opts = {
  'patchOperation': [new SeveraPublicRestApiDocumentation.PatchOperation()] // [PatchOperation] | JSON Patch document of UserCustomValueModel.
};
apiInstance.userCustomValuesPatchUserCustomValue(guid, opts, (error, data, response) => {
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
 **guid** | **String**| ID of the user custom value Can also be comma separate list of IDs to patch multiple user custom values with one call. When multiple IDs are given, returns model which has list of succeeded user custom values and list of errors. | 
 **patchOperation** | [**[PatchOperation]**](PatchOperation.md)| JSON Patch document of UserCustomValueModel. | [optional] 

### Return type

[**[UserCustomValueOutputModel]**](UserCustomValueOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## userCustomValuesPostUserCustomValue

> [UserCustomValueOutputModel] userCustomValuesPostUserCustomValue(opts)

Insert a user custom value.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.UsersWriteApi();
let opts = {
  'userCustomValueInputModel': new SeveraPublicRestApiDocumentation.UserCustomValueInputModel() // UserCustomValueInputModel | UserCustomValueModel.
};
apiInstance.userCustomValuesPostUserCustomValue(opts, (error, data, response) => {
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
 **userCustomValueInputModel** | [**UserCustomValueInputModel**](UserCustomValueInputModel.md)| UserCustomValueModel. | [optional] 

### Return type

[**[UserCustomValueOutputModel]**](UserCustomValueOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersPatchUser

> [UserOutputModel] usersPatchUser(guid, opts)

Update (Patch) an user or a part of it.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.UsersWriteApi();
let guid = "guid_example"; // String | ID of the user.
let opts = {
  'patchOperation': [new SeveraPublicRestApiDocumentation.PatchOperation()] // [PatchOperation] | JSON Patch document of UserModel.
};
apiInstance.usersPatchUser(guid, opts, (error, data, response) => {
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
 **guid** | **String**| ID of the user. | 
 **patchOperation** | [**[PatchOperation]**](PatchOperation.md)| JSON Patch document of UserModel. | [optional] 

### Return type

[**[UserOutputModel]**](UserOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersPostUser

> UserOutputModel usersPostUser(opts)

Insert an user.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.UsersWriteApi();
let opts = {
  'userInputModel': new SeveraPublicRestApiDocumentation.UserInputModel() // UserInputModel | UserModel.
};
apiInstance.usersPostUser(opts, (error, data, response) => {
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
 **userInputModel** | [**UserInputModel**](UserInputModel.md)| UserModel. | [optional] 

### Return type

[**UserOutputModel**](UserOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## workContractsPatchWorkContract_0

> [WorkContractOutputModel] workContractsPatchWorkContract_0(guid, opts)

Update (Patch) a work contract or a part of it.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.UsersWriteApi();
let guid = "guid_example"; // String | ID of the work contract.
let opts = {
  'patchOperation': [new SeveraPublicRestApiDocumentation.PatchOperation()] // [PatchOperation] | JSON patch document of WorkContractOutputModel.
};
apiInstance.workContractsPatchWorkContract_0(guid, opts, (error, data, response) => {
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
 **guid** | **String**| ID of the work contract. | 
 **patchOperation** | [**[PatchOperation]**](PatchOperation.md)| JSON patch document of WorkContractOutputModel. | [optional] 

### Return type

[**[WorkContractOutputModel]**](WorkContractOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## workContractsPostWorkContract_0

> WorkContractOutputModel workContractsPostWorkContract_0(opts)

Insert a work contract.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.UsersWriteApi();
let opts = {
  'resetFlextime': true, // Boolean | Optional. Reset flextime to zero when new work contract starts or keep the flextime value. Default true = reset flextime.
  'workContractInputModel': new SeveraPublicRestApiDocumentation.WorkContractInputModel() // WorkContractInputModel | WorkContractOutputModel.
};
apiInstance.workContractsPostWorkContract_0(opts, (error, data, response) => {
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
 **resetFlextime** | **Boolean**| Optional. Reset flextime to zero when new work contract starts or keep the flextime value. Default true &#x3D; reset flextime. | [optional] [default to true]
 **workContractInputModel** | [**WorkContractInputModel**](WorkContractInputModel.md)| WorkContractOutputModel. | [optional] 

### Return type

[**WorkContractOutputModel**](WorkContractOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## workdaysPatchWorkDay

> [WorkdayModel] workdaysPatchWorkDay(userGuid, date, opts)

Update (Patch) a workday or a part of it

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.UsersWriteApi();
let userGuid = "userGuid_example"; // String | ID of the user.
let date = new Date("2013-10-20T19:20:30+01:00"); // Date | Date of the workday..
let opts = {
  'patchOperation': [new SeveraPublicRestApiDocumentation.PatchOperation()] // [PatchOperation] | JSON patch document of WorkdayModel
};
apiInstance.workdaysPatchWorkDay(userGuid, date, opts, (error, data, response) => {
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
 **userGuid** | **String**| ID of the user. | 
 **date** | **Date**| Date of the workday.. | 
 **patchOperation** | [**[PatchOperation]**](PatchOperation.md)| JSON patch document of WorkdayModel | [optional] 

### Return type

[**[WorkdayModel]**](WorkdayModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

