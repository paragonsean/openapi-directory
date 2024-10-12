# AdvicentFactFinderService.ExpensesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

Method | HTTP request | Description
------------- | ------------- | -------------
[**expensesDeleteById**](ExpensesApi.md#expensesDeleteById) | **DELETE** /api/Expenses/{id} | 
[**expensesGetById**](ExpensesApi.md#expensesGetById) | **GET** /api/Expenses/{id} | 
[**expensesGetExpensesByFactFinderIdByFactfinderid**](ExpensesApi.md#expensesGetExpensesByFactFinderIdByFactfinderid) | **GET** /api/Expenses | 
[**expensesPostByModel**](ExpensesApi.md#expensesPostByModel) | **POST** /api/Expenses | 
[**expensesPutByIdModel**](ExpensesApi.md#expensesPutByIdModel) | **PUT** /api/Expenses/{id} | 



## expensesDeleteById

> expensesDeleteById(id)



Description: The operation removes an Expense tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of an Expense from a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.ExpensesApi();
let id = 56; // Number | The Expense ID used to identify which Expense to remove
apiInstance.expensesDeleteById(id, (error, data, response) => {
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
 **id** | **Number**| The Expense ID used to identify which Expense to remove | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## expensesGetById

> ExpenseWithIdModel expensesGetById(id)



Description: This operation retrieves a single Expense for the specified Expense ID.&lt;br /&gt;                Purpose: Provides access to the Expense including description and Expense type.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.ExpensesApi();
let id = 56; // Number | The ID of the Expense used to retreive the Expense
apiInstance.expensesGetById(id, (error, data, response) => {
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
 **id** | **Number**| The ID of the Expense used to retreive the Expense | 

### Return type

[**ExpenseWithIdModel**](ExpenseWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## expensesGetExpensesByFactFinderIdByFactfinderid

> ExpensesModel expensesGetExpensesByFactFinderIdByFactfinderid(factFinderId)



Description: This operation retrieves all Expenses for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Expenses including description and Expense type.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.ExpensesApi();
let factFinderId = 56; // Number | The ID of the Fact Finder used to retrieve Expenses
apiInstance.expensesGetExpensesByFactFinderIdByFactfinderid(factFinderId, (error, data, response) => {
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
 **factFinderId** | **Number**| The ID of the Fact Finder used to retrieve Expenses | 

### Return type

[**ExpensesModel**](ExpensesModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## expensesPostByModel

> ExpenseWithIdModel expensesPostByModel(model)



Description: The operation creates an Expense.&lt;br /&gt;                Purpose: Allows for creation of Expenses on a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.ExpensesApi();
let model = new AdvicentFactFinderService.ExpenseModel(); // ExpenseModel | The Expense to be added to the Fact Finder
apiInstance.expensesPostByModel(model, (error, data, response) => {
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
 **model** | [**ExpenseModel**](ExpenseModel.md)| The Expense to be added to the Fact Finder | 

### Return type

[**ExpenseWithIdModel**](ExpenseWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## expensesPutByIdModel

> ExpenseWithIdModel expensesPutByIdModel(id, model)



Description: The operation updates an Expense.&lt;br /&gt;                Purpose: Allows for complete replacement of an Expense on a Fact Finder. &lt;br /&gt;&lt;br /&gt;                Note: Expense type cannot be changed for expenses prepopulated from NaviPlan.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.ExpensesApi();
let id = 56; // Number | The existing Expense ID used to identify which Expense to update
let model = new AdvicentFactFinderService.ExpenseModel(); // ExpenseModel | The Expense to be updated on a Fact Finder
apiInstance.expensesPutByIdModel(id, model, (error, data, response) => {
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
 **id** | **Number**| The existing Expense ID used to identify which Expense to update | 
 **model** | [**ExpenseModel**](ExpenseModel.md)| The Expense to be updated on a Fact Finder | 

### Return type

[**ExpenseWithIdModel**](ExpenseWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

