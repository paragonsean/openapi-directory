# SeveraPublicRestApiDocumentation.TravelsWriteApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projectTravelExpensesPatchProjectTravelExpense**](TravelsWriteApi.md#projectTravelExpensesPatchProjectTravelExpense) | **PATCH** /v1/projecttravelexpenses/{guid} | Update (Patch) a project travel expense or a part of it.
[**projectTravelExpensesPostProjectTravelExpense**](TravelsWriteApi.md#projectTravelExpensesPostProjectTravelExpense) | **POST** /v1/projecttravelexpenses | Insert a project travel expense.
[**travelReimbursementsPatchTravelReimbursement**](TravelsWriteApi.md#travelReimbursementsPatchTravelReimbursement) | **PATCH** /v1/travelreimbursements/{guid} | Update (Patch) a travel reimbursement
[**travelReimbursementsPostTravelReimbursement**](TravelsWriteApi.md#travelReimbursementsPostTravelReimbursement) | **POST** /v1/travelreimbursements | Add a travel reimbursement



## projectTravelExpensesPatchProjectTravelExpense

> [ProjectTravelExpenseOutputModel] projectTravelExpensesPatchProjectTravelExpense(guid, opts)

Update (Patch) a project travel expense or a part of it.

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

let apiInstance = new SeveraPublicRestApiDocumentation.TravelsWriteApi();
let guid = "guid_example"; // String | ID of the project travel expense.
let opts = {
  'patchOperation': [new SeveraPublicRestApiDocumentation.PatchOperation()] // [PatchOperation] | JSON Patch document of ProjectTravelExpenseInputModel.
};
apiInstance.projectTravelExpensesPatchProjectTravelExpense(guid, opts, (error, data, response) => {
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
 **guid** | **String**| ID of the project travel expense. | 
 **patchOperation** | [**[PatchOperation]**](PatchOperation.md)| JSON Patch document of ProjectTravelExpenseInputModel. | [optional] 

### Return type

[**[ProjectTravelExpenseOutputModel]**](ProjectTravelExpenseOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectTravelExpensesPostProjectTravelExpense

> ProjectTravelExpenseOutputModel projectTravelExpensesPostProjectTravelExpense(opts)

Insert a project travel expense.

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

let apiInstance = new SeveraPublicRestApiDocumentation.TravelsWriteApi();
let opts = {
  'projectTravelExpenseInputModel': new SeveraPublicRestApiDocumentation.ProjectTravelExpenseInputModel() // ProjectTravelExpenseInputModel | ProjectTravelExpenseInputModel.
};
apiInstance.projectTravelExpensesPostProjectTravelExpense(opts, (error, data, response) => {
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
 **projectTravelExpenseInputModel** | [**ProjectTravelExpenseInputModel**](ProjectTravelExpenseInputModel.md)| ProjectTravelExpenseInputModel. | [optional] 

### Return type

[**ProjectTravelExpenseOutputModel**](ProjectTravelExpenseOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## travelReimbursementsPatchTravelReimbursement

> [TravelReimbursementOutputModel] travelReimbursementsPatchTravelReimbursement(guid, opts)

Update (Patch) a travel reimbursement

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

let apiInstance = new SeveraPublicRestApiDocumentation.TravelsWriteApi();
let guid = "guid_example"; // String | ID of the travel reimbursement
let opts = {
  'patchOperation': [new SeveraPublicRestApiDocumentation.PatchOperation()] // [PatchOperation] | JSON Patch document
};
apiInstance.travelReimbursementsPatchTravelReimbursement(guid, opts, (error, data, response) => {
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
 **guid** | **String**| ID of the travel reimbursement | 
 **patchOperation** | [**[PatchOperation]**](PatchOperation.md)| JSON Patch document | [optional] 

### Return type

[**[TravelReimbursementOutputModel]**](TravelReimbursementOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## travelReimbursementsPostTravelReimbursement

> TravelReimbursementOutputModel travelReimbursementsPostTravelReimbursement(opts)

Add a travel reimbursement

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

let apiInstance = new SeveraPublicRestApiDocumentation.TravelsWriteApi();
let opts = {
  'addAllUnreimbursedTravelExpenses': true, // Boolean | Optional: Add all of user's unreimbursed travel expenses to reimbursement. Default is true. If TravelExpenseReimbursementStartDate is given in organization settings, travel expenses are added from that date onwards. If value is false then expenses from includedProjectTravelExpenses list are added.
  'includedProjectTravelExpenses': ["null"], // [String] | Optional: A list of included projectTravelExpense GUIDs belonging to the user. If addAllUnreimbursedTravelExpenses is true then this list is ignored.
  'travelReimbursementInputModel': new SeveraPublicRestApiDocumentation.TravelReimbursementInputModel() // TravelReimbursementInputModel | TravelReimbursementModel
};
apiInstance.travelReimbursementsPostTravelReimbursement(opts, (error, data, response) => {
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
 **addAllUnreimbursedTravelExpenses** | **Boolean**| Optional: Add all of user&#39;s unreimbursed travel expenses to reimbursement. Default is true. If TravelExpenseReimbursementStartDate is given in organization settings, travel expenses are added from that date onwards. If value is false then expenses from includedProjectTravelExpenses list are added. | [optional] [default to true]
 **includedProjectTravelExpenses** | [**[String]**](String.md)| Optional: A list of included projectTravelExpense GUIDs belonging to the user. If addAllUnreimbursedTravelExpenses is true then this list is ignored. | [optional] 
 **travelReimbursementInputModel** | [**TravelReimbursementInputModel**](TravelReimbursementInputModel.md)| TravelReimbursementModel | [optional] 

### Return type

[**TravelReimbursementOutputModel**](TravelReimbursementOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

