# SeveraPublicRestApiDocumentation.ResourceallocationsReadApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resourceAllocationsGetResourceAllocation**](ResourceallocationsReadApi.md#resourceAllocationsGetResourceAllocation) | **GET** /v1/resourceallocations/{guid} | Get resource allocation by ID
[**resourceAllocationsGetResourceAllocations**](ResourceallocationsReadApi.md#resourceAllocationsGetResourceAllocations) | **GET** /v1/resourceallocations | Get resource allocations
[**resourceAllocationsGetResourceAllocationsByPhaseGuid**](ResourceallocationsReadApi.md#resourceAllocationsGetResourceAllocationsByPhaseGuid) | **GET** /v1/phases/{phaseGuid}/resourceallocations/allocations | Get resource allocations for a phase with required filters (startDate and endDate or changedSince, max 30 days to be fetched at once)
[**resourceAllocationsGetResourceAllocationsByProjectGuid**](ResourceallocationsReadApi.md#resourceAllocationsGetResourceAllocationsByProjectGuid) | **GET** /v1/projects/{projectGuid}/resourceallocations/allocations | Get resource allocations for a project with required filters (startDate and endDate or changedSince, max 30 days to be fetched at once)
[**resourceAllocationsGetResourceAllocationsByUserGuid**](ResourceallocationsReadApi.md#resourceAllocationsGetResourceAllocationsByUserGuid) | **GET** /v1/users/{userGuid}/resourceallocations/allocations | Get resource allocations for a user with required filters (startDate and endDate or changedSince, max 30 days to be fetched at once)
[**resourceAllocationsPostResourceAllocations**](ResourceallocationsReadApi.md#resourceAllocationsPostResourceAllocations) | **POST** /v1/resourceallocations/allocations | Get resource allocations (its POST because of being able to accommodate more filters)
[**roleAllocationsGetRoleAllocation**](ResourceallocationsReadApi.md#roleAllocationsGetRoleAllocation) | **GET** /v1/roleallocations/{guid} | Get role allocation by GUID.
[**roleAllocationsGetRoleAllocations**](ResourceallocationsReadApi.md#roleAllocationsGetRoleAllocations) | **GET** /v1/roleallocations | Get role allocations.



## resourceAllocationsGetResourceAllocation

> ResourceAllocationOutputModel resourceAllocationsGetResourceAllocation(guid)

Get resource allocation by ID

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

let apiInstance = new SeveraPublicRestApiDocumentation.ResourceallocationsReadApi();
let guid = "guid_example"; // String | GUID used to get the resource allocation.
apiInstance.resourceAllocationsGetResourceAllocation(guid, (error, data, response) => {
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
 **guid** | **String**| GUID used to get the resource allocation. | 

### Return type

[**ResourceAllocationOutputModel**](ResourceAllocationOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourceAllocationsGetResourceAllocations

> ResourceAllocationOutputModel resourceAllocationsGetResourceAllocations(opts)

Get resource allocations

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

let apiInstance = new SeveraPublicRestApiDocumentation.ResourceallocationsReadApi();
let opts = {
  'rowCount': 56, // Number | Optional: Number of rows to fetch.
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'changedSince': new Date("2013-10-20T19:20:30+01:00") // Date | Optional: Get resource allocations that have been added or changed after this date time (greater or equal).
};
apiInstance.resourceAllocationsGetResourceAllocations(opts, (error, data, response) => {
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
 **rowCount** | **Number**| Optional: Number of rows to fetch. | [optional] 
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **changedSince** | **Date**| Optional: Get resource allocations that have been added or changed after this date time (greater or equal). | [optional] 

### Return type

[**ResourceAllocationOutputModel**](ResourceAllocationOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourceAllocationsGetResourceAllocationsByPhaseGuid

> ResourceAllocationOutputModel resourceAllocationsGetResourceAllocationsByPhaseGuid(phaseGuid, opts)

Get resource allocations for a phase with required filters (startDate and endDate or changedSince, max 30 days to be fetched at once)

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

let apiInstance = new SeveraPublicRestApiDocumentation.ResourceallocationsReadApi();
let phaseGuid = "phaseGuid_example"; // String | 
let opts = {
  'startDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Get resource allocations with startDate. Using startDate and endDate or changedSince parameters are required to fetch a maximum of 30 days
  'endDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Get resource allocations with endDate. Using startDate and endDate or changedSince parameters are required to fetch a maximum of 30 days
  'changedSince': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional: Get resource allocations that have been added or changed after this date time (greater or equal).
  'userLicenseTypes': [new SeveraPublicRestApiDocumentation.LicenseUserType()], // [LicenseUserType] | 
  'projectGuid': "projectGuid_example", // String | 
  'userGuid': "userGuid_example", // String | 
  'projectBusinessUnitGuid': "projectBusinessUnitGuid_example", // String | 
  'userBusinessUnitGuid': "userBusinessUnitGuid_example", // String | 
  'projectManagerUserGuid': "projectManagerUserGuid_example", // String | 
  'userTagGuid': "userTagGuid_example", // String | 
  'useSalesProbability': true, // Boolean | 
  'projectStatusTypeGuid': "projectStatusTypeGuid_example", // String | 
  'projectTagGuid': "projectTagGuid_example", // String | 
  'superiorUserGuid': "superiorUserGuid_example", // String | 
  'salesStatusTypeGuid': "salesStatusTypeGuid_example", // String | 
  'resourceAllocationGuid': "resourceAllocationGuid_example", // String | 
  'salesProgress': new SeveraPublicRestApiDocumentation.SalesProgress(), // SalesProgress | 
  'rowCount': 56, // Number | Optional: Number of rows to fetch.
  'pageToken': "pageToken_example" // String | Optional: page token to fetch the next page.
};
apiInstance.resourceAllocationsGetResourceAllocationsByPhaseGuid(phaseGuid, opts, (error, data, response) => {
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
 **phaseGuid** | **String**|  | 
 **startDate** | **Date**| Get resource allocations with startDate. Using startDate and endDate or changedSince parameters are required to fetch a maximum of 30 days | [optional] 
 **endDate** | **Date**| Get resource allocations with endDate. Using startDate and endDate or changedSince parameters are required to fetch a maximum of 30 days | [optional] 
 **changedSince** | **Date**| Optional: Get resource allocations that have been added or changed after this date time (greater or equal). | [optional] 
 **userLicenseTypes** | [**[LicenseUserType]**](LicenseUserType.md)|  | [optional] 
 **projectGuid** | **String**|  | [optional] 
 **userGuid** | **String**|  | [optional] 
 **projectBusinessUnitGuid** | **String**|  | [optional] 
 **userBusinessUnitGuid** | **String**|  | [optional] 
 **projectManagerUserGuid** | **String**|  | [optional] 
 **userTagGuid** | **String**|  | [optional] 
 **useSalesProbability** | **Boolean**|  | [optional] [default to true]
 **projectStatusTypeGuid** | **String**|  | [optional] 
 **projectTagGuid** | **String**|  | [optional] 
 **superiorUserGuid** | **String**|  | [optional] 
 **salesStatusTypeGuid** | **String**|  | [optional] 
 **resourceAllocationGuid** | **String**|  | [optional] 
 **salesProgress** | [**SalesProgress**](.md)|  | [optional] 
 **rowCount** | **Number**| Optional: Number of rows to fetch. | [optional] 
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 

### Return type

[**ResourceAllocationOutputModel**](ResourceAllocationOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourceAllocationsGetResourceAllocationsByProjectGuid

> ResourceAllocationOutputModel resourceAllocationsGetResourceAllocationsByProjectGuid(projectGuid, opts)

Get resource allocations for a project with required filters (startDate and endDate or changedSince, max 30 days to be fetched at once)

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

let apiInstance = new SeveraPublicRestApiDocumentation.ResourceallocationsReadApi();
let projectGuid = "projectGuid_example"; // String | 
let opts = {
  'startDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Get resource allocations with startDate. Using startDate and endDate or changedSince parameters are required to fetch a maximum of 30 days
  'endDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Get resource allocations with endDate. Using startDate and endDate or changedSince parameters are required to fetch a maximum of 30 days
  'changedSince': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional: Get resource allocations that have been added or changed after this date time (greater or equal).
  'userLicenseTypes': [new SeveraPublicRestApiDocumentation.LicenseUserType()], // [LicenseUserType] | 
  'phaseGuid': "phaseGuid_example", // String | 
  'userGuid': "userGuid_example", // String | 
  'projectBusinessUnitGuid': "projectBusinessUnitGuid_example", // String | 
  'userBusinessUnitGuid': "userBusinessUnitGuid_example", // String | 
  'projectManagerUserGuid': "projectManagerUserGuid_example", // String | 
  'userTagGuid': "userTagGuid_example", // String | 
  'useSalesProbability': true, // Boolean | 
  'projectStatusTypeGuid': "projectStatusTypeGuid_example", // String | 
  'projectTagGuid': "projectTagGuid_example", // String | 
  'superiorUserGuid': "superiorUserGuid_example", // String | 
  'salesStatusTypeGuid': "salesStatusTypeGuid_example", // String | 
  'resourceAllocationGuid': "resourceAllocationGuid_example", // String | 
  'salesProgress': new SeveraPublicRestApiDocumentation.SalesProgress(), // SalesProgress | 
  'rowCount': 56, // Number | Optional: Number of rows to fetch.
  'pageToken': "pageToken_example" // String | Optional: page token to fetch the next page.
};
apiInstance.resourceAllocationsGetResourceAllocationsByProjectGuid(projectGuid, opts, (error, data, response) => {
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
 **projectGuid** | **String**|  | 
 **startDate** | **Date**| Get resource allocations with startDate. Using startDate and endDate or changedSince parameters are required to fetch a maximum of 30 days | [optional] 
 **endDate** | **Date**| Get resource allocations with endDate. Using startDate and endDate or changedSince parameters are required to fetch a maximum of 30 days | [optional] 
 **changedSince** | **Date**| Optional: Get resource allocations that have been added or changed after this date time (greater or equal). | [optional] 
 **userLicenseTypes** | [**[LicenseUserType]**](LicenseUserType.md)|  | [optional] 
 **phaseGuid** | **String**|  | [optional] 
 **userGuid** | **String**|  | [optional] 
 **projectBusinessUnitGuid** | **String**|  | [optional] 
 **userBusinessUnitGuid** | **String**|  | [optional] 
 **projectManagerUserGuid** | **String**|  | [optional] 
 **userTagGuid** | **String**|  | [optional] 
 **useSalesProbability** | **Boolean**|  | [optional] [default to true]
 **projectStatusTypeGuid** | **String**|  | [optional] 
 **projectTagGuid** | **String**|  | [optional] 
 **superiorUserGuid** | **String**|  | [optional] 
 **salesStatusTypeGuid** | **String**|  | [optional] 
 **resourceAllocationGuid** | **String**|  | [optional] 
 **salesProgress** | [**SalesProgress**](.md)|  | [optional] 
 **rowCount** | **Number**| Optional: Number of rows to fetch. | [optional] 
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 

### Return type

[**ResourceAllocationOutputModel**](ResourceAllocationOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourceAllocationsGetResourceAllocationsByUserGuid

> ResourceAllocationOutputModel resourceAllocationsGetResourceAllocationsByUserGuid(userGuid, opts)

Get resource allocations for a user with required filters (startDate and endDate or changedSince, max 30 days to be fetched at once)

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

let apiInstance = new SeveraPublicRestApiDocumentation.ResourceallocationsReadApi();
let userGuid = "userGuid_example"; // String | 
let opts = {
  'startDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Get resource allocations with startDate. Using startDate and endDate or changedSince parameters are required to fetch a maximum of 30 days
  'endDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Get resource allocations with endDate. Using startDate and endDate or changedSince parameters are required to fetch a maximum of 30 days
  'changedSince': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional: Get resource allocations that have been added or changed after this date time (greater or equal).
  'userLicenseTypes': [new SeveraPublicRestApiDocumentation.LicenseUserType()], // [LicenseUserType] | 
  'phaseGuid': "phaseGuid_example", // String | 
  'projectGuid': "projectGuid_example", // String | 
  'projectBusinessUnitGuid': "projectBusinessUnitGuid_example", // String | 
  'userBusinessUnitGuid': "userBusinessUnitGuid_example", // String | 
  'projectManagerUserGuid': "projectManagerUserGuid_example", // String | 
  'userTagGuid': "userTagGuid_example", // String | 
  'useSalesProbability': true, // Boolean | 
  'projectStatusTypeGuid': "projectStatusTypeGuid_example", // String | 
  'projectTagGuid': "projectTagGuid_example", // String | 
  'superiorUserGuid': "superiorUserGuid_example", // String | 
  'salesStatusTypeGuid': "salesStatusTypeGuid_example", // String | 
  'resourceAllocationGuid': "resourceAllocationGuid_example", // String | 
  'salesProgress': new SeveraPublicRestApiDocumentation.SalesProgress(), // SalesProgress | 
  'rowCount': 56, // Number | Optional: Number of rows to fetch.
  'pageToken': "pageToken_example" // String | Optional: page token to fetch the next page.
};
apiInstance.resourceAllocationsGetResourceAllocationsByUserGuid(userGuid, opts, (error, data, response) => {
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
 **startDate** | **Date**| Get resource allocations with startDate. Using startDate and endDate or changedSince parameters are required to fetch a maximum of 30 days | [optional] 
 **endDate** | **Date**| Get resource allocations with endDate. Using startDate and endDate or changedSince parameters are required to fetch a maximum of 30 days | [optional] 
 **changedSince** | **Date**| Optional: Get resource allocations that have been added or changed after this date time (greater or equal). | [optional] 
 **userLicenseTypes** | [**[LicenseUserType]**](LicenseUserType.md)|  | [optional] 
 **phaseGuid** | **String**|  | [optional] 
 **projectGuid** | **String**|  | [optional] 
 **projectBusinessUnitGuid** | **String**|  | [optional] 
 **userBusinessUnitGuid** | **String**|  | [optional] 
 **projectManagerUserGuid** | **String**|  | [optional] 
 **userTagGuid** | **String**|  | [optional] 
 **useSalesProbability** | **Boolean**|  | [optional] [default to true]
 **projectStatusTypeGuid** | **String**|  | [optional] 
 **projectTagGuid** | **String**|  | [optional] 
 **superiorUserGuid** | **String**|  | [optional] 
 **salesStatusTypeGuid** | **String**|  | [optional] 
 **resourceAllocationGuid** | **String**|  | [optional] 
 **salesProgress** | [**SalesProgress**](.md)|  | [optional] 
 **rowCount** | **Number**| Optional: Number of rows to fetch. | [optional] 
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 

### Return type

[**ResourceAllocationOutputModel**](ResourceAllocationOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourceAllocationsPostResourceAllocations

> [ResourceAllocationOutputModel] resourceAllocationsPostResourceAllocations(opts)

Get resource allocations (its POST because of being able to accommodate more filters)

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

let apiInstance = new SeveraPublicRestApiDocumentation.ResourceallocationsReadApi();
let opts = {
  'rowCount': 56, // Number | Optional: Number of rows to fetch.
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'changedSince': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional: Get resource allocations that have been added or changed after this date time (greater or equal).
  'resourceAllocationCriteriaModel': new SeveraPublicRestApiDocumentation.ResourceAllocationCriteriaModel() // ResourceAllocationCriteriaModel | resourceAllocationCriteriaModel
};
apiInstance.resourceAllocationsPostResourceAllocations(opts, (error, data, response) => {
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
 **rowCount** | **Number**| Optional: Number of rows to fetch. | [optional] 
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **changedSince** | **Date**| Optional: Get resource allocations that have been added or changed after this date time (greater or equal). | [optional] 
 **resourceAllocationCriteriaModel** | [**ResourceAllocationCriteriaModel**](ResourceAllocationCriteriaModel.md)| resourceAllocationCriteriaModel | [optional] 

### Return type

[**[ResourceAllocationOutputModel]**](ResourceAllocationOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## roleAllocationsGetRoleAllocation

> RoleAllocationOutputModel roleAllocationsGetRoleAllocation(guid)

Get role allocation by GUID.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ResourceallocationsReadApi();
let guid = "guid_example"; // String | ID used to get the role allocation.
apiInstance.roleAllocationsGetRoleAllocation(guid, (error, data, response) => {
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
 **guid** | **String**| ID used to get the role allocation. | 

### Return type

[**RoleAllocationOutputModel**](RoleAllocationOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## roleAllocationsGetRoleAllocations

> [RoleAllocationOutputModel] roleAllocationsGetRoleAllocations(startDate, opts)

Get role allocations.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ResourceallocationsReadApi();
let startDate = new Date("2013-10-20T19:20:30+01:00"); // Date | Starting date from which to get the role allocations. If end date is not specified on the role allocation then it will be compared with phase end date.
let opts = {
  'endDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional: Ending date to which to get the role allocations. If start date is not specified on the role allocation then it will be compared with phase start date.
  'pageToken': "pageToken_example", // String | Optional: Page token to fetch the next page.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default all.
  'useSalesProbability': true, // Boolean | Optional: Calculates the hours based on sales probability set for the project. Default is true.
  'roleGuids': ["null"], // [String] | Optional: Role IDs.
  'phaseGuids': ["null"], // [String] | Optional: Phase IDs.
  'projectGuids': ["null"] // [String] | Optional: Project IDs.
};
apiInstance.roleAllocationsGetRoleAllocations(startDate, opts, (error, data, response) => {
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
 **startDate** | **Date**| Starting date from which to get the role allocations. If end date is not specified on the role allocation then it will be compared with phase end date. | 
 **endDate** | **Date**| Optional: Ending date to which to get the role allocations. If start date is not specified on the role allocation then it will be compared with phase start date. | [optional] 
 **pageToken** | **String**| Optional: Page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default all. | [optional] 
 **useSalesProbability** | **Boolean**| Optional: Calculates the hours based on sales probability set for the project. Default is true. | [optional] [default to true]
 **roleGuids** | [**[String]**](String.md)| Optional: Role IDs. | [optional] 
 **phaseGuids** | [**[String]**](String.md)| Optional: Phase IDs. | [optional] 
 **projectGuids** | [**[String]**](String.md)| Optional: Project IDs. | [optional] 

### Return type

[**[RoleAllocationOutputModel]**](RoleAllocationOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

