# AdvicentFactFinderService.EducationGoalsApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

Method | HTTP request | Description
------------- | ------------- | -------------
[**educationGoalsDeleteByEducationgoalidId**](EducationGoalsApi.md#educationGoalsDeleteByEducationgoalidId) | **DELETE** /api/EducationGoals/{educationGoalId}/Expenses/{id} | 
[**educationGoalsDeleteById**](EducationGoalsApi.md#educationGoalsDeleteById) | **DELETE** /api/EducationGoals/{id} | 
[**educationGoalsGetById**](EducationGoalsApi.md#educationGoalsGetById) | **GET** /api/EducationGoals/{id} | 
[**educationGoalsGetEducationExpenseByEducationgoalidId**](EducationGoalsApi.md#educationGoalsGetEducationExpenseByEducationgoalidId) | **GET** /api/EducationGoals/{educationGoalId}/Expenses/{id} | 
[**educationGoalsGetEducationExpensesByEducationGoalIdByEducationgoalid**](EducationGoalsApi.md#educationGoalsGetEducationExpensesByEducationGoalIdByEducationgoalid) | **GET** /api/EducationGoals/{educationGoalId}/Expenses | 
[**educationGoalsGetEducationGoalsByFactFinderIdByFactfinderid**](EducationGoalsApi.md#educationGoalsGetEducationGoalsByFactFinderIdByFactfinderid) | **GET** /api/EducationGoals | 
[**educationGoalsPostByEducationgoalidModel**](EducationGoalsApi.md#educationGoalsPostByEducationgoalidModel) | **POST** /api/EducationGoals/{educationGoalId}/Expenses | 
[**educationGoalsPostByModel**](EducationGoalsApi.md#educationGoalsPostByModel) | **POST** /api/EducationGoals | 
[**educationGoalsPutByEducationgoalidIdModel**](EducationGoalsApi.md#educationGoalsPutByEducationgoalidIdModel) | **PUT** /api/EducationGoals/{educationGoalId}/Expenses/{id} | 
[**educationGoalsPutByIdModel**](EducationGoalsApi.md#educationGoalsPutByIdModel) | **PUT** /api/EducationGoals/{id} | 



## educationGoalsDeleteByEducationgoalidId

> educationGoalsDeleteByEducationgoalidId(educationGoalId, id)



Description: The operation removes an Education Goal Expense tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of an Education Goal Expense from a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.EducationGoalsApi();
let educationGoalId = 56; // Number | The Education Goal ID used to locate the Goal to delete the Expense under
let id = 56; // Number | The Education Goal Expense ID used to identify which Education Goal Expense to remove
apiInstance.educationGoalsDeleteByEducationgoalidId(educationGoalId, id, (error, data, response) => {
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
 **educationGoalId** | **Number**| The Education Goal ID used to locate the Goal to delete the Expense under | 
 **id** | **Number**| The Education Goal Expense ID used to identify which Education Goal Expense to remove | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## educationGoalsDeleteById

> educationGoalsDeleteById(id)



Description: The operation removes an Education Goal tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of an Education Goal from a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.EducationGoalsApi();
let id = 56; // Number | The Education Goal ID used to identify which Education Goal to remove
apiInstance.educationGoalsDeleteById(id, (error, data, response) => {
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
 **id** | **Number**| The Education Goal ID used to identify which Education Goal to remove | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## educationGoalsGetById

> EducationGoalWithIdModel educationGoalsGetById(id)



Description: This operation retrieves a single Education Goal for the specified Education Goal ID.&lt;br /&gt;                Purpose: Provides access to the Education Goal including description and projected cost.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.EducationGoalsApi();
let id = 56; // Number | The ID of the Education Goal used to retreive the Education Goal
apiInstance.educationGoalsGetById(id, (error, data, response) => {
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
 **id** | **Number**| The ID of the Education Goal used to retreive the Education Goal | 

### Return type

[**EducationGoalWithIdModel**](EducationGoalWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## educationGoalsGetEducationExpenseByEducationgoalidId

> EducationExpenseWithIdModel educationGoalsGetEducationExpenseByEducationgoalidId(educationGoalId, id)



Description: This operation retrieves a single Education Goal Expense for the specified Education Goal Expense ID.&lt;br /&gt;                Purpose: Provides access to the Education Goal Expense including description and annual cost.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.EducationGoalsApi();
let educationGoalId = 56; // Number | The ID of the Education Goal used to retrieve Education Goal Expenses
let id = 56; // Number | The ID of the Education Goal Expense used to retreive the Education Goal Expense
apiInstance.educationGoalsGetEducationExpenseByEducationgoalidId(educationGoalId, id, (error, data, response) => {
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
 **educationGoalId** | **Number**| The ID of the Education Goal used to retrieve Education Goal Expenses | 
 **id** | **Number**| The ID of the Education Goal Expense used to retreive the Education Goal Expense | 

### Return type

[**EducationExpenseWithIdModel**](EducationExpenseWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## educationGoalsGetEducationExpensesByEducationGoalIdByEducationgoalid

> EducationExpensesModel educationGoalsGetEducationExpensesByEducationGoalIdByEducationgoalid(educationGoalId)



Description: This operation retrieves all Education Goal Expenses for the specified Education Goal ID.&lt;br /&gt;                Purpose: Provides access to the Education Goal Expenses including description and annual cost.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.EducationGoalsApi();
let educationGoalId = 56; // Number | The ID of the Education Goal used to retrieve Education Goal Expenses
apiInstance.educationGoalsGetEducationExpensesByEducationGoalIdByEducationgoalid(educationGoalId, (error, data, response) => {
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
 **educationGoalId** | **Number**| The ID of the Education Goal used to retrieve Education Goal Expenses | 

### Return type

[**EducationExpensesModel**](EducationExpensesModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## educationGoalsGetEducationGoalsByFactFinderIdByFactfinderid

> EducationGoalsModel educationGoalsGetEducationGoalsByFactFinderIdByFactfinderid(factFinderId)



Description: This operation retrieves all Education Goals for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Education Goals including description and projected cost.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.EducationGoalsApi();
let factFinderId = 56; // Number | The ID of the Fact Finder used to retrieve Education Goals
apiInstance.educationGoalsGetEducationGoalsByFactFinderIdByFactfinderid(factFinderId, (error, data, response) => {
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
 **factFinderId** | **Number**| The ID of the Fact Finder used to retrieve Education Goals | 

### Return type

[**EducationGoalsModel**](EducationGoalsModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## educationGoalsPostByEducationgoalidModel

> EducationExpenseWithIdModel educationGoalsPostByEducationgoalidModel(educationGoalId, model)



Description: The operation creates an Education Goal Expense.&lt;br /&gt;                Purpose: Allows for creation of Education Goal Expenses on a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.EducationGoalsApi();
let educationGoalId = 56; // Number | The Education Goal ID used to locate the Goal to add the expense to
let model = new AdvicentFactFinderService.EducationExpenseModel(); // EducationExpenseModel | The Education Goal Expense to be added to the Fact Finder
apiInstance.educationGoalsPostByEducationgoalidModel(educationGoalId, model, (error, data, response) => {
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
 **educationGoalId** | **Number**| The Education Goal ID used to locate the Goal to add the expense to | 
 **model** | [**EducationExpenseModel**](EducationExpenseModel.md)| The Education Goal Expense to be added to the Fact Finder | 

### Return type

[**EducationExpenseWithIdModel**](EducationExpenseWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## educationGoalsPostByModel

> EducationGoalWithIdModel educationGoalsPostByModel(model)



Description: The operation creates an Education Goal.&lt;br /&gt;                Purpose: Allows for creation of Education Goals on a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.EducationGoalsApi();
let model = new AdvicentFactFinderService.EducationGoalModel(); // EducationGoalModel | The Education Goal to be added to the Fact Finder
apiInstance.educationGoalsPostByModel(model, (error, data, response) => {
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
 **model** | [**EducationGoalModel**](EducationGoalModel.md)| The Education Goal to be added to the Fact Finder | 

### Return type

[**EducationGoalWithIdModel**](EducationGoalWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## educationGoalsPutByEducationgoalidIdModel

> EducationExpenseWithIdModel educationGoalsPutByEducationgoalidIdModel(educationGoalId, id, model)



Description: The operation updates an Education Goal Expense.&lt;br /&gt;                Purpose: Allows for complete replacement of an Education Goal Expense on a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.EducationGoalsApi();
let educationGoalId = 56; // Number | The Education Goal ID used to locate the Goal to update the Expense under
let id = 56; // Number | The existing Education Goal Expense ID used to identify which Education Goal Expense to update
let model = new AdvicentFactFinderService.EducationExpenseModel(); // EducationExpenseModel | The Education Goal Expense to be added to the Fact Finder
apiInstance.educationGoalsPutByEducationgoalidIdModel(educationGoalId, id, model, (error, data, response) => {
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
 **educationGoalId** | **Number**| The Education Goal ID used to locate the Goal to update the Expense under | 
 **id** | **Number**| The existing Education Goal Expense ID used to identify which Education Goal Expense to update | 
 **model** | [**EducationExpenseModel**](EducationExpenseModel.md)| The Education Goal Expense to be added to the Fact Finder | 

### Return type

[**EducationExpenseWithIdModel**](EducationExpenseWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## educationGoalsPutByIdModel

> EducationGoalWithIdModel educationGoalsPutByIdModel(id, model)



Description: The operation creates an Education Goal Expense.&lt;br /&gt;                Purpose: Allows for creation of Education Goal Expenses on a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.EducationGoalsApi();
let id = 56; // Number | The Education Goal ID used to locate the Goal to add the Expense to
let model = new AdvicentFactFinderService.EducationGoalModel(); // EducationGoalModel | The Education Goal Expense to be added to the Fact Finder
apiInstance.educationGoalsPutByIdModel(id, model, (error, data, response) => {
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
 **id** | **Number**| The Education Goal ID used to locate the Goal to add the Expense to | 
 **model** | [**EducationGoalModel**](EducationGoalModel.md)| The Education Goal Expense to be added to the Fact Finder | 

### Return type

[**EducationGoalWithIdModel**](EducationGoalWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

