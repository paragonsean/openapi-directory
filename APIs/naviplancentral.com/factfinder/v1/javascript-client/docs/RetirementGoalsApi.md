# AdvicentFactFinderService.RetirementGoalsApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retirementGoalsDeleteById**](RetirementGoalsApi.md#retirementGoalsDeleteById) | **DELETE** /api/RetirementGoals/{id} | 
[**retirementGoalsDeleteByRetirementgoalidId**](RetirementGoalsApi.md#retirementGoalsDeleteByRetirementgoalidId) | **DELETE** /api/RetirementGoals/{retirementGoalId}/Expenses/{id} | 
[**retirementGoalsGetById**](RetirementGoalsApi.md#retirementGoalsGetById) | **GET** /api/RetirementGoals/{id} | 
[**retirementGoalsGetRetirementExpenseByRetirementgoalidId**](RetirementGoalsApi.md#retirementGoalsGetRetirementExpenseByRetirementgoalidId) | **GET** /api/RetirementGoals/{retirementGoalId}/Expenses/{id} | 
[**retirementGoalsGetRetirementExpensesByRetirementGoalIdByRetirementgoalid**](RetirementGoalsApi.md#retirementGoalsGetRetirementExpensesByRetirementGoalIdByRetirementgoalid) | **GET** /api/RetirementGoals/{retirementGoalId}/Expenses | 
[**retirementGoalsGetRetirementGoalsByFactFinderIdByFactfinderid**](RetirementGoalsApi.md#retirementGoalsGetRetirementGoalsByFactFinderIdByFactfinderid) | **GET** /api/RetirementGoals | 
[**retirementGoalsPostByModel**](RetirementGoalsApi.md#retirementGoalsPostByModel) | **POST** /api/RetirementGoals | 
[**retirementGoalsPostByRetirementgoalidModel**](RetirementGoalsApi.md#retirementGoalsPostByRetirementgoalidModel) | **POST** /api/RetirementGoals/{retirementGoalId}/Expenses | 
[**retirementGoalsPutByIdModel**](RetirementGoalsApi.md#retirementGoalsPutByIdModel) | **PUT** /api/RetirementGoals/{id} | 
[**retirementGoalsPutByRetirementgoalidIdModel**](RetirementGoalsApi.md#retirementGoalsPutByRetirementgoalidIdModel) | **PUT** /api/RetirementGoals/{retirementGoalId}/Expenses/{id} | 



## retirementGoalsDeleteById

> retirementGoalsDeleteById(id)



Description: The operation removes a Retirement Goal tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of a Retirement Goal from a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.RetirementGoalsApi();
let id = 56; // Number | The Retirement Goal ID used to identify which Retirement Goal to remove
apiInstance.retirementGoalsDeleteById(id, (error, data, response) => {
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
 **id** | **Number**| The Retirement Goal ID used to identify which Retirement Goal to remove | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## retirementGoalsDeleteByRetirementgoalidId

> retirementGoalsDeleteByRetirementgoalidId(retirementGoalId, id)



Description: The operation removes a Retirement Goal Expense tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of a Retirement Goal Expense from a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.RetirementGoalsApi();
let retirementGoalId = 56; // Number | The Retirement Goal ID used to locate the Goal to delete the Retirement Goal Expense under
let id = 56; // Number | The Retirement Goal Expense ID used to identify which Retirement Goal Expense to remove
apiInstance.retirementGoalsDeleteByRetirementgoalidId(retirementGoalId, id, (error, data, response) => {
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
 **retirementGoalId** | **Number**| The Retirement Goal ID used to locate the Goal to delete the Retirement Goal Expense under | 
 **id** | **Number**| The Retirement Goal Expense ID used to identify which Retirement Goal Expense to remove | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## retirementGoalsGetById

> RetirementGoalWithIdModel retirementGoalsGetById(id)



Description: This operation retrieves a single Retirement Goal for the specified Retirement Goal ID.&lt;br /&gt;                Purpose: Provides access to the Retirement Goal including retirement date.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.RetirementGoalsApi();
let id = 56; // Number | The ID of the Retirement Goal used to retreive the Retirement Goal
apiInstance.retirementGoalsGetById(id, (error, data, response) => {
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
 **id** | **Number**| The ID of the Retirement Goal used to retreive the Retirement Goal | 

### Return type

[**RetirementGoalWithIdModel**](RetirementGoalWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## retirementGoalsGetRetirementExpenseByRetirementgoalidId

> RetirementExpenseWithIdModel retirementGoalsGetRetirementExpenseByRetirementgoalidId(retirementGoalId, id)



Description: This operation retrieves a single Retirement Goal Expense for the specified Retirement Goal Expense ID.&lt;br /&gt;                Purpose: Provides access to the Retirement Goal Expense including description and amount.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.RetirementGoalsApi();
let retirementGoalId = 56; // Number | The ID of the Retirement Goal used to retrieve the Retirement Goal Expense
let id = 56; // Number | The ID of the Retirement Goal Expense used to retreive the Retirement Goal Expense
apiInstance.retirementGoalsGetRetirementExpenseByRetirementgoalidId(retirementGoalId, id, (error, data, response) => {
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
 **retirementGoalId** | **Number**| The ID of the Retirement Goal used to retrieve the Retirement Goal Expense | 
 **id** | **Number**| The ID of the Retirement Goal Expense used to retreive the Retirement Goal Expense | 

### Return type

[**RetirementExpenseWithIdModel**](RetirementExpenseWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## retirementGoalsGetRetirementExpensesByRetirementGoalIdByRetirementgoalid

> RetirementExpensesModel retirementGoalsGetRetirementExpensesByRetirementGoalIdByRetirementgoalid(retirementGoalId)



Description: This operation retrieves all Retirement Goal Expenses for the specified Retirement Goal ID.&lt;br /&gt;                Purpose: Provides access to the Retirement Goal Expenses including description and amount.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.RetirementGoalsApi();
let retirementGoalId = 56; // Number | The ID of the Retirement Goal used to retrieve Retirement Goal Expenses
apiInstance.retirementGoalsGetRetirementExpensesByRetirementGoalIdByRetirementgoalid(retirementGoalId, (error, data, response) => {
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
 **retirementGoalId** | **Number**| The ID of the Retirement Goal used to retrieve Retirement Goal Expenses | 

### Return type

[**RetirementExpensesModel**](RetirementExpensesModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## retirementGoalsGetRetirementGoalsByFactFinderIdByFactfinderid

> RetirementGoalsModel retirementGoalsGetRetirementGoalsByFactFinderIdByFactfinderid(factFinderId)



Description: This operation retrieves all Retirement Goals for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Retirement Goals including retirement date.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.RetirementGoalsApi();
let factFinderId = 56; // Number | The ID of the Fact Finder used to retrieve Retirement Goals
apiInstance.retirementGoalsGetRetirementGoalsByFactFinderIdByFactfinderid(factFinderId, (error, data, response) => {
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
 **factFinderId** | **Number**| The ID of the Fact Finder used to retrieve Retirement Goals | 

### Return type

[**RetirementGoalsModel**](RetirementGoalsModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## retirementGoalsPostByModel

> RetirementGoalWithIdModel retirementGoalsPostByModel(model)



Description: The operation creates a Retirement Goal.&lt;br /&gt;                Purpose: Allows for creation of Retirement Goals on a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.RetirementGoalsApi();
let model = new AdvicentFactFinderService.RetirementGoalModel(); // RetirementGoalModel | The Retirement Goal to be added to the Fact Finder
apiInstance.retirementGoalsPostByModel(model, (error, data, response) => {
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
 **model** | [**RetirementGoalModel**](RetirementGoalModel.md)| The Retirement Goal to be added to the Fact Finder | 

### Return type

[**RetirementGoalWithIdModel**](RetirementGoalWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## retirementGoalsPostByRetirementgoalidModel

> RetirementExpenseWithIdModel retirementGoalsPostByRetirementgoalidModel(retirementGoalId, model)



Description: The operation creates a Retirement Goal Expense.&lt;br /&gt;                Purpose: Allows for creation of Retirement Goal Expenses on a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.RetirementGoalsApi();
let retirementGoalId = 56; // Number | The ID of the Retirement Goal to add the Retirement Goal Expense to
let model = new AdvicentFactFinderService.RetirementExpenseModel(); // RetirementExpenseModel | The Retirement Goal Expense to be added to the Fact Finder
apiInstance.retirementGoalsPostByRetirementgoalidModel(retirementGoalId, model, (error, data, response) => {
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
 **retirementGoalId** | **Number**| The ID of the Retirement Goal to add the Retirement Goal Expense to | 
 **model** | [**RetirementExpenseModel**](RetirementExpenseModel.md)| The Retirement Goal Expense to be added to the Fact Finder | 

### Return type

[**RetirementExpenseWithIdModel**](RetirementExpenseWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## retirementGoalsPutByIdModel

> RetirementGoalWithIdModel retirementGoalsPutByIdModel(id, model)



Description: The operation updates a Retirement Goal.&lt;br /&gt;                Purpose: Allows for complete replacement of a Retirement Goal on a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.RetirementGoalsApi();
let id = 56; // Number | The existing Retirement Goal ID used to identify which Retirement Goal to update
let model = new AdvicentFactFinderService.RetirementGoalModel(); // RetirementGoalModel | The Retirement Goal to be updated on a Fact Finder
apiInstance.retirementGoalsPutByIdModel(id, model, (error, data, response) => {
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
 **id** | **Number**| The existing Retirement Goal ID used to identify which Retirement Goal to update | 
 **model** | [**RetirementGoalModel**](RetirementGoalModel.md)| The Retirement Goal to be updated on a Fact Finder | 

### Return type

[**RetirementGoalWithIdModel**](RetirementGoalWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## retirementGoalsPutByRetirementgoalidIdModel

> RetirementExpenseWithIdModel retirementGoalsPutByRetirementgoalidIdModel(retirementGoalId, id, model)



Description: The operation updates a Retirement Goal Expense.&lt;br /&gt;                Purpose: Allows for complete replacement of a Retirement Goal Expense on a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.RetirementGoalsApi();
let retirementGoalId = 56; // Number | The Retirement Goal ID used to locate the Goal to update the Retirement Goal Expense under
let id = 56; // Number | The existing Retirement Goal Expense ID used to identify which Retirement Goal Expense to update
let model = new AdvicentFactFinderService.RetirementExpenseModel(); // RetirementExpenseModel | The Retirement Goal Expense to be updated on a Fact Finder
apiInstance.retirementGoalsPutByRetirementgoalidIdModel(retirementGoalId, id, model, (error, data, response) => {
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
 **retirementGoalId** | **Number**| The Retirement Goal ID used to locate the Goal to update the Retirement Goal Expense under | 
 **id** | **Number**| The existing Retirement Goal Expense ID used to identify which Retirement Goal Expense to update | 
 **model** | [**RetirementExpenseModel**](RetirementExpenseModel.md)| The Retirement Goal Expense to be updated on a Fact Finder | 

### Return type

[**RetirementExpenseWithIdModel**](RetirementExpenseWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

