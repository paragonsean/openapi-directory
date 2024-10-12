# AvazaApiDocumentation.ExpenseApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**expenseApproval**](ExpenseApi.md#expenseApproval) | **POST** /api/ExpenseApproval/Submit | Submit Expenses for Approval.
[**expenseAttachment**](ExpenseApi.md#expenseAttachment) | **POST** /api/Expense/Attachment | 
[**expenseDelete**](ExpenseApi.md#expenseDelete) | **DELETE** /api/Expense | Delete a Timesheet Entry
[**expenseGet**](ExpenseApi.md#expenseGet) | **GET** /api/Expense | Gets list of Expenses
[**expenseGetByID**](ExpenseApi.md#expenseGetByID) | **GET** /api/Expense/{id} | Gets an Expense Entry by Expense ID
[**expensePost**](ExpenseApi.md#expensePost) | **POST** /api/Expense | Create an Expense
[**expensePut**](ExpenseApi.md#expensePut) | **PUT** /api/Expense | Update an Expense



## expenseApproval

> Object expenseApproval(expenseIDs, opts)

Submit Expenses for Approval.

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.ExpenseApi();
let expenseIDs = [null]; // [Number] | A collection of ExpenseID's that should be submitted for approval. If not provided, submits all verified expenses for approval.
let opts = {
  'userID': 56, // Number | The user to submit the Expenses for. Defaults to current user. Only allowed to be different from the current user when the current user has rights to Impersonate other users.
  'sendNotifications': true // Boolean | Send email alerts to expense approvers. Defaults to true
};
apiInstance.expenseApproval(expenseIDs, opts, (error, data, response) => {
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
 **expenseIDs** | [**[Number]**](Number.md)| A collection of ExpenseID&#39;s that should be submitted for approval. If not provided, submits all verified expenses for approval. | 
 **userID** | **Number**| The user to submit the Expenses for. Defaults to current user. Only allowed to be different from the current user when the current user has rights to Impersonate other users. | [optional] 
 **sendNotifications** | **Boolean**| Send email alerts to expense approvers. Defaults to true | [optional] 

### Return type

**Object**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## expenseAttachment

> ExpenseAttachmentUploadResult expenseAttachment(expenseAttachmentRequest)



### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.ExpenseApi();
let expenseAttachmentRequest = new AvazaApiDocumentation.ExpenseAttachmentRequest(); // ExpenseAttachmentRequest | 
apiInstance.expenseAttachment(expenseAttachmentRequest, (error, data, response) => {
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
 **expenseAttachmentRequest** | [**ExpenseAttachmentRequest**](ExpenseAttachmentRequest.md)|  | 

### Return type

[**ExpenseAttachmentUploadResult**](ExpenseAttachmentUploadResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/form-data
- **Accept**: application/json, text/json, application/xml, text/xml


## expenseDelete

> ExpenseDeleteResultSet expenseDelete(expenseIDs)

Delete a Timesheet Entry

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.ExpenseApi();
let expenseIDs = [null]; // [Number] | A collection of ExpenseIDs to delete
apiInstance.expenseDelete(expenseIDs, (error, data, response) => {
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
 **expenseIDs** | [**[Number]**](Number.md)| A collection of ExpenseIDs to delete | 

### Return type

[**ExpenseDeleteResultSet**](ExpenseDeleteResultSet.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## expenseGet

> ExpenseList expenseGet(opts)

Gets list of Expenses

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.ExpenseApi();
let opts = {
  'updatedAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'expenseDateFrom': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'expenseDateTo': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'userEmail': "userEmail_example", // String | 
  'userID': 56, // Number | 
  'categoryName': "categoryName_example", // String | 
  'customerID': 56, // Number | 
  'projectID': 56, // Number | 
  'isChargeable': true, // Boolean | 
  'isInvoiced': true, // Boolean | 
  'expenseReimbursementIDFK': 789, // Number | 
  'expensePaymentMethodIDFK': 56, // Number | 
  'expenseApprovalStatusCode': "expenseApprovalStatusCode_example", // String | 
  'search': "search_example", // String | 
  'pageSize': 56, // Number | Number of items per page (max 1000)
  'pageNumber': 56, // Number | Page to display. Starts from 1.
  'sort': "sort_example" // String | 
};
apiInstance.expenseGet(opts, (error, data, response) => {
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
 **updatedAfter** | **Date**|  | [optional] 
 **expenseDateFrom** | **Date**|  | [optional] 
 **expenseDateTo** | **Date**|  | [optional] 
 **userEmail** | **String**|  | [optional] 
 **userID** | **Number**|  | [optional] 
 **categoryName** | **String**|  | [optional] 
 **customerID** | **Number**|  | [optional] 
 **projectID** | **Number**|  | [optional] 
 **isChargeable** | **Boolean**|  | [optional] 
 **isInvoiced** | **Boolean**|  | [optional] 
 **expenseReimbursementIDFK** | **Number**|  | [optional] 
 **expensePaymentMethodIDFK** | **Number**|  | [optional] 
 **expenseApprovalStatusCode** | **String**|  | [optional] 
 **search** | **String**|  | [optional] 
 **pageSize** | **Number**| Number of items per page (max 1000) | [optional] 
 **pageNumber** | **Number**| Page to display. Starts from 1. | [optional] 
 **sort** | **String**|  | [optional] 

### Return type

[**ExpenseList**](ExpenseList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## expenseGetByID

> ExpenseDetails expenseGetByID(id)

Gets an Expense Entry by Expense ID

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.ExpenseApi();
let id = 789; // Number | Expense ID number
apiInstance.expenseGetByID(id, (error, data, response) => {
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
 **id** | **Number**| Expense ID number | 

### Return type

[**ExpenseDetails**](ExpenseDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## expensePost

> ExpenseDetails expensePost(model)

Create an Expense

Create an Expense

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.ExpenseApi();
let model = new AvazaApiDocumentation.NewExpense(); // NewExpense | 
apiInstance.expensePost(model, (error, data, response) => {
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
 **model** | [**NewExpense**](NewExpense.md)|  | 

### Return type

[**ExpenseDetails**](ExpenseDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## expensePut

> ExpenseDetails expensePut(model)

Update an Expense

Update an Expense

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.ExpenseApi();
let model = new AvazaApiDocumentation.UpdateExpense(); // UpdateExpense | 
apiInstance.expensePut(model, (error, data, response) => {
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
 **model** | [**UpdateExpense**](UpdateExpense.md)|  | 

### Return type

[**ExpenseDetails**](ExpenseDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml

