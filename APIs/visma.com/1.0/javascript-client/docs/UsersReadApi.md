# SeveraPublicRestApiDocumentation.UsersReadApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**flextimeAdjustmentsGetFlextimeAdjustment**](UsersReadApi.md#flextimeAdjustmentsGetFlextimeAdjustment) | **GET** /v1/flextimeadjustments/{guid} | Get Flextime Adjustment by ID.
[**flextimeAdjustmentsGetFlextimeAdjustments**](UsersReadApi.md#flextimeAdjustmentsGetFlextimeAdjustments) | **GET** /v1/users/{userGuid}/flextimeadjustments | Get the Flextime Adjustments.
[**flextimeGetFlextime**](UsersReadApi.md#flextimeGetFlextime) | **GET** /v1/users/{userGuid}/flextime | Get the flextime balance for a user for a specified date. Total balance is returned for the given date. Month balance is the balance for the month of the given date. Values are returned only if the advanced time tracking add-on is active.
[**keywordsGetUserKeywords**](UsersReadApi.md#keywordsGetUserKeywords) | **GET** /v1/users/{userGuid}/keywords | Get all the keywords for user.
[**projectMemberCostExceptionsGetProjectMemberCostExceptionsForUser**](UsersReadApi.md#projectMemberCostExceptionsGetProjectMemberCostExceptionsForUser) | **GET** /v1/users/{userGuid}/projectmembercostexceptions | Get all cost exceptions of project members for user.
[**userCustomValuesGetUserCustomValue**](UsersReadApi.md#userCustomValuesGetUserCustomValue) | **GET** /v1/users/customvalues/{guid} | Get user custom value by ID.
[**userCustomValuesGetUserCustomValues**](UsersReadApi.md#userCustomValuesGetUserCustomValues) | **GET** /v1/users/{userGuid}/customvalues | Get the user custom values.
[**usersGetUser**](UsersReadApi.md#usersGetUser) | **GET** /v1/users/{guid} | Get user by ID.
[**usersGetUsers**](UsersReadApi.md#usersGetUsers) | **GET** /v1/users | Get users
[**workContractsGetCurrentWorkContractForUser**](UsersReadApi.md#workContractsGetCurrentWorkContractForUser) | **GET** /v1/users/{userGuid}/workcontracts/current | Gets current work contract for the user
[**workContractsGetWorkContract_0**](UsersReadApi.md#workContractsGetWorkContract_0) | **GET** /v1/workcontracts/{guid} | Get work contract by ID.
[**workContractsGetWorkContractsForUser**](UsersReadApi.md#workContractsGetWorkContractsForUser) | **GET** /v1/users/{userGuid}/workcontracts | Get all the work contracts for the user.
[**workdaysGetWorkdays**](UsersReadApi.md#workdaysGetWorkdays) | **GET** /v1/users/{userGuid}/workdays | Get workdays for a user.



## flextimeAdjustmentsGetFlextimeAdjustment

> FlextimeAdjustmentOutputModel flextimeAdjustmentsGetFlextimeAdjustment(guid)

Get Flextime Adjustment by ID.

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

let apiInstance = new SeveraPublicRestApiDocumentation.UsersReadApi();
let guid = "guid_example"; // String | GUID used to get the Flextime Adjustment.
apiInstance.flextimeAdjustmentsGetFlextimeAdjustment(guid, (error, data, response) => {
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
 **guid** | **String**| GUID used to get the Flextime Adjustment. | 

### Return type

[**FlextimeAdjustmentOutputModel**](FlextimeAdjustmentOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## flextimeAdjustmentsGetFlextimeAdjustments

> [FlextimeAdjustmentOutputModel] flextimeAdjustmentsGetFlextimeAdjustments(userGuid, opts)

Get the Flextime Adjustments.

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

let apiInstance = new SeveraPublicRestApiDocumentation.UsersReadApi();
let userGuid = "userGuid_example"; // String | ID of the user for whom to get the adjustments.
let opts = {
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56 // Number | Optional: How many rows to fetch, Default 20, maximum 100.
};
apiInstance.flextimeAdjustmentsGetFlextimeAdjustments(userGuid, opts, (error, data, response) => {
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
 **userGuid** | **String**| ID of the user for whom to get the adjustments. | 
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 

### Return type

[**[FlextimeAdjustmentOutputModel]**](FlextimeAdjustmentOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## flextimeGetFlextime

> FlextimeModel flextimeGetFlextime(userGuid, opts)

Get the flextime balance for a user for a specified date. Total balance is returned for the given date. Month balance is the balance for the month of the given date. Values are returned only if the advanced time tracking add-on is active.

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

let apiInstance = new SeveraPublicRestApiDocumentation.UsersReadApi();
let userGuid = "userGuid_example"; // String | Id of the user.
let opts = {
  'eventDate': new Date("2013-10-20T19:20:30+01:00") // Date | Date for which to get the balance. Max 12 months into the future.
};
apiInstance.flextimeGetFlextime(userGuid, opts, (error, data, response) => {
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
 **userGuid** | **String**| Id of the user. | 
 **eventDate** | **Date**| Date for which to get the balance. Max 12 months into the future. | [optional] 

### Return type

[**FlextimeModel**](FlextimeModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## keywordsGetUserKeywords

> [UserKeywordModel] keywordsGetUserKeywords(userGuid, opts)

Get all the keywords for user.

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

let apiInstance = new SeveraPublicRestApiDocumentation.UsersReadApi();
let userGuid = "userGuid_example"; // String | ID of the user for who keywords are requested.
let opts = {
  'active': true, // Boolean | If not given, return all Keywords, if given as true return only active Keywords, if given as false returns only inactive Keywords.
  'sortings': [new SeveraPublicRestApiDocumentation.KeyValuePairOfStringAndSortDirection()] // [KeyValuePairOfStringAndSortDirection] | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=Keyword&sortings[0].value=Desc\".
};
apiInstance.keywordsGetUserKeywords(userGuid, opts, (error, data, response) => {
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
 **userGuid** | **String**| ID of the user for who keywords are requested. | 
 **active** | **Boolean**| If not given, return all Keywords, if given as true return only active Keywords, if given as false returns only inactive Keywords. | [optional] 
 **sortings** | [**[KeyValuePairOfStringAndSortDirection]**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Keyword&amp;sortings[0].value&#x3D;Desc\&quot;. | [optional] 

### Return type

[**[UserKeywordModel]**](UserKeywordModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectMemberCostExceptionsGetProjectMemberCostExceptionsForUser

> [ProjectMemberCostExceptionOutputModel] projectMemberCostExceptionsGetProjectMemberCostExceptionsForUser(userGuid, opts)

Get all cost exceptions of project members for user.

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

let apiInstance = new SeveraPublicRestApiDocumentation.UsersReadApi();
let userGuid = "userGuid_example"; // String | Guid of the user.
let opts = {
  'isProjectClosed': true, // Boolean | Search only for open or closed projects. Default all projects.
  'firstRow': 0, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56 // Number | Optional: How many rows to fetch, Default 20, maximum 100.
};
apiInstance.projectMemberCostExceptionsGetProjectMemberCostExceptionsForUser(userGuid, opts, (error, data, response) => {
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
 **userGuid** | **String**| Guid of the user. | 
 **isProjectClosed** | **Boolean**| Search only for open or closed projects. Default all projects. | [optional] 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0]
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 

### Return type

[**[ProjectMemberCostExceptionOutputModel]**](ProjectMemberCostExceptionOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## userCustomValuesGetUserCustomValue

> UserCustomValueOutputModel userCustomValuesGetUserCustomValue(guid)

Get user custom value by ID.

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

let apiInstance = new SeveraPublicRestApiDocumentation.UsersReadApi();
let guid = "guid_example"; // String | Id used to get the user custom value.
apiInstance.userCustomValuesGetUserCustomValue(guid, (error, data, response) => {
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
 **guid** | **String**| Id used to get the user custom value. | 

### Return type

[**UserCustomValueOutputModel**](UserCustomValueOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## userCustomValuesGetUserCustomValues

> [UserCustomValueOutputModel] userCustomValuesGetUserCustomValues(userGuid, opts)

Get the user custom values.

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

let apiInstance = new SeveraPublicRestApiDocumentation.UsersReadApi();
let userGuid = "userGuid_example"; // String | ID of the user.
let opts = {
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'isActive': true, // Boolean | Optional: Get only values of active or inactive user custom properties.
  'targets': ["null"], // [String] | Optional: List of target for which to get the values.
  'changedSince': new Date("2013-10-20T19:20:30+01:00") // Date | Optional: Get user custom values that have been added or changed after this date time (greater or equal).
};
apiInstance.userCustomValuesGetUserCustomValues(userGuid, opts, (error, data, response) => {
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
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **isActive** | **Boolean**| Optional: Get only values of active or inactive user custom properties. | [optional] 
 **targets** | [**[String]**](String.md)| Optional: List of target for which to get the values. | [optional] 
 **changedSince** | **Date**| Optional: Get user custom values that have been added or changed after this date time (greater or equal). | [optional] 

### Return type

[**[UserCustomValueOutputModel]**](UserCustomValueOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersGetUser

> UserOutputModel usersGetUser(guid)

Get user by ID.

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

let apiInstance = new SeveraPublicRestApiDocumentation.UsersReadApi();
let guid = "guid_example"; // String | GUID used to get the user.
apiInstance.usersGetUser(guid, (error, data, response) => {
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
 **guid** | **String**| GUID used to get the user. | 

### Return type

[**UserOutputModel**](UserOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersGetUsers

> [UserOutputModel] usersGetUsers(opts)

Get users

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

let apiInstance = new SeveraPublicRestApiDocumentation.UsersReadApi();
let opts = {
  'pageToken': "pageToken_example", // String | 
  'rowCount': 56, // Number | Optional: How many rows to fetch.
  'isActive': true, // Boolean | If not given, return all users, if given as true return only active users, if given as false returns only inactive users
  'businessUnitGuids': ["null"], // [String] | Optional: ID of the business unit of the user. If not provided, returns for all business units. Default all.
  'keywordGuids': ["null"], // [String] | Optional: ID of the keyword of the user. If not provided, returns for all keywords. Default all.
  'changedSince': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional: Get users that have been added or changed after this date time (greater or equal).
  'supervisorUserGuids': ["null"], // [String] | Optional: ID of the supervisor to get subordinates for.
  'code': "''", // String | Optional: Code of the user.
  'email': "''", // String | Optional: Email address of the user.
  'purpose': new SeveraPublicRestApiDocumentation.GetUsersPurpose() // GetUsersPurpose | Optional: Filter users by purpose.
};
apiInstance.usersGetUsers(opts, (error, data, response) => {
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
 **pageToken** | **String**|  | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch. | [optional] 
 **isActive** | **Boolean**| If not given, return all users, if given as true return only active users, if given as false returns only inactive users | [optional] 
 **businessUnitGuids** | [**[String]**](String.md)| Optional: ID of the business unit of the user. If not provided, returns for all business units. Default all. | [optional] 
 **keywordGuids** | [**[String]**](String.md)| Optional: ID of the keyword of the user. If not provided, returns for all keywords. Default all. | [optional] 
 **changedSince** | **Date**| Optional: Get users that have been added or changed after this date time (greater or equal). | [optional] 
 **supervisorUserGuids** | [**[String]**](String.md)| Optional: ID of the supervisor to get subordinates for. | [optional] 
 **code** | **String**| Optional: Code of the user. | [optional] [default to &#39;&#39;]
 **email** | **String**| Optional: Email address of the user. | [optional] [default to &#39;&#39;]
 **purpose** | [**GetUsersPurpose**](.md)| Optional: Filter users by purpose. | [optional] 

### Return type

[**[UserOutputModel]**](UserOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workContractsGetCurrentWorkContractForUser

> WorkContractOutputModel workContractsGetCurrentWorkContractForUser(userGuid)

Gets current work contract for the user

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

let apiInstance = new SeveraPublicRestApiDocumentation.UsersReadApi();
let userGuid = "userGuid_example"; // String | Id of the user
apiInstance.workContractsGetCurrentWorkContractForUser(userGuid, (error, data, response) => {
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
 **userGuid** | **String**| Id of the user | 

### Return type

[**WorkContractOutputModel**](WorkContractOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workContractsGetWorkContract_0

> WorkContractOutputModel workContractsGetWorkContract_0(guid)

Get work contract by ID.

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

let apiInstance = new SeveraPublicRestApiDocumentation.UsersReadApi();
let guid = "guid_example"; // String | Id used to get the work contract.
apiInstance.workContractsGetWorkContract_0(guid, (error, data, response) => {
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
 **guid** | **String**| Id used to get the work contract. | 

### Return type

[**WorkContractOutputModel**](WorkContractOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workContractsGetWorkContractsForUser

> [WorkContractOutputModel] workContractsGetWorkContractsForUser(userGuid)

Get all the work contracts for the user.

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

let apiInstance = new SeveraPublicRestApiDocumentation.UsersReadApi();
let userGuid = "userGuid_example"; // String | Id of the user.
apiInstance.workContractsGetWorkContractsForUser(userGuid, (error, data, response) => {
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
 **userGuid** | **String**| Id of the user. | 

### Return type

[**[WorkContractOutputModel]**](WorkContractOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workdaysGetWorkdays

> [WorkdayModel] workdaysGetWorkdays(userGuid, startDate, endDate)

Get workdays for a user.

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

let apiInstance = new SeveraPublicRestApiDocumentation.UsersReadApi();
let userGuid = "userGuid_example"; // String | ID of the user.
let startDate = new Date("2013-10-20T19:20:30+01:00"); // Date | Start date of the workdays.
let endDate = new Date("2013-10-20T19:20:30+01:00"); // Date | End date of the workdays.
apiInstance.workdaysGetWorkdays(userGuid, startDate, endDate, (error, data, response) => {
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
 **startDate** | **Date**| Start date of the workdays. | 
 **endDate** | **Date**| End date of the workdays. | 

### Return type

[**[WorkdayModel]**](WorkdayModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

