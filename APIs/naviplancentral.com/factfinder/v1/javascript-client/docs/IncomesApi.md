# AdvicentFactFinderService.IncomesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

Method | HTTP request | Description
------------- | ------------- | -------------
[**incomesDeleteById**](IncomesApi.md#incomesDeleteById) | **DELETE** /api/Incomes/{id} | 
[**incomesGetById**](IncomesApi.md#incomesGetById) | **GET** /api/Incomes/{id} | 
[**incomesGetIncomesByFactFinderIdByFactfinderid**](IncomesApi.md#incomesGetIncomesByFactFinderIdByFactfinderid) | **GET** /api/Incomes | 
[**incomesPostByModel**](IncomesApi.md#incomesPostByModel) | **POST** /api/Incomes | 
[**incomesPutByIdModel**](IncomesApi.md#incomesPutByIdModel) | **PUT** /api/Incomes/{id} | 



## incomesDeleteById

> incomesDeleteById(id)



Description: The operation removes an Income tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of an Income from a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.IncomesApi();
let id = 56; // Number | The Income ID used to identify which Income to remove
apiInstance.incomesDeleteById(id, (error, data, response) => {
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
 **id** | **Number**| The Income ID used to identify which Income to remove | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## incomesGetById

> IncomeWithIdModel incomesGetById(id)



Description: This operation retrieves a single Income for the specified Income ID.&lt;br /&gt;                Purpose: Provides access to the Income including annual amount and start date.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.IncomesApi();
let id = 56; // Number | The ID of the Income used to retreive the Income
apiInstance.incomesGetById(id, (error, data, response) => {
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
 **id** | **Number**| The ID of the Income used to retreive the Income | 

### Return type

[**IncomeWithIdModel**](IncomeWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## incomesGetIncomesByFactFinderIdByFactfinderid

> IncomesModel incomesGetIncomesByFactFinderIdByFactfinderid(factFinderId)



Description: This operation retrieves all Incomes for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Incomes including annual amount and start date.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.IncomesApi();
let factFinderId = 56; // Number | The ID of the Fact Finder used to retrieve Incomes
apiInstance.incomesGetIncomesByFactFinderIdByFactfinderid(factFinderId, (error, data, response) => {
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
 **factFinderId** | **Number**| The ID of the Fact Finder used to retrieve Incomes | 

### Return type

[**IncomesModel**](IncomesModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## incomesPostByModel

> IncomeWithIdModel incomesPostByModel(model)



Description: The operation creates an Income.&lt;br /&gt;                Purpose: Allows for creation of Incomes on a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.IncomesApi();
let model = new AdvicentFactFinderService.IncomeModel(); // IncomeModel | The Income to be added to the Fact Finder
apiInstance.incomesPostByModel(model, (error, data, response) => {
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
 **model** | [**IncomeModel**](IncomeModel.md)| The Income to be added to the Fact Finder | 

### Return type

[**IncomeWithIdModel**](IncomeWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## incomesPutByIdModel

> IncomeWithIdModel incomesPutByIdModel(id, model)



Description: The operation updates an Income.&lt;br /&gt;                Purpose: Allows for complete replacement of an Income on a Fact Finder.

### Example

```javascript
import AdvicentFactFinderService from 'advicent_fact_finder_service';

let apiInstance = new AdvicentFactFinderService.IncomesApi();
let id = 56; // Number | The existing Income ID used to identify which Income to update
let model = new AdvicentFactFinderService.IncomeModel(); // IncomeModel | The Income to be updated on a Fact Finder
apiInstance.incomesPutByIdModel(id, model, (error, data, response) => {
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
 **id** | **Number**| The existing Income ID used to identify which Income to update | 
 **model** | [**IncomeModel**](IncomeModel.md)| The Income to be updated on a Fact Finder | 

### Return type

[**IncomeWithIdModel**](IncomeWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

