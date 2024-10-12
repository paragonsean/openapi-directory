# SeveraPublicRestApiDocumentation.TravelsReadApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projectTravelExpensesGetDeletedProjectTravelExpenses**](TravelsReadApi.md#projectTravelExpensesGetDeletedProjectTravelExpenses) | **GET** /v1/deletedprojecttravelexpenses | Get the deleted project travel expenses.
[**projectTravelExpensesGetProjectTravelExpense**](TravelsReadApi.md#projectTravelExpensesGetProjectTravelExpense) | **GET** /v1/projecttravelexpenses/{guid} | Get project travel expense by ID.
[**projectTravelExpensesGetProjectTravelExpenses**](TravelsReadApi.md#projectTravelExpensesGetProjectTravelExpenses) | **GET** /v1/projecttravelexpenses | Get the project travel expenses.
[**projectTravelExpensesGetProjectTravelExpensesForProject**](TravelsReadApi.md#projectTravelExpensesGetProjectTravelExpensesForProject) | **GET** /v1/projects/{projectGuid}/projecttravelexpenses | Get all the project travel expenses for a project
[**projectTravelExpensesGetProjectTravelExpensesForTravelReimbursement**](TravelsReadApi.md#projectTravelExpensesGetProjectTravelExpensesForTravelReimbursement) | **GET** /v1/travelreimbursements/{travelReimbursementGuid}/projecttravelexpenses | Get all the project travel expenses for a travel reimbursement
[**projectTravelExpensesGetProjectTravelExpensesForUser**](TravelsReadApi.md#projectTravelExpensesGetProjectTravelExpensesForUser) | **GET** /v1/users/{userGuid}/projecttravelexpenses | Get all the project travel expenses for a user
[**travelReimbursementsGetTravelReimbursement**](TravelsReadApi.md#travelReimbursementsGetTravelReimbursement) | **GET** /v1/travelreimbursements/{guid} | Get travel reimbursement by ID
[**travelReimbursementsGetTravelReimbursements**](TravelsReadApi.md#travelReimbursementsGetTravelReimbursements) | **GET** /v1/travelreimbursements | Get travel reimbursements.



## projectTravelExpensesGetDeletedProjectTravelExpenses

> [DeletedProjectTravelExpenseModel] projectTravelExpensesGetDeletedProjectTravelExpenses(opts)

Get the deleted project travel expenses.

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

let apiInstance = new SeveraPublicRestApiDocumentation.TravelsReadApi();
let opts = {
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'projectGuid': ["null"], // [String] | Optional: ID of the project for the deleted project travel expenses to be fetched. If not provided, returns for all projects. Default all.
  'userGuid': ["null"], // [String] | Optional: ID of the user. If not provided, returns for all users. Default all.
  'deletedSince': new Date("2013-10-20T19:20:30+01:00") // Date | Optional: Get project travel expenses that have been deleted after this date time (greater or equal).
};
apiInstance.projectTravelExpensesGetDeletedProjectTravelExpenses(opts, (error, data, response) => {
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
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **projectGuid** | [**[String]**](String.md)| Optional: ID of the project for the deleted project travel expenses to be fetched. If not provided, returns for all projects. Default all. | [optional] 
 **userGuid** | [**[String]**](String.md)| Optional: ID of the user. If not provided, returns for all users. Default all. | [optional] 
 **deletedSince** | **Date**| Optional: Get project travel expenses that have been deleted after this date time (greater or equal). | [optional] 

### Return type

[**[DeletedProjectTravelExpenseModel]**](DeletedProjectTravelExpenseModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectTravelExpensesGetProjectTravelExpense

> ProjectTravelExpenseOutputModel projectTravelExpensesGetProjectTravelExpense(guid)

Get project travel expense by ID.

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

let apiInstance = new SeveraPublicRestApiDocumentation.TravelsReadApi();
let guid = "guid_example"; // String | Id used to get the project travel expense.
apiInstance.projectTravelExpensesGetProjectTravelExpense(guid, (error, data, response) => {
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
 **guid** | **String**| Id used to get the project travel expense. | 

### Return type

[**ProjectTravelExpenseOutputModel**](ProjectTravelExpenseOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectTravelExpensesGetProjectTravelExpenses

> [ProjectTravelExpenseOutputModel] projectTravelExpensesGetProjectTravelExpenses(opts)

Get the project travel expenses.

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

let apiInstance = new SeveraPublicRestApiDocumentation.TravelsReadApi();
let opts = {
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'changedSince': new Date("2013-10-20T19:20:30+01:00") // Date | Optional: Get project travel expenses that have been added or changed after this date time (greater or equal).
};
apiInstance.projectTravelExpensesGetProjectTravelExpenses(opts, (error, data, response) => {
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
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **changedSince** | **Date**| Optional: Get project travel expenses that have been added or changed after this date time (greater or equal). | [optional] 

### Return type

[**[ProjectTravelExpenseOutputModel]**](ProjectTravelExpenseOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectTravelExpensesGetProjectTravelExpensesForProject

> [ProjectTravelExpenseOutputModel] projectTravelExpensesGetProjectTravelExpensesForProject(projectGuid, opts)

Get all the project travel expenses for a project

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

let apiInstance = new SeveraPublicRestApiDocumentation.TravelsReadApi();
let projectGuid = "projectGuid_example"; // String | ID of the project.
let opts = {
  'isBillable': true, // Boolean | Optional: Filter the travel expenses. If true/false, only the billable/non-billable ones are returned. If null, all are returned. Default is null.
  'isBilled': true, // Boolean | Optional: Filter the travel expenses. If true/false, only the ones that are/are not invoiced are returned. If null, all are returned. Default is null.
  'invoiceableDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional: Filter the project fees. When given, only the ones that are invoiceable before or on the given date are returned. Default is null.
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'isBillablePeriodInFuture': true, // Boolean | Optional. Filter the project travel expenses. If true/false, only the ones that will be billable in the future are returned. If null, all are returned. Default is false.
  'expenseClass': new SeveraPublicRestApiDocumentation.ExpensesClass() // ExpensesClass | Optional: Class of the expense. Mileage, DailyAllowance or OtherTravelExpense
};
apiInstance.projectTravelExpensesGetProjectTravelExpensesForProject(projectGuid, opts, (error, data, response) => {
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
 **projectGuid** | **String**| ID of the project. | 
 **isBillable** | **Boolean**| Optional: Filter the travel expenses. If true/false, only the billable/non-billable ones are returned. If null, all are returned. Default is null. | [optional] 
 **isBilled** | **Boolean**| Optional: Filter the travel expenses. If true/false, only the ones that are/are not invoiced are returned. If null, all are returned. Default is null. | [optional] 
 **invoiceableDate** | **Date**| Optional: Filter the project fees. When given, only the ones that are invoiceable before or on the given date are returned. Default is null. | [optional] 
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **isBillablePeriodInFuture** | **Boolean**| Optional. Filter the project travel expenses. If true/false, only the ones that will be billable in the future are returned. If null, all are returned. Default is false. | [optional] 
 **expenseClass** | [**ExpensesClass**](.md)| Optional: Class of the expense. Mileage, DailyAllowance or OtherTravelExpense | [optional] 

### Return type

[**[ProjectTravelExpenseOutputModel]**](ProjectTravelExpenseOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectTravelExpensesGetProjectTravelExpensesForTravelReimbursement

> [ProjectTravelExpenseOutputModel] projectTravelExpensesGetProjectTravelExpensesForTravelReimbursement(travelReimbursementGuid, opts)

Get all the project travel expenses for a travel reimbursement

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

let apiInstance = new SeveraPublicRestApiDocumentation.TravelsReadApi();
let travelReimbursementGuid = "travelReimbursementGuid_example"; // String | Optional: ID of the travel reimbursement
let opts = {
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'expenseClass': new SeveraPublicRestApiDocumentation.ExpensesClass() // ExpensesClass | Optional: Class of the expense. Mileage, DailyAllowance or OtherTravelExpense
};
apiInstance.projectTravelExpensesGetProjectTravelExpensesForTravelReimbursement(travelReimbursementGuid, opts, (error, data, response) => {
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
 **travelReimbursementGuid** | **String**| Optional: ID of the travel reimbursement | 
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **expenseClass** | [**ExpensesClass**](.md)| Optional: Class of the expense. Mileage, DailyAllowance or OtherTravelExpense | [optional] 

### Return type

[**[ProjectTravelExpenseOutputModel]**](ProjectTravelExpenseOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectTravelExpensesGetProjectTravelExpensesForUser

> [ProjectTravelExpenseOutputModel] projectTravelExpensesGetProjectTravelExpensesForUser(userGuid, opts)

Get all the project travel expenses for a user

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

let apiInstance = new SeveraPublicRestApiDocumentation.TravelsReadApi();
let userGuid = "userGuid_example"; // String | ID of the user.
let opts = {
  'startDate': new Date("2013-10-20"), // Date | Optional: starting date from which to get the travel expenses. Default all.
  'endDate': new Date("2013-10-20"), // Date | Optional: starting date to which to get the travel expenses. Default all.
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'expenseClass': new SeveraPublicRestApiDocumentation.ExpensesClass(), // ExpensesClass | Optional: Class of the expense. Mileage, DailyAllowance or OtherTravelExpense
  'isReimbursed': true, // Boolean | Optional. Filter the project travel expenses. If true/false, only the ones that are reimbursed are returned. If null, all are returned. Default is null.
  'isTravelReimbursementRequired': true, // Boolean | Optional: Filter the project travel expenses by whether or not the reimbursement is required. Default all.
  'travelReimbursementGuid': "travelReimbursementGuid_example", // String | Optional: ID of the travel reimbursement
  'costCurrencyGuid': "costCurrencyGuid_example" // String | Optional: ID of the cost currency.
};
apiInstance.projectTravelExpensesGetProjectTravelExpensesForUser(userGuid, opts, (error, data, response) => {
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
 **startDate** | **Date**| Optional: starting date from which to get the travel expenses. Default all. | [optional] 
 **endDate** | **Date**| Optional: starting date to which to get the travel expenses. Default all. | [optional] 
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **expenseClass** | [**ExpensesClass**](.md)| Optional: Class of the expense. Mileage, DailyAllowance or OtherTravelExpense | [optional] 
 **isReimbursed** | **Boolean**| Optional. Filter the project travel expenses. If true/false, only the ones that are reimbursed are returned. If null, all are returned. Default is null. | [optional] 
 **isTravelReimbursementRequired** | **Boolean**| Optional: Filter the project travel expenses by whether or not the reimbursement is required. Default all. | [optional] 
 **travelReimbursementGuid** | **String**| Optional: ID of the travel reimbursement | [optional] 
 **costCurrencyGuid** | **String**| Optional: ID of the cost currency. | [optional] 

### Return type

[**[ProjectTravelExpenseOutputModel]**](ProjectTravelExpenseOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## travelReimbursementsGetTravelReimbursement

> TravelReimbursementOutputModel travelReimbursementsGetTravelReimbursement(guid)

Get travel reimbursement by ID

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

let apiInstance = new SeveraPublicRestApiDocumentation.TravelsReadApi();
let guid = "guid_example"; // String | ID of travel reimbursement
apiInstance.travelReimbursementsGetTravelReimbursement(guid, (error, data, response) => {
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
 **guid** | **String**| ID of travel reimbursement | 

### Return type

[**TravelReimbursementOutputModel**](TravelReimbursementOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## travelReimbursementsGetTravelReimbursements

> [TravelReimbursementOutputModel] travelReimbursementsGetTravelReimbursements(opts)

Get travel reimbursements.

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

let apiInstance = new SeveraPublicRestApiDocumentation.TravelsReadApi();
let opts = {
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56, // Number | Optional: How many rows to fetch.
  'changedSince': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional: Get travel reimbursements that have been added or changed after this date time (greater or equal).
  'travelReimbursementStatusGuids': ["null"] // [String] | Optional: List of travel reimbursement status ids.
};
apiInstance.travelReimbursementsGetTravelReimbursements(opts, (error, data, response) => {
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
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch. | [optional] 
 **changedSince** | **Date**| Optional: Get travel reimbursements that have been added or changed after this date time (greater or equal). | [optional] 
 **travelReimbursementStatusGuids** | [**[String]**](String.md)| Optional: List of travel reimbursement status ids. | [optional] 

### Return type

[**[TravelReimbursementOutputModel]**](TravelReimbursementOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

