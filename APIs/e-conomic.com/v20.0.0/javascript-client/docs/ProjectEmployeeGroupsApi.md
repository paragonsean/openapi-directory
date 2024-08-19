# VismaEConomicOpenApi.ProjectEmployeeGroupsApi

All URIs are relative to *https://apis.e-conomic.com/api/v20.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createProjectEmployeeGroup**](ProjectEmployeeGroupsApi.md#createProjectEmployeeGroup) | **POST** /project-employeegroups | Create a single Project employee group
[**deleteProjectEmployeeGroupById**](ProjectEmployeeGroupsApi.md#deleteProjectEmployeeGroupById) | **DELETE** /project-employeegroups/{number} | Delete single Project employee group
[**getAllProjectEmployeeGroups**](ProjectEmployeeGroupsApi.md#getAllProjectEmployeeGroups) | **GET** /project-employeegroups | Retrieve all Project employee groups
[**getNumberOfProjectEmployeeGroups**](ProjectEmployeeGroupsApi.md#getNumberOfProjectEmployeeGroups) | **GET** /project-employeegroups/count | Retrieve the number of Project employee groups
[**getPageOfProjectEmployeeGroups**](ProjectEmployeeGroupsApi.md#getPageOfProjectEmployeeGroups) | **GET** /project-employeegroups/paged | Retrieve a page of Project employee groups
[**getProjectEmployeeGroupById**](ProjectEmployeeGroupsApi.md#getProjectEmployeeGroupById) | **GET** /project-employeegroups/{number} | Retrieve single Project employee group
[**updateProjectEmployeeGroup**](ProjectEmployeeGroupsApi.md#updateProjectEmployeeGroup) | **PUT** /project-employeegroups | Update a single Project employee group



## createProjectEmployeeGroup

> CreatedResult createProjectEmployeeGroup(opts)

Create a single Project employee group

Use this endpoint to create a single Project employee group.

### Example

```javascript
import VismaEConomicOpenApi from 'visma_e_conomic_open_api';
let defaultClient = VismaEConomicOpenApi.ApiClient.instance;
// Configure API key authorization: X-AgreementGrantToken
let X-AgreementGrantToken = defaultClient.authentications['X-AgreementGrantToken'];
X-AgreementGrantToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AgreementGrantToken.apiKeyPrefix = 'Token';
// Configure API key authorization: X-AppSecretToken
let X-AppSecretToken = defaultClient.authentications['X-AppSecretToken'];
X-AppSecretToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AppSecretToken.apiKeyPrefix = 'Token';

let apiInstance = new VismaEConomicOpenApi.ProjectEmployeeGroupsApi();
let opts = {
  'projectEmployeeGroup': new VismaEConomicOpenApi.ProjectEmployeeGroup() // ProjectEmployeeGroup | 
};
apiInstance.createProjectEmployeeGroup(opts, (error, data, response) => {
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
 **projectEmployeeGroup** | [**ProjectEmployeeGroup**](ProjectEmployeeGroup.md)|  | [optional] 

### Return type

[**CreatedResult**](CreatedResult.md)

### Authorization

[X-AgreementGrantToken](../README.md#X-AgreementGrantToken), [X-AppSecretToken](../README.md#X-AppSecretToken)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json


## deleteProjectEmployeeGroupById

> deleteProjectEmployeeGroupById(number)

Delete single Project employee group

Use this endpoint to delete a single Project employee group by id/number.

### Example

```javascript
import VismaEConomicOpenApi from 'visma_e_conomic_open_api';
let defaultClient = VismaEConomicOpenApi.ApiClient.instance;
// Configure API key authorization: X-AgreementGrantToken
let X-AgreementGrantToken = defaultClient.authentications['X-AgreementGrantToken'];
X-AgreementGrantToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AgreementGrantToken.apiKeyPrefix = 'Token';
// Configure API key authorization: X-AppSecretToken
let X-AppSecretToken = defaultClient.authentications['X-AppSecretToken'];
X-AppSecretToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AppSecretToken.apiKeyPrefix = 'Token';

let apiInstance = new VismaEConomicOpenApi.ProjectEmployeeGroupsApi();
let number = 56; // Number | 
apiInstance.deleteProjectEmployeeGroupById(number, (error, data, response) => {
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
 **number** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

[X-AgreementGrantToken](../README.md#X-AgreementGrantToken), [X-AppSecretToken](../README.md#X-AppSecretToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllProjectEmployeeGroups

> ProjectEmployeeGroupCursorResults getAllProjectEmployeeGroups(opts)

Retrieve all Project employee groups

Use this endpoint to retrieve all Project employee groups in bulk.  Max number of items returned in a single call is 1000. Use the continuation cursor parameter to set the continuation cursor for retrieval of next set of data. [pagination instructions](#section/Retrieving-data/Pagination)

### Example

```javascript
import VismaEConomicOpenApi from 'visma_e_conomic_open_api';
let defaultClient = VismaEConomicOpenApi.ApiClient.instance;
// Configure API key authorization: X-AgreementGrantToken
let X-AgreementGrantToken = defaultClient.authentications['X-AgreementGrantToken'];
X-AgreementGrantToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AgreementGrantToken.apiKeyPrefix = 'Token';
// Configure API key authorization: X-AppSecretToken
let X-AppSecretToken = defaultClient.authentications['X-AppSecretToken'];
X-AppSecretToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AppSecretToken.apiKeyPrefix = 'Token';

let apiInstance = new VismaEConomicOpenApi.ProjectEmployeeGroupsApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'filter': "filter_example" // String | 
};
apiInstance.getAllProjectEmployeeGroups(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **filter** | **String**|  | [optional] 

### Return type

[**ProjectEmployeeGroupCursorResults**](ProjectEmployeeGroupCursorResults.md)

### Authorization

[X-AgreementGrantToken](../README.md#X-AgreementGrantToken), [X-AppSecretToken](../README.md#X-AppSecretToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNumberOfProjectEmployeeGroups

> Number getNumberOfProjectEmployeeGroups(opts)

Retrieve the number of Project employee groups

Call this endpoint to get the number of Project employee groups. You can use a filtering as well.

### Example

```javascript
import VismaEConomicOpenApi from 'visma_e_conomic_open_api';
let defaultClient = VismaEConomicOpenApi.ApiClient.instance;
// Configure API key authorization: X-AgreementGrantToken
let X-AgreementGrantToken = defaultClient.authentications['X-AgreementGrantToken'];
X-AgreementGrantToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AgreementGrantToken.apiKeyPrefix = 'Token';
// Configure API key authorization: X-AppSecretToken
let X-AppSecretToken = defaultClient.authentications['X-AppSecretToken'];
X-AppSecretToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AppSecretToken.apiKeyPrefix = 'Token';

let apiInstance = new VismaEConomicOpenApi.ProjectEmployeeGroupsApi();
let opts = {
  'filter': "filter_example" // String | 
};
apiInstance.getNumberOfProjectEmployeeGroups(opts, (error, data, response) => {
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
 **filter** | **String**|  | [optional] 

### Return type

**Number**

### Authorization

[X-AgreementGrantToken](../README.md#X-AgreementGrantToken), [X-AppSecretToken](../README.md#X-AppSecretToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPageOfProjectEmployeeGroups

> [ProjectEmployeeGroup] getPageOfProjectEmployeeGroups(opts)

Retrieve a page of Project employee groups

Use this endpoint to load a page of Project employee groups.

### Example

```javascript
import VismaEConomicOpenApi from 'visma_e_conomic_open_api';
let defaultClient = VismaEConomicOpenApi.ApiClient.instance;
// Configure API key authorization: X-AgreementGrantToken
let X-AgreementGrantToken = defaultClient.authentications['X-AgreementGrantToken'];
X-AgreementGrantToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AgreementGrantToken.apiKeyPrefix = 'Token';
// Configure API key authorization: X-AppSecretToken
let X-AppSecretToken = defaultClient.authentications['X-AppSecretToken'];
X-AppSecretToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AppSecretToken.apiKeyPrefix = 'Token';

let apiInstance = new VismaEConomicOpenApi.ProjectEmployeeGroupsApi();
let opts = {
  'filter': "filter_example", // String | 
  'sort': "sort_example", // String | 
  'pageSize': 20, // Number | 
  'skipPages': 0 // Number | 
};
apiInstance.getPageOfProjectEmployeeGroups(opts, (error, data, response) => {
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
 **filter** | **String**|  | [optional] 
 **sort** | **String**|  | [optional] 
 **pageSize** | **Number**|  | [optional] [default to 20]
 **skipPages** | **Number**|  | [optional] [default to 0]

### Return type

[**[ProjectEmployeeGroup]**](ProjectEmployeeGroup.md)

### Authorization

[X-AgreementGrantToken](../README.md#X-AgreementGrantToken), [X-AppSecretToken](../README.md#X-AppSecretToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProjectEmployeeGroupById

> ProjectEmployeeGroup getProjectEmployeeGroupById(number)

Retrieve single Project employee group

Use this endpoint to load a single Project employee group by id/number.

### Example

```javascript
import VismaEConomicOpenApi from 'visma_e_conomic_open_api';
let defaultClient = VismaEConomicOpenApi.ApiClient.instance;
// Configure API key authorization: X-AgreementGrantToken
let X-AgreementGrantToken = defaultClient.authentications['X-AgreementGrantToken'];
X-AgreementGrantToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AgreementGrantToken.apiKeyPrefix = 'Token';
// Configure API key authorization: X-AppSecretToken
let X-AppSecretToken = defaultClient.authentications['X-AppSecretToken'];
X-AppSecretToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AppSecretToken.apiKeyPrefix = 'Token';

let apiInstance = new VismaEConomicOpenApi.ProjectEmployeeGroupsApi();
let number = 56; // Number | 
apiInstance.getProjectEmployeeGroupById(number, (error, data, response) => {
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
 **number** | **Number**|  | 

### Return type

[**ProjectEmployeeGroup**](ProjectEmployeeGroup.md)

### Authorization

[X-AgreementGrantToken](../README.md#X-AgreementGrantToken), [X-AppSecretToken](../README.md#X-AppSecretToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateProjectEmployeeGroup

> updateProjectEmployeeGroup(opts)

Update a single Project employee group

Use this endpoint to update a single Project employee group.

### Example

```javascript
import VismaEConomicOpenApi from 'visma_e_conomic_open_api';
let defaultClient = VismaEConomicOpenApi.ApiClient.instance;
// Configure API key authorization: X-AgreementGrantToken
let X-AgreementGrantToken = defaultClient.authentications['X-AgreementGrantToken'];
X-AgreementGrantToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AgreementGrantToken.apiKeyPrefix = 'Token';
// Configure API key authorization: X-AppSecretToken
let X-AppSecretToken = defaultClient.authentications['X-AppSecretToken'];
X-AppSecretToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AppSecretToken.apiKeyPrefix = 'Token';

let apiInstance = new VismaEConomicOpenApi.ProjectEmployeeGroupsApi();
let opts = {
  'projectEmployeeGroup': new VismaEConomicOpenApi.ProjectEmployeeGroup() // ProjectEmployeeGroup | 
};
apiInstance.updateProjectEmployeeGroup(opts, (error, data, response) => {
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
 **projectEmployeeGroup** | [**ProjectEmployeeGroup**](ProjectEmployeeGroup.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[X-AgreementGrantToken](../README.md#X-AgreementGrantToken), [X-AppSecretToken](../README.md#X-AppSecretToken)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json

